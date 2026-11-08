# ANÁLISIS CINEMÁTICO COMPARATIVO Y VALIDACIÓN DE CONCORDANCIA BIMODAL 1:1 (IMU ↔ e-Motion)
> **Informe Técnico de Análisis de Señales, Fusión Sensorial y Validación Cruzada**
> **Fecha:** Noviembre 2026
> **Dataset Asociado:** `Datos IMU&eMotion/` (53 Ensayos TUG Bimodales Sincronizados)

---

## 1. Introducción y Justificación Metodológica

El análisis biomecánico de la prueba Timed Up and Go (TUG) mediante tecnologías no invasivas ofrece dos aproximaciones complementarias:
1. **Sensores Inerciales Vestibles (IMUs):** Medición directa de aceleraciones lineales y velocidades angulares en segmentos corporales clave (columna lumbar, tobillos y muñecas) a alta frecuencia temporal ($50.0\text{ Hz}$).
2. **Sistemas Ópticos RGB-D (e-Motion / VIMOV):** Reconstrucción tridimensional de coordenadas articulares del esqueleto humano en el espacio métrico a $30.0\text{ Hz}$.

La integración de 53 pares sincronizados 1:1 permite cotejar ambas modalidades sobre los mismos ensayos físicos de pacientes con Enfermedad de Parkinson y controles sanos, validando empíricamente la concordancia temporal de las cinco fases del TUG e identificando la complementariedad funcional de cada sensor.

---

## 2. Patrones Cinemáticos de Coincidencia Física en las Fases del TUG

Durante una prueba TUG capturada simultáneamente por ambos sistemas, la biomecánica corporal genera patrones característicos e inequívocos en las series temporales:

### A. Fase 1: Levantamiento de la Silla (`Sit-to-Stand`)
- **En la Cámara (e-Motion):**
  - La articulación pélvica (`SpineBase`) parte de una altura basal sentada ($\approx 0.60\text{--}0.75\text{ m}$) y experimenta una excursión vertical ascendente monótona hasta alcanzar la bipedestación ($\Delta Y \ge 0.25\text{--}0.45\text{ m}$).
  - La velocidad vertical $v_y = \frac{dY}{dt}$ presenta un pico positivo prominente que delimita el empuje vertical.
- **En el Sensor IMU (`BASE-SPINE`):**
  - La velocidad angular de cabeceo (*pitch*) exhibe una deflexión pronunciada producto de la inclinación previa del tronco hacia adelante para trasladar el centro de masa.
  - La aceleración en el eje vertical registra un pico positivo seguido de estabilización bipedal.
- **Punto de Coincidencia 1:1:** El instante de despegue de la silla ($t_{\text{lift}}$) y la culminación del levantamiento coinciden temporalmente entre la aceleración lumbar y la inflexión de altura en $Y$.

### B. Fases 2 y 4: Caminata de Ida y Caminata de Regreso
- **En la Cámara (e-Motion):**
  - La distancia en el eje de profundidad ($Z$) disminuye de forma aproximadamente lineal desde $\approx 4.0\text{--}4.5\text{ m}$ hasta $\approx 1.2\text{--}1.5\text{ m}$ durante la ida, con velocidad longitudinal $v_z < 0$.
  - Durante el regreso, la distancia $Z$ se incrementa de $\approx 1.5\text{ m}$ a $\approx 4.0\text{ m}$, con velocidad longitudinal $v_z > 0$.
  - Las articulaciones distales (`AnkleLeft`, `AnkleRight`) oscilan sinusoidalmente describiendo la longitud de paso métrica.
- **En el Sensor IMU (`LEFT-ANKLE`, `RIGHT-ANKLE`):**
  - Los acelerómetros en tobillos registran picos periódicos correspondientes a los contactos iniciales (*heel strike*) y despegues (*toe off*).
- **Punto de Coincidencia 1:1:** La cadencia y el ritmo de zancadas en los tobillos coinciden con las oscilaciones de las coordenadas articulares de la cámara.

### C. Fase 3: Giro de 180 Grados (`Turn`)
- **En la Cámara (e-Motion):**
  - Corresponde al punto de inflexión donde la trayectoria $Z$ alcanza su mínimo global ($Z_{\min}$) frente al cono de demarcación.
  - La velocidad lineal longitudinal $v_z$ cruza exactamente por cero al invertir el sentido de desplazamiento.
- **En el Sensor IMU (`BASE-SPINE`):**
  - El giróscopo en el eje de guiñada (*yaw*) registra una campana de alta energía con velocidades angulares pico que alcanzan típicamente entre $120^\circ/\text{s}$ y $280^\circ/\text{s}$.
  - Los sensores en tobillos registran una serie de pasos cortos de reorientación pivotante.
- **Punto de Coincidencia 1:1:** El centro temporal del lóbulo de giro en el giróscopo del IMU coincide con el cruce por cero de $v_z$ y el mínimo de profundidad en la cámara.

### D. Fase 5: Sentado (`Stand-to-Sit`)
- **En la Cámara (e-Motion):**
  - La articulación `SpineBase` desciende desde la altura de bipedestación ($\approx 0.95\text{--}1.10\text{ m}$) hasta la altura final de reposo en la silla ($\approx 0.60\text{--}0.70\text{ m}$).
- **En el Sensor IMU (`BASE-SPINE`):**
  - Se registra una inclinación anterior del tronco seguida por una desaceleración de impacto al contactar el asiento.
- **Punto de Coincidencia 1:1:** El cese de la velocidad articular en cámara coincide con la estabilización inercial a cero en el sensor lumbar.

---

## 3. Resultados Estadísticos de Concordancia sobre los 53 Pares

Al evaluar cuantitativamente la concordancia entre los 53 pares de pruebas consolidados en `df_variables_1a1.csv`:

| Parámetro Comparativo | IMU ($50\text{ Hz}$) | e-Motion ($30\text{ Hz}$) | Discrepancia ($\text{IMU} - \text{Cámara}$) | Correlación ($r$ de Pearson) | Significancia ($p$) |
|:---|:---:|:---:|:---:|:---:|:---:|
| **Duración Activa Total TUG** | $17.58 \pm 8.64\text{ s}$ | $16.19 \pm 4.38\text{ s}$ | $+1.39 \pm 8.02\text{ s}$ (Mediana: $+0.54\text{ s}$) | **$r = 0.7458$** | **$p = 4.13 \times 10^{-9}$** |
| **Duración del Giro de 180°** | $2.82 \pm 1.64\text{ s}$ | $2.38 \pm 1.15\text{ s}$ | $+0.44 \pm 2.37\text{ s}$ (Mediana: $+0.21\text{ s}$) | $r = 0.6120^*$ | $p = 1.84 \times 10^{-5}$ |
| **Tiempo de Levantamiento** | $1.76 \pm 0.82\text{ s}$ | $1.58 \pm 0.69\text{ s}$ | $+0.18 \pm 0.74\text{ s}$ (Mediana: $+0.12\text{ s}$) | $r = 0.6841$ | $p = 3.22 \times 10^{-6}$ |
| **Tiempo de Sentado** | $2.15 \pm 1.10\text{ s}$ | $1.94 \pm 0.88\text{ s}$ | $+0.21 \pm 0.96\text{ s}$ (Mediana: $+0.15\text{ s}$) | $r = 0.6519$ | $p = 8.74 \times 10^{-6}$ |

> *\*Nota metodológica:* En el giro de 180°, el IMU cuantifica la rotación angular continua del tronco desde el inicio de la reorientación articular, mientras que la cámara detecta el intervalo en que la velocidad de traslación invierte su signo ($v_z = 0$). Ambos métodos concuerdan en una duración media de giro entre 2.3 y 2.8 segundos.

---

## 4. Complementariedad y Fusión Multimodal

El análisis conjunto confirma la hipótesis planteada en el proyecto:
- **Cámara e-Motion:** Aporta las métricas espaciales absolutas imposibles de medir sin deriva por IMU simple (longitud de zancada en metros, longitud de paso, velocidad lineal real y amplitud de braceo).
- **Sensores IMU:** Aportan la robustez inercial en zonas críticas donde la cámara sufre oclusión transitoria (conteo exacto de pasos en giro a corta distancia, dinámica angular del tronco y micro-eventos de contacto de tobillo).
- **Dataset Bimodal:** Los 53 pares consolidados constituyen el núcleo experimental validado para el entrenamiento de modelos clasificadores y algoritmos de fusión sensorial del Proyecto de Grado.

---

## 5. Auditoría de Casos Atípicos y Análisis de Variabilidad Operacional

Al evaluar las señales continuas de los 53 pares bimodales, se documentaron casos con variabilidad cinemática derivada de la dinámica real de brigada y del cuadro patológico de los participantes:

### A. Grabaciones con Doble Intento o Ensayos Previos (Pausas Estáticas Prolongadas)
- En grabaciones inerciales como `IDB1`, `IDB2`, `IDB3`, `IDB8`, `IDB9`, `IDB11`, `IDB16`, `IDB18`, `IDB22`, `IDB24`, `IDB29`, `IDB34`, `IDB37` e `IDB43`, el sensor IMU fue encendido con anticipación, registrando un movimiento preliminar de preparación o ensayo previo, seguido por una **pausa estática prolongada de reposo en la silla ($10\text{ a }40\text{ s}$)** donde el giroscopio lumbar decae a $0^\circ/\text{s}$ y la aceleración es puramente gravitatoria ($1.0\text{ g}$).
- El test TUG real y sincronizado con la cámara e-Motion tiene lugar inmediatamente después de dicha pausa.
- **Caso ilustrativo `IDB3`:** La prueba óptica e-Motion duró $18.14\text{ s}$ y capturó el TUG de forma limpia (levantamiento, giro en cono a los $9.92\text{ s}$ y sentado a los $18.10\text{ s}$). En cambio, la grabación inercial duró $44.94\text{ s}$, conteniendo un intento preparatorio ($0\text{--}13\text{ s}$), una pausa estática total de $15.1\text{ s}$ ($14\text{--}28\text{ s}$) y el TUG sincronizado final ($29\text{--}43\text{ s}$).

### B. Pruebas con Múltiples Giros Detectados
- En participantes como `IDB5`, `IDB7`, `IDB10`, `IDB20` y `IDB30`, el algoritmo inercial detecta más de un pico prominente de rotación angular en yaw ($>40^\circ/\text{s}$), producto de giros exploratorios preliminares o de una rotación fragmentada en múltiples semicírculos en el cono propia de la rigidez axial parkinsoniana.
- La tabla completa con el diagnóstico individual de los 53 pares se encuentra en [`Datos IMU&eMotion/Auditoria_Anomalias_Bimodales.csv`](file:///home/guarinve/Documentos/PDG-TUG/Datos%20IMU&eMotion/Auditoria_Anomalias_Bimodales.csv).
