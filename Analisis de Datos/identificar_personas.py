"""
Identificación de personas en el dataset TUG.

Los archivos no traen ID de paciente explícito (patient.id, name y lastName vienen vacíos)
y el código del nombre del archivo (_temp_A, _temp_BX, ...) es por GRABACIÓN, no por persona.
Este script infiere la persona única mediante la tupla demográfica, audita duplicados exactos
por red (MD5), valida integridad biomecánica (sensores mínimos y advertencias) y genera personas.csv.

Uso:
    python3 identificar_personas.py [carpeta_json]

Salida:
    - Evidencia en consola (pasos 1 a 5).
    - personas.csv con participantes, metadatos y trazabilidad.
"""
import csv
import datetime
import glob
import hashlib
import itertools
import json
import os
import sys
from collections import defaultdict


def resolver_carpeta_datos(ruta_argumento=None):
    """
    Determina la ruta de datos crudos priorizando el argumento del usuario
    y verificando rutas relativas habituales en el repositorio.
    """
    candidatas = [
        ruta_argumento,
        "Datos Crudos",
        "../Datos Crudos",
        "./Datos Crudos",
        os.path.join(os.getcwd(), "Datos Crudos"),
        os.path.join(os.path.dirname(os.getcwd()), "Datos Crudos"),
        "datos_extraidos/anonymized_data",
    ]
    for r in candidatas:
        if r and os.path.exists(r) and os.path.isdir(r):
            if glob.glob(os.path.join(r, "*.json")):
                return r
    return ruta_argumento or "Datos Crudos"


CARPETA = resolver_carpeta_datos(sys.argv[1] if len(sys.argv) > 1 else None)


def cargar_registros(carpeta):
    registros = []
    rutas = sorted(glob.glob(os.path.join(carpeta, "*.json")))
    for ruta in rutas:
        nombre = os.path.basename(ruta)
        with open(ruta, "rb") as fh:
            crudo = fh.read()
        d = json.loads(crudo.decode("utf-8"))
        p = d.get("patient") or {}
        inicio = d.get("timestamp")

        # 1. Detección segura de sensores físicos presentes
        imu_data = d.get("imuData", [])
        devices = {x.get("deviceId") for x in imu_data if x.get("deviceId")}

        has_spine = any("spine" in x.lower() or "base" in x.lower() for x in devices)
        has_l_ankle = any("left-ankle" in x.lower() or "left_ankle" in x.lower() for x in devices)
        has_r_ankle = any("right-ankle" in x.lower() or "right_ankle" in x.lower() for x in devices)
        min_sensores_ok = bool(has_spine and has_l_ankle and has_r_ankle)

        # 2. Duración de la señal registrada
        ts_list = [x.get("timestamp", 0) for x in imu_data if "timestamp" in x]
        dur_s = (max(ts_list) - min(ts_list)) / 1000.0 if len(ts_list) > 1 else 0.0

        # 3. Detección robusta de Kit IMU (sin asumir indexación fija de imuData[0])
        kit = "K1" if any(x.startswith("K1-") for x in devices) else "base"

        # 4. Advertencias técnicas y pausas en grabación
        has_warning = bool(d.get("hasWarning", False))
        warning_reason = (d.get("warningReason") or "").strip()
        pausa_ms = d.get("pausedDurationMs", 0) or 0

        # 5. Observaciones clínicas y tareas experimentales
        obs_p = (p.get("observations") or "").strip()
        obs_t = (d.get("observations") or "").strip()
        todo_obs = f"{obs_p} {obs_t}".lower()

        es_dual = any(kw in todo_obs for kw in ["dual", "doble tarea", "resta", "ciudades", "tarea cognitiva"])
        tiene_dbs = "dbs" in todo_obs

        # Código de archivo (extraído de convención _temp_XX)
        codigo = nombre.split("_temp_")[1][:-5] if "_temp_" in nombre else nombre

        registros.append({
            "archivo": nombre,
            "codigo": codigo,
            "md5": hashlib.md5(crudo).hexdigest(),
            "id_campos": [p.get("id"), p.get("name"), p.get("lastName"), d.get("id")],
            "nacimiento": p.get("birthDate"),
            "sexo": p.get("sex"),
            "talla": p.get("height"),
            "tipo": p.get("patientType"),
            "obs_paciente": obs_p,
            "obs_prueba": obs_t,
            "kit": kit,
            "inicio": (datetime.datetime.fromtimestamp(inicio / 1000, datetime.timezone.utc)
                       .strftime("%Y-%m-%d %H:%M:%S") if inicio and inicio > 1e12 else ""),
            "duracion_s": round(dur_s, 2),
            "num_sensores": len(devices),
            "min_sensores_ok": min_sensores_ok,
            "tiene_warning": has_warning,
            "motivo_warning": warning_reason if has_warning else "",
            "pausa_ms": pausa_ms,
            "es_doble_tarea": es_dual,
            "tiene_dbs": tiene_dbs,
        })
    return registros


def main():
    print(f"Carpeta de datos crudos: {CARPETA}")
    R = cargar_registros(CARPETA)
    print(f"Archivos analizados: {len(R)}\n")

    if not R:
        print("No se encontraron archivos JSON en la ruta indicada.")
        return

    # Paso 1: no existe un identificador explícito
    con_id = [r["codigo"] for r in R if any(r["id_campos"])]
    print("PASO 1. Campos de identidad (patient.id, name, lastName, id) no vacíos:",
          con_id or "ninguno -> no hay ID explícito")

    # Paso 2: el código del archivo no identifica personas
    por_codigo = defaultdict(list)
    for r in R:
        por_codigo[r["codigo"]].append(r)
    repetidos = {c: rs for c, rs in por_codigo.items() if len(rs) > 1}
    print(f"\nPASO 2. Códigos distintos: {len(por_codigo)} de {len(R)} archivos. Códigos repetidos:")
    for c, rs in repetidos.items():
        iguales = len({r["md5"] for r in rs}) == 1
        print(f"   {c}: {[r['archivo'] for r in rs]} -> {'MISMO MD5 (duplicado byte a byte)' if iguales else 'contenido distinto'}")

    # Paso 3: agrupar por la llave demográfica (nacimiento + sexo + tipo)
    grupos = defaultdict(list)
    for r in R:
        grupos[(r["nacimiento"], r["sexo"], r["tipo"])].append(r)
    print("\nPASO 3. Grupos con más de un archivo bajo la llave (fecha de nacimiento, sexo, tipo).")
    print("        Columnas de corroboración: talla, kit, hora de inicio (UTC), observaciones.")
    for llave, rs in grupos.items():
        if len(rs) < 2:
            continue
        print(f"\n   {llave}")
        for r in rs:
            print(f"     {r['codigo']:3} talla={r['talla']} kit={r['kit']:4} inicio={r['inicio']} "
                  f"md5={r['md5'][:8]} obs_paciente={r['obs_paciente']!r} obs_prueba={r['obs_prueba']!r}")

    # Paso 4: control de falsos negativos (misma persona con fecha mal digitada)
    print("\nPASO 4. Fechas de nacimiento que difieren en un solo dígito (posible error de digitación):")
    etiquetados = [r for r in R if r["tipo"]]
    hallados = False
    for a, b in itertools.combinations(etiquetados, 2):
        if not a["nacimiento"] or not b["nacimiento"] or a["nacimiento"] == b["nacimiento"] or a["sexo"] != b["sexo"]:
            continue
        if len(a["nacimiento"]) == len(b["nacimiento"]) and sum(x != y for x, y in zip(a["nacimiento"], b["nacimiento"])) == 1:
            hallados = True
            veredicto = "misma talla -> REVISAR" if a["talla"] == b["talla"] else "talla distinta -> personas distintas"
            print(f"   {a['codigo']} ({a['nacimiento']}, {a['talla']} cm, {a['obs_paciente']!r}) vs "
                  f"{b['codigo']} ({b['nacimiento']}, {b['talla']} cm, {b['obs_paciente']!r}) -> {veredicto}")
    if not hallados:
        print("   ninguna")

    # Paso 5: asignar el ID de persona separando PRUEBA_TECNICA de participantes reales
    ids = {}
    p_count = 1
    for llave in sorted(grupos, key=lambda k: min(r["archivo"] for r in grupos[k])):
        tipo_llave = llave[2]
        if not tipo_llave or tipo_llave == "SIN_ETIQUETA":
            ids[llave] = "PRUEBA_TECNICA"
        else:
            ids[llave] = f"P{p_count:02d}"
            p_count += 1

    vistos_md5 = {}
    filas = []
    for r in R:
        llave = (r["nacimiento"], r["sexo"], r["tipo"])
        es_duplicado = r["md5"] in vistos_md5
        duplicado_de = vistos_md5.get(r["md5"], "")
        if not es_duplicado:
            vistos_md5[r["md5"]] = r["archivo"]

        filas.append({
            "archivo": r["archivo"],
            "codigo": r["codigo"],
            "persona_id": ids[llave],
            "tipo": r["tipo"] or "SIN_ETIQUETA",
            "sexo": r["sexo"] or "NO_REGISTRA",
            "nacimiento": r["nacimiento"] or "NO_REGISTRA",
            "talla": r["talla"] or "NO_REGISTRA",
            "kit": r["kit"],
            "inicio_utc": r["inicio"] or "NO_REGISTRA",
            "duracion_s": r["duracion_s"],
            "num_sensores": r["num_sensores"],
            "min_sensores_ok": r["min_sensores_ok"],
            "duplicado_exacto": es_duplicado,
            "duplicado_de": duplicado_de if es_duplicado else "",
            "tiene_warning": r["tiene_warning"],
            "motivo_warning": r["motivo_warning"] if r["tiene_warning"] else "Sin advertencias",
            "pausa_ms": r["pausa_ms"],
            "es_doble_tarea": r["es_doble_tarea"],
            "tiene_dbs": r["tiene_dbs"],
            "obs_paciente": r["obs_paciente"] or "Sin observaciones",
            "obs_prueba": r["obs_prueba"] or "Sin observaciones",
            "md5": r["md5"],
        })

    # Exportar archivo CSV en la misma carpeta que el script o directorio actual
    ruta_salida = "personas.csv"
    if os.path.exists("Analisis de Datos") and os.path.isdir("Analisis de Datos"):
        ruta_salida = os.path.join("Analisis de Datos", "personas.csv")

    with open(ruta_salida, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(filas[0].keys()))
        w.writeheader()
        w.writerows(filas)

    personas = defaultdict(set)
    for f in filas:
        personas[f["tipo"]].add(f["persona_id"])

    print("\nPASO 5. Resumen")
    print(f"   Archivos analizados:  {len(filas)}")
    print(f"   Duplicados exactos:   {sum(f['duplicado_exacto'] for f in filas)}")
    participantes_reales = {f["persona_id"] for f in filas if f["persona_id"] != "PRUEBA_TECNICA"}
    print(f"   Participantes reales: {len(participantes_reales)} (P01 a P{len(participantes_reales):02d})")
    print(f"   Pruebas técnicas:     {sum(1 for f in filas if f['persona_id'] == 'PRUEBA_TECNICA')} archivos")
    print("\n   Desglose por tipo:")
    for tipo, ps in sorted(personas.items()):
        n_arch = sum(1 for f in filas if f["tipo"] == tipo)
        ps_filtradas = {p for p in ps if p != "PRUEBA_TECNICA"}
        cant_p = len(ps_filtradas) if tipo != "SIN_ETIQUETA" else "N/A (Prueba técnica)"
        print(f"   • {tipo:<15} archivos={n_arch:2}  sujetos_únicos={cant_p}")

    print(f"\nTabla escrita en: {ruta_salida}")


if __name__ == "__main__":
    main()

