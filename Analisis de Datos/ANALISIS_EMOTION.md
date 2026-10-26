# Inventario y revisión de datos e-Motion

## 1. Resumen actual

La carpeta `Datos e-Motion/` contiene **30 archivos `*_raw.json`**, correspondientes a 30 capturas. No se encontraron duplicados exactos por SHA-256. **29** registros declaran una prueba TUG en `TypeTest` (28 usan `TIMED_UP_AND_GO` y uno `Timed up and Go`); el registro restante declara `Gait Analysis`, por lo que no debe tratarse como TUG.

Hay **25 registros Intel RealSense** (4 D455 y 21 D455F) y **5 Orbbec Astra 2**. La duración declarada va de 6 a 25 segundos. Los 23 registros Intel que ya estaban inventariados en la tabla siguiente contienen entre 281 y 689 fotogramas; los siete archivos añadidos al inventario contienen entre 195 y 796 registros `SkeletonLocation`. Estas cantidades provienen de estructuras distintas y no son directamente comparables.

El inventario corresponde a los archivos presentes actualmente en `Datos e-Motion/`; no incluye los dos JSON de esa carpeta que no tienen sufijo `_raw`.

## 2. Capturas RAW

La cobertura mínima es el menor porcentaje de fotogramas con coordenadas X, Y y Z presentes y no todas en cero entre `Head`, `SpineBase`, `AnkleLeft` y `AnkleRight`. Es un indicador técnico de seguimiento, no un umbral clínico ni una validación de la prueba.

| Archivo | Tipo declarado | Duración | Fotogramas | Cobertura mínima |
|---|---|---:|---:|---:|
| `20241016_intel_b7e13693_raw.json` | Timed up and Go | 20 s | 426 | 89.4% |
| `20261002_intel_09a4dc83_raw.json` | TIMED_UP_AND_GO | 14 s | 427 | 85.0% |
| `20261002_intel_84010489_raw.json` | TIMED_UP_AND_GO | 11 s | 355 | 87.9% |
| `20261002_intel_890b769c_raw.json` | TIMED_UP_AND_GO | 14 s | 427 | 81.5% |
| `20261002_intel_a7da7cf0_raw.json` | TIMED_UP_AND_GO | 16 s | 503 | 86.9% |
| `20261002_intel_c9e9720b_raw.json` | TIMED_UP_AND_GO | 13 s | 400 | 92.0% |
| `20261014_intel_2058a215_raw.json` | TIMED_UP_AND_GO | 15 s | 469 | 84.9% |
| `20261014_intel_4d3da61e_raw.json` | TIMED_UP_AND_GO | 13 s | 406 | 87.7% |
| `20261014_intel_64212756_raw.json` | TIMED_UP_AND_GO | 13 s | 391 | 86.7% |
| `20261014_intel_8a6c58e7_raw.json` | TIMED_UP_AND_GO | 14 s | 433 | 85.0% |
| `20261014_intel_c95b9599_raw.json` | TIMED_UP_AND_GO | 12 s | 384 | 88.5% |
| `20261014_intel_ddf77635_raw.json` | TIMED_UP_AND_GO | 16 s | 502 | 83.3% |
| `20261014_intel_eb4373aa_raw.json` | TIMED_UP_AND_GO | 19 s | 594 | 84.7% |
| `20261015_intel_0d4c2104_raw.json` | TIMED_UP_AND_GO | 12 s | 365 | 77.8% |
| `20261015_intel_282d8a1b_raw.json` | TIMED_UP_AND_GO | 14 s | 445 | 81.6% |
| `20261015_intel_3bb1c3b6_raw.json` | TIMED_UP_AND_GO | 14 s | 419 | 80.9% |
| `20261015_intel_3cbf990b_raw.json` | TIMED_UP_AND_GO | 12 s | 370 | 82.4% |
| `20261015_intel_684a7afe_raw.json` | TIMED_UP_AND_GO | 13 s | 411 | 82.5% |
| `20261015_intel_aba7198f_raw.json` | TIMED_UP_AND_GO | 14 s | 429 | 80.4% |
| `20261015_intel_d0dd12ae_raw.json` | TIMED_UP_AND_GO | 14 s | 426 | 84.5% |
| `20261015_intel_fb517029_raw.json` | TIMED_UP_AND_GO | 9 s | 281 | 90.0% |
| `20261016_intel_8f6b70f7_raw.json` | TIMED_UP_AND_GO | 20 s | 610 | 86.2% |
| `20261016_intel_cfa0d535_raw.json` | TIMED_UP_AND_GO | 23 s | 689 | 79.5% |

Los siete archivos incorporados después de ese inventario previo tienen una estructura distinta o adicional. En ellos, `CaptureTest.KinectMachineStatus[].SkeletonLocation` contiene los registros temporales del esqueleto:

| Archivo | `TypeTest` | Cámara | Captura local | Duración declarada | Registros `SkeletonLocation` |
|---|---|---|---|---:|---:|
| `3166462b-4d99-4f14-b560-5a9c1dc08d31_raw.json` | `TIMED_UP_AND_GO` | Intel RealSense D455F | 2026-06-25 08:24 | 11 s | 358 |
| `6f6fd032-b451-43c6-8554-b0328ee96b58_raw.json` | `Gait Analysis` | Intel RealSense D455 | 2026-07-04 10:13 | 6 s | 195 |
| `93b689a7-dfc2-4069-a935-efdde29de98a_raw.json` | `TIMED_UP_AND_GO` | Orbbec Astra 2 | 2026-07-04 10:50 | 20 s | 644 |
| `4849da67-9862-4f1a-b960-165cfa5306e7_raw.json` | `TIMED_UP_AND_GO` | Orbbec Astra 2 | 2026-07-04 10:58 | 17 s | 557 |
| `b6487716-3d2f-4728-b000-cd71ccc723c2_raw.json` | `TIMED_UP_AND_GO` | Orbbec Astra 2 | 2026-07-04 11:14 | 16 s | 520 |
| `56108fef-0268-4f6f-920e-97787068b311_raw.json` | `TIMED_UP_AND_GO` | Orbbec Astra 2 | 2026-07-04 12:49 | 25 s | 796 |
| `0cce5b72-f8d0-458e-b576-64c138fd2b53_raw.json` | `TIMED_UP_AND_GO` | Orbbec Astra 2 | 2026-07-04 13:50 | 11 s | 395 |

### Observaciones de calidad

- `20261015_intel_0d4c2104_raw.json` presenta la cobertura mínima más baja: **77.8%**. Conviene revisar sus pérdidas de seguimiento antes de usarlo.
- La cobertura mínima promedio de **84.8%** corresponde únicamente a los 23 registros de la primera tabla; no se calculó un porcentaje comparable para los siete archivos nuevos porque su estructura de datos es diferente. Los porcentajes no determinan por sí solos si una captura debe aceptarse o descartarse.
- `TypeTest` indica el tipo declarado por el sistema; no confirma que las cinco fases del TUG estén completas. La continuidad de las articulaciones y la ejecución de cada fase requieren validación adicional.

## 3. Bloque C: correspondencia temporal con IMUs

Se compararon los seis archivos IMU de la lista del bloque C con los `CaptureTest.Date` y los tiempos primero/último de `SkeletonLocation` de los RAW. Los `timestamp` y `endTimestamp` del IMU están en milisegundos Unix; para compararlos se convirtieron de UTC a hora de Colombia (UTC-5). Como los RAW de cámara no declaran zona horaria, se asumió que sus fechas son hora local de Colombia; debe confirmarse que el reloj de cámara estaba configurado así. La tolerancia utilizada para una coincidencia de inicio es ±60 segundos.

| Archivo IMU | Inicio IMU (Colombia) | RAW de cámara más cercano | Inicio de cámara | Diferencia cámara − IMU | Dentro de ±60 s |
|---|---|---|---|---:|---|
| `20260704154505_temp_AF.json` | 10:44:08.939 | `93b689a7-dfc2-4069-a935-efdde29de98a_raw.json` | 10:50:29.714 | +380.775 s | No |
| `20260704155929_temp_BE.json` | 10:58:15.070 | `4849da67-9862-4f1a-b960-165cfa5306e7_raw.json` | 10:58:37.606 | +22.536 s | **Sí** |
| `20260704165749_temp_E.json` | 11:56:59.852 | `b6487716-3d2f-4728-b000-cd71ccc723c2_raw.json` | 11:14:29.562 | −2550.290 s | No |
| `20260704172020_temp_Y.json` | 12:19:11.100 | `56108fef-0268-4f6f-920e-97787068b311_raw.json` | 12:49:13.064 | +1801.964 s | No |
| `20260704194015_temp_AY.json` | 14:00:00.064 | `0cce5b72-f8d0-458e-b576-64c138fd2b53_raw.json` | 13:50:36.417 | −563.647 s | No |
| `20260704194635_temp_BG.json` | 14:44:43.713 | `0cce5b72-f8d0-458e-b576-64c138fd2b53_raw.json` | 13:50:36.417 | −3247.296 s | No |

El par `BE`–`4849...` también presenta solapamiento de las ventanas observadas: la secuencia de cámara va aproximadamente de 10:58:37 a 10:58:56 y el IMU termina aproximadamente a las 10:58:56. Es evidencia de **coincidencia temporal candidata**, no prueba de que sea la misma persona o la misma ejecución: los archivos no incluyen una clave común ni una tabla de correspondencia entre identificadores. Además, los seis IMU seleccionados son del **4 de julio de 2026**, mientras que el backlog describe una brigada del **24–28 de julio**; no hay RAW de cámara fechado entre el 24 y el 28 de julio en la carpeta actual. Los RAW sí sirven para explorar por separado la cinemática de TUG por cámara, pero con estos archivos no se puede atribuir la coincidencia a esa brigada ni justificar todavía una fusión IMU-cámara.

## 4. Índice tabular `emotion_features.csv`

El CSV contiene **30 filas de datos**, una por cada `*_raw.json` actualmente presente en `Datos e-Motion/`, y conserva estas columnas:

1. `archivo`
2. `id_sujeto`
3. `take_id`
4. `clase`
5. `sensor`
6. `fecha_captura`
7. `protocolo`
8. `tipo_marcha`

Los campos se interpretan de forma conservadora:

- `id_sujeto` es un seudónimo creado con los primeros ocho caracteres de `Patient.Id`; no representa una identidad clínica verificada.
- `take_id` figura como `NO INFORMADO` porque no aparece como tal en los JSON.
- `clase` figura como `SIN ETIQUETA`; no se infiere CONTROL o PATIENT.
- `sensor` normaliza el modelo de cámara declarado en `Camera`.
- `fecha_captura` se toma de `CaptureTest.Date` y se presenta con precisión de minuto.
- `protocolo` se conserva solo si es una descripción no clínica; se deja vacío cuando el campo contiene notas clínicas o personales.
- `tipo_marcha` indica que el TUG está declarado en `TypeTest`, no que se hayan validado sus fases.

## 5. Privacidad y límites

En los 30 registros, los campos de nombre, apellido, fecha de nacimiento y número de documento dentro de `Patient` están vacíos. Los identificadores internos, las fechas de captura y algunos comentarios clínicos en `Protocol` siguen presentes en los JSON; por ello los datos deben tratarse como seudonimizados y sensibles, no como anónimos.

Antes de usar las capturas, validar coordenadas ausentes o nulas, continuidad por articulación y presencia de cada fase. El porcentaje de seguimiento de esta revisión no sustituye una inspección biomecánica de la prueba.
