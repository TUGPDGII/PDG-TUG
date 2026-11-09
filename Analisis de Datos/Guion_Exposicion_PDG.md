# Guion de Exposición de Avances, Estado del Arte y Matriz de Riesgos — Proyecto PDG-TUG

Este documento sirve como guía de apoyo para presentar las **16 láminas** de [`Presentacion_Avances_PDG_TUG.html`](file:///home/jjarias/Documents/UNIVERSIDAD/8vo%20semestre/PDG/PDG-TUG/Analisis%20de%20Datos/Presentacion_Avances_PDG_TUG.html). Está redactado en un tono natural para que cualquiera del grupo pueda explicarlo con sus propias palabras durante la sustentación.

* **Controles de teclado en la presentación:**
  * Avanzar / Retroceder: `Flecha Derecha (→)` / `Flecha Izquierda (←)` o `Barra Espaciadora`.
  * Pantalla completa: tecla `F`.
  * Ampliar cualquier gráfica o diagrama en pantalla completa: hacer **clic** sobre la imagen (cerrar con otro clic o `Esc`).

---

## Lámina 01 — Portada Editorial
* **Título:** Análisis Cinemático y Biomecánico Bimodal de la Prueba *Timed Up and Go* en Enfermedad de Parkinson
* **Qué decir:**
  > "Buenos días, profesores. En esta exposición vamos a presentar el consolidado de los avances que ya están unificados en la rama `main`: el ciclo metodológico CRISP-DM y el ajuste de objetivos, nuestra búsqueda en anchura y priorización de variables, el pipeline de preprocesamiento inercial, las modificaciones que hicimos al algoritmo de segmentación frente al proyecto anterior, el pipeline completo para las grabaciones ópticas de cámara e-Motion, el cruce bimodal 1 a 1, los hallazgos estadísticos significativos y la matriz oficial de análisis de riesgos."

---

## Lámina 02 — Objetivos Ajustados y Ciclo Metodológico CRISP-DM
* **Puntos clave en pantalla:**
  * Objetivo General y los 4 Objetivos Específicos (`OE1` a `OE4`, con el ajuste formal de `OE4` sin prometer el 80 % fijo).
  * Diagrama [`OverLeaf/Imagenes/CRISP-DM_Diagram.png`](file:///home/jjarias/Documents/UNIVERSIDAD/8vo%20semestre/PDG/PDG-TUG/OverLeaf/Imagenes/CRISP-DM_Diagram.png).
* **Qué decir:**
  > "En el documento de Overleaf formalizamos el ajuste del cuarto objetivo específico (`OE4`) para evaluar la capacidad de discriminación mediante exactitud y sensibilidad a nivel grupal, sin fijar un umbral arbitrario del 80 %.
  >
  > Además, estructuramos el trabajo bajo el ciclo **CRISP-DM** que se ve a la derecha: partimos de la comprensión clínica del TUG y de por qué se requieren dos sensores complementarios —los **IMUs a 50 Hz** para segmentar las 5 fases y medir el giro sin oclusión, y las **cámaras RGB-D a 30 Hz** para medir longitud de zancada, velocidad lineal, braceo y doble apoyo en los tramos rectos—, pasando luego a la auditoría de los datos de brigadas, el preprocesamiento de señales y la extracción de biomarcadores."

---

## Lámina 03 — Búsqueda en Anchura v2 (Parte I: Evidencia Clínica y Metodológica)
* **Puntos clave en pantalla:**
  * **`R₁` — Molero-Mateo et al. (2026, *Sensors*):** 79 participantes (38 EP temprana `mH&Y 1–1.5` y `2` en estado *OFF* vs. 41 controles, 316 ensayos iTUG).
  * **`R₂` — Vervoort et al. (2016, *PLOS ONE*):** Segmentación con IMU lumbar (*pitch*, *yaw*, aceleración AP + wavelets `db5`) y reducción multivariada PLS (`VIP > 0.8`) + PLS-DA (AUC 94.7 %).
* **Qué decir:**
  > "En nuestra *Búsqueda en anchura v2* analizamos a fondo dos estudios que guían nuestras decisiones técnicas:
  > * Primero, **Molero-Mateo et al. (2026)** en *Sensors*, con 316 ensayos en pacientes con Parkinson temprano (`mH&Y 1 a 2`). Ellos demuestran que el tiempo total del TUG distingue controles de `mH&Y 2`, pero **no logra discriminar estadios tempranos `mH&Y 1–1.5`**. En cambio, al separar el TUG por fases, la **duración del primer giro de 180°** fue la única variable temporal capaz de diferenciar `mH&Y 1–1.5` de los controles. También encuentran mayor **doble apoyo**, menor **longitud de zancada**, menor **velocidad de marcha**, **asimetría del codo** como marcador temprano y el **ROM sagital del tronco** como única variable que separó `mH&Y 1–1.5` frente a `mH&Y 2`.
  > * Segundo, **Vervoort et al. (2016)**, que respalda nuestro procesamiento en IMU lumbar usando velocidad angular *pitch* para levantarse/sentarse, *yaw* para inicio y fin de los giros, y aceleración AP con wavelets para pasos. Además, advierte que el *doble apoyo* no debe inferirse con una sola IMU lumbar sin tener contacto y despegue de ambos pies —razón por la cual nosotros lo medimos directamente con ambos tobillos en la cámara RGB-D y en las IMUs distales— y demuestra que seleccionar variables con PLS (`VIP > 0.8`) antes de clasificar alcanza un AUC del 94.7 %."

---

## Lámina 04 — Búsqueda en Anchura v2 (Parte II: Matriz de Priorización para `TUG 2`)
* **Puntos clave en pantalla:**
  * Jerarquía de variables para `TUG 2` (**Prioridad Alta**, **Prioridad Media** y **Prioridad Baja**).
  * Decisiones adoptadas en nuestro código: desglose en 5 fases + giro final, descarte de coeficientes de variación (*CV*) ruidosos y agrupación por sujeto.
* **Qué decir:**
  > "A partir de esta revisión definimos la tabla de priorización para nuestras matrices de variables:
  > * En **Prioridad Alta** dejamos la duración, número de pasos y pendiente angular de los giros, el porcentaje de doble apoyo, la longitud de zancada, la velocidad de marcha y el rango/pendiente sagital del tronco.
  > * En **Prioridad Media**, la amplitud y asimetría de braceo como marcador temprano.
  > * Y en **Prioridad Baja**, descartamos como marcadores principales el ancho de paso y los coeficientes de variación (*CV*) paso a paso, porque ambos artículos demuestran que en un recorrido corto de 3 metros (~17 pasos) los coeficientes de variación no se estabilizan y solo meten ruido al clasificador."

---

## Lámina 05 — Pipeline de Preprocesamiento Inercial (`Datos IMUs/`, Módulos 1 al 4)
* **Puntos clave en pantalla:**
  * **Control de calidad (Módulo 3):** 78 archivos JSON $\rightarrow$ 12 descartados (7 pruebas técnicas sin etiqueta, 2 duplicados exactos por red verificados con MD5 y 3 pruebas de doble tarea cognitiva) $\rightarrow$ **66 muestras válidas (84.6 %)**.
  * **Identificación de personas (Módulo 2):** **61 participantes únicos** (54 pacientes EP y 7 controles) mediante la tupla $\langle\text{birthDate}, \text{sex}, \text{height}, \text{patientType}\rangle$ y mapeo de 8 grupos con tomas múltiples (DBS, amantadina, pausas en prueba).
  * **Homologación de hardware y frecuencia (Módulo 4):** Normalización de **`Kit Base` (41)** vs. **`Kit K1` (37)** y remuestreo uniforme a **50.0 Hz**.
* **Qué decir:**
  > "Entrando al **Pipeline 1 de sensores IMU (Módulos 1 al 4)**:
  > 1. Aplicamos las reglas determinísticas de descarte sobre los 78 archivos crudos, aislando 7 pruebas internas de calibración sin etiqueta clínica, 2 archivos duplicados byte a byte por reintentos de red en campo (confirmados con hash MD5) y 3 ensayos de doble tarea cognitiva del paciente `P26`, consolidando **66 muestras válidas** (todas con los 5 sensores operativos).
  > 2. Como los datos vienen anonimizados sin nombres ni cédulas, reconstruimos la identidad de los **61 participantes únicos** (54 pacientes y 7 controles) y documentamos los 8 sujetos con repeticiones múltiples, incluyendo pacientes con estimulación cerebral profunda (DBS) y las 11 pruebas donde el médico activó el botón de pausa (`pausedDurationMs` de hasta 55.6 segundos).
  > 3. Además, descubrimos un detalle técnico crítico: el dataset mezcla dos generaciones de hardware, el **`Kit Base`** y el **`Kit K1`** (que le agrega el prefijo `K1-` a cada sensor y rota la carcasa 90°). Si no normalizábamos esos nombres y ejes en el Módulo 4, cualquier script fallaba silenciosamente en el 47 % del dataset. Finalmente, corregimos el desfase inicial entre los relojes locales de los sensores interpolando todo a una rejilla común de **50.0 Hz**."

---

## Lámina 06 — Modificaciones y Mejoras al Algoritmo de Segmentación IMU (Módulos 5 y 7)
* **Puntos clave en pantalla:**
  * Tabla comparativa: **Algoritmo Previo** vs. **Nuestra Modificación (PDG-TUG)**.
  * Logro de **63 de 66 muestras válidas (95.5 %)** segmentadas en las 5 fases.
  * Figuras del Módulo 5 y Módulo 7 (Gráfica compuesta superpuesta de las 5 fases TUG).
* **Qué decir:**
  > "En esta lámina resumimos qué tenía el algoritmo establecido del proyecto anterior y qué modificamos nosotros en los **Módulos 5 y 7**:
  > * Primero, el código anterior asumía el esquema JSON viejo y una tasa de muestreo ideal; nosotros acoplamos el adaptador del nuevo JSON, la normalización del `Kit K1` y la rejilla uniforme a 50 Hz antes del filtro Butterworth a 3 Hz.
  > * Segundo, diagnosticamos por qué fallaban los casos bordes: en dos controles previos a brigada cambia el eje donde cae la gravedad en `BASE-SPINE`, y en varias tomas de brigada el paciente hace un movimiento o giro preparatorio seguido de una pausa sentado antes de empezar formalmente el TUG.
  > * Tercero, pasamos de detectar eventos sueltos a **encadenar de forma contigua las 5 fases del TUG** (*Levantamiento, Marcha de Ida, Giro de 180°, Marcha de Regreso y Sentado*), logrando segmentar **63 de las 66 muestras válidas (95.5 %)**.
  > * Y cuarto, creamos la **gráfica compuesta superpuesta (Figura 2.2)** donde se ven al mismo tiempo la energía de flexo-extensión del tronco y la energía rotacional de guiñada con las franjas de las 5 fases."

---

## Lámina 07 — Detección de Giros y Clasificación de Cada Paso según su Fase TUG (Módulos 6 y 8)
* **Puntos clave en pantalla:**
  * **Módulo 6:** Detección de intervalos de giro (giro de 180° en cono y giro de reorientación frente a la silla) con ventana de energía sobre velocidad angular.
  * **Módulo 8:** Detección de ciclos `SWING` y `STANCE` en ambos tobillos, asignación de la columna `fase_tug` en `SegmentacionFases_IMUs.csv` y conteo de pasos ejecutados dentro del giro.
* **Qué decir:**
  > "Para completar el pipeline inercial, en el **Módulo 6 (Figura 3.1)** aislamos tanto el giro de 180° en el cono como el segundo giro antes de sentarse usando la energía en ventana deslizante de la velocidad angular de guiñada.
  >
  > Y en el **Módulo 8 (Figura 3.2)** detectamos cada apoyo y balanceo (`STANCE` y `SWING`) en las señales de los tobillos izquierdo y derecho, y cruzamos cada paso con los límites de las 5 fases para agregar la columna **`fase_tug`** en el CSV. Con esto sabemos exactamente cuántos pasos da cada paciente en la caminata de ida, **cuántos pasos necesita para completar el giro de 180°** y cuántos da en el regreso."

---

## Lámina 08 — Ingeniería de Datos sobre las Grabaciones de Cámara RGB-D (`Datos e-Motion/`, Módulo 10)
* **Puntos clave en pantalla:**
  * Depuración de 269 $\rightarrow$ **225 grabaciones 3D en disco**: **130 pruebas TUG** (`TUG/`) y **95 de marcha continua de 10 m** (`GAIT/`).
  * Vinculación con cohortes **`LARGE_PD`** y **`GEOREF`** (70 sujetos únicos; **48 pacientes con TUG + Marcha Continua**).
  * Unificación de esqueletos **`v1.2.0` (19 nodos)** y **`v1.3.0` (15 nodos)** sobre **`SpineBase`**.
  * Tabla de cobertura empírica por fase en las 130 pruebas TUG y máscara de continuidad ($\le 250\text{ ms}$).
* **Qué decir:**
  > "Pasando al **Pipeline 2 de cámaras de profundidad e-Motion (Módulo 10)**:
  > 1. De las 269 capturas descargadas de VIMOV depuramos 44 réplicas y pruebas de soporte, dejando **225 grabaciones válidas en disco** separadas por protocolo: **130 de TUG** y **95 de marcha continua de 10 metros**.
  > 2. Cruzando los identificadores con las cohortes clínicas `LARGE_PD` y `GEOREF`, identificamos 70 participantes únicos y comprobamos que **48 pacientes tienen tanto la prueba TUG como la de marcha continua**, lo que nos permite comparar al mismo paciente caminando en línea recta frente a la exigencia de levantarse y girar.
  > 3. También descubrimos que en cámara existen dos versiones de esqueleto: `v1.2.0` con 19 articulaciones y `v1.3.0` con 15 articulaciones (donde desaparece `MidSpine`). Estandarizamos todo el cálculo de centro de masa sobre el nodo pélvico **`SpineBase`**, que está presente en el 100 % de los archivos.
  > 4. Finalmente, medimos programáticamente la cobertura de las 5 fases en las 130 pruebas TUG (tabla derecha): demostramos que la marcha de ida y de regreso tienen **100 % de visibilidad limpia**, mientras que en el giro de 180° el intervalo temporal se detecta al 100 % por el cambio de signo de la velocidad $v_z$, pero los tobillos sufren oclusión parcial o total en el **84.8 %** de los casos por cercanía a la cámara."

---

## Lámina 09 — Algoritmo de Segmentación Óptica e-Motion: PCHIP, “Escalerita” y Wavelet Ricker (Módulos 11 y 12)
* **Puntos clave en pantalla:**
  * **Módulo 11:** Interpolación hermítica **PCHIP a 30.0 Hz**, remoción DC, FFT ($1.44\text{ Hz}$) y filtro Butterworth a $3.0\text{ Hz}$; macro-segmentación de las 5 fases con $v_z(t)$ de `SpineBase` y energía vertical $E_y(t)$ en silla.
  * **Módulo 12:** Morfología en **"escalerita"** de los tobillos, detección de "codos" de contacto de talón con **Wavelet Ricker (*Mexican Hat*, 1.0–2.5 Hz)** y cálculo booleano del **Doble Apoyo** ($\text{Stance}_{\text{Izq}}(t) \land \text{Stance}_{\text{Der}}(t)$).
* **Qué decir:**
  > "En los **Módulos 11 y 12** diseñamos el algoritmo de segmentación y extracción espacial para las cámaras:
  > * Primero corregimos la fluctuación del reloj de la cámara ($\Delta t \approx 33\text{ ms}$) usando interpolación monótona **PCHIP a 30.0 Hz**. Elegimos PCHIP porque respeta las mesetas planas cuando el pie está apoyado en el suelo sin inventar oscilaciones como haría un spline cúbico normal.
  > * En el **Módulo 11 (Figura 4.1)** segmentamos las 5 fases usando la velocidad sagital $v_z(t)$ de `SpineBase` y la energía vertical $E_y(t)$ de la pelvis y la cabeza al levantarse y sentarse.
  > * Y en el **Módulo 12 (Figura 4.2)** aprovechamos la morfología en **'escalerita'** que dibujan los dos tobillos en el eje de profundidad $Z$: cada escalón plano es un apoyo (`STANCE`) y cada rampa es un avance (`SWING`). Aplicando la transformada **Wavelet Ricker (*Mexican Hat*)**, localizamos con precisión los 'codos' de contacto de talón y medimos directamente en metros la **longitud de zancada**, la **longitud de paso**, la **amplitud de braceo** y el **porcentaje de doble apoyo** cuando ambos pies están simultáneamente en `STANCE`."

---

## Lámina 10 — Cruce Bimodal 1:1, Concordancia Temporal y Energía Espectral por Fase (Módulos 14 y 15)
* **Puntos clave en pantalla:**
  * Consolidación de los **53 pares bimodales simultáneos (`IDB1` a `IDB53`)** en `Datos IMU&eMotion/`.
  * Tabla de correlación de Pearson entre IMU y cámara: duración activa total ($r = 0.7458$, $p = 4.13 \times 10^{-9}$), levantamiento ($r = 0.6841$), sentado ($r = 0.6519$) y giro ($r = 0.6120$).
  * **Módulo 15:** Comparación de energía espectral consumida por fase y hallazgos de `Auditoria_Anomalias_Bimodales.csv`.
* **Qué decir:**
  > "En el **Pipeline 3 (Módulos 14 y 15)** cruzamos los 53 pares capturados al mismo tiempo por ambos sistemas en las brigadas de Santa Marta y CST:
  > * Comprobamos una alta concordancia estadística entre ambos equipos: en la duración activa total del TUG la correlación de Pearson es de **$r = 0.7458$ ($p = 4.13 \times 10^{-9}$)**. En la **Figura 5.1** se ve cómo las 5 fases detectadas por el IMU lumbar se alinean con la trayectoria de profundidad de la cámara, y cómo el pico de velocidad angular de giro coincide exactamente con el mínimo de distancia $Z_{\min}$ y el cruce por cero $v_z = 0$.
  > * En el **Módulo 15 (Figura 5.2)** analizamos la fracción de energía espectral consumida en cada fase por ambos sistemas, y dejamos documentada en `Auditoria_Anomalias_Bimodales.csv` la explicación de los 14 casos (como `IDB3`) donde la grabación IMU dura más que el video porque el sensor se encendió en un intento preparatorio seguido de una pausa estática de 10 a 40 segundos en la silla antes del TUG definitivo."

---

## Lámina 11 — Hallazgos Estadísticos Significativos (`p < 0.05`) y Validación frente a `R₁` (Módulos 9 y 13)
* **Puntos clave en pantalla:**
  * Contraste Pacientes con EP vs. Controles con pruebas *t* de Welch y *U* de Mann-Whitney:
    * **Longitud de zancada (TUG):** $0.839\text{ m}$ vs. $0.949\text{ m}$ ($p = 0.0032$).
    * **Longitud de paso (TUG en brigada):** $0.353\text{ m}$ vs. $0.422\text{ m}$ ($p = 0.0034$).
    * **Amplitud de braceo (TUG):** $0.270\text{ m}$ vs. $0.315\text{ m}$ ($p = 0.0065$).
    * **Duración activa TUG:** $15.91\text{ s}$ vs. $13.26\text{ s}$ en cámara ($p = 0.0082$) y $+36.2\%$ en IMU ($18.20\text{ s}$ vs. $13.37\text{ s}$).
    * **Porcentaje de Doble Apoyo (Marcha Continua 10 m):** $25.07\%$ vs. $18.23\%$ ($p = 0.0206$, $+37.5\%$ relativo).
    * **Asimetría de braceo y marcha de regreso:** $p = 0.0347$ y $p = 0.0378$.
* **Qué decir:**
  > "Al correr las pruebas *t* de Welch y *U* de Mann-Whitney sobre nuestras matrices de variables (Módulos 9 y 13), obtuvimos diferencias estadísticamente significativas ($p < 0.05$) que **confirman en nuestros propios datos de brigada exactamente los hallazgos de Molero-Mateo et al. (2026)**:
  > * En TUG, los pacientes con Parkinson muestran un **acortamiento significativo de la longitud de zancada** de 11 cm ($0.84\text{ m}$ frente a $0.95\text{ m}$, $p = 0.0032$), **menor longitud de paso** ($p = 0.0034$), **menor amplitud de braceo** ($p = 0.0065$), **mayor asimetría bilateral de braceo** ($22.7\%$ frente a $16.7\%$, $p = 0.0347$) y mayor tiempo tanto en el TUG activo ($p = 0.0082$, $+36.2\%$ en IMU) como en la caminata de regreso tras girar ($p = 0.0378$).
  > * Y en marcha continua de 10 metros, mientras la cadencia permanece prácticamente igual entre pacientes y controles ($\sim 91.5$ vs. $93.5\text{ pasos/min}$, $p = 0.66$), el **porcentaje de doble apoyo aumenta de $18.23\%$ en controles a $25.07\%$ en pacientes ($p = 0.0206$)**, demostrando que la bradicinesia se expresa en pasos más cortos y un mayor tiempo con ambos pies apoyados en el suelo para compensar la inestabilidad postural."

---

## Lámina 12 — Matriz Oficial de Análisis de Riesgos (I. Objetivo General)
* **Puntos clave en pantalla:**
  * Tabla oficial de 7 columnas integrada en la Sección 7 de `OverLeaf/PDG-II TUG.tex`.
  * Los 4 riesgos del **Objetivo General** (desbalance de controles, sincronización bimodal, costos de brigadas y consentimientos informados).
* **Qué decir:**
  > "Pasando a la matriz oficial de análisis de riesgos que construimos siguiendo el ejemplo de referencia del curso, la dividimos en cuatro láminas para que cada bloque se lea con total claridad:
  >
  > En el **Objetivo General**, el riesgo operacional principal es la **baja cantidad de muestras de controles frente a pacientes** en las brigadas (probabilidad *Probable*, impacto *Mayor*), que mitigamos programando nuevas jornadas con voluntarios sanos y aplicando estadística adaptada a grupos desbalanceados. También incluimos el riesgo tecnológico de sincronización entre equipos, los costos de desplazamiento a brigadas fuera de la ciudad y el control ético de anonimización y consentimientos informados."

---

## Lámina 13 — Matriz Oficial de Análisis de Riesgos (II. Productos 1 al 5)
* **Puntos clave en pantalla:**
  * Riesgos asociados a los **5 Productos entregables** (Conjunto de datos bimodal, Algoritmo de segmentación, Modelo de clasificación, Módulo en VIMOV e Informe final).
* **Qué decir:**
  > "En la segunda parte de la matriz abordamos los **5 Productos entregables**:
  > * En el **Producto 1** (conjunto de datos bimodal) y **Producto 2** (algoritmo de segmentación), contemplamos la pérdida de datos por desconexión, duplicados de red, la oclusión de los tobillos al girar frente a la cámara y los cambios de orientación de sensores o pausas del paciente, mitigados con nuestras reglas de descarte, la homologación de kits y el reparto funcional entre cámara e IMU.
  > * En los **Productos 3, 4 y 5**, incluimos la similitud motora entre pacientes leves y adultos mayores sanos, los tiempos de acoplamiento con la plataforma VIMOV y el seguimiento semanal de la redacción del documento final."

---

## Lámina 14 — Matriz Oficial de Análisis de Riesgos (III. Actividades `OE1` y `OE2`)
* **Puntos clave en pantalla:**
  * Desglose para `OE1.A1` (auditoría y depuración de grabaciones), `OE1.A2` (jornadas de captura de controles) y `OE2.A1` (adaptación y validación de algoritmos de segmentación).
* **Qué decir:**
  > "En la tercera lámina de la matriz desglosamos las actividades de datos y segmentación (`OE1` y `OE2`):
  > * En **`OE1.A1`**, el riesgo de mezclar pruebas de calibración o de doble tarea con pruebas TUG estándar, mitigado con la revisión de las notas clínicas y las fichas técnicas.
  > * En **`OE1.A2`**, la logística para convocar voluntarios sanos del mismo rango de edad en laboratorio y brigadas.
  > * Y en **`OE2.A1`**, las frecuencias de muestreo variables y los movimientos previos del paciente antes de la orden de inicio, mitigados con el remuestreo a 50 Hz y 30 Hz y la verificación con nuestras gráficas superpuestas."

---

## Lámina 15 — Matriz Oficial de Análisis de Riesgos (IV. Actividades `OE3` y `OE4`)
* **Puntos clave en pantalla:**
  * Desglose para `OE3.A1` (selección de variables y entrenamiento), `OE3.A2` (integración en VIMOV) y `OE4.A1` (evaluación con exactitud y sensibilidad entre grupos).
* **Qué decir:**
  > "Y en la cuarta lámina de la matriz cubrimos el modelado, la integración y la validación (`OE3` y `OE4`):
  > * En **`OE3.A1`**, el riesgo de **sobreajuste (*overfitting*)** por usar demasiadas variables frente al número de participantes, que mitigamos reduciendo la dimensionalidad previamente (con pruebas estadísticas y PLS `VIP > 0.8`).
  > * En **`OE3.A2`**, la gestión anticipada de permisos para conectar con los servicios de VIMOV manteniendo el módulo funcional primero en local.
  > * Y en **`OE4.A1`**, un riesgo metodológico fundamental: como varios participantes tienen más de una repetición grabada, incluir tomas de la misma persona tanto en entrenamiento como en prueba inflaría artificialmente las métricas. La mitigación es agrupar siempre los registros por participante (`GroupKFold`)."

---

## Lámina 16 — Cumplimiento del Cronograma y Siguientes Pasos
* **Puntos clave en pantalla:**
  * Hitos completados en Fase I (Búsqueda en anchura v2, curaduría de los 3 repositorios, 15 módulos de procesamiento, hallazgos estadísticos con $p < 0.05$ y Matriz Oficial de Riesgos).
  * Hoja de ruta: captura de controles en Laboratorio y **Brigada de La Victoria (22 al 26 de noviembre)**, y selección multivariada PLS (`VIP > 0.8`) + validación `GroupKFold`.
* **Qué decir:**
  > "Para cerrar, frente al cronograma de Fase I ya completamos y dejamos en `main` la búsqueda en anchura, la depuración de los tres conjuntos de datos con sus fichas técnicas, los 15 módulos de los tres pipelines, los hallazgos estadísticos significativos y la matriz oficial de riesgos en Overleaf.
  >
  > Nuestros próximos pasos inmediatos son ejecutar las tomas adicionales de sujetos de control en el laboratorio de la universidad y en la brigada de La Victoria del 22 al 26 de noviembre, y aplicar la selección multivariada con validación agrupada por participante para el cierre de PDG I."
