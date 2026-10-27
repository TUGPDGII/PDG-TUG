#!/usr/bin/env python3
"""
Prueba del algoritmo de segmentacion TUG del PDG anterior sobre los datos actuales.
Mantiene la logica y parametros originales del notebook predecesor, agregando
unicamente el adaptador de lectura JSON y validaciones de indices para evitar
errores de ejecucion.
"""

import argparse
import csv
import datetime
import json
import os
import numpy as np
from scipy.signal import butter, filtfilt, find_peaks

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_DATA_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), "Datos Crudos")
DEFAULT_PERSONAS_CSV = os.path.join(SCRIPT_DIR, "personas.csv")
DEFAULT_OUTPUT_CSV = os.path.join(SCRIPT_DIR, "segmentacion_fases_tug.csv")

MAPA_SENSORES = [
    ("spine",       "espina_base"),
    ("base",        "espina_base"),
    ("right-ankle", "derecha"),
    ("left-ankle",  "izquierda"),
    ("right-hand",  "mano_derecha"),
    ("left-hand",   "mano_izquierda"),
]

ESCALA_ACC = 4096.0
ESCALA_GYRO = 1000.0


def _clave_sensor(device_id):
    dev = device_id.lower()
    for subcadena, clave in MAPA_SENSORES:
        if subcadena in dev:
            return clave
    return None


def cargar_datos_json(ruta_archivo):
    """Carga datos desde un archivo JSON."""
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as file:
            raw = json.load(file)
            if isinstance(raw, dict) and "data" in raw and isinstance(raw["data"], dict):
                return raw["data"]
            return raw
    except FileNotFoundError:
        print(f"Error: No se encontro el archivo '{ruta_archivo}'")
        return None
    except json.JSONDecodeError:
        print(f"Error: El archivo '{ruta_archivo}' no contiene un JSON valido")
        return None


def adaptar_esquema_json(json_data, fs_destino=50.0):
    """
    Convierte un JSON del formato actual (imuData) al diccionario 'pruebas'
    que espera el codigo del PDG anterior, remuestreando a 50 Hz.
    """
    if not json_data or "imuData" not in json_data:
        return json_data

    ts_inicio = json_data.get("timestamp", 0)
    timestamp_clave = (
        datetime.datetime.fromtimestamp(ts_inicio / 1000, datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
        if ts_inicio and ts_inicio > 1e12 else "muestra_0"
    )

    grupos = {}
    for reg in json_data["imuData"]:
        clave = _clave_sensor(reg.get("deviceId", ""))
        if clave is not None:
            grupos.setdefault(clave, []).append(reg)

    estructurado = {}
    for clave, registros in grupos.items():
        registros = sorted(registros, key=lambda r: r.get("timestamp", 0))
        if len(registros) < 2:
            continue

        primer_ts = registros[0].get("timestamp", 0)
        factor = 1e6 if primer_ts > 1e15 else 1.0
        t_cero = primer_ts / factor

        ts = np.array([r.get("timestamp", 0) / factor for r in registros], dtype=float)
        t_orig = (ts - t_cero) / 1000.0

        def canal(grupo, eje):
            return np.array([r.get(grupo, {}).get(eje, 0.0) for r in registros], dtype=float)

        duracion = t_orig[-1] - t_orig[0]
        if duracion <= 0:
            continue
        n = int(np.floor(duracion * fs_destino)) + 1
        t_dest = np.arange(n) / fs_destino

        acc_x = np.interp(t_dest, t_orig, canal("accelerometer", "x")) * ESCALA_ACC
        acc_y = np.interp(t_dest, t_orig, canal("accelerometer", "y")) * ESCALA_ACC
        acc_z = np.interp(t_dest, t_orig, canal("accelerometer", "z")) * ESCALA_ACC
        gyr_x = np.interp(t_dest, t_orig, canal("gyroscope", "x")) * ESCALA_GYRO
        gyr_y = np.interp(t_dest, t_orig, canal("gyroscope", "y")) * ESCALA_GYRO
        gyr_z = np.interp(t_dest, t_orig, canal("gyroscope", "z")) * ESCALA_GYRO

        estructurado[clave] = [
            {
                "t": float(t_dest[i] * 1000.0),
                "x": int(acc_x[i]), "y": int(acc_y[i]), "z": int(acc_z[i]),
                "a": int(gyr_x[i]), "b": int(gyr_y[i]), "g": int(gyr_z[i]),
                "millis": int(t_cero + t_dest[i] * 1000.0),
            }
            for i in range(n)
        ]

    return {
        "pruebas": {timestamp_clave: estructurado},
        "meta": {
            "testType": json_data.get("testType"),
            "hasWarning": json_data.get("hasWarning", False),
            "warningReason": json_data.get("warningReason"),
            "pausedDurationMs": json_data.get("pausedDurationMs", 0),
        },
    }


def cargar_prueba_adaptada(nombre_o_ruta, carpeta_base=None, fs_destino=50.0):
    ruta = nombre_o_ruta
    if not os.path.isabs(ruta) and carpeta_base:
        ruta = os.path.join(carpeta_base, ruta)

    crudo = cargar_datos_json(ruta)
    if not crudo:
        raise ValueError(f"Archivo vacio o JSON no encontrado: {ruta}")

    adaptado = adaptar_esquema_json(crudo, fs_destino=fs_destino)
    if not adaptado or "pruebas" not in adaptado:
        raise ValueError(f"Formato no reconocido: {ruta}")
    return adaptado["pruebas"]


# ------------------------------------------------------------------------------
# Funciones originales del algoritmo de segmentacion (PDG Predecesor)
# ------------------------------------------------------------------------------

def filter_signal(signal, cutoff_hz=3, fs=50.0, order=20):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff_hz / nyquist
    b, a = butter(order, normal_cutoff, btype="low", analog=False)
    filtered = filtfilt(b, a, signal)
    return filtered


def energy_spectrum(signal, fs, window_size_samples, step_size_samples, apply_window=True):
    energies = []
    times = []
    num_samples = len(signal)

    for start in range(0, num_samples - window_size_samples + 1, step_size_samples):
        end = start + window_size_samples
        window = signal[start:end]

        if apply_window:
            window = window * np.hanning(window_size_samples)

        energy = np.sum(window ** 2)
        energies.append(energy)

        t_center = (start + end) / 2 / fs
        times.append(t_center)

    energies = np.array(energies)
    times = np.array(times)

    if len(energies) > 0 and np.max(np.abs(energies)) > 0:
        energies = energies / np.max(np.abs(energies))

    return times, energies


def binary_threshold(signal: np.ndarray, threshold: float = 0.2) -> np.ndarray:
    return (signal >= threshold).astype(int)


def promediomovil(senal, ventana=50, fs=50):
    senal = np.array(senal, dtype=float)
    kernel = np.ones(ventana) / ventana
    prom = np.convolve(senal, kernel, mode="valid")

    if len(prom) > 0 and np.max(prom) != 0:
        prom = prom / np.max(prom)

    t = (np.arange(len(prom)) + ventana - 1) / fs
    return t, prom


def detectar_fases_tug(tiempo, senal_binaria, duracion_minima=0.5):
    """
    Detecta las fases de levantamiento y sentado en la prueba TUG
    segun el criterio original: primera fase valida = levantamiento,
    ultima fase valida = sentado.
    """
    if len(senal_binaria) == 0:
        return {"levantamiento": None, "sentado": None, "todas_las_fases": []}

    transiciones = np.diff(senal_binaria.astype(int))
    indices_subida = np.where(transiciones == 1)[0] + 1
    indices_bajada = np.where(transiciones == -1)[0] + 1

    if senal_binaria[0] == 1:
        indices_subida = np.concatenate([[0], indices_subida])

    if senal_binaria[-1] == 1:
        indices_bajada = np.concatenate([indices_bajada, [len(senal_binaria) - 1]])

    fases_movimiento = []
    min_indices = min(len(indices_subida), len(indices_bajada))

    for i in range(min_indices):
        inicio_mov = indices_subida[i]
        fin_mov = indices_bajada[i]

        if inicio_mov < fin_mov:
            t_inicio = float(tiempo[inicio_mov])
            t_fin = float(tiempo[fin_mov])
            duracion = t_fin - t_inicio

            if duracion >= duracion_minima:
                fases_movimiento.append({
                    "inicio_tiempo": t_inicio,
                    "fin_tiempo": t_fin,
                    "duracion": duracion,
                    "inicio_indice": int(inicio_mov),
                    "fin_indice": int(fin_mov),
                })

    fases_clasificadas = {
        "levantamiento": None,
        "sentado": None,
        "todas_las_fases": fases_movimiento,
    }

    if len(fases_movimiento) >= 1:
        fases_clasificadas["levantamiento"] = fases_movimiento[0]

    if len(fases_movimiento) >= 2:
        fases_clasificadas["sentado"] = fases_movimiento[-1]

    return fases_clasificadas


def detectar_giros_original(t_movil, binary):
    """
    Extrae los intervalos de giro a partir de los cambios de la senal binaria
    tal como en la seccion 'CORTES EN EL TIEMPO PARA LA FASE DE GIRO'.
    """
    if len(binary) == 0:
        return []

    cambios = np.diff(binary)
    inicios = np.where(cambios == 1)[0]
    fines = np.where(cambios == -1)[0]

    # Si empieza activo en 1, agregamos el inicio en 0 para no desfasar los pares
    if binary[0] == 1:
        inicios = np.insert(inicios, 0, 0)

    if len(fines) < len(inicios):
        fines = np.append(fines, len(binary) - 1)

    intervalos_giro = []
    for i, inicio in enumerate(inicios):
        fin = fines[i] if i < len(fines) else None
        if fin is None or fin <= inicio:
            continue
        intervalos_giro.append({
            "inicio": float(t_movil[inicio]),
            "fin": float(t_movil[fin]),
            "duracion": float(t_movil[fin] - t_movil[inicio]),
        })

    return intervalos_giro


def detectar_pasos_intervalo(time, asignal_filtered, fs, t_inicio, t_fin):
    """
    Detecta subfases STANCE (picos) y SWING (valles) en un intervalo de tiempo
    tal como en la celda 'JOANDGOAG'.
    """
    mask = (time >= t_inicio) & (time <= t_fin)
    t_seg = time[mask]
    sig_seg = asignal_filtered[mask]

    if len(sig_seg) < 10 or np.max(np.abs(sig_seg)) == 0:
        return [], [], [], [], []

    min_stride_s = 0.4
    distance = int(min_stride_s * fs)
    prominence = 0.25 * np.max(np.abs(sig_seg))

    peaks, _ = find_peaks(sig_seg, prominence=prominence, distance=distance)
    valleys, _ = find_peaks(-sig_seg, prominence=prominence, distance=distance)

    eventos = np.concatenate([
        np.stack([t_seg[peaks], np.repeat("STANCE_START", len(peaks))], axis=1),
        np.stack([t_seg[valleys], np.repeat("SWING_START", len(valleys))], axis=1),
    ])

    if len(eventos) == 0:
        return [], t_seg, sig_seg, peaks, valleys

    eventos = eventos[np.argsort(eventos[:, 0].astype(float))]

    fases_det = []
    for i in range(len(eventos) - 1):
        fase = eventos[i][1]
        t_i = float(eventos[i][0])
        t_f = float(eventos[i + 1][0])
        dur = t_f - t_i

        if fase == "STANCE_START":
            fases_det.append({"fase": "STANCE", "inicio": t_i, "fin": t_f, "duracion": dur})
        else:
            fases_det.append({"fase": "SWING", "inicio": t_i, "fin": t_f, "duracion": dur})

    return fases_det, t_seg, sig_seg, peaks, valleys


def ejecutar_segmentacion_archivo(ruta_archivo, fs=50):
    """
    Ejecuta los tres bloques del algoritmo predecesor sobre un archivo JSON:
    1. Levantamiento y sentado (espina_base, canal 'b')
    2. Cortes de giro (espina_base, canal 'a')
    3. Caminata de ida y vuelta + STANCE/SWING en tobillos (canal 'x')
    """
    patientdata = cargar_prueba_adaptada(ruta_archivo, fs_destino=fs)
    claves = list(patientdata.keys())
    indice_muestra = 0
    clave_muestra = claves[indice_muestra]
    muestra = patientdata[clave_muestra]

    # 1. Levantamiento y sentado (espina_base, canal 'b')
    sample_espina = muestra["espina_base"]
    sig_b = np.array([d["b"] for d in sample_espina], dtype=float)
    if np.max(np.abs(sig_b)) > 0:
        sig_b = sig_b / np.max(np.abs(sig_b))
    sig_b_filt = filter_signal(sig_b, fs=fs)
    time_espina = np.array([d["t"] / 1000.0 for d in sample_espina], dtype=float)

    _, energies_b = energy_spectrum(sig_b_filt, fs=fs, window_size_samples=50, step_size_samples=1, apply_window=True)
    t_movil_b, pmovil_b = promediomovil(energies_b, ventana=50, fs=fs)
    binary_b = binary_threshold(pmovil_b, threshold=0.2)
    fases_detectadas = detectar_fases_tug(t_movil_b, binary_b, duracion_minima=0.5)

    # 2. Deteccion de giros (espina_base, canal 'a')
    sig_a = np.array([d["a"] for d in sample_espina], dtype=float)
    if np.max(np.abs(sig_a)) > 0:
        sig_a = sig_a / np.max(np.abs(sig_a))
    sig_a_filt = filter_signal(sig_a, fs=fs)

    _, energies_a = energy_spectrum(sig_a_filt, fs=fs, window_size_samples=50, step_size_samples=1, apply_window=True)
    t_movil_a, pmovil_a = promediomovil(energies_a, ventana=50, fs=fs)
    binary_a = binary_threshold(pmovil_a, threshold=0.2)
    intervalos_giro = detectar_giros_original(t_movil_a, binary_a)

    # 3. Integracion de caminatas y deteccion de pasos (bloque JOANDGOAG)
    caminatas = None
    pasos_tobillos = {}

    if fases_detectadas["levantamiento"] is not None and len(intervalos_giro) >= 2:
        t_lev_fin = fases_detectadas["levantamiento"]["fin_tiempo"]
        t_giro1_ini = intervalos_giro[0]["inicio"]
        t_giro1_fin = intervalos_giro[0]["fin"]
        t_giro2_ini = intervalos_giro[1]["inicio"]
        t_giro2_fin = intervalos_giro[1]["fin"]

        t_inicio_ida = t_lev_fin
        t_fin_ida = t_giro1_ini
        t_inicio_vuelta = t_giro1_fin
        t_fin_vuelta = t_giro2_ini

        caminatas = {
            "ida": {"inicio": t_inicio_ida, "fin": t_fin_ida, "duracion": t_fin_ida - t_inicio_ida},
            "giro_1": intervalos_giro[0],
            "vuelta": {"inicio": t_inicio_vuelta, "fin": t_fin_vuelta, "duracion": t_fin_vuelta - t_inicio_vuelta},
            "giro_2": intervalos_giro[1],
        }

        for lateral in ["izquierda", "derecha"]:
            sample_tob = muestra[lateral]
            sig_x = np.array([d["x"] for d in sample_tob], dtype=float)
            time_tob = np.array([d["t"] / 1000.0 for d in sample_tob], dtype=float)
            if np.max(np.abs(sig_x)) > 0:
                sig_x = sig_x / np.max(np.abs(sig_x))
            sig_x_filt = filter_signal(sig_x, fs=fs)

            fases_ida, _, _, _, _ = detectar_pasos_intervalo(
                time_tob, sig_x_filt, fs, t_inicio_ida, t_fin_ida
            )
            fases_vuelta, _, _, _, _ = detectar_pasos_intervalo(
                time_tob, sig_x_filt, fs, t_inicio_vuelta, t_fin_vuelta
            )

            stance_ida = [x["duracion"] for x in fases_ida if x["fase"] == "STANCE"]
            swing_ida = [x["duracion"] for x in fases_ida if x["fase"] == "SWING"]
            stance_vuelta = [x["duracion"] for x in fases_vuelta if x["fase"] == "STANCE"]
            swing_vuelta = [x["duracion"] for x in fases_vuelta if x["fase"] == "SWING"]

            pasos_tobillos[lateral] = {
                "ida": fases_ida,
                "vuelta": fases_vuelta,
                "stance_mean_ida": float(np.mean(stance_ida)) if stance_ida else 0.0,
                "swing_mean_ida": float(np.mean(swing_ida)) if swing_ida else 0.0,
                "stance_mean_vuelta": float(np.mean(stance_vuelta)) if stance_vuelta else 0.0,
                "swing_mean_vuelta": float(np.mean(swing_vuelta)) if swing_vuelta else 0.0,
            }

    return {
        "archivo": os.path.basename(ruta_archivo),
        "clave_muestra": clave_muestra,
        "duracion_grabacion_s": round(float(time_espina[-1]), 2),
        "fases_tronco": fases_detectadas,
        "intervalos_giro": intervalos_giro,
        "caminatas": caminatas,
        "pasos_tobillos": pasos_tobillos,
    }


def imprimir_resultado_archivo(res):
    print("-" * 70)
    print(f"Archivo: {res['archivo']} (duracion total: {res['duracion_grabacion_s']} s)")
    print("-" * 70)

    fases = res["fases_tronco"]
    print(f"Fases de tronco detectadas (canal b): {len(fases['todas_las_fases'])}")
    if fases["levantamiento"]:
        lev = fases["levantamiento"]
        print(f"  Levantamiento : {lev['inicio_tiempo']:.2f} s -> {lev['fin_tiempo']:.2f} s (duracion: {lev['duracion']:.2f} s)")
    else:
        print("  Levantamiento : No detectado")

    if fases["sentado"]:
        sent = fases["sentado"]
        print(f"  Sentado       : {sent['inicio_tiempo']:.2f} s -> {sent['fin_tiempo']:.2f} s (duracion: {sent['duracion']:.2f} s)")
    else:
        print("  Sentado       : No detectado")

    giros = res["intervalos_giro"]
    print(f"\nIntervalos de giro detectados (canal a): {len(giros)}")
    for i, g in enumerate(giros):
        print(f"  Giro {i + 1}: inicio = {g['inicio']:.2f} s, fin = {g['fin']:.2f} s, duracion = {g['duracion']:.2f} s")

    if res["caminatas"]:
        cam = res["caminatas"]
        print("\nIntervalos de caminata (bloque JOANDGOAG):")
        print(f"  Caminata ida    : {cam['ida']['inicio']:.2f} s -> {cam['ida']['fin']:.2f} s (duracion: {cam['ida']['duracion']:.2f} s)")
        print(f"  Caminata vuelta : {cam['vuelta']['inicio']:.2f} s -> {cam['vuelta']['fin']:.2f} s (duracion: {cam['vuelta']['duracion']:.2f} s)")

        for lateral in ["izquierda", "derecha"]:
            p = res["pasos_tobillos"][lateral]
            print(f"\n  Tobillo {lateral}:")
            print(f"    Ida    ({len(p['ida'])} subfases) -> promedio STANCE = {p['stance_mean_ida']:.2f} s, SWING = {p['swing_mean_ida']:.2f} s")
            print(f"    Vuelta ({len(p['vuelta'])} subfases) -> promedio STANCE = {p['stance_mean_vuelta']:.2f} s, SWING = {p['swing_mean_vuelta']:.2f} s")
    else:
        print("\nNo se pudieron armar las caminatas (se requiere levantamiento y al menos 2 giros).")
    print("-" * 70)


def procesar_lote(carpeta_datos, ruta_personas_csv, ruta_salida_csv):
    aceptados = []
    with open(ruta_personas_csv, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("estado_metodologico") == "ACEPTADO":
                aceptados.append(row)

    filas_csv = []
    completos = 0

    for meta in aceptados:
        ruta = os.path.join(carpeta_datos, meta["archivo"])
        if not os.path.exists(ruta):
            continue

        res = ejecutar_segmentacion_archivo(ruta)
        lev = res["fases_tronco"]["levantamiento"]
        sent = res["fases_tronco"]["sentado"]
        giros = res["intervalos_giro"]
        cam = res["caminatas"]
        pasos = res["pasos_tobillos"]

        tiene_5_fases = cam is not None and sent is not None
        if tiene_5_fases:
            completos += 1

        filas_csv.append({
            "archivo": meta["archivo"],
            "codigo": meta["codigo"],
            "persona_id": meta["persona_id"],
            "tipo": meta["tipo"],
            "duracion_grabacion_s": res["duracion_grabacion_s"],
            "num_fases_tronco": len(res["fases_tronco"]["todas_las_fases"]),
            "num_giros_detectados": len(giros),
            "lev_inicio_s": round(lev["inicio_tiempo"], 2) if lev else None,
            "lev_fin_s": round(lev["fin_tiempo"], 2) if lev else None,
            "lev_dur_s": round(lev["duracion"], 2) if lev else None,
            "ida_inicio_s": round(cam["ida"]["inicio"], 2) if cam else None,
            "ida_fin_s": round(cam["ida"]["fin"], 2) if cam else None,
            "ida_dur_s": round(cam["ida"]["duracion"], 2) if cam else None,
            "giro1_inicio_s": round(giros[0]["inicio"], 2) if len(giros) >= 1 else None,
            "giro1_fin_s": round(giros[0]["fin"], 2) if len(giros) >= 1 else None,
            "giro1_dur_s": round(giros[0]["duracion"], 2) if len(giros) >= 1 else None,
            "vuelta_inicio_s": round(cam["vuelta"]["inicio"], 2) if cam else None,
            "vuelta_fin_s": round(cam["vuelta"]["fin"], 2) if cam else None,
            "vuelta_dur_s": round(cam["vuelta"]["duracion"], 2) if cam else None,
            "giro2_inicio_s": round(giros[1]["inicio"], 2) if len(giros) >= 2 else None,
            "giro2_fin_s": round(giros[1]["fin"], 2) if len(giros) >= 2 else None,
            "giro2_dur_s": round(giros[1]["duracion"], 2) if len(giros) >= 2 else None,
            "sent_inicio_s": round(sent["inicio_tiempo"], 2) if sent else None,
            "sent_fin_s": round(sent["fin_tiempo"], 2) if sent else None,
            "sent_dur_s": round(sent["duracion"], 2) if sent else None,
            "izq_stance_ida_s": round(pasos["izquierda"]["stance_mean_ida"], 2) if "izquierda" in pasos else None,
            "izq_swing_ida_s": round(pasos["izquierda"]["swing_mean_ida"], 2) if "izquierda" in pasos else None,
            "der_stance_ida_s": round(pasos["derecha"]["stance_mean_ida"], 2) if "derecha" in pasos else None,
            "der_swing_ida_s": round(pasos["derecha"]["swing_mean_ida"], 2) if "derecha" in pasos else None,
            "izq_stance_vuelta_s": round(pasos["izquierda"]["stance_mean_vuelta"], 2) if "izquierda" in pasos else None,
            "izq_swing_vuelta_s": round(pasos["izquierda"]["swing_mean_vuelta"], 2) if "izquierda" in pasos else None,
            "der_stance_vuelta_s": round(pasos["derecha"]["stance_mean_vuelta"], 2) if "derecha" in pasos else None,
            "der_swing_vuelta_s": round(pasos["derecha"]["swing_mean_vuelta"], 2) if "derecha" in pasos else None,
        })

    if filas_csv:
        with open(ruta_salida_csv, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(filas_csv[0].keys()))
            writer.writeheader()
            writer.writerows(filas_csv)

    print("-" * 70)
    print("Resumen de ejecucion del algoritmo predecesor en muestras aceptadas")
    print("-" * 70)
    print(f"Muestras aceptadas procesadas : {len(filas_csv)}")
    print(f"Muestras con las 5 fases      : {completos}")
    print(f"Archivo de resultados         : {ruta_salida_csv}")
    print("-" * 70)


def main():
    parser = argparse.ArgumentParser(description="Ejecuta el algoritmo de segmentacion TUG del PDG anterior.")
    parser.add_argument("--archivo", type=str, default=None, help="Archivo JSON individual a procesar")
    parser.add_argument("--lote", action="store_true", help="Procesar las 66 muestras aceptadas de personas.csv")
    args = parser.parse_args()

    if args.archivo:
        ruta = args.archivo
        if not os.path.isabs(ruta) and not os.path.exists(ruta):
            ruta = os.path.join(DEFAULT_DATA_DIR, ruta)
        res = ejecutar_segmentacion_archivo(ruta)
        imprimir_resultado_archivo(res)

    if args.lote or not args.archivo:
        procesar_lote(DEFAULT_DATA_DIR, DEFAULT_PERSONAS_CSV, DEFAULT_OUTPUT_CSV)


if __name__ == "__main__":
    main()
