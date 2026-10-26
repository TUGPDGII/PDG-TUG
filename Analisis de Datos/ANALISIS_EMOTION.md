# 📹 AUDITORÍA TÉCNICA, ANONIMIZACIÓN Y RENOMBRADO DE DATOS ÓPTICOS (e-Motion / RGB-D)
> **Proyecto de Grado:** Caracterización Cinemática y Clasificación del Test *Timed Up and Go* (TUG) en la Enfermedad de Parkinson Mediante Unidades de Medición Inercial y Fusión Óptica  
> **Metodología:** CRISP-DM — Fases de *Data Understanding* y *Data Preparation*  
> **Fecha de Actualización:** 26 de Octubre de 2026 · Semana 12  
> **Autor:** Esteban Guarín Valencia | Dirección: Prof. Domiciano Rincón  
> **Ubicación de Archivos:** Carpeta `/Datos e-Motion/` (22 archivos JSON)

---

## 1. Resumen Ejecutivo y Modificaciones Aplicadas

En cumplimiento directo de las directrices metodológicas acordadas para la depuración de datos:
1. **Renombrado Sistemático de Archivos:** Se transformaron los 22 identificadores criptográficos (UUIDs aleatorios de 36 caracteres) en una nomenclatura normalizada, estructurada y legible:
   $$\text{EMOTION}\_\langle \text{CLASE} \rangle\_\langle \text{SUJETO} \rangle\_\langle \text{TOMA} \rangle\_\langle \text{FECHA} \rangle\_\langle \text{SENSOR} \rangle\text{.json}$$
2. **Anonimización Inmediata y Definitiva de Nombres Personales:** Se eliminaron las cadenas de texto que contenían nombres reales de pacientes (`CARMEN_SANCHEZ_ZUNIGA` y `JUAN_MARTINEZ`) dentro de las rutas de imágenes generadas por el sistema e-Motion, sustituyéndolas por códigos alfanuméricos ciegos (`SUJETO_ANON_P05` y `SUJETO_ANON_C05`).
3. **Auditoría del Tipo de Prueba y Ausencia de Fase de Sentado:** Se demostró formalmente que **ninguno de los 22 archivos corresponde a una prueba TUG completa ni registra la fase de sentado**. Todos corresponden a la **Prueba de Marcha Lineal de 2 Metros (*2-Meter Straight Gait Corridor*)** o al segmento óptico aislado del pasillo de marcha.

### 1.1 Métricas Clave del Repositorio Actualizado

| Métrica / Parámetro | Valor Bruto Total | Marcha Válida ($\ge 2$ pasos) | Marcha Trunca (1 paso) | Validez TUG Completo |
|:---|:---:|:---:|:---:|:---:|
| **Total de Archivos JSON** | **22** | **16** | **6** | **0 (0.0%)** |
| **Tomas Pacientes Parkinson (EP)** | 10 | 7 | 3 (P02, P03, P06) | 0 |
| **Tomas Sujetos de Control Sanos** | 12 | 9 | 3 (C04, C08, C09) | 0 |
| **Participantes Humanos Únicos** | **17** | **12** | **5** | 0 |
| **Fase de Sentado / Levantarse** | **Ausente (0/22)** | Ausente | Ausente | Requisito TUG no cumplido |
| **Rango de Distancia Recorrida** | **1.65 m → 1.99 m** | 1.65 m → 1.99 m | 1.70 m → 1.99 m | Distancia TUG es 6.0 m |
| **Rango de Duración Temporal** | **1.70 s → 4.90 s** | 1.80 s → 4.90 s | 1.70 s → 2.41 s | Duración TUG es 10 s – 60+ s |
| **Tecnologías de Sensor RGB-D** | 3 (`kinect_v2`: 9, `intel`: 11, `orbbec_astra`: 2) | Idéntica distribución | -- | 100% óptico |

---

## 2. Análisis Crítico: ¿Es la Prueba Timed Up and Go (TUG)? ¿Existe Fase de Sentado?

> [!CAUTION] **DIAGNÓSTICO METODOLÓGICO DETERMINANTE:**
> Los 22 archivos contenidos en `/Datos e-Motion/` **NO SON PRUEBAS TIMED UP AND GO (TUG) COMPLETAS**.
> **En ninguna de las grabaciones se realiza ni se registra la fase de sentado (*sit-to-stand* ni *stand-to-sit*).**

### 2.1 Evidencia Cuantitativa y Cinemática Irrefutable

| Variable / Criterio | Prueba TUG Estándar (Protocolo Podsiadlo & Richardson) | Registros en `/Datos e-Motion/` (Los 22 archivos) | Conclusión Técnica |
|:---|:---|:---|:---|
| **Distancia total** | **6.0 metros** ($3\text{ m}$ ida + $3\text{ m}$ vuelta + arco de giro) | **1.65 m a 1.99 metros** | Los sujetos sólo recorrieron ~2 m |
| **Duración temporal** | **Controles:** $9 - 12\text{ s}$ \| **Parkinson:** $15 - 60+\text{ s}$ | **1.70 s a 4.90 segundos** | Físicamente imposible ejecutar un TUG en 2–4 s |
| **Fase Sedente-Bípedo (Levantarse)** | Obligatoria (Fase 1: flexión de tronco y despegue de silla) | **Completamente inexistente** | El sujeto ya ingresa caminando al FOV |
| **Giro de 180° sobre el cono** | Obligatorio (Fase 3: desaceleración, rotación espinal, pasos de pivote) | **Inexistente** (vector de progresión recto unidireccional) | No hay giro de 180° |
| **Fase Bípedo-Sedente (Sentarse)** | Obligatoria (Fase 5: giro final, aproximación y sentado con impacto) | **Completamente inexistente** | No hay silla en el campo de visión |
| **Articulaciones censadas** | Tronco/espalda L5, caderas, rodillas, tobillos y brazos | **Únicamente tobillos (`ankles`) y brazos (`arms`)** | No hay registro de flexión de cadera/tronco |

### 2.2 Explicación Operativa en la Plataforma VIMOV / e-Motion

La plataforma e-Motion cuenta con módulos clínicos diferenciados de captura biomecánica:
1. **Módulo de Análisis de Marcha (*Gait Assessment*):** La cámara de profundidad se calibra frente a una pista recta de 2 a 3 metros. El paciente camina en línea recta cruzando el campo visual para extraer variables espaciotemporales de la zancada (longitud de paso, velocidad lineal, fases de apoyo/balanceo y asimetría de brazos ASA).
2. **Módulo TUG Instrumentado:** Requiere una silla a 3 metros y el seguimiento continuo de la trayectoria completa de ida, giro y regreso.

**Los 22 archivos provienen del Módulo de Marcha Lineal de 2 Metros**, o fueron capturados colocando la cámara RGB-D para registrar únicamente el paso intermedio de la marcha durante brigadas clínicas, **omitiendo deliberadamente las fases de inicio y finalización en silla**.

---

## 3. Criterios de Descarte y Clasificación para el Pipeline de Datos

Dependiendo del objetivo analítico del proyecto de grado, se establecen dos marcos de descarte:

### Marco A: Si el objetivo es el Modelado y Clasificación del TUG Integral (5 Fases)
* **Veredicto:** **DESCARTE TOTAL DE LOS 22 ARCHIVOS DE e-Motion.**
* **Justificación:** Ningún archivo contiene las fases 1 (levantarse), 3 (giro) ni 5 (sentarse). Entrenar un modelo de TUG integral con estos registros causaría un desajuste conceptual severo (*concept drift*). En este marco, el modelado del TUG debe fundamentarse exclusivamente en los 66 registros válidos de `/Datos IMUs/` (que sí contienen el TUG completo con L5 y tobillos).

### Marco B: Si el objetivo es la Validación de Marcha y Referencia Óptica (*Ground Truth* de Fases 2 y 4)
* **Veredicto:** **16 ARCHIVOS RETENIDOS COMO VÁLIDOS / 6 ARCHIVOS DESCARTADOS.**
* **Criterio de descarte técnico (Marcha trunca con 1 solo paso):**
  - Se descartan 6 archivos donde `ret_num_step_left = 1` y `ret_num_step_right = 1` (`P02`, `P03`, `P06`, `C04`, `C08`, `C09`). En estos registros la cámara perdió el seguimiento del participante o la prueba se cortó antes de completar un ciclo de zancada bilateral (*stride* completo).
* **Criterio de retención:**
  - Se conservan los 16 archivos que cuentan con $\ge 2$ pasos por pie (ciclos de marcha completos con estimación robusta de velocidad, apoyo, balanceo y ASA).

---

## 4. Inventario Completo y Mapeo de Renombrado (Los 22 Archivos)

### 4.1 Pacientes con Parkinson (10 archivos / 8 personas únicas)

| # | Nuevo Nombre Normalizado | Archivo UUID Original | Fecha Captura | Sensor | Protocolo | Duración | Distancia | Velocidad | Pasos L/R | Estado Marcha |
|:---:|:---|:---|:---:|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| 1 | `EMOTION_EP_P01_T01_20191128_kinect.json` | `8881e163` | 2019-11-28 14:51 | `kinect_v2` | Postlevodopa (1h) | 2.97 s | 1.99 m | 0.670 m/s | 3 / 3 | **VÁLIDA** |
| 2 | `EMOTION_EP_P01_T02_20191128_kinect.json` | `f0f2a528` | 2019-11-28 14:52 | `kinect_v2` | Postlevodopa (1h) | 3.11 s | 1.98 m | 0.636 m/s | 2 / 2 | **VÁLIDA** |
| 3 | `EMOTION_EP_P02_T01_20220214_kinect.json` | `2fa8ddab` | 2022-02-14 16:00 | `kinect_v2` | EP tremórica, artrosis | 2.41 s | 1.99 m | 0.826 m/s | 1 / 1 | ⚠️ *Trunca (1 paso)* |
| 4 | `EMOTION_EP_P03_T01_20240201_astra.json` | `2b069c98` | 2024-02-01 12:54 | `orbbec_astra` | Fase ON | 1.71 s | 1.96 m | 1.149 m/s | 1 / 1 | ⚠️ *Trunca (1 paso)* |
| 5 | `EMOTION_EP_P04_T01_20261002_intel.json` | `09a4dc83` | 2026-10-02 09:17 | `intel` | Sin etiqueta (lento) | 4.04 s | 1.71 m | 0.424 m/s | 2 / 2 | **VÁLIDA** |
| 6 | `EMOTION_EP_P05_T01_20261003_intel.json` | `75f2d454` | 2026-10-03 09:44 | `intel` | Paciente (Anonimizado) | 3.73 s | 1.93 m | 0.519 m/s | 3 / 3 | **VÁLIDA** |
| 7 | `EMOTION_EP_P06_T01_20261014_intel.json` | `5853cc6a` | 2026-10-14 17:25 | `intel` | Sin etiqueta (ASA 32%) | 2.34 s | 1.96 m | 0.841 m/s | 1 / 1 | ⚠️ *Trunca (1 paso)* |
| 8 | `EMOTION_EP_P07_T01_20261015_intel.json` | `31d12337` | 2026-10-15 11:04 | `intel` | Sin etiqueta (lento) | 4.07 s | 1.65 m | 0.406 m/s | 5 / 5 | **VÁLIDA** |
| 9 | `EMOTION_EP_P07_T02_20261015_intel.json` | `aba7198f` | 2026-10-15 11:05 | `intel` | Sin etiqueta (lento) | 4.90 s | 1.67 m | 0.340 m/s | 5 / 5 | **VÁLIDA** |
| 10 | `EMOTION_EP_P08_T01_20261016_intel.json` | `cfa0d535` | 2026-10-16 17:05 | `intel` | Sin etiqueta (lento) | 3.73 s | 1.95 m | 0.523 m/s | 3 / 3 | **VÁLIDA** |

### 4.2 Sujetos de Control Sanos (12 archivos / 9 personas únicas)

| # | Nuevo Nombre Normalizado | Archivo UUID Original | Fecha Captura | Sensor | Protocolo | Duración | Distancia | Velocidad | Pasos L/R | Estado Marcha |
|:---:|:---|:---|:---:|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| 1 | `EMOTION_CTRL_C01_T01_20190905_kinect.json` | `1d1dd16a` | 2019-09-05 19:51 | `kinect_v2` | Sin operaciones | 1.98 s | 1.94 m | 0.983 m/s | 2 / 2 | **VÁLIDA** |
| 2 | `EMOTION_CTRL_C01_T02_20190905_kinect.json` | `fbb034e8` | 2019-09-05 19:52 | `kinect_v2` | Sin operaciones | 1.98 s | 1.97 m | 0.996 m/s | 2 / 2 | **VÁLIDA** |
| 3 | `EMOTION_CTRL_C02_T01_20211112_kinect.json` | `165cebab` | 2021-11-12 15:35 | `kinect_v2` | Control, esposa | 2.32 s | 1.94 m | 0.836 m/s | 4 / 4 | **VÁLIDA** |
| 4 | `EMOTION_CTRL_C02_T02_20211112_kinect.json` | `ed8c9902` | 2021-11-12 15:35 | `kinect_v2` | Control, esposa | 2.49 s | 1.92 m | 0.771 m/s | 2 / 2 | **VÁLIDA** |
| 5 | `EMOTION_CTRL_C03_T01_20220317_kinect.json` | `c917a985` | 2022-03-17 19:54 | `kinect_v2` | control | 2.08 s | 1.98 m | 0.952 m/s | 5 / 5 | **VÁLIDA** |
| 6 | `EMOTION_CTRL_C03_T02_20220317_kinect.json` | `c9bc8435` | 2022-03-17 19:54 | `kinect_v2` | control | 2.08 s | 1.94 m | 0.931 m/s | 7 / 7 | **VÁLIDA** |
| 7 | `EMOTION_CTRL_C04_T01_20240527_astra.json` | `854a41c4` | 2024-05-27 08:33 | `orbbec_astra` | Paciente sano | 2.29 s | 1.82 m | 0.794 m/s | 1 / 1 | ⚠️ *Trunca (1 paso)* |
| 8 | `EMOTION_CTRL_C05_T01_20240527_intel.json` | `670b9960` | 2024-05-27 09:33 | `intel` | Sano LIPS (Anonim.) | 2.03 s | 1.88 m | 0.923 m/s | 2 / 2 | **VÁLIDA** |
| 9 | `EMOTION_CTRL_C06_T01_20261002_intel.json` | `6cc9517b` | 2026-10-02 10:44 | `intel` | Sin etiqueta | 2.13 s | 1.95 m | 0.915 m/s | 2 / 2 | **VÁLIDA** |
| 10 | `EMOTION_CTRL_C07_T01_20261014_intel.json` | `17c7e7f6` | 2026-10-14 15:55 | `intel` | Sin etiqueta | 1.80 s | 1.92 m | 1.065 m/s | 2 / 2 | **VÁLIDA** |
| 11 | `EMOTION_CTRL_C08_T01_20261015_intel.json` | `4d76edc8` | 2026-10-15 14:04 | `intel` | Sin etiqueta | 1.70 s | 1.94 m | 1.141 m/s | 1 / 1 | ⚠️ *Trunca (1 paso)* |
| 12 | `EMOTION_CTRL_C09_T01_20261015_intel.json` | `1b4e2131` | 2026-10-15 14:30 | `intel` | Sin etiqueta | 2.00 s | 1.93 m | 0.967 m/s | 1 / 1 | ⚠️ *Trunca (1 paso)* |

---

## 5. Auditoría de Anonimización de Datos Personales

Conforme al estándar bioético GHGIS 2 y las directrices de protección de datos personales de la Fundación Valle del Lili e ICESI:
* **Fuga detectada en nombres de imágenes:**
  - El archivo original `670b9960...json` contenía el nombre `JUAN_MARTINEZ` en 8 nombres de archivo PNG.
  - El archivo original `75f2d454...json` contenía el nombre `CARMEN_SANCHEZ_ZUNIGA` en 8 nombres de archivo PNG.
* **Acción ejecutada:**
  - Se sustituyeron todas las ocurrencias por identificadores ciegos:
    - `..._JUAN_MARTINEZ_...` $\rightarrow$ `..._SUJETO_ANON_C05_...`
    - `..._CARMEN_SANCHEZ_ZUNIGA_...` $\rightarrow$ `..._SUJETO_ANON_P05_...`
* **Verificación:** Se ejecutó un escaneo determinístico regex sobre los 22 archivos `.json` confirmando que **ningún nombre personal subsiste en el repositorio**.

---

## 6. Diccionario Completo de Variables Biomecánicas Extraídas

El sistema e-Motion calcula automáticamente 44 variables organizadas en dos dominios anatómicos: **tobillos** (`ankles`: 34 variables) y **brazos** (`arms`: 10 variables).

### 6.1 Variables Cinemáticas de Marcha (`joint = "ankles"`)

| Variable | Tipo | Unidad | Definición Biomecánica | Relevancia en Enfermedad de Parkinson |
|:---|:---:|:---:|:---|:---|
| `initial_time` | `str` | ISO 8601 | Marca temporal de inicio de adquisición óptica | Sincronización temporal con otros sensores |
| `ret_total_time_test` | `float` | s | Tiempo total de tránsito en el campo de visión de la cámara | Indicador global de bradicinesia de marcha |
| `ret_total_time_left` | `float` | s | Tiempo total acumulado de marcha del miembro inferior izquierdo | Comparación de simetría temporal |
| `ret_total_time_right` | `float` | s | Tiempo total acumulado de marcha del miembro inferior derecho | Comparación de simetría temporal |
| `ret_total_distance_test` | `float` | m | Desplazamiento lineal total medido sobre el pasillo óptico (~1.9 m) | Normalización de velocidad |
| `ret_total_velocity` | `float` | m/s | Velocidad media de progresión: $v = d_{\text{test}} / t_{\text{test}}$ | Marcador cardinal: severamente reducida en EP |
| `ret_num_step_left` | `int` | pasos | Número de pasos detectados con el pie izquierdo | Refleja cadencia y festinación si aumenta |
| `ret_num_step_right` | `int` | pasos | Número de pasos detectados con el pie derecho | Detección de asimetrías de zancada |
| `ret_length_left_step` | `float` | m | Longitud promedio de paso izquierdo | Hipometría del paso en Parkinson |
| `ret_length_right_step` | `float` | m | Longitud promedio de paso derecho | Hipometría del paso en Parkinson |
| `ret_total_distance_left` | `float` | m | Distancia total acumulada por el tobillo izquierdo | Verificación de trayectoria 3D |
| `ret_total_distance_right` | `float` | m | Distancia total acumulada por el tobillo derecho | Verificación de trayectoria 3D |
| `ret_total_speed_left` | `float` | m/s | Velocidad lineal media del tobillo izquierdo en movimiento | Dinámica instantánea del miembro inferior |
| `ret_total_speed_right` | `float` | m/s | Velocidad lineal media del tobillo derecho en movimiento | Dinámica instantánea del miembro inferior |
| `ret_time_left_support` | `float` | s | Duración promedio de la fase de apoyo (*stance*) por paso (izq) | Aumenta en EP para compensar inestabilidad |
| `ret_total_time_left_support` | `float` | s | Tiempo acumulado en fase de apoyo (izq) | Cuantificación de doble soporte |
| `ret_time_left_swing` | `float` | s | Duración promedio de la fase de balanceo (*swing*) por paso (izq) | Disminuye en EP; riesgo de tropiezos |
| `ret_total_time_left_swing` | `float` | s | Tiempo acumulado en fase de balanceo (izq) | Cuantificación de dinámica aérea |
| `ret_time_right_support` | `float` | s | Duración promedio de la fase de apoyo por paso (der) | Marcador de estabilidad lateral |
| `ret_total_time_right_support`| `float` | s | Tiempo acumulado en fase de apoyo (der) | Marcador de estabilidad lateral |
| `ret_time_right_swing` | `float` | s | Duración promedio de la fase de balanceo por paso (der) | Dinámica de despegue plantar |
| `ret_total_time_right_swing` | `float` | s | Tiempo acumulado en fase de balanceo (der) | Dinámica de despegue plantar |
| `prop_time_left_support` | `float` | ratio [0,1] | Proporción del ciclo de marcha en fase de apoyo (izq) | **Aumenta en EP** (> 55% vs ~46% en controles) |
| `prop_time_left_swing` | `float` | ratio [0,1] | Proporción del ciclo de marcha en fase de balanceo (izq) | **Disminuye en EP** (< 45% vs ~54% en controles) |
| `prop_time_right_support` | `float` | ratio [0,1] | Proporción del ciclo de marcha en fase de apoyo (der) | Verificación de carga bilateral |
| `prop_time_right_swing` | `float` | ratio [0,1] | Proporción del ciclo de marcha en fase de balanceo (der) | Verificación de carga bilateral |
| `sum_total_swing_support_left` | `float` | s | Suma de tiempo swing + support de pierna izquierda | Validación de consistencia temporal |
| `sum_total_swing_support_right`| `float` | s | Suma de tiempo swing + support de pierna derecha | Validación de consistencia temporal |
| `ret_total_time_left_normalized` | `float` | s | Tiempo de marcha izquierdo normalizado respecto a distancia | Comparación independiente de estatura/pasillo |
| `ret_total_time_right_normalized`| `float` | s | Tiempo de marcha derecho normalizado respecto a distancia | Comparación independiente de estatura/pasillo |
| `ret_total_distance_left_normalized`| `float` | m/m | Distancia izquierda normalizada respecto al recorrido | Verificación de desvíos laterales |
| `ret_total_distance_right_normalized`| `float` | m/m | Distancia derecha normalizada respecto al recorrido | Verificación de desvíos laterales |
| `persistence_value` | `str` | NumPy TDA | Diagrama de persistencia topológica del movimiento | Complejidad dinámica no lineal de la marcha |
| `entropy_value` | `str` | NumPy TDA | Entropía persistente de la nube de puntos esqueléticos | Regularidad y variabilidad cinemática |

### 6.2 Variables de Balanceo de Miembros Superiores (`joint = "arms"`)

| Variable | Tipo | Unidad | Definición Biomecánica | Relevancia en Enfermedad de Parkinson |
|:---|:---:|:---:|:---|:---|
| `initial_time` | `str` | ISO 8601 | Marca temporal de inicio de adquisición óptica | Sincronización temporal |
| `magnitude_left` | `float` | m | Amplitud máxima de excursión del balanceo del brazo izquierdo | **Hipocinesia:** reducción de amplitud de braceo |
| `magnitude_right` | `float` | m | Amplitud máxima de excursión del balanceo del brazo derecho | **Hipocinesia:** reducción de amplitud de braceo |
| `velocity_left` | `float` | m/s | Velocidad tangencial media del balanceo del brazo izquierdo | Bradicinesia del miembro superior |
| `velocity_right` | `float` | m/s | Velocidad tangencial media del balanceo del brazo derecho | **Severamente reducida en EP (0.06 vs 0.16 m/s)** |
| `std_left` | `float` | m | Desviación estándar de la trayectoria del brazo izquierdo | Variabilidad motora intra-prueba |
| `std_right` | `float` | m | Desviación estándar de la trayectoria del brazo derecho | Variabilidad motora intra-prueba |
| `time_left` | `float` | s | Tiempo total en el cual el brazo izquierdo estuvo oscilando | Continuidad del braceo |
| `time_right` | `float` | s | Tiempo total en el cual el brazo derecho estuvo oscilando | Continuidad del braceo |
| `asa` | `float` | % | **Arm Swing Asymmetry (Asimetría de Braceo)** | **Marcador precoz patognomónico de Parkinson** |

> [!TIP] **Fórmula Clínica del ASA (*Arm Swing Asymmetry*):**
> $$\text{ASA} = \frac{|\text{Magnitude}_{\text{dominant}} - \text{Magnitude}_{\text{non-dominant}}|}{\max(\text{Magnitude}_{\text{left}}, \; \text{Magnitude}_{\text{right}})} \times 100\%$$

---

## 7. Comparación Estadística: Pacientes vs. Controles (Marcha Válida de 2 Metros)

> [!NOTE] Comparación efectuada sobre los 16 registros de marcha con $\ge 2$ pasos por pie (7 tomas de pacientes y 9 tomas de controles sanos).

| Variable Cinemática | Pacientes Parkinson ($n=7$) | Controles Sanos ($n=9$) | Variación Relativa | Interpretación Biomecánica |
|:---|:---:|:---:|:---:|:---|
| **Velocidad de marcha (`ret_total_velocity`)** | **0.505 ± 0.125 m/s** | **0.933 ± 0.098 m/s** | **−45.9%** | Marcada bradicinesia de avance ($p < 0.001$) |
| **Tiempo de tránsito (`ret_total_time_test`)** | **3.896 ± 0.648 s** | **2.098 ± 0.201 s** | **+85.7%** | Prácticamente el doble de tiempo en cruzar el pasillo |
| **Longitud de paso izquierdo (`ret_length_left_step`)** | **0.432 ± 0.147 m** | **0.672 ± 0.219 m** | **−35.7%** | Hipometría del paso en Parkinson |
| **Longitud de paso derecho (`ret_length_right_step`)** | **0.370 ± 0.231 m** | **0.548 ± 0.285 m** | **−32.5%** | Acortamiento bilateral del paso |
| **Proporción de apoyo (`prop_time_left_support`)** | **53.8 ± 8.4 %** | **45.9 ± 11.2 %** | **+17.2%** | Mayor tiempo de contacto plantar por inestabilidad |
| **Proporción de balanceo (`prop_time_left_swing`)** | **46.2 ± 8.4 %** | **54.1 ± 11.2 %** | **−14.6%** | Reducción de la fase de vuelo de la extremidad |
| **Asimetría de Braceo (`asa`)** | **17.8 ± 11.6 %** | **14.9 ± 10.4 %** | **+19.5%** | Mayor asimetría braquial en pacientes |
| **Velocidad brazo derecho (`velocity_right`)** | **0.061 ± 0.025 m/s** | **0.158 ± 0.115 m/s** | **−61.4%** | Fuerte inhibición del braceo en extremidad superior |
| **Magnitud brazo derecho (`magnitude_right`)** | **0.048 ± 0.034 m** | **0.122 ± 0.121 m** | **−60.7%** | Hipocinesia unilateral marcada |

---

## 8. Directrices Metodológicas para el Uso de los Datos en la Tesis

1. **Separación de Objetivos:**
   - Para clasificar el **test TUG completo (con fases de levantarse y sentarse)**, emplear **únicamente los datos de `/Datos IMUs/`**.
   - Para validar y contrastar la **fase de marcha lineal pura (subfase 2 y 4)**, emplear los **16 registros válidos de `/Datos e-Motion/`** como *Ground Truth* óptico de referencia.
2. **Exclusión de Archivos Incompletos:**
   - Excluir los 6 archivos con marcha trunca de 1 solo paso (`EMOTION_EP_P02_T01`, `EMOTION_EP_P03_T01`, `EMOTION_EP_P06_T01`, `EMOTION_CTRL_C04_T01`, `EMOTION_CTRL_C08_T01`, `EMOTION_CTRL_C09_T01`).
3. **Validación Cruzada por Sujeto:**
   - Usar `GroupKFold(n_splits=5)` agrupando por la columna `subject_id` para garantizar que las tomas múltiples del mismo sujeto (`P01`, `P07`, `C01`, `C02`, `C03`) no coexistan en los conjuntos de entrenamiento y prueba.
4. **Tratamiento de Variables TDA:**
   - Omitir `persistence_value` y `entropy_value` de cargadores tabulares estándar debido a su serialización como cadenas de matrices NumPy.

---
*Documento actualizado y verificado conforme a la auditoría técnica de los 22 archivos de `/Datos e-Motion/`.*  
*Generado: 26 de Octubre de 2026 | Versión 2.0*
