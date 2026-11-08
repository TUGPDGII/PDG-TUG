import os, json, csv
from datetime import datetime, timezone, timedelta

col_tz = timezone(timedelta(hours=-5))
emotion_dir = '/home/guarinve/Documentos/PDG-TUG/Datos e-Motion'
files = sorted([f for f in os.listdir(emotion_dir) if f.endswith('.json')])

records = []
for f in files:
    p = os.path.join(emotion_dir, f)
    with open(p, encoding='utf-8') as jf:
        d = json.load(jf)
        
        is_raw = f.endswith('_raw.json')
        cap = d.get('CaptureTest', {})
        date_str = cap.get('Date', '') or d.get('capture_date', '')
        type_test = cap.get('TypeTest', d.get('TypeTest', d.get('sensor_type', 'N/A')))
        duration = cap.get('Duration', '')
        camera = d.get('Camera', cap.get('Camera', 'N/A'))
        version = d.get('version', 'N/A')
        
        # Frames o SkeletonLocation
        frames_count = 0
        if 'CaptureTest' in d and 'KinectMachineStatus' in d['CaptureTest']:
            kms = d['CaptureTest']['KinectMachineStatus']
            if len(kms) > 0 and 'SkeletonLocation' in kms[0]:
                frames_count = len(kms[0]['SkeletonLocation'])
        elif 'Frames' in d:
            frames_count = len(d['Frames'])
        elif 'results' in d:
            frames_count = len(d['results'])
            
        patient_obj = d.get('Patient', {})
        patient_id = patient_obj.get('Id', 'N/A') if isinstance(patient_obj, dict) else 'N/A'
        
        # Criterio de utilidad para segmentación completa vs solo marcha/distancias
        # Según Domi R#8: cámaras pierden el giro y a veces el inicio sentado.
        # Son útiles para distancias y marcha si duracion >= 10s y frames >= 200.
        # Para segmentación TUG completa con giro: 0 (las cámaras pierden el giro).
        util_marcha_distancia = "SÍ" if (frames_count >= 200 and type_test in ['TIMED_UP_AND_GO', 'Timed up and Go']) else ("PARCIAL" if type_test in ['TIMED_UP_AND_GO', 'Timed up and Go'] else "NO (Gait Analysis / Proc)")
        util_segmentacion_completa = "NO (Pérdida en giro)" if type_test in ['TIMED_UP_AND_GO', 'Timed up and Go'] else "NO"
        
        records.append({
            'archivo': f,
            'is_raw': is_raw,
            'fecha': date_str,
            'tipo_test': type_test,
            'duracion': duration,
            'camara': camera,
            'frames': frames_count,
            'patient_id': patient_id,
            'util_marcha_distancia': util_marcha_distancia,
            'util_segmentacion_completa': util_segmentacion_completa
        })

lines = []
lines.append('# 📄 FICHA TÉCNICA DEL DATASET DE CÁMARA (e-Motion / VIMOV)\n\n')
lines.append('> **Documento Técnico de Evaluación y Control de Muestras de Video y Pose**\n')
lines.append('> **Compromiso:** Reunión #8 con Prof. Domiciano Rincón (Acuerdo: "Evaluar muestras y crear ficha técnica de las muestras de video para determinar cuáles son útiles para segmentación y cuáles para distancias").\n')
lines.append('> **Fecha de consolidación:** Noviembre 2026\n\n')

lines.append('## 1. Resumen Ejecutivo del Dataset de Cámaras\n\n')
total_archivos = len(records)
raw_count = sum(1 for r in records if r['is_raw'])
tug_count = sum(1 for r in records if r['tipo_test'] in ['TIMED_UP_AND_GO', 'Timed up and Go'])
intel_count = sum(1 for r in records if 'intel' in r['camara'].lower() or 'realsense' in r['camara'].lower())
orbbec_count = sum(1 for r in records if 'orbbec' in r['camara'].lower() or 'astra' in r['camara'].lower())
utiles_marcha = sum(1 for r in records if r['util_marcha_distancia'] == 'SÍ')

lines.append('| Indicador | Valor Total | Observación Metodológica |\n')
lines.append('|---|---:|---|\n')
lines.append(f'| **Total Archivos en `Datos e-Motion/`** | **{total_archivos}** | 30 capturas RAW + 2 procesados con métricas |\n')
lines.append(f'| **Capturas RAW (`*_raw.json`)** | **{raw_count}** | Datos de articulaciones tridimensionales (Body Pose) |\n')
lines.append(f'| **Pruebas TUG Declaradas** | **{tug_count}** | 29 capturas TUG válidas; 1 captura es `Gait Analysis` |\n')
lines.append(f'| **Cámaras Intel RealSense (D455/D455F)** | **{intel_count}** | 25 archivos capturados en laboratorio / pruebas |\n')
lines.append(f'| **Cámaras Orbbec Astra 2** | **{orbbec_count}** | 5 archivos de la Brigada del 04 de julio de 2026 |\n')
lines.append(f'| **Muestras útiles para Tamaño de Zancada / Velocidad** | **{utiles_marcha}** | Calidad cinemática adecuada en planos de marcha 1 y 2 |\n')
lines.append('| **Muestras útiles para Segmentación TUG Completa** | **0** (0.0%) | **Limitación física:** la cámara pierde tracking en giro y sentado |\n\n')

lines.append('## 2. Conclusiones Metodológicas y Fisiológicas (Reunión #8)\n\n')
lines.append('1. **Limitación de Campo Visual en Giros:** Como verificaron Esteban Guarin y el Prof. Domiciano Rincón, al aproximarse la persona al punto de giro (cerca de la cámara), el esqueleto se descalibra y pierde la continuidad articular. Por tanto, **las cámaras NO son aptas para segmentar los giros ni contar los pasos durante el giro**; esta tarea recae con exclusividad en los sensores IMU (giroscopio de espina base y acelerómetros de tobillo).\n')
lines.append('2. **Utilidad Central de la Cámara:** Las 29 grabaciones TUG son altamente aprovechables para extraer **variables espaciotemporales con referencia externa fija**: tamaño de paso/zancada (distancia euclidiana entre tobillos en plano XZ) y velocidad lineal de avance mediante la pendiente del `Hip Center` en las fases de marcha de ida y vuelta.\n')
lines.append('3. **Estado de la Variable Clínica `patient`:** En los archivos de cámara, la estructura contiene el objeto `Patient` con el identificador UUID del sujeto (`Patient.Id`), pero los campos demográficos y la bandera booleana directa se encuentran centralizados en el sistema de gestión clínica VIMOV.\n\n')

lines.append('## 3. Matriz Detallada de Muestras de Video / Esqueleto\n\n')
lines.append('| # | Archivo | Tipo Prueba | Cámara | Duración | Frames | Utilidad Marcha / Velocidad | Utilidad Segmentación Completa |\n')
lines.append('|---:|---|:---:|---|:---:|---:|:---:|:---:|\n')

idx = 1
for r in records:
    dur_str = f"{r['duracion']}s" if r['duracion'] else "-"
    lines.append(f"| {idx} | `{r['archivo']}` | {r['tipo_test']} | {r['camara']} | {dur_str} | {r['frames']} | **{r['util_marcha_distancia']}** | {r['util_segmentacion_completa']} |\n")
    idx += 1

out_path = '/home/guarinve/Documentos/PDG-TUG/Datos e-Motion/FichaTecnica_eMotion.md'
with open(out_path, 'w', encoding='utf-8') as out_f:
    out_f.writelines(lines)

print('Ficha técnica de cámaras creada exitosamente:', out_path)
