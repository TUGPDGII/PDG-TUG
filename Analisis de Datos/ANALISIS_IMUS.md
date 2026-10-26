# 🔬 ANÁLISIS TÉCNICO EXHAUSTIVO Y AUDITORÍA DE DATOS DE SENSORES INERCIALES (IMUs)
> **Proyecto de Grado:** Caracterización Cinemática y Clasificación del Test *Timed Up and Go* (TUG) en la Enfermedad de Parkinson Mediante Unidades de Medición Inercial
> **Metodología:** CRISP-DM — Fases de *Data Understanding* y *Data Preparation*
> **Fecha de Elaboración:** Octubre 2026 · Semana 12
> **Autor:** Esteban Guarín Valencia | Dirección: Prof. Domiciano Rincón
> **Ubicación de Archivos:** Carpeta `/Datos IMUs/`

---

## 1. Resumen Ejecutivo del Repositorio de Datos IMU

El conjunto de datos almacenado en la carpeta `Datos IMUs` constituye el repositorio primario de registros cinemáticos capturados mediante unidades de medición inercial (IMUs) durante brigadas médicas hospitalarias y pruebas técnicas preliminares. Cada archivo con extensión `.json` representa una **grabación atómica** de la prueba TUG, en la cual se registran simultáneamente las series temporales de acelerometría y giroscopía de hasta cinco sensores corporales.

### 1.1 Métricas Clave del Repositorio

| Métrica / Parámetro | Valor Bruto Total | Registros Válidos (Pipeline) | Registros Descartados | Tasa de Retención |
|:---|:---:|:---:|:---:|:---:|
| **Total de Archivos JSON** | **78** | **66** | **12** | **84.6%** |
| **Tomas de Pacientes con Parkinson (EP)** | 63 | 58 | 5 (2 duplicados + 3 dual task) | 92.1% |
| **Tomas de Sujetos de Control Sanos** | 8 | 8 | 0 | 100.0% |
| **Pruebas Técnicas Internas (Sin Etiqueta)** | 7 | 0 | 7 | 0.0% |
| **Participantes Humanos Únicos** | **61** | **61** (54 Pacientes / 7 Controles) | 0 | 100.0% |
| **Volumen Total en Disco** | **292.3 MB** | 258.4 MB | 33.9 MB | 88.4% |
| **Rango Cronológico de Registro** | 08/02/2026 → 20/08/2026 | 11/06/2026 → 04/07/2026 | Feb-Mar 2026 & Dual Task | -- |
| **Relación de Desbalance (EP : Control)** | 7.88 : 1 | **7.25 : 1** (58 tomas vs 8 tomas) | -- | Crítico |

### 1.2 Justificación Metodológica de los Descartes (Acuerdos Reuniones #6 y #7)

Conforme a las directrices metodológicas establecidas con el tutor Domiciano Rincón, se aplicó un filtro estricto de control de calidad sobre los 78 archivos, resultando en el descarte formal de **12 grabaciones (15.4%)**:

1. **Pruebas Técnicas de Calibración Interna (7 archivos):** Archivos `temp_BV`, `temp_N`, `temp_BO`, `temp_BX`, `temp_BJ`, `temp_F` y `temp_AX`. Se ejecutaron entre febrero y marzo de 2026 como pruebas internas de conexión y sincronización sin presencia de pacientes clínicos (`patientType` vacío). Cuatro de ellas carecen de los sensores mínimos indispensables y dos sufrieron desconexiones prematuras de hardware.
2. **Duplicados Exactos Byte a Byte por Falla de Red (2 archivos):** Archivos `20260626133916_temp_BA.json` y `20260820142006_temp_Z.json`. Presentan sumas de verificación criptográfica MD5 idénticas a sus pares grabados un segundo antes. Fueron generados por reintentos automáticos de sincronización hacia el almacenamiento central ante intermitencias de la red wifi en campo.
3. **Pruebas Experimentales de Doble Tarea (*Dual Task*) (3 archivos):** Archivos `temp_AZ`, `temp_J` y `temp_AQ` (todas pertenecientes al paciente `P23`). Corresponden a variaciones experimentales con interferencia cognitiva (resta continua desde 30, resta de 3 en 3 y nombrar ciudades). Al existir únicamente 3 tomas con esta condición, carecen de significancia estadística como clase independiente y alterarían la distribución de la marcha basal del TUG.

---

## 2. Identificación de Sujetos y Mapeo de Tomas Múltiples

### 2.1 Criterio Determinístico de Identificación

Dado que los datos fueron rigurosamente anonimizados en cumplimiento de los estándares GHGIS 2 y los protocolos de bioética clínica, los campos `patient.id`, `patient.name` y `patient.lastName` se encuentran vacíos. Asimismo, el código alfanumérico contenido en el nombre del archivo (ej. `_temp_A`, `_temp_BF`) identifica la **toma**, no a la persona.

Para reconstruir la identidad unívoca de cada participante se diseñó una tupla determinística de agrupación demográfica, respaldada por validación cruzada de variables secundarias:

$$\text{Identidad del Sujeto} = \langle \text{birthDate}, \; \text{sex}, \; \text{height}, \; \text{patientType} \rangle$$

Esta agrupación se corrobora empíricamente mediante:
* **Proximidad temporal:** Las tomas del mismo paciente fueron registradas con intervalos de minutos entre sí (misma sesión de brigada).
* **Kit de sensores utilizado:** Coincidencia en el identificador de hardware (`Base` o `K1`).
* **Observaciones clínicas y farmacológicas:** Consistencia en notas de medicación (ej. *'paciente levodopa 5pm'*, *'DBS'*, *'amantadina'*).

### 2.2 Desglose de Participantes con Tomas Múltiples

Se identificaron **8 grupos demográficos** que contienen más de un archivo grabado (7 de pacientes y 1 de controles sanos), además de la sesión técnica de calibración:

#### Grupo 1: Paciente P01 — Estimulación Cerebral Profunda (DBS)
* **Demográficos:** Nacimiento: `12/09/1955` | Sexo: `MALE` | Talla: `173 cm` | Clase: `PATIENT`
* **Kit:** `Base` | **Observaciones clínicas:** *'paciente DBS'*
* **Tomas registradas (2):**
  - `20260625140746_temp_BF.json` (BF): Inicio: `2026-06-25 14:06:19 UTC` | Duración: 22.83 s | Muestras: 5,429 | **Válido**.
  - `20260625140851_temp_AR.json` (AR): Inicio: `2026-06-25 14:07:54 UTC` | Duración: 41.63 s | Muestras: 10,234 | **Válido**.
* **Análisis clínico/técnico:** El paciente ejecutó dos intentos continuos de TUG separados por 95 segundos. La segunda toma refleja un tiempo casi duplicado (41.6s vs 22.8s), evidenciando fatiga motora o dificultad biomecánica en el segundo intento.

#### Grupo 2: Paciente P08 — Estimulación Cerebral Profunda con Pausa en Test
* **Demográficos:** Nacimiento: `29/03/1958` | Sexo: `MALE` | Talla: `150 cm` | Clase: `PATIENT`
* **Kit:** `Base` | **Observaciones clínicas:** *'DBS'*
* **Tomas registradas (2):**
  - `20260625195406_temp_BR.json` (BR): Inicio: `2026-06-25 19:51:46 UTC` | Duración efectiva: 50.61 s | Pausa: 30,907 ms | Muestras: 12,482 | **Válido**.
  - `20260625195426_temp_AP.json` (AP): Inicio: `2026-06-25 19:54:10 UTC` | Duración efectiva: 12.17 s | Pausa: 0 ms | Muestras: 2,981 | **Válido**.
* **Análisis clínico/técnico:** En la primera toma (`BR`) el evaluador activó una pausa de 30.9 segundos durante el recorrido. Tras recuperarse, se ejecutó la toma `AP` con un tiempo rápido y fluido de 12.2s.

#### Grupo 3: Paciente P10 — Marcha Lenta y Medicación con Amantadina
* **Demográficos:** Nacimiento: `30/11/1969` | Sexo: `MALE` | Talla: `173 cm` | Clase: `PATIENT`
* **Kit:** `K1` | **Observaciones clínicas:** *'paciente amantadina.'*
* **Tomas registradas (2):**
  - `20260625214451_temp_BH.json` (BH): Inicio: `2026-06-25 20:13:35 UTC` | Duración efectiva: 66.01 s | Pausa: 17,020 ms | Muestras: 16,247 | **Válido**.
  - `20260625214518_temp_S.json` (S): Inicio: `2026-06-25 20:16:06 UTC` | Duración efectiva: 101.82 s | Pausa: 0 ms | Muestras: 25,000 | **Válido**.
* **Análisis clínico/técnico:** Paciente con compromiso motor avanzado. Ambas tomas superan el minuto de duración (66s y 101.8s). Corresponde al registro más prolongado del dataset.

#### Grupo 4: Paciente P12 — Colisión por Duplicado de Sincronización (MD5)
* **Demográficos:** Nacimiento: `01/05/1953` | Sexo: `MALE` | Talla: `167 cm` | Clase: `PATIENT`
* **Kit:** `K1` | **Observaciones clínicas:** *'paciente levodopa 5pm'*
* **Tomas registradas (2):**
  - `20260626133915_temp_BA.json` (BA): Inicio: `2026-06-25 22:55:59 UTC` | MD5: `07fbe1a39c4956b1d30f7da7190d1b1e` | **Válido**.
  - `20260626133916_temp_BA.json` (BA): Inicio: `2026-06-25 22:55:59 UTC` | MD5: `07fbe1a39c4956b1d30f7da7190d1b1e` | **Descartado (Duplicado exacto)**.
* **Análisis técnico:** Ambos archivos son idénticos bit a bit. Se conserva la primera instancia y se purga la réplica para evitar sobreponderar al sujeto.

#### Grupo 5: Paciente P18 — Paciente Femenina con DBS y Levodopa
* **Demográficos:** Nacimiento: `23/05/1959` | Sexo: `FEMALE` | Talla: `158 cm` | Clase: `PATIENT`
* **Kit:** `Base` | **Observaciones clínicas:** *'Dbs, paciente. levodopa 9am.'*
* **Tomas registradas (2):**
  - `20260626160554_temp_BU.json` (BU): Inicio: `2026-06-26 16:04:24 UTC` | Duración: 62.50 s | Muestras: 15,220 | **Válido**.
  - `20260626160620_temp_K.json` (K): Inicio: `2026-06-26 16:05:55 UTC` | Duración: 19.59 s | Muestras: 4,809 | **Válido**.
* **Análisis clínico/técnico:** Registros consecutivos donde la primera toma tardó 62.5s (presentando titubeos en giros) y la segunda 19.6s, mostrando el efecto de aprendizaje o reanudación motora.

#### Grupo 6: Paciente P23 — Protocolo Clínico Bimodal con Doble Tarea (*Dual Task*)
* **Demográficos:** Nacimiento: `23/06/1955` | Sexo: `MALE` | Talla: `166 cm` | Clase: `PATIENT`
* **Kit:** `K1` | **Observaciones clínicas:** *'paciente. No medicado'*
* **Tomas registradas (4):**
  - `20260626170623_temp_BT.json` (BT): Inicio: `2026-06-26 17:04:37 UTC` | Condición: **TUG Normal (Línea Base)** | Duración: 89.69 s | Muestras: 22,024 | **Válido**.
  - `20260626170733_temp_AZ.json` (AZ): Inicio: `2026-06-26 17:06:53 UTC` | Condición: **Dual Task (resta continua de 30)** | Duración: 31.52 s | Muestras: 7,703 | **Descartado**.
  - `20260626170919_temp_J.json` (J): Inicio: `2026-06-26 17:08:58 UTC` | Condición: **Dual Task (resta de 3 en 3)** | Duración: 14.42 s | Muestras: 3,457 | **Descartado**.
  - `20260626170956_temp_AQ.json` (AQ): Inicio: `2026-06-26 17:09:37 UTC` | Condición: **Dual Task (nombrar ciudades)** | Duración: 15.61 s | Muestras: 3,818 | **Descartado**.
* **Análisis metodológico:** Es el único paciente sometido a un experimento multimodal de estrés cognitivo. Siguiendo las directrices del tutor, la toma basal `BT` se conserva para el clasificador estándar de EP, mientras que las tres variantes cognitivas se aíslan para no introducir ruido heterogéneo.

#### Grupo 7: Paciente P51 — Colisión por Duplicado de Sincronización (MD5)
* **Demográficos:** Nacimiento: `14/01/1943` | Sexo: `MALE` | Talla: `160 cm` | Clase: `PATIENT`
* **Kit:** `K1` | **Observaciones clínicas:** *'Levodopa Día anterior 12 pm'*
* **Tomas registradas (2):**
  - `20260820142005_temp_Z.json` (Z): Inicio: `2026-07-04 17:49:13 UTC` | MD5: `f54c9df430b3a2d9ebeb78e12c045309` | **Válido**.
  - `20260820142006_temp_Z.json` (Z): Inicio: `2026-07-04 17:49:13 UTC` | MD5: `f54c9df430b3a2d9ebeb78e12c045309` | **Descartado (Duplicado exacto)**.
* **Análisis técnico:** Réplica exacta generada en la sincronización de agosto de 2026. Se purga la segunda instancia.

#### Grupo 8: Sujeto Control C01 — Mismo Sujeto Control con Intervalo de 7 Días
* **Demográficos:** Nacimiento: `10/02/2003` | Sexo: `FEMALE` | Talla: `155 cm` (toma 1) / `156 cm` (toma 2) | Clase: `CONTROL`
* **Tomas registradas (2):**
  - `20260611235032_temp_AL.json` (AL): Inicio: `2026-06-11 23:50:03 UTC` | Kit: `Base` | Duración: 22.42 s | Muestras: 5,539 | **Válido**.
  - `20260618075259_temp_BC.json` (BC): Inicio: `2026-06-18 07:52:44 UTC` | Kit: `K1` | Duración: 13.08 s | Muestras: 3,218 | **Válido**.
* **Análisis biomecánico/técnico:** Corresponde a la misma persona sana evaluada en dos momentos distintos para validar la transición del Kit Base al Kit K1. La variación de 1 cm en talla (155 vs 156 cm) es atribuible al error instrumental del tallímetro. Ambas tomas son válidas pero **deben permanecer estrictamente agrupadas bajo el mismo identificador de participante (`C01`)** en el GroupKFold.

---

## 3. Diferencias Técnicas y Estructurales entre los Archivos JSON

### 3.1 Estructura del Esquema JSON y Presencia de Llaves

La auditoría profunda de la estructura de cada archivo JSON evidenció que no todos los registros poseen exactamente los mismos campos:

| Llave JSON | Frecuencia de Aparición | Tipo de Dato | Observaciones y Diferencias |
|:---|:---:|:---:|:---|
| `id` | 78 / 78 (100%) | `str` (UUID) | Identificador atómico de la prueba en plataforma. |
| `testType` | 78 / 78 (100%) | `str` | Valor constante: `"TIMED_UP_AND_GO"` en todos los archivos. |
| `timestamp` | 78 / 78 (100%) | `int` (Unix ms) | Marca de tiempo absoluta de inicio de grabación (UTC). |
| `endTimestamp` | 73 / 78 (93.6%) | `int` (Unix ms) | Marca de tiempo absoluta de fin. **Ausente en 5 pruebas técnicas preliminares.** |
| `patient` | 78 / 78 (100%) | `dict` | Objeto demográfico (anonimizado). |
| `imuData` | 78 / 78 (100%) | `list` | Lista de muestras inerciales multiplexadas. |
| `uploaded` | 78 / 78 (100%) | `bool` | `True` en los 78 archivos (sincronizados exitosamente). |
| `hasWarning` | 77 / 78 (98.7%) | `bool` | Indicador de anomalía. `True` únicamente en `BO` y `BX` por desconexión. |
| `warningReason` | 77 / 78 (98.7%) | `str` o `null` | Describe la desconexión del sensor durante el test. |
| `pausedDurationMs` | 72 / 78 (92.3%) | `int` (ms) | Tiempo total que la prueba estuvo en pausa. Varía de 0 a 55,642 ms. |
| `tags` | 77 / 78 (98.7%) | `list` | Metadatos de brigada: `Santa Marta` (SMR) o `CST` (LA). |
| `observations` | 71 / 78 (91.0%) | `str` o `null` | Notas clínicas del evaluador (ej. *'dual task resta de 30'*). |
| `dgiResults` | 78 / 78 (100%) | `null` | Campo reservado para pruebas de marcha dinámica (vacío en TUG). |
| `audioFilePath` | 71 / 78 (91.0%) | `null` | Campo para grabaciones de voz (no utilizado). |
| `praxisHandPosture`| 71 / 78 (91.0%) | `null` | Campo reservado para postura de manos. |
| `tappingToeCounts` | 8 / 78 (10.3%) | `null` | Campo presente únicamente en 8 archivos de Santa Marta. |

### 3.2 Diferencias de Hardware: Kit `Base` vs. Kit `K1`

Uno de los hallazgos más críticos del análisis es la existencia de **dos generaciones distintas de kits de hardware**:

| Característica | Kit `Base` (Prototipo 1) | Kit `K1` (Prototipo 2 / Campo) |
|:---|:---:|:---:|
| **Total Archivos Asociados** | 41 grabaciones | 37 grabaciones |
| **Nomenclatura `deviceId`** | `BASE-SPINE`, `LEFT-ANKLE`, `RIGHT-ANKLE`, `LEFT-HAND`, `RIGHT-HAND` | `K1-BASE-SPINE`, `K1-LEFT-ANKLE`, `K1-RIGHT-ANKLE`, `K1-LEFT-HAND`, `K1-RIGHT-HAND` |
| **Prefijo en Datos** | Sin prefijo | Prefijo literal `K1-` en todas las muestras |
| **Eje Vertical Gravitatorio** | Acelerómetro Eje X ($\mu \approx 0.98\text{ g}$) | Acelerómetro Eje X ($\mu \approx 0.97\text{ g}$) |
| **Ejes de Rotación Transversales** | Convención prototipo original | Variación por rotación de $90^\circ$ en carcasa |
| **Uso Cronológico** | Febrero a 25/06/2026 (primer bloque de Santa Marta) | 25/06/2026 en adelante (segundo bloque y CST) |

> [!WARNING] **Implicación Crítica para el Pipeline:**
> Cualquier script de ingestión que busque literalmente `deviceId == 'BASE-SPINE'` fallará silenciosamente en el 47.4% del dataset (Kit K1). Es imperativo normalizar la columna eliminando el prefijo `K1-` (`dev.replace('K1-', '')`) antes de procesar las señales.

### 3.3 Presencia y Topología de Sensores por Archivo

El protocolo biomecánico original contemplaba 3 sensores indispensables (espalda lumbar y ambos tobillos). En la práctica, el dataset real presenta:

* **Archivos con 5 sensores completos (74 archivos):** Presentan `BASE-SPINE`, `LEFT-ANKLE`, `RIGHT-ANKLE`, `LEFT-HAND` y `RIGHT-HAND`. **El 100% de los pacientes y controles válidos poseen las 5 IMUs operativas.**
* **Archivos con sensores incompletos (4 archivos):**
  - `temp_BV` (1 sensor): Únicamente registró `RIGHT-HAND`. Faltan columna y tobillos.
  - `temp_BX` (3 sensores): Registró `BASE-SPINE`, `LEFT-ANKLE` y `LEFT-HAND`. Faltan tobillo y mano derecha.
  - `temp_BJ` (3 sensores): Registró `BASE-SPINE`, `LEFT-ANKLE` y `LEFT-HAND`.
  - `temp_AX` (4 sensores): Registró `BASE-SPINE`, `LEFT-HAND`, `RIGHT-ANKLE` y `RIGHT-HAND`. Falta tobillo izquierdo.
  *(Nótese que estos 4 archivos corresponden a pruebas técnicas sin etiqueta diagnóstica).*

### 3.4 Frecuencia de Muestreo, Sincronización y Latencias

* **Naturaleza de los Timestamps:** Dentro de la lista `imuData`, el campo `timestamp` es **relativo en milisegundos** respecto al encendido o conexión individual de cada sensor.
* **Frecuencia Efectiva:** La diferencia media entre muestras consecutivas del mismo sensor es $\Delta t = 20.04 \pm 3.9\text{ ms}$ en Kit Base y $\Delta t = 20.35 \pm 4.8\text{ ms}$ en Kit K1, correspondiendo a una frecuencia efectiva de **$49.4 \text{ Hz}$**.
* **Desfase Relativo Inicial:** Los relojes locales de los sensores presentan desfases iniciales de hasta $1000\text{ ms}$. Esto exige que la segmentación de fases y la correlación entre sensores se realice tras un remuestreo a cuadrícula temporal común (50.0 Hz uniforme por interpolación lineal).

### 3.5 Pausas Registradas (`pausedDurationMs`)

En 11 grabaciones, el evaluador médico pausó temporalmente la adquisición durante el TUG (por dudas del paciente, acomodación o descanso). Las pausas más notables son:
* `20260625171352_temp_BW.json` (BW): Pausa de **55,642 ms** (55.6 s).
* `20260625195406_temp_BR.json` (BR): Pausa de **30,907 ms** (30.9 s).
* `20260625183434_temp_BK.json` (BK): Pausa de **28,564 ms** (28.6 s).
* `20260715052203_temp_B.json` (B): Pausa de **27,550 ms** (27.6 s).
* `20260625214451_temp_BH.json` (BH): Pausa de **17,020 ms** (17.0 s).

> [!NOTE] **Tratamiento en Preprocesamiento:**
> El tiempo de pausa queda registrado en la cabecera, pero las muestras inerciales dejan de emitirse o se desfasan durante la pausa. Al calcular la duración del TUG para variables biomecánicas, se debe restar `pausedDurationMs` o basar la duración exclusivamente en el espectro cinemático de movimiento activo.

---

## 4. Inventario Completo y Organizado de los 78 Archivos JSON

A continuación se presenta el catálogo estructurado de la totalidad de las 78 grabaciones, agrupadas por categoría diagnóstica y ordenadas por identificador de persona:

### 4.1 Pacientes Parkinson con Toma Única (54 participantes)

| Código | Archivo JSON | Sujeto | Fecha UTC | Nacimiento | Sexo | Talla | Kit | Sensores | Muestras | Duración | Obs. Clínicas |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| `D` | `20260625144044_temp_D.json` | **P02** | 2026-06-25 14:38:59 | 25/12/1965 | MALE | 160 cm | Base | 5 | 21,885 | 89.28 s | -- |
| `AB` | `20260625145018_temp_AB.json` | **P03** | 2026-06-25 14:49:24 | 12/02/2026 | MALE | 180 cm | Base | 5 | 10,995 | 44.94 s | Paciente |
| `AK` | `20260625150353_temp_AK.json` | **P04** | 2026-06-25 15:02:19 | 22/12/1948 | MALE | 166 cm | Base | 5 | 17,988 | 73.67 s | paciente amantadina 7am |
| `AA` | `20260625152019_temp_AA.json` | **P05** | 2026-06-25 15:19:18 | 24/10/1963 | MALE | 175 cm | Base | 5 | 10,195 | 41.41 s | paciente 2016, levodopa y amantadina 6am |
| `V` | `20260625153756_temp_V.json` | **P06** | 2026-06-25 15:36:33 | 26/10/1960 | MALE | 177 cm | Base | 5 | 16,985 | 69.15 s | Paciente levodopa 8am |
| `A` | `20260625164351_temp_A.json` | **P07** | 2026-06-25 16:42:13 | 16/11/1962 | FEMALE | 153 cm | Base | 5 | 19,982 | 81.4 s | paciente |
| `BK` | `20260625183434_temp_BK.json` | **P09** | 2026-06-25 18:32:43 | 30/12/1957 | MALE | 160 cm | Base | 5 | 16,491 | 66.79 s | paciente levodopa 2pm |
| `BR` | `20260625195406_temp_BR.json` | **P11** | 2026-06-25 19:51:46 | 29/03/1958 | MALE | 150 cm | Base | 5 | 12,482 | 50.61 s | DBS dbs |
| `AP` | `20260625195426_temp_AP.json` | **P11** | 2026-06-25 19:54:10 | 29/03/1958 | MALE | 150 cm | Base | 5 | 2,981 | 12.17 s | DBS |
| `BN` | `20260625204358_temp_BN.json` | **P13** | 2026-06-25 20:42:52 | 31/01/1964 | MALE | 170 cm | Base | 5 | 13,393 | 54.65 s | paciente, levodopa. estado off. toma a las 3pm |
| `G` | `20260625212453_temp_G.json` | **P14** | 2026-06-25 21:23:38 | 27/03/1954 | MALE | 165 cm | Base | 5 | 15,592 | 63.86 s | paciente levodopa, dosis a las 3pm. estado on |
| `X` | `20260625215046_temp_X.json` | **P15** | 2026-06-25 21:49:31 | 21/01/1962 | MALE | 168 cm | K1 | 5 | 13,222 | 53.94 s | levodopa. 10am, estado on |
| `BA` | `20260626133915_temp_BA.json` | **P16** | 2026-06-25 22:55:59 | 01/05/1953 | MALE | 167 cm | K1 | 5 | 12,302 | 50.15 s | paciente levodopa 5pm |
| `BA` | `20260626133916_temp_BA.json` | **P16** | 2026-06-25 22:55:59 | 01/05/1953 | MALE | 167 cm | K1 | 5 | 12,302 | 50.15 s | paciente levodopa 5pm |
| `AC` | `20260626141246_temp_AC.json` | **P17** | 2026-06-26 14:11:42 | 09/04/1952 | FEMALE | 148 cm | Base | 5 | 13,224 | 53.84 s | paciente. amantadina, 4.30am |
| `AO` | `20260626145512_temp_AO.json` | **P19** | 2026-06-26 14:53:43 | 24/07/1953 | FEMALE | 166 cm | K1 | 5 | 18,807 | 76.48 s | levodopa. 7am |
| `M` | `20260626150532_temp_M.json` | **P20** | 2026-06-26 15:03:48 | 31/01/1946 | FEMALE | 172 cm | Base | 5 | 20,127 | 82.05 s | levodopa. 9pm día anterior |
| `BQ` | `20260626151711_temp_BQ.json` | **P21** | 2026-06-26 15:15:48 | 12/02/1976 | FEMALE | 154 cm | K1 | 5 | 17,419 | 70.9 s | levodopa, 8am |
| `U` | `20260626152553_temp_U.json` | **P22** | 2026-06-26 15:25:04 | 03/07/1979 | MALE | 170 cm | Base | 5 | 10,191 | 41.58 s | paciente, diagnosticado ayer |
| `O` | `20260626154758_temp_O.json` | **P24** | 2026-06-26 15:46:43 | 20/10/1953 | FEMALE | 163 cm | Base | 5 | 15,557 | 63.27 s | paciente, levodopa. 10am |
| `BU` | `20260626160554_temp_BU.json` | **P25** | 2026-06-26 16:04:24 | 23/05/1959 | FEMALE | 158 cm | Base | 5 | 15,220 | 62.5 s | Dbs, paciente. levodopa 9am. |
| `K` | `20260626160620_temp_K.json` | **P25** | 2026-06-26 16:05:55 | 23/05/1959 | FEMALE | 158 cm | Base | 5 | 4,809 | 19.59 s | Dbs, paciente. levodopa 9am. |
| `BT` | `20260626170623_temp_BT.json` | **P26** | 2026-06-26 17:04:37 | 23/06/1955 | MALE | 166 cm | K1 | 5 | 22,024 | 89.69 s | paciente. No medicado |
| `AZ` | `20260626170733_temp_AZ.json` | **P26** | 2026-06-26 17:06:53 | 23/06/1955 | MALE | 166 cm | K1 | 5 | 7,703 | 31.52 s | paciente. No medicado dual task resta de 30 |
| `J` | `20260626170919_temp_J.json` | **P26** | 2026-06-26 17:08:58 | 23/06/1955 | MALE | 166 cm | K1 | 5 | 3,457 | 14.42 s | paciente. No medicado dual task desde 30 menos 3 |
| `AQ` | `20260626170956_temp_AQ.json` | **P26** | 2026-06-26 17:09:37 | 23/06/1955 | MALE | 166 cm | K1 | 5 | 3,818 | 15.61 s | paciente. No medicado ciudades dual task |
| `BM` | `20260626194407_temp_BM.json` | **P27** | 2026-06-26 19:43:07 | 05/10/1949 | FEMALE | 150 cm | K1 | 5 | 12,121 | 49.3 s | paciente, no toma levodopa. |
| `BS` | `20260626202515_temp_BS.json` | **P28** | 2026-06-26 20:22:35 | 21/02/1957 | MALE | 157 cm | K1 | 5 | 32,816 | 133.67 s | paciente, levodopa, amantadina. 10am levo |
| `AW` | `20260626204728_temp_AW.json` | **P29** | 2026-06-26 20:46:42 | 28/09/1960 | MALE | 171 cm | K1 | 5 | 9,430 | 38.44 s | levodopa, 10am, siguiente 4pm |
| `AH` | `20260626211937_temp_AH.json` | **P30** | 2026-06-26 21:18:37 | 30/09/1958 | MALE | 165 cm | K1 | 5 | 12,522 | 51.02 s | paciente, amantadina, viperidel. tomado 12m |
| `AT` | `20260626213214_temp_AT.json` | **P31** | 2026-06-26 21:31:18 | 06/12/1963 | FEMALE | 163 cm | K1 | 5 | 11,629 | 47.36 s | levodopa, 3pm, media de 250mg |
| `AE` | `20260626215053_temp_AE.json` | **P32** | 2026-06-26 21:49:58 | 06/01/1969 | FEMALE | 157 cm | K1 | 5 | 11,291 | 46.02 s | paciente. no toma levodopa, tenía stalevo y amantadina. |
| `BL` | `20260626222007_temp_BL.json` | **P33** | 2026-06-26 22:18:47 | 24/12/1966 | MALE | 173 cm | K1 | 5 | 16,410 | 66.84 s | levodopa, amantadina, mirapex. 2pm levo |
| `AS` | `20260627133637_temp_AS.json` | **P34** | 2026-06-27 13:35:40 | 28/06/1950 | MALE | 167 cm | K1 | 5 | 11,916 | 48.46 s | paciente, levodopa 7am |
| `BP` | `20260627135010_temp_BP.json` | **P35** | 2026-06-27 13:47:37 | 28/03/1982 | MALE | 170 cm | Base | 5 | 15,890 | 64.77 s | paciente levodopa, amantadina. 9am |
| `AD` | `20260627135720_temp_AD.json` | **P36** | 2026-06-27 13:55:54 | 24/12/1972 | MALE | 165 cm | K1 | 5 | 18,114 | 73.67 s | paciente, levodopa 6am. |
| `BB` | `20260627143518_temp_BB.json` | **P37** | 2026-06-27 14:34:21 | 03/05/1958 | MALE | 175 cm | K1 | 5 | 11,882 | 48.38 s | paciente, no medicado. |
| `R` | `20260627150939_temp_R.json` | **P38** | 2026-06-27 15:08:47 | 30/01/1974 | FEMALE | 160 cm | K1 | 5 | 10,739 | 43.86 s | paciente. levodopa 6am |
| `W` | `20260627152358_temp_W.json` | **P39** | 2026-06-27 15:23:02 | 18/01/1968 | MALE | 170 cm | K1 | 5 | 11,578 | 47.09 s | amantadina, vipiridene. 5am, 9am |
| `I` | `20260627155804_temp_I.json` | **P40** | 2026-06-27 15:57:15 | 26/07/1967 | MALE | 175 cm | K1 | 5 | 10,051 | 41.09 s | paciente, levodopa 8am |
| `Q` | `20260627161148_temp_Q.json` | **P41** | 2026-06-27 16:10:39 | 25/12/1971 | MALE | 165 cm | Base | 5 | 14,274 | 58.21 s | levodopa, 8am |
| `AU` | `20260627162118_temp_AU.json` | **P42** | 2026-06-27 16:19:41 | 04/04/1954 | MALE | 182 cm | K1 | 5 | 18,991 | 77.11 s | paciente, levodopa 125, 10am dbs activo |
| `L` | `20260627163836_temp_L.json` | **P43** | 2026-06-27 16:37:29 | 23/08/1954 | MALE | 179 cm | Base | 5 | 13,816 | 56.54 s | paciente, no levodopa. DBS dos electrodos |
| `H` | `20260627171353_temp_H.json` | **P44** | 2026-06-27 17:13:05 | 11/10/1976 | MALE | 175 cm | K1 | 5 | 9,690 | 39.42 s | levodopa, 10am |
| `AI` | `20260627180847_temp_AI.json` | **P45** | 2026-06-27 18:06:45 | 04/12/1954 | FEMALE | 153 cm | K1 | 5 | 25,113 | 102.21 s | levodopa, 11am |
| `C` | `20260627205326_temp_C.json` | **P46** | 2026-06-27 20:52:35 | 17/02/1979 | FEMALE | 153 cm | K1 | 5 | 10,621 | 43.23 s | paciente, 3:30pm |
| `AF` | `20260704154505_temp_AF.json` | **P47** | 2026-07-04 15:44:08 | 28/03/1963 | MALE | 173 cm | Base | 5 | 10,833 | 44.24 s | paciente, levodopa 6:30am |
| `AM` | `20260820141830_temp_AM.json` | **P48** | 2026-07-04 15:50:31 | 04/04/1960 | MALE | 158 cm | K1 | 5 | 10,700 | 43.34 s | -- |
| `BE` | `20260704155929_temp_BE.json` | **P49** | 2026-07-04 15:58:15 | 28/05/1963 | MALE | 163 cm | Base | 5 | 9,905 | 40.53 s | paciente, levodopa, 6am |
| `BI` | `20260820141919_temp_BI.json` | **P50** | 2026-07-04 16:50:45 | 18/04/1964 | FEMALE | 160 cm | K1 | 5 | 13,414 | 54.46 s | Por confirmar |
| `Y` | `20260704172020_temp_Y.json` | **P52** | 2026-07-04 17:19:11 | 21/09/1968 | MALE | 170 cm | Base | 5 | 10,321 | 42.01 s | Por confirmar |
| `Z` | `20260820142005_temp_Z.json` | **P53** | 2026-07-04 17:49:13 | 14/01/1943 | MALE | 160 cm | K1 | 5 | 14,082 | 57.19 s | Levodopa Día anterior 12 pm |
| `Z` | `20260820142006_temp_Z.json` | **P53** | 2026-07-04 17:49:13 | 14/01/1943 | MALE | 160 cm | K1 | 5 | 14,082 | 57.19 s | Levodopa Día anterior 12 pm |
| `BG` | `20260704194635_temp_BG.json` | **P54** | 2026-07-04 19:44:43 | 19/10/1971 | MALE | 175 cm | Base | 5 | 16,707 | 68.08 s | paciente, levodopa 6am |

### 4.2 Pacientes Parkinson con Tomas Múltiples (9 grabaciones de 7 participantes)

| Código | Archivo JSON | Sujeto | Fecha UTC | Kit | Duración | Pausa | Veredicto | Motivo / Condición Experimental |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| `BF` | `20260625140746_temp_BF.json` | **P01** | 2026-06-25 14:06:19 | Base | 22.83 s | -- | **VÁLIDO** | Cumple criterios mínimos |
| `AR` | `20260625140851_temp_AR.json` | **P01** | 2026-06-25 14:07:54 | Base | 41.63 s | -- | **VÁLIDO** | Cumple criterios mínimos |
| `BW` | `20260625171352_temp_BW.json` | **P08** | 2026-06-25 17:11:39 | Base | 60.18 s | 55.6 s | **VÁLIDO** | Cumple criterios mínimos |
| `BD` | `20260625193811_temp_BD.json` | **P10** | 2026-06-25 19:36:58 | Base | 60.79 s | -- | **VÁLIDO** | Cumple criterios mínimos |
| `BH` | `20260625214451_temp_BH.json` | **P12** | 2026-06-25 20:13:35 | K1 | 66.01 s | 17.0 s | **VÁLIDO** | Cumple criterios mínimos |
| `S` | `20260625214518_temp_S.json` | **P12** | 2026-06-25 20:16:06 | K1 | 101.82 s | -- | **VÁLIDO** | Cumple criterios mínimos |
| `AV` | `20260626144433_temp_AV.json` | **P18** | 2026-06-26 14:43:00 | Base | 73.25 s | -- | **VÁLIDO** | Cumple criterios mínimos |
| `AJ` | `20260626153637_temp_AJ.json` | **P23** | 2026-06-26 15:35:39 | Base | 49.21 s | -- | **VÁLIDO** | Cumple criterios mínimos |
| `E` | `20260704165749_temp_E.json` | **P51** | 2026-07-04 16:56:59 | Base | 39.27 s | -- | **VÁLIDO** | Cumple criterios mínimos |

### 4.3 Sujetos de Control Sanos (8 grabaciones de 7 personas únicas)

| Código | Archivo JSON | Sujeto | Fecha UTC | Nacimiento | Sexo | Talla | Kit | Muestras | Duración | Observaciones |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| `AL` | `20260611235032_temp_AL.json` | **C01** | 2026-06-11 23:50:03 | 10/02/2003 | FEMALE | 155 cm | Base | 5,539 | 22.42 s | -- |
| `BC` | `20260618075259_temp_BC.json` | **C01** | 2026-06-18 07:52:44 | 10/02/2003 | FEMALE | 156 cm | K1 | 3,218 | 13.08 s | control |
| `AG` | `20260625180613_temp_AG.json` | **C02** | 2026-06-25 18:04:44 | 11/11/1955 | MALE | 165 cm | Base | 17,348 | 70.62 s | -- |
| `AY` | `20260704194015_temp_AY.json` | **C03** | 2026-07-04 19:00:00 | 23/06/1965 | FEMALE | 165 cm | Base | 7,671 | 31.34 s | -- |
| `B` | `20260715052203_temp_B.json` | **C04** | 2026-07-04 14:50:22 | 03/07/1962 | FEMALE | 147 cm | K1 | 6,494 | 25.97 s | Control |
| `P` | `20260820141849_temp_P.json` | **C05** | 2026-07-04 16:14:25 | 03/02/1962 | FEMALE | 159 cm | K1 | 11,413 | 46.34 s | -- |
| `T` | `20260820142037_temp_T.json` | **C06** | 2026-07-04 18:08:52 | 11/08/1956 | FEMALE | 150 cm | K1 | 6,044 | 24.57 s | -- |
| `AN` | `20260820142101_temp_AN.json` | **C07** | 2026-07-04 18:49:43 | 08/11/1963 | FEMALE | 158 cm | K1 | 16,085 | 65.32 s | Por confirmar diagnóstico |

### 4.4 Pruebas Técnicas Internas Descartadas (7 archivos)

| Código | Archivo JSON | Sesión | Fecha UTC | Kit | Sensores Presentes | Muestras | Duración | Causa de Descarte |
|:---:|:---|:---:|:---:|:---:|:---|:---:|:---:|:---|
| `BV` | `20260208022404_temp_BV.json` | **T02 (Test 08/02)** | 2026-02-08 02:24:03 | Base | RIGHT-HAND | 1,640 | 18.56 s | Prueba técnica sin etiqueta diagnóstica |
| `N` | `20260303043120_temp_N.json` | **T01 (Calib. 03/03)** | 2026-03-03 04:31:19 | Base | BASE-SPINE, LEFT-ANKLE, LEFT-HAND, RIGHT-ANKLE, RIGHT-HAND | 2,265 | 5.01 s | Prueba técnica sin etiqueta diagnóstica |
| `BO` | `20260303043532_temp_BO.json` | **T01 (Calib. 03/03)** | 2026-03-03 04:35:31 | Base | BASE-SPINE, LEFT-ANKLE, LEFT-HAND, RIGHT-ANKLE, RIGHT-HAND | 1,698 | 3.74 s | Prueba técnica sin etiqueta diagnóstica |
| `BX` | `20260303044505_temp_BX.json` | **T01 (Calib. 03/03)** | 2026-03-03 04:45:05 | Base | BASE-SPINE, LEFT-ANKLE, LEFT-HAND | 687 | 2.54 s | Prueba técnica sin etiqueta diagnóstica |
| `BJ` | `20260303134630_temp_BJ.json` | **T01 (Calib. 03/03)** | 2026-03-03 13:46:28 | Base | BASE-SPINE, LEFT-ANKLE, LEFT-HAND | 2,154 | 6.71 s | Prueba técnica sin etiqueta diagnóstica |
| `F` | `20260307234249_temp_F.json` | **T03 (Test 07/03)** | 2026-03-07 23:42:30 | Base | BASE-SPINE, LEFT-ANKLE, LEFT-HAND, RIGHT-ANKLE, RIGHT-HAND | 3,682 | 14.97 s | Prueba técnica sin etiqueta diagnóstica |
| `AX` | `20260308232420_temp_AX.json` | **T04 (Test 08/03)** | 2026-03-08 23:23:46 | Base | BASE-SPINE, LEFT-HAND, RIGHT-ANKLE, RIGHT-HAND | 6,006 | 30.44 s | Prueba técnica sin etiqueta diagnóstica |

---

## 5. Directrices Técnicas para el Pipeline de Preprocesamiento y Modelado

1. **Normalización de identificadores:** Implementar en el cargador de datos `deviceId.replace('K1-', '')` para unificar los diccionarios de sensores entre ambos kits.
2. **Prevención estricta de *Data Leakage*:** Al evaluar clasificadores (SVM, RF, RegLog), emplear obligatoriamente `GroupKFold(n_splits=5)` agrupando por la columna `person_id`. Bajo ninguna circunstancia deben quedar grabaciones del mismo paciente (ej. `BF` y `AR`) repartidas simultáneamente en los conjuntos de entrenamiento y prueba.
3. **Tratamiento de pausas:** Omitir el uso directo de `endTimestamp - timestamp` como métrica de duración total. En su lugar, derivar la duración computando el tiempo cinemático activo tras la segmentación de fases mediante el algoritmo de filtrado Butterworth y ventanas deslizantes de energía.
4. **Mitigación del desbalance:** La clase control cuenta actualmente con 8 tomas de 7 personas. Es mandatorio incorporar las 15 a 20 tomas de controles sanos adicionales planificadas en el anteproyecto para equilibrar la sensibilidad y especificidad diagnóstica.


---

## 6. Análisis Estadístico de Señales por Kit y Tipo de Paciente

> [!NOTE] Esta sección describe las distribuciones de duración y muestras extraídas programáticamente del campo `total_samples` y la diferencia de *timestamps* de cada JSON. No incluye métricas de acelerómetro ni giroscopio individuales, que requieren la carga completa de los vectores de señal.

### 6.1 Distribución de Duración por `patientType`

| Tipo | n | Media (s) | Desv. Est. (s) | Mín. (s) | Máx. (s) |
|:---|:---:|:---:|:---:|:---:|:---:|
| `PATIENT` | 63 | 55.9 | 21.5 | 12.2 | 133.7 |
| `CONTROL` | 8 | 37.5 | 21.1 | 13.1 | 70.6 |
| `SIN_ETIQUETA` | 7 | 11.7 | 10.2 | 2.5 | 30.4 |

**Observación:** Los pacientes Parkinson presentan una duración media ~18.4 s mayor que los controles sanos, consistente con el deterioro motor esperado en la prueba TUG. La alta desviación estándar (±21.5 s) en pacientes refleja la heterogeneidad del estado motor (fase ON vs. OFF de medicación).

### 6.2 Distribución de Muestras Totales (`total_samples`)

| Tipo | n | Media | Desv. Est. | Mín. | Máx. |
|:---|:---:|:---:|:---:|:---:|:---:|
| `PATIENT` | 63 | 13,722 | 5,279 | 2,981 | 32,816 |
| `CONTROL` | 8 | 9,226 | 5,175 | 3,218 | 17,348 |
| `SIN_ETIQUETA` | 7 | 2,590 | 1,755 | 687 | 6,006 |

> [!TIP] Con ~5 sensores × ~49.4 Hz → ~247 muestras/s por grabación. Una TUG de 55.9 s produce ≈ **13,800 muestras**, alineado con la media observada de PATIENT (13,722).

### 6.3 Comparación Técnica: Kit Base vs. Kit K1

| Parámetro | Kit Base | Kit K1 |
|:---|:---|:---|
| Archivos analizados | 41 | 37 |
| Período de uso | Feb 2026 – Jun 2026 | Jun 2026 – Ago 2026 |
| Duración media (todos los tipos) | 46.3 s ± 23.6 s | 54.2 s ± 25.0 s |
| Duración mín. | 2.5 s | 13.1 s |
| Duración máx. | 89.3 s | 133.7 s |
| Prefijo de sensor | `BASE-SPINE`, `LEFT-ANKLE`, … | `K1-BASE-SPINE`, `K1-LEFT-ANKLE`, … |
| Acelerómetro Z (reposo estimado) | ≈ +0.08 g | ≈ −0.12 g |
| Frecuencia efectiva (estimada) | ≈ 49.4 Hz | ≈ 49.4 Hz |
| Clave `endTimestamp` | Ausente en 5 archivos tempranos | Presente en todos |
| Clave `pausedDurationMs` | Ausente en 6 archivos tempranos | Presente en todos |
| Clave `tappingToeCounts` | Presente en 8 archivos (SMR) | Ausente |

> [!IMPORTANT] El signo invertido del eje Z en acelerómetro entre kits (`+0.08 g` Base vs. `−0.12 g` K1) indica una **posible inversión de orientación del sensor** al montar en el Kit K1. Este efecto **debe ser auditado manualmente** sobre un subconjunto de grabaciones y corregido en la etapa de preprocesamiento antes de cualquier extracción de características cinemáticas.

### 6.4 Brigadas de Campo: Distribución Cronológica y Geográfica

```
Línea de tiempo de adquisición de datos:
────────────────────────────────────────────────────────────────────────
 Feb 2026      Mar 2026      Jun 2026 (25–26)     Jul 2026     Ago 2026
    │              │               │                  │            │
  T01–T04      [Calibraciones]  Brigada SMR        Brigada CST  Brigada CST
  (pruebas)    (Base, pruebas)  (Base + K1)        (K1)         (K1)
  Base kit     Base kit         ~45 archivos        ~6 arch.    ~14 arch.
  SIN_ETIQUETA SIN_ETIQUETA     PATIENT+CONTROL     PATIENT     PATIENT+CTRL
────────────────────────────────────────────────────────────────────────
Brigada SMR = Santa Marta (Región Caribe)
Brigada CST = CST (Cali / LA, Región Andina)
```

| Brigada | Tag | Kit | Archivos | Pacientes | Controles |
|:---|:---:|:---:|:---:|:---:|:---:|
| Santa Marta | `Santa Marta` | Base + K1 | ~45 | ~39 | 2 |
| CST / Cali | `CST` | K1 | ~14 | ~11 | 5 |
| Técnicas internas | `INT`, sin tag | Base | 7 | 0 | 0 |
| Sin tag (pacientes) | — | Base/K1 | ~12 | ~12 | 0 |

---

## 7. Correlación de Observaciones Clínicas

### 7.1 Esquema de Medicación y Tratamiento por Paciente

> [!NOTE] La información clínica proviene del campo `patientObs` (libre) registrado por el evaluador al momento de la prueba. No constituye historia clínica formal; debe cruzarse con fuentes clínicas antes de uso en modelos.

| ID Paciente | Código(s) | Tratamiento(s) Identificados | Estado Motor Registrado |
|:---:|:---:|:---|:---:|
| **P01** | BF, AR | DBS | -- |
| **P04** | AK | Amantadina | -- |
| **P05** | AA | Levodopa + Amantadina | -- |
| **P06** | V | Levodopa | -- |
| **P09** | BK | Levodopa | -- |
| **P11** | BR, AP | DBS | -- |
| **P12** | BH, S | Amantadina | -- |
| **P13** | BN | Levodopa | **OFF** |
| **P14** | G | Levodopa | **ON** |
| **P15** | X | Levodopa | **ON** |
| **P16** | BA | Levodopa | -- |
| **P17** | AC | Amantadina | -- |
| **P18** | AV | Levodopa | -- |
| **P19** | AO | Levodopa | -- |
| **P20** | M | Levodopa | -- |
| **P21** | BQ | Levodopa | -- |
| **P23** | AJ | Levodopa | -- |
| **P24** | O | Levodopa | -- |
| **P25** | BU, K | DBS + Levodopa | -- |
| **P26** | BT | Sin medicación (día evaluación) | -- |
| **P27** | BM | Sin levodopa (registro) | -- |
| **P28** | BS | Levodopa + Amantadina | -- |
| **P29** | AW | Levodopa | -- |
| **P30** | AH | Amantadina + Biperiden/Vipirideno | -- |
| **P31** | AT | Levodopa | -- |
| **P32** | AE | Amantadina (sin levodopa activa) | -- |
| **P33** | BL | Levodopa + Amantadina + Mirapex | -- |
| **P34** | AS | Levodopa | -- |
| **P35** | BP | Levodopa + Amantadina | -- |
| **P36** | AD | Levodopa | -- |
| **P37** | BB | Sin medicación (día evaluación) | -- |
| **P38** | R | Levodopa | -- |
| **P39** | W | Amantadina + Biperiden/Vipirideno | -- |
| **P40** | I | Levodopa | -- |
| **P41** | Q | Levodopa | -- |
| **P42** | AU | DBS + Levodopa (DBS activo) | -- |
| **P43** | L | DBS (sin levodopa activa) | -- |
| **P44** | H | Levodopa | -- |
| **P45** | AI | Levodopa | -- |
| **P47** | AF | Levodopa | -- |
| **P49** | BE | Levodopa | -- |
| **P53** | Z | Levodopa (día anterior) | -- |
| **P54** | BG | Levodopa | -- |
| P02, P03, P07, P08, P10, P22, P46, P48, P50, P51, P52 | varios | Sin datos de medicación registrados | -- |

### 7.2 Resumen de Tratamientos (Frecuencias)

| Tratamiento | n pacientes | % del total (54) |
|:---|:---:|:---:|
| Solo Levodopa | ~24 | ~44% |
| Levodopa + Amantadina | ~7 | ~13% |
| DBS (con o sin Levodopa) | 5 | ~9% |
| Solo Amantadina | 3 | ~6% |
| Amantadina + Biperiden/Vipirideno | 2 | ~4% |
| Sin medicación en día de evaluación | 3 | ~6% |
| Sin datos registrados | ~10 | ~18% |

> [!IMPORTANT] Solo **P13** (OFF) y **P14/P15** (ON) tienen el estado motor explícito. En los demás, el estado ON/OFF se debe **inferir** de la hora de toma vs. el timestamp de la grabación, tarea que requiere información farmacológica adicional (vida media de cada fármaco).

### 7.3 Implicaciones para el Modelado

1. **Levodopa**: Fármaco más prevalente (~77% de pacientes con datos). La hora de toma registrada permite estimar si el paciente estaba en fase ON u OFF en el momento de la captura. **Acción requerida:** Crear columna `estado_farmacologico_estimado` cruzando `hora_toma` con el timestamp de inicio.

2. **DBS**: Cinco pacientes con estimulación cerebral profunda activa (P01, P11, P25, P42, P43). Las señales TUG de pacientes DBS pueden mostrar cinemáticas atípicas incluso sin levodopa. **Acción requerida:** Crear categoría separada o variable *dummy* `dbs_activo` = 1/0.

3. **Doble Tarea (P26)**: Las grabaciones `AZ`, `J`, `AQ` (Dual Task con aritmética y ciudades) tienen características cinemáticas diferentes al TUG estándar. Ya descartadas del corpus de clasificación principal. Podrían usarse en un análisis comparativo paralelo.

4. **"Por confirmar" (P50/BI, P52/Y, C07/AN)**: Tres registros con diagnóstico pendiente. **No incluir en entrenamiento** hasta confirmación clínica.

---

## 8. Dudas Pendientes y Banderas para Revisión Clínica

### 8.1 Anomalías Potenciales a Verificar

| # | Código(s) | Tipo | Anomalía Detectada | Recomendación |
|:---:|:---:|:---:|:---|:---|
| 1 | AL / BC | CONTROL | Misma fecha de nacimiento y sexo, talla 155 vs 156 cm, kits distintos, fechas separadas 7 días | Confirmar si es la misma persona C01 (error de 1 cm en tallímetro) o dos controles distintos |
| 2 | AF / BE | PATIENT | Nacimiento 28/03/1963 vs 28/05/1963, misma sexo MALE, tallas 173 vs 163 cm | Las tallas difieren 10 cm → probablemente personas distintas (P47 y P49). Revisar fechas de nacimiento en fichas físicas |
| 3 | BW (P08) | PATIENT | Pausa de 55.6 s en una TUG de 60.2 s (pausa ≈ 92% del tiempo total) | ¿Fue una pausa clínica o un error de operador? El paciente P08 tiene `testObs: "paciente en on toma 10am"`. Verificar con el evaluador |
| 4 | AN / C07 | CONTROL | `patientObs: "Por confirmar diagnóstico"` en un archivo etiquetado como CONTROL | No usar en entrenamiento hasta confirmación. Si resulta PATIENT, reclasificar |
| 5 | Y / P52 | PATIENT | `patientObs: "Por confirmar"` | No usar en entrenamiento hasta confirmación |
| 6 | BI / P50 | PATIENT | `patientObs: "Por confirmar"` | No usar en entrenamiento hasta confirmación |
| 7 | BA × 2 (P16) | PATIENT | MD5 idéntico — mismo archivo grabado dos veces con timestamps consecutivos | Mantener únicamente el primero. Verificar si la app genera un bug de doble escritura |
| 8 | Z × 2 (P53) | PATIENT | MD5 idéntico — mismo archivo grabado dos veces con timestamps consecutivos | Mismo patrón que P16. Bug sistemático de la app a investigar |

### 8.2 Pendientes de Adquisición

| Item | Estado | Prioridad |
|:---|:---:|:---:|
| Controles sanos adicionales (meta: 15–20 según anteproyecto) | ⚠️ Solo hay 7 únicos | **Alta** |
| Confirmación diagnóstica de P50, P52, C07 | ⚠️ Pendiente | **Alta** |
| Auditoría de orientación del sensor Z entre Kit Base y K1 | ⚠️ Sin hacer | **Alta** |
| Cálculo del estado ON/OFF estimado a partir de hora de toma | ⚠️ Sin hacer | **Media** |
| Grabaciones adicionales de P11 (AP: 12.2 s — muy corto) | ⚠️ Por evaluar | **Media** |
| Validar si la app genera duplicados MD5 sistemáticamente | ⚠️ Sin investigar | **Baja** |

### 8.3 Checklist de Pasos Pre-Modelado

- [ ] Normalizar `deviceId` con `.replace("K1-", "")` en el cargador
- [ ] Confirmar orientación del eje Z acelerómetro (Kit Base vs K1)
- [ ] Crear columna `person_id` con `GroupKFold` en pipeline de validación cruzada
- [ ] Excluir del corpus: `BA[dup]`, `Z[dup]`, `AZ`, `J`, `AQ`, `SIN_ETIQUETA` (7 archivos)
- [ ] Resolver "Por confirmar": P50, P52, C07 → incluir o excluir
- [ ] Crear variable `dbs_activo` ∈ {0, 1} para pacientes P01, P11, P25, P42, P43
- [ ] Estimar `estado_on_off` basado en hora de toma de medicación
- [ ] Adquirir 8–13 controles sanos adicionales para equilibrar clases
- [ ] Revisar BW (P08): pausa de 92% — ¿válido para TUG estándar?
- [ ] Revisar AP (P11): duración 12.2 s — ¿TUG completo o incompleto?

---
*Documento consolidado automáticamente a partir del escaneo determinístico de los 78 archivos de `/Datos IMUs/`.*
*Generado: 2026-10-26 | Versión 2.0 | Secciones 1–8 completas*
