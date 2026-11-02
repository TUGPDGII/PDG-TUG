# 📄 FICHA TÉCNICA DEL DATASET DE CÁMARA (e-Motion / VIMOV)

> **Documento Técnico de Evaluación y Control de Muestras de Video y Pose**
> **Compromiso:** Reunión #8 con Prof. Domiciano Rincón (Acuerdo: "Evaluar muestras y crear ficha técnica de las muestras de video para determinar cuáles son útiles para segmentación y cuáles para distancias").
> **Fecha de consolidación:** Noviembre 2026

## 1. Resumen Ejecutivo del Dataset de Cámaras

| Indicador | Valor Total | Observación Metodológica |
|---|---:|---|
| **Total Archivos en `Datos e-Motion/`** | **32** | 30 capturas RAW + 2 procesados con métricas |
| **Capturas RAW (`*_raw.json`)** | **30** | Datos de articulaciones tridimensionales (Body Pose) |
| **Pruebas TUG Declaradas** | **29** | 29 capturas TUG válidas; 1 captura es `Gait Analysis` |
| **Cámaras Intel RealSense (D455/D455F)** | **25** | 25 archivos capturados en laboratorio / pruebas |
| **Cámaras Orbbec Astra 2** | **5** | 5 archivos de la Brigada del 04 de julio de 2026 |
| **Muestras útiles para Tamaño de Zancada / Velocidad** | **29** | Calidad cinemática adecuada en planos de marcha 1 y 2 |
| **Muestras útiles para Segmentación TUG Completa** | **0** (0.0%) | **Limitación física:** la cámara pierde tracking en giro y sentado |

## 2. Conclusiones Metodológicas y Fisiológicas (Reunión #8)

1. **Limitación de Campo Visual en Giros:** Como verificaron Esteban Guarin y el Prof. Domiciano Rincón, al aproximarse la persona al punto de giro (cerca de la cámara), el esqueleto se descalibra y pierde la continuidad articular. Por tanto, **las cámaras NO son aptas para segmentar los giros ni contar los pasos durante el giro**; esta tarea recae con exclusividad en los sensores IMU (giroscopio de espina base y acelerómetros de tobillo).
2. **Utilidad Central de la Cámara:** Las 29 grabaciones TUG son altamente aprovechables para extraer **variables espaciotemporales con referencia externa fija**: tamaño de paso/zancada (distancia euclidiana entre tobillos en plano XZ) y velocidad lineal de avance mediante la pendiente del `Hip Center` en las fases de marcha de ida y vuelta.
3. **Estado de la Variable Clínica `patient`:** En los archivos de cámara, la estructura contiene el objeto `Patient` con el identificador UUID del sujeto (`Patient.Id`), pero los campos demográficos y la bandera booleana directa se encuentran centralizados en el sistema de gestión clínica VIMOV.

## 3. Matriz Detallada de Muestras de Video / Esqueleto

| # | Archivo | Tipo Prueba | Cámara | Duración | Frames | Utilidad Marcha / Velocidad | Utilidad Segmentación Completa |
|---:|---|:---:|---|:---:|---:|:---:|:---:|
| 1 | `0cce5b72-f8d0-458e-b576-64c138fd2b53_raw.json` | TIMED_UP_AND_GO | Orbbec Orbbec Astra 2 | - | 395 | **SÍ** | NO (Pérdida en giro) |
| 2 | `20241016_intel_b7e13693_raw.json` | Timed up and Go | Intel RealSense D455 | - | 426 | **SÍ** | NO (Pérdida en giro) |
| 3 | `20261002_intel_09a4dc83_raw.json` | TIMED_UP_AND_GO | Intel Intel RealSense D455F | - | 427 | **SÍ** | NO (Pérdida en giro) |
| 4 | `20261002_intel_84010489_raw.json` | TIMED_UP_AND_GO | Intel Intel RealSense D455F | - | 355 | **SÍ** | NO (Pérdida en giro) |
| 5 | `20261002_intel_890b769c_raw.json` | TIMED_UP_AND_GO | Intel Intel RealSense D455F | - | 427 | **SÍ** | NO (Pérdida en giro) |
| 6 | `20261002_intel_a7da7cf0_raw.json` | TIMED_UP_AND_GO | Intel Intel RealSense D455F | - | 503 | **SÍ** | NO (Pérdida en giro) |
| 7 | `20261002_intel_c9e9720b_raw.json` | TIMED_UP_AND_GO | Intel Intel RealSense D455F | - | 400 | **SÍ** | NO (Pérdida en giro) |
| 8 | `20261014_intel_2058a215_raw.json` | TIMED_UP_AND_GO | Intel Intel RealSense D455F | - | 469 | **SÍ** | NO (Pérdida en giro) |
| 9 | `20261014_intel_4d3da61e_raw.json` | TIMED_UP_AND_GO | Intel Intel RealSense D455F | - | 406 | **SÍ** | NO (Pérdida en giro) |
| 10 | `20261014_intel_64212756_raw.json` | TIMED_UP_AND_GO | Intel Intel RealSense D455F | - | 391 | **SÍ** | NO (Pérdida en giro) |
| 11 | `20261014_intel_8a6c58e7_raw.json` | TIMED_UP_AND_GO | Intel Intel RealSense D455F | - | 433 | **SÍ** | NO (Pérdida en giro) |
| 12 | `20261014_intel_c95b9599_raw.json` | TIMED_UP_AND_GO | Intel Intel RealSense D455F | - | 384 | **SÍ** | NO (Pérdida en giro) |
| 13 | `20261014_intel_ddf77635_raw.json` | TIMED_UP_AND_GO | Intel Intel RealSense D455F | - | 502 | **SÍ** | NO (Pérdida en giro) |
| 14 | `20261014_intel_eb4373aa_raw.json` | TIMED_UP_AND_GO | Intel Intel RealSense D455F | - | 594 | **SÍ** | NO (Pérdida en giro) |
| 15 | `20261015_intel_0d4c2104_raw.json` | TIMED_UP_AND_GO | Intel Intel RealSense D455F | - | 365 | **SÍ** | NO (Pérdida en giro) |
| 16 | `20261015_intel_282d8a1b_raw.json` | TIMED_UP_AND_GO | Intel Intel RealSense D455F | - | 445 | **SÍ** | NO (Pérdida en giro) |
| 17 | `20261015_intel_3bb1c3b6_raw.json` | TIMED_UP_AND_GO | Intel Intel RealSense D455F | - | 419 | **SÍ** | NO (Pérdida en giro) |
| 18 | `20261015_intel_3cbf990b_raw.json` | TIMED_UP_AND_GO | Intel Intel RealSense D455F | - | 370 | **SÍ** | NO (Pérdida en giro) |
| 19 | `20261015_intel_684a7afe_raw.json` | TIMED_UP_AND_GO | Intel Intel RealSense D455F | - | 411 | **SÍ** | NO (Pérdida en giro) |
| 20 | `20261015_intel_aba7198f_raw.json` | TIMED_UP_AND_GO | Intel Intel RealSense D455F | - | 429 | **SÍ** | NO (Pérdida en giro) |
| 21 | `20261015_intel_d0dd12ae_raw.json` | TIMED_UP_AND_GO | Intel Intel RealSense D455F | - | 426 | **SÍ** | NO (Pérdida en giro) |
| 22 | `20261015_intel_fb517029_raw.json` | TIMED_UP_AND_GO | Intel Intel RealSense D455F | - | 281 | **SÍ** | NO (Pérdida en giro) |
| 23 | `20261016_intel_8f6b70f7_raw.json` | TIMED_UP_AND_GO | Intel Intel RealSense D455 | - | 610 | **SÍ** | NO (Pérdida en giro) |
| 24 | `20261016_intel_cfa0d535_raw.json` | TIMED_UP_AND_GO | Intel Intel RealSense D455 | - | 689 | **SÍ** | NO (Pérdida en giro) |
| 25 | `3166462b-4d99-4f14-b560-5a9c1dc08d31_raw.json` | TIMED_UP_AND_GO | Intel Intel RealSense D455F | - | 358 | **SÍ** | NO (Pérdida en giro) |
| 26 | `4849da67-9862-4f1a-b960-165cfa5306e7_raw.json` | TIMED_UP_AND_GO | Orbbec Orbbec Astra 2 | - | 557 | **SÍ** | NO (Pérdida en giro) |
| 27 | `49196b62-cc36-4dea-87dc-0ba91cd9c229.json` | intel | N/A | - | 2 | **NO (Gait Analysis / Proc)** | NO |
| 28 | `56108fef-0268-4f6f-920e-97787068b311_raw.json` | TIMED_UP_AND_GO | Orbbec Orbbec Astra 2 | - | 796 | **SÍ** | NO (Pérdida en giro) |
| 29 | `6f6fd032-b451-43c6-8554-b0328ee96b58_raw.json` | Gait Analysis | Intel RealSense D455 | - | 195 | **NO (Gait Analysis / Proc)** | NO |
| 30 | `93b689a7-dfc2-4069-a935-efdde29de98a_raw.json` | TIMED_UP_AND_GO | Orbbec Orbbec Astra 2 | - | 644 | **SÍ** | NO (Pérdida en giro) |
| 31 | `b6487716-3d2f-4728-b000-cd71ccc723c2_raw.json` | TIMED_UP_AND_GO | Orbbec Orbbec Astra 2 | - | 520 | **SÍ** | NO (Pérdida en giro) |
| 32 | `fa5aaa78-0ba9-4c21-abf5-c6a94f6748c3.json` | orbbec_astra_2 | N/A | - | 2 | **NO (Gait Analysis / Proc)** | NO |
