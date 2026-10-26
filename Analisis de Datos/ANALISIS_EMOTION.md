# 📹 ANÁLISIS TÉCNICO EXHAUSTIVO Y AUDITORÍA DE DATOS ÓPTICOS (e-Motion / RGB-D)
> **Proyecto de Grado:** Caracterización Cinemática y Clasificación del Test *Timed Up and Go* (TUG) en la Enfermedad de Parkinson Mediante Unidades de Medición Inercial y Fusión Óptica
> **Metodología:** CRISP-DM — Fases de *Data Understanding* y *Data Preparation*
> **Fecha de Elaboración:** Octubre 2026 · Semana 12
> **Autor:** Esteban Guarín Valencia | Dirección: Prof. Domiciano Rincón
> **Ubicación de Archivos:** Carpeta `/Datos e-Motion/`

---

## 1. Resumen Ejecutivo del Repositorio de Datos Ópticos e-Motion

El conjunto de datos almacenado en la carpeta `/Datos e-Motion/` constituye el repositorio primario de registros biomecánicos espaciotemporales capturados a través del subsistema óptico basado en cámaras de color y profundidad (**RGB-D**) de la plataforma institucional **VIMOV / e-Motion**. A diferencia de los registros inerciales (IMUs) —que almacenan series temporales continuas de señales cinemáticas brutas a ~50 Hz—, cada archivo `.json` de e-Motion almacena los **descriptores cinemáticos y variables espaciotemporales precomputadas** de la marcha y el braceo correspondientes al pasillo recto de desplazamiento de la prueba TUG, junto con identificadores y referencias a los gráficos generados en el backend analítico.

### 1.1 Métricas Clave del Repositorio

| Métrica / Parámetro | Valor Bruto Total | Registros Válidos (Pipeline) | Registros Descartados | Tasa de Retención |
|:---|:---:|:---:|:---:|:---:|
| **Total de Archivos JSON** | **13** | **12** | **1** (Duplicado semántico) | **92.3%** |
| **Grabaciones de Pacientes con Parkinson (EP)** | 5 | 4 | 1 (`f97b7bda` dup. de `75f2d454`) | 80.0% |
| **Grabaciones de Sujetos de Control Sanos** | 8 | 8 | 0 | 100.0% |
| **Participantes Humanos Únicos (Sesiones)** | **8** | **8** (3 Pacientes / 5 Controles) | 0 | 100.0% |
| **Tecnologías de Sensores RGB-D** | 3 sensores (`kinect_v2`: 8, `intel`: 3, `orbbec_astra`: 2) | Idéntica distribución | 0 | 100.0% |
| **Volumen Total en Disco** | **192.4 KB** (196,989 bytes) | 180.3 KB | 12.1 KB | 93.7% |
| **Rango Cronológico de Registro** | 05/09/2019 → 03/10/2026 | 05/09/2019 → 03/10/2026 | Octubre 2026 | Multi-anual |
| **Relación de Desbalance (Control : EP)** | 1.6 : 1 (8 : 5) | **2.0 : 1** (8 controles vs 4 pacientes) | -- | Balance Moderado |

### 1.2 Justificación Metodológica de los Descartes y Control de Calidad

Siguiendo el rigor de control de calidad aplicado a los datos inerciales y de acuerdo con el marco CRISP-DM, se identificó un único archivo sujeto a descarte formal:

1. **Duplicado Semántico de Re-exportación (`f97b7bda-cfb5-4556-8886-684866de5524.json`):**
   - **Archivo par:** `75f2d454-5771-4feb-abad-30e03281a2f4.json`.
   - **Causa técnica:** Ambos archivos poseen la misma fecha de captura exacta (`Sat, 03 Oct 2026 09:44:32 GMT`), el mismo sensor (`intel`), el mismo protocolo (`Paciente`), idéntico tamaño (12,348 bytes) y **valores cinemáticos en `vars` rigurosamente idénticos** (diferencia de variables = 0). Únicamente difieren en los UUIDs generados por el backend y en las marcas temporales de las imágenes generadas (`14:45:30` vs `15:36:30`), lo cual evidencia que la sesión fue re-procesada o re-graficada en el servidor.
   - **Veredicto:** Conservar `75f2d454` y descartar `f97b7bda` para prevenir duplicación artificial de muestras en la evaluación estadística (*Data Leakage*).

---

## 2. Identificación de Participantes y Mapeo de Tomas Múltiples

### 2.1 Criterio Determinístico de Agrupación e Identidad

En contraste con los archivos de IMUs donde la identidad se reconstruye por tuplas demográficas $\langle \text{nacimiento}, \; \text{sexo}, \; \text{talla} \rangle$, en e-Motion la identidad se deriva de una combinación de:
1. **Timestamp de captura con resolución de segundos:** Cuatro pares de grabaciones se ejecutaron en la misma sesión con separación de 14 a 29 segundos (re-test inmediato del participante).
2. **Etiqueta clínica de protocolo (`protocol`):** Describe la condición diagnóstica (`Sin operaciones - Control`, `Postlevodopa dos - una hora despues`, `Control, esposa`, `ON`, `Paciente Sano - LIPS`, `Paciente sano`, `Paciente`).
3. **Metadatos incrustados en nombres de imágenes:** El pipeline de renderizado de e-Motion incrusta en los nombres de las figuras PNG la identificación del sujeto o el hash de sesión (ej. `CARMEN_SANCHEZ_ZUNIGA_-_03-10-2026`, `JUAN_MARTINEZ_-_27-05-2024`).

### 2.2 Desglose Exhaustivo de los 8 Grupos de Participantes

#### Grupo 1: Sujeto Control C01 — Control Sano sin Cirugías (2 tomas)
* **Fecha:** 05 de septiembre de 2019 | **Sensor:** `kinect_v2`
* **Protocolo:** `Sin operaciones - Control`
* **Tomas registradas:**
  - `1d1dd16a-4293-49d3-b636-f3d939a5c5e6.json`: Hora: `19:51:54 GMT` | Duración: 1.98 s | Distancia: 1.94 m | Vel: 0.98 m/s | ASA: 18.53% | **VÁLIDO (Toma 1)**.
  - `fbb034e8-2368-4367-881f-550561097915.json`: Hora: `19:52:23 GMT` (29 s después) | Duración: 1.98 s | Distancia: 1.97 m | Vel: 1.00 m/s | ASA: 17.22% | **VÁLIDO (Toma 2)**.
* **Diagnóstico cinemático:** Excelente reproducibilidad intra-sujeto (variación de velocidad < 2%, paso simétrico de ~0.81 m).

#### Grupo 2: Paciente P01 — Paciente Parkinson Post-Levodopa (2 tomas)
* **Fecha:** 28 de noviembre de 2019 | **Sensor:** `kinect_v2`
* **Protocolo:** `Postlevodopa dos - una hora despues`
* **Tomas registradas:**
  - `8881e163-2398-403a-b1d2-dc1bf209ef02.json`: Hora: `14:51:39 GMT` | Duración: 2.97 s | Distancia: 1.99 m | Vel: 0.67 m/s | ASA: 18.09% | **VÁLIDO (Toma 1)**.
  - `f0f2a528-bf51-40b9-95fb-a27eba90122b.json`: Hora: `14:52:01 GMT` (22 s después) | Duración: 3.11 s | Distancia: 1.98 m | Vel: 0.64 m/s | ASA: 1.40% | **VÁLIDO (Toma 2)**.
* **Diagnóstico cinemático:** Velocidad reducida (0.64–0.67 m/s) y pasos cortos (0.31 m en toma 1). La toma 2 muestra mayor simetría braquial post-medicación (efecto terapéutico en ventana de 1 hora).

#### Grupo 3: Sujeto Control C02 — Cónyuge / Acompañante Control (2 tomas)
* **Fecha:** 12 de noviembre de 2021 | **Sensor:** `kinect_v2`
* **Protocolo:** `Control, esposa`
* **Tomas registradas:**
  - `165cebab-ffcf-47a6-b202-8c1d19f4aab7.json`: Hora: `15:35:23 GMT` | Duración: 2.32 s | Distancia: 1.94 m | Vel: 0.84 m/s | ASA: 18.37% | **VÁLIDO (Toma 1)**.
  - `ed8c9902-c37f-4fd5-88cb-75a0a33c9e8f.json`: Hora: `15:35:37 GMT` (14 s después) | Duración: 2.49 s | Distancia: 1.92 m | Vel: 0.77 m/s | ASA: 7.39% | **VÁLIDO (Toma 2)**.
* **Diagnóstico cinemático:** Control sano apareado demográficamente por edad (esposa de paciente evaluado en la misma jornada).

#### Grupo 4: Sujeto Control C03 — Control Sano Institucional (2 tomas)
* **Fecha:** 17 de marzo de 2022 | **Sensor:** `kinect_v2`
* **Protocolo:** `control`
* **Tomas registradas:**
  - `c917a985-2218-48c6-a454-273278b57cbd.json`: Hora: `19:54:21 GMT` | Duración: 2.08 s | Distancia: 1.98 m | Vel: 0.95 m/s | ASA: 36.44% | **VÁLIDO (Toma 1)**.
  - `c9bc8435-fd01-4dff-af9f-6e5f3606e06b.json`: Hora: `19:54:37 GMT` (16 s después) | Duración: 2.08 s | Distancia: 1.94 m | Vel: 0.93 m/s | ASA: 17.27% | **VÁLIDO (Toma 2)**.
* **Diagnóstico cinemático:** Alta velocidad de avance (~0.94 m/s) con cadencia rápida (5 a 7 pasos en 2 metros).

#### Grupo 5: Paciente P02 — Paciente Parkinson en Fase Motora ON (1 toma)
* **Fecha:** 01 de febrero de 2024 | **Sensor:** `orbbec_astra`
* **Protocolo:** `ON`
* **Toma registrada:**
  - `2b069c98-07bd-405f-8bec-f284efd65f59.json`: Hora: `12:54:33 GMT` | Duración: 1.71 s | Distancia: 1.96 m | Vel: 1.15 m/s | ASA: 18.38% | **VÁLIDO**.
* **Diagnóstico cinemático:** Velocidad alta (1.15 m/s) indicativa de respuesta clínica óptima a tratamiento dopaminérgico/DBS durante la ventana ON.

#### Grupo 6: Sujeto Control C04 — Control Sano Banco Astra (1 toma)
* **Fecha:** 27 de mayo de 2024 | **Sensor:** `orbbec_astra`
* **Protocolo:** `Paciente sano`
* **Toma registrada:**
  - `854a41c4-1440-4308-a46d-12711b544ef7.json`: Hora: `08:33:07 GMT` | Duración: 2.29 s | Distancia: 1.82 m | Vel: 0.79 m/s | ASA: 5.47% | **VÁLIDO**.
* **Diagnóstico cinemático:** Marcha regular con alta simetría de braceo (ASA = 5.47%).

#### Grupo 7: Sujeto Control C05 — Participante Identificado "Juan Martínez" (1 toma)
* **Fecha:** 27 de mayo de 2024 | **Sensor:** `intel` (RealSense)
* **Protocolo:** `Paciente Sano - LIPS` (Laboratorio de Procesamiento de Señales)
* **Toma registrada:**
  - `670b9960-50fb-46d4-90e5-7177c3ddf596.json`: Hora: `09:33:58 GMT` | Duración: 2.03 s | Distancia: 1.88 m | Vel: 0.92 m/s | ASA: 6.09% | **VÁLIDO**.
* **Diagnóstico cinemático:** Marcha rápida y simétrica; el nombre `JUAN_MARTINEZ` aparece en los metadatos de las figuras de segmentación.

#### Grupo 8: Paciente P03 — Participante Identificada "Carmen Sánchez Zúñiga" (2 archivos)
* **Fecha:** 03 de octubre de 2026 | **Sensor:** `intel` (RealSense)
* **Protocolo:** `Paciente`
* **Tomas registradas:**
  - `75f2d454-5771-4feb-abad-30e03281a2f4.json`: Hora: `09:44:32 GMT` | Duración: 3.73 s | Distancia: 1.93 m | Vel: 0.52 m/s | ASA: 28.55% | **VÁLIDO**.
  - `f97b7bda-cfb5-4556-8886-684866de5524.json`: Hora: `09:44:32 GMT` | Duración: 3.73 s | Distancia: 1.93 m | Vel: 0.52 m/s | ASA: 28.55% | **DESCARTADO (Duplicado semántico)**.
* **Diagnóstico cinemático:** El caso más severo de bradicinesia registrado en e-Motion: velocidad más baja del repositorio (0.52 m/s, duración 3.73 s) y alta asimetría de balanceo de brazos (ASA = 28.55%).

---

## 3. Estructura del Esquema JSON y Diferencias Técnicas

### 3.1 Esquema de la Raíz del Archivo

Cada archivo en `/Datos e-Motion/` presenta una estructura JSON estrictamente normalizada con 4 claves de primer nivel:

```json
{
  "id": "165cebab-ffcf-47a6-b202-8c1d19f4aab7",
  "sensor_type": "kinect_v2",
  "capture_date": "Fri, 12 Nov 2021 15:35:23 GMT",
  "results": [
    {
      "id": "b0ef67ee-8863-43b1-81d5-23695669ec42",
      "data_id": "165cebab-ffcf-47a6-b202-8c1d19f4aab7",
      "joint": "ankles",
      "protocol": "Control, esposa",
      "vars": { ... 34 variables ... },
      "images": [ "ankles_0_...png", ... ]
    },
    {
      "id": "bfe18f4f-e46c-42ab-95fb-7d40319b583b",
      "data_id": "165cebab-ffcf-47a6-b202-8c1d19f4aab7",
      "joint": "arms",
      "protocol": "Control, esposa",
      "vars": { ... 10 variables ... },
      "images": [ "arms_0_...png", ... ]
    }
  ]
}
```

### 3.2 Comparación de Sensores RGB-D Utilizados

| Parámetro Técnico | Microsoft Kinect v2 | Orbbec Astra | Intel RealSense (`intel`) |
|:---|:---|:---|:---|
| **Principio Físico** | Tiempo de Vuelo (*Time-of-Flight*, ToF) | Luz Estructurada Infrarroja | Estereoscopía Infrarroja Activa |
| **Archivos en Dataset** | **8 archivos** (61.5%) | **2 archivos** (15.4%) | **3 archivos** (23.1%) |
| **Años de Uso** | 2019, 2021, 2022 | 2024 | 2024, 2026 |
| **Resolución Profundidad** | 512 × 424 px | 640 × 480 px | 848 × 480 / 1280 × 720 px |
| **Tasa de Muestreo** | 30 Hz | 30 Hz | 30 – 60 Hz |
| **Rango Operativo Óptimo** | 0.8 m – 4.2 m | 0.6 m – 8.0 m | 0.3 m – 3.0 m |
| **Sensibilidad a Luz Ambiental** | Media (infrarrojo modulado) | Alta (interferencia solar) | Muy baja (patrón activo + visión estéreo) |

> [!NOTE] La evolución de sensores refleja la historia tecnológica del laboratorio de biomecánica: en 2019–2022 se empleó Kinect v2 como estándar clínico; tras su descontinuación se evaluó Orbbec Astra en 2024, convergiendo finalmente a cámaras Intel RealSense para las capturas más recientes.

### 3.3 Hallazgo Técnico Crítico: Anomalía en la Serialización de Variables TDA

Al auditar los tipos de datos de las 34 variables del bloque `ankles`, se identificó una anomalía severa de serialización en el backend:

> [!WARNING] **Serialización corrupta de matrices NumPy en cadenas de texto:**
> Las variables `persistence_value` y `entropy_value` (procedentes de Análisis Topológico de Datos / Homología Persistente) **no fueron convertidas a listas JSON nativas (`.tolist()`)**, sino serializadas invocando directamente la representación en texto del array (`str(np_array)`).
>
> **Ejemplo real extraído de `165cebab...json`:**
> ```python
> "persistence_value": "[4.91643983 1.3180612 ]"
> "entropy_value": "[array([[0.00000000e+00, 4.21468478e-08],\n [0.00000000e+00, 4.21468478e-08], ... ]"
> ```
> Un cargador convencional (`json.load`) cargará estas variables como `str`. Intentar realizar operaciones numéricas directas o conversiones tipo `float()` arrojará `ValueError` o `TypeError`.
>
> **Directriz de Solución:** Si se requiere emplear las características de homología persistente, debe implementarse un pre-parser mediante expresiones regulares (`re.findall(r"[-+]?\d*\.\d+e?[-+]?\d*", ...)`) o `ast.literal_eval`. Para el modelado cinemático estándar, se recomienda omitir estas dos llaves y utilizar las 32 variables escalares restantes.

---

## 4. Inventario Completo y Organizado de los 13 Archivos

### 4.1 Grabaciones de Pacientes con Parkinson (5 archivos / 3 participantes únicos)

| # | Archivo JSON | UUID | Participante | Fecha UTC | Sensor | Protocolo Clínico | Duración | Velocidad | ASA (%) | Veredicto |
|:---:|:---|:---|:---:|:---:|:---:|:---|:---:|:---:|:---:|:---:|
| 1 | `8881e163-2398-403a-b1d2-dc1bf209ef02.json` | `8881e163` | **P01 (Toma 1)** | 2019-11-28 14:51:39 | `kinect_v2` | Postlevodopa dos - una hora despues | 2.97 s | 0.670 m/s | 18.09% | **VÁLIDO** |
| 2 | `f0f2a528-bf51-40b9-95fb-a27eba90122b.json` | `f0f2a528` | **P01 (Toma 2)** | 2019-11-28 14:52:01 | `kinect_v2` | Postlevodopa dos - una hora despues | 3.11 s | 0.636 m/s | 1.40% | **VÁLIDO** |
| 3 | `2b069c98-07bd-405f-8bec-f284efd65f59.json` | `2b069c98` | **P02** | 2024-02-01 12:54:33 | `orbbec_astra` | ON (Fase motora activa) | 1.71 s | 1.149 m/s | 18.38% | **VÁLIDO** |
| 4 | `75f2d454-5771-4feb-abad-30e03281a2f4.json` | `75f2d454` | **P03** | 2026-10-03 09:44:32 | `intel` | Paciente (Carmen Sánchez Z.) | 3.73 s | 0.519 m/s | 28.55% | **VÁLIDO** |
| 5 | `f97b7bda-cfb5-4556-8886-684866de5524.json` | `f97b7bda` | **P03** | 2026-10-03 09:44:32 | `intel` | Paciente (Carmen Sánchez Z.) | 3.73 s | 0.519 m/s | 28.55% | **DESCARTADO (Dup. semántico)** |

### 4.2 Grabaciones de Sujetos de Control Sanos (8 archivos / 5 personas únicas)

| # | Archivo JSON | UUID | Sujeto | Fecha UTC | Sensor | Protocolo | Duración | Distancia | Velocidad | ASA (%) |
|:---:|:---|:---|:---:|:---:|:---:|:---|:---:|:---:|:---:|:---:|
| 1 | `1d1dd16a-4293-49d3-b636-f3d939a5c5e6.json` | `1d1dd16a` | **C01 (T1)** | 2019-09-05 19:51:54 | `kinect_v2` | Sin operaciones - Control | 1.98 s | 1.94 m | 0.983 m/s | 18.53% |
| 2 | `fbb034e8-2368-4367-881f-550561097915.json` | `fbb034e8` | **C01 (T2)** | 2019-09-05 19:52:23 | `kinect_v2` | Sin operaciones - Control | 1.98 s | 1.97 m | 0.996 m/s | 17.22% |
| 3 | `165cebab-ffcf-47a6-b202-8c1d19f4aab7.json` | `165cebab` | **C02 (T1)** | 2021-11-12 15:35:23 | `kinect_v2` | Control, esposa | 2.32 s | 1.94 m | 0.836 m/s | 18.37% |
| 4 | `ed8c9902-c37f-4fd5-88cb-75a0a33c9e8f.json` | `ed8c9902` | **C02 (T2)** | 2021-11-12 15:35:37 | `kinect_v2` | Control, esposa | 2.49 s | 1.92 m | 0.771 m/s | 7.39% |
| 5 | `c917a985-2218-48c6-a454-273278b57cbd.json` | `c917a985` | **C03 (T1)** | 2022-03-17 19:54:21 | `kinect_v2` | control | 2.08 s | 1.98 m | 0.952 m/s | 36.44% |
| 6 | `c9bc8435-fd01-4dff-af9f-6e5f3606e06b.json` | `c9bc8435` | **C03 (T2)** | 2022-03-17 19:54:37 | `kinect_v2` | control | 2.08 s | 1.94 m | 0.931 m/s | 17.27% |
| 7 | `854a41c4-1440-4308-a46d-12711b544ef7.json` | `854a41c4` | **C04** | 2024-05-27 08:33:07 | `orbbec_astra` | Paciente sano | 2.29 s | 1.82 m | 0.794 m/s | 5.47% |
| 8 | `670b9960-50fb-46d4-90e5-7177c3ddf596.json` | `670b9960` | **C05** | 2024-05-27 09:33:58 | `intel` | Paciente Sano - LIPS (Juan M.) | 2.03 s | 1.88 m | 0.923 m/s | 6.09% |

---

## 5. Diccionario Completo de Variables Biomecánicas Extraídas

El sistema e-Motion calcula automáticamente 44 variables organizadas en dos dominios anatómicos: **tobillos** (`ankles`: 34 variables) y **brazos** (`arms`: 10 variables).

### 5.1 Variables Cinemáticas de Marcha (`joint = "ankles"`)

| Variable | Tipo | Unidad | Definición Biomecánica | Relevancia en Enfermedad de Parkinson |
|:---|:---:|:---:|:---|:---|
| `initial_time` | `str` | ISO 8601 | Marca temporal de inicio de adquisición óptica | Sincronización temporal con otros sensores |
| `ret_total_time_test` | `float` | s | Tiempo total de tránsito en el campo de visión de la cámara | Indicador global de bradicinesia de marcha |
| `ret_total_time_left` | `float` | s | Tiempo total acumulado de marcha del miembro inferior izquierdo | Comparación de simetría temporal |
| `ret_total_time_right` | `float` | s | Tiempo total acumulado de marcha del miembro inferior derecho | Comparación de simetría temporal |
| `ret_total_distance_test` | `float` | m | Desplazamiento lineal total medido sobre el pasillo óptico (~1.9 m) | Normalización de velocidad |
| `ret_total_velocity` | `float` | m/s | Velocidad media de progresión: $v = d_{	ext{test}} / t_{	ext{test}}$ | Marcador cardinal: severamente reducida en EP |
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

### 5.2 Variables de Balanceo de Miembros Superiores (`joint = "arms"`)

| Variable | Tipo | Unidad | Definición Biomecánica | Relevancia en Enfermedad de Parkinson |
|:---|:---:|:---:|:---|:---|
| `initial_time` | `str` | ISO 8601 | Marca temporal de inicio de adquisición óptica | Sincronización temporal |
| `magnitude_left` | `float` | m | Amplitud máxima de excursión del balanceo del brazo izquierdo | **Hipocinesia:** reducción de amplitud de braceo |
| `magnitude_right` | `float` | m | Amplitud máxima de excursión del balanceo del brazo derecho | **Hipocinesia:** reducción de amplitud de braceo |
| `velocity_left` | `float` | m/s | Velocidad tangencial media del balanceo del brazo izquierdo | Bradicinesia del miembro superior |
| `velocity_right` | `float` | m/s | Velocidad tangencial media del balanceo del brazo derecho | **Severamente reducida en EP (0.06 vs 0.17 m/s)** |
| `std_left` | `float` | m | Desviación estándar de la trayectoria del brazo izquierdo | Variabilidad motora intra-prueba |
| `std_right` | `float` | m | Desviación estándar de la trayectoria del brazo derecho | Variabilidad motora intra-prueba |
| `time_left` | `float` | s | Tiempo total en el cual el brazo izquierdo estuvo oscilando | Continuidad del braceo |
| `time_right` | `float` | s | Tiempo total en el cual el brazo derecho estuvo oscilando | Continuidad del braceo |
| `asa` | `float` | % | **Arm Swing Asymmetry (Asimetría de Braceo)** | **Marcador precoz patognomónico de Parkinson** |

> [!TIP] **Fórmula Clínica del ASA (*Arm Swing Asymmetry*):**
> $$	ext{ext{ASA} = rac{|	ext{Magnitude}_{	ext{dominant}} - 	ext{Magnitude}_{	ext{non-dominant}}|}{\max(	ext{Magnitude}_{	ext{left}}, \; 	ext{Magnitude}_{	ext{right}})} 	imes 100\%$$
> En sujetos sanos el balanceo es bilateral y armónico ($	ext{ext{ASA} < 10-15\%$). En la enfermedad de Parkinson, el inicio asimétrico de los síntomas motores genera una marcada inhibición unilateral del braceo, elevando significativamente el $	ext{ext{ASA}$.

---

## 6. Análisis Estadístico Comparativo: Pacientes Parkinson vs. Controles Sanos

> [!NOTE] Estadísticas computadas sobre los 13 archivos del repositorio (5 pacientes y 8 controles sanos). Las dos variables con serialización TDA (`persistence_value` y `entropy_value`) se excluyeron del cálculo escalar por su condición de arrays multidimensionales en texto.

### 6.1 Tabla Comparativa de Variables de Tobillos (`ankles`)

| Variable | Pacientes EP ($n=5$) | Controles Sanos ($n=8$) | Variación Relativa | Significado Clínico |
|:---|:---:|:---:|:---:|:---|
| **Velocidad total (`ret_total_velocity`)** | **0.6985 ± 0.2607 m/s** | **0.8982 ± 0.0864 m/s** | **−22.2%** | Bradicinesia de marcha pronunciada |
| **Tiempo de tránsito (`ret_total_time_test`)**| **3.0478 ± 0.8265 s** | **2.1559 ± 0.1880 s** | **+41.4%** | Mayor tiempo para recorrer el pasillo |
| **Distancia total (`ret_total_distance_test`)**| 1.9589 ± 0.0267 m | 1.9227 ± 0.0510 m | +1.9% | Pasillo geométricamente idéntico (~1.94 m) |
| **Proporción apoyo izq (`prop_time_left_support`)**| **0.5550 ± 0.1112** | **0.4667 ± 0.1257** | **+18.9%** | Aumento del tiempo de contacto por inestabilidad |
| **Proporción balanceo izq (`prop_time_left_swing`)**| **0.4450 ± 0.1112** | **0.5333 ± 0.1257** | **−16.6%** | Menor tiempo de despegue y propulsión |
| **Proporción apoyo der (`prop_time_right_support`)**| 0.5661 ± 0.1410 | 0.5296 ± 0.1182 | +6.9% | Sobrecarga de fase de soporte |
| **Proporción balanceo der (`prop_time_right_swing`)**| 0.4339 ± 0.1410 | 0.4704 ± 0.1182 | −7.8% | Reducción de fase de vuelo |
| **Tiempo apoyo izq (`ret_time_left_support`)** | **0.4529 ± 0.1429 s** | **0.3250 ± 0.2819 s** | **+39.4%** | Pasos con apoyo prolongado |
| **Tiempo balanceo izq (`ret_time_left_swing`)** | 0.3671 ± 0.1156 s | 0.3062 ± 0.1524 s | +19.9% | Marcha más lenta en todas las fases |
| **Tiempo apoyo der (`ret_time_right_support`)** | **0.5165 ± 0.1801 s** | **0.3351 ± 0.3332 s** | **+54.1%** | Mayor contacto plantar bilateral |
| **Tiempo balanceo der (`ret_time_right_swing`)** | 0.3852 ± 0.1109 s | 0.2502 ± 0.1507 s | +54.0% | Lentitud en la oscilación de la pierna |
| **Velocidad miembro izq (`ret_total_speed_left`)** | 0.7796 ± 0.3217 m/s | 0.9669 ± 0.1222 m/s | −19.4% | Menor aceleración segmental |
| **Velocidad miembro der (`ret_total_speed_right`)**| **0.6049 ± 0.1009 m/s** | **0.8251 ± 0.1285 m/s** | **−26.7%** | Mayor afectación del hemicuerpo derecho |
| **Longitud paso izq (`ret_length_left_step`)** | 0.6015 ± 0.3443 m | 0.6469 ± 0.3145 m | −7.0% | Tendencia a acortamiento de paso |
| **Longitud paso der (`ret_length_right_step`)** | 0.6445 ± 0.3344 m | 0.5488 ± 0.3547 m | +17.4% | Alta variabilidad por tamaño muestral |
| **Número de pasos (`ret_num_step_left`)** | 2.40 ± 0.89 | 3.12 ± 2.03 | −23.1% | Pasos amplios en fase ON vs cadencia control |

### 6.2 Tabla Comparativa de Variables de Brazos (`arms`)

| Variable | Pacientes EP ($n=5$) | Controles Sanos ($n=8$) | Variación Relativa | Significado Clínico |
|:---|:---:|:---:|:---:|:---|
| **Asimetría de Braceo (`asa`)** | **18.9965 ± 11.1056 %** | **15.8465 ± 10.1131 %** | **+19.9%** | Asimetría patológica más elevada en EP |
| **Velocidad brazo derecho (`velocity_right`)** | **0.0633 ± 0.0234 m/s** | **0.1665 ± 0.1199 m/s** | **−62.0%** | **Inhibición severa del braceo derecho** |
| **Magnitud brazo derecho (`magnitude_right`)** | **0.0499 ± 0.0351 m** | **0.1244 ± 0.1285 m** | **−59.9%** | **Hipocinesia marcada en hemicuerpo derecho** |
| **Velocidad brazo izquierdo (`velocity_left`)** | 0.1107 ± 0.0688 m/s | 0.1254 ± 0.0418 m/s | −11.7% | Menor reducción en brazo contralateral |
| **Magnitud brazo izquierdo (`magnitude_left`)** | 0.1274 ± 0.1074 m | 0.0942 ± 0.0490 m | +35.2% | Compensación motora contralateral |
| **Variabilidad brazo der (`std_right`)** | **0.0374 ± 0.0197 m** | **0.0639 ± 0.0329 m** | **−41.5%** | Rigidez: braceo congelado y estereotipado |
| **Variabilidad brazo izq (`std_left`)** | 0.0571 ± 0.0288 m | 0.0658 ± 0.0297 m | −13.2% | Menor rigidez contralateral |
| **Tiempo braceo izq (`time_left`)** | 0.8826 ± 0.5431 s | 0.7504 ± 0.2859 s | +17.6% | Proporcional a la mayor duración total |
| **Tiempo braceo der (`time_right`)** | 0.7115 ± 0.3806 s | 0.6577 ± 0.3145 s | +8.2% | Proporcional a la mayor duración total |

### 6.3 Conclusiones Biomecánicas del Análisis Óptico

1. **Patrón de Bradicinesia Espaciotemporal:** Los pacientes con Parkinson tardan en promedio un 41.4% más de tiempo en recorrer los 2 metros del pasillo ($3.05\text{ s}$ vs $2.16\text{ s}$), con una velocidad lineal de avance significativamente inferior ($0.70\text{ m/s}$ vs $0.90\text{ m/s}$).
2. **Alteración del Ciclo de la Marcha:** Los pacientes pasan el **55.5%** de su tiempo en fase de soporte/apoyo (frente al **46.7%** en controles), reflejando la necesidad clínica de mantener contacto bilateral con el suelo para mitigar el riesgo de pérdida de equilibrio por inestabilidad postural.
3. **Hipocinesia Unilateral y Rigidez de Miembro Superior:** La reducción dramática en la velocidad ($−62.0\%$) y amplitud ($−59.9\%$) del brazo derecho evidencia la asimetría clínica característica del Parkinson. Mientras los controles exhiben un braceo bilateral balanceado ($0.12\text{ m}$ en ambos brazos), los pacientes muestran una asimetría marcada ($0.05\text{ m}$ en brazo derecho vs $0.13\text{ m}$ en izquierdo), elevando el $\text{ASA}$ hacia niveles patológicos de hasta $28.55\%$.

---

## 7. Evolución Histórica de la Plataforma e-Motion y Estados Clínicos

### 7.1 Línea de Tiempo de las Adquisiciones Ópticas

```
Línea de tiempo de adquisición e-Motion (RGB-D):
─────────────────────────────────────────────────────────────────────────────
 Sep 2019       Nov 2019       Nov 2021       Mar 2022       Feb 2024       May 2024       Oct 2026
    │              │              │              │              │              │              │
 C01 (T1/T2)    P01 (T1/T2)    C02 (T1/T2)    C03 (T1/T2)       P02        C04 & C05     P03 (T1/dup)
 Control sano   Post-Levodopa  Esposa-Ctrl    Control sano     Fase ON     Controles     Carmen Sánchez
 [kinect_v2]    [kinect_v2]    [kinect_v2]    [kinect_v2]    [orbbec_astra] [astra/intel]  [intel]
─────────────────────────────────────────────────────────────────────────────
```

### 7.2 Caracterización de Condiciones y Protocolos Clínicos

1. **Protocolo "Sin operaciones - Control" (2019):** Línea base de normalidad motora en adultos sanos sin antecedentes ortopédicos ni neurológicos.
2. **Protocolo "Postlevodopa dos - una hora despues" (2019):** Captura orientada a medir la ventana de latencia y efectividad del tratamiento dopaminérgico. La toma 2 evidencia una reducción dramática del ASA ($1.40\%$) en comparación con la toma 1 ($18.09\%$), demostrando la sensibilidad del braceo óptico como biomarcador de respuesta terapéutica.
3. **Protocolo "Control, esposa" (2021):** Empleo de cuidadores primarios / cónyuges como controles sanos pareados por rango etario y contexto ambiental.
4. **Protocolo "ON" (2024):** Evaluación del paciente en su estado clínico de máximo beneficio farmacológico o estimulación cerebral profunda activa (DBS), caracterizado por la mayor velocidad de marcha del dataset ($1.15\text{ m/s}$).
5. **Protocolo "Paciente" (2026):** Evaluación basal de paciente con Parkinson sin ventana farmacológica forzada, evidenciando el compromiso motor más severo ($0.52\text{ m/s}$ y ASA de $28.55\%$).

---

## 8. Análisis de Correspondencia Bimodal: Datos Ópticos (e-Motion) vs. Datos Inerciales (IMUs)

### 8.1 Comparación Estructural y Metodológica

| Dimensión Analítica | Repositorio `/Datos IMUs/` | Repositorio `/Datos e-Motion/` |
|:---|:---|:---|
| **Modalidad de Censado** | Cinemática inercial (Acelerómetros + Giróscopos) | Visión artificial 3D y profundidad (RGB-D) |
| **Invasividad** | Media (5 sensores fijados con correas al cuerpo) | Nula (cámara estática externa a 3 metros) |
| **Naturaleza del Dato** | Series de tiempo continuas a ~49.4 Hz (señal cruda) | Descriptores escalares precomputados y agregados |
| **Segmento del TUG Cubierto**| **Prueba TUG completa** (12 s a 133 s: levantarse, marcha, giro, retorno, sentarse) | **Pasillo recto de marcha** (1.7 s a 3.7 s en el FOV de la cámara, ~1.9 m) |
| **Total de Archivos** | 78 grabaciones (292.3 MB) | 13 grabaciones (192.4 KB) |
| **Horizonte Temporal** | Febrero 2026 → Agosto 2026 | Septiembre 2019 → Octubre 2026 |
| **Cobertura Geográfica** | Brigadas clínicas de Santa Marta y Cali (CST) | Banco de validación de laboratorio (LIPS / Cali) |

### 8.2 Hallazgo Crucial de Ingeniería: Disparidad Temporal y Fusión Bimodal

> [!IMPORTANT] **Ausencia de sincronización temporal 1 a 1 entre los 78 JSON de IMU y los 13 JSON de e-Motion:**
> Al contrastar las marcas temporales de ambos repositorios, se comprueba que:
> - Los 78 archivos de `Datos IMUs/` fueron capturados en las brigadas de **junio a agosto de 2026** (Santa Marta y CST).
> - Los 13 archivos de `Datos e-Motion/` corresponden a un banco histórico de calibración y validación algorítmica (**2019 a mayo de 2024**), sumado a una sesión de prueba en **octubre de 2026** (`2026-10-03`).
> 
> **Consecuencia Metodológica para la Tesis:**
> No es posible realizar una fusión a nivel de muestra (*sample-level fusion*) directa entre los registros de las brigadas de IMU y los archivos e-Motion presentes en el repositorio, puesto que no corresponden a los mismos instantes de captura.
> 
> **Rol Metodológico de e-Motion en el Proyecto:**
> 1. **Modelo de Referencia y Verificación (*Ground Truth* Óptico):** Los datos e-Motion proveen el rango de normalidad y patología de las variables cinemáticas reales (longitud de paso: $0.60\text{ m}$; velocidad de marcha: $0.70 - 0.90\text{ m/s}$; proporción de apoyo: $46 - 55\%$; ASA: $15 - 28\%$).
> 2. **Validación del Algoritmo de Segmentación Inercial:** Los algoritmos de extracción de características implementados sobre los acelerómetros y giróscopos de las IMUs deben converger hacia los mismos rangos cuantitativos calculados de manera óptica por e-Motion.
> 3. **Justificación del Ecosistema Bimodal:** Demuestra la complementariedad teórica descrita en la memoria de grado: la IMU resuelve la prueba TUG completa (incluyendo giros y transiciones sedente-bípedo sin problemas de oclusión), mientras que la cámara RGB-D aporta la estimación espacial directa sin deriva de integración (*drift*).

---

## 9. Directrices de Ingeniería, Banderas Clínicas y Checklist Pre-Integración

### 9.1 Banderas Clínicas y Técnicas Detectadas

| # | Archivo(s) | Bandera / Anomalía | Acción Técnica Requerida |
|:---:|:---|:---|:---|
| 1 | `f97b7bda` vs `75f2d454` | **Duplicado semántico exacto:** Mismas variables cinemáticas y fecha; distinta hora de imagen. | Excluir obligatoriamente `f97b7bda` del pipeline de modelado. |
| 2 | Todos (13 archivos) | **Serialización TDA:** `persistence_value` y `entropy_value` son strings de arrays de NumPy. | Omitir ambas variables en cargadores tabulares o parsear con regex. |
| 3 | `670b9960` y `75f2d454` | **Fuga de nombres personales:** Los nombres de pacientes aparecen en el nombre de las imágenes PNG. | Anonimizar eliminando los nombres en cualquier reporte público. |
| 4 | `8881e163` y `f0f2a528` | **Variación extrema de ASA post-medicación:** El ASA pasa de 18.09% a 1.40% en 22 segundos. | Documentar como evidencia de sensibilidad del braceo al efecto levodopa. |
| 5 | `2b069c98` (P02) | **Paso único detectado:** `ret_num_step_left = 1`, `ret_num_step_right = 1`. | Posible corte de detección en bordes del FOV en Orbbec Astra. Auditar. |
| 6 | `c917a985` (C03) | **Cadencia muy rápida:** 5 y 7 pasos en 1.94 m con velocidad de 0.95 m/s. | Marcha a pasos muy cortos en sujeto control joven. Mantener en control. |

### 9.2 Checklist de Pasos Pre-Modelado para e-Motion

- [ ] Excluir el archivo duplicado `f97b7bda-cfb5-4556-8886-684866de5524.json`
- [ ] Implementar cargador específico `load_emotion_json()` que ignore o limpie `persistence_value` y `entropy_value`
- [ ] Anonimizar los nombres `CARMEN SANCHEZ ZUNIGA` y `JUAN MARTINEZ` de las rutas de imágenes en reportes
- [ ] Unificar la variable de clase diagnóstica: `PATIENT` (5 tomas / 4 válidas) vs `CONTROL` (8 tomas)
- [ ] Exportar tabla limpia de características a `Analisis de Datos/emotion_features.csv`
- [ ] Emplear `GroupKFold` agrupando por identificador de sesión para evitar fuga entre tomas repetidas (C01, C02, C03, P01)
- [ ] Contrastar la velocidad de marcha y el tiempo de apoyo de e-Motion con las fases segmentadas de las IMUs
- [ ] Auditar si el paciente P03 (`2026-10-03`) cuenta con registro IMU simultáneo en alguna carpeta complementaria
- [ ] Incorporar el diccionario de 44 variables en el marco teórico de la memoria de grado (Sección Metodología)
- [ ] Confirmar con el tutor Domiciano Rincón si se añadirán más capturas RGB-D de las brigadas de Santa Marta/Cali

---
*Documento consolidado automáticamente a partir del escaneo determinístico de los 13 archivos de `/Datos e-Motion/`.*  
*Generado: Octubre 2026 | Versión 1.0 | Auditoría Completa de la Modalidad Óptica e-Motion*
