# Resumen de Datos, Preprocesamiento y Algoritmo de Segmentación TUG

Este documento reúne el análisis exploratorio de las grabaciones recolectadas en las brigadas, los resultados obtenidos tras ejecutar el script de identificación y filtrado de participantes (`identificar_personas.py` -> `personas.csv`), y la explicación detallada de cómo funciona el algoritmo de segmentación heredado del PDG anterior (`PDGI_Clasificación.ipynb` y `segmentar_tug.py`) al probarlo con nuestras muestras actuales.

---

## 1. Estructura de los datos crudos (`Datos Crudos/`)

Contamos con **78 archivos JSON** dentro de la carpeta `Datos Crudos/`. Cada archivo corresponde a una sesión de grabación de la prueba *Timed Up and Go* (`testType = "TIMED_UP_AND_GO"`), donde las lecturas de todos los sensores inerciales vienen intercaladas en una única lista llamada `imuData`.

### Sensores IMU y canales disponibles

En cada grabación participan hasta **5 sensores IMU** trabajando a una frecuencia nominal de **50 Hz** (~49.4 Hz efectivos en las brigadas, es decir, una muestra cada ~20 ms). Durante las jornadas de captura se usaron dos kits distintos (uno sin prefijo y otro identificado con el prefijo `K1-`):

| `deviceId` (kit `base`) | `deviceId` (kit `K1`) | Ubicación anatómica | Nombre asignado en código |
|---|---|---|---|
| `BASE-SPINE` | `K1-BASE-SPINE` | Espalda baja (vértebra L5) | `espina_base` |
| `LEFT-ANKLE` | `K1-LEFT-ANKLE` | Tobillo izquierdo | `izquierda` |
| `RIGHT-ANKLE` | `K1-RIGHT-ANKLE` | Tobillo derecho | `derecha` |
| `LEFT-HAND` | `K1-LEFT-HAND` | Mano / muñeca izquierda | `mano_izquierda` |
| `RIGHT-HAND` | `K1-RIGHT-HAND` | Mano / muñeca derecha | `mano_derecha` |

Cada registro dentro de `imuData` contiene:
- `accelerometer` (`x`, `y`, `z`): aceleración lineal medida en unidades de gravedad (**g**, donde $1\text{ g} \approx 9.81\text{ m/s}^2$). En el código adaptado al formato del PDG anterior estos ejes se guardan como `x`, `y`, `z`.
- `gyroscope` (`x`, `y`, `z`): velocidad angular medida en grados por segundo (**°/s**). En el código adaptado se mapean como `a` (`gyroscope.x`), `b` (`gyroscope.y`) y `g` (`gyroscope.z`).
- `timestamp`: tiempo relativo en milisegundos desde el inicio de la prueba.

### Particularidades encontradas en los archivos JSON

1. **Formato envuelto de la plataforma web (`data`)**: Algunos JSON descargados directamente desde el endpoint de la plataforma vienen envueltos dentro de una llave raíz `{"data": { ... }}`, mientras que los demás tienen los campos directamente en la raíz.
2. **Anonimización sin ID único**: Los campos `id`, `name`, `lastName` y `patient.id` vienen vacíos por privacidad. Además, el código al final del nombre del archivo (`_A`, `_AR`, `_R`, etc.) identifica la grabación y no al paciente, por lo que una misma persona que repitió la prueba aparece en varios archivos con letras distintas.
3. **Orientación del sensor de la espalda (`BASE-SPINE`)**: En todas las grabaciones de brigada (desde el 25 de junio de 2026) el sensor lumbar se colocó de forma que la gravedad cae sobre el eje `x` ($\approx 1\text{ g}$). Por eso, la rotación horizontal del tronco al girar (*yaw*) se registra en el canal `a` (`gyroscope.x`), mientras que la inclinación hacia adelante al levantarse o sentarse (*pitch*) se registra en el canal `b` (`gyroscope.y`).

---

## 2. Resultados del preprocesamiento (`identificar_personas.py` y `personas.csv`)

Para organizar el dataset antes de pasar a la segmentación, el script `identificar_personas.py` procesa los 78 archivos JSON, reconstruye la identidad de cada participante cruzando sus datos demográficos (`birthDate`, `sex`, `patientType`) y aplica los criterios metodológicos de exclusión definidos con el tutor en la Reunión #6.

### Resumen general de la base de datos

| Métrica | Cantidad | Detalle |
|---|---|---|
| **Total de archivos JSON analizados** | **78** | 63 `PATIENT`, 8 `CONTROL`, 7 `SIN_ETIQUETA` |
| **Participantes únicos identificados** | **61** | Numerados de `P01` a `P61` (54 pacientes y 7 controles) |
| **Grabaciones ACEPTADAS** | **66** | **58 `PATIENT` y 8 `CONTROL`** (`estado_metodologico = ACEPTADO`) |
| **Grabaciones DESCARTADAS** | **12** | Excluidas automáticamente (`estado_metodologico = DESCARTADO`) |

### Desglose de las 12 grabaciones descartadas

El script marca como `DESCARTADO` únicamente los archivos que incumplen los criterios de validez técnica o experimental:

1. **Pruebas técnicas sin etiqueta clínica (7 archivos)**:
   - `20260208022404_temp_BV.json` (`BV`): sin etiqueta, solo tiene 1 sensor (`RIGHT-HAND`).
   - `20260303043120_temp_N.json` (`N`): prueba técnica interna (5.01 s).
   - `20260303043532_temp_BO.json` (`BO`): prueba técnica (3.73 s) y con advertencia de dispositivo desconectado.
   - `20260303044505_temp_BX.json` (`BX`): prueba técnica (2.51 s), faltan sensores y reporta desconexión.
   - `20260303134630_temp_BJ.json` (`BJ`): prueba técnica (6.69 s), solo tiene 3 sensores (falta tobillo derecho).
   - `20260307234249_temp_F.json` (`F`): prueba técnica etiquetada como `"Test"`.
   - `20260308232420_temp_AX.json` (`AX`): prueba sin etiqueta clínica y sin sensor en el tobillo izquierdo.
2. **Duplicados exactos por reintento de guardado en red (2 archivos)**:
   - `20260626133916_temp_BA.json` (`BA`): hash MD5 idéntico a `20260626133915_temp_BA.json` (`P22`).
   - `20260820142006_temp_Z.json` (`Z`): hash MD5 idéntico a `20260820142005_temp_Z.json` (`P60`).
3. **Condición experimental de Doble Tarea / Dual Task (3 archivos)**:
   - `20260626170733_temp_AZ.json` (`AZ`): paciente `P31` haciendo restas sucesivas desde 30.
   - `20260626170919_temp_J.json` (`J`): paciente `P31` en prueba cognitiva secundaria (30 menos 3).
   - `20260626170956_temp_AQ.json` (`AQ`): paciente `P31` nombrando ciudades mientras camina. *(Se conserva su prueba TUG normal `BT`)*.

### Participantes con varias grabaciones válidas en `personas.csv`

Como una misma persona pudo realizar más de una grabación, el archivo `personas.csv` agrupa bajo el mismo `persona_id` los siguientes casos aceptados:
- **`P01` (CONTROL, F, nac. 10/02/2003)**: archivos `AL` y `BC`.
- **`P02` (PATIENT, M, nac. 12/09/1955, con DBS)**: archivos `BF` y `AR`.
- **`P13` (PATIENT, M, nac. 29/03/1958, con DBS)**: archivos `BR` y `AP`.
- **`P17` (PATIENT, M, nac. 30/11/1969)**: archivos `BH` y `S`.
- **`P30` (PATIENT, F, nac. 23/05/1959, con DBS)**: archivos `BU` y `K`.

*(Nota: al entrenar modelos de clasificación más adelante, la partición de entrenamiento y prueba debe hacerse por `persona_id` usando `GroupKFold` para no filtrar muestras del mismo paciente en ambos conjuntos).*

---

## 3. Explicación del Notebook y del Algoritmo de Segmentación (`PDGI_Clasificación.ipynb` y `segmentar_tug.py`)

El objetivo en esta etapa es probar el algoritmo de segmentación que desarrolló el grupo del PDG anterior aplicándolo sobre las grabaciones actuales. Para ello, conservamos intacta su lógica matemática y sus parámetros originales, adaptando únicamente la lectura de datos para que funcione con el formato JSON nuevo sin errores de ejecución.

### 3.1. Adaptación de los datos crudos (`adaptar_esquema_json`)

El código del semestre pasado fue escrito esperando un diccionario con la estructura `{"pruebas": {"<timestamp>": {"espina_base": [...], "izquierda": [...], "derecha": [...]}}}`. La función `adaptar_esquema_json` toma cada JSON actual de `Datos Crudos/` y realiza tres pasos:
1. **Agrupación por sensor (`_clave_sensor`)**: separa la lista `imuData` según el `deviceId` en `espina_base`, `izquierda`, `derecha`, `mano_izquierda` y `mano_derecha` (tanto para el kit `base` como para el `K1-`).
2. **Remuestreo a 50 Hz por interpolación lineal (`np.interp`)**: como los sensores tienen pequeñas variaciones en su reloj (~19 a 20 ms entre muestras), crea un vector de tiempo uniforme a $50\text{ Hz}$ (pasos exactos de $0.02\text{ s}$) e interpola los 6 canales de cada sensor.
3. **Mapeo de canales**: guarda las lecturas con las llaves que usa el código predecesor (`t` en milisegundos, `x, y, z` para acelerómetro y `a, b, g` para giroscopio). Además, como cada archivo nuevo contiene una sola sesión de captura en el diccionario `pruebas`, se accede siempre con `indice_muestra = 0`.

---

### 3.2. Cadena de procesamiento de señal (sección `Domiciano`)

Tanto para detectar cuándo la persona se levanta/sienta como para detectar los giros, el algoritmo predecesor pasa la señal cruda por una cadena de 5 etapas:

```
Señal cruda del sensor -> Normalización [-1, 1] -> Filtro Butterworth pasa-bajos (3 Hz)
  -> Energía en ventana deslizante (1 s) -> Promedio móvil (1 s) -> Umbral binario (>= 0.2)
```

1. **Normalización en amplitud (`asignal / max(abs(asignal))`)**:
   Divide toda la señal por su valor absoluto máximo para acotarla en el rango $[-1, 1]$. Así se puede usar un mismo umbral porcentual (`0.2`) sin importar la escala numérica original.
2. **Filtro pasa-bajos Butterworth (`filter_signal`)**:
   ```python
   def filter_signal(signal, cutoff_hz=3, fs=50.0, order=20):
       nyquist = 0.5 * fs
       normal_cutoff = cutoff_hz / nyquist
       b, a = butter(order, normal_cutoff, btype='low', analog=False)
       return filtfilt(b, a, signal)
   ```
   Los movimientos gruesos del cuerpo humano durante el TUG (inclinar el tronco, girar o dar pasos) ocurren a frecuencias bajas, entre $0.5\text{ Hz}$ y $2.5\text{ Hz}$. Todo lo que esté por encima de $3\text{ Hz}$ corresponde a vibraciones de la ropa, temblor o ruido electrónico del IMU. Se usa `filtfilt` (filtrado hacia adelante y hacia atrás) porque tiene **fase cero**, es decir, limpia la señal sin desplazar en el tiempo el instante en que ocurren los picos.
3. **Cálculo de energía en el dominio del tiempo (`energy_spectrum`)**:
   ```python
   def energy_spectrum(signal, fs, window_size_samples, step_size_samples, apply_window=True):
       ...
       if apply_window:
           window = window * np.hanning(window_size_samples)
       energy = np.sum(window ** 2)
   ```
   Aunque la función se llamó `energy_spectrum`, **no aplica Transformada de Fourier (FFT)**. Lo que calcula es la **energía de corto tiempo en el dominio temporal**:
   - Toma una ventana deslizante de `50 muestras` ($1.0\text{ s}$ a $50\text{ Hz}$) que avanza de 1 en 1 muestra (`step_size_samples = 1`).
   - Multiplica el fragmento por una campana de Hanning (`np.hanning(50)`) para suavizar los bordes de la ventana.
   - Eleva cada muestra al cuadrado y las suma:
     $$E[k] = \sum_{n=0}^{N-1} \left(x[n] \cdot w[n]\right)^2$$
   - Al elevar al cuadrado, cualquier movimiento fuerte del sensor (sea en sentido positivo o negativo) se vuelve una curva positiva alta, mientras que los tramos de quietud quedan pegados a $0$. Finalmente se normaliza dividiendo por la energía máxima.
4. **Suavizado por promedio móvil (`promediomovil`)**:
   ```python
   def promediomovil(senal, ventana=50, fs=50):
       kernel = np.ones(ventana) / ventana
       prom = np.convolve(senal, kernel, mode='valid')
       ...
   ```
   Aplica una media móvil de `50 muestras` ($1.0\text{ s}$) mediante convolución (`np.convolve`) sobre la curva de energía. Esto sirve para unir oscilaciones cercanas dentro de un mismo gesto biomecánico (por ejemplo, cuando el paciente inclina el tronco hacia adelante y luego lo endereza al terminar de pararse) en una sola campana suave, evitando que un mismo movimiento se parta en dos.
5. **Binarización por umbral fijo (`binary_threshold`)**:
   Convierte el promedio móvil en una señal cuadrada de `0` y `1` usando un umbral de `0.2` (el 20 % del pico máximo de energía suavizada). Cuando vale `1` el algoritmo interpreta que hay una transición activa; cuando vale `0`, reposo o caminata recta.

---

### 3.3. Detección de las 5 fases del TUG y conteo de pasos (`STANCE` / `SWING`)

El algoritmo divide la prueba TUG combinando las señales de la espalda (`espina_base`) y de los tobillos (`izquierda` y `derecha`):

#### A. Levantamiento y Sentado (`detectar_fases_tug` — `espina_base`, canal `b`)
- **Señal utilizada**: canal `b` (`gyroscope.y`), que mide la velocidad angular de flexión/extensión anteroposterior (*pitch*) del tronco al despegarse de la silla y al volver a apoyarse.
- **Lógica**: busca los cambios de `0 -> 1` (subidas) y de `1 -> 0` (bajadas) con `np.diff(senal_binaria)`. Filtra los pulsos que duren al menos `0.5 s` (`duracion_minima = 0.5`) y asigna:
  - **Levantamiento**: el primer pulso detectado (`fases_movimiento[0]`).
  - **Sentado**: el último pulso detectado (`fases_movimiento[-1]`).

#### B. Cortes de Giro (`espina_base`, canal `a`)
- **Señal utilizada**: canal `a` (`gyroscope.x`), que en el montaje de brigada coincide con el eje vertical del tronco y registra la rotación en el plano horizontal (*yaw*).
- **Lógica**: aplica el mismo pipeline de energía y promedio móvil sobre el canal `a`, binariza con `threshold = 0.2` y extrae cada par `(inicio, fin)` donde la señal binaria sube a `1` y vuelve a `0`, guardándolos en la lista `intervalos_giro`.

#### C. Caminata de Ida, Caminata de Vuelta y subfases `STANCE` / `SWING` (sección `JOANDGOAG`)
Una vez obtenidos `fases_detectadas` y `intervalos_giro`, el bloque de integración arma la línea de tiempo completa del TUG:
- **Caminata de ida**: desde que termina el levantamiento (`fases["levantamiento"]["fin_tiempo"]`) hasta que empieza el primer giro en el cono (`giros[0]["inicio"]`).
- **Giro 1 (180° en el cono)**: de `giros[0]["inicio"]` a `giros[0]["fin"]`.
- **Caminata de vuelta**: desde que termina el primer giro (`giros[0]["fin"]`) hasta que empieza el segundo giro antes de la silla (`giros[1]["inicio"]`).
- **Giro 2 (giro previo a sentarse)**: de `giros[1]["inicio"]` a `giros[1]["fin"]`.

Dentro de los intervalos exclusivos de **caminata de ida** y **caminata de vuelta**, la función `detectar_pasos_intervalo` analiza el canal `x` del acelerómetro de cada tobillo (`izquierda` y `derecha`):
- Recorta la señal filtrada del tobillo únicamente al tramo `[t_inicio, t_fin]` de la caminata.
- Usa `scipy.signal.find_peaks` con una separación mínima entre pasos de `0.4 s` (`distance = int(0.4 * 50) = 20 muestras`) y una prominencia relativa del 25 % de la amplitud máxima del segmento (`prominence = 0.25 * max(|sig_seg|)`).
- Identifica los **picos positivos** como inicio de la fase de apoyo (**`STANCE`**, contacto del talón con el suelo) y los **valles negativos** (`find_peaks(-sig_seg)`) como inicio de la fase de balanceo (**`SWING`**, despegue del pie en el aire).
- Ordena cronológicamente todos los eventos `STANCE_START` y `SWING_START` y calcula la duración individual y promedio de apoyo y balanceo para cada pierna.

---

## 4. Resultados de probar el algoritmo en nuestras muestras (`segmentar_tug.py`)

El script `segmentar_tug.py` ejecuta exactamente este algoritmo tanto en muestras individuales como en lote sobre las **66 grabaciones aceptadas**, exportando la tabla `segmentacion_fases_tug.csv`.

### Prueba 1: Grabación con una sola repetición TUG (`20260625140851_temp_AR.json`)
En el archivo `AR` (`P02`, paciente con DBS, 41.10 s en el sensor de espalda), el paciente realiza un único ensayo TUG y el algoritmo predecesor identifica limpiamente las 5 fases y los pasos de ambos tobillos:

- **Fases de tronco (`canal b`)**:
  - **Levantamiento**: `21.72 s -> 23.92 s` (duración: `2.20 s`)
  - **Sentado**: `37.72 s -> 40.12 s` (duración: `2.40 s`)
- **Intervalos de giro (`canal a`)**:
  - **Giro 1 (cono)**: `28.84 s -> 31.06 s` (duración: `2.22 s`)
  - **Giro 2 (silla)**: `36.44 s -> 38.20 s` (duración: `1.76 s`)
- **Caminatas y pasos (`bloque JOANDGOAG`)**:
  - **Caminata de ida**: `23.92 s -> 28.84 s` (duración: `4.92 s`)
    - Tobillo izquierdo (11 subfases): promedio `STANCE = 0.24 s`, `SWING = 0.50 s`
    - Tobillo derecho (10 subfases): promedio `STANCE = 0.35 s`, `SWING = 0.41 s`
  - **Caminata de vuelta**: `31.06 s -> 36.44 s` (duración: `5.38 s`)
    - Tobillo izquierdo (11 subfases): promedio `STANCE = 0.43 s`, `SWING = 0.34 s`
    - Tobillo derecho (11 subfases): promedio `STANCE = 0.34 s`, `SWING = 0.38 s`

### Prueba 2: Grabación con dos repeticiones seguidas (`20260627150939_temp_R.json`)
En el archivo `R` (`P42`, paciente, 43.66 s en el sensor de espalda), la persona realizó **dos pruebas TUG consecutivas** dentro de la misma grabación. Al correr el algoritmo original se observa claramente cómo responde cada bloque:

- **Fases de tronco (`canal b`)**: detecta **4 pulsos** de movimiento del tronco (2 del primer intento y 2 del segundo). Como la regla original toma el primero (`fases_movimiento[0]`) como levantamiento y el último (`fases_movimiento[-1]`) como sentado, reporta:
  - **Levantamiento**: `3.18 s -> 5.12 s` (del primer TUG, duración: `1.94 s`)
  - **Sentado**: `41.38 s -> 42.62 s` (del segundo TUG, duración: `1.24 s`)
- **Intervalos de giro (`canal a`)**: detecta los **4 giros** reales de la grabación:
  - **Giro 1**: `8.40 s -> 9.80 s` (`1.40 s`, giro en el cono del 1.° TUG)
  - **Giro 2**: `12.84 s -> 14.44 s` (`1.60 s`, giro para sentarse del 1.° TUG)
  - **Giro 3**: `35.20 s -> 36.68 s` (`1.48 s`, giro en el cono del 2.° TUG)
  - **Giro 4**: `39.58 s -> 41.20 s` (`1.62 s`, giro para sentarse del 2.° TUG)
- **Caminatas y pasos (`bloque JOANDGOAG`)**: como toma `levantamiento`, `giros[0]` y `giros[1]`, recorta correctamente las caminatas de ida y vuelta del **primer ensayo TUG**:
  - **Caminata de ida**: `5.12 s -> 8.40 s` (`3.28 s`) -> Izquierda: `STANCE = 0.31 s`, `SWING = 0.23 s` | Derecha: `STANCE = 0.31 s`, `SWING = 0.23 s`.
  - **Caminata de vuelta**: `9.80 s -> 12.84 s` (`3.04 s`) -> Izquierda: `STANCE = 0.37 s`, `SWING = 0.24 s` | Derecha: `STANCE = 0.33 s`, `SWING = 0.23 s`.

### Resumen del lote completo (`segmentacion_fases_tug.csv`)
Al ejecutar `python3 "Analisis de Datos/segmentar_tug.py" --lote` sobre las **66 grabaciones aceptadas**:
- El algoritmo corre de principio a fin sin errores en las **66 muestras**.
- En **63 de las 66 muestras** logra extraer la estructura completa de las 5 fases (levantamiento, caminata de ida, giro 1, caminata de vuelta, giro 2 y sentado).
- En las **3 muestras restantes**, el umbral fijo de `0.2` detecta solo 1 pulso de tronco (cuando el paciente se sienta muy despacio en comparación con el impulso al levantarse) o solo 1 giro (en las pruebas donde el sensor lumbar tenía otra orientación o un segundo giro más lento). Este resultado refleja fielmente el desempeño base del algoritmo heredado sobre los datos reales de las brigadas.
