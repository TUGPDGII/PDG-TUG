oct 6, 2026

## **Reunión del 6 oct 2026 a las 08:54 GMT-05:00**

Registros de la reunión [Transcripción](https://docs.google.com/document/d/18YSjtkmU1vcjPwAKgVMipwWwZ0Qq1WZeuoXxAzdp8CY/edit?usp=drive_web&tab=t.ughuxx2pbupg) [Grabación](https://drive.google.com/file/d/1Vteom96x-mwGlcCVyGueQbPjRcLuAmxO/view?usp=drive_web) 

### **Resumen**

Revisión metodológica del proyecto evaluando integración y métricas estadísticas.

**Alineación de objetivos y alcance**  
Propuesta de combinar el tercer objetivo integrando BIMOP al final del desarrollo.

**Análisis del dataset y variables**  
Depuración de registros duplicados e identificación de 63 pacientes y 8 controles.

**Formulación del cuarto objetivo**  
Validación del desempeño del algoritmo de clasificación mediante métricas estándar de evaluación.

### **Decisiones**

## **Acordada**

* **Estructuración de los objetivos específicos del proyecto** Se acordó modificar el tercer objetivo para incluir la integración con la plataforma Bimop y añadir un objetivo final enfocado en la validación del estudio.  
* **Adopción de una metodología mixta de desarrollo** Se definió emplear una metodología mixta que combina bucles de CRISP-DM para el entendimiento y modelado de datos, y una metodología iterativa incremental para la fase de despliegue e integración.  
* **Criterios de validez para las muestras de datos** Se estableció que una muestra es válida si contiene como mínimo tres sensores específicos y se descartarán todos los registros duplicados.  
* **Levantamiento adicional de datos de control** Se determinó planear un levantamiento de datos de aproximadamente 20 personas de control adicionales para equilibrar el conjunto de datos del clasificador.  
* **Redacción definitiva del cuarto objetivo** Se fijó formalmente que el último objetivo consistirá en validar el desempeño del algoritmo de clasificación mediante métricas como exactitud, sensibilidad y puntaje F1.  
* **Aplicación directa del algoritmo de segmentación** Se acordó aplicar el algoritmo de segmentación directamente dentro de la metodología del estudio.  
* **Tratamiento de muestras con doble tarea** Se determinó seguir tratando las muestras de doble tarea como muestras normales de pacientes o descartarlas debido a su bajo número.

### **Próximos pasos**

- [ ] \[Esteban Guarin Valencia, Santiago Gomez Robledo\] Actualizar objetivos: Actualizar los objetivos del proyecto. Se debe modificar el tercer objetivo para incluir la integración con la plataforma BMA y añadir un nuevo objetivo específico para la validación.  
- [ ] \[El grupo\] Recolectar datos de control: Realizar el levantamiento de datos de aproximadamente 20 nuevos sujetos de control. El objetivo es mejorar el balanceo del conjunto de datos para el clasificador.  
- [ ] \[El grupo\] Redactar metodología y cronograma: Redactar la sección de metodología y el cronograma del proyecto. Esto debe seguir la estructura discutida en la reunión.  
- [ ] \[Juan José Arias Gallego, Heiner Danit Rincon\] Limpiar datos: Eliminar las muestras duplicadas detectadas en el script de procesamiento de datos. Es necesario asegurar la integridad del dataset antes del análisis.  
- [ ] \[El grupo\] Aplicar algoritmo segmentación: Implementar el algoritmo de segmentación en las muestras actuales para separar las fases de marcha y extraer las variables temporales.  
- [ ] \[El grupo\] Validar algoritmo clasificación: Evaluar el desempeño del algoritmo de clasificación utilizando métricas de exactitud, sensibilidad y F1 score.  
- [ ] \[El grupo\] Incluir matriz confusión: Integrar la matriz de confusión, incluyendo falsos positivos y negativos, como cuarto objetivo dentro de los documentos del proyecto.  
- [ ] \[El grupo\] Filtrar referencias: Continuar con la selección y filtrado de las referencias más significativas de la literatura para el estudio.

### **Detalles**

* **Criterios para la verificación y medición de objetivos específicos**: Esteban Guarin Valencia solicitó establecer un indicador, número o porcentaje de habilidad para verificar el cumplimiento de los objetivos específicos. Santiago Gomez Robledo aclaró que se debe definir cómo contrastar cada objetivo (mediante otro estudio o prueba similar), mientras que Domiciano Rincón precisó que se debe determinar qué entregable específico respalda y valida la salida de cada objetivo ([00:01:37](#00:01:37)).  
* **Alineación de objetivos y alcance de la integración con BIMOP**: Esteban Guarin Valencia reportó que el profesor Navarro recomendó añadir un objetivo de validación del algoritmo de clasificación y degradar la integración con la plataforma BIMOP a una subtarea ([00:01:37](#00:01:37)). Esteban Guarin Valencia argumentó que la integración debería ocurrir al final, una vez validado el algoritmo ([00:02:57](#00:02:57)). Domiciano Rincón corrigió la propuesta sugiriendo combinar el tercer objetivo añadiendo la integración a BIMOP como la parte final del desarrollo, e indicó mover la validación al objetivo final alineándolo directamente con el objetivo general ([00:01:37](#00:01:37)) ([00:04:13](#00:04:13)).  
* **Estrategia y métricas para la validación del algoritmo de clasificación**: Domiciano Rincón explicó que la validación no debe comprometerse con un umbral de precisión fijo (como superar el 80%), ya que descubrir que los datos no son clasificables sigue siendo un resultado válido. Señaló que el objetivo debe orientarse a la metodología de evaluación utilizando métricas estándar de clasificadores frente al desbalance de datos, tales como \*accuracy\*, precisión, \*recall\* (sensibilidad), matriz de confusión y \*F1-score\*. Santiago Gomez Robledo destacó la coincidencia con las recomendaciones previas de Navarro ([00:05:39](#00:05:39)) ([00:08:11](#00:08:11)), mientras que Esteban Guarin Valencia y Juan José Arias Gallego indicaron no haber visto aún la materia de analítica de datos ([00:09:25](#00:09:25)). Domiciano Rincón aseguró que Heiner Danit Rincon domina dichos conceptos estadísticos ([00:10:47](#00:10:47)).  
* **Exploración del conjunto de datos y depuración de muestras**: Domiciano Rincón detalló el proceso de depuración del \*dataset\*: descartar registros incompletos por fallas de sensores, evaluar las proporciones entre controles y pacientes, y probar el algoritmo de segmentación previo para ajustarlo si los nuevos dispositivos lo requieren ([00:10:47](#00:10:47)). Juan José Arias Gallego informó que desarrollaron un \*script\* en Python para procesar datos de sensores IMU, utilizando combinaciones de fecha de nacimiento, altura y otros marcadores para asociar las grabaciones anonimizadas a identificadores únicos por persona ([00:11:59](#00:11:59)). Domiciano Rincón validó la estrategia de anonimización acorde al estándar GHGIS 2 y los requerimientos de protección de datos de la Fundación Valle del Lili ([00:13:24](#00:13:24)) ([00:25:32](#00:25:32)).  
* **Revisión de antecedentes para la extracción de variables biomecánicas**: Juan José Arias Gallego mencionó que el profesor Navarro sugirió revisar la literatura de Molero Mateo sobre la prueba \*Timed Up and Go\* (TUG) para identificar biomarcadores temporales y espaciotemporales ([00:14:41](#00:14:41)).  
* **Definición de la metodología de desarrollo del proyecto**: Domiciano Rincón estructuró el marco metodológico como un enfoque mixto. La fase actual emplea el marco CRISP-DM ejecutando ciclos iterativos en cinco bloques: \*business understanding\*, \*data understanding\*, \*data preparation\*, \*modeling\* y \*evaluation\* ([00:17:04](#00:17:04)) ([00:22:41](#00:22:41)). Explicó que el despliegue (\*deployment\*) consistirá en la integración final a la plataforma BIMOP utilizando una metodología iterativa incremental (como \*sprints\*), proceso programado para el siguiente semestre ([00:20:24](#00:20:24)).  
* **Inconsistencias y estructura de sensores en las grabaciones**: Heiner Danit Rincon planteó dudas sobre por qué existen personas con múltiples grabaciones y otras con registros incompletos o códigos de archivos específicos ([00:23:56](#00:23:56)). Domiciano Rincón aclaró que en las brigadas de campo se generan omisiones por pruebas erróneas o fallas de sensores. Precisó que una prueba se considera válida para el estudio si cuenta con un mínimo de tres sensores IMU: dos en los tobillos y uno en la base de la columna (\*spine base\*) ([00:27:42](#00:27:42)). Asimismo, aclaró que los sensores en los brazos son opcionales para evaluar parámetros como el \*arm swinging\* o la asimetría, pero no son indispensables ([00:28:51](#00:28:51)).  
* **Tratamiento de registros duplicados por sincronización de red**: Heiner Danit Rincon y Juan José Arias Gallego identificaron grabaciones repetidas con códigos distintos pero idénticas en contenido y verificadas mediante pruebas MD5. Domiciano Rincón instruyó eliminar todos los registros duplicados, explicando que estos se generan por reintentos de sincronización a la nube cuando falla la cobertura de internet en las zonas de recolección, y mantenerlos sesgaría los análisis estadísticos ([00:31:16](#00:31:16)) ([00:33:15](#00:33:15)).  
* **Consolidación del dataset y estrategia de recolección de controles**: Juan José Arias Gallego presentó el resumen del \*dataset\*: 63 pacientes (61 tras eliminar dos duplicados), 8 controles (7 tras depurar etiquetas) y 7 pruebas sin etiqueta debido a pruebas técnicas ([00:33:15](#00:33:15)). Ante el desbalance de datos, Domiciano Rincón propuso incorporar una tarea en el cronograma para recolectar al menos 15 a 20 sujetos de control adicionales mediante pruebas con estudiantes, profesores o investigadores ([00:34:18](#00:34:18)) ([00:37:28](#00:37:28)). Destacó que esto es viable sin requerir aprobación del comité de ética de la Valle del Lili ni pareamiento estricto por edad o altura, ya que la meta del estudio es la explicabilidad biomecánica de la enfermedad de Parkinson frente a patrones normales ([00:35:25](#00:35:25)).  
* **Análisis de variables biomecánicas según la literatura de Molero Mateo**: Juan José Arias Gallego expuso el análisis del estudio de Molero Mateo, el cual evalúa marcadores biomecánicos en la escala Hoehn and Yahr (estadios 1, 1.5 y 2\) frente a controles utilizando captura optoelectrónica Vicon y sensores IMU ([00:41:00](#00:41:00)) ([00:48:23](#00:48:23)). Se destacó que la prueba de Molero Mateo divide el movimiento en seis fases, mientras que el diseño experimental del grupo combina las dos últimas etapas ([00:42:31](#00:42:31)). Los hallazgos revelaron que las variables temporales simples no diferencian bien entre controles y estadios tempranos, siendo la fase de giro la más sensible y diciente para la clasificación ([00:43:36](#00:43:36)) ([00:51:19](#00:51:19)). Además, se resaltó que la asimetría de codo y el rango de movimiento (ROM) muestran alteraciones en estadio 2, mientras que la variabilidad de la marcha no resultó estadísticamente significativa ([00:52:42](#00:52:42)).  
* **Consideraciones sobre sistemas Gold Standard y repetibilidad intersujeto**: Domiciano Rincón explicó que los sistemas como Vicon representan el \*Gold Standard\* de alta precisión utilizado en laboratorios especializados, pero el objetivo de la investigación es ofrecer una alternativa ambulatoria y económica basada en sensores IMU y cámaras de profundidad ([00:48:23](#00:48:23)) ([00:52:42](#00:52:42)). Respecto al coeficiente de correlación intraclass (ICC), Domiciano Rincón señaló que las variables biológicas presentan alta variabilidad intersujeto, por lo que en el análisis se tratarán las múltiples tomas de un mismo paciente como datos independientes o promediados para mitigar diferencias individuales ([00:53:39](#00:53:39)).  
* **Formulación formal del cuarto objetivo específico y siguientes pasos**: Domiciano Rincón redactó el enunciado para el cuarto objetivo específico del proyecto: "Validar el desempeño del algoritmo de clasificación mediante esquemas de validación a nivel de los grupos de pacientes, verificando la capacidad de discriminación a través de las métricas de exactitud, sensibilidad, F1-score y matriz de confusión" ([00:45:59](#00:45:59)). Para la siguiente fase, Juan José Arias Gallego y el equipo continuarán filtrando las 25 referencias bibliográficas en la plantilla estructurada, y intentarán ejecutar el algoritmo de segmentación previo sobre los datos actuales para aislar las fases del movimiento y extraer las primeras variables temporales ([00:56:44](#00:56:44)).  
* **Aplicación del algoritmo de segmentación**: Domiciano Rincón propuso como tarea intentar aplicar directamente el algoritmo de segmentación en el plazo de una semana ([00:58:59](#00:58:59)).  
* **Tratamiento y relevancia de los datos de doble tarea ("double task")**: Esteban Guarin Valencia preguntó sobre el manejo de los datos de doble tarea. Domiciano Rincón explicó que estas muestras forman parte del grupo de pacientes e indicó que si son pocas muestras (menos de 30), carecen de relevancia estadística para el alcance de su análisis, por lo que pueden seguir tratándose como muestras de pacientes ([00:58:59](#00:58:59)). Esteban Guarin Valencia aclaró que en los comentarios solo figuran aproximadamente tres muestras de este tipo, a lo que Domiciano Rincón respondió que, al ser solo tres, incluso se podrían descartar ([01:00:14](#01:00:14)).  
* **Justificación médica de las pruebas de doble tarea**: Domiciano Rincón detalló la razón detrás de estas pruebas, señalando que los médicos las solicitan cuando un paciente con Parkinson en etapa temprana no presenta alteraciones motoras visibles y actúa con normalidad. En tales casos, se les asigna una tarea cognitiva para exacerbar sus síntomas motores; por ende, es probable que la muestra sirva como muestra de paciente, ya que la doble tarea hace que manifiesten sus inconvenientes motores ([01:00:14](#01:00:14)).  
* **Avanzo metodológico y cronograma**: Domiciano Rincón concluyó que las dudas metodológicas quedaron resueltas, lo que permitirá al equipo avanzar en la elaboración del cronograma. Asimismo, elogió la planilla y el resumen que el equipo utiliza para las referencias más importantes, destacándolo como un método muy ordenado para probar variables de la literatura en el estudio ([01:01:17](#01:01:17)).  
* **Revisión de Sprinlift y Overlif**: Esteban Guarin Valencia mencionó que agregaron algunos elementos relacionados con "sprinlift" y "overlif", incluyendo fórmulas, y propuso que este aspecto se revise en una próxima reunión, lo cual fue aceptado por Domiciano Rincón ([01:01:17](#01:01:17)).  
* **Cierre de la reunión**: Juan José Arias Gallego, Esteban Guarin Valencia, Domiciano Rincón, Heiner Danit Rincon y Santiago Gomez Robledo expresaron sus agradecimientos y despedidas finales, dando por concluida la sesión ([01:01:17](#01:01:17)).

*Revisa las notas de Gemini para asegurarte de que sean precisas. [Obtén sugerencias y descubre cómo Gemini toma notas](https://support.google.com/meet/answer/14754931)*

*Cómo es la calidad de **estas notas específicas?** [Responde una breve encuesta](https://google.qualtrics.com/jfe/form/SV_5bXzKQfylMIhSXc?confid=QIUEcfhKcYodFF0c4VAUDxIXOBEQAjIGCIoCIAAYAQg&detailLevel=longer&hasImages=False&entryPoint=footerMain&isGoogler=False) para darnos tu opinión; por ejemplo, cuán útiles te resultaron las notas.*

oct 6, 2026

## **Reunión del 6 oct 2026 a las 08:54 GMT-05:00 \- Transcripción**

### **00:00:01**

**Esteban Guarin Valencia:** Listo.

**Santiago Gomez Robledo:** Bueno,

**Esteban Guarin Valencia:** Es como es que estaba buscando notas, es como para mostrar un indicador, como un porcentaje o digamos un porcentaje, un indicador para demostrar de que eso sea correcto, ya sea como que lo tomemos de una,

**Santiago Gomez Robledo:** que yo

**Esteban Guarin Valencia:** digamos, como referencia a otro paper o otras cosas.

**Domiciano Rincón:** No entiendo. O sea, lo que les piden es

**Esteban Guarin Valencia:** como un indicador, como un porcentaje, un número, un número para habilidad, digamos, para hablar así lo que estamos haciendo.

**Santiago Gomez Robledo:** Eh, lo que está diciendo Guarín es que por lo menos para cada objetivo específico es cómo lo vamos a comprobar, cómo vamos a identificar si eh se completó tal objetivo, entonces eh si va a ser un porcentaje, si al momento de validar Entonces, vamos a validar con otro estudio similar o con otra prueba similar o contra qué lo vamos a contrastar. Pues él ahí está hablando de los objetivos específicos, creo que es. Y pues a nivel de eso eh fue cuando Navarro nos estaba realizando los objetivos, que era también como lo que vos nos habías mencionado antes, profe, de bueno, según qué objetivo, pues que si se cumple este objetivo, ¿qué me está qué me está soltando?

### **00:01:37** {#00:01:37}

**Santiago Gomez Robledo:** Que eh por así decirlo,

**Domiciano Rincón:** entregable.

**Santiago Gomez Robledo:** ¿cómo?

**Domiciano Rincón:** ¿Qué entregable está? Eh,

**Santiago Gomez Robledo:** Sí,

**Domiciano Rincón:** digamos como que con qué entrega habla

**Santiago Gomez Robledo:** exactamente, exacto. entregable me está a mí eh verificando, dando esa verificación o dando ese esa salida del el cumplimiento del objetivo.

**Esteban Guarin Valencia:** Además eh Navarro nos comentó de que además de como teníamos los objetivos como de desarrollar el los de clasificación, faltaría como agregar el objetivo de valiar el el algoritmo de clasificación y convertir el objetivo de lo de integrarlo con Bimo a como una subtarea, una subtarea deada como a una de esos objetivos.

**Domiciano Rincón:** A a cuál a cuál lo podrían eh agregar, o sea, está bien. O sea, podemos poner de validación, pero pues ese tema de la de la integración tendría que poder e, o sea, lo que se puede hacer es esto, o sea, como que el objetivo de desarrollar los algoritmos y no sé qué, el predicado, o sea, la parte siguiente pues del objetivo puede ser integrándolos a la plataforma BIMAP.

### **00:02:57** {#00:02:57}

**Domiciano Rincón:** como una terminación así ya que implícito de que ustedes lo van a, o sea, luego de desarrollarlo lo van a integrar.

**Esteban Guarin Valencia:** Yo estaba pensando que como se está como se piensa añadir el objetivo de validar y dado que cuando se valida pues se supone que uno ya comprada de que ya esté más mejor hecho, ya esté digamos por decirlo así, pues esté ya como en su mejor estado. Ahí sí se podría poner de que se integra la plataforma Bimop, como ya está como validado de que funciona completamente bueno según los parámetros que le impusimos.

**Domiciano Rincón:** Lo que pasa es que validar es más como, o sea, validar es verificar que efectivamente el objetivo general se cumplió. El objetivo general en este momento, ¿cómo estás? Estamos un poquito a ciegas. ¿Por qué no ponemos los los objetivos?

**Esteban Guarin Valencia:** Listo. Ya. Pues lo único es que como todavía no le hemos corregido, pues todavía está como como estaban antes. Un momento. Me parece que es esta.

### **00:04:13** {#00:04:13}

**Domiciano Rincón:** A ver.

**Esteban Guarin Valencia:** Ahí ya.

**Domiciano Rincón:** Ajá.

**Esteban Guarin Valencia:** Ah, me parece que no me acuerdo que habíamos cambiado los objetivos como para combinarlos con lo que habías comentado en la reunión pasada con los que ya teníamos

**Domiciano Rincón:** ¿Y cuál es de mostrar?

**Esteban Guarin Valencia:** estos estos que estamos mostrando actualmente.

**Domiciano Rincón:** Pero esos eh esos tienen lo que hablamos la semana pasada.

**Esteban Guarin Valencia:** Sí, señor.

**Domiciano Rincón:** Listo. Entonces, e lo estoy leyendo. Sí, ¿no? O sea, la integración puede ir en el tercer objetivo perfectamente si le ponen al final coma integrando los con la plataforma mismo. Entonces el de validación de todo el estudio. Ahorita miramos el objetivo general. La validación tiene que ir marcada sobre el objetivo general. Es decir, o sea, yo no puedo eh poner como subarea, digamos, un despliegue eh en un objetivo de validación. Regularmente, por ejemplo, la validación para que lo lo tengamos, digamos, claro, es eh verificar los supuestos iniciales, por ejemplo, con la corte actual de datos. Eh, sí, se van a entender.

### **00:05:39** {#00:05:39}

**Domiciano Rincón:** Es decir, digamos como que la validación del algoritmo tendría que ser entonces después de sacar todas las vares biomecánicas y demás, eh, verificar, por ejemplo, las métricas de clasificación. dado que nosotros vamos a hacer un modelo de clasificación, entonces eso tiene asociadas unas métricas, pues las métricas tendría que eh ser eh digamos eh o sea, no nos podemos casar por un umbral porque descubrir que no que no son clasificables también es un resultado, pero sí al menos tendríamos que generar entonces esa validación basada pues en los en las métricas que tienen que ver pues con un clasificador común, ¿no? Entonces el cuarto objetivo lo uniría con el tercero pues según la indicación de ahorro, pero realmente solamente es eh coma integrando eh los integrando los algoritmos, pues más como que quedaría así, integrándolos a la plataforma BMA. Y el último, pues entonces pueden poner el el objetivo que les comentaba na barro de validación. ¿Puedes poner el objetivo general?

**Santiago Gomez Robledo:** De hecho, profe, creo que Navarro nos dijo algo muy similar a lo que nos acabas de mencionar,

**Domiciano Rincón:** El objetivo general lo podemos ver.

### **00:06:50**

**Esteban Guarin Valencia:** Sí, profe. Ya, ya, ya. Listo.

**Domiciano Rincón:** desarrollar de control cada fase apoyo al diagnóstico. Por ejemplo, también una validación puede ser eh el tema de de lo que pasa es que estamos digamos como lidiando con ese problema justamente en eh PDG2. Eh los doctores no son las personas más disponibles de la vida. Entonces, eh planear una reunión con ellos puede tomar mucho tiempo. Entonces, pero igual una validación puede ser también con el experto clínico. Por ejemplo, uno puede hacer muchas cosas, o sea, por ejemplo, uno puede hacer incluso un diseño experimental en donde uno puede hacer eh un contraste de pacientes y controles eh y verificar si efectivamente lo que digamos como que nuestro clasificador clasifica correctamente las cosas. Eh, seguramente ustedes se han se han visto en la tarea de hacer eso mismo con datos en en las materias que tienen que ver con analítica de inteligencia, ¿cierto? Que ustedes hacen un 70\. Los datos ya los tenemos y la idea es entonces verificar de forma aleatoria eh y eh con los con las mismas muestras que nosotros tenemos hacerlas hacer las validaciones de que efectivamente el clasificador está funcionando, ¿no?

### **00:08:11** {#00:08:11}

**Domiciano Rincón:** Entonces, digamos, como que ya de por si el trabajo ofrece valor con los indicadores numéricos que vamos a sacar, pero si esos indicadores eh se meten en un en un clasificador incluso de tipo estadístico, nosotros podemos entonces tener eh pues las métricas eh comunes de un algoritmo de clasificación como la y el recall, ¿sí? El DF1 score. Digamos como que hay varias de esas métricas. Entonces, probablemente el cuarto objetivo podría ser el tema de la validación. eh con el propio dataset e dentro de los estudios antecedentes, ¿ustedes qué han visto dentro de los resultados? Porque, por ejemplo, o sea, lo peor que podremos hacer aquí para el objetivo es poner al final, por ejemplo, nuestro objetivo es que nuestro clasificador de un porcentaje de más del 80% de precisión. Eso no lo podemos saber. Entonces, podríamos incluso dejar el objetivo eh como no cumplido si nosotros nos damos cuenta que a lo largo del estudio pues eh no no pudimos ser concluyentes o que el clasificador ofreció una precisión de 60% eh lo cual es super malo, pero entonces ahí uno ya se da cuenta pues de que efectivamente haber casado el algoritmo con el objetivo, perdón, con un número particular pues era era desde el principio un error.

### **00:09:25** {#00:09:25}

**Domiciano Rincón:** Entonces, el objetivo está debería estar más orientado como hacia el método de validación antes que al objetivo de de esa validación, el el o digamos como acaba con los números que nos va a ofrecer la validación. No sé si me hago entender. Entonces, por ejemplo, mi metodología de validación, yo podría yo, por ejemplo, eh, a ver, no sé exactamente qué les qué les dijo Navarro con el tema de los estudios antecedentes, pero una validación puede ser simplemente medir las métricas de el clasificador ya una vez esté finalizado, o sea, evaluar las métricas eh para verificar el eh desempeño del clasificador acorde a el las métricas extraídas. Eso, eso que les digo ustedes lo sacab cierto. Rec F1 score

**Juan José Arias Gallego:** Hola, profe.

**Esteban Guarin Valencia:** Pues no sé si ah pues

**Juan José Arias Gallego:** poras.

**Esteban Guarin Valencia:** por la parte, o sea, de lo que dijiste, profe, pues no sé si eso se ven en la analítica porque pues yo actualmente no he visto analítica de datos, entonces no sabía decirte

**Domiciano Rincón:** eh tiene que ver con los falsos positivos y los falsos negativos, sí, hay una matriz eh matriz de confusión, sí que pues entonces uno verifica,

### **00:10:47** {#00:10:47}

**Esteban Guarin Valencia:** Listo.

**Domiciano Rincón:** bueno, digamos como que ustedes pueden, ¿no? Mario, eso es un tema de de clasificadores, no estoy seguro si alguien del equipo lo sabe. Heiner de pronto si lo sabe, ¿no?

**Esteban Guarin Valencia:** No está acá actualmente.

**Domiciano Rincón:** Heiner con total con total seguridad lo conoce, pero sí, entonces uno saca ciertas métricas, ¿no? Entonces uno saca pues primero la cura como la sera como la exactitud, también hay un elemento de precisión, también hay un elemento como de recall que mide como la sensibilidad e y eh pues sí, digamos como que hay una métrica llamada F1 Score que también digamos como que ofrece métricas que o sea ofrece un número pues que me permite saber de alguna u otra manera pues el desempeño eh del clasificador ante pues el desbalanceo, pero digamos como que lo que espero ver dentro del dentro del la exploración de los datos es verificar, por ejemplo, las proporciones. Eh, tenemos que identificar varias cosas, como por ejemplo, tendríamos ya que poder identificar eh qué muestras no vamos a incluir en el estudio. Entonces, por ejemplo, qué muestras no cuando el sensor se desconectó, cuando algo sucedió durante la prueba y demás.

### **00:11:59** {#00:11:59}

**Domiciano Rincón:** Yo esperaría que sean unas muestras más pequeñas, ¿sí? Entonces, esas claramente no tendrían que ir dentro del estudio. Lo siguiente es eh pues verificar el balanceo de control versus pacientes. O sea, tendríamos que saber eh de todas las muestras que tenemos, pues cuáles son pacientes y cuáles son controles. Mm. y y creo que ya, o sea, es básicamente como la exploración que tendríamos que hacer, no solamente eso, sino que adicionalmente implementarle a esas muestras el mismo algoritmo de segmentación que se tenía de antes, pues de su de sus compañeros antecesores eh para verificar si efectivamente podemos seguir haciendo la segmentación, porque eh digamos como que ese objetivo que dice como validar también entre otras está implícito que si con los nuevos dispositivos no llegó a ser digamos como lo suficientemente concluyente, entonces pues tendríamos que ajustar el algoritmo para para hacer esa segmentación. H dentro de esos datos, muchachos, ustedes pudieron eh saber cuántos controles, cuántos pacientes, cuántas muestras malas tenemos.

**Juan José Arias Gallego:** Eh, sí, profe, nosotros trabajamos en un en un script que de Python que más o menos cogía principalmente los datos de los sensores de los inus porque los del los de las cámaras aún no los hemos revisado Y

### **00:13:24** {#00:13:24}

**Domiciano Rincón:** Exacto. O sea, las cámaras podría podría esperar un ratico más. O sea, yo sé que Imus podría ser más pues digamos como dispendioso, así que pues nada, lo que necesitemos pues de tiempo.

**Juan José Arias Gallego:** eh sí, entonces nosotros con el SCP generamos un SSV en el cual se lista porque al principio era un poquito confuso, ya que las grabaciones eh pues no especificaban de por sí la persona. Entonces, lo que se hizo fue que por medio de datos como la fecha de nacimiento y digamos otros otros marcadores que tenían la la prueba o la grabación eh se fue asociando a una

**Domiciano Rincón:** Claro, lo que pasa es que esos datos salen anonimizados de la plataforma, o sea, no se pueden disponer de los datos pues digamos con cédula real, pero pues me parece que la estrategia de fecha de nacimiento podría funcionar. Eh, tener en cuenta igual digamos como que pues es bastante probable después de como 30 personas que dos personas tengan la misma fecha de nacimiento, ¿no?

**Juan José Arias Gallego:** Ajá. No, también hay otros, o sea, otros marcadores asociados ahí que son que aparte de que coincida la fecha de nacimiento, también la altura y creo que ha hay otros,

### **00:14:41** {#00:14:41}

**Domiciano Rincón:** Okay, okay, okay.

**Juan José Arias Gallego:** o sea, para hacer un poquito más de validaciones y que efectivamente el la grabación

**Domiciano Rincón:** Me parece chévere. Me parece chévere lo que hicieron.

**Juan José Arias Gallego:** se deba se coincida con una sola persona y pues se le di un identificador como persona uno, persona dos,

**Domiciano Rincón:** Y tenemos los datos de cuántos pacientes y cuántos controles.

**Juan José Arias Gallego:** Eh eh sí,

**Domiciano Rincón:** El balanceo de las clave

**Juan José Arias Gallego:** ahorita mismo no tengo bien el otro, pero ya ya vamos a mostrar el pues el script y que lo que arrojó.

**Domiciano Rincón:** y muestras malas. También tenemos conteo en el script.

**Juan José Arias Gallego:** Creo que sí hay muestras incompletas, o sea, por ejemplo,

**Domiciano Rincón:** Eso,

**Juan José Arias Gallego:** sin un sensor de de mano izquierda,

**Domiciano Rincón:** eso, eso.

**Juan José Arias Gallego:** creo que es. Entonces sí ahí está todo el conteo y pues aparte de eso también hemos hecho análisis en en algunos en algunas referencias de los antecedentes para sacar variables espaciotemporales. Navarro nos dijo que que revisáramos las referencias, especialmente las de Molero Mateo.

### **00:15:45**

**Domiciano Rincón:** Perdón, perdón.

**Juan José Arias Gallego:** tenía eh hasta qué punto,

**Domiciano Rincón:** Lo pued lo puedes repetir, ¿no? No entendí.

**Juan José Arias Gallego:** ¿sabes?

**Domiciano Rincón:** Eh,

**Juan José Arias Gallego:** este a que revisáramos especialmente

**Domiciano Rincón:** eso último que Navarro les dijo que qué

**Juan José Arias Gallego:** las referencias de Molero Mateo, los o los estudios que había hecho, porque él tiene pues varios varios estudios referentes a al time go y hay uno

**Domiciano Rincón:** interesante. interesante.

**Juan José Arias Gallego:** específicamente que en el que encontramos pues algunos biomarcadores temporales y espaciotemporales.

**Domiciano Rincón:** Okay, okay, okay. Respecto al tema de la de la, ¿cómo decir? Eh, ahí está abriendo el overlift. Eh, entonces también les dijeron que metodología, que hacía falta la metodología, me dijeron.

**Juan José Arias Gallego:** Eh, sí, profe, también nos dijeron, o sea, que metodología y pues cronograma, ese sí lo podemos realizar nosotros.

**Domiciano Rincón:** acá. Hm. Entonces, les voy a comentar como el tema de metodologías que regularmente nosotros manejamos dentro de este tipo de proyectos. e cuando es un proyecto meramente de desarrollo, entonces uno pues utiliza metodologías iterativas, no hablamos de Scrom, digamos como que el número de participantes de pronto pues no es suficiente.

### **00:17:04** {#00:17:04}

**Domiciano Rincón:** Entonces hablamos como metodología iterativa incremental, pues entonces uno genera incrementos, entonces los incrementos pueden ir con spray y demás, pero cuando tiene que ver con ese tipo de elementos, eh no podemos perder de vista que el objetivo final pues es justamente integrarlo a Bimob, es decir, que algo de desarrollo tiene. Sin embargo, el desarrollo para poder ser el desarrollo, digamos, como que primero tiene que haber desarrollados pues justamente los métodos algorítmicos. Entonces ahí eh o sea, regularmente digamos como que uno puedo utilizar una metodología mixta en donde vamos a comenzar con Cris DM. Eh, no sé si las mencionaron, pero es un elemento pues que nos permite a nosotros entender los datos. Es un bucle, lo pueden buscar allí. A ver, voy a buscar allí rápidamente un grafiquito para mostrarles, porque es un ciclo. Entonces, ese ciclo es muy el ciclo que nosotros estamos siguiendo. Lo que pasa es que pues como de una forma muy eh a ver, lo voy a pegar aquí en el grupo de WhatsApp que lo tengamos por allí. Entonces, si ustedes se dan cuenta, eso es un bucle que pues cuyos centros son los datos, ¿no?

### **00:18:10**

**Domiciano Rincón:** Entonces, como que lo primero es el business understanding, entonces ahí lo que ustedes van a verificar es justo lo que están haciendo. O sea, desde el principio, digamos como que todos los grupos intento pues que se metan en el problema a través de la lectura mínimamente pues de abstract de estudios antecedentes, que se den como una contextualización a nivel literario pues de de qué es lo que se está buscando pues en el proyecto y demás. Así que creo que ya todos tenemos el business understanding bien, digámoslo así. Eh, luego el data understanding. Entonces, aquí nos va a tocar que hacer, digamos, como dos pasos, uno pues con el tema de IMOs y el otro pues con el tema de cámara. Luego entonces del data understanding viene como la data preparation, ¿sí? Estamos viendo el grafito, ¿cierto? Entonces el el el está en el WhatsApp. Entonces, el data preparation es justamente lo que estamos eh haciendo, es decir, verificando pues lo que les decía, o sea, que los identificar las muestras malas o incompletas, o sea, muestras que nosotros no vamos a incluir en el estudio, verificar el tema de cómo es el balanceo, cuántos controles y cuántos pacientes tenemos.

### **00:19:12**

**Domiciano Rincón:** El de el de dual task podemos incluso tener en cuenta pues como un como una clase aparte, pero también digamos como que para estudios generales pues podemos hacer que esa muestra simplemente sea de paciente y ya. Eh, si tenemos claro, pues digamos si dentro del Jon aparece lo del tema del dual task, pues bueno, o sea, podemos tagarla de una forma especial, pero igual hace parte del grupo de de pacientes, ¿no? El grupo de control. Luego entonces viene el tema de modelamiento. Entonces en el modelamiento ahí es en donde pues digamos como que nosotros desde el colab vamos entonces a verificar eh las variables espaciotemporales. Vamos entonces a tener una lista pues de variables espacio temporales en donde nosotros vamos a probar grado que cíclico. Nosotros podemos, por ejemplo, incluir unas primeras cuatro, unas primeras cinco, o sea, nos podemos enfocar en categorías de variables y en estas categorías de variables, pues entonces nosotros podemos llegar y decir, bueno, el imuno nos puede sacar, por ejemplo, por decir un algo particular, pues la zancada o el doble soporte. Entonces nosotros podemos, digamos, como hacer dentro de la dentro del bloque de modelamiento podemos hacer el tema de de incluir pues las variables espaciotemporales y programar en en el script pues eh la extracción de eso a partir de las señales de IMOS.

### **00:20:24** {#00:20:24}

**Domiciano Rincón:** Luego pasa a evaluación. Entonces, en evaluación, nosotros podemos verificar, entre otras, de qué manera nosotros eh hacemos, o sea, si los datos efectivamente sí son eh consecuentes con lo que observa la muestra, por decirlo de alguna manera, eh entiendo yo que las muestras se tomaron al mismo tiempo. Prende. Dado que ustedes ahorita tienen un acceso a la plataforma, ustedes pueden buscar eh digamos como la la la la la la muestra pues con la fecha en la que con la fecha y hora pues que se extrajo la muestra y la plataforma les va a mostrar un video, ¿cierto? Entonces uno puede evaluarlo a nivel visual, uno puede evaluarlo a nivel de verificar si es consecuente pues la zancada con lo que se está viendo dentro de los dentro de los gráficos y luego se hace un deployment. Ese deployment no se trata como de no sé como de hacer el GIF action y entonces desplegar en cubernetes y no sé qué, no. ese deployment se trata de hacer que todo ese tema de datos que se ha venido eh digamos como desarrollando, pues finalmente haga parte del proyecto.

### **00:21:25**

**Domiciano Rincón:** Entonces, ese deployment es el que nosotros vamos a tomar como e elemento de integración a a BIMP. Sí, pero nuevamente fíjense que antes de deployment yo puedo hacer varios bucles por business understanding, data understanding, data preparation modeling y nuevamente evaluation. y luego evaluation me puede devolver y así tantas veces yo pues digamos como que me haga falta para poder entonces tener ese ese tema. Entonces este semestre muchachos pues estamos justamente en Cruise DM ya más adelante, por ejemplo, en la medida en la que nosotros vayamos teniendo resultados consecuentes, validados, probados, validados nuevamente de forma interna, o sea, nosotros podemos validarlo de forma interna dado que creo que la mayoría de las situaciones tenemos los los videos. Eh, pues el tema es empezar, digamos, como a hacer varios ciclos, varios bucles de este CRUDM y ya más adelante, entonces dentro de deployment uno puede efectivamente pues hacer las fases de de de metodología terapativa incremental, porque con esa metodología nosotros somos capaces entonces ahorita sí de planear eh cómo programar, o sea, primero entender BIMP, luego cómo programar las eh los métodos o los o los procesos que vamos nosotros a incluir dentro de las pruebas en Bimop y posteriormente hacer el despliegue en BIMOP.

### **00:22:41** {#00:22:41}

**Domiciano Rincón:** ¿Sí me hago entender? Entonces, eso de Bimop, esa es esa ese tema todavía no lo vamos a tocar, pero para su capítulo de metodología ustedes pueden decir que van a hacer entonces una metodología mixta donde pues van a combinar Cris DN nuevamente Cris DNCle que vemos entonces en y eso que que tome muy bien nota Yemini es business understanding, data understanding, data preparation modeling y evaluation. Vamos a hacer varios bucles de esos de esos cuatro bloques, de esos 1 2 3 cu de esos cinco bloques. Posteriormente cuando tengamos lo suficiente, entonces nos vamos a pasar a deployment, pero en sí deployment va a ser un un, ¿cómo decir? Como una fase en donde nosotros aplicaremos la metodología iterativa incremental. nuevamente para vamos a hacer algo muy similar y es los elementos que ya están probados, los elementos que nosotros vamos pudiendo extraer y demás, pues los vamos a ir eh poco a poco entregando o haciendo el delivery pues a la aplicación de BMOP y eso pues puede comenzar seguramente el siguiente semestre, o sea, este semestre va a ser como de eh entendiendo los datos, entendiendo las eh el negocio, los datos, eh hacer esto que es como que estamos haciendo con eh externar las variables espaciotemporales y luego Luego pues sí, hacer la evaluación interna.

### **00:23:56** {#00:23:56}

**Domiciano Rincón:** Es es clara.

**Heiner Danit Rincon:** Bueno,

**Domiciano Rincón:** Sí. Bien, supongo que sí. Asumo que sí. Bueno, aquí vamos a ver entonces los datos, ¿cierto?

**Heiner Danit Rincon:** Sí, profe. Profe, respecto a los datos, pues nosotros queremos como, a ver, nosotros estuvimos analizando los datos y pues nos dimos cuenta de que de

**Domiciano Rincón:** Eh

**Heiner Danit Rincon:** que de que son varias grabaciones que puede haber para una persona o simplemente puede haber una única grabación.

**Domiciano Rincón:** Ah.

**Heiner Danit Rincon:** Pues también teníamos como esa cuestión de por qué una persona puede tener varias grabaciones y pues hay unas que simplemente una una que una persona solo puede tener, digo, una persona solo tiene una grabación de, por ejemplo, el sensor de la mano izquierda, mientras que otra sí tiene todas las grabaciones completas. Entonces estábamos averiguando eso y teníamos esa cuestión.

**Domiciano Rincón:** Hm.

**Heiner Danit Rincon:** También hicimos como una categorización, como un agrupamiento, digo, de todas las grabaciones y lo hicimos con las variables demográficas de las personas, pues era como el único insumo que teníamos para poder encontrar un patrón y poder clasificar por personas las grabaciones.

### **00:25:32** {#00:25:32}

**Heiner Danit Rincon:** Entonces,

**Domiciano Rincón:** Sí, eso me comentó.

**Heiner Danit Rincon:** digamos que sí,

**Domiciano Rincón:** Quanto.

**Heiner Danit Rincon:** entonces digamos que eso lo realizamos y ya tenemos como, por ejemplo, las grabaciones organizadas por personas, pero pues sí tenemos como esa cuestión, esa pregunta de por qué una persona sí puede sí, o sea, hay personas que tienen varias grabaciones y hay personas que tienen una sola y también el código, el código también lo quisiéramos entender y pues más o menos ahí sí, porque es que por ejemplo el nombre de los archivos tiene un código que es como las últimas siglas, que es, por ejemplo, en el primer archivo podemos ver que es V, BV, el otro NO y así. Entonces,

**Domiciano Rincón:** Vale, vale. Eh, vamos como que a ver la la respuesta es la siguiente. Ese código es por una anonimización que se hacen de los datos. La plataforma sigue un estándar que se llama GH eh GHGIS 2, algo así. Eh, sí, algo como GH GIS 2\. Eh, tengo que verificar bien el el nombre de ese de ese estándar, pero sé que para cualquier hm, es decir, digamos como que por un tema de interventoría y demás, nosotros tenemos que guardar esos datos como privados.

### **00:26:42**

**Domiciano Rincón:** Entonces, nosotros ni siquiera sabemos pues las cédulas además a pesar de que las tomamos. Las cédulas las tomamos es porque en algún momento cualquier persona da los estudios puede llegar y llamar a la Fundación Vallaril y decir, "El estudio en el que participé, yo quiero que eliminen mis datos y lo tenemos que eliminar." O sea, eso se tiene como que garantizar. Entonces, e pues nada, digamos como que nuevamente a pesar de que tomamos el dato allí en campo, pues eh al final al tener los datos pues no vamos a poder eh observarlos, sí, tener, digamos, como las cédulas y demás nuevamente a pesar de que se a pesar de que se toma. Eh, entonces ese código tiene que, o sea, hace parte seguramente del tema de ese tema de anonimización. Entonces, eh me parece bien pues que ustedes hayan sacado el tema de de de cómo diferenciar a las personas basados en pues en los datos de fecha de nacimiento y lo otro era altura que era Sí, porque pues asumo que es bastante improbable pues que la persona mida lo mismo y que y que cumplan años en día.

### **00:27:42** {#00:27:42}

**Domiciano Rincón:** Así que pues bueno, o sea,

**Heiner Danit Rincon:** Sí.

**Domiciano Rincón:** digamos como que esa extracción asuma pues que está bien. Lo otro es que porque unas las personas tienen algunas grabaciones completas y algunas otras no. e digamos como que esta estas tomas son tomadas en campo y regularmente pues las tomas es como, a ver, digamos como que eso eso es un montón de gente el día de la de las de las brigadas y pues eh en algún punto hay pruebas que solamente toman una grabación. Si la persona que está detrás de hacer las pruebas se equivoca y tomó, por ejemplo, no sé, otra que no es la de Tabet Go, sino otra prueba particular, por ejemplo, hay una que solamente es un tema de postura, entonces solamente tiene el spine base. Entonces, eh pues las otras básicamente no se toman. Sí. Entonces, eh y otra otra razón es que lanzó la prueba, pero sin toda la sin todos los sensores. Nosotros para el estudio, digamos, solamente realmente necesitamos eh tres sensores de movimiento, que es el spine base y las dos articulaciones de de de tobillo.

### **00:28:51** {#00:28:51}

**Domiciano Rincón:** ¿Sí? Es decir, que nuestra muestra es válida si tiene mínimo esas tres, no necesariamente las cinco, porque yo sé que pues hay pacientes que tienen las cinco, ¿sí o no? O sea, como brazos, piernas y spine baits. Entonces, mínimo mínimo necesitamos esas tres, o sea, las dos ankles y el spine base. ¿Vale? Eh, el algoritmo de segmentación, si lo revisaron, él solamente requiere el spine base, o sea, que nosotros incluso también podríamos medir las mismas variables que se medían en el estudio anterior, es decir, eh la diferencia de fes únicamente con el spine base. Entonces esa podría ser, digamos, como una un dato e es decir,

**Heiner Danit Rincon:** Oh.

**Domiciano Rincón:** digamos como que no no a todos segur seguramente no todos los pacientes vamos a poder sacar los mismos elementos, pero si nosotros peluqueamos el dataset y solamente ponemos como pruebas válidas las que tienen esas mínimamente digamos esas tres muestras, está bien. Entonces esa es la razón.

**Heiner Danit Rincon:** Ah, okay, profe.

**Domiciano Rincón:** O sea, que entonces nosotros podemos chublear que la muestra quedó bien o que la persona quedó bien muestra si eh pues sus pruebas no están incompletas eh porque un sensor se haya apagado y además eh que los datos en tobillos y spine base estén presentes.

### **00:30:06**

**Domiciano Rincón:** Y están el tema de los arms, los atrazos, pues ese podría ser interesante, digamos como que hay estudios sobre arm swinging, pero la verdad es que no es pues muy pues como mucho más diciente para esta prueba particular

**Heiner Danit Rincon:** Okay, profe. Okay.

**Domiciano Rincón:** porque sí.

**Juan José Arias Gallego:** Eh,

**Domiciano Rincón:** Eh, a ver,

**Juan José Arias Gallego:** E A

**Domiciano Rincón:** a a mí tengo que hacer en el pasado el estudio de de Arm Swinging y, por ejemplo, sacar giro con arm swwinging es imposible. O sea, verdad, lo intentamos de todas las maneras, de todos los medios, pero es como estar a ciegas e únicamente teniendo en cuenta los brazos. Los brazos sí efectivamente pues nos dan elementos adicionales como por ejemplo temblor, temblor esencial, temblor perquinsoniano, si nos puede dar el swing. Lo otro también es la asimetría, pero asimetría es algo que no medimos en esta prueba, sino en la prueba de marcho, no es la de ta

**Heiner Danit Rincon:** pregunta es que bueno,

**Domiciano Rincón:** Mhm.

**Heiner Danit Rincon:** en el en los datos también teníamos como una cuestión que son problemas en consistencias que habíamos detectado.

### **00:31:16** {#00:31:16}

**Heiner Danit Rincon:** Sí. Y habíamos visto de que, por ejemplo, cuando estábamos haciendo el análisis se habían encontrado un duplicado y una y una grabación repetida. Eso lo eliminamos o lo dejamos tal cual como está. Aunque bueno, tiene diferente código y la única diferencia es un segundo de tiempo. serían prácticamente casi los mismos datos,

**Juan José Arias Gallego:** Vamos.

**Heiner Danit Rincon:** pero pues usted opina que daría variabilidad al digamos al a la grabación No.

**Domiciano Rincón:** Eh, es ahí la tenemos que descartar. También hay un tema. A ver, si, no, o sea, digamos como que ustedes están seguramente viendo como como seas manes porque hicieron esto, pero la verdad es que sucede que dentro de campo pasa lo siguiente. Eh, las zonas las zonas digamos como las que se va son zonas que no tienen pues digamos como una cobertura adecuada de internet, ¿no? No podemos decir que están desconectadas, pero pues como que su cobertura puede fallar. Entonces, el los sistemas están hechos para que haya,

**Heiner Danit Rincon:** Ok.

**Domiciano Rincón:** pues digamos superposición en en todo tipo, ¿sí?

### **00:32:16**

**Domiciano Rincón:** O sea, por ejemplo, eh nosotros guardamos los datos dentro de los dispositivos como datos locales y los intentamos lanzar. Sí, pero puede ser que nos los lance a la nube y que eh alcancen a llegar al servidor y demás, pero que cuando, o sea, pero que no alcanzamos a obtener la seca o un error de conexión, de modo entonces que la persona eh digamos como que va a quedar como si no estuviera sincronizada. Entonces, cuando tenemos otra vez las condiciones de internet, vuelve a sincronizar la muestra y entonces queda duplicada en el sistema. Pero incluso si ustedes le sacan un MD5 o un SH1,

**Heiner Danit Rincon:** Sí.

**Juan José Arias Gallego:** Ok.

**Domiciano Rincón:** ustedes se van a dar cuenta que es la misma muestra y debe, o sea, la pregunta es, ¿tendríamos que que dejarla o eliminarla? Tendríamos que eliminarla dado que es una muestra duplicada. Entonces, eh pues si yo duplico, por ejemplo, si yo tengo un dataset de 100 y tengo en el peor de los casos, por ejemplo, 100 duplicados de una de las 100 muestras, pues entonces voy a tener, pues, digamos, como un grupo bastante representativo e igual, eh, y eso afecta pues estadísticamente la la muestra.

### **00:33:15** {#00:33:15}

**Heiner Danit Rincon:** Okay.

**Domiciano Rincón:** Entonces, si eso se debe, digamos, a la superposición, o sea, como que preferimos que se nos duplique el dato, que se elimine eh en condiciones desentendidas de internet es algo usual, digámoslo.

**Juan José Arias Gallego:** Eh, bueno, profe, entonces nosotros también sacamos como un archivo resumen. Entonces, aquí también dice lo que estamos nombrando,

**Domiciano Rincón:** Mhm. Yeah.

**Juan José Arias Gallego:** que la agrupación por personas es por be date, sex, hate, pa. Incluso hay una validación porque a veces estas tres coinciden, pero creo que hay unas fechas mal escritas y puede que sea la misma persona,

**Heiner Danit Rincon:** M.

**Juan José Arias Gallego:** o sea, que para dos grabaciones de la misma persona hayan dos fechas diferentes

**Domiciano Rincón:** Ok.

**Juan José Arias Gallego:** de nacimiento.

**Domiciano Rincón:** M.

**Juan José Arias Gallego:** Entonces, puede haber sido también un error. y encontramos que, por ejemplo, estos duplicados exactos en estas grabaciones, lo que decía Heiner que

**Domiciano Rincón:** Ah, sí, literalmente sacaron prueba MD5 también acá. Okay.

**Juan José Arias Gallego:** Ajá.

### **00:34:18** {#00:34:18}

**Juan José Arias Gallego:** Eh, ¿qué es lo otro? Aquí está el resumen de los de los del número de pacientes, eh, que nos da un total de de 63 y pues quitándole los dos duplicados da 61 y de controles eh ocho y ahí sin etiquetas siete que pueden deberse a pruebas técnicas.

**Domiciano Rincón:** Okay. Dentro de los dentro de los 63\. A ver, tengo que verificar. Listo. Sí, yo creo que en algún punto nosotros debemos parear eh los controles con los pacientes y entonces el objetivo de validación creo que podría tener más sentido sobre ese tema. O sea, hay una buena noticia entre otras y es que los controles, a pesar de que digamos como que sí son poquitos dentro del estudio, son los más fáciles de conseguir,

**Juan José Arias Gallego:** L

**Domiciano Rincón:** o sea, son los más fáciles de evaluar. Nosotros podemos hacer pues simplemente sacar un día de PDG1 o PDG2 para tomar una muestras de diferentes personas con las mismas, o sea, con el mismo diseño experimental con el que se sacaron las pruebas.

### **00:35:25** {#00:35:25}

**Domiciano Rincón:** Eso es algo sencillo porque pues eso ya está documentado y demás, ¿cierto? Y eh pues nada, digamos, como que yo le pediré pues ayuda también a las personas del grupo de investigación, sobre todo a las que estuvieron en la brigada pasada, para que hagamos exactamente el mismo pues el mismo levantamiento de datos. Eh, si tenemos unos unas 15 personas adicionales, digamos, como que lo podríamos validar, me hago entender. Es decir, digamos, como que las variables espaciotemporales de pacientes están allí, pero eh digamos que con ocho controles probablemente pues sí nos quede bastante desbalanceado para un clasificador. Entonces,

**Juan José Arias Gallego:** Ok.

**Domiciano Rincón:** pues nada, en algún momento seguramente nos va a tocar que poner como un, o sea, como tarea para hacer eh un levantamiento de datos de controles, pero eso es más fácil. O sea, pacientes, pacientes es bastante difícil porque pues la persona tiene que estar diagnosticada y que además tiene que tener como un eh Sí. Es decir, digamos como que el el protocolo de medición tiene que pasar por algo que se llama un comité de ética.

### **00:36:24**

**Domiciano Rincón:** El comité de ética es el comité de ética de Valle de Lili. Eh, eso en general es muy burocrático y al final digamos como que puede h entorpecer digamos como la muestra. Mientras que si dado que son controles los que nos faltan, entonces pues eso lo podemos hacer seguramente eh, ¿sí, no? O sea, lo podemos dividir en en algunos días teniendo los sensores, teniendo los dispositivos, eh no debería haber tanto problema. O sea, podemos evaluar no a personas del estudio ni nada, pero sí, por ejemplo, a personas sí, ¿no? Incluso ni siquiera tienen que estar parejadas por edad. Sí. Sí, sí, me hago entender. Es decir, la prueba de control al final digamos como que nosotros estamos verificando pues cuáles son las afectaciones respecto a tener Parkinson versus a no tenerlo. Entonces, un robot eh podría también seguramente dar la prueba específica a una persona realmente sin importar la edad, porque lo que nosotros estamos mirando es pues como signos de diferencia respecto pues alguien que puede desempeñar la prueba normal independientemente de la edad.

**Juan José Arias Gallego:** Okay, prof.

### **00:37:28** {#00:37:28}

**Domiciano Rincón:** Así que sí,

**Juan José Arias Gallego:** y

**Domiciano Rincón:** esa esa es esa tarea tiene que estar en algún momento en algún punto en el cronograma. O sea, yo digo no igualar los 63 porque sería superclicado, pues yo creo que levantar 20 personas perfectamente se puede hacer. Eso tomará un tiempo, pero creo que eh pues nada, o sea, nuevamente teniendo los sensores uno puede eh hacerlo incluso pues con participantes, eh estudiantes, profesores, doctores, investigadores, etcétera.

**Juan José Arias Gallego:** Y profe, por ejemplo, he visto en algunas de las referencias que también han hecho la prueba de Tug instrumental que parean los pacientes con controles, pero también como que debería coincidir, por ejemplo, la edad, eh, o parámetros como la altura.

**Domiciano Rincón:** los paredan por por grupo de tarea. Sí, sí. digamos como que allí nosotros tenemos, o sea, digamos como que nosotros no lo podemos hacer dado que dentro de pues dentro de los pacientes que nos llegan, pues nosotros realmente no podemos controlar el tema de, por ejemplo, altura o peso o edad. O sea, digamos como que nosotros tenemos pacientes entre los 40 y 70 años en es en esos estudios, eh, o sea, pacientes diagnos diagnosticadas personas así incluso jóvenes, pues 40 45 años.

### **00:38:56**

**Domiciano Rincón:** Entonces, pues nada, digamos como que regularmente ante la ante los pocos datos, regularmente nosotros no lo paramos por el dato, ¿sí? Pero si el estudio digamos como que es concluyente la medida en la que nosotros podemos llegar y decir, por ejemplo, e a ver eh nosotros tenemos entonces este signo que tienen los pacientes, que es por ejemplo, no sé, como que las ancadas menor o que son más lentos o demás. Eso es perfectamente concluyente porque pues al final digamos como que hacen parte de grupos diferentes, o sea, un grupo que se levanta, gira y camina con normalidad versus uno que no. Entonces nosotros estamos más, es decir, digamos como que si fuera un estudio meramente de clasificación, claramente nosotros tendríamos que hacer eso, dado que pues en el clasificador es es ciego, o sea, digamos como que no no intenta tener explicabilidad, el objetivo es clasificar y listo. Mientras que este tipo de estudios lo que busca es explicabilidad, es decir, listo, vio diferente, hace parte del grupo de pacientes, pero ¿por qué? O sea, ¿qué indicador, qué elemento dentro de nuestros clasificadores hace que tengan esa diferencia?

### **00:40:01**

**Domiciano Rincón:** Ah, es que la diferencia es en la zancada, que la que los pacientes tienen menos ancada y los controles más ancada. ¿Listo? Entonces eso es concluyente porque pues entonces yo puedo decir eh o explicable al menos porque yo puedo llegar y decir pues sí, digamos como que los los pacientes en general pues tienen menor zancada que los controles y pues aquí presentamos las diferencias significativas. Ah, es que el control, el paciente era muy alto estadísticamente, digamos como que no todos, no todas las personas pues van a ser altas, sino que se van también a a tornar en una en una media. Entonces, eh seguramente si la persona tiene parking y tiene una zancada muy alta, pues la explicabilidad se ve porque sea una persona muy alta, pero va a ser un outlier, no va no va a ser parte, digamos, como de del grupo normal, ¿sí? O sea, estadísticamente es es concluyente. Entonces, regularmente por eso no lo hacemos. O sea, tenemos tan pocos datos que pues tener, digamos, como, no sé, 100 datos de personas exactamente paradas en el mismo grupo etario con otro grupo de control, pues eso se hace complicado.

### **00:41:00** {#00:41:00}

**Domiciano Rincón:** Entonces, ustedes ven que dentro del grupo de pacientes, pues probablemente pues hayan eh pues sí, digamos, como de todas las edades, tamaños y tipos.

**Juan José Arias Gallego:** profe. E y pues básicamente también hicimos una pequeña investigación de variables espaciotemporales

**Domiciano Rincón:** Aha.

**Juan José Arias Gallego:** y pues tenemos con el compañero Robledo el también reunidó alrededor de 15 variables espaciotemporales y estamos intentando como manejar una plantilla para cada referencia. Entonces, por ejemplo,

**Domiciano Rincón:** Bacanísimo.

**Juan José Arias Gallego:** con esta con esta que es de Molerom Mateo, que es instrumento de básicamente esta se encarga estudio se encarga como de encontrar marcadores biomecánicos para poder realizar una diferenciación entre pacientes dentro de la escala de joven iningar. Eh, creo que es 1 1.5 y hasta dos y eh controles.

**Domiciano Rincón:** Yeah. Eh,

**Juan José Arias Gallego:** Entonces, pues aquí están los datos de la muestra. se utilizaron tantos pacientes sanos, tantos pacientes en esta estadía, en este estadio y el total de pacientes con con enfermedad de parqu

**Domiciano Rincón:** okay, okay, okay,

### **00:42:31** {#00:42:31}

**Juan José Arias Gallego:** se se nombra también el estado de medicación y las variables. Para la segmentación es esta que es en seis fases.

**Domiciano Rincón:** nice, aí Sabemos que tenemos una diferencia respecto a nuestro a nuestro diseño experimental, ¿no? O sea, las últimas dos fases están combinadas en nuestro estudio, pero está bien, o sea, no pasa nada. Realmente, digamos, como que si ya lo tenemos así, todo el diseño está experimental está así, pues nada, tenemos que saber lidiar con eso. Igual tenemos un giro puro, o sea, un giro de pie, así que pues que el último giro sea giro más sentado, ¿no? Realmente no pasa nada.

**Juan José Arias Gallego:** Sí, sí. Aquí sí realizan algo un poquito diferente, es hacer más pasos. Eh, y aquí está como una tablita de variables temporales por FAS que extrayeron en ese estudio. Entonces, está la variable original, digamos, el nombre en español porque pues el estudio está escrito en inglés, el descriptor, eh, la fase, la que se extrae la variable, la unidad y el resultado relevante que hallaron.

### **00:43:36** {#00:43:36}

**Juan José Arias Gallego:** Oke.

**Domiciano Rincón:** O sea, está está muy bien, o sea, eso esto formato me gusta bastante. Está bien bacano.

**Juan José Arias Gallego:** Mm. Eh,

**Domiciano Rincón:** Miren que de hecho eso es como eh data understanding, es decir, digamos como que dentro de lo que les mostraba de Cris DM, pues eso es lo que nosotros vamos a hacer. Es decir, creo que lo que podemos hacer son iteraciones de hacer esto, intentarlo eh digamos buscar en los datos, pues aplicar esto mismo, pero en los datos y verificar que no sale a nosotros.

**Juan José Arias Gallego:** sí. Y pues, o sea, incluso también nos ayuda mucho a poder extraer lo más importante de cada referencia, porque pues, por ejemplo, en este estudio se nombran todas estas variables temporales, pero muy pocas son estadísticamente dicientes. Entonces, al final eh se nombra que, por ejemplo, estas variables temporales en IP temprano las diferencias son sutiles y se expresan principalmente durante el giro. Eh, o sea, lo que básicamente entendimos de esta de este estudio en estas variables temporales es que es muy difícil hacer un clasificador o diferenciar pacientes y controles eh solo con con una variable temporal.

### **00:44:56**

**Juan José Arias Gallego:** la más diciente es el giro.

**Domiciano Rincón:** Mhm.

**Juan José Arias Gallego:** Y pues ellos en vez de anova eh utilizan chapiro porque pues los datos creo que no manejan distur

**Domiciano Rincón:** Sí. E ah, qué chévere, qué chévere. Sí, claro. O sea, digamos como que ahí, por ejemplo, están todos los todos los estadísticos que nosotros sacamos allí. A ver, o sea, yo sé que mejor dicho, o sea, eh dentro del equipo sé que Heiner todavía está, sí. Eh, dentro del equipo. Hm. Pues digamos como que tenemos pues digamos como varios skills, pero pues por ejemplo una es seguramente todos vieron este tema de estadística descriptiva, ¿cómo se llama?

**Juan José Arias Gallego:** inferencia.

**Domiciano Rincón:** Eso,

**Juan José Arias Gallego:** diferencia

**Domiciano Rincón:** diferencia, digamos como que hay unas técnicas. Lo chévere de todo es que con las pruebas estadísticas nosotros tenemos, por ejemplo, podríamos verificar de todas las métricas diferencias significativas por medio de diferentes de diferentes estrategias. Chapiro Will es una, prueba Z es otra, TTU es otra. En algún momento si llegamos por ejemplo a tener variables categóricas, entonces sería unchi cuadrada.

### **00:45:59** {#00:45:59}

**Domiciano Rincón:** Bueno, digamos como que hay muchas pruebas estadísticas para poder verificar, por ejemplo, diferencias. ANOA, por ejemplo, es cuando uno quiere verificar diferencias, pero de dos de más de dos grupos, o sea, por ejemplo, tengo tres grupos, no sé, controles, pacientes y pacientes medicados. Y yo quiero verificar diferencias entre los tres grupos, entonces uno utiliza una nova. Entonces, si uno si uno tiene la diferencia significativa, significa que uno puede, por ejemplo, plantear gráficos en donde mi eje X sea una variable con diferencias significativas y el eje Y también. Y entonces, por ende, yo puedo analizar clusters, clústers de datos, o sea, nubes de datos separados. Y pues por definición, si yo tengo dos nubes de datos separadas, yo perfectamente puedo hacer un clasificador estadístico. Y pues el clasificador estadístico, pues al final digamos como que eh el resumen es yo puedo trazar una línea que diferencie los dos clústers y pues entonces tener un clasificador super bueno. Entonces al final digamos como que la el objetivo deación puede ser algo así, ¿no? Entonces, para mí, para mí el último objetivo y pues para ahí para que quede para Gemini, porque sé que ese objetivo ese quedó como ahí volando, para mí sería como validar el desempeño del algoritmo de clasificación.

### **00:47:08**

**Domiciano Rincón:** Ahora, ¿mié? mediante sí, eh digamos como mediante esquemas de validación, eh no no sé qué más de validación puede ser como a nivel de los grupos, o sea, a nivel de pacientes, eh verificando pues si efectivamente podemos discriminar con los datos de un clasificador, o sea, con las métricas del clasificador que les decía. Entonces, nuevamente está la exactitud, está la sensibilidad, está el F1 score. Eh, pues también se puede poner la matriz de confusión, o sea, como los falsos negativos y los falsos positivos, pero eso que acabo de decir Jemy podría ser el cuarto objetivo. Recuérdalo.

**Juan José Arias Gallego:** Listo.

**Domiciano Rincón:** Ahí seguramente cuando vean las notas, entonces va a quedar por ahí el resumen del cuarto objetivo. Pero sí, si si nosotros seguimos haciendo esto estaría super bien,

**Juan José Arias Gallego:** Sí.

**Domiciano Rincón:** porque entonces Nosotros al final podemos llegar y decir, "Listo, las métricas verifiquemos. Entonces, saquemos pruebas eh estadísticas y verificamos si hay diferencias entre los grupos o no.

**Juan José Arias Gallego:** Mm. Sí, incluso la plantilla de la tablita que ha mostrado para las temporales es exactamente la misma para las espaciotemporales y los resultados también en en temas de las pruebas estadísticas que se hicieron.

### **00:48:23** {#00:48:23}

**Domiciano Rincón:** Ellos, ¿qué ellos qué dispositivo utilizan?

**Juan José Arias Gallego:** Y al final ellos utilizan,

**Domiciano Rincón:** ¿También o cámaras?

**Juan José Arias Gallego:** uf, utilizan unos infrarrojos. Aquí está el resumen, creo que es. Eh, y también utilizan imus, o sea, eh,

**Domiciano Rincón:** M.

**Juan José Arias Gallego:** dice captura autoelectrónica.

**Domiciano Rincón:** ¿Qué nos combinan?

**Juan José Arias Gallego:** Ajá. Incluso ellos no tienen cámaras de profundidad,

**Domiciano Rincón:** Ah, con Bicon.

**Juan José Arias Gallego:** sino que sino que lo que hacen es como recrear la dimensión 3D a partir de dos cámaras posicionadas, creo que una en plano frontal y otra en plano sargital.

**Domiciano Rincón:** Uy, pero de todas maneras el sistema Bacon. El sistema BON es ese sistema que utilizan en las películas para ese tema de de que el muñeco en 3D o el muñeco de la película tenga como el movimiento de la persona. No sé si han visto que eh, o sea, cuando muestran los detrás de cámaras de películas que tienen ese tipo de efectos especiales, entonces tienen como los actores tienen como pegados unas unas cosas en el cuerpo.

### **00:49:21**

**Juan José Arias Gallego:** Sí, sí,

**Domiciano Rincón:** Esos son como marcadores, pues digamos eh fotomarcadores. Entonces,

**Juan José Arias Gallego:** no que ser costoso.

**Domiciano Rincón:** las cámaras Bonso es como el eso es s super mega costoso. De hecho, nosotros lo tenemos como gold standard. O sea, todo lo que nosotros hacemos es para evitar tener un laboratorio de marcha de ese nivel, porque claro, el laboratorio de marcha de ese nivel está super bien y nosotros podemos hacer todos, ¿sí o no? Pero nuestra investigación intenta eh abaratar cosas, o sea, tener instrumentos de medición baratos que sean ambulatorios, digámoslo así. O sea, que incluso en un entorno de consulta, o sea, como que la persona viene, yo te pongo esa esas cosas aquí, camine y yo le saco la prueba, ¿sí o no? En lugar, digamos, como de ir a un sitio especializado con ese tema pues de cámaras porque tienen que estar posicionadas en unos sitios específicos y demás, ¿no? Claro, entiendo por qué el autor eh es importante, digamos, para el profe, porque el autor utiliza el Gold Standard, entre otros.

### **00:50:16**

**Domiciano Rincón:** O sea, si nosotros podemos sacar ese tipo de datos sin utilizar el Gold Standard, sino por ejemplo únicamente con IMOS, pues está super bien. Incluso no sé si la si la intención del estudio es comparar o o mezclar, o sea, comparar el go estándar, o sea, Bicon versus IMO o Bicon más IMO, pero la Bicon en sí, o sea, laamos como que nos permite a nosotros eh como capturar capturar y reproducir el el el movimiento exacto que hizo las extremidades de la persona. Pero cuando yo hablo de movimiento exacto, es Exacto, exacto. De hecho, en la Escuela Nacional del Deporte, aquí en Cali, pues hay un laboratorio de marcha. el único pues digamos como al al que nosotros digamos dentro de la dentro de la investigación hemos ido. Eli no tiene uno, por ejemplo, sí lo tiene la Escuela Nacional del Deporte, pero lo hacen es porque analizan, pues digamos como h la técnica de los corredores o la técnica de lo que tengan que analizar o el atleta pues que está. Entonces, por ejemplo, le pueden decir, no sé, consejos como de cómo mejorar su aerodinámica y no sé qué, pero porque nuevamente eso captura exactamente el el movimiento corporal, ¿no?

### **00:51:19** {#00:51:19}

**Domiciano Rincón:** Ajá. Es como el gold estándar, es como el estándar de oro, el el deber ser lo que uno quisiera siempre tener.

**Juan José Arias Gallego:** Sí, pues casi no vimos, o sea, no vimos como la intención de de comparar las cámaras versus los imus, eh, pero pues si lo el objetivo también nosotros era más que todo fijarnos en las variables extraídas y y en los resultados que obtuvieron.

**Domiciano Rincón:** Ok.

**Juan José Arias Gallego:** E y aquí hay un apartado como de resultados principales, por ejemplo, lo del tiempo total que no distinguió controles de fe con de fe en en estadio oillar 2 con los controles. Eh, el giro fue la fase más sensible. Yo creo que esto es un dato importante eh como

**Domiciano Rincón:** No, eso es importantísimo. Sí, o sea, definitivamente está bien suero.

**Juan José Arias Gallego:** variable temporal.

**Domiciano Rincón:** Pero, ¿qué? ¿Por qué se demoró más?

**Juan José Arias Gallego:** Y bueno,

**Domiciano Rincón:** O sea, se demoraron más los pacientes.

**Juan José Arias Gallego:** sí se demoraron mucho más los pacientes y eh ahí sí se pudo, o sea, casi siempre el la diferencia muy clara se notaba entre eh pacientes en estadio Onillar 2 y controles, pero no se diferenciaban casi entre controles y eh pacientes en estadio 1.5 o 1\.

### **00:52:42** {#00:52:42}

**Domiciano Rincón:** Ok.

**Juan José Arias Gallego:** Entonces, el giro si fue clave en ese en ese descubrimiento,

**Domiciano Rincón:** ¡Uf\!

**Juan José Arias Gallego:** en esa diferenciación. Eh,

**Domiciano Rincón:** simetría de coda.

**Juan José Arias Gallego:** también dicen que las alteraciones de marcha fueron más evidentes en pacientes en este estadio y la simetría de codo

**Domiciano Rincón:** Ah, está chévere. O sea, bueno,

**Juan José Arias Gallego:** también.

**Domiciano Rincón:** por ejemplo, la simetría de codo es algo que probablemente no podamos nosotros sacar, excepto si excepto con cámaras, mejor yo con estamos nosotros en IMO, ¿no? O sea, como nosotros vamos a comprobar cámaras, probablemente podamos sacar algo como lo de la simetría de codo, pero es difícil porque pues no tenemos el bicon y ustedes van a ver que esas señales son más bien unas señales que duran poco, ¿sí? eh no solamente duran poco, sino que pueden llegar a ser imprecistas cuando la persona se aleja mucho o se acerca mucho a la cámara. Pero en el en la ventana de tiempo, en donde la donde el esqueleto está posicionado exactamente en la en en digamos como en la las extremidades del paciente, algo se debe poder hacer, ¿no?

### **00:53:39** {#00:53:39}

**Juan José Arias Gallego:** Sí, sí. O sea, puede ser incluso interesante si siamos hallar cómo

**Domiciano Rincón:** Como eso mismo.

**Juan José Arias Gallego:** cómo sacar la simetría.

**Domiciano Rincón:** Sería super bien. Sería sería super bacana.

**Juan José Arias Gallego:** También un tema de ROM, que si no estoy mal es respecto a los al ángulo máximo y al ángulo mínimo en los movimientos. Yeah. Eh,

**Domiciano Rincón:** Ahora,

**Juan José Arias Gallego:** por ejemplo,

**Domiciano Rincón:** ahora quiero verificar.

**Juan José Arias Gallego:** inclinaciones o o la el ancho de de la marcha, o sea, el ancho entre paso de la marcha. Eh, sí, también hay datos que los que dice que no fue significativo, como la variabilidad de la marcha y

**Domiciano Rincón:** Increíble. O sea, uno pensaría que sí.

**Juan José Arias Gallego:** y dice que la confiabilidad, que es olvid el nombre de esto identificador interclasses, algo así,

**Domiciano Rincón:** Sí, sí, sí.

**Juan José Arias Gallego:** no recuerdo,

**Domiciano Rincón:** Ajá. Eh,

**Juan José Arias Gallego:** es cuando se repiten varias veces una prueba.

### **00:54:37**

**Domiciano Rincón:** es exacto. O sea, pues me parece me parece algo chévere. Lo que pasa es que regularmente uno en experimentos para asegurar repetibilidad uno debería tomar la prueba tres veces. Eh, pero sí,

**Juan José Arias Gallego:** M.

**Domiciano Rincón:** pues eso eso en brigada es imposible. O sea, como que si nosotros tenemos una muestra de un paciente, pues digamos como que está está bien, digamos, nos damos por bien servidos. Pero esto de hecho puede ser algo algo bueno para que nuestro nuestra conclusión del trabajo futuro, por ejemplo, ya cuando ustedes presentan PG2 eso, o sea, como que el uno puede tener mejores resultados si uno hace eso para que la viabilidad de intersujeto pues no sea un problema. ¿Cuál es el detalle de eso? que las variables biológicas son eh poco repetibles, o sea, tienen una alta sensibilidad y es la es lo siguiente. Hagan de cuenta que ustedes les ponen a, no sé, a caminar en una línea y lo que están evaluando es su trayectoria, o sea, que ustedes sigan la sigan una línea.

### **00:55:32**

**Domiciano Rincón:** Eh, es muy difícil que ustedes lo hagan exactamente en el tiempo, eh, que sigan exactamente la misma trayectoria y que y que den los pasos exactamente los mismos en los mismos puntos en dos o tres pruebas diferentes. Es prácticamente imposible. Entonces ese tema digamos como de como de la que de una tarea, pues si ustedes la miran como microscópicamente, pues si ustedes miran un poco con mayor detalle, ustedes se dan cuenta de que efectivamente eh la repetibilidad de intersujeto es un dato que hay que cuidar. Si es demasiada variable, entonces quizás el diseño experimental no está bien fundamentado, pero nosotros partimos con la suposición de que sí. Es decir, la prueba de TG está hecha para que la repetibilidad la la repetibilidad de intersujeto sea una mínima necesaria al menos controlada. ¿Sí? ¿Por qué? porque la persona va a hacer básicamente las mismas tareas y a pesar de que no lo haga exactamente igual en todas las ocasiones, pues ahí nos damos cuenta en esa conclusión de que efectivamente promediar las muestras de paciente, o sea, que no hayan tres muestras del mismo paciente, sino que esas tres muestras se representen en una y y se promedie todo, es mejor que que pues sí, o sea, que que que tratarlas como muestras independientes.

### **00:56:44** {#00:56:44}

**Domiciano Rincón:** a nosotros seguramente nos to que liar con eso, es decir, no tenemos la forma de sacar el el digamos como una sola muestra representativa por paciente, excepto pues para los pacientes que que se tomaron más muestras. Entonces, pues nada, lo podemos a digamos los podemos tomar como observación, o sea, un paciente que tiene tres tres tres pruebas, para mí son tres datos. En el estudio debería ser tomado así porque no podemos asegurar la repetibilidad ni tampoco el proceso de ICC para todos los pues para todas las muestras de todos los pacientes. Sí.

**Juan José Arias Gallego:** Sí, profe. O sea, yo creo que es con lo que con las condiciones que vos nombras, pues es difícil extraer, digamos, ese dato. Eh, pero entonces básicamente estamos intentando hacer ese ese especie de plantilla con las referencias más importantes, porque si bien en la primera búsqueda en anchura que hicimos, sacamos 25 referencias, puede que hayan unas que no sean tan significativas o tan relevantes.

**Domiciano Rincón:** tan relevante. Exacto.

**Juan José Arias Gallego:** Entonces, estamos intentando como hacer es ese filtro y las que más importen sacar

### **00:57:50**

**Domiciano Rincón:** S,

**Juan José Arias Gallego:** ahí pues la mayoría traer los datos más más importantes.

**Domiciano Rincón:** no super muchos. La verdad es que me parece que están avanzando de una forma muy buena, o sea, eh de forma metódica, sobre todo. Entonces, nada, la siguiente, ¿qué nos esperamos? e vamos variables temporales o espaciotemporales. Yo creo que lo que tendríamos que hacer dado que casi todas asumen la digamos como el corte el el corte específicamente de la muestra completa en fases, lo que se podría hacer, me dirán si si es posible, igual podemos avanzar y si en la siguiente pues no lo tenemos listo, pues pues nada, igual estamos avanzando. Muy bien. Es intentar utilizar el algoritmo de corte que se desarrolló en algún momento, pero en las muestras que en estas muestras o en las muestras actuales, si nosotros logramos separar las fases y logramos ver las mismas montañitas y las mismas formas de onda, significa que vamos a poder entonces ya directamente sacar nuestras primeras variables temporales, o sea, tiempos de levantamiento, tiempos de marcha, tiempos de giro, eso sería fabuloso.

### **00:58:59** {#00:58:59}

**Domiciano Rincón:** Sí. Así que la tarea sería hacerlo.

**Esteban Guarin Valencia:** Sí,

**Domiciano Rincón:** No sé si para una semana podemos intentarlo, eh, pero sí aplicar el algoritmo de corte ya directamente de segmentación, digámosle el algoritmo de segmentación.

**Esteban Guarin Valencia:** profe, eh una pregunta que me quedó es más que todo sobre lo del doble task. Ahí, ¿cómo haríamos con los datos?

**Domiciano Rincón:** Ah, los datos, digamos, como que están dentro del grupo de pacientes. Igual, sí, pero eh lo que podemos hacer es tener de todas maneras saber cuáles son, porque en algún momento también podríamos, o sea, si no son muchos, a ver, lo que pasa es que dentro de dentro de lo dentro de las muestras que se toman y demás, digamos, como que al doctor le pudo haber parecido interesante, entonces eh dijo seguramente no. Entonces, esta porém leer double TAS, pero si no son tantas muestras, o sea, si no son tantas muestras, me refiero a menos de 30, estadísticamente para nosotros realmente no tiene ninguna relevancia.

**Esteban Guarin Valencia:** M.

**Domiciano Rincón:** Sí, estadísticamente, o sea, si uno ya luego quiere sacar un análisis diferenciado de ver qué qué habrá pasado con el con el double task, pues entonces uno podría sacar algo, pero realmente no hace parte de de digamos como de nuestro alcance.

### **01:00:14** {#01:00:14}

**Domiciano Rincón:** Las podemos seguir tratando como muestras de paciente.

**Esteban Guarin Valencia:** son como pues de lo que aparecen en los comentarios son como tres muestras no más.

**Domiciano Rincón:** Sí. Y de seguro simplemente porque se dio la indicación como deb. Pongámosles las voltas a ver que a ver cómo actúa. Así que incluso hasta las podemos descartar si son solamente tres. Ajá. Pero la digamos como que la prueba se va a ver afectada digamos como más hacia hacia ser paciente. A ver, digamos como que el doctor cuando lo pide, cuando la persona con Parkinson con un estadio, digamos, no no no tan tardío, pues no, o sea, más bien en un estadio temprano, eh, no presenta alteraciones motoras y pareciera como que se comportara con normalidad absoluta, o sea, como que se se para, se levanta, gira sin problema, como si no fuera paciente. Entonces, a veces el doctor dice, "Hombre, o sea, yo ya la diagnostiqué, ya e pues digamos como que no está tomando medicamentos, pero pues debería tener como algún síntoma motor. Entonces voy a ponerle una tarea cognitiva para saber si puedo eh exacervar pues su

### **01:01:17** {#01:01:17}

**Domiciano Rincón:** su alteración motora. Sí. Entonces, eh pues sí, lo más probable es que la muestra en sí no sirva como muestra de paciente, dado que eh hacer el double tas va hacer que ella se pues sí, digamos como que manifieste ahorita sí sus su sus inconvenientes motores.

**Esteban Guarin Valencia:** Listo, profe. Muchas gracias. M.

**Domiciano Rincón:** Vale, muchachos. Entonces, creo que quedamos así, ¿cierto? Ya todo ahí quedó respondido, ya tienen cómo entonces hacer la metodología. Con la metodología ya pueden seguramente hacer el tema de cronograma. Y eh bueno, nada, creo que está el tema de la del digamos como el resumen o la planilla que tienen para las referencias como más importantes para ustedes, pues me parece que es una muy buena forma de pues una forma muy metódica de de de probar variables de la literatura dentro de este estudio. Así que super bien ahí. que vamosos hay algo más.

**Juan José Arias Gallego:** Bueno, y creo que es sería todo.

**Esteban Guarin Valencia:** Pues nosotros unas cositas al sprinlift, al overlif, pero digamos como una parte como con fórmulas y toda esa parte, pero pues eso se podría mirar más en otra reunión.

**Domiciano Rincón:** Eh, vale, vale, está bien.

**Esteban Guarin Valencia:** Listo, profe. Muchas gracias.

**Domiciano Rincón:** Muchas gracias por tiempo. Listo, nos vemos entonces.

**Esteban Guarin Valencia:** Saludo.

**Domiciano Rincón:** Ciao Co.

**Heiner Danit Rincon:** Listo,

**Santiago Gomez Robledo:** Sí.

**Heiner Danit Rincon:** profe. Muchas gracias.

**Juan José Arias Gallego:** Gracias,

### **La transcripción finalizó después de 01:02:57**

*Esta transcripción editable se generó por computadora y puede contener errores. Los usuarios también pueden cambiar el texto después de que se cree.*