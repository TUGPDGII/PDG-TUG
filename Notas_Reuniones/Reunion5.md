sept 29, 2026

## **Reunión del 29 sept 2026 a las 08:54 GMT-05:00**

Registros de la reunión [Transcripción](https://docs.google.com/document/d/1NVTSHcYWAmRpCOcPLcUcF1pBKwCg7-c3P1Kozj0bRhU/edit?usp=drive_web&tab=t.eira285owhv9) [Grabación](https://drive.google.com/file/d/1-U6ViKU9lJcQGRaajiYcAQealkIrnNqY/view?usp=drive_web) 

### **Resumen**

Revisión técnica de infraestructura, análisis de señales inerciales y reestructuración metodológica de objetivos académicos.

**Infraestructura y análisis de señales**  
Se detalló el almacenamiento en PostgreSQL y MinIO, estableciendo el filtrado de muestras por energía y el uso del IMU en espalda y tobillos.

**Estrategia de procesamiento de datos**  
Se discutió la implementación de un pipeline para la limpieza de señales y la adaptación de algoritmos ante variaciones físicas en el hardware.

**Reformulación de objetivos metodológicos**  
Se estructuraron y ajustaron los objetivos específicos del proyecto en Overleaf para enfocar el desarrollo en la clasificación y validación de variables biomecánicas.

### **Decisiones**

## **Acordada**

* **Estándar de frecuencia de muestreo predeterminada** Se acordó utilizar por defecto la misma frecuencia de muestreo del Colab y trabajar sobre una copia para evitar modificar el archivo original.  
* **Documentación del pipeline de preprocesamiento de datos** Se acordó documentar los pasos de preprocesamiento de las muestras mediante un diagrama de flujo o pipeline.  
* **Eliminación del componente temporal en objetivos Smart** Se acordó eliminar el parámetro temporal de la metodología Smart al redactar los objetivos del proyecto.  
* **Reestructuración de los objetivos específicos del proyecto** Se acordó estructurar los objetivos específicos en torno a la exploración de datos, validación del algoritmo de segmentación e integración algorítmica.

### **Próximos pasos**

- [ ] \[The group\] Definir N de muestras: Determinar el número de muestras adecuadas para el estudio, clasificándolas según la presencia de patrones de energía consistentes con levantamiento, giro y sentado.  
- [ ] \[The group\] Clasificar dataset: Categorizar el número de muestras que no cumplen con los criterios de calidad y reportar el conteo de pacientes versus controles.  
- [ ] \[The group\] Visualizar patrones: Crear un visualizador en Colab o Jupyter Lab para verificar el cumplimiento de los patrones de movimiento en las muestras de datos.  
- [ ] \[Domiciano Rincón\] Consultar frecuencia muestreo: Confirmar con Luisa Castaño si la frecuencia de muestreo de los datos actuales coincide con la utilizada en el Colab del trabajo antecedente.  
- [ ] \[The group\] Documentar pipeline: Documentar el pipeline de preprocesamiento de las señales mediante un diagrama de flujo para establecer los pasos de limpieza y selección de muestras.  
- [ ] \[The group\] Validar objetivos: Someter la actualización de los objetivos específicos y generales al curso con el profesor Navarro para su validación.  
- [ ] \[El grupo\] Mejorar objetivos: Ajustar la redacción y corregir la ortografía de los objetivos en el documento del proyecto.  
- [ ] \[El grupo\] Enviar objetivos: Someter la versión actualizada de los objetivos del proyecto.  
- [ ] \[El grupo\] Identificar variables: Compilar las variables identificadas a partir de la literatura científica para la próxima reunión.

### **Detalles**

* **Contexto de almacenamiento de datos e infraestructura en BMOP**: Domiciano Rincón explicó que dentro del sistema BMOP existe una base de datos PostgreSQL con extensión PostGIS utilizada para guardar los metadatos de las muestras tomadas a los pacientes, aprovechando características avanzadas de posicionamiento global. Precisó que los datos crudos, correspondientes a las señales e archivos JSON recibidos por el equipo, no se guardan directamente en PostGIS sino en un servicio de almacenamiento MinIO local en Docker, el cual imita la API de Amazon S3. Santiago Gomez Robledo y Domiciano Rincón aclararon la dinámica de registro automatizado en las notas.  
* **Estrategia de extracción de datos y problemática del dataset**: Domiciano Rincón detalló que el ingeniero Leonardo utiliza un script para filtrar únicamente las muestras cuyos archivos JSON fueron etiquetados en campo con la marca TUG. Explicó que esta extracción automática genera un sesgo implícito al incluir muestras sucias, incompletas o no estandarizadas debido a la dinámica de adquisición en brigadas médicas, donde prima la atención masiva continua sobre el filtrado riguroso en tiempo real ([00:01:01](#00:01:01)). Domiciano Rincón comparó esta limitación con la naturaleza habitual de los conjuntos de datos públicos en Kaggle ([00:02:09](#00:02:09)).  
* **Criterios de aceptación y evaluación de muestras en la ficha técnica**: Domiciano Rincón instruyó la creación de una ficha técnica que defina el número de muestras adecuadas (N bueno), el número de muestras malas (N malo) y el conteo detallado de pacientes y controles ([00:02:09](#00:02:09)) ([00:08:51](#00:08:51)). Estableció que el criterio formal de aceptación para una muestra válida es que presente el patrón de energía característico. Para verificar este patrón, se aplica una ventana deslizante (\*sliding window\*) sobre la señal, se calcula la FFT y se realiza la sumatoria por ventana para graficar la energía consumida en el tiempo, identificando picos claros al momento de levantarse y sentarse ([00:03:10](#00:03:10)) ([00:08:51](#00:08:51)).  
* **Estructura de las señales y análisis por ejes biomecánicos**: Ante la inquietud de Santiago Gomez Robledo sobre si los archivos JSON detallan las fases del test (levantamiento, giro, sentado), Domiciano Rincón aclaró que la muestra registra todas las fases y sensores simultáneamente, representando el reto principal de segmentación ([00:04:16](#00:04:16)). Detalló que las señales de los brazos presentan alta varianza y desviación estándar por falta de repetibilidad experimental, por lo que el análisis primario debe concentrarse en el IMU ubicado en la espalda alta (entre los omóplatos) y en los tobillos ([00:05:18](#00:05:18)). Aportó que en la espalda alta se deben revisar los seis ejes (tres del acelerómetro y tres del giroscopio) para identificar los patrones de movimiento en el plano ([00:06:34](#00:06:34)).  
* **Identificación visual de las fases de giro y sentado**: Esteban Guarin Valencia mostró una gráfica del entorno Colab destacando la presencia de los picos de energía inicial y final. Domiciano Rincón y Esteban Guarin Valencia analizaron la onda naranja, concluyendo que los ejes de aceleración diferencian el impulso inicial de pararse y el descenso al sentarse, pero no permiten aislar el giro ([00:10:05](#00:10:05)) ([00:17:06](#00:17:06)). Domiciano Rincón compartió una gráfica guía en el grupo manifestando que el giro modifica el plano de movimiento y se manifiesta en otro eje específico (señal G) mediante dos picos: un giro central al completar el recorrido y un giro final combinado con el proceso de sentado ([00:07:47](#00:07:47)) ([00:15:55](#00:15:55)).  
* **Estrategia para el pipeline de procesamiento de datos**: Santiago Gomez Robledo propuso la implementación de un \*data pipeline\* para la depuración y limpieza de las señales ([00:11:16](#00:11:16)). Domiciano Rincón respaldó esta propuesta especificando que el flujo debe replicar y afinar el algoritmo antecedente de los IMUs. Se discutieron ajustes en los parámetros del filtro Butterworth (como la frecuencia de corte) y la evaluación de umbrales de corte con operadores de ventana ([00:12:22](#00:12:22)). Domiciano Rincón sugirió la alternativa teórica de aplicar derivadas o la transformada Wavelet para la detección de cambios mínimos, aunque consideró que el algoritmo previo sintonizado puede ser suficiente ([00:13:37](#00:13:37)).  
* **Variaciones de hardware en los sensores IMU**: Domiciano Rincón expuso que los datos del estudio antecedente se recopilaron con un hardware prototipo anterior, mientras que el dataset actual utiliza una nueva versión de IMUs desplegada en brigadas. Advirtió que variaciones físicas en el ensamblaje de los nuevos sensores pueden haber alterado la orientación de los ejes (por ejemplo, giros de 90 grados que rotan el orden de X, Y, Z a Y, Z, X) ([00:14:44](#00:14:44)). Por esta razón, la fuente de verdad debe ser la comparación visual de patrones contra las gráficas de referencia ([00:15:55](#00:15:55)) ([00:18:04](#00:18:04)).  
* **Plan de trabajo semanal y verificación de parámetros**: Domiciano Rincón asignó como tarea para la siguiente semana la construcción de un visualizador en Colab o Jupyter Lab para auditar que los patrones de energía se cumplan en las muestras, considerando que sujetos con movimientos lentos mostrarán el mismo patrón extendido en el tiempo ([00:18:04](#00:18:04)). Esteban Guarin Valencia confirmó la creación de una copia del código para adaptar los algoritmos a las nuevas muestras entrantes ([00:19:04](#00:19:04)). Domiciano Rincón mencionó que consultará con la ingeniera Luisa Castaño para confirmar si la frecuencia de muestreo empleada en campo equivale a la del Colab ([00:20:19](#00:20:19)).  
* **Ajuste metodológico de objetivos bajo el esquema SMART**: Heiner Danit Rincon y Santiago Gomez Robledo informaron sobre las correcciones realizadas a los objetivos específicos atendiendo a las recomendaciones del docente Navarro, señalando que decidieron omitir el componente estrictamente temporal (T) dentro del formato SMART ([00:21:16](#00:21:16)). Domiciano Rincón coincidió con esta decisión explicándole a Heiner Danit Rincon que el uso de asistentes de inteligencia artificial suele forzar plazos o metas rígidas poco convenientes para la redacción técnica de proyectos de grado ([00:22:23](#00:22:23)).  
* **Revisión del objetivo general y estructura en Overleaf**: Esteban Guarin Valencia compartió en pantalla el documento formal compilado en LaTeX en Overleaf ([00:22:23](#00:22:23)). Domiciano Rincón examinó la propuesta del objetivo general centrada en desarrollar un algoritmo de clasificación basado en señales inerciales y cámaras RGBD para apoyar el diagnóstico de la enfermedad de Parkinson ([00:23:45](#00:23:45)) ([00:27:22](#00:27:22)). Domiciano Rincón recomendó reestructurar la formulación para precisar que el fin es diferenciar entre pacientes y controles mediante variables biomecánicas extraídas de las fases del test TUG, e integrar los algoritmos en MinIO y BMOP ([00:24:54](#00:24:54)) ([00:27:22](#00:27:22)).  
* **Reformulación y debate de los objetivos específicos**: Heiner Danit Rincon envió por WhatsApp el texto de los objetivos para revisión. Domiciano Rincón analizó cada punto, desaconsejando citar "Proyecto de Grado 1 o 2" y solicitando reducir la densidad de los textos para dar flexibilidad metodológica ([00:26:06](#00:26:06)). Tras revisar el proyecto antecedente, Domiciano Rincón propuso sustituir la revisión sistemática y el filtrado básico por tres o cuatro objetivos estratégicos: la exploración bimodal del dataset frente a la literatura, la validación y ajuste del mecanismo de segmentación de fases antecedente, la extracción de variables biomecánicas para el desarrollo del clasificador, y la integración de los algoritmos TUG en la plataforma BMOP ([00:30:58](#00:30:58)) ([00:36:42](#00:36:42)).  
* **Discusión sobre la validación de segmentación y anotación manual**: Domiciano Rincón, Esteban Guarin Valencia y Santiago Gomez Robledo debatieron sobre el alcance del objetivo de segmentación. Esteban Guarin Valencia sugirió enfocar los esfuerzos en la clasificación dado que la segmentación venía del proyecto anterior ([00:33:45](#00:33:45)) ([00:38:21](#00:38:21)). Domiciano Rincón advirtió sobre el peligro de condicionar el objetivo de segmentación a una "anotación manual de referencia", dado que esto exige la existencia garantizada de registros en video para cada muestra; propuso redactar el objetivo mediante la estructura sintáctica de verbo en infinitivo seguido del método en gerundio, enfocándolo en ajustar el algoritmo a la última versión del hardware de adquisición ([00:40:15](#00:40:15)) ([00:50:39](#00:50:39)).  
* **Consolidación final de objetivos y revisión académica**: Domiciano Rincón presentó la versión final recomendada para la secuencia de objetivos específicos (identificados como OEX, OW, OY, OZ), abarcando exploración de datos bimodales, ajuste de la segmentación en hardware nuevo, extracción de variables para el clasificador e integración funcional en BMOP ([00:43:03](#00:43:03)) ([00:47:27](#00:47:27)). Esteban Guarin Valencia y Domiciano Rincón acordaron intentar validar esta redacción con el profesor Navarro el siguiente lunes o en un espacio semanal alterno ([00:50:39](#00:50:39)).  
* **Cierre de la reunión y compromisos futuros**: Santiago Gomez Robledo, Esteban Guarin Valencia y Domiciano Rincón coordinaron el intercambio de enlaces actualizados del repositorio y del visualizador de Overleaf para el seguimiento mediante capturas y comentarios ([00:51:38](#00:51:38)). Como compromiso para el próximo encuentro, Santiago Gomez Robledo y Esteban Guarin Valencia señalaron que presentarán la identificación de las variables espacio-temporales y biomecánicas derivadas de la literatura, lo que facilitará la validación rápida durante la fase de limpieza de datos ([00:52:37](#00:52:37)).

*Revisa las notas de Gemini para asegurarte de que sean precisas. [Obtén sugerencias y descubre cómo Gemini toma notas](https://support.google.com/meet/answer/14754931)*

*Cómo es la calidad de **estas notas específicas?** [Responde una breve encuesta](https://google.qualtrics.com/jfe/form/SV_5bXzKQfylMIhSXc?confid=aFrrxUcsLif00p8yLv7kDxIWOBEQAjIGCIoCIAAYAQg&detailLevel=longer&hasImages=False&entryPoint=footerMain&isGoogler=False) para darnos tu opinión; por ejemplo, cuán útiles te resultaron las notas.*

sept 29, 2026

## **Reunión del 29 sept 2026 a las 08:54 GMT-05:00 \- Transcripción**

### **00:00:00**

**Domiciano Rincón:** entonces el el ¿Qué?

**Santiago Gomez Robledo:** Sí.

**Domiciano Rincón:** El trabajo es el siguiente, o sea, eh tenemos entonces, a ver, dentro de BMAP, y eso digamos como que de todas maneras para que queden las notas y demás, dentro de BMOP nosotros tenemos eh pues un registro en base de datos de todos los de todas las muestras que se toman. Sin embargo, digamos, esas esa esos datos que se toman en la base de datos llamada postgs, no es posstgres, sino postgis, es como una base de datos con el, digamos como con algunas features avanzadas para el tema de posicionamiento global. Por eso el tema de GIS eh es una base de datos en donde regularmente nosotros guardamos estos datos de los pacientes, pero lo que se guarda realmente son los metadatos, los datos en sí, o sea, todo el tema de señales, eh los JSONs específicamente que ustedes recibieron, se guardan en un en un S3, en un realmente no es un S3, o sea, se digamos como que las aplicaciones se vinculan por medio del mismo API de Amazon S3, pero eh se utiliza un minion.

### **00:01:01** {#00:01:01}

**Domiciano Rincón:** Mm. Sí, saben cuál es, cierto, mini mini es un eh digamos servicio de almacenamiento que pueden encontrar en Docker y es básicamente la forma un premis de de tener pues un servicio pues de almacenamiento y storage.

**Esteban Guarin Valencia:** Yeah.

**Domiciano Rincón:** Entonces ese storage eh es el que guarda las muestras realmente. Entonces se hace la estrategia de guardar los metadatos, se guarda un indicador como una especie de de referencia al archivo y el archivo luego eh pues lo podemos obtener desde mínimo. Entonces, lo que hace Leonardo, eh, pues el ingeniero pues que extrae los datos, él me mostró que lo que tiene básicamente es un script en donde verifica que los TAGs hayan estado marcados como TUG, o sea, en campo cuando tomaron las muestras, eh, la aplicación tagea todos los JSONs para que sean modo TUG, ¿sí? O sea, como que vamos a tomar la muestra de TUG, entonces queda tagado en el Jason y entonces por ende pues él puede buscar todas las muestras que se hicieron. Eso digamos como que invisibiliza varias cosas. Lo primero es que eh van a estar ahí todas las muestras incluyendo las que no están limpias.

### **00:02:09** {#00:02:09}

**Domiciano Rincón:** Entonces eh era lo que les decía y eso es como problema de cualquier dataset. O sea, si ustedes van a cualquier dataset de de Kagol, por ejemplo, no sé si han entrado pues a alguna vez alguna algún reto de Kagol o se o se han descargado algún ret de Kag, pues casi siempre viene con datos sucios, o sea, nulos en algún punto y demás, pero sobre todo es por la característica de adquisición de datos que se tienen en esas brigadas. La la adquisición de datos básicamente no es como un trabajo de oficina en el que yo puedo seleccionar eh de una forma tranquila eh qué muestra quedó mal o qué muestra quedó bien para eliminarla o para dejarla, sino que eso, mejor dicho, va llegando gente en fila y y uno intenta básicamente atenderlos a todos. Entonces, pues digamos como que habrán muchas eh muestras que no que que pues no están eh seguramente eh completas o que algunas estén sucias y que no sigan del mismo patrón y demás. Entonces, lo que quiero que establezcamos dentro de la ficha técnica es primero el N bueno, o sea, el N de muestras adecuadas.

### **00:03:10** {#00:03:10}

**Domiciano Rincón:** Para mí el criterio de aceptación de una muestra buena es que tenga el mismo patrón de energía. Sí, el el patrón de energía lo pueden realmente sacar de el colap de el trabajo de grado antecedente, porque en ese trabajo de grado antecedente, independientemente de de, o sea, antes de llegar al paso de segmentación, lo que se hace es un ventaneo de la señal, se saca la FFT y eh se hace la sumatoria de cada ventana. esa sumatoria entonces se establece pues como un gráfico en la en el tiempo. La la la ventana es una sliding window, pues o sea, una una ventana deslizante y entonces se desliza cada n muestras. Entonces, al final, digamos, como que tenemos, pues sí, básicamente la energía consumida por el paciente en el tiempo y eso pues digamos como que tiene unas montañitas de acuerdo pues a los ejes que se hayan tomado. Entonces, lo que yo esperaría ver es eh que solamente acepten pues aquellas que tienen el el patrón adecuado, por decirlo así. O sea, que cuando yo me levanto cuando yo me levanto gasto energía y cuando yo me siento también.

### **00:04:16** {#00:04:16}

**Domiciano Rincón:** Entonces, regularmente uno ve en esas señales como eh hay un pico inicial en el levantamiento y cómo hay un pico final en el en el sentado. Eh, sí. Entonces, por ejemplo, ahí digamos como que se manifiestan ciertos ejes del de la de los sensores de movimiento, ¿no? Todos, ¿no? Eh, el del giro, por ejemplo, el del giro no se no se mueve porque el giro va a permanecer intacto porque nosotros estamos orientados hacia, digámoslo, estamos orientados hacia el frente, pero cuando nos estamos devolviendo cambiamos 180 gr. Entonces ese giro se manifiesta en otro eje. Pero entonces hay un eje,

**Santiago Gomez Robledo:** Profe,

**Domiciano Rincón:** un eje que segura Sí, sí, dime.

**Santiago Gomez Robledo:** es que para en ese caso tengo una duda y es que por lo menos dentro de yo estaba

**Domiciano Rincón:** Sí.

**Santiago Gomez Robledo:** anoche revisando los datos y como tal pues en los Jason no viene como la fase. Entonces, nosotros nos toca definir a qué fase pertenece eh la medición en el Jason o cómo es eso, cómo hacemos ahí, porque lo que yo vio solamente sale como,

### **00:05:18** {#00:05:18}

**Domiciano Rincón:** con

**Santiago Gomez Robledo:** ah, bueno, este es el sensor del brazo derecho, este es el sensor del pie izquierdo, así.

**Domiciano Rincón:** fases te refieres a levantamiento, giro, sentado y demás.

**Santiago Gomez Robledo:** Exactamente.

**Domiciano Rincón:** E la muestra se toma toda en un en un solo momento. Es ese básicamente es el reto, ¿sí? O sea, el problema central del del proyecto es que digamos como que no se segmenta solo, sino que se toma todo en una sola muestra, o sea, todo me refiero a todos los sensores, espalda, piernas, todo al mismo tiempo. Sí,

**Santiago Gomez Robledo:** Listo.

**Domiciano Rincón:** los algoritmos que utilizaron en el trabajo antecedente solamente eran era con tres IMUS. Aquí pues también quisiera, digamos, como que ustedes me contaran a partir de los datos, pues cómo se tomaron. se tomaron con las cinco imos, aunque los brazos, muchachos, los brazos son muy son muy eh digámoslo hm muy poco repetibles experimentalmente. Eso significa que los los brazos en general, digamos como que no van a dar, o sea, van a dar el mismo patrón, pero a nivel digamos como de movimientos, RMS, arm swinging, eso va a ser, o sea, los datos son supremamente eh, digámoslo, variables, variantes, o sea, tienen una varianza grande, ¿sí?

### **00:06:34** {#00:06:34}

**Domiciano Rincón:** una una desviación estándar grande. Pues entonces, por ende, eh los brazos si están tomados está bien, o sea, chévere, pues probablemente nos sirva para algo adicional, digamos, en un análisis posterior, pero inicialmente nos tendríamos que que enfocar en el en el imu que está en la spine base, o sea, en la espalda baja, perdón, en la espalda alta, es en es como en medio de los de los omóplatos y e en los en los tobillos, ¿vale? Lo otro es que experimentalmente nosotros utilizamos una unos digamos como los IMUS los pusimos en una posición específica. Podría ser que quienes tomaron las pruebas eh hayan girado los IMU y si y si los giraron, entonces también nos tendríamos que percatar de eso. Hm. Pero sí, entonces digamos como que continuando con con lo demás, eh hay unos hay unos marcadores, pues, sobre todo en la espina base, ustedes van a ver que la espina base tiene seis ejes, pues porque es un IU igual. Entonces, de esos seis ejes ustedes lo que deben hacer es verificar en el en el en el trabajo antecedente cuál es el cuál de los seis ejes es el importante para poder establecer eh levantamiento y sentado.

### **00:07:47** {#00:07:47}

**Domiciano Rincón:** ¿Y cuál es el importante para establecer giros? ¿Sí? Entonces nosotros no utilizamos eh para eso las piernas. Las piernas las utilizamos, por ejemplo, para temas de pasos y cosas que no se desarrollaron completamente, pero que sí creo que puede tener, bueno, una, digamos, como un buen desarrollo en este proyecto de grado, pero casi todo lo hicimos con ejes del spine base. Si ustedes se fijan, entonces hay un hay un eje. Lo que pasa que claro, tendríamos que pronto como vernos, o sea, hagamos el hagamos ese tema, pero si que explicarlo así con palabras es es muy complejo, pero todos sabemos cuál es la prueba, ¿cierto? Y todos sabemos que nos levantamos y nos devolvemos, o sea, que la persona va a estar orientada y se va a mover en un plano, ¿sí o no? Es es claro eso, ¿cierto? lo del plano para que nos movemos en dos.

**Santiago Gomez Robledo:** Sí, sí, sí.

**Heiner Danit Rincon:** Sí, profe.

**Domiciano Rincón:** Pero,

**Santiago Gomez Robledo:** M.

**Domiciano Rincón:** pero cuando la persona gira, cuando la persona gira, en el momento en el que gira, e esa persona está modificando el plano, o sea, está girando en el en el mismo plano en el que en el que se encuentra.

### **00:08:51** {#00:08:51}

**Domiciano Rincón:** Entonces, ese giro se manifiesta en otro en otro eje. Entonces, al final, digamos, como que uno sabe que la montañita eh en ese eje corresponde al giro porque la persona iba recta y solamente modifica el eje en una fase de de esa de esa eh muestra. Entonces, pues uno ya sabe que esa montañita corresponde pues al giro. Entonces, uno regularmente pues eh nosotros lo hicimos con umbrales, entonces nosotros sabíamos cuándo la persona estaba girando y cuándo no. Bueno, digamos como que el propósito es es verificarlo. Entonces, nuevamente la definición de si está buena o no la muestra es que cumpla con esas dos mínimas condiciones, o sea, que se pueda ver la montañita del levantamiento, la montañita del giro y la montañita del sentado. ¿Listo? Y eh las pistas están sobre los seis ejes. Cuando yo me refiero a los seis ejes, me refiero a los tres ejes del acelerómetro y los tres ejes del ciroscopio. ¿Listo? Entonces, lo primero que tenemos que sacar es el n de muestras buenas, luego tenemos que sacar el n de muestras malas y luego tenemos que eh verificar pues cuántos pacientes y cuántos controles tenemos.

### **00:10:05** {#00:10:05}

**Domiciano Rincón:** Eso para mí, digamos, como que sería la ficha técnica hasta ese punto.

**Esteban Guarin Valencia:** Listo, profe. Mira que, o sea, yo pues como ya había revisado pues hace ya tiempo las los datos los datos que nos habías mandado antes en el en el colap,

**Domiciano Rincón:** Sí.

**Esteban Guarin Valencia:** pues si noté había una gráfica que si se nota como ese pico que vos comentáas.

**Domiciano Rincón:** Eh, sí, de hecho, de hecho, ustedes tienen acceso a ese colab, ¿cierto?

**Esteban Guarin Valencia:** Sí, señor.

**Domiciano Rincón:** Eso todavía tiene graficados los datos originales, digámoslo. Voy a mirarlo acá un momentico.

**Esteban Guarin Valencia:** ¿Cómo?

**Domiciano Rincón:** Eso todavía tiene los gráficos.

**Esteban Guarin Valencia:** Ahí mandé una foto que es más o

**Domiciano Rincón:** Ah, ah, eso, eso, eso, eso. Lo que pasa es que ahí, ahí es es solamente levantamiento y sentado. Ahí, ahí no se ve el giro, pero en una en un elemento posterior sí se ve el giro, pero sí, si esas montañitas literalmente son eh levantamiento y y sentado, o sea, lo que está en el centro que que pareciera como, o sea, como que la onda, todos estamos viendo la onda, ¿cierto?

### **00:11:16** {#00:11:16}

**Domiciano Rincón:** la onda naranja, la onda naranja pareciera que se levantara como hacia la mitad,

**Esteban Guarin Valencia:** Hm.

**Domiciano Rincón:** pero eso eso realmente no nos permite saber cuál es el inicio del giro y el final del giro, pero eh al menos ese ese esos ejes sí nos permiten saber pues cuándo cuándo comienza él a pararse y cuándo cuándo comienza él la marcha, porque regularmente lo que la persona hace es como que se como que se impulsa hacia adelante y se levanta, pero cuando ya está un estado como estable, o sea, cuando ya está de pie, eh pues ya esa energía de levantamiento pues ya no se gasta. Y lo mismo sucede para la onda eh final, digamos, o sea, la misma la misma onda naranja, pero para hacia el final. Entonces, así al final pasa lo mismo, o sea, la persona gasta una energía en descender para sentarse.

**Esteban Guarin Valencia:** Listo. No.

**Santiago Gomez Robledo:** Profe, para esta parte como de la depuración de datos, yo estaba mirando y como bueno, pues no sé que sería bueno implementarle un data pipeline para empezar con la limpieza o vos qué crees

### **00:12:22** {#00:12:22}

**Domiciano Rincón:** Eh, con data pipeline os referís a simplemente seguir unos pasos de preprocesamiento antes de tener las señales correctas.

**Santiago Gomez Robledo:** sí como para Pues sí, sí, sí, sí, sí.

**Domiciano Rincón:** Es eso es lo que esperamos, ¿no? O sea, eso es lo que quisiera que se generara, ¿sí? O sea, es decir, eh el paso por paso del preprocesamiento para sacar esa ficha técnica, pues ustedes pueden seguramente replicar lo que ya se tenía con IMUS, o sea, con replicar es llegar al mismo punto que llegaron sus antecesores, dado que ese algoritmo nosotros vamos a partir de él, pero vamos a verificar, o sea, seguramente lo tengamos que sintonizar en qué elementos hay que sintonizarlo. Por ejemplo, nosotros ahí utilizamos un filtro borderw pero de un de un crow frequency diferente. que que podría, por ejemplo, a la luz de los datos que ya tenemos entonces modificar ese cura of frequency o no. Otro elemento digamos como que podríamos verificar es los nosotros aquí utilizamos un umbral, o sea, básicamente un un operador de de ventana nada más. Entonces, después de que él supera el umbral o después de que disminuye cierto umbral, entonces nosotros hacemos el corte.

### **00:13:37** {#00:13:37}

**Domiciano Rincón:** Podríamos pensar de pronto en alguna técnica un poco más avanzada para sentir ese como ese ese cambio mínimo. Regularmente uno lo puede hacer o con derivada o con la transformada wavelet, pero pues son técnicas que quizás digamos como que no necesitamos y el algoritmo quedó lo suficientemente bien eh sintonizado como para que uno pueda hacer los cortes de los de los demás elementos, pero mínimamente tendría que cumplir con ese patrón. Este es de pronto el otro que tiene la montaña en el centro, o sea, en una de las en una de las detección de fases hay uno en donde aparece el giro. Lo voy a buscar aquí si de pronto lo tenemos como para dejarlo allí en el grupo, pues como para que sepamos pues que cuál es cuál es la guía, o sea, cuál es el patrón que debería seguir cada cosa.

**Esteban Guarin Valencia:** Pues lo estoy buscando y no lo encuentro.

**Domiciano Rincón:** Voy a verificar.

**Esteban Guarin Valencia:** Es que como es que ese día como yo subí todos los datos y y reinicié las gráficas,

**Domiciano Rincón:** Sí.

**Esteban Guarin Valencia:** pues ahí tenía el dato, pero como cada vez que se reinicia cola se reinician los datos y todo eso, entonces me estoy volviéndolo a insertar a ver.

### **00:14:44** {#00:14:44}

**Domiciano Rincón:** Pero, pero, pero probablemente también What?

**Esteban Guarin Valencia:** Vamos.

**Domiciano Rincón:** estar en el en el en el documento en el documento de los muchachos anteriores. Lo que pasa es que eso esas épicas me importan porque literal ese es el comportamiento esperado. Entonces lo que les decía era ustedes probablemente, o sea, eso se hizo con IMUS viejas, o sea, es una versión de IMUS, o sea, una versión de hardware que nosotros hicimos aquí en el grupo de investigación que tenía unos parámetros X. Sin embargo, los mismos los mismos eh sensores, sin embargo, con diferentes hardware eh fueron implementados posteriormente. Entonces, los nuevos IMUS son con los que se tomaron todas estas pruebas. Entonces, lo que les decía es que puede ser que durante el ensamblaje nosotros tengamos algún inconveniente con con algunos ejes,

**Esteban Guarin Valencia:** pago.

**Domiciano Rincón:** o sea, como que si por ejemplo el inmuno quedó a 90 gr, sino que quedó a 0 gr, entonces bien, pues porque concuerda efectivamente con con nuestros con nuestras con nuestros mismos ejes de ese análisis preliminar, pero por si por x razón los imus quedaron girados en alguno de los ejes, entonces el mismo elemento replicable, lo que pasa es que si si antes era, o sea, si antes era x yz, probablemente el mismo orden sea y zx, por poner un ejemplo.

### **00:15:55** {#00:15:55}

**Esteban Guarin Valencia:** ya

**Domiciano Rincón:** Tendríamos que verificar pues en el momento de los datos. Por eso digo que nuestra fuente de verdad debería ser la forma en la que salieron los en

**Esteban Guarin Valencia:** o

**Domiciano Rincón:** la que en la que teníamos, digamos, como los estudios antecesores. Eh, aquí tengo los los elementos. A ver. Eh, ah, sí, sí, sí. Aquí tengo uno que lo que si es en el trabajo está, pero pues lo voy a poner aquí en el grupo para que sepamos, digamos, como que cuáles son los gráficos espetables con todo.

**Esteban Guarin Valencia:** correo.

**Domiciano Rincón:** Eh, porfa, miren el grupo un momentico. Ese es el giro. El giro a todas estas ya me acordé que no no solamente tiene una montañita central, tiene una montañita final. Pero la razón es que la última fase es giro más sentado. Entonces la persona vuelve a salirse de su propio eje de movimiento porque la persona gira para sentarse. Sí. Entonces, eh pues digamos como que eh gracias a que la persona empieza a girar también podemos saber cuál es el inicio del giro, porque la persona como que se va a sentar, pero también digamos como que gira en el en el en el en en digamos como que en ese mismo evento de tiempo, ¿sí?

### **00:17:06** {#00:17:06}

**Domiciano Rincón:** Entonces, las dos gráficas son complementarias, ¿no? Entonces, con una gráfica yo puedo saber cuáles son los separadores de ciertas fases, pero como en el giro vieron que vieron que no, o sea, la la gráfica que mandó Esteban eh no digamos como que no tiene esa montaña central o ese pico central, entonces pues nosotros no podemos distinguir con ese mismo eje, no podemos distinguir el giro, pero con el eje correcto. En este caso nosotros teníamos la señal G, tendríamos que verificar pues en los nuevos IMUS cómo está tipificada. Eh, esa onda pues nos da dos giros, ¿sí? Que es el giro central y el giro final. ¿Sí o no? O sea, estamos claros entonces que hay dos giros. durante todo el evento.

**Juan José Arias Gallego:** Eh, sí,

**Santiago Gomez Robledo:** Sí,

**Juan José Arias Gallego:** profe.

**Santiago Gomez Robledo:** profe.

**Domiciano Rincón:** Listo, listo. No me había acordado de eso, o sea, me había acordado el giro central, pero claro, claro, la persona vuelve a girar, entonces eso se manifiesta pues en el que ah me va a

### **00:18:04** {#00:18:04}

**Esteban Guarin Valencia:** que reintegrar

**Domiciano Rincón:** tocar que si no eh si nos para que una vez en el semestre nos veamos y aclaramos todo, digamos, a nivel de que yo les muestre los imus, que miremos cómo se ponen en la en la Claro que quizá con los videos también ustedes lo puedan lo puedan verificar, pero dado que Unimos está en la espalda, pues Hay un eje de giro que cuando la persona pues se mueve en una en una sola dirección pues no se modifica, pero cuando la persona comienza a girar en su propio eje, es decir, para girar por ejemplo 180 gr, ese esa energía se se empieza a manifestar en ese eje de gir. Entonces, ese es el que nosotros estábamos viendo en esa última gráfica que mandé por el grupo. Eh, entonces esos patrones tendrían que cumplirse para todas las para todas las muestras. Entonces, un poco es, yo sé que es mucho, mucho que ver, pero ustedes pueden armarse un pequeño visualizador allí con el colap o con eh Júpiter Lab o lo que sea, en donde ustedes vayan mirando eh que los que los dos patrones se cumplen.

### **00:19:04** {#00:19:04}

**Domiciano Rincón:** Eso eso es lo mínimo necesario. Si la persona, por ejemplo, se levantó de una forma muy lenta, eh tendría que también igual verse la misma gráfica, pero distribuida en un tiempo mayor. Sí.

**Esteban Guarin Valencia:** Sí, profe.

**Domiciano Rincón:** Y eso es básicamente la tarea para la siguiente semana. O sea, nosotros distinguiendo ya cuáles cuáles gráficas, sí, cuáles gráficas, ¿no? Estamos muy bien. Lo otro es que estas gráficas está los datos que les pasaron están anonimizados, pero tienen una bandera que se llama istient o algo parecido. Entonces, patient true es que es paciente, patient false es que es control. Efectivamente,

**Esteban Guarin Valencia:** Listo. Entonces, si algo pues nos tocará que modificar un poco el código, pues para adaptarlo a las nuevas muestras que van llegando, No.

**Domiciano Rincón:** efectivamente eh pueden encontrarse como la mejor muestra posible, ¿no? O sea, como que ustedes distingan que efectivamente la gráfica se se pues digamos como que hay unos picos distinguibles que dura alrededor de unos 10 15 segundos y se pueden basar en una de las, o sea, dentro de todo el mar de muestras en una que es que es que esté, o sea, que se vea bien.

### **00:20:19** {#00:20:19}

**Domiciano Rincón:** Eh, con eso entonces pueden afinar pues cuáles son los ejes que se tomaron, pero los algoritmos deberían funcionar exactamente m exactamente igual, aunque aunque no estoy seguro. Sí, yo creo que igual contamos con el con la misma frecuencia de muestreo, pero de todas maneras dado que la dado que la transformada de furiero o sea la la técnica en la que se basa casi todo el análisis de energía que se hace acá, eh se basa en ese parámetro. Yo le voy a preguntar Luisa Castaño. Ella pues entre otras fue de las inineras que sacó las muestras en campo. Entonces, pues le va a preguntar si efectivamente la frecuencia de muestra es la misma que en el colap, pero de momento y por defecto manejemos la misma que en el colap.

**Esteban Guarin Valencia:** Listo, profe. Entonces, vamos a crear como una copia, pues, para no modificar que ya que ya está.

**Domiciano Rincón:** Perfecto, perfecto, perfecto. Lo otro que les iba a comentar era que eh los pasos del preprocesamiento, es decir, ¿qué es lo que hacen con las muestras?

### **00:21:16** {#00:21:16}

**Domiciano Rincón:** y demás para establecer nuevamente cuáles sí y cuáles no. Eh, documéntenlo de todas maneras, eso nos va a servir. Puede ser un diagrama de flujo. Al final el diagrama de flujo pues lo pueden pasar como el pipeline al que se refería Santiago.

**Esteban Guarin Valencia:** Listo. M.

**Domiciano Rincón:** No sé si hay algo más.

**Santiago Gomez Robledo:** Eh, profe,

**Heiner Danit Rincon:** Profe,

**Santiago Gomez Robledo:** ¿te parece si revisamos las correcciones que mencionaste la semana pasada o qué

**Domiciano Rincón:** Ah, sí, puede ser,

**Santiago Gomez Robledo:** hacemos?

**Domiciano Rincón:** puede ser.

**Heiner Danit Rincon:** check. Ah, bueno, profe. Profe, entonces nosotros hicimos las correcciones respecto también a los objetivos específicos que habíamos hablado la vez pasada de que teníamos que agregarle, teníamos que escribirlas en el formato Smar o teniendo en cuenta las siglas de los objetivos Smar. Y pues lo tratamos de hacer, sin embargo, nos dimos cuenta de que o bueno, en clase se mencionó con el profesor Navarro de que no íbamos a tener tanto en cuenta el tiempo, o sea, lo temporal dentro de las siglas Smart.

### **00:22:23** {#00:22:23}

**Heiner Danit Rincon:** Entonces, pues sería como lo único que tendríamos que quitarle más o menos.

**Domiciano Rincón:** Sí, lo entiendes lo que decís. Lo que pasa es que claro, o sea, cuando uno hace el objetivo Smart y uno tiene en cuenta la T y lo pasa por pues sí, por un asistente, pues un elemento de inteligencia artificial, él siempre les va a o a preguntar o a suponer que uno,

**Esteban Guarin Valencia:** Oh.

**Domiciano Rincón:** por ejemplo, no sé, vamos a analizar 70 muestras o vamos a analizarlo antes del yo no sé qué, de julio de 2027\. Sí, hace ese tipo de cosas, ¿no?

**Heiner Danit Rincon:** Sí, más o menos. o o simplemente nos la deja abierta, pues para colocarle una fecha en n semanas vamos a hacer esto y demás. Entonces, pues la fecha no se quitamos el espacio temporal dentro de los objetivos Smart.

**Domiciano Rincón:** Okay, okay, okay. ¿Quién

**Heiner Danit Rincon:** Sí. Eh, compartan

**Domiciano Rincón:** comparte? M. Yeah.

**Heiner Danit Rincon:** para acá.

**Esteban Guarin Valencia:** Ya, ya comparto. Dame un momento. Compartir pantalla.

### **00:23:45** {#00:23:45}

**Esteban Guarin Valencia:** Parece que esto. A ver, ya se está viendo.

**Heiner Danit Rincon:** Sí.

**Domiciano Rincón:** Sí. M.

**Esteban Guarin Valencia:** Listo. Este ya es como el archivo que tenemos ya en over. Pues ahí pues ya se ve comoas mejor presentad lo que ya estaba antes. Voy a ponerle unos objetivos.

**Domiciano Rincón:** Excelente. Todo debería estar en en latex en

**Esteban Guarin Valencia:** Sí,

**Heiner Danit Rincon:** Eh,

**Esteban Guarin Valencia:** nosotros pues teníamos también unos objetivos antes de ponerlos en SM, pero que

**Heiner Danit Rincon:** ¿ves? No pusiste los objetivos, Smar.

**Domiciano Rincón:** me refería al formato. Vamos a ver. Esos están. Ah, ya.

**Heiner Danit Rincon:** Sí.

**Domiciano Rincón:** Sí, claro. Ahí todavía saco los números, ¿no? Mm. Ah, ya, ya no, ya desarrollar un algoritmo de clasificación. basado en el análisis conjunto de señales inerciales, datos de cámaras, extra de las fases de la prueba con el fin de identificar patrones motores que apoyan el diagnóstico objetivo a la enfermedad parón.

### **00:24:54** {#00:24:54}

**Domiciano Rincón:** Me parece que está bien, o sea, me parece que está bien, o sea, igual ustedes ya lo ya lo sometieron también con con Navarro, ¿no? Esa actualización,

**Esteban Guarin Valencia:** No, profe, como ayer no tuvimos clase, entonces no hemos podido charlar con Navarro.

**Domiciano Rincón:** eh, o sea, eso dejémoslo, pero sí me gustaría que lo que igual lo sometieran, ¿no? O sea, si la oportunidad pues en el curso que lo que lo validen. A mí me parece que está super bien. Lo único que no sé es en el objetivo general dice como que identificar patrones, pero el objetivo podría ser establecer un primer clasificador, ¿no? No un primer, sino establecer un clasificador entre pacientes y controles a partir de la identificación de patrones motores, coma, que apoyen el diagnosismo. os entender porque el objetivo general sigue siendo mm o sea, añadamos eso, pero el objetivo me parece bien. Lo único que hay que hacer es lo que les decía, o sea, con el fin de eh a ver cómo cómo decir, eh, bueno, lo que dije, o sea, Yamina y por favor, eso último que dijimos, anótalo como importante.

### **00:26:06** {#00:26:06}

**Domiciano Rincón:** Entonces, dice identificar y perfilar.

**Heiner Danit Rincon:** Prof.

**Domiciano Rincón:** Sí.

**Heiner Danit Rincon:** Es que creo que los objetivos dentro del documento no están actualizados, entonces pues con el formato Smart.

**Esteban Guarin Valencia:** Hai

**Heiner Danit Rincon:** Entonces, los voy a enviar por el eso lo voy a enviar por el grupo para que lo podamos revisar por

**Domiciano Rincón:** Ah, eso, eso.

**Heiner Danit Rincon:** ahí. Entonces, ese que envié, este es el objetivo general.

**Domiciano Rincón:** A ver,

**Heiner Danit Rincon:** No.

**Domiciano Rincón:** desarrollar, validar, integrar los sistemas. M. el proyecto de grado.

**Esteban Guarin Valencia:** Buenos días.

**Domiciano Rincón:** E en ese primero, a ver, regularmente el objetivo general es el objetivo de todo el proyecto, entonces no debemos hacer referencia al proyecto de grado uno ni al proyecto de grado dos. ¿Listo? Eh, para mí sería desarrollar, es que no estoy seguro si algoritmo, es que es que sí, claro, o sea, no, sí podríamos pensarlo como en un algoritmo. Para mí sería casi quitar varias partes de eso porque eso me parece que es más como el predicado.

### **00:27:22** {#00:27:22}

**Domiciano Rincón:** Lo importante en en el objetivo es como lo primero que se dice. Entonces, yo diría como desarrollar un algoritmo de clasificación que diferencie pacientes con enfermedad de Parkinson de sujetos de control a partir de variables biomecánicas extraídas extraídas de cada fase de la prueba and go registradas con IMU y cámara RGBD. no le pondría el tema a los pacientes y le diría coma integrándolo en eh TMION y BMOP. Eh, a ver, dice, con un desempeño superior al de un modelo B que utilicé, ¿no? O sea, entiendo eso, pero para mí sería el que les dije, o sea, desarrollar un algoritmo de clasificación que diferencia de pacientes con enfermedad de Parkinson de sujetos de control a partir de variables biomecánicas extraídas de cada una de las fases de la prueba Tetapan Go registradas con IMU y cámara RGBD. Ya,

**Heiner Danit Rincon:** Eh,

**Domiciano Rincón:** hasta ahí en el objetivo uno que se

**Heiner Danit Rincon:** Señor

**Domiciano Rincón:** caracterizar durante las primeras semanas del proyecto. Bueno, ya sabemos entonces que se lo quitamos, ¿cierto? El tema de la T ya está quitado porque ahí todavía aparece

### **00:28:39**

**Heiner Danit Rincon:** el tema de la ¿Qué, profe?

**Domiciano Rincón:** de la T del temporal.

**Heiner Danit Rincon:** Ah, no. Pues tocaría entonces quitárselo al Sí, toca quitárselo al formato, profe. Ok.

**Domiciano Rincón:** pas que los los objetivos los los siento como como demasiado cargados de texto. Regularmente son un poco como más concisos. A ver, entonces voy a leerlo todo y lo lo podemos pensar como dice caracterizar durante las primeras semanas del proyecto el dataset bimodal. Bimodal se refiere a que tiene dos dos clases, aproximadamente 70 pacientes recolectado en brigadas de fundación, cuantificando la distribución y el balance de clases. Hm. la disponibilidad de etiquetas y el porcentaje de registro completas sincronizadas con ese es como el objetivo inicial, pues eso es como la tarea para la siguiente, ¿no? Conso li dando los resultados en un reporte de viabilidad que defina un sujunto de datos, ¿no? O sea, para mí es como caracterizar el dataset de imus y cámaras eh cuantificando la distribución, el balance de clases y la viabilidad, algo parecido. Es que ah es que es igual ese objetivo todavía lo siento.

### **00:29:46**

**Domiciano Rincón:** como un poco más un poco más débil, pero sí, eh, tiene tienen demasiado texto, ¿no? Eh, regularmente son, o sea, suelen ser más concilios. Hm.

**Heiner Danit Rincon:** Okay.

**Domiciano Rincón:** A ver, denme un momentico. Ah, es allá mandando por WhatsApp. A ver, eh, con, por ejemplo, en el trabajo antecedente a ustedes, eh, los objetivos no los veo, pero por ahí deben estar para que ustedes verifiquen pues lo que les comentaba. Hm. Qué raro. Eso pareciera que no está completo. Ah, ya. No, no, es que este es otro otro gráfico. A ver, es que demasiadas vainas por todo lado. Objetivo. A ver, un momentito, ¿no? Claro. Por ejemplo, miren que el primer objetivo creo que calza muy bien con respecto al elemento antecedente. Dice, "Realizar la exploración de datos obtenidos de las unidades inerciales durante la prueba TUG, identificando patrones y posibles variables relevantes. Yo creo que ese a pesar de que quedó como un poco más abierto, en nuestro caso puede ser algo similar.

### **00:30:58** {#00:30:58}

**Domiciano Rincón:** ¿Por qué podríamos mezclar el análisis documental que se ha hecho respecto al a la caracterización que ustedes están extrayendo? Sí, de hecho, ese objetivo me parece me parece como muy similar, muy cercano, digamos, al que ustedes podrían tener. Voy a ponerlo como que va a escribirlo por acá por WhatsApp, pues como un boceto. En este caso, digamos como que vamos a realizar la exploración de datos de los datos obtenidos en brigada. tanto de IMU como cámaras. Ya luego lo afinan, pues, cámara RGBD, no sé qué cosa. Eh, identificando identificando patrones. Ajá. Y variables relevantes. Eh, a ver. algo así. A ver, ¿cómo cómo lo ven? En el objetivo específico uno, ahí tendríamos dos entregables. Uno es el análisis de las variables y otro es el la misma exploración de los datos obtenidos. e porque ahí ahí sale mucho, o sea, ahí podríamos digamos como no quedarnos en el informe en el informe inicial porque literal la tarea que les puse es como si fuera el objetivo uno, pero el objetivo los objetivos en general tendrían que ir mucho más allá.

### **00:32:30**

**Domiciano Rincón:** Entonces, en este caso, por ejemplo, necesariamente para poder cumplir el objetivo uno que estoy proponiendo allí, tendrían ustedes que caracterizar los datos, posteriormente realizar la exploración ante los estudios antecedentes que ustedes ya habían realizado preliminarmente. Entonces, eh es es superior ¿no? Entonces, yo tengo de hecho varios entregables, o sea, tengo las posibles variables, eh puedo hacer análisis de viabilidad de una vez, la viabilidad va implícita a pesar de que no se exprese, eh, se entiende, ¿cierto? O sea, como que, ah, por acá en X Studio sacaron esas tres variables biomecánicas. Entonces, vamos a ver si las podemos sacar. Ah, sí, las podemos sacar. Y ese informe que en el que nosotros vamos a establecer cuáles sí, cuáles no, eh cuáles nos sirven y demás, eh es justo lo que nosotros podríamos requerir en este proyecto. Para mí el objetivo e el objetivo podría ser ese, porque fíjense que ya de aquí en adelante en el objetivo dos como que listo, o sea, ustedes establecen ahí como una como la la revisión sistemática pues de la literatura, pero creo que incluso se creo que esa incluso esa esa podría ser hasta el objetivo uno porque temporalmente tendría que ser primero el tema de la exploración en la literatura y posteriormente ahorita sí verificar esa viabilidad, No,

### **00:33:45** {#00:33:45}

**Heiner Danit Rincon:** Ok.

**Domiciano Rincón:** pero sí mirando a ver esta ventanita de esta cosa. A ver, voy a cambiar por el O2. El O1 sería el este primero. Lo que pasa es que incluso el análisis sistemático de la literatura podría no ser objetivo y más bien sí el tema de la de la integración con BMOP. A ver, seleccionar el el dos podría ser el dos, ¿no? Pero es que igualo, o sea, para un trabajo de estas características, yo creo que incluso suma más valor si ustedes lo pueden, pues, si ustedes lo integran con mismo, que es el plan inicial, eh, validar y ajustar el mecanismo de segmentación de fases. En la en la reunión pasada habíamos comentado que la segmentación de fases eh sí debía o no debía ser tenido en cuenta.

**Esteban Guarin Valencia:** Me parece que más que todo es como la clasificación porque es que la cimentación no como ya sí ya está.

**Domiciano Rincón:** Mm, exactamente.

**Esteban Guarin Valencia:** Ups.

**Domiciano Rincón:** Eh, validar Sí, sí, no, no sé. validar y ajustar el mecanismo deación de fases del proyecto precesor sobre el subconjunto de registros acompañando los límites.

### **00:35:20**

**Domiciano Rincón:** O sea, entiendo lo que quieren decir. O sea, están reconociendo igual que deben continuar pues con el el algoritmo de segmentación del del pasado, pero nuevamente eso me parece como un paso más interno en lugar de un objetivo.

**Esteban Guarin Valencia:** Es es como refinarlo, pero entonces no lo colocaríamos ahí.

**Domiciano Rincón:** Eh, sí, creo que no. Y el último es extraer para cada fase. Extraer para cada fase. Extraer para cada fase. Mm. Las variables mecánicas priorizadas. Priorizadas, no estoy seguro. En el objetivo dos ustedes dijeron algo como de como de priorización, pero no sé si el análisis sistemático de la literatura. Lo que pasa es que el objetivo que les que que propongo allí realmente suma tanto el tema de de de análisis de literatura como eh la validación de los datos de brigada. O sea, lo el primer objetivo que tendría que uno que realizar sería algo así como la exploración de los datos obtenidos y hacer como como un versus con la literatura. es realizar la exploración de los datos obtenidos en brigada, tanto mismo como en cámaras, identificando patrones y variables relevantes eh acorde a la literatura.

### **00:36:42** {#00:36:42}

**Domiciano Rincón:** Si, o sea, si se fijan, ese último objetivo suma más o menos los dos primeros de una forma, pues, digamos, como un poco más concisa. da en general, digamos como que los objetivos, y bien digamos como que son específicos, tiene la suficiente holgura como para uno poder darlo por terminado de una forma más sencilla, o sea, como que da más como que uno tiene que ser estratégico al momento de escribir esos objetivos porque eh si uno pone un objetivo pues muy difícil de cumplir, pues uno puede salir con un proyecto en donde pues no se haya cumplido un objetivo. si uno los pone como lo suficientemente hm flexibles, pues uno puede responder al objetivo de una forma pues similar. Eh, a ver, quisiera ver igual es que el el último, a ver, eh, seleccionar, validar. Es que nosotros aquí hacemos validación. Para mí están claros tres objetivos. No sé si no sé si un cuart para mí está siguen siendo como a ver el oy el oe y podría ser algo como h desarrollar el algoritmo que estoy escribiendo en el grupo algoritmo de clasificación basado en los marcadores, los indicadores, marcadores, variables en las variables extra la exploración y el OZ nuevamente eso es un boceto, ¿no?

### **00:38:21** {#00:38:21}

**Domiciano Rincón:** No es que deban quedar así. Y el último es integrar el algoritmo de la plataforma de Bmot. lo va a presentar como algoritmo de TUG porque los hay varios, ¿no? Entonces habría digamos como que haría falta pues el algoritmo de segmentación, haría falta el algoritmo de de clasificación,

**Esteban Guarin Valencia's Presentation:** Ah.

**Domiciano Rincón:** el de análisis de eh de marcadores biomecánicos, integrar los algoritmos de de TUG a la plataforma BMA, algo así para mí. Claros, claros, claros están esos tres objetivos, eh, pero siempre me queda la duda de cuáles fueron los objetivos iniciales, iniciales, iniciales. Eh, a ver, creo que los puedo tener por acá. Denme un momentico.

**Esteban Guarin Valencia:** Dale, profe.

**Domiciano Rincón:** Creo si ya lo encontré. Espero que raro. No puedo abrir, eh. implementar y verifiquemos su objetivo tres, objetivo dos, que seleccionar. Ah, no, ese no. Validar y ajustar el mecanismo de segmentación de proyecto precesor. Le comento datos contra una anotación manual de referencia. Mm, ya sé lo que quieren decir.

### **00:40:15** {#00:40:15}

**Domiciano Rincón:** No sé la no sé la forma, o sea, no sé si eh tengamos un bloqueo a nivel de saber si es viable, mejor dicho, el objetivo tres, porque lo que ustedes están proponiendo es validar el el el o el mecanismo predecesor de segmentación. Me parece bien, o sea, le podemos dar como continuidad y podemos gastar unos como el último objetivo específico en eso. Eh, pero dado que ustedes dicen como eh contra una referencia manual, eh dependemos exclusivamente de si existen videos para cada una de las muestras. Si no existen videos para cada una de las muestras, eso no lo podemos hacer. Entonces, lo podemos un poco generalizar más, de modo que nosotros podamos eh pues tener como esa holgura de que si existe video pues mucho mejor y se puede validar perfecto, pero si no va a estar va a estar complicado, ¿eh? O sea, si no, yo lo dejaría validar y ajustar, validar y ajustar, no estoy seguro si no validar y ajustar. Lo otro es que también en ese tipo de objetivos uno regularmente utiliza un verbo y luego eh da da la frase de cuál es el objetivo y luego coma eh y utiliza uno el gerundi entonces o sea es como validar ta coma ajustando tal tal.

### **00:41:31**

**Domiciano Rincón:** Sí, regularmente es como la como la forma en la que uno establece pues esos objetivos. Entonces uno podría llegar y decir, "A ver, e que pasa es que no estoy seguro en qué orden va. Lo puse con letras, pero luego luego le damos como números. M.

**Esteban Guarin Valencia's Presentation:** Yeah.

**Domiciano Rincón:** o x o y o z. Voy a ponerlo e o o e a o e validar el mecanismo que el algoritmo también un algoritmo validar el algoritmo de segmentación de fases de proyecto presor sobre sobre el subconjunto, ¿no? sobre el proyecto recesor sobre el e conjunto de datos e adquiridos en brigado. Variedades mm comparando los límites de fase detectados contra anotación manual. Eso es lo que creo que no deberíamos poner y reportando el error temporal promedio por transición y porcentaje de fase. O sea, claro, está super bien específico, sino que eso implica pues que si por x o y razón no tenemos los elementos suficientes para poder dar eh pues con exactamente tal cual como es el objetivo, eh vamos a terminar como en un cumplimiento parcial y eso pues no no es lo que uno quisiera.

### **00:43:03** {#00:43:03}

**Domiciano Rincón:** Validar el algoritmo de segmentación de fases, o sea, el que propongo, a ver, ese es el draft de momento. Validar el algoritmo de segmentación de fases del proyecto predecesor sobre el conjunto de datos adquiridos en brigadas. Eh, e sí, no, lo que pasa es que igual tenemos la SIM, digo, tenemos las cámaras segmentación eh ajustando Eh,

**Esteban Guarin Valencia:** Profe, y en comparación a los que están en el Smart, sería mejor dejar los que están en el que en el Smart en el en el overl

**Domiciano Rincón:** no los Ah, ya. Lo es que lo como lo tengo minimizado, no no vi que todavía estabas presentando. Ya los miro, ya los miro.

**Esteban Guarin Valencia:** que igual pues el de los como no están con Su están un poco mejor.

**Domiciano Rincón:** Eh, lo que pasa es que claro, o sea, a ver, los voy a, o sea, voy a poner los que los que creo que deberían ir y ya miramos el de over, ¿vale?

**Esteban Guarin Valencia:** Listo, profe. Yeah.

**Domiciano Rincón:** Para mí quedaría algo así. Fíjense en ese objetivo.

### **00:44:33**

**Domiciano Rincón:** Ya luego entonces voy a poner la temporalidad, pero validar el algoritmo de segmentación de fases del proyecto predecesor sobre el conjunto de datos adquiridos en brigadas, ajustando el algoritmo a la última versión de los sistemas de adquisición de datos. eh en lugar, digamos, de los sistemas deción de los sistemas es que sí,

**Esteban Guarin Valencia's Presentation:** M.

**Domiciano Rincón:** ¿no? Sí, los sistemas de equisión de datos se yo creo que se sobreentiende que es hardware e y la temporalidad sería la siguiente. X \= 1, W \= 2, \= 3 y Z \= 4\. Para mí serían esos que están allí. Eh, ya miro entonces los que tienen tienes compartidos. Se van. Entonces dice, hm, identificar el dataset bimodal existente tan tan. Listo. Es muy similar al al objetivo. Yo me quedaría con el de WhatsApp. Realizar la exploración, perdón, realizar la exploración. Es que no lo entiendo. Realizar la exploración. Las técnicas reportadas en la literatura científica sobre la prueba Tug instrumental para identificar el conjunto teorías biomecánicas.

### **00:45:39**

**Domiciano Rincón:** Ese se podría un poco combinar con el objetivo que en este momento está como el segundo. Lu analizar los datos tomados en campo para extraer las variables biomecánicas. Eh, denme un momento, yo verifico los otros. Mm, ya el Z, el Z podría mejorar entonces. Eh, perdón, no el Z, el Y desarrollar el algoritmo de clasificación. Claro, sería como eh A ver cómo dice ese objetivo. Dice realizar la excavación, analizar sumados en campo. A ver cómo echar a ver. Eh, exer las bares biomecánicas para desarrollar clasificación. A ver, pasa que yo no sé cuánto da WhatsApp para editar las cosas. A ver, dice, extraer las variables biomecánicas extraídas durante la exploración de datos para desarrollar el algoritmo de clasificación. Creo que ese objetivo acumula todo lo que tiene que ver con desarrollo de algoritmos, ¿no? O sea, extraer las variables biomecánicas y dado que x es igalizar la exploración de datos obtenidos en brigadas tanto como en cámaras identificando patrones. identificando patrones y variables relevantes acuerdas de la literatura científica o encontradas más bien o encontradas o así clar y ese ya no me lo permite editar.

### **00:47:27** {#00:47:27}

**Domiciano Rincón:** Yo creo que los que están en WhatsApp están ajustados con ese. A ver, el segundo, el tercero, perdón, analizar. Ah, no, eso ya lo habíamos leído. Implementar un algoritmo de clasificación. Lo que pasa es que lo que yo veo los algoritmos que están allí en el overlif es que hay, o sea, se gastan dos para el procesamiento de datos que son el segundo y el tercero. Y el primero que es identificar el dataset. Yeah. La propuesta que les hago es eh que el primero tenga que ver entonces con la, o sea, que la exploración y la búsqueda de de de de datos hagan parte del primer objetivo. O sea, como que la exploración de los datos de brigada más verificar las variables de de brigada. Están básicamente como en conjunto en el primer objetivo, ¿no? El OEX.

**Santiago Gomez Robledo:** What?

**Domiciano Rincón:** En el segundo solamente gastamos eh en el segundo extraer las variables biomecánicas. El el segundo a pesar de que es pues como un poquito más más conciso, más corto, es el que, perdón, ese sería el tercero, ¿no?

### **00:48:32**

**Domiciano Rincón:** A ver, estoy luego con esta numeración. W validar el algoritmo de segmentación de fases. Ya, ya, ya, listo. Entonces, primero entonces se realiza la exploración de datos. El segundo es validar el algoritmo de segmentación. El tercero es extraer las variables biomecánicas extraídas durante la exploración de datos. Ahí tien en cuenta las dos cosas, ¿no? Tiene en cuenta las variables encontradas dentro de la exploración de los datos, que la exploración de los datos le estamos llamando a explorar los datos de brigada más eh verificar, digamos, como las variables biomecánicas en en eso hace realmente parte del mismo proceso, ¿no? Porque nosotros vamos a tener que limpiar el dataset necesariamente para poder hacer esa exploración y esa exploración implica pues que tengamos que buscar en la literatura para marcar cuáles variables podrían ser adecuadas para el estudio o no. Eh, luego entonces después de que se tiene el algoritmo, que es el tercer objetivo, validar el algoritmo es, perdón, extraer las variables mecánicas para crear el algoritmo de clasificación. Entonces, al final sí se puede integrar los algoritmos de TUG ABIMP, ¿sí o no se

### **00:49:30**

**Esteban Guarin Valencia:** Sí,

**Domiciano Rincón:** entiende?

**Esteban Guarin Valencia:** profe.

**Domiciano Rincón:** O sea, entonces quedarían así. A ver, este sería el uno, el dos sería el W. Y ahí creo que pues igual entiendo el la importancia del segundo objetivo igual porque pues digamos como que ahí tienen en cuenta que viene un trabajo predecesor. Entonces, creo que es creo que está bien, o sea, creo que está bien porque igual digamos como que son diferentes datos, son diferentes sistemas de adquición de datos, pero al final el el objetivo es darle continuidad al al al otro al otro proyecto y creo que tiene incluso pues por ahí errores de ortografía, pues que no escribir las palabras correctamente, pero bueno, confío en que ustedes lo pueden mejorar. Creo que serían esos. Yo sé que le hemos perdido varios varios minutos a esto, pero la verdad eso es quizá lo más importante. Eso es al final lo que ustedes en la exposición final ustedes dicen, por ejemplo, ustedes dicen, por ejemplo, no sé, van a presentar una una diapositiva en donde ustedes muestren cómo cumplieron cada objetivo.

### **00:50:39** {#00:50:39}

**Domiciano Rincón:** Entonces, si yo veo los objetivos, yo ya veo claramente los entregables. Sí, obviamente habrá que ajustar algunas cosas. Podemos quitar la T.

**Esteban Guarin Valencia's Presentation:** M.

**Domiciano Rincón:** como ustedes dicen, pero tendrían que ser lo suficientemente eh sucintos como están acá, ¿sí? O sea, por máximo dos frases. Entonces, va validar tan tan tan coma ajustando tal cosa. Sí, regularmente la la el patrón de objetivos entonces es así como el el verbo en infinitivo diciendo qué es lo que voy a hacer en el objetivo, coma y luego cómo lo voy a hacer a través del gerundio. Listo.

**Esteban Guarin Valencia:** Prof.

**Domiciano Rincón:** Pero creo que esa última versión que sacamos aquí, pues mezclando un poco pues lo que está en el overlift, lo que desarrolló Heiner y eso, pues digamos como que creo que esos son pues estamos muy cerca como de la de la última última última versión, pero sí me gustaría que pudieran someterlo si es posible dentro de la clase, si no es posible y ya están en otro tema, pues pues nada, los dejamos así, pues es posible que los puedan someter.

### **00:51:38** {#00:51:38}

**Domiciano Rincón:** ¿Listo?

**Esteban Guarin Valencia:** Listo, profe. Pues esperamos el lunes hablar con Navarro o a ver si encontramos un espacio esta semana.

**Domiciano Rincón:** Vale, vale, vale. De un igual eso es un draft, ¿no? Entonces mejoran, pues digamos un poco la redacción. El último objetivo digamos como que no le hemos puesto gerundio, entonces pues digamos como que también puede ser algo adicional. Listo.

**Esteban Guarin Valencia:** Prof.

**Domiciano Rincón:** Eh, ustedes en la descripción del grupo tienen el trabajo y demás, ¿cierto? O sea, tienen,

**Esteban Guarin Valencia:** del

**Domiciano Rincón:** o sea, esa descripción del grupo ya sería un link caducado, pues porque eso es un sharepoint, pues que me imagino que ya no vamos a utilizar.

**Esteban Guarin Valencia:** documento PD. Ah, sí, ya lo modificó el de Olif,

**Santiago Gomez Robledo:** Sí, profe, ya lo actualizamos.

**Esteban Guarin Valencia:** que este guía

**Domiciano Rincón:** Vale,

**Santiago Gomez Robledo:** Dame un segundito.

**Domiciano Rincón:** vale, vale. Gracias.

**Santiago Gomez Robledo:** Ya pongo el rapo ahí.

**Domiciano Rincón:** También podría ser, también podría ser pues el enlace de overlift, aunque pues ustedes me lo mandaron, pero yo no entré.

### **00:52:37** {#00:52:37}

**Esteban Guarin Valencia:** por allí arriba.

**Domiciano Rincón:** Ah, bueno, no, pero lo puedo ver, pero obviamente en modo visualizador. Listo, listo.

**Esteban Guarin Valencia:** Sí, pues es que es como tenemos ese pequeño problema con el overl,

**Domiciano Rincón:** No, no,

**Esteban Guarin Valencia:** pues igual

**Domiciano Rincón:** realmente no le veo tanto problema. O sea, lo que les digo es eso, puedo sacar una pequeña captura de pantalla y en qué página me estoy refiriendo a los comentarios que pues vaya a poner en los en lo sucesivo. Pues de esa forma ustedes pueden encontrar.

**Esteban Guarin Valencia:** igual como Igual ¿Cómo lo vamos a pasar, digamos, a a ver cómo lo sincronizamos con el con el repositorio y cómo lo vamos a manejar? Pues se hará más fácil pues editarlo y pues poner los comentarios y toda la todos los pasos.

**Domiciano Rincón:** Vale, vale, listo. Entonces quedamos Q, ¿cierto?

**Esteban Guarin Valencia:** Sí, porfa.

**Heiner Danit Rincon:** Sí.

**Domiciano Rincón:** Bueno, muchachos. Listo. Entonces,

**Santiago Gomez Robledo:** Profe,

**Domiciano Rincón:** eh

**Santiago Gomez Robledo:** yo creo que para la próxima reunión nos faltaría solamente Okay. como las variables que se identificaron de de la literatura.

**Esteban Guarin Valencia:** espacio temporales.

**Domiciano Rincón:** está bien, está bien. Aunque creo que adelantarnos en ese paso eh nos va a ayudar seguramente porque dado que la tarea ahora es limpiar los datos, nosotros vamos a poder validar rápidamente si podemos implementar eso y de una vez si nos da pues digamos como buenos resultados. Sí.

**Esteban Guarin Valencia:** Profe,

**Domiciano Rincón:** consecuentes con la literatura.

**Santiago Gomez Robledo:** Listo, brother.

**Domiciano Rincón:** Vale, muchachos, muchas gracias.

**Santiago Gomez Robledo:** Hasta luego,

**Esteban Guarin Valencia:** muchas gracias a usted,

**Santiago Gomez Robledo:** profe. Gracias.

**Esteban Guarin Valencia:** profe.

**Heiner Danit Rincon:** Profe,

**Juan José Arias Gallego:** Sí,

**Heiner Danit Rincon:** usted muchas gracias.

### **La transcripción finalizó después de 00:54:25**

*Esta transcripción editable se generó por computadora y puede contener errores. Los usuarios también pueden cambiar el texto después de que se cree.*