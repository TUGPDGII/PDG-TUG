# Guion de Exposición de Avances y Matriz de Riesgos — Proyecto PDG-TUG

Este documento sirve como guía de apoyo para presentar las 10 diapositivas de [`Presentacion_Avances_PDG_TUG.html`](file:///home/jjarias/Documents/UNIVERSIDAD/8vo%20semestre/PDG/PDG-TUG/Analisis%20de%20Datos/Presentacion_Avances_PDG_TUG.html) (también disponible en [`Presentacion_Avances_PDG_TUG.pptx`](file:///home/jjarias/Documents/UNIVERSIDAD/8vo%20semestre/PDG/PDG-TUG/Analisis%20de%20Datos/Presentacion_Avances_PDG_TUG.pptx)). Está redactado en un tono natural para que cualquiera del grupo pueda explicarlo con sus propias palabras durante la reunión con el profesor.

---

## Diapositiva 1 — Portada
* **Título:** Análisis Cinemático y Biomecánico Bimodal de la Prueba Timed Up and Go (PDG-TUG)
* **Qué decir:**
  > "Buenos días, profe. En esta presentación vamos a mostrar el consolidado de los avances que ya quedaron unificados en la rama `main` del repositorio: la depuración de los conjuntos de datos de IMUs y cámaras, la validación del algoritmo de segmentación del PDG anterior, los primeros resultados estadísticos comparando pacientes y controles, y la matriz oficial de análisis de riesgos que nos solicitó incorporar."

---

## Diapositiva 2 — Contexto, Objetivos Ajustados y Delimitación Bimodal
* **Puntos clave en pantalla:**
  * Objetivo General y los 4 Objetivos Específicos (con el `OE4` ajustado sin prometer un porcentaje fijo).
  * División funcional entre IMUs (50 Hz) y Cámaras RGB-D (30 Hz).
* **Qué decir:**
  > "Primero, dejamos formalizado en el documento de Overleaf el ajuste del cuarto objetivo específico (`OE4`) para evaluar la capacidad de discriminación mediante exactitud y sensibilidad a nivel de grupos, sin fijar un umbral arbitrario como el 80 %.
  >
  > Además, definimos formalmente qué aporta cada sensor según lo que vimos en las pruebas:
  > 1. Los **sensores IMU a 50 Hz** se encargan de segmentar las 5 fases temporales del TUG (levantarse, marcha de ida, giro de 180°, marcha de regreso y sentarse) y de medir los pasos dentro del giro, porque van fijos al cuerpo y no sufren oclusión.
  > 2. Las **cámaras RGB-D a 30 Hz** se utilizan en los tramos rectos de marcha para estimar variables espaciales como longitud de paso, longitud de zancada, velocidad lineal de la cadera (`SpineBase`) y amplitud de braceo, que en IMU pura son difíciles de medir sin deriva por integración."

---

## Diapositiva 3 — Consolidación y Depuración de los Conjuntos de Datos
* **Puntos clave en pantalla:**
  * **Datos IMU (`Datos IMUs/`):** 78 archivos $\rightarrow$ 12 descartados $\rightarrow$ **66 muestras válidas** (58 de pacientes con EP y 8 de controles).
  * **Datos Cámara (`Datos e-Motion/`):** 269 capturas $\rightarrow$ 44 descartadas $\rightarrow$ **225 grabaciones en disco** (130 TUG y 95 de marcha continua de 10 m).
  * **Cruce Bimodal 1 a 1 (`Datos IMU&eMotion/`):** **53 pares simultáneos** en brigadas (42 estrictamente TUG con género verificado).
* **Qué decir:**
  > "En cuanto a la organización de los datos, dividimos el repositorio en tres carpetas principales, cada una con su inventario, su ficha técnica, su tabla de variables y su documento de análisis:
  > * En **IMUs**, de los 78 archivos crudos descartamos 12 (7 pruebas técnicas sin etiqueta clínica, 2 duplicados exactos por red verificados con MD5 y 3 pruebas de doble tarea cognitiva), quedando con **66 grabaciones válidas** (58 de pacientes y 8 de controles) que exigen mínimo la espina base y ambos tobillos.
  > * En **cámaras e-Motion**, de 269 registros iniciales depuramos 44 réplicas de sincronización y pruebas de soporte, dejando **225 archivos en disco**: 130 de TUG y 95 de marcha continua de 10 metros.
  > * Y al cruzar las marcas de tiempo y datos demográficos de las brigadas, consolidamos **53 pares bimodales 1 a 1** (42 de ellos estrictamente TUG con coincidencia total de género)."

---

## Diapositiva 4 — Validación del Algoritmo de Segmentación IMU (Proyecto Anterior)
* **Puntos clave en pantalla:**
  * Adecuación de lectura JSON y remuestreo uniforme a 50 Hz.
  * Flujo del algoritmo predecesor: Butterworth pasabajas (3 Hz), energía en ventana deslizante + FFT en tronco y velocidad angular para giros.
  * **Resultado:** **63 de las 66 muestras válidas (95.5 %)** segmentadas en las 5 fases.
* **Qué decir:**
  > "Para cumplir con el segundo objetivo específico (`OE2`), pusimos a prueba el algoritmo de segmentación que habían desarrollado los compañeros del PDG anterior sobre nuestras 66 muestras válidas, haciendo únicamente la adaptación del formato JSON y el remuestreo a 50 Hz para evitar errores de ejecución.
  >
  > El método filtra las señales a 3 Hz, calcula la energía por ventana deslizante con FFT en la espina base para encontrar los pulsos de levantarse y sentarse, e integra la velocidad angular del tronco para delimitar los dos giros de 180°.
  >
  > Al correrlo sobre las 66 grabaciones, el algoritmo identificó las 5 fases en **63 muestras (95.5 %)**. También nos permitió diagnosticar por qué falla en casos puntuales: en dos controles previos a brigada cambia el eje donde cae la gravedad en el sensor lumbar, y en algunas grabaciones donde el paciente da un giro o se sienta antes de iniciar formalmente la prueba, tomar siempre el primer pulso desacomoda el inicio de la caminata de ida."

---

## Diapositiva 5 — Gráfica Compuesta de Fases, Pasos y Pipeline de Cámara
* **Puntos clave en pantalla:**
  * Gráfica superpuesta de energía de flexo-extensión de tronco + energía de giro con las 5 fases delimitadas.
  * Etiquetado de cada paso (`Stance` / `Swing`) según la fase TUG y conteo de pasos en el giro.
  * Procesamiento en cámara: interpolación PCHIP a 30 Hz, filtro a 3 Hz y detección de apoyos con wavelets.
* **Qué decir:**
  > "Siguiendo la recomendación de la última reunión, implementamos la gráfica compuesta donde se superponen la energía de flexo-extensión del tronco y la energía de guiñada del giro, marcando con franjas de color y líneas verticales dónde empieza y termina cada una de las 5 fases.
  >
  > Además, en la detección de apoyos y balanceos (`Stance` y `Swing`) de los tobillos agregamos la columna `fase_tug` para saber exactamente qué pasos ocurren durante la marcha de ida, cuáles ocurren dentro del giro de 180° y cuáles en el regreso. En paralelo, para las cámaras aplicamos interpolación PCHIP a 30 Hz y transformada wavelet sobre las trayectorias de los tobillos para medir longitud de paso y doble apoyo."

---

## Diapositiva 6 — Avance en Extracción de Variables y Contraste Estadístico Basal
* **Puntos clave en pantalla:**
  * Comparación preliminar entre Pacientes con EP y Controles (pruebas *t* de Welch y *U* de Mann-Whitney):
    * **IMUs:** Duración efectiva TUG ($18.20\text{ s}$ vs. $13.37\text{ s}$, $+36.2\%$), tiempo total de marcha ($10.44\text{ s}$ vs. $7.10\text{ s}$, $+47.0\%$) y duración de balanceo ($0.50\text{ s}$ vs. $0.36\text{ s}$).
    * **Cámaras RGB-D:** Longitud de zancada en TUG ($0.84\text{ m}$ vs. $0.95\text{ m}$, $p = 0.0032$), amplitud de braceo ($0.27\text{ m}$ vs. $0.32\text{ m}$, $p = 0.0065$) y porcentaje de doble apoyo en marcha continua ($25.07\%$ vs. $18.23\%$, $p = 0.0206$).
* **Qué decir:**
  > "Con las tablas de variables ya generadas, hicimos el primer contraste estadístico usando la prueba *t* de Welch y *U* de Mann-Whitney por el desbalance entre grupos:
  > * En **IMUs**, vemos que los pacientes con Parkinson tardan en promedio un 36 % más en la duración efectiva del TUG ($18.20\text{ s}$ frente a $13.37\text{ s}$ en controles) y un 47 % más en el tiempo total de marcha.
  > * En **cámaras**, encontramos diferencias estadísticamente significativas ($p < 0.05$) en variables clínicas clave de la enfermedad: los pacientes tienen menor longitud de zancada ($0.84\text{ m}$ frente a $0.95\text{ m}$, $p = 0.0032$), menor amplitud de braceo ($p = 0.0065$) y, en marcha continua, un mayor porcentaje de tiempo en doble apoyo ($25.1\%$ frente a $18.2\%$, $p = 0.0206$), lo que refleja la postura más cautelosa y la bradicinesia."

---

## Diapositiva 7 — Matriz Oficial de Análisis de Riesgos (I. Objetivo General)
* **Puntos clave en pantalla:**
  * Tabla con las 7 columnas oficiales (*Tipo de riesgo, Descripción, Probabilidad, Impacto, Efecto, Medidas de mitigación, Supuestos*).
  * Los 4 riesgos transversales del **Objetivo General**.
* **Qué decir:**
  > "Pasando a la matriz de análisis de riesgos que construimos siguiendo el formato de referencia y que ya dejamos integrada tanto en el documento de Overleaf como en el repositorio, la dividimos en tres láminas para que se pueda leer con claridad:
  >
  > En el **Objetivo General**, el riesgo operacional más importante es el **desbalance entre pacientes y controles** en las muestras de brigada (probabilidad *Probable*, impacto *Mayor*), que mitigamos programando tomas adicionales de controles en laboratorio y brigadas y aplicando pruebas no paramétricas y validación estratificada. También contemplamos las fallas de sincronización entre equipos, los costos de desplazamiento a brigadas y el cumplimiento de consentimientos informados."

---

## Diapositiva 8 — Matriz Oficial de Análisis de Riesgos (II. Productos 1 al 5)
* **Puntos clave en pantalla:**
  * Riesgos asociados a los **5 Productos entregables** (Conjunto de datos bimodal, Algoritmo de segmentación, Modelo de clasificación, Módulo en VIMOV y Monografía final).
* **Qué decir:**
  > "En la segunda lámina de la matriz agrupamos los riesgos de los **5 Productos entregables**:
  > * En el **Producto 1** (conjunto de datos bimodal) y **Producto 2** (algoritmo de segmentación), contemplamos los riesgos tecnológicos por cortes de conexión en campo, desconexión de sensores o cambios en la orientación de los ejes respecto al proyecto anterior, mitigados con la validación de los 3 sensores mínimos y la revisión de ejes antes de segmentar.
  > * Y en los **Productos 3, 4 y 5**, incluimos el riesgo de solapamiento de variables en pacientes leves, posibles demoras en la integración con los servicios de VIMOV y el control de tiempos de redacción de la monografía con entregas parciales."

---

## Diapositiva 9 — Matriz Oficial de Análisis de Riesgos (III. Actividades `OE1` a `OE4`)
* **Puntos clave en pantalla:**
  * Desglose por actividades `OE1.A1`, `OE1.A2`, `OE2.A1`, `OE3.A1`, `OE3.A2` y `OE4.A1`.
* **Qué decir:**
  > "En la tercera lámina de la matriz desglosamos los riesgos por actividad de cada objetivo específico (`OE1` a `OE4`):
  > * En **`OE1.A1` y `OE1.A2`**, abordamos el riesgo de mezclar pruebas de calibración técnica con pruebas clínicas —lo cual resolvimos con las fichas técnicas de descarte— y la logística para convocar voluntarios de control adicionales.
  > * En **`OE2.A1`**, el riesgo de tasas de muestreo variables entre equipos y movimientos previos del paciente antes de la orden de inicio, que mitigamos interpolando a frecuencias fijas (50 Hz y 30 Hz) y verificando con las gráficas superpuestas.
  > * En **`OE3.A1` y `OE3.A2`**, el riesgo de sobreajuste (*overfitting*) al entrenar los clasificadores y los permisos técnicos para conectar con MinIO y PostgreSQL en VIMOV.
  > * Finalmente, en **`OE4.A1`**, un riesgo metodológico clave: como varios participantes tienen más de una repetición del TUG, si partiéramos los archivos al azar habría fuga de información entre entrenamiento y prueba. La mitigación es agrupar siempre por participante para que todas las tomas de una misma persona queden en el mismo subconjunto."

---

## Diapositiva 10 — Estado frente al Cronograma y Próximos Pasos
* **Puntos clave en pantalla:**
  * Actividades completadas en Fase I (Inventario, fichas técnicas, validación del algoritmo anterior, cruce bimodal 1 a 1, primeros contrastes estadísticos y matriz de riesgos).
  * Próximos pasos inmediatos: ampliación de muestras de control (laboratorio y brigada de La Victoria del 22 al 26 de noviembre), ajuste fino de segmentación en casos atípicos y consolidación del documento de cierre de PDG I.
* **Qué decir:**
  > "Para cerrar, frente al cronograma de Fase I ya tenemos completada la depuración de los dos conjuntos de datos, las fichas técnicas, el cruce bimodal 1 a 1, la validación del algoritmo del PDG anterior, las primeras pruebas estadísticas y la matriz de riesgos dentro del documento en Overleaf.
  >
  > Nuestros siguientes pasos se concentran en recolectar las muestras adicionales de sujetos de control —aprovechando las sesiones en laboratorio y la brigada de finales de noviembre en La Victoria—, afinar la selección de variables en los casos atípicos de segmentación y dejar listo el documento final de PDG I."
