# FICHA TÉCNICA OFICIAL DEL DATASET ÓPTICO (e-Motion / VIMOV) — PROYECTO TUG-V2
> **Documento Oficial de Auditoría, Control de Calidad y Caracterización Biomecánica**
> **Fecha de Consolidación:** 02 de Noviembre de 2026
> **Metodología:** CRISP-DM (Fases de Comprensión y Preparación de Datos)
> **Directrices Metodológicas y Clínicas:** Tutor Prof. Domiciano Rincón (Reunión #8 y actas previas)

---

## 1. Resumen Ejecutivo del Conjunto de Datos Ópticos

| Indicador Metodológico | Valor Total | Observación y Respaldo Técnico |
|:---|:---:|:---|
| **Total Grabaciones JSON en el Dataset** | **269** | Totalidad de capturas descargadas, auditadas y anonimizadas de VIMOV |
| **Grabaciones Protocolo TUG (`Datos e-Motion/`)** | **132** | Evaluaciones Timed Up and Go estándar con silla y giro a 3 metros |
| **Grabaciones Protocolo Marcha (`No_TUG_Gait_Analysis/`)** | **137** | Pruebas de marcha continua lineal (10 metros) + 2 archivos de métricas comparativas |
| **Capturas Brigada Santa Marta (`SMR_`)** | **225** | **100% de la brigada descargada** (103 TUG + 122 Marcha Continua) |
| **Capturas Brigada CST / La Victoria (`CST_`)** | **21** | 6 TUG + 13 Marcha Continua + 2 comparativas Orbbec vs Intel |
| **Capturas de Laboratorio / Pilotos (`LAB_`)** | **23** | 23 TUG de calibración en laboratorio Icesi (octubre 2024 / 2026) |
| **Pares Bimodales IMU ↔ e-Motion Confirmados** | **42** | Coincidencia temporal estricta (<180s), protocolo TUG y validación de sexo |
| **Integridad de Archivos (Corrupción / Vacíos)** | **0 colisiones / 0 vacíos** | 100% archivos JSON válidos con secuencias esqueléticas tridimensionales |
| **Anonimización Ética** | **100% Verificada** | Despersonalización según estándar GHGIS 2 (sin nombres ni identificaciones) |

---

## 2. Criterios de Descarte vs. Conservación (Directrices Reunión #8)

En concordancia con las conclusiones acordadas con el tutor metodológico **Prof. Domiciano Rincón** en la Reunión #8 (27 de octubre de 2026), se fijaron las siguientes directrices formales:

### A. Conservación de Datos Externos a la Brigada
* **Fundamento:** Esteban Guarín consultó expresamente sobre la pertinencia de descartar o eliminar grabaciones tomadas fuera de la Brigada Santa Marta (ej. Laboratorio Icesi o CST).
* **Decisión Acordada:** **No descartar los datos externos**. Mientras compartan el diseño experimental básico (recorrido de 3 metros, cámara fija frontal a distancia estándar), constituyen un insumo válido para calibración, validación algorítmica y caracterización de variabilidad.

### B. Conservación de Muestras con Pérdida en Giro o Sentado (Delimitación Metodológica)
* **Fundamento Clínico/Técnico:** Durante la prueba TUG, las cámaras ópticas pierden el rastreo esquelético durante la rotación de 180° (por salir de la cobertura angular o por oclusión corporal al cambiar de plano sagital a frontal) y en la fase sentado/levantado (debido a la lejanía a 4 metros y la posición flexionada contra la silla).
* **Decisión Acordada:** **No descartar las muestras por este motivo**. Las cámaras se delimitan metodológicamente de manera exclusiva para medir el **tamaño de la zancada** (distancia euclidiana entre tobillos) y la **velocidad lineal de marcha** (pendiente de desplazamiento del `Hip Center` en el tiempo) durante las fases de marcha recta (Marcha 1 de ida y Marcha 2 de regreso). La segmentación de los giros, levantamiento y sentado se delega íntegramente a los sensores inerciales (IMUs).

### C. Integración y Conservación de Grabaciones de Marcha Continua (`No_TUG_Gait_Analysis/`)
* **Fundamento:** Las grabaciones de marcha continua de 10 metros capturadas en Santa Marta permiten monitorear parámetros locomotores puros (cadencia, velocidad continua y zancada) sin la perturbación dinámica de las transiciones de postura ni el giro cerrado.
* **Decisión Acordada:** Conservar y documentar las 137 grabaciones de marcha en su propia subcarpeta, permitiendo análisis espaciotemporales complementarios.

### D. Criterio Estricto de Concordancia de Género en Bimodalidad
* **Fundamento:** El emparejamiento entre sensores inerciales y cámaras no puede sustentarse únicamente en cercanía temporal. Cuando se detecta discrepancia de sexo (ej. IMU masculino vs e-Motion femenino), el registro se desvincula del pareo bimodal para evitar falsas correspondencias.

---

## 3. Especificaciones Técnicas del Sistema Óptico (e-Motion / VIMOV)

* **Dispositivos de Captura:** Cámaras de profundidad RGB-D Intel RealSense D455 / D455F y Orbbec Astra 2.
* **Frecuencia de Muestreo:** Nominal 30.0 Hz (Efectiva: 29.8 ± 0.9 FPS). Los vectores de tiempo (`Timestamp` en ms) permiten interpolación temporal (*PCHIP*) cuando se requiere regularidad estricta para análisis frecuencial.
* **Topología Esquelética (15 Articulaciones 3D):**
  1. `SpineBase` / `BodyCenter`: Centro de masa pélvico, utilizado para calcular la velocidad de avance en el eje Z.
  2. `AnkleLeft` / `AnkleRight`: Tobillo izquierdo y derecho, fundamentales para la detección de impacto de talón (*heel strike*) y cálculo de longitud de zancada.
  3. `LeftHip` / `RightHip`, `LeftKnee` / `RightKnee`: Cinemática articular de miembros inferiores.
  4. `Head`, `LeftShoulder` / `RightShoulder`: Alineación cefálica y estabilidad del tronco superior.
  5. `LeftElbow` / `RightElbow`, `WristLeft` / `WristRight`: Balanceo de miembros superiores (*arm swing*).
* **Rango Operativo en Profundidad (Eje Z):** 0.85 m (zona de proximidad máxima en giro) a 4.30 m (posición de la silla al inicio y final).
* **Tasa Media de Seguimiento Articular Válido:** 95.9% en TUG y 89.2% en Marcha Continua.

---

## 4. Auditoría de Integridad y Ausencia de Pruebas Falsas

| Parámetro de Control | Resultado Obtenido | Estado de Validación |
|---|:---:|:---|
| **Archivos duplicados (colisión SHA-256)** | **0 colisiones** | **Verificado:** Cada uno de los 269 archivos posee contenido binario único |
| **Archivos corruptos o no parseables** | **0 archivos** | **Verificado:** 100% de archivos leídos y validados con parser JSON estricto |
| **Pruebas técnicas abortadas (< 3.0 s o 0 frames)** | **0 archivos** | **Verificado:** Ninguna captura vacía; duración mínima 9.4 s en TUG y 6.4 s en Marcha |
| **Tasa de frames por captura** | 281 a 2,382 frames | **Verificado:** Cobertura temporal íntegra para todas las pruebas |

---

## 5. Matriz de Complementariedad Biomecánica: IMUs vs. Cámaras

| Fase de la Prueba TUG | Aporte de Cámaras (e-Motion) | Aporte de Sensores IMU | Decisión Metodológica |
|---|---|---|---|
| **1. Levantamiento (Sit-to-Stand)** | Parcial / Limitado (distancia lejana a 4m) | **Óptimo:** Detección de energía en flexo-extensión (Canal B lumbar) | Segmentación por **IMU** |
| **2. Marcha de Ida (Marcha 1)** | **Excelente:** Longitud de zancada y velocidad real en metros | Local: Tiempos de swing/stance y aceleración de impacto | **Bimodal:** Distancia por Cámara, Fases por IMU |
| **3. Giro de 180°** | Deficiente: Pérdida de tracking por rotación fuera del plano | **Excelente:** Pico de velocidad angular en eje vertical (Canal L) | Segmentación y conteo por **IMU** |
| **4. Marcha de Regreso (Marcha 2)** | **Excelente:** Longitud de zancada y velocidad en aproximación | Local: Tiempos de swing/stance y cadencia | **Bimodal:** Distancia por Cámara, Fases por IMU |
| **5. Sentado (Stand-to-Sit)** | Parcial / Limitado (oclusión al flexionarse) | **Óptimo:** Potencia de desaceleración y flexión lumbar (Canal B) | Segmentación por **IMU** |

---

## 6. Auditoría Detallada de Grabaciones TUG (`Datos e-Motion/`, 132 Archivos)

| # | Archivo JSON | Brigada | Bimodal IMU | Sujeto ID | Clase Clínica | Sensor | Duración | Frames | FPS | Utilidad Biomecánica |
|---:|---|:---:|:---:|:---:|:---:|---|:---:|:---:|:---:|---|
| 1 | `CST_20260704_NO_IMU_522b4991_raw.json` | CST | NO | - | SIN_ETIQUETA | Orbbec Orbbec Astra 2 | 17.3 s | 520 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 2 | `CST_20260704_NO_IMU_5f9ae035_raw.json` | CST | NO | - | SIN_ETIQUETA | Orbbec Orbbec Astra 2 | 18.53 s | 557 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 3 | `CST_20260704_NO_IMU_6d6ae96f_raw.json` | CST | NO | - | SIN_ETIQUETA | Orbbec Orbbec Astra 2 | 21.43 s | 644 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 4 | `CST_20260704_NO_IMU_76d99a7d_raw.json` | CST | NO | - | SIN_ETIQUETA | Orbbec Orbbec Astra 2 | 13.13 s | 395 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 5 | `CST_20260704_NO_IMU_94c36593_raw.json` | CST | NO | - | SIN_ETIQUETA | Orbbec Orbbec Astra 2 | 26.5 s | 796 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 6 | `CST_20260704_P54_BE_c1b8493f_raw.json` | CST | SÍ (BE) | P54 | PATIENT | Orbbec Orbbec Astra 2 | 15.47 s | 465 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 7 | `LAB_20241016_INTEL_70e0d22c_raw.json` | LAB | NO | - | SIN_ETIQUETA | Intel RealSense D455 | 18.07 s | 426 | 23.6 | Marcha 1 & 2 (Zancada/Velocidad) |
| 8 | `LAB_20261002_INTEL_2956b231_raw.json` | LAB | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 13.31 s | 400 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 9 | `LAB_20261002_INTEL_520b776a_raw.json` | LAB | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 11.8 s | 355 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 10 | `LAB_20261002_INTEL_a9cf4492_raw.json` | LAB | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 14.21 s | 427 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 11 | `LAB_20261002_INTEL_cc51de7a_raw.json` | LAB | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 14.21 s | 427 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 12 | `LAB_20261002_INTEL_f30efa85_raw.json` | LAB | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 16.74 s | 503 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 13 | `LAB_20261014_INTEL_121da856_raw.json` | LAB | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 12.77 s | 384 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 14 | `LAB_20261014_INTEL_16b33e8a_raw.json` | LAB | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 14.41 s | 433 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 15 | `LAB_20261014_INTEL_79040a90_raw.json` | LAB | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 13.01 s | 391 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 16 | `LAB_20261014_INTEL_7fc5835d_raw.json` | LAB | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 15.64 s | 469 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 17 | `LAB_20261014_INTEL_b9a45110_raw.json` | LAB | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 13.51 s | 406 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 18 | `LAB_20261014_INTEL_d32af61b_raw.json` | LAB | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 16.71 s | 502 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 19 | `LAB_20261014_INTEL_f15708bb_raw.json` | LAB | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 19.81 s | 594 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 20 | `LAB_20261015_INTEL_55d2638e_raw.json` | LAB | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 12.34 s | 370 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 21 | `LAB_20261015_INTEL_63b55b0a_raw.json` | LAB | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 14.24 s | 426 | 29.9 | Marcha 1 & 2 (Zancada/Velocidad) |
| 22 | `LAB_20261015_INTEL_6eaf8dc9_raw.json` | LAB | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 12.14 s | 365 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 23 | `LAB_20261015_INTEL_a08f5d5d_raw.json` | LAB | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 14.27 s | 429 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 24 | `LAB_20261015_INTEL_c811ed2b_raw.json` | LAB | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 13.67 s | 411 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 25 | `LAB_20261015_INTEL_cd0662f6_raw.json` | LAB | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 14.01 s | 419 | 29.9 | Marcha 1 & 2 (Zancada/Velocidad) |
| 26 | `LAB_20261015_INTEL_da9df617_raw.json` | LAB | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 14.81 s | 445 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 27 | `LAB_20261015_INTEL_ec8f8ef4_raw.json` | LAB | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 9.4 s | 281 | 29.9 | Marcha 1 & 2 (Zancada/Velocidad) |
| 28 | `LAB_20261016_INTEL_633d0b5c_raw.json` | LAB | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 20.64 s | 610 | 29.6 | Marcha 1 & 2 (Zancada/Velocidad) |
| 29 | `LAB_20261016_INTEL_7d2dcd48_raw.json` | LAB | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 23.28 s | 689 | 29.6 | Marcha 1 & 2 (Zancada/Velocidad) |
| 30 | `SMR_20260625_NO_IMU_009ef8c0_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 22.4 s | 673 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 31 | `SMR_20260625_NO_IMU_0f778525_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 16.77 s | 504 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 32 | `SMR_20260625_NO_IMU_15bfcaa6_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 11.9 s | 358 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 33 | `SMR_20260625_NO_IMU_288e95dc_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 24.31 s | 730 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 34 | `SMR_20260625_NO_IMU_3c28cd08_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 14.03 s | 422 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 35 | `SMR_20260625_NO_IMU_43c24bf0_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 12.8 s | 385 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 36 | `SMR_20260625_NO_IMU_447fcdb7_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel RealSense D455 | 11.93 s | 359 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 37 | `SMR_20260625_NO_IMU_4ed70428_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 24.6 s | 739 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 38 | `SMR_20260625_NO_IMU_4efdbb56_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 23.18 s | 696 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 39 | `SMR_20260625_NO_IMU_6c8f0a73_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 79.4 s | 2382 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 40 | `SMR_20260625_NO_IMU_6dc36ad3_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 15.43 s | 464 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 41 | `SMR_20260625_NO_IMU_6f0edb81_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 15.38 s | 462 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 42 | `SMR_20260625_NO_IMU_92c49963_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 20.87 s | 627 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 43 | `SMR_20260625_NO_IMU_9eabbeda_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 16.47 s | 495 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 44 | `SMR_20260625_NO_IMU_a5508452_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 14.01 s | 421 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 45 | `SMR_20260625_NO_IMU_ae0b301a_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 18.7 s | 562 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 46 | `SMR_20260625_NO_IMU_b193794c_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 11.27 s | 339 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 47 | `SMR_20260625_NO_IMU_b4540bcd_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 19.87 s | 597 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 48 | `SMR_20260625_NO_IMU_b969b991_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 26.31 s | 790 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 49 | `SMR_20260625_NO_IMU_c111bc5e_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 12.5 s | 376 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 50 | `SMR_20260625_NO_IMU_e50718e8_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 12.67 s | 381 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 51 | `SMR_20260625_NO_IMU_e6619a94_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 14.27 s | 429 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 52 | `SMR_20260625_NO_IMU_ed8ad33f_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 15.77 s | 474 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 53 | `SMR_20260625_NO_IMU_f1d4af72_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 19.73 s | 593 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 54 | `SMR_20260625_P06_BF_4cd523b7_raw.json` | SMR | SÍ (BF) | P06 | PATIENT | Intel Intel RealSense D45 | 21.94 s | 659 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 55 | `SMR_20260625_P07_D_c71c489e_raw.json` | SMR | SÍ (D) | P07 | PATIENT | Intel Intel RealSense D45 | 25.05 s | 752 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 56 | `SMR_20260625_P08_AB_ff5603a4_raw.json` | SMR | SÍ (AB) | P08 | PATIENT | Intel Intel RealSense D45 | 18.14 s | 545 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 57 | `SMR_20260625_P09_AK_2adb11ee_raw.json` | SMR | SÍ (AK) | P09 | PATIENT | Intel Intel RealSense D45 | 24.37 s | 732 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 58 | `SMR_20260625_P10_AA_bf709abb_raw.json` | SMR | SÍ (AA) | P10 | PATIENT | Intel Intel RealSense D45 | 13.63 s | 410 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 59 | `SMR_20260625_P11_V_7ed2f2de_raw.json` | SMR | SÍ (V) | P11 | PATIENT | Intel Intel RealSense D45 | 15.24 s | 458 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 60 | `SMR_20260625_P13_BW_5eeb5a37_raw.json` | SMR | SÍ (BW) | P13 | PATIENT | Intel Intel RealSense D45 | 17.57 s | 528 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 61 | `SMR_20260625_P15_BK_b8317644_raw.json` | SMR | SÍ (BK) | P15 | PATIENT | Intel Intel RealSense D45 | 10.94 s | 329 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 62 | `SMR_20260625_P16_BD_f16693f6_raw.json` | SMR | SÍ (BD) | P16 | PATIENT | Intel Intel RealSense D45 | 16.5 s | 496 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 63 | `SMR_20260625_P18_BN_1f325d38_raw.json` | SMR | SÍ (BN) | P18 | PATIENT | Intel Intel RealSense D45 | 16.71 s | 502 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 64 | `SMR_20260625_P21_X_28ac951e_raw.json` | SMR | SÍ (X) | P21 | PATIENT | Intel Intel RealSense D45 | 21.77 s | 654 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 65 | `SMR_20260625_P22_BA_a22ff952_raw.json` | SMR | SÍ (BA) | P22 | PATIENT | Intel Intel RealSense D45 | 12.5 s | 376 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 66 | `SMR_20260626_NO_IMU_06d4e110_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 19.3 s | 580 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 67 | `SMR_20260626_NO_IMU_08f525af_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 13.4 s | 403 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 68 | `SMR_20260626_NO_IMU_270d9ce6_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 14.7 s | 442 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 69 | `SMR_20260626_NO_IMU_2e340220_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 18.27 s | 549 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 70 | `SMR_20260626_NO_IMU_39200f59_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 14.8 s | 445 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 71 | `SMR_20260626_NO_IMU_447fcdb7_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel RealSense D455 | 11.93 s | 359 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 72 | `SMR_20260626_NO_IMU_528dd3aa_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 21.6 s | 649 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 73 | `SMR_20260626_NO_IMU_65af5e95_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 20.1 s | 604 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 74 | `SMR_20260626_NO_IMU_67e1d010_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 21.44 s | 644 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 75 | `SMR_20260626_NO_IMU_6eea596c_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 14.17 s | 426 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 76 | `SMR_20260626_NO_IMU_73f8e2dd_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 18.57 s | 558 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 77 | `SMR_20260626_NO_IMU_77aab222_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 22.77 s | 684 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 78 | `SMR_20260626_NO_IMU_807435b0_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 17.87 s | 537 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 79 | `SMR_20260626_NO_IMU_97490f79_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 17.27 s | 519 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 80 | `SMR_20260626_NO_IMU_acb959ff_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 13.97 s | 420 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 81 | `SMR_20260626_NO_IMU_ae1bf11f_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 16.84 s | 506 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 82 | `SMR_20260626_NO_IMU_bb1a6ed3_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 30.93 s | 929 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 83 | `SMR_20260626_NO_IMU_c3cf78c7_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 13.8 s | 415 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 84 | `SMR_20260626_NO_IMU_d69fd999_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 21.53 s | 647 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 85 | `SMR_20260626_NO_IMU_db5953a4_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 12.3 s | 370 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 86 | `SMR_20260626_NO_IMU_dda03461_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 22.88 s | 687 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 87 | `SMR_20260626_NO_IMU_e5e1c5a8_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 18.8 s | 565 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 88 | `SMR_20260626_NO_IMU_fb6cfbf2_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 16.1 s | 484 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 89 | `SMR_20260626_P24_AV_fc8711e0_raw.json` | SMR | SÍ (AV) | P24 | PATIENT | Intel Intel RealSense D45 | 25.8 s | 775 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 90 | `SMR_20260626_P25_AO_ce5691b9_raw.json` | SMR | SÍ (AO) | P25 | PATIENT | Intel Intel RealSense D45 | 21.67 s | 651 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 91 | `SMR_20260626_P26_M_0ec82be7_raw.json` | SMR | SÍ (M) | P26 | PATIENT | Intel Intel RealSense D45 | 33.97 s | 1020 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 92 | `SMR_20260626_P27_BQ_156f5309_raw.json` | SMR | SÍ (BQ) | P27 | PATIENT | Intel Intel RealSense D45 | 20.57 s | 618 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 93 | `SMR_20260626_P30_O_5432070f_raw.json` | SMR | SÍ (O) | P30 | PATIENT | Intel Intel RealSense D45 | 17.73 s | 533 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 94 | `SMR_20260626_P31_BU_f89f97d0_raw.json` | SMR | SÍ (BU) | P31 | PATIENT | Intel Intel RealSense D45 | 17.67 s | 531 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 95 | `SMR_20260626_P31_K_4e5316e1_raw.json` | SMR | SÍ (K) | P31 | PATIENT | Intel Intel RealSense D45 | 16.27 s | 489 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 96 | `SMR_20260626_P32_AQ_22f0ff21_raw.json` | SMR | SÍ (AQ) | P32 | PATIENT | Intel Intel RealSense D45 | 13.86 s | 417 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 97 | `SMR_20260626_P32_AZ_fbe58f01_raw.json` | SMR | SÍ (AZ) | P32 | PATIENT | Intel Intel RealSense D45 | 18.93 s | 569 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 98 | `SMR_20260626_P32_J_dabe0112_raw.json` | SMR | SÍ (J) | P32 | PATIENT | Intel Intel RealSense D45 | 13.83 s | 416 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 99 | `SMR_20260626_P33_BM_ed61ac9f_raw.json` | SMR | SÍ (BM) | P33 | PATIENT | Intel Intel RealSense D45 | 17.61 s | 529 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 100 | `SMR_20260626_P34_BS_87a49c65_raw.json` | SMR | SÍ (BS) | P34 | PATIENT | Intel Intel RealSense D45 | 24.21 s | 727 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 101 | `SMR_20260626_P35_AW_452eaaa1_raw.json` | SMR | SÍ (AW) | P35 | PATIENT | Intel Intel RealSense D45 | 28.55 s | 857 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 102 | `SMR_20260626_P36_AH_b622b020_raw.json` | SMR | SÍ (AH) | P36 | PATIENT | Intel Intel RealSense D45 | 16.6 s | 499 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 103 | `SMR_20260626_P37_AT_0dcde044_raw.json` | SMR | SÍ (AT) | P37 | PATIENT | Intel Intel RealSense D45 | 14.9 s | 448 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 104 | `SMR_20260626_P38_AE_80c945b3_raw.json` | SMR | SÍ (AE) | P38 | PATIENT | Intel Intel RealSense D45 | 13.8 s | 415 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 105 | `SMR_20260626_P39_BL_294c3933_raw.json` | SMR | SÍ (BL) | P39 | PATIENT | Intel Intel RealSense D45 | 16.2 s | 487 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 106 | `SMR_20260627_NO_IMU_170b8f66_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 14.7 s | 442 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 107 | `SMR_20260627_NO_IMU_23b44cf6_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 12.97 s | 390 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 108 | `SMR_20260627_NO_IMU_527a2c9d_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 14.71 s | 442 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 109 | `SMR_20260627_NO_IMU_77ff8380_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 23.14 s | 695 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 110 | `SMR_20260627_NO_IMU_7819c5a8_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 13.93 s | 419 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 111 | `SMR_20260627_NO_IMU_78cca52a_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 12.0 s | 361 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 112 | `SMR_20260627_NO_IMU_7b1024d0_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 14.14 s | 425 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 113 | `SMR_20260627_NO_IMU_8f7ae2b1_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 14.9 s | 448 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 114 | `SMR_20260627_NO_IMU_c3777a40_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 16.16 s | 486 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 115 | `SMR_20260627_NO_IMU_c425b54e_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 18.43 s | 554 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 116 | `SMR_20260627_NO_IMU_d9ea79f2_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 13.94 s | 419 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 117 | `SMR_20260627_NO_IMU_eb67e769_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 15.81 s | 475 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 118 | `SMR_20260627_NO_IMU_f2b0f18f_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 13.7 s | 412 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 119 | `SMR_20260627_NO_IMU_f86c7503_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 20.74 s | 623 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 120 | `SMR_20260627_NO_IMU_fb596b7d_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 13.33 s | 401 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 121 | `SMR_20260627_NO_IMU_fe7cfb72_raw.json` | SMR | NO | - | SIN_ETIQUETA | Intel Intel RealSense D45 | 12.77 s | 384 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 122 | `SMR_20260627_P40_AS_4df833f1_raw.json` | SMR | SÍ (AS) | P40 | PATIENT | Intel Intel RealSense D45 | 15.14 s | 455 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 123 | `SMR_20260627_P42_AD_25f298d4_raw.json` | SMR | SÍ (AD) | P42 | PATIENT | Intel Intel RealSense D45 | 21.47 s | 645 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 124 | `SMR_20260627_P43_BB_580b902a_raw.json` | SMR | SÍ (BB) | P43 | PATIENT | Intel Intel RealSense D45 | 14.37 s | 432 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 125 | `SMR_20260627_P44_R_89d757d6_raw.json` | SMR | SÍ (R) | P44 | PATIENT | Intel Intel RealSense D45 | 15.7 s | 472 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 126 | `SMR_20260627_P46_I_ba2c6e63_raw.json` | SMR | SÍ (I) | P46 | PATIENT | Intel Intel RealSense D45 | 12.47 s | 375 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 127 | `SMR_20260627_P47_Q_907121bd_raw.json` | SMR | SÍ (Q) | P47 | PATIENT | Intel Intel RealSense D45 | 13.7 s | 412 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 128 | `SMR_20260627_P48_AU_4781f6d7_raw.json` | SMR | SÍ (AU) | P48 | PATIENT | Intel Intel RealSense D45 | 12.63 s | 380 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 129 | `SMR_20260627_P49_L_6943624b_raw.json` | SMR | SÍ (L) | P49 | PATIENT | Intel Intel RealSense D45 | 18.77 s | 564 | 30.0 | Marcha 1 & 2 (Zancada/Velocidad) |
| 130 | `SMR_20260627_P50_H_d3efbdfa_raw.json` | SMR | SÍ (H) | P50 | PATIENT | Intel Intel RealSense D45 | 13.17 s | 396 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 131 | `SMR_20260627_P51_AI_18c58989_raw.json` | SMR | SÍ (AI) | P51 | PATIENT | Intel Intel RealSense D45 | 19.53 s | 587 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |
| 132 | `SMR_20260627_P52_C_029c450a_raw.json` | SMR | SÍ (C) | P52 | PATIENT | Intel Intel RealSense D45 | 14.97 s | 450 | 30.1 | Marcha 1 & 2 (Zancada/Velocidad) |

---

## 7. Resumen de Grabaciones de Marcha Continua (`No_TUG_Gait_Analysis/`, 137 Archivos)

El subconjunto de marcha continua alberga 137 registros dedicados al monitoreo de marcha lineal pura (10 metros en línea recta):

- **Total Capturas Santa Marta (`SMR_`):** 122 grabaciones de marcha.
- **Total Capturas CST / La Victoria (`CST_`):** 14 grabaciones (12 pruebas esqueléticas en formato Orbbec/Intel + 2 archivos de métricas comparativas precalculadas: `CST_20260704_METRICS_49196b62.json` y `CST_20260704_METRICS_fa5aaa78.json`).
- **Total Capturas Laboratorio (`LAB_`):** 1 grabación de validación técnica.
- **Duración Media:** 27.0 ± 14.8 segundos (Rango: 6.4 s a 146.5 s).
- **Frames Promedio:** 789.2 cuadros por toma.
- **Utilidad Biomecánica Primaria:** Caracterización de la longitud de zancada en marcha sostenida, cadencia media y velocidad media sin influencia de transiciones posturales.

| # | Archivo JSON | Brigada | Protocolo | Frames | Duración | Calidad Tracking | Observación |
|---:|---|:---:|:---:|:---:|:---:|:---:|---|
| 1 | `CST_20260704_METRICS_49196b62.json` | CST | METRICS_COMPARISON | 0 | 0.0 s | 100.0% | Marcha continua lineal validada |
| 2 | `CST_20260704_METRICS_fa5aaa78.json` | CST | METRICS_COMPARISON | 0 | 0.0 s | 100.0% | Marcha continua lineal validada |
| 3 | `CST_20260704_NO_IMU_6f6fd032_raw.json` | CST | GAIT_COMPLETE | 195 | 6.38 s | 87.6% | Marcha continua lineal validada |
| 4 | `CST_20260704_P53_AF_2337aee0_raw.json` | CST | GAIT_COMPLETE | 504 | 16.68 s | 87.2% | Marcha continua lineal validada |
| 5 | `CST_20260704_P55_E_dc68dbc6_raw.json` | CST | GAIT_COMPLETE | 376 | 12.5 s | 86.2% | Marcha continua lineal validada |
| 6 | `CST_20260704_P56_Y_081dd40b_raw.json` | CST | GAIT_COMPLETE | 526 | 17.4 s | 86.0% | Marcha continua lineal validada |
| 7 | `CST_20260704_P57_AY_d48689ef_raw.json` | CST | GAIT_COMPLETE | 543 | 18.15 s | 87.7% | Marcha continua lineal validada |
| 8 | `CST_20260704_P58_BG_c4300982_raw.json` | CST | GAIT_COMPLETE | 503 | 16.88 s | 85.5% | Marcha continua lineal validada |
| 9 | `CST_20260704_P59_B_a5f5f669_raw.json` | CST | GAIT_COMPLETE | 702 | 23.55 s | 87.7% | Marcha continua lineal validada |
| 10 | `CST_20260704_P60_AM_8fe2ed6b_raw.json` | CST | GAIT_COMPLETE | 537 | 17.81 s | 87.0% | Marcha continua lineal validada |
| 11 | `CST_20260704_P61_P_4f9d38a1_raw.json` | CST | GAIT_COMPLETE | 580 | 19.92 s | 88.4% | Marcha continua lineal validada |
| 12 | `CST_20260704_P62_BI_cb6b1535_raw.json` | CST | GAIT_COMPLETE | 547 | 18.25 s | 88.7% | Marcha continua lineal validada |
| 13 | `CST_20260704_P63_Z_773a51d3_raw.json` | CST | GAIT_COMPLETE | 775 | 25.93 s | 87.5% | Marcha continua lineal validada |
| 14 | `CST_20260704_P64_T_f31bbc49_raw.json` | CST | GAIT_COMPLETE | 545 | 18.13 s | 83.5% | Marcha continua lineal validada |
| 15 | `CST_20260704_P65_AN_91f0fb23_raw.json` | CST | GAIT_COMPLETE | 337 | 11.22 s | 84.4% | Marcha continua lineal validada |
| 16 | `SMR_20260625_NO_IMU_0e409a32_raw.json` | SMR | GAIT_COMPLETE | 1483 | 49.42 s | 94.7% | Marcha continua lineal validada |
| 17 | `SMR_20260625_NO_IMU_10ea6b0a_raw.json` | SMR | GAIT_COMPLETE | 249 | 9.58 s | 88.5% | Marcha continua lineal validada |
| 18 | `SMR_20260625_NO_IMU_1f3d9243_raw.json` | SMR | GAIT_COMPLETE | 673 | 22.62 s | 82.0% | Marcha continua lineal validada |
| 19 | `SMR_20260625_NO_IMU_395edfb9_raw.json` | SMR | GAIT_COMPLETE | 382 | 14.1 s | 82.5% | Marcha continua lineal validada |
| 20 | `SMR_20260625_NO_IMU_a08a083b_raw.json` | SMR | GAIT_COMPLETE | 549 | 18.21 s | 88.2% | Marcha continua lineal validada |
| 21 | `SMR_20260625_NO_IMU_a7bcca1d_raw.json` | SMR | GAIT_COMPLETE | 488 | 16.21 s | 87.0% | Marcha continua lineal validada |
| 22 | `SMR_20260625_NO_IMU_a9046855_raw.json` | SMR | GAIT_COMPLETE | 1460 | 48.65 s | 98.3% | Marcha continua lineal validada |
| 23 | `SMR_20260625_NO_IMU_c86c4bff_raw.json` | SMR | GAIT_COMPLETE | 1371 | 45.69 s | 97.1% | Marcha continua lineal validada |
| 24 | `SMR_20260625_NO_IMU_c8ce4ec2_raw.json` | SMR | GAIT_COMPLETE | 531 | 17.9 s | 85.5% | Marcha continua lineal validada |
| 25 | `SMR_20260625_NO_IMU_f8632d2f_raw.json` | SMR | GAIT_COMPLETE | 412 | 13.68 s | 86.2% | Marcha continua lineal validada |
| 26 | `SMR_20260625_P06_AR_7639eee3_raw.json` | SMR | GAIT_COMPLETE | 689 | 22.85 s | 85.7% | Marcha continua lineal validada |
| 27 | `SMR_20260625_P08_AB_4b2ab6b4_raw.json` | SMR | GAIT_COMPLETE | 455 | 15.39 s | 88.2% | Marcha continua lineal validada |
| 28 | `SMR_20260625_P09_AK_34480359_raw.json` | SMR | GAIT_COMPLETE | 529 | 17.59 s | 88.5% | Marcha continua lineal validada |
| 29 | `SMR_20260625_P10_AA_95436a8a_raw.json` | SMR | GAIT_COMPLETE | 624 | 20.78 s | 86.7% | Marcha continua lineal validada |
| 30 | `SMR_20260625_P12_A_92dcbfca_raw.json` | SMR | GAIT_COMPLETE | 552 | 18.24 s | 88.5% | Marcha continua lineal validada |
| 31 | `SMR_20260625_P13_BW_66c8ba46_raw.json` | SMR | GAIT_COMPLETE | 541 | 17.96 s | 87.5% | Marcha continua lineal validada |
| 32 | `SMR_20260625_P14_AG_e6bce349_raw.json` | SMR | GAIT_COMPLETE | 489 | 16.17 s | 82.5% | Marcha continua lineal validada |
| 33 | `SMR_20260625_P15_BK_f2d38bdb_raw.json` | SMR | GAIT_COMPLETE | 659 | 22.12 s | 85.5% | Marcha continua lineal validada |
| 34 | `SMR_20260625_P16_BD_3583831d_raw.json` | SMR | GAIT_COMPLETE | 836 | 27.75 s | 87.0% | Marcha continua lineal validada |
| 35 | `SMR_20260625_P18_BN_ed8cb966_raw.json` | SMR | GAIT_COMPLETE | 468 | 15.81 s | 85.7% | Marcha continua lineal validada |
| 36 | `SMR_20260625_P20_BH_11f23d05_raw.json` | SMR | GAIT_COMPLETE | 628 | 20.9 s | 88.5% | Marcha continua lineal validada |
| 37 | `SMR_20260625_P20_S_dde1028c_raw.json` | SMR | GAIT_COMPLETE | 1707 | 56.87 s | 88.6% | Marcha continua lineal validada |
| 38 | `SMR_20260625_P21_X_78bc1d98_raw.json` | SMR | GAIT_COMPLETE | 1608 | 53.59 s | 90.3% | Marcha continua lineal validada |
| 39 | `SMR_20260625_P22_BA_548926c5_raw.json` | SMR | GAIT_COMPLETE | 583 | 19.58 s | 83.2% | Marcha continua lineal validada |
| 40 | `SMR_20260626_NO_IMU_041d3765_raw.json` | SMR | GAIT_COMPLETE | 655 | 21.79 s | 89.0% | Marcha continua lineal validada |
| 41 | `SMR_20260626_NO_IMU_05b76765_raw.json` | SMR | GAIT_COMPLETE | 1633 | 54.42 s | 94.8% | Marcha continua lineal validada |
| 42 | `SMR_20260626_NO_IMU_0bb39bc0_raw.json` | SMR | GAIT_COMPLETE | 412 | 13.68 s | 86.2% | Marcha continua lineal validada |
| 43 | `SMR_20260626_NO_IMU_12e2ca22_raw.json` | SMR | GAIT_COMPLETE | 668 | 22.63 s | 86.2% | Marcha continua lineal validada |
| 44 | `SMR_20260626_NO_IMU_14fbacd4_raw.json` | SMR | GAIT_COMPLETE | 443 | 15.34 s | 86.7% | Marcha continua lineal validada |
| 45 | `SMR_20260626_NO_IMU_21a7e236_raw.json` | SMR | GAIT_COMPLETE | 310 | 10.5 s | 89.2% | Marcha continua lineal validada |
| 46 | `SMR_20260626_NO_IMU_22dd97ba_raw.json` | SMR | GAIT_COMPLETE | 529 | 17.59 s | 88.5% | Marcha continua lineal validada |
| 47 | `SMR_20260626_NO_IMU_2f19de60_raw.json` | SMR | GAIT_COMPLETE | 453 | 15.59 s | 89.0% | Marcha continua lineal validada |
| 48 | `SMR_20260626_NO_IMU_40364e38_raw.json` | SMR | GAIT_COMPLETE | 1637 | 54.56 s | 97.5% | Marcha continua lineal validada |
| 49 | `SMR_20260626_NO_IMU_4514952a_raw.json` | SMR | GAIT_COMPLETE | 836 | 27.85 s | 97.5% | Marcha continua lineal validada |
| 50 | `SMR_20260626_NO_IMU_48d3537f_raw.json` | SMR | GAIT_COMPLETE | 689 | 22.85 s | 85.7% | Marcha continua lineal validada |
| 51 | `SMR_20260626_NO_IMU_4a7c71c4_raw.json` | SMR | GAIT_COMPLETE | 538 | 18.46 s | 87.5% | Marcha continua lineal validada |
| 52 | `SMR_20260626_NO_IMU_4e8e3df8_raw.json` | SMR | GAIT_COMPLETE | 583 | 19.58 s | 83.2% | Marcha continua lineal validada |
| 53 | `SMR_20260626_NO_IMU_5d4b160b_raw.json` | SMR | GAIT_COMPLETE | 1623 | 54.09 s | 98.3% | Marcha continua lineal validada |
| 54 | `SMR_20260626_NO_IMU_609d5059_raw.json` | SMR | GAIT_COMPLETE | 396 | 13.17 s | 88.0% | Marcha continua lineal validada |
| 55 | `SMR_20260626_NO_IMU_7381b7e6_raw.json` | SMR | GAIT_COMPLETE | 541 | 17.96 s | 87.5% | Marcha continua lineal validada |
| 56 | `SMR_20260626_NO_IMU_855fa26d_raw.json` | SMR | GAIT_COMPLETE | 1804 | 60.13 s | 96.5% | Marcha continua lineal validada |
| 57 | `SMR_20260626_NO_IMU_866f499c_raw.json` | SMR | GAIT_COMPLETE | 455 | 15.39 s | 88.2% | Marcha continua lineal validada |
| 58 | `SMR_20260626_NO_IMU_8b76c66f_raw.json` | SMR | GAIT_COMPLETE | 504 | 17.23 s | 87.7% | Marcha continua lineal validada |
| 59 | `SMR_20260626_NO_IMU_8f13944e_raw.json` | SMR | GAIT_COMPLETE | 1120 | 37.32 s | 95.5% | Marcha continua lineal validada |
| 60 | `SMR_20260626_NO_IMU_92686d86_raw.json` | SMR | GAIT_COMPLETE | 514 | 17.47 s | 87.0% | Marcha continua lineal validada |
| 61 | `SMR_20260626_NO_IMU_95b50d47_raw.json` | SMR | GAIT_COMPLETE | 531 | 17.9 s | 85.5% | Marcha continua lineal validada |
| 62 | `SMR_20260626_NO_IMU_98184b25_raw.json` | SMR | GAIT_COMPLETE | 659 | 22.12 s | 85.5% | Marcha continua lineal validada |
| 63 | `SMR_20260626_NO_IMU_9a8d8781_raw.json` | SMR | GAIT_COMPLETE | 549 | 18.21 s | 88.2% | Marcha continua lineal validada |
| 64 | `SMR_20260626_NO_IMU_9d0680ef_raw.json` | SMR | GAIT_COMPLETE | 1957 | 146.48 s | 95.9% | Marcha continua lineal validada |
| 65 | `SMR_20260626_NO_IMU_a22cdc34_raw.json` | SMR | GAIT_COMPLETE | 644 | 21.7 s | 87.7% | Marcha continua lineal validada |
| 66 | `SMR_20260626_NO_IMU_ab67edea_raw.json` | SMR | GAIT_COMPLETE | 1255 | 41.8 s | 99.0% | Marcha continua lineal validada |
| 67 | `SMR_20260626_NO_IMU_ad4866d3_raw.json` | SMR | GAIT_COMPLETE | 1144 | 38.12 s | 96.5% | Marcha continua lineal validada |
| 68 | `SMR_20260626_NO_IMU_b052040a_raw.json` | SMR | GAIT_COMPLETE | 488 | 16.21 s | 87.0% | Marcha continua lineal validada |
| 69 | `SMR_20260626_NO_IMU_b152ceff_raw.json` | SMR | GAIT_COMPLETE | 1805 | 60.16 s | 94.4% | Marcha continua lineal validada |
| 70 | `SMR_20260626_NO_IMU_b2d46fa4_raw.json` | SMR | GAIT_COMPLETE | 468 | 15.81 s | 85.7% | Marcha continua lineal validada |
| 71 | `SMR_20260626_NO_IMU_b4a3f987_raw.json` | SMR | GAIT_COMPLETE | 685 | 22.93 s | 86.7% | Marcha continua lineal validada |
| 72 | `SMR_20260626_NO_IMU_b54cb03a_raw.json` | SMR | GAIT_COMPLETE | 483 | 16.57 s | 86.5% | Marcha continua lineal validada |
| 73 | `SMR_20260626_NO_IMU_b9296c26_raw.json` | SMR | GAIT_COMPLETE | 624 | 20.78 s | 86.7% | Marcha continua lineal validada |
| 74 | `SMR_20260626_NO_IMU_bbb60c6f_raw.json` | SMR | GAIT_COMPLETE | 628 | 20.9 s | 88.5% | Marcha continua lineal validada |
| 75 | `SMR_20260626_NO_IMU_bc15f52a_raw.json` | SMR | GAIT_COMPLETE | 483 | 16.57 s | 86.5% | Marcha continua lineal validada |
| 76 | `SMR_20260626_NO_IMU_bd4fcb3a_raw.json` | SMR | GAIT_COMPLETE | 1362 | 45.39 s | 97.0% | Marcha continua lineal validada |
| 77 | `SMR_20260626_NO_IMU_c293dc31_raw.json` | SMR | GAIT_COMPLETE | 1318 | 43.92 s | 95.1% | Marcha continua lineal validada |
| 78 | `SMR_20260626_NO_IMU_dce3bc73_raw.json` | SMR | GAIT_COMPLETE | 673 | 22.62 s | 82.0% | Marcha continua lineal validada |
| 79 | `SMR_20260626_NO_IMU_e0b89e59_raw.json` | SMR | GAIT_COMPLETE | 459 | 15.7 s | 86.2% | Marcha continua lineal validada |
| 80 | `SMR_20260626_NO_IMU_e998adc9_raw.json` | SMR | GAIT_COMPLETE | 310 | 10.5 s | 89.2% | Marcha continua lineal validada |
| 81 | `SMR_20260626_NO_IMU_ef1d26a2_raw.json` | SMR | GAIT_COMPLETE | 595 | 20.61 s | 87.0% | Marcha continua lineal validada |
| 82 | `SMR_20260626_NO_IMU_f18f1bb8_raw.json` | SMR | GAIT_COMPLETE | 552 | 18.24 s | 88.5% | Marcha continua lineal validada |
| 83 | `SMR_20260626_NO_IMU_fb9ec0a6_raw.json` | SMR | GAIT_COMPLETE | 489 | 16.17 s | 82.5% | Marcha continua lineal validada |
| 84 | `SMR_20260626_NO_IMU_ff12f3b9_raw.json` | SMR | GAIT_COMPLETE | 836 | 27.75 s | 87.0% | Marcha continua lineal validada |
| 85 | `SMR_20260626_P23_AC_5106035d_raw.json` | SMR | GAIT_COMPLETE | 655 | 21.79 s | 89.0% | Marcha continua lineal validada |
| 86 | `SMR_20260626_P24_AV_d57ba7a5_raw.json` | SMR | GAIT_COMPLETE | 1877 | 62.56 s | 93.7% | Marcha continua lineal validada |
| 87 | `SMR_20260626_P25_AO_fe8d3176_raw.json` | SMR | GAIT_COMPLETE | 1773 | 59.09 s | 95.7% | Marcha continua lineal validada |
| 88 | `SMR_20260626_P26_M_023b8c9b_raw.json` | SMR | GAIT_COMPLETE | 2199 | 73.28 s | 97.2% | Marcha continua lineal validada |
| 89 | `SMR_20260626_P27_BQ_a2fa578b_raw.json` | SMR | GAIT_COMPLETE | 595 | 20.61 s | 87.0% | Marcha continua lineal validada |
| 90 | `SMR_20260626_P28_U_3f8afb20_raw.json` | SMR | GAIT_COMPLETE | 396 | 13.17 s | 88.0% | Marcha continua lineal validada |
| 91 | `SMR_20260626_P29_AJ_c86d30f1_raw.json` | SMR | GAIT_COMPLETE | 685 | 22.93 s | 86.7% | Marcha continua lineal validada |
| 92 | `SMR_20260626_P30_O_e00dfee7_raw.json` | SMR | GAIT_COMPLETE | 644 | 21.7 s | 87.7% | Marcha continua lineal validada |
| 93 | `SMR_20260626_P31_BU_ebb1a945_raw.json` | SMR | GAIT_COMPLETE | 459 | 15.7 s | 86.2% | Marcha continua lineal validada |
| 94 | `SMR_20260626_P31_K_e7bf509c_raw.json` | SMR | GAIT_COMPLETE | 879 | 29.28 s | 97.6% | Marcha continua lineal validada |
| 95 | `SMR_20260626_P32_AZ_898d2089_raw.json` | SMR | GAIT_COMPLETE | 1484 | 49.46 s | 94.0% | Marcha continua lineal validada |
| 96 | `SMR_20260626_P32_BT_d6e7fbaa_raw.json` | SMR | GAIT_COMPLETE | 538 | 18.46 s | 87.5% | Marcha continua lineal validada |
| 97 | `SMR_20260626_P33_BM_00d7dc00_raw.json` | SMR | GAIT_COMPLETE | 668 | 22.63 s | 86.2% | Marcha continua lineal validada |
| 98 | `SMR_20260626_P34_BS_e5bc268a_raw.json` | SMR | GAIT_COMPLETE | 514 | 17.47 s | 87.0% | Marcha continua lineal validada |
| 99 | `SMR_20260626_P35_AW_6eff50a6_raw.json` | SMR | GAIT_COMPLETE | 1392 | 46.39 s | 96.5% | Marcha continua lineal validada |
| 100 | `SMR_20260626_P36_AH_8fc3f6de_raw.json` | SMR | GAIT_COMPLETE | 504 | 17.23 s | 87.7% | Marcha continua lineal validada |
| 101 | `SMR_20260626_P37_AT_ea1720a7_raw.json` | SMR | GAIT_COMPLETE | 443 | 15.34 s | 86.7% | Marcha continua lineal validada |
| 102 | `SMR_20260626_P38_AE_abea9085_raw.json` | SMR | GAIT_COMPLETE | 453 | 15.59 s | 89.0% | Marcha continua lineal validada |
| 103 | `SMR_20260626_P39_BL_cda48534_raw.json` | SMR | GAIT_COMPLETE | 1634 | 54.44 s | 96.2% | Marcha continua lineal validada |
| 104 | `SMR_20260627_NO_IMU_04c0f4f2_raw.json` | SMR | GAIT_COMPLETE | 487 | 16.08 s | 86.5% | Marcha continua lineal validada |
| 105 | `SMR_20260627_NO_IMU_12b50c3b_raw.json` | SMR | GAIT_COMPLETE | 709 | 23.34 s | 86.5% | Marcha continua lineal validada |
| 106 | `SMR_20260627_NO_IMU_1b893ca6_raw.json` | SMR | GAIT_COMPLETE | 1115 | 37.15 s | 94.8% | Marcha continua lineal validada |
| 107 | `SMR_20260627_NO_IMU_1d67416b_raw.json` | SMR | GAIT_COMPLETE | 1007 | 33.55 s | 93.4% | Marcha continua lineal validada |
| 108 | `SMR_20260627_NO_IMU_266bbad9_raw.json` | SMR | GAIT_COMPLETE | 1244 | 41.45 s | 91.7% | Marcha continua lineal validada |
| 109 | `SMR_20260627_NO_IMU_2a3e0319_raw.json` | SMR | GAIT_COMPLETE | 370 | 12.19 s | 87.2% | Marcha continua lineal validada |
| 110 | `SMR_20260627_NO_IMU_37dd5945_raw.json` | SMR | GAIT_COMPLETE | 1147 | 38.22 s | 96.7% | Marcha continua lineal validada |
| 111 | `SMR_20260627_NO_IMU_4110d539_raw.json` | SMR | GAIT_COMPLETE | 594 | 19.67 s | 87.2% | Marcha continua lineal validada |
| 112 | `SMR_20260627_NO_IMU_42228267_raw.json` | SMR | GAIT_COMPLETE | 719 | 24.0 s | 86.7% | Marcha continua lineal validada |
| 113 | `SMR_20260627_NO_IMU_5364306d_raw.json` | SMR | GAIT_COMPLETE | 1865 | 62.16 s | 90.4% | Marcha continua lineal validada |
| 114 | `SMR_20260627_NO_IMU_597e52ed_raw.json` | SMR | GAIT_COMPLETE | 655 | 21.99 s | 87.7% | Marcha continua lineal validada |
| 115 | `SMR_20260627_NO_IMU_59db65ca_raw.json` | SMR | GAIT_COMPLETE | 390 | 12.98 s | 86.2% | Marcha continua lineal validada |
| 116 | `SMR_20260627_NO_IMU_925eff62_raw.json` | SMR | GAIT_COMPLETE | 1172 | 39.03 s | 96.9% | Marcha continua lineal validada |
| 117 | `SMR_20260627_NO_IMU_92899a60_raw.json` | SMR | GAIT_COMPLETE | 370 | 12.19 s | 87.2% | Marcha continua lineal validada |
| 118 | `SMR_20260627_NO_IMU_b475e9fe_raw.json` | SMR | GAIT_COMPLETE | 655 | 21.8 s | 100.0% | Marcha continua lineal validada |
| 119 | `SMR_20260627_NO_IMU_c1a682ac_raw.json` | SMR | GAIT_COMPLETE | 1942 | 64.73 s | 96.0% | Marcha continua lineal validada |
| 120 | `SMR_20260627_NO_IMU_c5a03517_raw.json` | SMR | GAIT_COMPLETE | 556 | 18.49 s | 85.7% | Marcha continua lineal validada |
| 121 | `SMR_20260627_NO_IMU_de8fac34_raw.json` | SMR | GAIT_COMPLETE | 719 | 24.0 s | 86.7% | Marcha continua lineal validada |
| 122 | `SMR_20260627_NO_IMU_df97753c_raw.json` | SMR | GAIT_COMPLETE | 412 | 13.73 s | 85.5% | Marcha continua lineal validada |
| 123 | `SMR_20260627_NO_IMU_e27a033e_raw.json` | SMR | GAIT_COMPLETE | 2026 | 67.53 s | 93.4% | Marcha continua lineal validada |
| 124 | `SMR_20260627_NO_IMU_e7696b05_raw.json` | SMR | GAIT_COMPLETE | 1432 | 47.72 s | 97.1% | Marcha continua lineal validada |
| 125 | `SMR_20260627_NO_IMU_e80df38f_raw.json` | SMR | GAIT_COMPLETE | 1101 | 36.68 s | 96.6% | Marcha continua lineal validada |
| 126 | `SMR_20260627_NO_IMU_ea337c30_raw.json` | SMR | GAIT_COMPLETE | 390 | 12.98 s | 86.2% | Marcha continua lineal validada |
| 127 | `SMR_20260627_P40_AS_a5b26747_raw.json` | SMR | GAIT_COMPLETE | 709 | 23.34 s | 86.5% | Marcha continua lineal validada |
| 128 | `SMR_20260627_P41_BP_adb07dac_raw.json` | SMR | GAIT_COMPLETE | 594 | 19.67 s | 87.2% | Marcha continua lineal validada |
| 129 | `SMR_20260627_P42_AD_537cd466_raw.json` | SMR | GAIT_COMPLETE | 487 | 16.08 s | 86.5% | Marcha continua lineal validada |
| 130 | `SMR_20260627_P43_BB_3ee0ecde_raw.json` | SMR | GAIT_COMPLETE | 1790 | 59.66 s | 94.0% | Marcha continua lineal validada |
| 131 | `SMR_20260627_P44_R_f6f2191f_raw.json` | SMR | GAIT_COMPLETE | 1203 | 40.07 s | 96.4% | Marcha continua lineal validada |
| 132 | `SMR_20260627_P45_W_c5eaec1e_raw.json` | SMR | GAIT_COMPLETE | 556 | 18.49 s | 85.7% | Marcha continua lineal validada |
| 133 | `SMR_20260627_P46_I_ed550cc5_raw.json` | SMR | GAIT_COMPLETE | 412 | 13.73 s | 85.5% | Marcha continua lineal validada |
| 134 | `SMR_20260627_P47_Q_120c1be5_raw.json` | SMR | GAIT_COMPLETE | 455 | 15.33 s | 87.7% | Marcha continua lineal validada |
| 135 | `SMR_20260627_P48_AU_04316299_raw.json` | SMR | GAIT_COMPLETE | 455 | 15.33 s | 87.7% | Marcha continua lineal validada |
| 136 | `SMR_20260627_P49_L_e0bbd4e9_raw.json` | SMR | GAIT_COMPLETE | 655 | 21.99 s | 87.7% | Marcha continua lineal validada |
| 137 | `SMR_20260627_P52_C_b020da75_raw.json` | SMR | GAIT_COMPLETE | 379 | 13.0 s | 87.6% | Marcha continua lineal validada |

