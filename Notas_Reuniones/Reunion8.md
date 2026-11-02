oct 27, 2026

## **Reunión del 27 oct 2026 a las 08:54 GMT-05:00**

Registros de la reunión [Transcripción](https://docs.google.com/document/d/1WJvPPoDmZ8H5U84xqHQgQma1cb50VRIN9rIoUCaFO8E/edit?usp=drive_web&tab=t.e7u024n6fn3l) [Grabación](https://drive.google.com/file/d/1_qvUmhW5k2p4BOAsnLbiDrtVrAEItne-/view?usp=drive_web) 

### **Resumen**

Revisión de procesamiento de señales y análisis de datos con sensores para el proyecto.

**Preprocesamiento de señales de movimiento**  
Discusión sobre la interpolación temporal y la aplicación de la transformada Wavelet para segmentar pasos.

**Consolidación de datos de brigadas**  
Procesamiento de archivos JSON y adaptación de algoritmos para la segmentación con sensores IMU.

**Evaluación de datos y controles**  
Estrategia para incrementar el grupo de controles y planificar pruebas estadísticas robustas.

### **Decisiones**

## **Acordada**

* **Alcance metodológico del sistema de cámaras** Se acordó que el sistema de cámaras se utilizará exclusivamente para medir el tamaño de la zancada y la velocidad de la marcha, limitando los giros del TUG a los sensores IMU debido a limitaciones de cobertura.  
* **Uso provisional de aumento de datos** Utilización temporal de la técnica de aumento de datos como una muleta hasta disponer de suficientes datos finales.  
* **Conservación de datos externos compatibles** Retención de datos externos a la brigada que compartan exactamente el mismo diseño experimental.  
* **Búsqueda de controles en el Bod** Búsqueda de controles y datos en el Bod para complementar las mediciones de las IMU.

### **Próximos pasos**

- [ ] \[Juan José Arias Gallego\] Solicitar permisos: Enviar un mensaje interno al profesor Domiciano para gestionar las autorizaciones del viaje.  
- [ ] \[Domiciano Rincón\] Gestionar autorizaciones: Realizar las gestiones necesarias ante los directores de programa para los permisos estudiantiles.  
- [ ] \[Domiciano Rincón\] Consultar datos: Solicitar a Leonardo la información faltante sobre las grabaciones de la brigada.  
- [ ] \[El grupo\] Analizar grabaciones: Ejecutar el preprocesamiento y validar las señales presentes en los videos de las cámaras.  
- [ ] \[Esteban Guarin Valencia\] Identificar variable: Buscar la variable booleana de paciente dentro del sistema de cámaras.  
- [ ] \[Juan José Arias Gallego\] Clasificar pasos: Agregar una columna con una etiqueta para identificar la fase del movimiento a la tabla de datos.  
- [ ] \[Juan José Arias Gallego\] Graficar fases: Generar una gráfica compuesta que superponga la energía de la señal del eje de giro con los picos de levantamiento y sentado.  
- [ ] \[Juan José Arias Gallego\] Actualizar repositorio: Realizar un merge de la rama refactor con la rama main del repositorio.  
- [ ] \[Esteban Guarin Valencia\] Evaluar muestras: Crear una ficha técnica de todas las muestras de video para determinar cuáles son útiles para la segmentación.  
- [ ] \[Esteban Guarin Valencia\] Buscar controles: Buscar datos de controles adicionales en el repositorio de la universidad.

### **Detalles**

**Invitación a la comunidad La Victoria**: Domiciano Rincón abrió una invitación para que los integrantes del grupo asistan a una experiencia el 22 de noviembre por la mañana, con regreso el 26 de noviembre por la noche, junto al profesor Navarro en La Victoria. Mencionó que hay cupo solo para una persona por PDG y que se gestionarán los permisos académicos necesarios con los directores de programa a través del departamento. Juan José Arias Gallego mostró interés en asistir y Domiciano Rincón le indicó que le escribiera por privado para gestionar el proceso con tiempo ([00:00:00](#00:00:00)).

---

**Dificultades en la descarga de datos de la Brigada Santa Marta**: Esteban Guarin Valencia reportó que al filtrar los datos de la Brigada Santa Marta en el sistema Bod utilizando las fechas específicas dadas por Domiciano Rincón (del 24 al 28 de julio), solo aparecían uno o dos datos ([00:01:16](#00:01:16)). Domiciano Rincón se mostró sorprendido, ya que esa información fue la que le compartió Leonardo, y decidió escribirle directamente para consultar el motivo. Esteban Guarin Valencia aclaró que si ampliaba el rango de búsqueda a todo el mes de julio (del 1 al 31 de julio), aparecían bastantes más datos registrados, algunos incluso con video ([00:02:24](#00:02:24)) ([00:05:01](#00:05:01)).

---

**Preprocesamiento de datos e interpolación temporal**: Domiciano Rincón explicó el flujo de trabajo para el procesamiento de señales de movimiento y video. Señaló que las señales de los tobillos permiten calcular variables espaciotemporales como la distancia ([00:03:47](#00:03:47)) ([00:07:12](#00:07:12)). Enfatizó que las muestras podrían no estar distribuidas equitemporalmente, por lo que instó a verificar el vector de tiempo y realizar una interpolación con métodos como Pchip si fuera necesario, dado que la transformada de Fourier exige una tasa de muestreo constante ([00:09:33](#00:09:33)). Esteban Guarin Valencia comentó que en el proyecto anterior filtraban a partir de 3 Hz, a lo que Domiciano Rincón agregó que la dinámica de interés suele durar entre 1 y 2 Hz y sugirió aplicar un filtro paso bajas para suavizar la señal y eliminar el ruido ([00:08:19](#00:08:19)).

---

**Aplicación de la transformada Wavelet para la segmentación de pasos**: Domiciano Rincón propuso remover el componente de corriente directa (DC) a la señal restándole la media, eliminando componentes en 0 Hz, para posteriormente aplicar la transformada Wavelet mediante herramientas como Google Colab, SciPy y Cloud Code ([00:10:35](#00:10:35)). Explicó que esta técnica permite detectar cambios grandes o "codos" en la señal para realizar una segmentación precisa a nivel de pasos, lo cual es fundamental para calcular métricas antecedente como el tamaño del paso (distancia recorrida entre paso y paso) ([00:11:35](#00:11:35)).

---

**Análisis del punto central de la cadera (Hip Center) y estimación de velocidad**: Domiciano Rincón detalló que mediante la variable Hip Center se puede observar cómo la persona se acerca a la cámara y que la pendiente de esta gráfica representa la velocidad del desplazamiento al relacionar distancia y tiempo ([00:13:46](#00:13:46)). Precisó que mientras las cámaras permiten calcular la velocidad general del recorrido y la distancia de la zancada gracias a que poseen una referencia fija en el piso, los sensores inerciales (IMU) dificultan este cálculo de distancia por no tener una referencia externa fija, aunque sí permiten medir la velocidad local de cada pierna ([00:17:58](#00:17:58)) ([00:22:38](#00:22:38)).

---

**Limitaciones del sistema de cámaras en la prueba TUG**: Esteban Guarin Valencia y Domiciano Rincón revisaron registros en video de la prueba Timed Up and Go (TUG) y observaron que las cámaras pierden el seguimiento de la persona durante el giro o cuando está muy cerca de la cámara ([00:15:52](#00:15:52)) ([00:18:50](#00:18:50)). Domiciano Rincón concluyó que las cámaras únicas para la prueba TUG sirven principalmente para calcular el tamaño del paso y la velocidad, pero no para registrar los pasos dados durante el giro ni la fase inicial de levantamiento ([00:17:58](#00:17:58)) ([00:22:38](#00:22:38)). En cambio, los sensores IMU capturan el proceso completo al estar fijos al cuerpo del paciente ([00:17:58](#00:17:58)) ([00:19:44](#00:19:44)). Añadió que en el futuro se podrían probar técnicas de visión por computadora como OpenCV o Bounding Boxes para reconstruir los momentos de levantamiento y giro ([00:20:43](#00:20:43)).

---

**División de tareas del equipo**: Domiciano Rincón propuso dividir el trabajo asignando a dos integrantes el análisis de las señales de las cámaras, abarcando el preprocesamiento y la verificación de datos utilizables en la prueba TUG. Esteban Guarin Valencia confirmó la propuesta y mencionó que la parte de segmentación con sensores IMU sería expuesta por su compañero Juan José Arias Gallego ([00:19:44](#00:19:44)) ([00:26:01](#00:26:01)).

---

**Cruzamiento de datos mediante registros de fecha y hora**: Domiciano Rincón y Esteban Guarin Valencia discutieron la posibilidad de cruzar la información de las cámaras en BMO con los datos de los sensores IMU mediante las estampas de tiempo (timestamps) e historial de fechas ([00:23:39](#00:23:39)). Domiciano Rincón advirtió que al ser lugares desatendidos las cámaras pudieron tener desfases en la sincronización de la hora exacta, pero la fecha sirve como referencia suficiente para ubicar las muestras paralelas ([00:24:51](#00:24:51)).

---

**Identificación de la condición de paciente mediante la variable 'patient'**: Ante la duda de Esteban Guarin Valencia sobre la distinción entre pacientes y controles en los datos de las cámaras, Domiciano Rincón aclaró que en el sistema de entrada Motion existe una variable booleana llamada \`patient\` (\`true\` o \`false\`) dentro del formato de cámaras donde se registran los datos demográficos del usuario ([00:24:51](#00:24:51)). Esteban Guarin Valencia indicó que buscaría dicha variable en el sistema ([00:26:01](#00:26:01)).

---

**Limpieza y filtrado de la base de datos de la brigada**: Juan José Arias Gallego presentó el avance en la consolidación de datos dentro de la carpeta \`análisis datos\`, informando que se procesaron 78 archivos JSON de la brigada ([00:26:01](#00:26:01)). Tras aplicar criterios de descarte —como falta de sensores, duraciones muy cortas, pruebas técnicas, duplicados o condición de doble tarea— se obtuvieron 66 grabaciones aceptadas y 12 descartadas, lo que representa un 58% de pacientes válidos (58 pacientes y 8 controles). Toda la información detallada fue exportada a un archivo Excel consolidado ([00:27:28](#00:27:28)) ([00:31:17](#00:31:17)).

---

**Estrategia para el incremento de datos de control**: Domiciano Rincón señaló que se requieren aproximadamente entre 22 y 23 datos adicionales para alcanzar un grupo de 30 controles que permita efectuar pruebas estadísticas robustas ([00:28:57](#00:28:57)). Sugirió coordinar sesiones de toma de datos en el laboratorio con profesores para emparejar los rangos de edad, o aprovechar las próximas brigadas para completar la muestra de control necesaria para el contraste ([00:30:07](#00:30:07)).

---

**Adaptación del algoritmo de segmentación con sensores IMU**: Juan José Arias Gallego explicó la actualización del script \`adaptar esquema JSON\`, diseñado para compatibilizar los nombres de las variables actuales en español (como \`espina base\`, \`derecha\`, \`izquierda\`) con el esquema utilizado en el PDG anterior ([00:32:53](#00:32:53)) ([00:44:20](#00:44:20)). Detalló los canales utilizados: el canal B (giroscopio) para medir la velocidad angular de flexión/extensión en levantamiento y sentado; el canal L (giroscopio X de la espina base) para detectar los cortes de giro; y el acelerómetro del tobillo para identificar el aterrizaje y la energía de cada paso ([00:34:33](#00:34:33)) ([00:42:06](#00:42:06)).

---

**Fundamento físico de la energía y el movimiento en la segmentación**: Domiciano Rincón profundizó en la metodología del algoritmo, destacando el uso de una ventana deslizante (\*sliding window\*) para sumar el espectro y calcular la energía consumida durante cada fase del movimiento ([00:37:07](#00:37:07)). Explicó que al levantarse o sentarse se generan picos de energía en el eje vertical de la espina base, mientras que al girar 180 grados la persona cambia de plano de movimiento (plano XY a Z), lo que genera un pico de velocidad angular perceptible en el giroscopio ([00:38:13](#00:38:13)) ([00:41:08](#00:41:08)).

---

**Resultados de la ejecución del algoritmo de segmentación**: Juan José Arias Gallego mostró las gráficas generadas por el algoritmo, destacando la correcta identificación de los momentos de levantamiento, sentado y giros ([00:44:20](#00:44:20)). Indicó que el algoritmo logró procesar exitosamente 63 de las 66 muestras, fallando únicamente en 3 grabaciones que presentaban vacíos o ausencia de movimiento en los pulsos del tronco. Los resultados finales con los tiempos por fase fueron exportados a un archivo CSV ([00:43:07](#00:43:07)) ([00:52:00](#00:52:00)).

---

**Requerimiento de etiquetado por fases y gráfico compuesto**: Domiciano Rincón solicitó a Juan José Arias Gallego incluir una columna adicional en las tablas generadas para clasificar a qué fase específica del movimiento (\`marcha\`, \`giro\`, etc.) corresponde cada par de pasos (\`swing\` / \`stance\`) ([00:51:01](#00:51:01)). Asimismo, le encomendó generar un gráfico compuesto superponiendo la señal de energía de levantamiento/sentado con la señal de giro y trazando líneas verticales para delimitar visualmente el inicio y fin de cada fase ([00:47:43](#00:47:43)) ([00:54:29](#00:54:29)).

---

**Planteamiento de pruebas estadísticas y Data Augmentation**: Domiciano Rincón planteó que la meta hacia el final del PDG1 es obtener un hallazgo estadístico significativo comparando pacientes y controles ([00:56:33](#00:56:33)). Indicó que la etapa de giro suele ser el mejor predictor para diferenciar a un paciente con Parkinson de un control ([00:48:48](#00:48:48)). Debido al desbalance actual de la muestra, sugirió emplear la prueba T de Welch o realizar un \*data augmentation\* sobre los datos del CSV de controles como solución metodológica temporal mientras se recolectan más datos reales en las siguientes brigadas ([00:56:33](#00:56:33)).

---

**Gestión del repositorio de código**: Juan José Arias Gallego informó que los avances del código y el análisis de datos se encuentran disponibles en el repositorio dentro de la rama \`refactor\`, e indicó que realizará la fusión (\*merge\*) correspondiente hacia la rama principal (\`main\`). Domiciano Rincón felicitó al equipo por los logros alcanzados en el procesamiento de la prueba TUG ([00:55:36](#00:55:36)).

---

**Impacto del aumento de datos en la varianza y estrategia estadística**: Domiciano Rincón explicó que no suelen aplicar técnicas de aumento de datos (\*data augmentation\*) en observaciones de campo de personas debido a que la repetibilidad de los experimentos no es totalmente idéntica (ejemplificándolo con la variabilidad al hacer una firma), por lo que aumentar datos sobre muestras de alta repetibilidad sesga estadísticamente la muestra y evita que la varianza aumente o se disperse ([00:58:56](#00:58:56)). Domiciano Rincón indicó que la técnica servirá como un recurso temporal hasta contar con buenos datos; si al finalizar el proyecto no se tienen los datos suficientes para realizar estadística de prueba C TD+, se recurrirá a la prueba t de Welch, lo cual es una estrategia adecuada por el momento para el clasificador que se está construyendo ([01:00:20](#01:00:20)).

---

**Criterios para incluir datos externos a la brigada**: Esteban Guarin Valencia preguntó si debía eliminar datos que había descargado por fuera de la brigada, a lo que Domiciano Rincón respondió que no deben descartarse (como muestras tomadas en Valle del Lili) siempre y cuando correspondan al mismo diseño experimental, como la distancia del recorrido y de la cámara ([01:00:20](#01:00:20)).

---

**Evaluación de datos y Ficha Técnica para la segmentación**: Esteban Guarin Valencia mencionó que había descartado datos que carecían de la fase de la persona sentada y que ahora los agregaría, ante lo cual Domiciano Rincón sugirió elaborar una ficha técnica del conjunto de muestras para determinar cuáles sirven y cuáles no ([01:01:30](#01:01:30)). Domiciano Rincón detalló que si se evidencia que en la mitad de las muestras no se calcula la porción de tiempo sentada, esos datos no servirán para segmentación pero sí para evaluar distancias (de paso) y velocidades en las fases de marcha uno y marcha dos ([01:02:36](#01:02:36)).

---

**Búsqueda de controles y datos históricos de sensores IMU**: Esteban Guarin Valencia propuso buscar datos de control en Bod, a lo que Domiciano Rincón estuvo de acuerdo, explicando que la transición entre el sistema de medición anterior y las nuevas IMU fue asumida por el equipo actual, quienes ya tienen el algoritmo adaptado ([01:02:36](#01:02:36)). Domiciano Rincón sugirió verificar si existen datos de las nuevas IMU tomados en Valle del Lili previos a las últimas brigadas ([01:03:40](#01:03:40)).

---

**Cierre de la reunión**: Domiciano Rincón felicitó al equipo expresando que van muy bien y manifestó su expectativa de obtener hallazgos sobre las variables identificadas en la literatura previa al finalizar el proyecto; posteriormente, los participantes (Esteban Guarin Valencia, Juan José Arias Gallego y Heiner Danit Rincon) se despidieron y Domiciano Rincón le indicó a Juan José Arias Gallego que le escribiera si necesitaba algo ([01:03:40](#01:03:40)).

*Revisa las notas de Gemini para asegurarte de que sean precisas. [Obtén sugerencias y descubre cómo Gemini toma notas](https://support.google.com/meet/answer/14754931)*

*Cómo es la calidad de **estas notas específicas?** [Responde una breve encuesta](https://google.qualtrics.com/jfe/form/SV_5bXzKQfylMIhSXc?confid=nq2RUxVemUd1GlbxhC_wDxISOBEQAjIGCIoCIAAYAQg&detailLevel=longer&hasImages=False&entryPoint=footerMain&isGoogler=False&lang=es-US) para darnos tu opinión; por ejemplo, cuán útiles te resultaron las notas.*

oct 27, 2026

## **Reunión del 27 oct 2026 a las 08:54 GMT-05:00 \- Transcripción**

### **00:00:00** {#00:00:00}

**Esteban Guarin Valencia:** Buenos días, profe.

**Domiciano Rincón:** Buenos días. Buenas, muchachos, una pregunta antes de de comenzar. Hay una brigada de Parkinson que va a suceder en eh creo que la población llama La Victoria. Es con el profe Navarro, todo pago, pues, etcétera, etcétera, etcétera. Y es el día 22 en la mañana y se regresan. Momento, me escribo esto, pero entonces en el 26 en la noche de noviembre eh queda la invitación abierta por si quieren hacer pues digamos que ir y pues digamos como vivir, conocer la experiencia y demás, pero me avisan con tiempo porque también les estaré diciendo a los a los otros PDGs, pues yo tengo cuatro PDGs, entonces a los cuatro los voy a invitar solamente es para una persona. Listo.

**Esteban Guarin Valencia:** Profe,

**Domiciano Rincón:** ¿Alguien lo le suena?

**Juan José Arias Gallego:** Pues sí, profe, la verdad es una ch la idea. Solo tocaría mirar como que se tiene para esa fecha

**Domiciano Rincón:** Okay, okay, okay. Igual cuenten con permisos o cosas y demás.

**Juan José Arias Gallego:** otras materias.

### **00:01:16** {#00:01:16}

**Domiciano Rincón:** Yo sé que pues hay unos exámenes y y ese tipo de cosas, pero pues cuenten con los permisos, igual eh los podemos gestionar desde aquí, desde el departamento con los directores de programa. Eh, solamente sería con tiempo, pero si te suena Juan José, eh, me escribes por interno que yo ahorita lo lo lo puedo gestionar desde ya, mejor dicho, para que, o sea, hay tiempo, hay como un mes, entonces se puede gestionar con tiempo o para que tengamos como todo en orden.

**Juan José Arias Gallego:** Listo. Probaro.

**Domiciano Rincón:** Bueno, muchachos, respecto entonces al al proyecto, ¿cómo vamos? ¿Cómo cómo nos fue de la semana pasada hoy?

**Esteban Guarin Valencia:** Profe, yo sí estaba mirando los datos del Bod, pues para descargarlos y todo.

**Domiciano Rincón:** Sí.

**Esteban Guarin Valencia:** Y pues estaba mirando pues la los de la Brigada Santa Marta, pues para descargarlos y pues para cuando yo coloqué solamente digamos las fechas que había dado su nombrado, no solamente apareció como un dato. Bueno, dos.

**Domiciano Rincón:** Es que raro, en serio.

**Esteban Guarin Valencia:** Sí, profe,

**Domiciano Rincón:** Eh,

### **00:02:24** {#00:02:24}

**Esteban Guarin Valencia:** que es del 24 al 28 en julio,

**Domiciano Rincón:** no puedo preguntar.

**Esteban Guarin Valencia:** ¿cierto?

**Domiciano Rincón:** Eh, ya te digo, lo que está en el grupo, literalmente lo que está en el grupo lo escribí el día que me reuní con Leonardo. Leonardo me mostró pues como todos los datos.

**Esteban Guarin Valencia:** Mira que solamente me aparecen estos dos.

**Domiciano Rincón:** Va a preguntar directamente entonces a Leonardo. Vamos.

**Esteban Guarin Valencia:** Pues si yo lo pongo en todo lo todo el rango de julio,

**Domiciano Rincón:** Está ahí, ¿no?

**Esteban Guarin Valencia:** ahí sí aparecen más.

**Domiciano Rincón:** Creo que se fue. Sí, se perdió. ¿Qué es, muchachos? Eh, a ver, le voy a preguntar entonces a Leonard. Eh, hola León.

**Esteban Guarin Valencia:** Ahí estoy presentando pantalla de lo que se ve, profe,

**Domiciano Rincón:** Vale, vale.

**Esteban Guarin Valencia:** si es que estoy haciendo algo mal o lo estoy mirando donde no es

**Domiciano Rincón:** Me recorda las fechas. Eh,

**Esteban Guarin Valencia:** del 24 al 28 de julio, me parece.

**Domiciano Rincón:** eso le pregunté Leonardo igual íbamos como que lo o sea en la exploración nos salió eso, o sea, no tenemos nada ningunos datos sino esos.

### **00:03:47** {#00:03:47}

**Esteban Guarin Valencia:** Sí, profe, pues aquí solamente aparecen pues igual yo pues estuve mirando otros datos, ¿no? pues para descargar y no quedarme con eso y estuve mirando revisando si concordara y todo eso.

**Domiciano Rincón:** otras fechas. A ver,

**Esteban Guarin Valencia:** Es igual.

**Domiciano Rincón:** ahí ya le pregunta apenas me contesta les digo para que lo para que lo podamos buscar. Igual yo creo que me veo ahorita. Ah, no, ahorita no. Hoy es hoy es martes. Es que, o sea, el lunes tan largo que pareciera miércoles. Yo me veo con él el miércoles, pero bueno, igual digamos como que lo que podemos hacer, o sea, hay digamos como que todavía un trabajo largo, por decirlo así, que nos podemos, digamos, enfocar directamente en en IMU, pues eh y sacar, digamos, como todos los algoritmos posibles utilizando sensores de movimiento y pues nada, digamos, como que con el tema de cámaras al menos vemos la la weightform, ¿no? La cómo decirlo el gráfico, la onda. Entonces, uno más o menos puede saber pues cómo es el recorrido, el algoritmo de segmentación en esa en ese pues en esos gráficos es mucho más fácil, ¿no?

### **00:05:01** {#00:05:01}

**Domiciano Rincón:** pues porque literalmente es una cámara que está observando todo el tiempo al paciente, porque los levantamientos son más, digamos, o sea, hay un punto de referencia eh fijo en el piso, lo que hace que pues los puntos de levantamiento sentado y giro, pues se noten superb. Entonces, nada, digamos como que la idea es eh al menos con la estructura del del de la de las cámaras se puede hacer algo, ¿cierto? O sea, que cuando lleguen las demás muestras, lo más probable es que se pueda hacer lo mismo, ¿cierto? Eh, yo de todas maneras, a ver, eh, no me quiero quedar con la duda, que no no me contestó allí, eh, Leo, eh, voy a intentar iniciar sesión, pues, y buscarlo. Pues igual creo que están entrando con mi mismo con mi mismo mail. Lo que pasa es que a veces le bajamos los permisos para que ustedes pudieran entrar.

**Esteban Guarin Valencia:** Sí, profe.

**Domiciano Rincón:** Eh, voy a buscar en todo, Julio, por si acaso, como del primero al 31\. A ver qué tal.

**Esteban Guarin Valencia:** Pues Desde primero al 31 de julio aparecen bastantes.

### **00:06:02**

**Esteban Guarin Valencia:** Pues yo sí descargué algunos de esos,

**Domiciano Rincón:** Okay.

**Esteban Guarin Valencia:** pero pues no sé si sean de la brigada o no, pero puede ser.

**Domiciano Rincón:** O sea, sí, cuando, o sea, cuandoamos como cuando en el tiempo, Sí, claro, ahí estoy mirando uno, o sea, si lo pongo del primero al 31 de julio, el primer registro de la página dos tiene hasta video y todo. Eh,

**Esteban Guarin Valencia:** Ok.

**Domiciano Rincón:** ¿quieren? Comparto un momentico, pues, y creo que de alguna forma, digamos, como que nos podemos desestancar si le aplicamos eh de una vez, digamos, como una una técnica de segmentación a cualquiera de los videos. Nuevamente ese esa segmentación es super precisa porque es con cámara. Los únicos cuidados. Ya ya les voy a decir qué técnicas deberíamos utilizar, que deberíamos poder utilizar. Pues eh, a ver, ¿ves? No me sale para compartirte, pero un momentico que

**Esteban Guarin Valencia:** Yo creo que creo que hasta en un video via vía Navarro

**Domiciano Rincón:** Okay, okay, okay. Eh, window, window, entire screen.

**Esteban Guarin Valencia:** Pero

### **00:07:12** {#00:07:12}

**Domiciano Rincón:** Ajá. para compartir. Listo. Eh, se está viendo, ¿cierto? Bueno,

**Esteban Guarin Valencia:** Sí, profe. Ah.

**Domiciano Rincón:** entonces estos son los esos son los datos e es lo que les decía de los joins, ¿no? Entonces aquí vamos que yo encontrar pues esas esas gráficas, estas gráficas digamos como que e están las gráficas de tobillos. Las gráficas de tobillos en general, digamos, como que nos dicen los pasos, o sea, para hacer las variables ese espacio temporales nos sirve superb. porque esto mide distancia, o sea, no sé si si se interpreta el gráfico correctamente, pero fíjense que aquí nosotros tenemos ah bueno, eh digamos como que el número de elementos es el número de muestras realmente, pero pues seguramente nosotros podemos encontrar la tasa de muestra utilizando pues la el tiempo total del video, el tiempo total de la toma, ¿cierto? Incluso creo que él tiene un vector de tiempo dentro del dentro del Jason. Habría simplemente que verificarlo. No sé de hecho porque no está graficado con tiempo, pero sé que sé que hay vector de tiempo, o sea, independientemente de eso, en el vector de tiempo nosotros tenemos entonces, digamos, como esta línea, ¿cierto?

### **00:08:19** {#00:08:19}

**Domiciano Rincón:** Eh, pero nosotros también tenemos la distancia. Fíjense que si va disminuyendo la distancia, la razón es eh justamente pues porque la persona arranca de forma lejana pues y se va acercando al sensor poco a poco, ¿cierto? A esto hay que hacerle un preprocesamiento. Regularmente el preprocesamiento es hacer un filtro paso bajas, es decir, eh algo que suavice la la señal un poco. Eh hay que encontrar las características frecuenciales para no ir a filtrar algo de nuestro interés. Es decir, tendríamos que filtrar el ruido, el ruido, digamos, como que pues podemos verificar, pero pues nuestra nuestra dinámica, la señal que nosotros queremos nosotros eh observar dura más o menos entre 1 y 2 Hz. Cuando yo digo 2 Hz es porque pues digamos como que hay unas ondas sobre todo en y que eh se repiten dos veces en un segundo. Entonces, si ustedes observan, pues ahí aparecen, digamos, como las personas, ¿cierto? Si se fijaron que hay como unos errores en el tobillo, esos errores al final se pueden filtrar. Si esos errores como son como saltos, saltos de la onda, por ejemplo, un pequeño salto que pudo haber dado de un punto a otro, pero ese salto generalmente se filtra y la señal queda lo más correcta posible, por decirlo de alguna manera.

### **00:09:33** {#00:09:33}

**Domiciano Rincón:** ¿Cierto? Entonces,

**Esteban Guarin Valencia:** Si no estoy,

**Domiciano Rincón:** eh, ¿cómo

**Esteban Guarin Valencia:** si no estoy mal, pues en el anterior proyecto filtraban a partir de 3 heros.

**Domiciano Rincón:** está bien? O sea, puede ser algo algo bueno, digamos, pero digamos como que las características de la de las de las muestras las tenemos que mejor dicho, en el prepamiento que tenemos que tener en consideración. Eh, si quieren lo anotan o si nos está escuchando Gemini, entonces que que sea de esta manera. Las muestras podrían no estar equitemporalmente distribuidas. Eso significa que si, o sea, hay que verificarlo, o sea, simplemente hay que hacer una validación, verificar que el vector de tiempo sí esté correcto, o sea, que sí esté equ temporal, porque donde no llegue a estar equit temporal, hay que hacer una interpolación. La interpolación se logra, por ejemplo, con métodos como P chip, se llama literalmente así, P chip, ¿sí? Entonces, el el digamos que el algoritmo lo que nos va a permitir es calcular un nuevo eje X. Yo le puedo pasar el vector que yo quiera y lo que se va a hacer son unas interpolaciones para encontrar los datos.

### **00:10:35** {#00:10:35}

**Domiciano Rincón:** Pues sí, es decir, vamos a conservar la misma forma de onda y eh los datos, digamos, como que van a eh quedar de forma equitemporalmente distribuida. Sí, eso, ¿por qué? Porque Furier exige esto, o sea, Furier exige que la tasa de muestreo sea constante. Si la tasa de muestreo no es constante, no estamos haciendo nada con Furier. ¿Listo? Ya. Luego, entonces después de hacer ese preprocesamiento,

**Esteban Guarin Valencia:** Yes.

**Domiciano Rincón:** entonces lo que podemos hacer es una pues una transformada. Para la transformada, lo que regularmente hacemos es quitarle el factor DBC, es decir, a la señal original le quitamos la media, ¿cierto? Le quitamos la media y entonces quitamos los componentes en 0 Hz. Eh, sí. Es decir, digamos, como que es lo es lo típico, o sea, cuando tenemos una señal eh compuesta por AC y DC, entonces el DC lo quitamos simplemente restándole la media de la señal completa. Y si ustedes se fijan, esto casi siempre tiene, digamos, como una forma de escalerita, ¿cierto?

**Esteban Guarin Valencia:** H

**Domiciano Rincón:** Esa forma de escalerita representa el eh, ¿cómo decirlo?

### **00:11:35** {#00:11:35}

**Domiciano Rincón:** Eh, pues sí, digamos, como el acercamiento de la persona a la cámara, pero nosotros podemos hacer un filtrado sencillo utilizando eh la transformada wavelet, se llama así, transformada wavelet, o sea, eso ahora antes digamos como que tocaba mejor dicho que leer los libros de Wavel y mejor dicho hacer el superduro en en en técnicas espaciotemporales. Pero la verdad es que ahora eh lo pueden hacer de una forma muy sencilla con Google Colab y con eh, ¿cómo decir? SPI y e cloud Cod. Entonces, pues eso sale de una forma, creo yo, sencilla. Lo único que tienen ustedes que saber es la parte de de de cuál es el criterio de aplicarla, ¿sí me hago entender, o sea, eh se los digo, digamos, es como que nosotros hemos aplicado esa técnica anteriormente dentro de este tipo de de ondas y eh la idea con la transformada web es poder sentir o poder detectar los cambios grandes en la señal. Entonces, por ejemplo, yo podría calcular este codo, por decirlo así. También podría detectar este codo de acá, también podría detectar este codo de acá y al final entonces yo puedo hacer una segmentación también.

### **00:12:48**

**Domiciano Rincón:** Y esa segmentación es es una segmentación a nivel de pasos. Entonces uno puede nuevamente utilizando estas técnicas pues intentar nuevamente hacer la segmentación. Para mí el preprocesamiento va hasta la segmentación, porque luego de la segmentación es donde comienza lo bueno, o sea, es como el trabajo duro, como moler los datos, intentar hacer que que, o sea, como que en el video concuerden los los, ¿cómo decir?, los cortes que nosotros estamos haciendo sobre la señal y ya después de eso, entonces nosotros podemos decir, listo, o sea, ya sabemos cómo cómo actúa la señal, en qué cuáles son los y o cuáles son las cuáles son los cortes adecuados de la señal. Y ya después entonces tenemos los cortes adecuados de las señales. Entonces ya podemos empezar a calcular, por ejemplo, eh tamaño del paso con tamaño del paso me refiero a la distancia recorrida entre paso y paso. Son como ustedes ya han visto en las en los estudios antecedentes, eso es lo que pues como lo mandatorio, ¿cierto? O sea, lo que regularmente pues uno verifica y que pueden haber diferencias significativas entre controles y pacientos.

### **00:13:46** {#00:13:46}

**Domiciano Rincón:** Algo digamos como que no podemos dejar de lado es el hip center. En el hip center ustedes van a encontrar la pues sí, digamos esta es este elemento de acá, uno de los dos. De hecho, ve qué raro. Hip center. Hip center. Eh, tenemos que verificarlo bien porque el hip center regularmente es el centro del muñequito. ¿Listo? Y en el centro del muñequito, pues nosotros podemos encontrar justamente pues que la persona se va acercando. Eso de pronto nos nos eh la pendiente nos puede marcar la velocidad. ¿Listo? Dado que tenemos tiempo y distancia, entonces la pendiente sería velocidad, ¿cierto? Entonces eso es lo que básicamente nosotros tendríamos que hacer. O sea, que si queremos avanzar en en las dos bandas, nosotros lo que tenemos que hacer es lo siguiente. Independientemente de lo de de los datos pues que estén aquí calculados y demás, eh lo que creo que debemos o lo que creo que podemos hacer es ir avanzando en una técnica de segmentación. Esta nuevamente es más sencilla, esta no tiene antecedente, pero sí es más sencilla por el por lo que les comento.

### **00:14:48**

**Domiciano Rincón:** Entonces, el proceso que tendríamos que seguir sería lo que les acabo de decir, el preprocesamiento, verificar que los tiempos sean constantes, sacar la transform formada, verificar las características frecuenciales de esto, hacer probablemente el filtro que que dice que dice Esteban, que es el filtro paso bajas de 3 Hz y luego entonces empezar a verificar cómo podemos hacer la segmentación de la señal. Yo sé que eso pareciera como señales como unas ondas de ruido y demás, pero la verdad creo que nos dice bastante bien eh, pues digámoslo las los cómo decir los los puntos que nosotros estamos intentando medir. Hay que igual verificar esto de eh only swing y pero creo que eso es tema de brazos, no estoy seguro, puede ser de tobillos, pero no lo sé. Pero igual verifiquemos, verifiquemos entonces las señales crudas y verifiquemos de qué manera podemos hacer la segmentación. De hecho, acá yo veo, yo noto pues que no está el TUG, no está simplemente la marcha, pero en el TUG,

**Esteban Guarin Valencia:** Sí, profe.

**Domiciano Rincón:** por ejemplo,

**Esteban Guarin Valencia:** Eh,

**Domiciano Rincón:** Ajá. Ajá.

### **00:15:52** {#00:15:52}

**Esteban Guarin Valencia:** digamos que í hay dos videos que he visto que en todos están. Uno que es solamente la marcha,

**Domiciano Rincón:** Sí,

**Esteban Guarin Valencia:** que es el que más dura,

**Domiciano Rincón:** sí,

**Esteban Guarin Valencia:** y el otro que sí incluye el TUG. Si quieres allí debajo de ese el datico que está ahí debajo,

**Domiciano Rincón:** está acá.

**Esteban Guarin Valencia:** ese sí es el Tug. Normalmente siempre es el segundo que tiene el DTG.

**Domiciano Rincón:** Ah, no, excelente. O sea, les hicieron todas las pruebas. Igual creo que la la ventana que tenemos que verificar es Julio, pero fíjense, o sea, ahí, por ejemplo, lo empezó a capturar. Ah, okay. Este tiene TUG, pero no tiene no tiene ¿Cómo se llama eso?

**Esteban Guarin Valencia:** A veces se demora en cargar, a veces sí demora de cargar el resto, pero creo que sí,

**Domiciano Rincón:** Eh,

**Esteban Guarin Valencia:** ese sí lo tiene.

**Domiciano Rincón:** las gráficas también las va a sacar o qué.

**Esteban Guarin Valencia:** Algunos,

**Domiciano Rincón:** A ver.

**Esteban Guarin Valencia:** la mayoría que he visto tienen gráficas.

### **00:16:37**

**Esteban Guarin Valencia:** A veces se demora en cargar las gráficas y el video, pero siempre los ha tenido.

**Domiciano Rincón:** Okay, okay, okay, okay. Eh, listo. Miremos igual. digamos como que, por ejemplo, una conclusión que podemos nosotros sacar son elementos como, por ejemplo, decir eh los la ventana de la de la cámara, por ejemplo, la ventana, me refiero a qué allá, la ventana de la cámara eh no agarra a la persona sentada. Entonces, si no la agarra sentada, pues nosotros ya sabemos pues que nos podemos esperar, ¿cierto? Por ejemplo, ahí digamos como que la persona incluso está con los con los IMO y demás, ¿cierto? Ahí digamos como que va a ser todo el proceso, por ejemplo, el giro y demás. Si ustedes se fijan la señal, digamos como que se pierde hasta que se vuelve a tomar. Entonces, digamos como que probablemente la información más valiosa que nosotros tengamos acá sea el tamaño de la zancada, ¿cierto? Que igual se puede sacar con las demás con las demás ondas. Eh, y pues digamos como que la idea es pues intentar con algunas gráficas, pero luego digamos podemos por ejemplo concluir con cámaras no es posible el TUG porque el el momento del giro se pierde dado que cuando ya la cuando ya se vuelve a detectar, digamos, como la escalelitización de la persona, ya ha llevado algún tiempo en el giro, si me hago entender,

### **00:17:58** {#00:17:58}

**Esteban Guarin Valencia:** Ne.

**Domiciano Rincón:** pero lo podemos capturar completamente con los IMU, dado que pues están constantemente en el cuerpo de la persona. Entonces, digamos como que uno puede sacar cuáles son las limitaciones de una de un sistema de medición versus el otro. Por ejemplo, nosotros podríamos concluir y decir, vea, las cámaras únicas para este Tugmente nos sirve para calcular el tamaño del paso, que creo que el tamaño del paso está bien. La velocidad, por ejemplo, con la que se mueve. La velocidad, por ejemplo, no la podremos calcular con los imos. Los están allí, ¿cierto? Yo puedo calcular la velocidad local de cada pierna, ¿cierto? pero no la distancia que recorro. O sea, yo puedo hacer una aproximación, pero uf, o sea, es dificilísimo dado que el sensor eh digamos como que no tiene una referencia fija, sino que es literalmente la persona, el cuerpo de la persona. Pero como la cámara sí tiene una referencia fija, yo puedo calcular efectivamente cómo es la velocidad, cuál es la eh la velocidad, digamos, como de la marcha.

### **00:18:50** {#00:18:50}

**Domiciano Rincón:** Eh, puedo calcular los tamaños de los pasos, ¿sí? Es decir, eso eso se puede calcular, pero por ejemplo, ¿qué no se puede calcular? los pasos que la persona da en el giro, porque si ustedes se fijan, la persona se acerca y cuando ya está muy cerca, pues la escalitación se pierde. Fíjense que aquí todavía está en marcha, ¿cierto? Pero no está girando. Aquí perdemos, por ejemplo, los pasos que que hizo para el giro y cuando vuelve a girar en este punto, miren que todavía es queción no está lista, ¿cierto? Justo está aquí en este punto cuando ya han pasado algunos segundos. Entonces, por eso les comentaba que la el el algoritmo de cor, el mejor algoritmo de corte, digamos, de momento, pues está haciendo lo sim, dado que pues lo tenemos en el en el en esta en esta, ¿cómo decirlo? Eh, o sea, está anclado pues a la persona. Este podría ser sencillo si el giro se hiciera delante de la cámara en este punto, pero pues esos son elementos que uno podría concluir posteriormente, ¿no?

### **00:19:44** {#00:19:44}

**Domiciano Rincón:** Vale,

**Esteban Guarin Valencia:** Listo.

**Domiciano Rincón:** entonces nos nos dividimos para esa tarea, es decir, que dos personas se encarguen de analizar cámaras con lo que acabo de decir, con preprocesamiento más verificación de de de qué señales tenemos y qué no dentro del TG.

**Esteban Guarin Valencia:** Listo, profe. Y una cosa es que ahí hay unos donde si se, o sea, literalmente todos está mal la parte del giro,

**Domiciano Rincón:** Ah,

**Esteban Guarin Valencia:** ahí si se pierde por completo,

**Domiciano Rincón:** sí, eso definitivamente es una limitación que tenemos que

**Esteban Guarin Valencia:** pero la parte de sentado hay algunos que si los toman.

**Domiciano Rincón:** concluir. Tenemos que verificar cuántos y cuál es la tasa, por ejemplo, de de de fallo. Eh, o sea, con fallo me refiero, por ejemplo, lo que pasa es que aquí no se ve la gráfica, pero la gráfica tendría que estar, por ejemplo, aquí en este punto, dado que no tenemos esqueletas de punto. Miren que lo empieza a tomar es cuando ya la persona se va medio levantada. Entonces aquí, por ejemplo, el hip center va a tener como un pico de levantamiento, si van a entender hasta aquí.

### **00:20:43** {#00:20:43}

**Domiciano Rincón:** Entonces se queda fijo en ese pico y luego se acerca de una forma un poquito más lenta. Ahí seguramente, por ejemplo, no podemos calcular cuál es el tiempo cero y el, o sea, cuál es el tiempo cero desde que la persona comienza a levantarse hasta el tiempo final. Ya digamos como que uno puede aplicar otras técnicas, por ejemplo, de de video, o sea, por ejemplo, va a ser sí como elementos de video, o sea, va a ser bounding boxes,

**Esteban Guarin Valencia:** Hai

**Domiciano Rincón:** pero probablemente sea pues digamos como un poco malgastar el el tiempo, eh o sea, podemos avanzar lo máximo que podamos con las señales que sí tenemos y ya luego, digamos, como que hacer una reconstrucción de señales se puede hacer luego con otras técnicas de visión por computadora. Sí, por ejemplo, uno puede utilizar OpenC Open CB yo, por ejemplo, podría segmentar la persona, ¿cierto? O sea, eh presentarle varios ejemplos y al final, digamos, como que el OpenC me podría decir cuál es el tronco, cuáles son los brazos, cuál es la cabeza y cuáles son las piernas. Como el tronco se levantó, entonces yo podría llegar y decidir, ya sé cuál es el tiempo uno y el tiempo dos de levantamiento.

### **00:21:42**

**Domiciano Rincón:** Y lo mismo para el giro, o sea, a pesar de que se vea así, eh, digamos como en perspectiva, eh, con OpenC también se puede eh hacer, digamos, como cuando la persona comienza a girar, ¿cierto? Aquí, por ejemplo, se nos saldría de la cámara, probablemente sea una mala muestra, ¿sí? Pero es es básicamente eso. ¿Listo? O sea, tendríamos que, digamos, como que la la información que seguramente nos aporta eh yo hipotizo, pues que es los pasos. Los pasos definitivamente parece ser que sí,

**Esteban Guarin Valencia:** La marcha uno y la marcha dos.

**Domiciano Rincón:** incluso en la marcha uno, la marcha dos, yo creo que podríamos no necesariamente tener, digamos, como una segmentación de cada paso, digámoslo así, sino un promedio, por ejemplo, un promedio de de de de distancia de zancada, un promedio de velocidad, un promedio, por ejemplo, ¿saben qué es muy importante para Parkinson? el tiempo de de doble soporte. Ah, pues ustedes ya lo saben, ¿cierto? O sea, fíjense que aquí la persona, el pie derecho está en el aire, ¿cierto?

### **00:22:38** {#00:22:38}

**Domiciano Rincón:** O sea, aquí en este punto está en el aire y cuando aterriza esa es otra otra fase aquí recién aterrizó. ese tiempo de soporte es un tiempo que uno puede calcular y luego vuelve a volar el zapato yamente. Entonces, uno lo que puede hacer es por cada extremidad poder calcularse, por ejemplo, una eh digamos como unos tiempos de cuánto el zapato duró en el aire, cuánto y cuánto aterrizó. Eso creo que también se puede saber de una mejor forma con los IMU. O sea, igual son complementarios, pero la distancia es algo que no podemos medir con los que seguramente las cámaras la cámara nos ayude. O sea, que por ejemplo uno podría concluir a partir de este primer PDG, uno puede decir, vea, las cámaras solamente nos sirven para medir la distancia de la Sancada y la velocidad, nada más. Y es una buena conclusión porque pues ustedes son los que están verificando los datos, pues qué tanto le podemos sacar a eso. En mi opinión y nuevamente hipotetizando, solamente vamos a poder sacar eso porque la fase no se segmenta, o sea, la persona hace el giro demasiado cerca de la cámara, ¿sí o no?

### **00:23:39** {#00:23:39}

**Esteban Guarin Valencia:** Exactamente.

**Domiciano Rincón:** Lo bueno es que siempre tenía esto, o sea, lo bueno es que siempre tenían estos elementos. Lo otro es que por fecha por por fecha y hora, ¿será que tiene algún tipo de de de relación fecha y hora con los o sea con los IMO, con los datos que tenemos en IMU para poderlos venir a buscar aquí en el en Yeah. ¿Qué? En el en el BMOP, no sé cómo dejar de tomar,

**Esteban Guarin Valencia:** ¿Cómo así?

**Domiciano Rincón:** eh, sí. O sea, como dado que tenemos las fechas en las que se tomaron los IMO, pues probablemente uno pueda también e pues si si por ejemplo la el IMO se tomó el 12 de septiembre, entonces puedo ir a esa misma muestra dentro de BMO para verificar la grabación. ¿Estás entiende lo que quiero

**Esteban Guarin Valencia:** Listo.

**Domiciano Rincón:** decir? O sea, dado que las tomas fueron en paralelo, tanto cámaras como IMOS, las IMOS tienen un time stamp. Eh, pregunto

**Esteban Guarin Valencia:** Ah, sí, laimos que nos habían entregado la Sí, tiene pues la fecha y todo eso,

### **00:24:51** {#00:24:51}

**Domiciano Rincón:** a los datos.

**Esteban Guarin Valencia:** los datos. se podrían como buscar

**Domiciano Rincón:** Entonces uno puede ver eso, uno puede ver complementariamente pues cuáles son los rangos de fecha y entonces venirlos a buscar en en mismo. Cámaras. Lo único con cámaras es que cámara, o sea, como son lugares desatendidos, probablemente las sincronizaciones sucedieron en tiempos diferentes. Eh, nunca ha sido crítico saber exactamente la hora, sino más bien la fecha. Sí. Entonces, algunas muestras seguramente estén, digamos, como eh, ¿cómo decirlo? eh descoordinadas eh o sea, no van a tener exactamente la misma la misma fecha o time stamp, pero pues creo que uno más o menos puede darse como la idea, ¿no?

**Esteban Guarin Valencia:** Claro. Pues otra cosa es que como allí no aparece si es paciente control, entonces pues igual eso no importa por el momento o

**Domiciano Rincón:** No importa por el momento, no importa por el momento. Hay una variable que spent,

**Esteban Guarin Valencia:** listo.

**Domiciano Rincón:** no

**Esteban Guarin Valencia:** Yes.

**Domiciano Rincón:** igual y espent y true o false.

### **00:26:01** {#00:26:01}

**Domiciano Rincón:** Entonces ahí ya lo ya lo saben. Motion en general digamos como que es como el el sistema de cámaras, mejor dicho, es el sistema de entrada. O sea, es ahí en donde se le pregunta como la como todos los datos básicos de la persona, como datos demográficos, o sea, dónde vives, miedad, grupo etario, pues todo eso se pregunta allí. Entonces,

**Esteban Guarin Valencia:** Yeah.

**Domiciano Rincón:** entre otras pues está si es paciente o no. Y la variable se llama patient, es un buling dentro de cámaras.

**Esteban Guarin Valencia:** Es que me parece que la mayoría de datos que que se apcían pues aparecían como en o sea, no aparecía literalmente. Igual voy a intentar buscar la variable ahora que ya sé cuál es.

**Domiciano Rincón:** Listo, listo. Respecto al mismo segmentación de IMO, avanzamos en eso.

**Esteban Guarin Valencia:** Ya, mi compañero Arias te habla más sobre esa parte. M.

**Domiciano Rincón:** Listo.

**Juan José Arias Gallego:** Ya comparto pantal.

**Domiciano Rincón:** Claro.

**Juan José Arias Gallego:** Eh, pues bueno, profe, básicamente lo que hicimos fue reunir en en esta carpeta de análisis datos está el algoritmo de procesamiento.

### **00:27:28** {#00:27:28}

**Juan José Arias Gallego:** Y está la segmentación utilizada en el PD anterior, solo que adapta a los datos de la brigada que nos pasaron, o sea, al nuevo formato J.

**Domiciano Rincón:** es decir,

**Juan José Arias Gallego:** Eh,

**Domiciano Rincón:** est están pasados, están adaptados.

**Juan José Arias Gallego:** Ajá, están adaptados. Entonces, en este documento tenemos como un resumen de del del avance pues del preprocesamiento y las segmentaciones. Eh, básicamente aquí muestran qué contiene pues archo. dice, dice que la grabación participando sensores, eh la frecuencia de sus cuentas,

**Domiciano Rincón:** Sí.

**Juan José Arias Gallego:** bla bla. Mm. Aquí hay una tablita que muestra resultados,

**Domiciano Rincón:** material.

**Juan José Arias Gallego:** pues dice que se analizaron 78 Jason, eh los participantes identificados desde un cariolo, las gracias aceptadas 66 y descartadas dos.

**Domiciano Rincón:** Okay.

**Juan José Arias Gallego:** Y pues aquí hay un resumen de el motivo por el cual se descartaron cada una de las grabaciones. Entonces, hay unas que no cuentan con todos los sensores o hay unas que solo tienen un sensor.

### **00:28:57** {#00:28:57}

**Juan José Arias Gallego:** Eh, también unas que duran muy poco tiempo, eh, unas que son marcadas como pruebas técnicas o de pest. Y también hay otras que están duplicadas y las de condición de doble tarea eran tres.

**Domiciano Rincón:** Okay. Okay. Y en total entonces después de todos los descartes, los datos son los de arriba o o sea,

**Juan José Arias Gallego:** Ajá. Esto de acá.

**Domiciano Rincón:** esos datos son después ya desglose las aceptadas.

**Juan José Arias Gallego:** Ajá.

**Domiciano Rincón:** Okay, okay. 58% está super bien ahí,

**Juan José Arias Gallego:** 66\.

**Domiciano Rincón:** por ejemplo, muchachos o sea eh lo que me contó Navarro pues acerca de la obrigada que les que les estaba comentando ayer en la Victoria es que eh la mayoría van a hacer controles, entonces eh se puede hacer una una toma de datos para mejorar esos datos de control. Si bien nosotros podemos hacer elementos estadísticos y prosterizaciones y elementos, digamos, eh de clasificadores estadísticos, pues con esos 58 pacientes Yeah. Eh, es cierto también que si nosotros necesitamos hacer como pruebas estadísticas severas, pues necesitaríamos un poquito más de controles.

### **00:30:07** {#00:30:07}

**Domiciano Rincón:** Poquito es alrededor de unos 22 23 datos para completar unos 30 en la parte de control. Los controles en general son más fáciles de obtener, es decir, se hace la misma la el mismo proceso de muestra de toma, pero los controles son más sencillos porque eh son personas no diagnosticadas. Si bien uno espera pues que estén pareados por edad, pues uno puede hacer una ronda de de toma de datos en el laboratorio, pues invitamos algunos profes para igualar, digamos, como el grupo de edad, ¿cierto? Pero si ustedes se fijan en los en las edades y bien, digamos, como que hay varios adultos mayores, también hay personas diagnosticadas a partir de los 40 años. Hay personas que les han detectado el Parkinson eh a los 40 años y no son poquitas, o sea, son alrededor unas tres o cuatro personas, o sea, digo, o sea, sí sé que son poquitos, pues, pero no no respecto porcentualmente pues al total de pacientes que hay organizar, digamos, como esa toma o en la brigada definitivamente se pueden terminar de sacar los los pues algunos datos de control como para poder tener un mejor contraste.

### **00:31:17** {#00:31:17}

**Juan José Arias Gallego:** Eh, sí, pues aquí en este caso encontramos que solo hay o y pues pacientes

**Domiciano Rincón:** Okay.

**Juan José Arias Gallego:** 58 que resultan bastantes. Eh,

**Domiciano Rincón:** Los pacientes son los más difíciles de conseguir, o sea, es una buena muestra igual.

**Juan José Arias Gallego:** y pues eh entonces ya este resumen de todos los datos, o sea, lo que hace es exportarlo a un Excel, que básicamente es este y pues identificar la grabación, eh, ¿qué tipo de grabación? es si es de una persona o de una técnica. Eh, hay unos que tienen etiqueta contra el paciente, el sexo, nacimiento, la talla. Eh, este es como el inicio de la de la grabación, la fecha, eh, la duración,

**Domiciano Rincón:** Sí.

**Juan José Arias Gallego:** el número de sensores, eh mínimo de sensores, le habíamos puesto tres, el del la espina base y los dos tobillos, aunque la mayoría cuenta con cinco.

**Domiciano Rincón:** Okay.

**Juan José Arias Gallego:** Eh,

**Domiciano Rincón:** Okay.

**Juan José Arias Gallego:** para identificar los duplicados, pues aquí dice en esta columna se es duplicado de quién, que creo que solo hay tres duplicados a dos.

### **00:32:53** {#00:32:53}

**Juan José Arias Gallego:** Mm. Aquí otro, otro tipo de etiqueta que también marcaba la grabación. Eh, si habían pausas, si es doble tarea, eh, y las observaciones.

**Domiciano Rincón:** Okay. Como la ficha técnica de los datos creo que ya quedaron quedaron super limpios.

**Juan José Arias Gallego:** Ajá. Sí, ya están perfectamente eh identificados y después ya fuimos a la parte de la segmentación, o sea, ya teniendo por el procesamiento y los los datos descartados, las grabaciones descartadas. Eh, entonces hicimos un algoritmo que se llama adaptar esquema Jason porque pues los nombres de las variables en algunos sensores eran diferentes a las utilizadas en el PG anterior,

**Domiciano Rincón:** Mhm.

**Juan José Arias Gallego:** creo que están en inglés y las actuales están en español como espina base, derecha, izquierda Y y pues básicamente intentamos también identificar como la cadena procesamiento de la señal. Es eh ahí está la señal pro del sensor. También identificamos como

**Domiciano Rincón:** es

**Juan José Arias Gallego:** qué eje el sensor se está tomando en cuenta para extraer la señal.

### **00:34:33** {#00:34:33}

**Juan José Arias Gallego:** que por ejemplo en el de la espina base sabemos que es el que el del el creo que es el el eje G que se denomina como G, que es el que identifica como la inclinación giro. Sabemos que después se hace una normalización, después se pasa por un filtro, es el que muestre a tres herz y se aplica lo de energía en ventanas de licentes. Después un promedio móvil y umbral al binario.

**Domiciano Rincón:** Ajá. Ajá. Sí, sí.

**Juan José Arias Gallego:** E y básicamente aquí tenemos como una identificación de las partes de la segmentación y qué sensor y qué canal se utilizó para extraer la señal. Entonces, por ejemplo, en el caso de levantamiento y sentado está que es el canal B y es está identificado como giroscope. Y que envía la velocidad angular de flexión, extensión y básicamente aquí decimos que identifica el levantamiento y el sentado que es el último pulso detectado. los cortes de giro que también utilizan el canal L de la espina base,

### **00:35:52**

**Domiciano Rincón:** Dos.

**Juan José Arias Gallego:** el tensor espina base que está identificado como giros. X eh, y también la parte de caminata de caminata de vuelta, eh, que ahí sí son obtenidos,

**Domiciano Rincón:** Ahí ahí en general se entiende se entiende cuál es el algoritmo de de segmentación,

**Juan José Arias Gallego:** ahí sí ya.

**Domiciano Rincón:** o sea, digamos como que eh sabrían cómo explicarle palabras castizal.

**Juan José Arias Gallego:** Ajá. Sí, es como como y o sea, en parte también lo hicimos para nosotros poder entender el algoritmo segmento del proyecto

**Domiciano Rincón:** Ajá.

**Juan José Arias Gallego:** anterior.

**Domiciano Rincón:** Ajá. ¿Y cuál es,

**Juan José Arias Gallego:** Entonces

**Domiciano Rincón:** o sea, cómo cómo fluye? ¿Qué cuál es el objetivo? ¿Qué hace?

**Juan José Arias Gallego:** eh o sea, ¿te refieres al algoritmo de sentación?

**Domiciano Rincón:** Sí.

**Juan José Arias Gallego:** Sí. O sea, básicamente es que a partir de de la señal de ciertos sensores eh intente identificar picos, por ejemplo, en el caso de del inicio y fin, eh también identificar la caminata de y la camioneta de vuelta.

### **00:37:07** {#00:37:07}

**Juan José Arias Gallego:** Eh, vamos identificando identificando

**Domiciano Rincón:** Sí, digamos como que ahí el ahí el digamos como que el concepto central es el tema de la energía, o sea, sí se fijaron, o sea, esa técnica es fabulosa. O sea, uno digamos como que uno utiliza el sliding window para hacer una sumatoria del espectro. Cuando uno hace la sumatoria del espectro, lo que estás calculando es la energía o la potencia, depende de la característica de la señal. Ah, en este caso, digamos, es la energía. Entonces, dado que nosotros estamos haciendo la sumatoria del espectro eh con una sliding window, la sliding window, digamos, como que se va muestra por muestra. Eh, estamos como haciendo una sumatoria completa de los datos desde el inicio hasta el fin. Entonces, cuando ya llegamos al al final, ¿cierto? Lo chévere es que el rastro que deja es cuánto, o sea, cuánta energía gastó la persona en ese en ese ejer. Entonces, algo bien chévere. ¿Por qué? Porque uno sabe automáticamente, pues que la persona pronto gasta más energía cuando se levanta, ¿cierto?

### **00:38:13** {#00:38:13}

**Domiciano Rincón:** eh al menos digamos como en el eje en el eje y en el eje digamos que que es paralelo a la altura de la persona, por decirlo de alguna manera, a veces donde gasta más energía en ese eje y en el resto no porque pues yo me mantengo más o menos a una energía en una altura estable, digámoslo así. O sea, no gasto energía para bajar el tronco o para subir el tronco. Entonces, por ejemplo, ahí se utiliza el spine base, el eje y pues el eje que va hacia arriba, hacia la cabeza de la persona, justamente por lo que acabo de comentar, porque cuando la persona se levanta es donde gasta más energía. Y entonces hay dos picos en general dentro de esa señal, eh cuando me levanto y cuando me cuando me siento, porque estoy imprimiendo movimiento, estoy gastando energía para poder eh mover esos puntos. Sí, eso es una técnica bacanísima. Lo mismo. el giro, o sea, en el giro lo que se mira es el giro, o sea, el eje de giro e en el eje que va a parerlo también a la a la cabeza de la persona.

### **00:39:09**

**Domiciano Rincón:** Entonces, ese plano, digamos, como que la persona se mueve en un plano, cuando camina se mueve en un plano, digamos, lo el plano XY, pero cuando gira en ese plano, o sea, cuando se mueve en Z, es que ahí se manifiesta el giro. Entonces, se puede, o sea, se puede segmentar dado que la persona se está literalmente cambiando de plano, ¿sí? O sea, entonces pues sí parece que es una técnica avanzada.

**Juan José Arias Gallego:** Eh,

**Domiciano Rincón:** Bueno,

**Juan José Arias Gallego:** pues sí,

**Domiciano Rincón:** a ver,

**Juan José Arias Gallego:** profe, o sea,

**Domiciano Rincón:** continuamos.

**Juan José Arias Gallego:** al inicio teníamos como como esa esa duda y por ejemplo que no siempre se usan todos los ejes, o sea, para calcular la señal, la energía, la señal que, o sea, simplemente en la mayoría se hace uso del del espina base y y un solo eje, o sea, para registrar si hubo eh un cambio o no.

**Domiciano Rincón:** Pero ya ahora sabemos por qué, ¿cierto?

**Juan José Arias Gallego:** Sí, sí, ahora ya queda mucho más claro, pues con con todo el desglose que que se hice.

### **00:40:02**

**Domiciano Rincón:** O sea, lo que lo o sea, lo que lo que hay que verificar allí es es eso, o sea, digamos como entender que el movimiento de la persona sucede en un primero de en un plano, luego ese plano gira y luego el movimiento vuelve a estar en el mismo plano. Eh, la espina base, digamos, como que ahí es mandatoria porque la espina base es la que sufre el cambio de altura cuando la persona se levanta. Entonces, por eso se utiliza espinavase para levantamiento y sentado, que son, digamos, como dos de las fases, ¿cierto?

**Juan José Arias Gallego:** Mhm.

**Domiciano Rincón:** Pero para el giro, para el giro se, o sea, ustedes deben entender que, o sea, digamos como la forma en la que uno modela o mira un giroscopio. Los giroscopios en general miden velocidad angular, entonces digamos como que es raro porque uno se imagina los vectores como flechitas que apuntan a una sola dirección, pero en el giroscopio nosotros tenemos que analizar más bien como que los ejes X, Y, Z. eh pueden rotar sobre su propio eje. Entonces, cuando yo detecto una rotación en un eje, por ejemplo, si yo detecto la rotación en el eje Z, detecto la rotación en el eje X o en el eje Y, ahí yo estoy hablando de la velocidad angular, que es lo que justamente mide el giroscopio.

### **00:41:08** {#00:41:08}

**Domiciano Rincón:** Entonces, en el giroscopio uno puede verificar cuando algo está, o sea, cuando algo rota sobre su propio eje. Entonces, por eso hay un eje particular que solamente se mira en el giro, porque ese eje es el eje que está a ser un eje que es paralelo al plano de movimiento y es el eje que apunta hacia el techo, por decirlo de alguna manera. ¿Cierto? Que pasa es que claro, o sea, aquí pues con las camaritas y con bueno, conversándonos así, digamos como que no es muy visible, pero sí eh es es esa es la razón. Entonces, cuando la persona rota, pues entonces hay un gasto de energía para cambiar el plano, o sea, para cambiar para girar 180 gr, mejor dicho. Entonces, esa energía es la que se detecta para finalmente segmentar el el giro. M.

**Juan José Arias Gallego:** Mm. ¿no? Y y pues digamos que ya identificando giro y y fase inicial y fase final. Entonces, el restante sería la caminata de vida y la caminata de vuelta.

### **00:42:06** {#00:42:06}

**Juan José Arias Gallego:** Pues es lo que tenemos entendido. M.

**Domiciano Rincón:** Exacto, exacto. Sí. Y y con la caminata, por ejemplo, también puede, por ejemplo, ah, bueno, hay unos hay unos ejes que uno, o sea, eso nunca le sacamos el juego que que ameritaba pues en el anterior trabajo, pero hay algo y es que uno también puede detectar cuando la persona hace el el landing, aterrizaje, cada seis golpe que la persona le da al piso cuando aterriza en cada paso, eso también es detectable. Entonces, uno también puede saber, entre otras los tiempos de cada paso. La, o sea, cuánto se demora entre paso y paso también se puede ver, pero no la velocidad completa, o sea, no la velocidad vista desde un observador externo como si puede hacerlo la cámara. O sea, que hay tiempos y elementos que sí se pueden definitivamente sacar y sacarle sacarle provecho.

**Juan José Arias Gallego:** Eh, pues si no estoy mal, creo que aquí la detección de los pasos se hacía por por el el imu del tobillo,

**Domiciano Rincón:** Okay,

**Juan José Arias Gallego:** el exactamente el canal del acelerador

### **00:43:07** {#00:43:07}

**Domiciano Rincón:** okay. Asumo que Ajá, exacto. Me imagino que el acelerómetro ahí es en donde en donde queda presa la energía.

**Juan José Arias Gallego:** Y y pues bueno, básicamente ese sería como un resumen del del funcionamiento de del algoritmo de segmentación.

**Domiciano Rincón:** Okay, lo lo intentaste aplicar.

**Juan José Arias Gallego:** Sí. Eh, entonces hicimos una prueba con una de las grabaciones y pues ya las voy a mostrar por allí.

**Domiciano Rincón:** Listo.

**Juan José Arias Gallego:** En realidad intentamos, o sea, algoritmo de segmentación hay un script en el cual exporta también un SSV, intenta aplicar la segmentación para todas para todas las muestras.

**Domiciano Rincón:** Sí. Okay.

**Juan José Arias Gallego:** El caso es que hay tres muestras que tienen un espacios vacíos, o sea, no detecta como como movimiento en un en un pulso del tronco.

**Domiciano Rincón:** Está como si la persona se hubiera quedado quieta.

**Juan José Arias Gallego:** Entonces, Ajá. como si la persona se hubiera quedado quieta. Entonces, hay tres muestras en las que no termina el de realizar todo el proceso.

**Domiciano Rincón:** Okay.

**Juan José Arias Gallego:** Eh,

### **00:44:20** {#00:44:20}

**Domiciano Rincón:** igual digamos como que son son muchos datos, pero son pocos para hacer una inspección visual esa grafita que mostraste o cualquiera de esas,

**Juan José Arias Gallego:** eh,

**Domiciano Rincón:** esas esas seguramente no sirven.

**Juan José Arias Gallego:** sí. Entonces, espérate entonces, profe, inicio desde desde aquí. Eh, pues lo que te comentaba, este es el algoritmo, esto es un script que básicamente adapta el JSON que teníamos eh para el PD anterior y el que tenemos ahorita.

**Domiciano Rincón:** Ok.

**Juan José Arias Gallego:** Por ejemplo, eh definimos como mapa de sensores, porque por ejemplo tenían sí variaban los nombres, eran diferentes. Fontóal.

**Domiciano Rincón:** Okay,

**Juan José Arias Gallego:** de segmentación no lo identificaba.

**Domiciano Rincón:** está mejorado.

**Juan José Arias Gallego:** Y

**Domiciano Rincón:** Está mejorado. Seguramente han mejorado el algormá

**Juan José Arias Gallego:** básicamente aquí están la parte de levantamiento sentado. El pues lo probamos con esta muestra y nos dio esta gráfica.

**Domiciano Rincón:** increíble. Entonces ahí están y giro, giro lo tenés, o sea, esos son lo reconoces,

**Juan José Arias Gallego:** Eh,

### **00:45:31**

**Domiciano Rincón:** ¿cierto? se hace es como levantamiento y sentado.

**Juan José Arias Gallego:** ajá. Sí, son que son los pues los picos del del sensor

**Domiciano Rincón:** Ah, ya me acordé,

**Juan José Arias Gallego:** en y

**Domiciano Rincón:** me acordé de esto. Sí. Ah, o sea, se saca, se saca la promedio móvil.

**Juan José Arias Gallego:** ahorita tenemos los cortes de giro que también hicimos uso de la misma prueba. Entonces aparece tal que así.

**Domiciano Rincón:** Detección de giros. Okay. Por por qué, o sea, ¿por qué? O sea, ¿será que la persona hizo una sola? O sea, la la forma de onda la ignoro porque es así, o sea, giro uno, giro dos, giro tres, giro cuatro. O sea, la persona hizo dos muestras en una sola toma.

**Juan José Arias Gallego:** Creo, creo que sí, creo que esta es de las grabaciones que tiene Dos,

**Domiciano Rincón:** Uy,

**Juan José Arias Gallego:** dos.

**Domiciano Rincón:** pero a pesar a pesar de eso detecta sin problema, o sea, digamos como que si la señal viene dos, tres, cu c paquetes de señal en la misma cosa, lo es capaz de hacer en toda la detección.

### **00:46:45**

**Juan José Arias Gallego:** Sí,

**Domiciano Rincón:** O sea,

**Juan José Arias Gallego:** si no esa parte nos ha tocado revisarla porque creo que est es de

**Domiciano Rincón:** es increíble.

**Juan José Arias Gallego:** la de una grabación que tiene dos personas o la misma persona dos veces.

**Domiciano Rincón:** Puede ser como la misma persona dos veces. Sí, porque yo veo el pico de Okay, okay. Giros, giro uno, giro dos, giro tres. Bueno, habría habría que revisarlo. Habría que revisarlo. O sea, por ejemplo, uno puede superponer, uno puede superponer la segmentación de, o sea, como hacer una sola gráfica en donde aparezcan dos cosas, en donde aparezcan la, o sea, solamente la gráfica descriptiva del giro, o sea, la energía que gasta en ese en ese eje que les digo, porque ese eje se va, o sea, si ustedes se fijan, dado que la persona eh digamos como que se mueve solamente en un plano, pero se sale de ese plano cuando gira, entonces la señal de giro, o sea, la señal naranjita, pues que que está allí, eh solamente va a presentar un pico en el centro.

### **00:47:43** {#00:47:43}

**Domiciano Rincón:** Entonces, yo puedo superponer o graficar ambas, digamos, cuando la persona está girando ese ese elemento naranja, pues eh cuando la persona, digamos, está girando, pero también puedo graficar el de la espina base e porque pues digamos como que las señales van a ser complementarias, o sea, digamos como que no va a haber mucho ruido visual y yo puedo directamente mostrar cuáles son los rangos de Sí, como los como los rangos de giro, como los rangos de como para tener toda la toda la muestra completa, o sea,

**Juan José Arias Gallego:** Sí, graficar.

**Domiciano Rincón:** generar un gráfico que tenga todos los todos los, ¿cómo decir? en todas las fases.

**Juan José Arias Gallego:** Sí, sí. O sea, graficar la detección de inicio, fin, giros y pues comin y vuelta.

**Domiciano Rincón:** Eso sí, exacto. O sea, si si logramos tener como como toda la señal compuesta, simplemente entonces tendríamos que generar cuántas cuántas líneas eh inicio como inicio, final, o sea, inicio y final del levantamiento, pero el final concuerda con inicio marcha uno. Entonces ahí van solamente dos separaciones.

### **00:48:48** {#00:48:48}

**Domiciano Rincón:** Luego inicio del giro uno, final del giro uno, eh, luego marcha, que es el mismo, o sea, inicio de la marcha, que es el mismo final de giro, y luego levantamiento más sentado y final. Son como cinco o seis líneas, son cinco o seis líneas sobre la sobre la sobre el eje. Podríamos finalizar, digamos, como en eso, pues porque la la la las separaciones ya directamente nos dan los tiempos. Entonces, nosotros podemos hacer un análisis de tiempos, esta vez ahorita sí, a nivel estadístico, y poder de pronto señalar algunas algunos tiempos y por ejemplo en en en eh ustedes creo que fueron los que lo hallaron, ¿cierto? Un taper en donde decía algo como que el giro era como el máximo predictor, como que era el mejor predictor más bien, como que la persona eh con Parkinson o diagnosticada se demoraba definitivamente más en el giro, significativamente más que un control. Eso lo podemos seguramente directamente mirar después de que tengamos como las separaciones completas,

**Esteban Guarin Valencia:** Okay.

**Domiciano Rincón:** pues como un gráfico completo en donde yo tenga los tiempos en los que sucede cada cosa, ¿sí o no?

### **00:49:51**

**Juan José Arias Gallego:** Ajá. Sí, sí, sí, profe. Yo sí. Nosotros habíamos mencionado un paper en el que decía que de los de las etapas de la segmentación más sensibles para para detectar algún alguna diferencia entre control y paciente giro.

**Domiciano Rincón:** Suena super bien, es prometedor, o sea, la verdad es que el algoritmo está funcionando super Madera.

**Juan José Arias Gallego:** Y pues eh esta es la parte de integración de caminatadas. y de vuelta. Eh, pues no, básicamente nos da los tiempos, no hay no hay gráfico.

**Domiciano Rincón:** Okay, okay, okay. Swing stance. Okay. Para cada paso.

**Juan José Arias Gallego:** Sí, para acá pas.

**Domiciano Rincón:** Ahí podríamos ahí podríamos, por ejemplo, meterle una categoría adicional si si lo si lo si lo prefieren. ¿En qué fase se da? Porque el swing stance es para para cualquier par de pasos, pero hay pares de pasos que están dentro del giro. Me hago entender, como ya lo tenemos segmentado o como ya tendríamos los tiempos, pues entonces yo puedo saber cuáles pasos corresponden al giro y cuáles pasos corresponden a la marcha.

### **00:51:01** {#00:51:01}

**Domiciano Rincón:** Obviamente levantamiento y centrada no van a tener pasos, pero podría ser que también que sí. O sea, digamos como que hay muchas personas y muchas formas de levantarse, pero hay personas que dan dos o tres pasos antes de poderse levantar. Y el hecho es simplemente que haya una columna adicional, pues en donde diga ese swing es sans, o sea, ese par de pasos, pues a qué fase corresponden, simplemente es verificar pues en qué fase se encuentran a nivel de tiempo, ¿cierto? Es este Sans está en toda la fase de de de o sea, está dentro del rango de tiempos de la marcha unis. Entonces, ya sé que el paso o el el swing o el stance hace parte, digamos, del del, ¿cómo decir? De la fase de marcha. O también podríamos saber cuáles son los o caracterizar, por ejemplo, los pasos de de giro. ¿Por qué lo digo? Porque por ejemplo, algo que uno también puede hipotizar es el que que el número de pasos para poder dar un giro cambia si eso es contra lo paciente.

### **00:52:00** {#00:52:00}

**Domiciano Rincón:** Y eso puede ayudar bastante también, digamos, a tener algún otro hallazgo. Pueden ser para para el final del PDG1.

**Juan José Arias Gallego:** Listo. Entonces,

**Domiciano Rincón:** Entonces,

**Juan José Arias Gallego:** vamos a tener en cuenta

**Domiciano Rincón:** quizá agregarle, Yemin, por favor, que Juan José agregue una columna adicional con eh un tag que diga a qué pase corresponde el paso que está listando allí en esa tabla.

**Juan José Arias Gallego:** listo.

**Domiciano Rincón:** Ahí se pueden sacar seguramente los promedios.

**Juan José Arias Gallego:** Y pues eh ah bueno, lo que te comentaba, profe, que intentamos aplicar el algoritmo de segmentación para todas las muestras y básicamente se completaron en 63 de 66\.

**Domiciano Rincón:** Y bueno, pues entonces tiene bastante buena pinta, o sea, está s super bien. Claro, o sea, porque

**Juan José Arias Gallego:** Este es como el algoritmo eh con todas las fases incluidas que extrae este CCO. Entonces está la grabación, el tipo de paciente, la persona y aquí están los tiempos por fase. Entonces, inicio, fin, e duración total. Ah, no, espérate.

### **00:53:25**

**Juan José Arias Gallego:** Entonces, tiempo de de levantamiento.

**Domiciano Rincón:** de levantamiento,

**Juan José Arias Gallego:** Ajá. Ida. Eh,

**Domiciano Rincón:** ya que sería la resta de fin menos inicio

**Juan José Arias Gallego:** Ajá. Estos son los pacientes que que no registraban en ese tiempo, que eran tres.

**Domiciano Rincón:** para las muestras que están como dañadas, por decirlo así.

**Juan José Arias Gallego:** Ajá. el los tiempos de los giros y también la vuelta, el inicio y fin,

**Domiciano Rincón:** Okay, okay,

**Juan José Arias Gallego:** el giro dos,

**Domiciano Rincón:** okay.

**Juan José Arias Gallego:** el inicio y fin y el sentado inicio.

**Domiciano Rincón:** Okay, okay. Creo que entonces está segmentado, o sea, eh te pediría solamente ese gráfico, Juan José, o sea, como que para una muestra de entradas y tal cual como lo tienes en el en el en el faderno. Mm. Para una muestra de entrada,

**Juan José Arias Gallego:** Eh,

**Domiciano Rincón:** entonces hacer como el gráfico compuesto. Ajá.

**Juan José Arias Gallego:** ok.

**Domiciano Rincón:** O sea, acuérdate, simplemente necesitamos la gráfica naranjita, o sea, la naranja.

### **00:54:29** {#00:54:29}

**Domiciano Rincón:** Entonces, esa es una, o sea, esa es una que es la que nos muestra como levantamiento y sentado, pero en el centro de las de los dos picos naranjas que se ve en esa misma figura que estamos viendo actualmente, pues en el centro uno puede superponer la del eje de giro, la del eje de giro en y, ¿sí? Es decir, la que utilizamos, o sea, la energía manifestada, pues cuando la persona hace el giro, eh, porque porque está gastando energía cambiando o haciendo la vuelta a 180 gr para poder eh nuevamente caer en el en el en el plano XY sobre el cual se mueve.

**Juan José Arias Gallego:** Listo.

**Domiciano Rincón:** Y entonces si las si las superpongo solamente tendría entonces esas dos gráficas esas dos gráficas superpuestas naranjas que es pues la cómo decir la la energía pues la energía gastada en cada una de las fases y graficar verticalmente pues los los tiempos que se hallaron. Ajá. Eso sí, pues que concuerde, por ejemplo, el tiempo de, o sea, el tiempo de final de marcha tendría que concordar con el tiempo de inicio de de de inicio de marcha, ¿cierto?

### **00:55:36** {#00:55:36}

**Domiciano Rincón:** O sea, debería ser el mismo tiempo

**Juan José Arias Gallego:** Eh,

**Domiciano Rincón:** y quedaría,

**Juan José Arias Gallego:** listo, profe.

**Domiciano Rincón:** ¿no?

**Juan José Arias Gallego:** Igual los avances se pueden consultar

**Domiciano Rincón:** Bueno, eso está avanzado, la verdad. Eso está avanzado. Eso está avanzado. Se pueden hacer unas pruebas estadísticas preliminares. Si bien ocho muestras de control no son tantas, se puede hacer algo mientras se compensa lo en en las siguientes tomas.

**Juan José Arias Gallego:** igual aquí está. Creo que nosotros compartimos el repo e en la rama refactor,

**Domiciano Rincón:** Okay, okay.

**Juan José Arias Gallego:** mejorar identificación personas. Ahí está. Igual yo le voy a hacer merch a la con la con la RAM 1000\.

**Domiciano Rincón:** Al main no está super bien,

**Juan José Arias Gallego:** Ajá.

**Domiciano Rincón:** está super bien.

**Juan José Arias Gallego:** Y pues ahí en la parte de análisis de datos van a estar todos los pues

**Domiciano Rincón:** Qué buen trabajo,

**Juan José Arias Gallego:** la la información.

**Domiciano Rincón:** ¿no? La verdad super buen trabajo, o sea, vamos por camino en esta en esta sección, en esta en esta parte de de Tug.

### **00:56:33** {#00:56:33}

**Domiciano Rincón:** intentemos, o sea, digamos como que mi objetivo pues eh es poder hacer que de aquí a la semana, bueno, la que sea la final para PDG1, podamos hacer algún hallazgo estadístico. Sería genial, sería increíble. Eh, regularmente uno hace pruebas estadísticas de diferencia de grupos, seguramente ustedes las vieron en inferencia estadística. Aquí solamente tenemos dos dos clases que es pacientes y controles. Regularmente uno hace pues prueba Z, prueba T de WH, prueba T de student, ¿sí? O sea, ese tipo de pruebas que es para dos muestra. Por ejemplo, si tuviéramos tres tres tres, ¿cómo decir? clases y yo quisiera verificar, o sea, tres, cuatro o n clases y yo quisiera verificar diferencia entre más de dos grupos, eh la técnica sería la ANOA. que creo que la utilizaron en su momento,

**Juan José Arias Gallego:** Mhm.

**Domiciano Rincón:** pero las otras frases estadísticas son regularmente muy sencillitas. Eh, sí, es decir, es simplemente aplicar un script de Python que hasta se puede pedir con HPT, pero lo importante es tener el criterio de cuál es la que nosotros vamos a aplicar.

### **00:57:39**

**Domiciano Rincón:** En este momento nosotros podemos aplicar probablemente TDW dado que nuestras nuestros grupos están desbalanceados. Eh, entonces y no solamente es balanceado, sino que el grupo de controles puedes puede no ser significativamente eh grande,

**Juan José Arias Gallego:** He.

**Domiciano Rincón:** loentemente grande, por aplicar la prueba que tendríamos que aplicar, que es la prueba Z, ¿cierto? Eh, necesitamos, o sea, estadísticamente necesitamos mínimo 30 datos de control para poder aplicar pruebas Z. Sin embargo, no no importa, por ejemplo, no puede hacer, o sea, hay algo que a mí no me gusta hacer, pero que se puede hacer en este caso, por ejemplo, para poder quedar tranquilos metodológicamente con el con la estadística del de las pruebas y es un data augmentation, pero el data augmentation lo podemos hacer hasta después de postprocesado todo, es decir, como que ese CSV que sacaste, eh, Juan José, eso nos sirve de insumo para poder generar un clúster con más datos y poder ahorita sí analizarlo estadísticamente. Eso es como una pata coja que tenemos de seguro no no nos perseguirá, digamos, aquí al final del proyecto, pero pues como va a haber también brigadas y casi casi todos son controles y demás, algo bacano se puede se puede poder sacar, digamos, se debería poder sacar luego posteriormente, pero mientras tenemos esa pata coja, pues la muleta, nuestra muleta va a ser hacer un detentation en la en la parte de controles.

### **00:58:56** {#00:58:56}

**Domiciano Rincón:** Regularmente nosotros no lo hacemos, muchachos, porque las observaciones que nosotros hacemos en campo son de personas y regularmente, digamos, como que es decir, o sea, la repetibilidad de los experimentos es tan alta que regularmente nosotros haciendo un data augmentation estamos sesgando el grupo para que sea, o sea, para que la varianza no aumente. No, no sé si me explico. O sea, cuando uno eh, por ejemplo, no sé, algo que sea demasiado irrepetible, como por ejemplo, ¿ustedes creen que que ustedes hacen su firma? Ustedes tienen firma esa de de señor, pues esas firmas que son raras y que rayan eh o o su firma es un nombre pero escrito correctamente. Igual puede ser ese tema de la firma. La firma ustedes seguramente no hacen la firma totalmente igual de la todas las veces, o sea, se parece el resultado final puede ser parecido, pero la firma no siempre se hace igual, ¿cierto? O sea, la repetibilidad de ese experimento pues es muy compleja, es es es supercleja. Entonces, eh cuando uno hace un data augmentation sobre una muestra que su repetibilidad se presume es alta, como en este caso, eh lo que yo estoy haciendo al hacer un data augmentation es eh digamos sesgar estadísticamente la muestra de modo que la varianza eh queda autoconenida.

### **01:00:20** {#01:00:20}

**Domiciano Rincón:** La varianza no aumenta con el data augmentation, no se dispersa y lo que yo esperaría con más datos es que se dispersie un poquito más. Sí. Entonces, por eso la técnica va a servirnos como amuleta hasta que tengamos buenos datos. Si al finalizar el proyecto no tenemos los siguientes datos como para hacer el eh estadística de prueba CTD+ás, eh podemos llegar sencillamente hasta TD Welh y esto, digamos, es suficiente, digamos. Ajá. como nosotros estamos haciendo un clasificador, creo que es una es una buena, pues es al menos una buena estrategia de momento. nuevamente es una estrategia que es una muleta, no es la estrategia que tendríamos que seguir con, o sea, si tuviéramos todos los datos y las pudiéramos eh generar hoy mismo.

**Esteban Guarin Valencia:** Listo, profe. Profe, una pregunta, una última pregunta. Eh, lo es que yo antes de aparte de los datos de la brigada, pues como no los había bueno, había descargado otros datos aparte de la de fuera de la brigada, esos los elimino o

**Domiciano Rincón:** fuera de la brigada,

**Esteban Guarin Valencia:** Ja.

### **01:01:30** {#01:01:30}

**Domiciano Rincón:** o sea, tienen video, están en un, por ejemplo, hay muestras que se toman en Valle de Lil sino que pues uno quisiera, ¿no?, pues como eh tener solamente los datos de la brigada, pero si ves que son datos que corresponden a la prueba tal cual como fue tomada la brigada, eh no no hay por qué votarlos. Sí. ¿A qué es lo que me refiero? que si el diseño experimental es el mismo, por ejemplo, si la persona recorre lo mismo, si la cámara más o menos está a la misma distancia que están en las demás muestras de la brigada, no tenemos por qué descartarlo. O sea, lo bueno es que tenemos video, eh, y bueno, el el el seguramente en el video uno se puede dar cuenta si sí o si no.

**Esteban Guarin Valencia:** Listo. Y pues yo hasta el momento había descartado los que no tenían fase, bueno, esa partecita de sentado, pues ahora mismo pues los agregos también,

**Domiciano Rincón:** Sí, yo creo que lo mejor es, por ejemplo, sacar una ficha técnica similar a la que nos pudo haber mostrado Juan José ahorita con los con otros datos y y y decir a a la luz de los datos, esto no nos sirve para segmentar, por ejemplo, esto no nos sirve para segmentar, eh puede ser una una conclusión.

### **01:02:36** {#01:02:36}

**Domiciano Rincón:** Ahora, esa conclusión nos invita entonces a Bueno, entonces las cámaras se tomaron para nada, ¿será que nos sirven para algo? probablemente para la distancia, que era lo que les decía, pero para poder tener el criterio de decir esto no nos va a servir para la segmentación, pues primero habría que sacar una pequeña fecha técnica de de todas las de todo el conjunto de muestras, pues cuál eh cuántas si si toman bien todo y cuántas no. Pues si yo ya veo que casi todas las muestras se mal lograron o que tenemos la mitad en donde no no calculamos o no calcula la la la porción del tiempo en la que la persona está sentada, Entonces solamente nos sirve para las fases de marcha uno y marcha dos a nivel de distancias, pues distancia de paso, distancias, distancias y velocidades.

**Esteban Guarin Valencia:** Listo, profe. Y una cosa respecto con lo de los simos es que digamos como por la parte de controles pues bueno, después de todo lo que hiciste, pues pienso dejarlo así, pero tenía pensado que si podíamos buscar en el Bod pues algunos controles o algunos datos.

### **01:03:40** {#01:03:40}

**Domiciano Rincón:** Podemos hacerlo, o sea, podemos hacerlo definitivamente podemos hacerlo. Dices parao, ¿cierto?

**Esteban Guarin Valencia:** Sí, para lo decimos como para lo de los controles que son más bajitos.

**Domiciano Rincón:** Sí, sí, definitivamente, definitivamente. Lástima, o sea, lástima que los seguramente se van a encontrar con datos de de las IMU viejas, eh, porque pues el el cambio les tocó a ustedes, o sea, como que el cambio, la la transición pues entre un sistema de medición y el otro les ha tocado a ustedes y de hecho pues ustedes ya tienen el algoritmo adaptado, o sea, eso está mejor dicho, marchando super bien porque los anteriores imos sí habían durado más o menos unos 2 años y medio en en campo pues tomando muestra. Estos nuevos pues ya con todas las técnicas acomodadas y demás pues son de los que más datos se tiene por las últimas brigadas que se hicieron, pero los anteriores puede ser que tengamos eh datos de pues de las imbus nuevas antes de esa brigada. Hay que comprobarlo. Seguramente fueron tomadas en Valle de Lilo. Puedes buscarlo y y y pues sí llegará a la conclusión de si sí o si no.

**Esteban Guarin Valencia:** Listo, profe. Muchas gracias.

**Domiciano Rincón:** Bueno, muchachos, no a ustedes, muchas gracias. Vamos, vamos muy bien, la verdad. Vamos muy bien. Esperemos entonces eh que al final del proyecto entonces podamos tener alguno de esos hallazgos de de de alguna de las variables pues que hemos encontrado en papers antecedentes.

**Esteban Guarin Valencia:** Listo, profe. Muchas gracias. Hasta luego.

**Domiciano Rincón:** Hasta luego. Que est muy bien. Juan José,

**Juan José Arias Gallego:** Muchas gracias.

**Heiner Danit Rincon:** Muchas gracias,

**Domiciano Rincón:** si algo me escribes. Chao. Vamos a ver.

### **La transcripción finalizó después de 01:05:11**

*Esta transcripción editable se generó por computadora y puede contener errores. Los usuarios también pueden cambiar el texto después de que se cree.*