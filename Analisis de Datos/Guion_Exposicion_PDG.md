# Guion de Exposición de Avances, Estado del Arte y Matriz de Riesgos — Proyecto PDG-TUG

Este documento sirve como guía de apoyo para presentar las 12 láminas de [`Presentacion_Avances_PDG_TUG.html`](file:///home/jjarias/Documents/UNIVERSIDAD/8vo%20semestre/PDG/PDG-TUG/Analisis%20de%20Datos/Presentacion_Avances_PDG_TUG.html). Está redactado en un tono natural para que cualquiera del grupo pueda explicarlo con sus propias palabras durante la sustentación con los profesores.

---

## Lámina 01 — Portada Editorial
* **Título:** Análisis Cinemático y Biomecánico Bimodal de la Prueba *Timed Up and Go* en Enfermedad de Parkinson
* **Qué decir:**
  > "Buenos días, profesores. En esta presentación vamos a mostrar el consolidado de nuestros avances en `main`: la búsqueda en anchura y priorización de variables que guía nuestro modelo, la curaduría de los tres conjuntos de datos del repositorio (`Datos IMUs/`, `Datos e-Motion/` y `Datos IMU&eMotion/`), los tres pipelines de procesamiento y fusión bimodal (15 módulos en total), los resultados estadísticos donde ya encontramos diferencias significativas entre pacientes y controles, y la matriz oficial de análisis de riesgos."

---

## Lámina 02 — Tesis Central, Objetivos y Complementariedad Bimodal
* **Puntos clave en pantalla:**
  * Tesis central: el tiempo total del TUG oculta déficits tempranos; descomponer la prueba en sus 5 fases con sensores complementarios revela las alteraciones reales.
  * Ajuste formal del `OE4` en Overleaf (evaluar discriminación grupal con exactitud y sensibilidad sin fijar un umbral arbitrario del 80 %).
  * División funcional: **IMUs (50 Hz)** vs. **Cámaras RGB-D (30 Hz)**.
* **Qué decir:**
  > "El punto de partida de nuestro trabajo es que medir únicamente el tiempo total del TUG no basta para detectar alteraciones sutiles en etapas tempranas. Por eso combinamos dos tecnologías que se complementan físicamente:
  > 1. Los **sensores inerciales IMU a 50 Hz**, fijos a la espalda lumbar, tobillos y muñecas, no sufren oclusión visual. Se encargan de segmentar las 5 fases temporales del TUG, medir las velocidades angulares de inclinación (*pitch*) y giro (*yaw*), y contar los pasos dentro del giro de 180°.
  > 2. Las **cámaras de profundidad RGB-D a 30 Hz**, en los tramos rectos de caminata donde tienen 100 % de visibilidad, entregan medidas espaciales directas en metros sin la deriva que tendría integrar un acelerómetro: longitud de zancada, longitud de paso, velocidad lineal de la pelvis (`SpineBase`), porcentaje de doble apoyo y amplitud/asimetría de braceo."

---

## Lámina 03 — Búsqueda en Anchura v2: De la Literatura al Pipeline (`Búsqueda en anchura v2.pdf`)
* **Puntos clave en pantalla:**
  * **`R₁` — Molero-Mateo et al. (2026, *Sensors*):** 79 participantes (38 EP temprana `mH&Y 1–1.5` y `2` en estado *OFF* vs. 41 controles, 316 ensayos).
  * **`R₂` — Vervoort et al. (2016, *PLOS ONE*):** Segmentación con IMU lumbar (*pitch*, *yaw*, aceleración AP + wavelets) y reducción multivariada PLS (`VIP > 0.8`) + PLS-DA (AUC 94.7 %).
  * Tabla de priorización de variables para `TUG 2` (**Alta**, **Media** y **Baja**).
* **Qué decir:**
  > "Antes de extraer variables a ciegas, documentamos en nuestra *Búsqueda en anchura v2* dos estudios clave que fundamentan nuestras decisiones técnicas:
  > * El primero es **Molero-Mateo et al. (2026)** en *Sensors*, con 316 ensayos en pacientes con Parkinson temprano (`mH&Y 1 a 2`). Ellos demuestran que el tiempo total del TUG no separa controles de estadios `1–1.5`, mientras que la **duración del primer giro** sí lo logra. Además, identifican como marcadores de **Prioridad Alta** en marcha el **mayor porcentaje de doble apoyo**, la **menor longitud de zancada**, la **velocidad de marcha** y el **ROM sagital del tronco**, junto con la **asimetría de brazo/codo** como marcador temprano. También demuestran que los coeficientes de variación (*CV*) paso a paso y el ancho de paso no discriminan en un recorrido corto de 3 metros, por lo que los dejamos en prioridad baja.
  > * El segundo es **Vervoort et al. (2016)**, que valida el flujo sobre IMU lumbar usando *pitch* para levantarse/sentarse, *yaw* para giros y wavelets para contactos de pie, seleccionando las mejores variables con PLS (`VIP > 0.8`) antes de clasificar. Un detalle clave que señalan es que el *doble apoyo* no debe inferirse con una sola IMU lumbar sin tener contacto y despegue de ambos pies; por eso en nuestro proyecto lo calculamos directamente con ambos tobillos en la cámara RGB-D y en las IMUs distales."

---

## Lámina 04 — Auditoría de Brigadas, Homologación de Hardware y Cruce Bimodal
* **Puntos clave en pantalla:**
  * **`Datos IMUs/`:** 78 archivos $\rightarrow$ 12 descartados $\rightarrow$ **66 muestras válidas** (61 sujetos únicos: 54 EP y 7 controles). Homologación `Kit Base` vs. `Kit K1`.
  * **`Datos e-Motion/`:** **225 capturas 3D** en disco (130 TUG y 95 de marcha continua de 10 m). Cohortes `LARGE_PD` y `GEOREF` (48 pacientes con TUG + Marcha Continua). Unificación de esqueletos `v1.2.0` (19 nodos) y `v1.3.0` (15 nodos) en `SpineBase`.
  * **`Datos IMU&eMotion/`:** **53 pares bimodales 1 a 1** (`IDB1` a `IDB53`).
* **Qué decir:**
  > "En cuanto a ingeniería de datos, estructuramos el repositorio en tres carpetas auditadas:
  > 1. En **`Datos IMUs/`**, de 78 archivos descartamos 12 (7 pruebas internas sin paciente, 2 duplicados exactos por red verificados con MD5 y 3 ensayos de doble tarea cognitiva), quedando con **66 grabaciones válidas** de 61 personas únicas. Reconstruimos la identidad de los pacientes con tomas múltiples (como pacientes con estimulación cerebral profunda DBS o pausas en la prueba) y normalizamos las dos generaciones de hardware (`Kit Base` y `Kit K1`) para que el código procese el 100 % del conjunto.
  > 2. En **`Datos e-Motion/`**, depuramos 269 capturas iniciales dejando **225 grabaciones 3D en disco**: 130 de TUG y 95 de marcha continua de 10 metros, vinculadas a las cohortes `LARGE_PD` y `GEOREF` (donde 48 pacientes tienen tanto TUG como marcha continua). También resolvimos el cambio de versión del software de cámara unificando los esqueletos de 19 y 15 articulaciones sobre el nodo pélvico `SpineBase`.
  > 3. Y en **`Datos IMU&eMotion/`**, cruzamos fecha, hora UTC y datos demográficos de las brigadas de Santa Marta y CST para consolidar **53 pares bimodales 1 a 1** capturados simultáneamente por ambos equipos."

---

## Lámina 05 — Pipeline 1 (IMUs): Segmentación de 5 Fases y Eventos de Paso por Fase
* **Puntos clave en pantalla:**
  * Módulos 5 al 8 de `PDGI_Colab.ipynb`: interpolación a 50 Hz, filtro Butterworth a 3 Hz, energía lumbar en ventana deslizante + velocidad angular de giro (*yaw*).
  * Etiquetado `SWING` / `STANCE` por `fase_tug` y conteo de pasos en el giro.
  * **63 de 66 muestras válidas (95.5 %)** segmentadas en sus 5 fases.
* **Qué decir:**
  > "En el **Pipeline 1 (Módulos 5 al 8)** procesamos las 66 muestras inerciales: primero alineamos los relojes de los 5 sensores a una rejilla uniforme de 50 Hz y filtramos a 3 Hz sin desfase.
  >
  > Luego, como se ve en la **Figura 1.1**, superponemos la energía de flexo-extensión del tronco con la energía rotacional de guiñada para delimitar de forma contigua las 5 fases del TUG, logrando segmentar **63 de las 66 muestras válidas (95.5 %)**. En la **Figura 1.2** mostramos el Módulo 8, donde detectamos cada apoyo y balanceo (`STANCE` y `SWING`) en los tobillos y le asignamos automáticamente en qué fase del TUG ocurrió, lo que nos permite contar con exactitud cuántos pasos emplea el paciente para girar 180°."

---

## Lámina 06 — Pipeline 2 (Cámaras e-Motion): PCHIP, “Escalerita” de Tobillos y Wavelet Ricker
* **Puntos clave en pantalla:**
  * Auditoría de cobertura en las 130 pruebas TUG: 100 % en marcha de ida y regreso vs. 84.8 % de oclusión distal en el giro.
  * Módulos 11 y 12: interpolación monótona **PCHIP a 30 Hz**, filtro a 3 Hz, velocidad sagital $v_z(t)$ y **Wavelet Ricker (*Mexican Hat*, 1.0–2.5 Hz)** sobre la "escalerita" de tobillos para medir contacto de talón y **Doble Apoyo**.
* **Qué decir:**
  > "En el **Pipeline 2 (Módulos 11 y 12)** primero medimos programáticamente la visibilidad de las 5 fases en las 130 grabaciones TUG de cámara: comprobamos que las fases de marcha de ida y regreso tienen **100 % de captura limpia**, mientras que en el giro de 180°, aunque el intervalo temporal se delimita al 100 % cuando la velocidad $v_z$ invierte su signo, los tobillos sufren oclusión parcial o total en el **84.8 %** de los casos por cercanía al lente.
  >
  > Para extraer las variables espaciales en la caminata, aplicamos interpolación **PCHIP a 30 Hz** (que evita oscilaciones falsas en las mesetas de apoyo) y analizamos la morfología en **'escalerita'** que describen los tobillos al acercarse o alejarse de la cámara (**Figura 2.2**). Usando la transformada **Wavelet Ricker (*Mexican Hat*)**, detectamos con precisión los 'codos' de contacto de talón y calculamos el **Doble Apoyo** como los instantes en que ambos pies están simultáneamente en fase `STANCE`."

---

## Lámina 07 — Pipeline 3 (Bimodal 1:1): Concordancia Física y Energía Espectral por Fase
* **Puntos clave en pantalla:**
  * Módulos 14 y 15 sobre los **53 pares simultáneos**: correlación de Pearson $r = 0.7458$ ($p = 4.13 \times 10^{-9}$) en duración activa TUG; correlaciones significativas en levantamiento ($r = 0.6841$), sentado ($r = 0.6519$) y giro ($r = 0.6120$).
  * Distribución de energía espectral consumida por fase y auditoría de anomalías operacionales (`Auditoria_Anomalias_Bimodales.csv`).
* **Qué decir:**
  > "En el **Pipeline 3 (Módulos 14 y 15)** enfrentamos cara a cara las señales de los 53 pares bimodales:
  > * Encontramos una correlación altamente significativa entre la duración activa medida por el IMU y por la cámara ($r = 0.7458$, $p = 4.13 \times 10^{-9}$). En la **Figura 3.1** se observa cómo el pico de velocidad angular de guiñada en el IMU lumbar coincide en el tiempo con el mínimo de profundidad $Z_{\min}$ y el cruce por cero de la velocidad en la cámara.
  > * En el **Módulo 15 (Figura 3.2)** comparamos la distribución de energía espectral por fase entre ambas modalidades, y documentamos en `Auditoria_Anomalias_Bimodales.csv` los casos de brigada donde el sensor IMU se encendió durante un intento preparatorio seguido de una pausa estática de 10 a 40 segundos en la silla antes del TUG real."

---

## Lámina 08 — Hallazgos Estadísticos Basales (`p < 0.05`) y Contraste con Literatura (`R₁`)
* **Puntos clave en pantalla:**
  * Pruebas *t* de Welch y *U* de Mann-Whitney (Módulos 9 y 13) comparadas directamente con Molero-Mateo et al. (2026):
    * **Longitud de zancada (TUG):** $0.839\text{ m}$ en EP vs. $0.949\text{ m}$ en controles ($p = 0.0032$).
    * **Longitud de paso (TUG en brigada):** $0.353\text{ m}$ vs. $0.422\text{ m}$ ($p = 0.0034$).
    * **Amplitud y asimetría de braceo (TUG):** menor amplitud ($0.270\text{ m}$ vs. $0.315\text{ m}$, $p = 0.0065$) y mayor asimetría ($22.74\%$ vs. $16.71\%$, $p = 0.0347$).
    * **Duración activa TUG:** $15.91\text{ s}$ vs. $13.26\text{ s}$ en cámara ($p = 0.0082$) y $+36.2\%$ en IMU ($18.20\text{ s}$ vs. $13.37\text{ s}$).
    * **Porcentaje de Doble Apoyo (Marcha Continua 10 m):** $25.07\%$ en EP vs. $18.23\%$ en controles ($p = 0.0206$, $+37.5\%$ relativo).
* **Qué decir:**
  > "Al aplicar las pruebas *t* de Welch y *U* de Mann-Whitney sobre nuestras tablas de variables, cumplimos la meta de obtener hallazgos estadísticamente significativos ($p < 0.05$) antes del cierre de PDG I, y lo más valioso es que **nuestros resultados reproducen en nuestra cohorte lo reportado por Molero-Mateo et al. (2026)**:
  > * En TUG, los pacientes presentan un **acortamiento significativo de la zancada** de 11 centímetros ($0.84\text{ m}$ frente a $0.95\text{ m}$, $p = 0.0032$), **menor amplitud de braceo** ($p = 0.0065$), **mayor asimetría de braceo** ($22.7\%$ frente a $16.7\%$, $p = 0.0347$) y un retorno más lento a la silla tras el giro ($p = 0.0378$).
  > * Y en marcha continua de 10 metros, mientras la cadencia se mantiene casi idéntica ($\sim 91.5$ pasos por minuto), el **porcentaje de doble apoyo sube de $18.2\%$ en controles a $25.1\%$ en pacientes ($p = 0.0206$)**, confirmando que la lentitud del paciente responde a pasos más cortos y mayor tiempo con ambos pies en tierra para proteger su estabilidad."

---

## Lámina 09 — Matriz Oficial de Análisis de Riesgos (I. Objetivo General)
* **Puntos clave en pantalla:**
  * Formato oficial de 7 columnas intégré en la Sección 7 de `OverLeaf/PDG-II TUG.tex`.
  * Los 4 riesgos transversales del **Objetivo General** (desbalance de controles, sincronización bimodal, costos de brigadas y consentimientos informados).
* **Qué decir:**
  > "Pasando a la matriz oficial de análisis de riesgos que incorporamos en el documento de Overleaf siguiendo el formato de referencia, la dividimos en tres láminas para que se lea con total claridad:
  >
  > En el **Objetivo General**, el riesgo operacional principal es el **desbalance entre pacientes y controles** en las jornadas de captura (probabilidad *Probable*, impacto *Mayor*), que mitigamos con nuevas jornadas de captura de voluntarios sanos y estadística adaptada a grupos desbalanceados. También contemplamos la sincronización entre equipos, los costos de desplazamiento a brigadas y la verificación de consentimientos informados y anonimización."

---

## Lámina 10 — Matriz Oficial de Análisis de Riesgos (II. Productos 1 al 5)
* **Puntos clave en pantalla:**
  * Riesgos asociados a los **5 Productos entregables** (Conjunto de datos bimodal, Algoritmo de segmentación, Modelo de clasificación, Módulo en VIMOV e Informe final).
* **Qué decir:**
  > "En la segunda lámina desglosamos los **5 Productos entregables**:
  > * En los **Productos 1 y 2**, abordamos los riesgos tecnológicos por desconexión de sensores, duplicados de red, oclusión de tobillos al girar frente a la cámara y cambios en la orientación de los sensores o pausas del paciente, mitigados con nuestras reglas de control de calidad, la homologación de kits y el reparto funcional entre cámara e IMU.
  > * En los **Productos 3, 4 y 5**, contemplamos la similitud motora entre pacientes leves y adultos mayores sanos, los tiempos de integración con la plataforma VIMOV y el cronograma de entregas parciales del documento escrito."

---

## Lámina 11 — Matriz Oficial de Análisis de Riesgos (III. Actividades `OE1` a `OE4`)
* **Puntos clave en pantalla:**
  * Desglose por actividades `OE1.A1`, `OE1.A2`, `OE2.A1`, `OE3.A1`, `OE3.A2` y `OE4.A1`.
* **Qué decir:**
  > "En la tercera lámina de la matriz cubrimos las actividades de los cuatro objetivos específicos (`OE1` a `OE4`):
  > * Destacamos en **`OE1.A1` y `OE1.A2`** el aislamiento de pruebas de calibración o doble tarea y la convocatoria de voluntarios sanos del mismo rango de edad;
  > * En **`OE2.A1`**, la interpolación a frecuencias fijas (50 Hz y 30 Hz) y la validación visual con gráficas superpuestas frente a ensayos con movimientos previos;
  > * Y en **`OE3.A1` y `OE4.A1`**, dos riesgos metodológicos críticos para el clasificador: evitar el sobreajuste (*overfitting*) reduciendo antes el número de variables, y evitar la fuga de datos agrupando siempre por participante (`GroupKFold`) para que distintas repeticiones de una misma persona nunca queden repartidas entre entrenamiento y prueba."

---

## Lámina 12 — Cumplimiento del Cronograma y Siguientes Pasos
* **Puntos clave en pantalla:**
  * Hitos completados al 100 % en `main` (Búsqueda en anchura v2, curaduría de los 3 datasets, 15 módulos de procesamiento, hallazgos estadísticos con $p < 0.05$ y Matriz Oficial de Riesgos).
  * Hoja de ruta: toma de controles adicionales en Laboratorio y **Brigada de La Victoria (22 al 26 de noviembre)**, y selección multivariada PLS (`VIP > 0.8`) + validación `GroupKFold`.
* **Qué decir:**
  > "Para concluir, frente al cronograma de Fase I ya tenemos completados y subidos a la rama `main` la búsqueda en anchura, los tres conjuntos de datos depurados con sus fichas técnicas, los 15 módulos de procesamiento inercial, óptico y bimodal, los primeros hallazgos estadísticos significativos y la matriz de riesgos en Overleaf.
  >
  > Nuestros siguientes pasos inmediatos son ampliar la muestra de sujetos de control en el laboratorio y en la brigada de La Victoria del 22 al 26 de noviembre, y aplicar la selección multivariada de variables con validación agrupada por sujeto para cerrar el documento de PDG I."
