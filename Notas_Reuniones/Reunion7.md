oct 20, 2026

## **Reunión del 20 oct 2026 a las 08:59 GMT-05:00**

Registros de la reunión [Transcripción](https://docs.google.com/document/d/12ttQseRWPcL1auDeiR9Tfp-C2nKdokrIXTIWyG5Kc9k/edit?usp=drive_web&tab=t.pzgp751w1sdh) [Grabación](https://drive.google.com/file/d/1sqUWcD4Ll_nvZTZdIIg5L__yysWC_zYT/view?usp=drive_web) 

### **Resumen**

Revisión de cronograma y metodología y desarrollo técnico y gestión de datos

**Ajustes de cronograma y metodología**  
Cronograma ajustado para importar diagramas externos. Metodología enriquecida con diagramas explicativos y enfoque híbrido.

**Procesamiento de datos y objetivos**  
Limpieza de datos completada y objetivos específicos modificados. Algoritmo de corte y procesamiento de JSON acelerados.

**Desarrollo técnico y almacenamiento**  
Extracción de variables biomecánicas priorizada sobre la documentación. Datos anonimizados almacenados en GitHub.

### **Decisiones**

## **Acordada**

* **Integración del cuarto objetivo específico** Se acordó integrar el cuarto objetivo específico con el tercero y enfocar el cuarto objetivo en la validación.  
* **Simplificación de métricas en el objetivo de validación** Se determinó simplificar el objetivo de validación eliminando menciones específicas como puntaje F1 y matriz de confusión para dejar únicamente aptitud y sensibilidad.  
* **Priorización del desarrollo práctico sobre la documentación** Se acordó priorizar el avance del proyecto práctico sobre los ajustes de forma en la documentación del PDG.

### **Próximos pasos**

- [ ] \[El grupo\] Generar ficha técnica: Elaborar una ficha técnica que detalle la cantidad de muestras de cada clase en el conjunto de datos.  
- [ ] \[El grupo\] Verificar equivalencia datos: Comprobar la existencia de correspondencia temporal o de fenómeno entre las muestras de sensores inerciales y las grabaciones de cámara.  
- [ ] \[El grupo\] Finalizar preprocesamiento: Completar el procesamiento y segmentación de las señales de los sensores inerciales.  
- [ ] \[El grupo\] Extraer variables biomecánicas: Seleccionar las variables relevantes para analizar diferencias estadísticas significativas entre los grupos de estudio.  
- [ ] \[El grupo\] Incluir gráfico metodología: Añadir una imagen ilustrativa que represente el flujo del proceso metodológico híbrido utilizado en el proyecto.

### **Detalles**

**Ajustes en el cronograma y diagramación en LaTeX**: Esteban Guarin Valencia presentó el cronograma actual en un formato horizontal y Domiciano Rincón aconsejó generar las imágenes o diagramas de Gantt de forma externa para luego importarlas en LaTeX dentro de una carpeta de imágenes, señalando que la herramienta lo soporta adecuadamente y que el gráfico actual mostraba líneas y rombos inusuales ([00:00:00](#00:00:00)).

---

**Sugerencias sobre la metodología e inclusión de diagramas explicativos**: Domiciano Rincón enfatizó la importancia de incluir un diagrama de flujo o gráfico representativo en la sección de metodología para ilustrar el proceso del proyecto, sugiriendo el uso de inteligencia artificial (como Cloud Code) para generar diagramas en formato SVG, dado que el documento se estaba estructurando con un enfoque excesivamente textual ([00:02:47](#00:02:47)).

---

**Enfoque híbrido de la metodología (CRISP-DM e iterativo)**: Domiciano Rincón detalló que el proyecto debe articular las fases de CRISP-DM para la comprensión y procesamiento de datos con una metodología iterativa para la integración en BIMOP, explicando que tras validar estadísticamente cuáles variables biomecánicas y cinemáticas diferencian mejor a pacientes de controles, se procederá con la integración en el software ([00:06:25](#00:06:25)).

---

**Modificación de los objetivos específicos**: Esteban Guarin Valencia indicó que el cuarto objetivo específico se integró con el tercero respecto al desarrollo, dejando el cuarto enfocado en la validación; ante esto, Domiciano Rincón recomendó no ser tan específico en la formulación del objetivo, manteniendo términos generales como exactitud y sensibilidad, y omitiendo detalles puntuales como la puntuación F1 y la matriz de confusión ([00:10:59](#00:10:59)).

---

**Estado de la limpieza y ficha técnica de los datos**: Esteban Guarin Valencia reportó que se completó el descarte de datos sucios y repetidos mediante un borrador en Google Colab; por su parte, Domiciano Rincón solicitó elaborar la ficha técnica que detalle la cantidad exacta de datos por cada categoría o clase ([00:12:38](#00:12:38)).

---

**Urgencia en el preprocesamiento de señales e imus**: Domiciano Rincón urgió al equipo a acelerar el preprocesamiento de los datos de los sensores IMU e integrar el algoritmo de corte existente durante la presente semana (semana 12), para evaluar la adaptación de las variables ante posibles variaciones en unidades o dispositivos, y evitar retrasos en las fases avanzadas del semestre ([00:14:21](#00:14:21)).

---

**Procesamiento de archivos JSON y sincronización entre IMUs y cámaras**: Esteban Guarin Valencia compartió que desarrollaron un script en Python para procesar los nuevos archivos JSON y visualizar las gráficas; a su vez, Domiciano Rincón propuso verificar mediante marcas de tiempo si existe correspondencia entre los datos de las IMUs y las grabaciones de las cámaras de las brigadas (como la de Santa Marta del 24 al 28 de julio) para decidir si se realiza un análisis conjunto o si se desarrolla un algoritmo de segmentación independiente para cámaras ([00:19:13](#00:19:13)).

---

**Extracción de variables biomecánicas e hipótesis sobre giros**: Domiciano Rincón y Esteban Guarin Valencia conversaron sobre la meta de extraer variables biomecánicas (como la zancada o las características del giro) al finalizar el primer periodo, y someterlas a pruebas de significancia estadística (como la prueba Z con R \< 0.01) para identificar patrones distintivos entre pacientes y controles, tomando como referencia investigaciones previas y las observaciones del profesor Navarro ([00:25:33](#00:25:33)).

---

**Priorización del desarrollo técnico sobre la documentación**: Domiciano Rincón instó al grupo a enfocar la mayor parte de sus esfuerzos en el avance técnico del proyecto y la segmentación de señales, dejando la documentación formal del anteproyecto para las revisiones específicas con el profesor Navarro ([00:31:30](#00:31:30)) ([00:34:09](#00:34:09)).

---

**Gestión y almacenamiento de la base de datos**: Ante la duda de Esteban Guarin Valencia sobre la organización de la información, Domiciano Rincón autorizó descargar y guardar los datos anonimizados dentro de un repositorio privado de GitHub, recordando que los videos pesados de las cámaras se mantendrán accesibles mediante la plataforma asignada ([00:38:31](#00:38:31)).

*Revisa las notas de Gemini para asegurarte de que sean precisas. [Obtén sugerencias y descubre cómo Gemini toma notas](https://support.google.com/meet/answer/14754931)*

*Cómo es la calidad de **estas notas específicas?** [Responde una breve encuesta](https://google.qualtrics.com/jfe/form/SV_5bXzKQfylMIhSXc?confid=FFLqJ8Crqteccw3IaKjFDxITOBEQAjIGCIoCIAAYAQg&detailLevel=longer&hasImages=False&entryPoint=footerMain&isGoogler=False&lang=es-US) para darnos tu opinión; por ejemplo, cuán útiles te resultaron las notas.*

oct 20, 2026

## **Reunión del 20 oct 2026 a las 08:59 GMT-05:00 \- Transcripción**

### **00:00:00** {#00:00:00}

**Domiciano Rincón:** Mucho, mucho que mostrar, ¿cierto?

**Esteban Guarin Valencia:** Pues habíamos quedado con la con la de cronología, la metodología, eh pues habíamos quedado con cambiar un poquito una cosita con los objetivos específicos y pues

**Domiciano Rincón:** La la cronología,

**Esteban Guarin Valencia:** cómo no es

**Domiciano Rincón:** la cronología dijiste que es les pidieron algo así.

**Esteban Guarin Valencia:** que no me el cronograma Sí,

**Domiciano Rincón:** El cronograma. Ok.

**Esteban Guarin Valencia:** exactamente. Para el cronograma pues no esperamos pues que esté actualmente bien, sino es que esperamos pues como ir cambiándolo con sugerencias que vayas a dar.

**Domiciano Rincón:** Eh, ¿lo miramos o qué?

**Esteban Guarin Valencia:** Sí, profe, ya presento pantalla.

**Domiciano Rincón:** Yes.

**Esteban Guarin Valencia:** momento. Ese más o menos sería el cronograma que tenemos actualmente. Pues tuve que separarlo un poquito pues para queera así grande. No hay problema con que quede como horizontal o se pondría vertical.

**Domiciano Rincón:** Eh, no, regularmente no hay no hay problema con eso. Lo que sí es que el diagrama de Gant luce un poquito raro. O sea, mi consejo es hagan la imagen y, o sea, realicen la imagen por fuera e y lo importan.

### **00:01:46**

**Domiciano Rincón:** Eh, o sea, en su su file e látex soporta eso por si acaso. Eh, pues yo sé que ustedes saben, eh, una carpeta images o figures y entonces ahí van poniendo algunas figuras porque el látex no nos, o sea, incluso es bueno porque vamos a arrancar como el como un trag en donde vamos a generar muchas imágenes. Entonces, imágenes pues las vamos a generar y las vamos a poner sobre la sobre el folder pues de del proyecto y entonces allí mismo pues sobre lo que muestran allí en overlift y la idea es pues que uno pueda verificar o visualizar pues eh figuras más acertadas, pero sí, sí, el el diagrama de Guns que muestran allí se ve un poquito raro,

**Esteban Guarin Valencia:** ingres.

**Domiciano Rincón:** o sea, claramente se entiende, pero por ejemplo hay un sí hay unas líneas como raras, hay unos rombitos que no sé si hacen parte pues de Gant específicamente o qué. Pero sí creo que lo pueden pueden apoyarse en una figura diferente. O sea, realmente no hay problema con que la con que la hoja quede horizontal porque pues regularmente esos documentos son son virtuales, pues.

### **00:02:47** {#00:02:47}

**Domiciano Rincón:** E pero si digamos como que uno puede mantener, o sea, digamos como que sí, o sea, uno puede mantener el esquema normal de la hoja respetando pues el diagrama de G normalito.

**Esteban Guarin Valencia:** Aquí tenemos como un poquito las fases que tenemos en el principio. colocamos en las primeras pues lo que ya habíamos hecho como la compresión de problema, marco teórico, pues digamos la reacción pues de documento, la recesión pues de los datos y el descarte y cositas y pues ya el resto lo que sería futuro pues ahí más o menos pues pensé un poquito pues qué es lo que podría hacer, pero pues supongo que eso tocará que modificarlo o cambiarlo.

**Domiciano Rincón:** Miremos e, o sea, el el diagrama el diagrama de G, o sea, antes de revisar esto y quisiera revisar la metodología, ¿cómo la tienen en este momento? Entonces, llegado como a una como a un híbrido, ¿no?

**Esteban Guarin Valencia:** Si con Cris DM y y listo. Aquí tenemos la metodología.

**Domiciano Rincón:** La la metodología sí es sí es super bueno que que le metan figuras.

### **00:04:04**

**Domiciano Rincón:** Eh, hay hay una forma, muchachos, bacanísima de generar figuras, pues si ustedes lo lo prefieren, les gusta y demás y verifiquen a todas estas. Yo sé que se puede eh traerse uno un un PNG y un JPG, pero no estoy seguro de los SBGs, pero eh me he estado pues probando un skill de generación de diagramas de todo tipo NSBG con inteligencia artificial y funciona ultra bien, ultra mega bien, o sea, es increíble. No sé si si lo han hecho alguna vez, pero incluso Cloud Code ni siquiera ya necesita skill. O sea, vos le decís, "Créame un diagrama en SBG." Eh, pero literalmente sería como SBG diagrams, por si acaso, si lo buscan por allí o hacen la skill, eh, sale super bacano. Entonces, les digamos como que les aconsejo eso porque el trabajo en general, digamos, como que también se nutre mucho con imágenes. ¿Sí? Entonces sé que pues lo están haciendo, lo está intentando hacer digamos como muy basado en texto, está super bien. Pues pues también digamos como que hay unos elementos que igual es BG también está en código, pues simplemente sería como hacer la importación y hay que verificar si la TEC lo permite, pero en la metodología, o sea, todo eso para decirles que en la metodología regularmente la metodología siempre lleva una imagen ilustrativa de cómo es el

### **00:05:21**

**Domiciano Rincón:** proceso, cómo es el flujo. Ustedes se han visto que en las metodologías cada vez que uno habla de ellas siempre les presentamos de alguna u otra manera un flujograma. No en forma de diagrama de flujo, sino en forma de gráfico custom, ya digamos como que Cris DM tiene el suyo propio, el iterativo tiene el suyo propio,

**Esteban Guarin Valencia:** Hope

**Domiciano Rincón:** pero la verdad es que al final digamos como que generan unas cosas muy pues pues sí, super buenas, que además se pueden adaptar a lo que a las necesidades que ustedes tienen en el proyecto, o sea, como que la el foco general. Es más, ¿será que lanzo una un grafiquito ahí de de muestra o qué? Y se los mando,

**Esteban Guarin Valencia:** Listo, profe.

**Domiciano Rincón:** eh, pues como por no dejar. A ver, eh, a ver, denme un momentico entonces genero ahí una carpetica rápido, ¿eh? Y miro a ver ese entonces voy a literalmente a decir, a ver, eh, lo que va a decir, digamos, aquí es literalmente lo que lo que tendríamos que tener en nuestro proyecto que va a ser para Cloud Code.

### **00:06:25** {#00:06:25}

**Domiciano Rincón:** Hm. En el en el proyecto generalmente nosotros lo que buscamos es eh seguir las fases de CRDM, ¿no? Entonces, eh quiero un gráfico custom de metodología en SBG eh busque mostrar que estamos eh como decir e haciendo o desarrollo, ¿no? haciendo, no sé, viendo una metodología híbrida entre Pero ustedes ya lo leyeron entonces el CR DN, ¿no es cierto? Cruz DM, básicamente el flujo es entender los datos, eh hacer el análisis y el output pues e eh incluirlo en alguna parte, ¿cierto? Eh, digamos como que dentro de Cris DM normalito, yo lo que esperaría es que una de las fases sea la parte de la de la del desarrollo de software, como digamos como que en algún momento nosotros todos los métodos que hagamos los tenemos que que incorporar pues en en Bimap. Entonces uno puede seguir la parte de datos de Cris DM e iterar dado que nosotros digamos como que vamos a tener, o sea, nosotros hicimos algunas búsquedas de de métodos, pero entonces esos métodos ahora los vamos a probar. Entonces, el primero que vamos a probar lo más probable, eh, ahorita les les pregunto noticias acerca de eso, pero el que el primero teníamos que probar era el divisor de fases.

### **00:07:56**

**Domiciano Rincón:** Entonces, el divisor de fases, listo, nosotros hacemos el script DM, ya entendimos, ya entendimos el negocio, ya entendimos los datos, ya los procesamos. Ahora, el siguiente paso cae en la metodología iterativa en donde nosotros pues intentamos hacer una una integración con con mi mob, ¿cierto? y luego se repite el ciclo cridm. Es decir, nuevamente entendemos los datos, vamos a aplicar otra otra técnica. Eh, por ejemplo, para la vamos a aplicar técnicas para la fase de del giro. Entonces, hacemos las fases del giro, verificamos qué elementos nos dan significancia estadística, qué elementos son adecuados, qué elementos son buenos y luego integramos. No significa que la integración la vamos a hacer este mismo semestre porque pues el ciclo CRISDM pues puede durar todo este primer semestre. tranquilamente porque tenemos dos fuentes de datos que analizar, pero la verdad es que sí, pues digamos como que sí si uno puede encontrar un un mix. Pues literalmente el programa que estoy haciendo ahí es que un gráfico custom metodología NCBG que busque mostrar que estamos haciendo una metodología hbdais DN y eh iterativa iterativa.

### **00:09:02**

**Domiciano Rincón:** Eh en CR DM eh analizamos datos de cámaras GBD. No sé si lo necesita para el gráfico, pero lo voy a poner hacemos el ciclo compondiendo los datos, probando técnicas y aquellas técnicas que nos sirvan para diferenciares y controles técnicas y luego desarrollamos o integramos en BMP. Estas dos últimas fases son desarrollo subiendo metodología iterativa. Listo. Ahí lo voy a poner a trabajar ahí mientras mientras hablamos. Pero sí, eso es básicamente lo que lo que nosotros entonces debemos hacer. A ver, entonces dice el proyecto aborda a las de exploración, procesamiento, seguimiento DM. Ajá. concebido como un proceso cíclico iterativo, estructuro, bloques funcionales con retroalimentación continua. Todo eso se puede expresar en un gráfico. Eh, posteriormente, una vez los modelos algorítmicos, las variables cinemáticas se encuentran validadicamente. Sí, sí, no. Es decir, digamos, como que no solamente es la validación, sino que lo que vamos a hacer es como una un sometimiento estadístico de cuáles son las mejores variables predictivas para diferenciar pacientes de controles y aquellas que sean las mejores, las que nos den, las que nos ofrezcan un mejor resultado, son las que van a ir integradas en BIMOP.

### **00:10:59** {#00:10:59}

**Domiciano Rincón:** Ese es básicamente pues el pequeño cambio que le haría yo a la metodología. Eh, luego dice, "Posteriormente, una vez los modelos de Ajá, se ejecuta activa." Exactamente. Eh, BMOP se escribiría entonces eh la segunda, el BMO, no sé cuál es, pero BM o P. Sí, sería BMA. BAP. Esta articulación responde comparación del problema. segura si apenas me generé el gráfico. Ya les ya les muestro a ver qué qué sacó. Bueno, entonces es básicamente eso. Listo. Entonces sería como generar un gráfico. me pasé el gráfico, el artificial, entonces se las las las comparte, pero pues no necesariamente es como un primer acercamiento, ¿no? O sea, se va por un programa allí a la carrera. Listo. ¿Qué más? ¿Qué más tenemos? ¿Estás hablando? ¿Estás muteado?

**Esteban Guarin Valencia:** Ya, profe, pues teníamos también que habíamos cambiado los objetivos específicos, pero solamente una cosita con lo de la valiación. No sé si tenemos bien.

**Domiciano Rincón:** Eh, sí.

**Esteban Guarin Valencia:** Listo.

### **00:12:38** {#00:12:38}

**Esteban Guarin Valencia:** Pues lo único es que pues se había acordado que el cuarto objetivo específico pues se integraba con el tercero que es el de desarrollar y el cuarto quedaba como de validar.

**Domiciano Rincón:** Ajá. Desarrollificación capacidad discriminación. Yo pondría métricas de aptitud y sensibilidad, puntaje F1 y matriz de confusión. eh son hacen parte, digamos, como de eso, sino que ya sería demasiado específico, o sea, yo quitaría F1 y matriz confusión, o sea, no las quitaría del trabajo, sino las quitaría de ese objetivo.

**Esteban Guarin Valencia:** Listo. O sea, pues que no quede tan específicos aparte.

**Domiciano Rincón:** Sí, sí, exacto. Si alel vamos a hacer eso, pero pues no necesitamos especificar hasta ese punto. Simplemente esa actitud y sensibilidad está super bien porque pues esas son como las digamos como los valores que nosotros extraemos de un clasificador.

**Esteban Guarin Valencia:** Listo. Y otra cosa, pues como habíamos terminado con los con las sugerencias que había anterior vez, pues terminamos de descartar los datos segundo última reunión, o sea,

**Domiciano Rincón:** Sí.

**Esteban Guarin Valencia:** pese al final que ambos yo pues había modificado un colar para que quede bien mostrado eso como la descarte de los datos.

### **00:14:21** {#00:14:21}

**Domiciano Rincón:** Vale, vale. O sea, quitar los sucios y los repetidos.

**Esteban Guarin Valencia:** Exactamente.

**Domiciano Rincón:** ¿Listo? Entonces, y tenemos ficha técnica de los datos. Es decir, eh confio técnico, me refiero a cuántos de cuánt cuántos de cada clase

**Esteban Guarin Valencia:** Pues digamos que

**Domiciano Rincón:** no lo tenemos.

**Esteban Guarin Valencia:** aquí en Nicolás se podemos ver como los que quedaron al final, pero sí no lo hemos clasificado en sí.

**Domiciano Rincón:** Bueno, bueno, eso, eso lo tenemos que hacer eh para anteayer. Está

**Esteban Guarin Valencia:** Eso está perfecto.

**Domiciano Rincón:** y con Ah,

**Esteban Guarin Valencia:** Y pues no,

**Domiciano Rincón:** sí, sí, dime, dime. Ajá.

**Esteban Guarin Valencia:** no.

**Domiciano Rincón:** e en términos, digamos, como de de procesamiento, de procesamiento, ¿qué en qué más hemos avanzado? O sea, estamos involucrando el algoritmo de corte, eh lo hemos probado con las muestras, ¿cómo nos ha ido con eso?

**Esteban Guarin Valencia:** No, profe, no hemos casi avanzado como la parte de clasificación.

**Domiciano Rincón:** O sea, esa no sería clasificación, sino sería realmente un preprocesamiento, que es como la fase en la que nos encontramos, ¿sí?

### **00:15:43**

**Domiciano Rincón:** Es decir, digamos, como que en el preprocesamiento nosotros tenemos que poder, ¿sí?, es decir, digamos, como que dado que nosotros tenemos pues ya los datos y tenemos como un algoritmo preliminar eh dejado por por el anterior grupo, validada además por pues por todo trabajo de 2 años en donde sabemos pues que la distribución de energía en el tiempo es la forma correcta de analizar el problema. Eso también tendría que poderse incorporar, no nos demos sino más allá de una semana, muchachos. Estamos en la semana 12, ya estamos cerca del final del semestre, o sea, estamos a un mes más o menos. Eh, yo creo que sí es bueno que pues que sí, o sea, que podamos tener en consideración eso, ¿vale? Eh, ¿por qué?

**Esteban Guarin Valencia:** St.

**Domiciano Rincón:** porque ahí se nos va a estar ya seguramente el algoritmo con ciertas partes. Vamos a necesitar saber eh cuál es el, o sea, el los análisis que les había pedido desde, bueno, la última vez que nos vimos, que es verificar eh o sea, es el mismo sensor, pero puede ser que los sensores estén orientados de una forma distinta o que las variables se llamen diferente.

### **00:16:52**

**Domiciano Rincón:** Entonces, nosotros necesitamos adaptar el algoritmo para que funcione con eso, con esas variables. O sea, independientemente de que sea un sensor diferente o un dispositivo electrónico diferente, se está midiendo lo mismo. Entonces, puede que cambien las las, ¿cómo se llama?, las unidades de medición. Puede que cambien, puede que cambie ciertas, pero lo que no va a cambiar, por ejemplo, son las formas de onda, ¿sí? O sea, una persona se para, camina, eh da la vuelta y tan, tan, todo eso es igualito porque va a estar en los mismos puntos en los que eh inicialmente nosotros hicimos el diseño experimental. Entonces, hay que hacer ese match entre los datos que eh o los gráficos o los eh algoritmos que había dejado el anterior grupo versus los datos que en los que está tomado su dataset. Entonces, ese preprocesamiento eh urge hacerlo, ¿sí? O sea, es eh ¿Por qué? porque eh es decir, o sea, en el peor de los casos va a dar que el algoritmo hay que refinarlo o rehacerlo. Y entonces cuando nosotros llegamos a ese punto eh denme un momentico, muchachos.

### **00:17:57**

**Domiciano Rincón:** Espera.

**Esteban Guarin Valencia:** Listo. Ok.

**Domiciano Rincón:** Eh, listo, muchachos. Eh, entonces e sí, lo que les decía es en el peor de los casos nos que refinar el algoritmo de de corte. Entonces, el refinamiento del algoritmo de corte pues puede ser uno muy fácil, pero también nos puede tomar mucho trabajo. Entonces, yo no quisiera, digamos, como que solamente hiciéramos algoritmo de corte hasta hasta el final del semestre, porque hay otros estadísticos u otras variables biomecánicas que necesitamos analizar, sobre todo, por ejemplo, eh al menos tocar el el el los Jason de las cámaras. Sí. ¿Por qué? Porque en el Jason de las cámaras uno puede sacar elementos de distancia como por ejemplo zancada, eh tamaño de los pasos, todo eso se puede sacar. Eh, sí. Entonces, o sea, dado que el que que el que que que tenemos dos dos datasets, eh, urge que nos movamos con eso, porque es decir, digamos, como que ya no estamos al principio del semestre, ya estamos hacia el final, eh los digamos como que los el procesamiento puede demorar un poquito y eso para dejarlo en el último semestre está complejo.

### **00:19:13** {#00:19:13}

**Domiciano Rincón:** Para que se hagan una idea, en el último semestre regularmente nosotros hacemos validaciones sobre la semana 12, o sea, por ejemplo, mis trabajos de de grado que están en PDG2 eh ya terminaron, o sea, literalmente ya han terminado. Entonces, yo no quisiera, digamos, como que estuviéramos corriendo contra el tiempo en el segundo semestre. ¿Ustedes planean trabajarle en vacaciones?

**Esteban Guarin Valencia:** Pues si hace falta, sí, profe, o sea, si se podría Ya pues

**Domiciano Rincón:** Pues yo creo que que podría hacer falta, pero pues eso ya es decisión de ustedes porque pues sí es super.

**Esteban Guarin Valencia:** no, profe, pues si toca toca pues en sí lo que se ha hecho es digamos que en el colá que nosotros tenemos es ya tenemos pues para o sea como en los yesos que habías mandado pues tenían como un estilo diferente a los que tenía el semestre pasado,

**Domiciano Rincón:** Exacto, exacto. Sí.

**Esteban Guarin Valencia:** pues se hizo un una un Python para que los pudiera procesar y transformarlo pues a algo más legible y empecé intenté pues hacer como esa

**Domiciano Rincón:** Ese

### **00:20:17**

**Esteban Guarin Valencia:** transformación de para poder ya verificar las gráficas. O sea, que ya es una gráfica de digamos un Jason que nos había mandado,

**Domiciano Rincón:** es un Jason antiguo, ¿cierto? O sea,

**Esteban Guarin Valencia:** ¿no?

**Domiciano Rincón:** es un Jason con el estilo anterior,

**Esteban Guarin Valencia:** de ahora.

**Domiciano Rincón:** es el de ahora. Entonces,

**Esteban Guarin Valencia:** Mm.

**Domiciano Rincón:** eso está hecho, o sea, eso está hecho definitivamente. Lo que necesitamos saber es si, o sea, qué tal es el desempeño de ese de ese algoritmo de corte. Sí. Yo creería que, o sea, nosotros somos, o sea, somos somos son cuatro en el grupo, ¿no?

**Esteban Guarin Valencia:** Sí,

**Domiciano Rincón:** Entonces,

**Esteban Guarin Valencia:** señor.

**Domiciano Rincón:** yo creo que pueden sacar una facción paralela que les ayude a hacer el análisis de cámaras. Eh, ¿por qué? Porque, por ejemplo, sobre todo, me gustaría hacer lo siguiente, creo yo, creo yo, pero no puedo estar seguro porque pues no no no fui a la brigada y es que el algoritmo, dicho, o sea, el algoritmo no, perdón, la toma de datos, la toma de datos de cámara se hizo al mismo tiempo que la ve de si por hora de la de, o sea, si por fecha pues si hora se puede sacar o extraer eh la muestra correspondiente en cámaras y en IMOS, significa que nosotros podríamos tener la la misma observación de fenómeno con dos instrumentos de medición.

### **00:21:36**

**Domiciano Rincón:** Eso es posible, sería brutal porque podemos hacer que de una marcha sacar todo. Sí, pero si no es posible, entonces estaríamos utilizando dos datas diferentes en donde en uno podemos sacar una cosa y en el otro podemos sacar otra. E en cámaras, por ejemplo, no tenemos algoritmo de algoritmo de segmentación. Entonces, eh si la, es decir, o sea, si por ejemplo nosotros analizamos las cámaras y vemos que no encontramos la forma de relacionar la muestra de cámara con la muestra de, o sea, si si si no hemos observado el o si no sabemos cómo e pues sí, digamos referenciar una toma de la otra, significa entonces que nosotros tendríamos que hacer una algoritmo de segmentación propio para las cámaras

**Esteban Guarin Valencia:** H

**Domiciano Rincón:** o en el mejor de los casos, el algoritmo de segmentación se podría incluso mejorar utilizando pues el hecho de que ya tenemos las cámaras. Entonces, la siguiente tarea es verificar si eh o sea, la siguiente tarea pues de de muchas, ¿no? O sea, digamos como que esto eh pues sí es es de es de eh pues probar muchísimas cosas en poco tiempo y es hay que probar si efectivamente eh nosotros para cualquier muestra de IMU tenemos el equivalente en cámara.

### **00:22:55**

**Domiciano Rincón:** del mismo fenómeno. ¿Qué se me ocurre verificar por time stamp? Si tenemos un time stamp semejante, digámoslo así, sería super bueno, pero si ven que no tenemos realmente ese esa forma, digamos, como de observarlo, entonces pues nada, eh habría es que dividir como de alguna u otra manera los dos las dos fuentes de datos y analizarla. unas hacer análisis solamente paraos y hacer análisis solamente para cámaras, pero análisis conjuntos no los podríamos hacer dado que pues no podríamos tener esa esa digamos como ese nexo entre las dos tomas. ¿Se me hago entender?

**Esteban Guarin Valencia:** Profe,

**Domiciano Rincón:** Entonces, hay que verificar eso, pero eso es una verificación pequeña. O sea, si ustedes ven que definitivamente está muy complejo, bueno, pues nada, abandonamos la idea y entonces aplicamos ciertos algoritmos para una o para la otra.

**Esteban Guarin Valencia:** listo. Sorry.

**Domiciano Rincón:** Igual creen que ustedes tienen el acceso a cierto han entrado

**Esteban Guarin Valencia:** la base de datos que habías mandado por WhatsApp.

**Domiciano Rincón:** Sí,

**Esteban Guarin Valencia:** Sí, yo había Sí,

**Domiciano Rincón:** ahí está cámaras.

### **00:24:06**

**Esteban Guarin Valencia:** ahí yo lo revisé, pero pues no he analizado ninguno de esos datos.

**Domiciano Rincón:** ¿Tienen claras las fechas de las brigadas?

**Esteban Guarin Valencia:** No, señor.

**Domiciano Rincón:** Eh, yo creo que lo mandé al grupo, ¿no? Maneras lo va a buscar. A ver, ¿cuándo podría haber sido eso?

**Esteban Guarin Valencia:** Aquí está en la brigada Santa Marta del 24 al 28 de julio.

**Domiciano Rincón:** Eso. Entonces, digamos como que ahí en el buscador ustedes pueden mirar esas muestras y entonces pueden verificar, por ejemplo, si si el si la misma muestra tiene IMO y tiene y tiene cámara, entonces también pueden buscar el nexo por ese lado. Sí. Entonces, hay que responder la pregunta de si efectivamente yo puedo para cualquier muestra de emo puedo tener muestra de cámara y se puede analizar conjuntamente y si no, entonces ya sabemos entonces que el camino va a ser analizar primero y luego cámara de forma independiente.

**Esteban Guarin Valencia:** Ya se llama un algoritmo de cimentación como diferente para el otro.

**Domiciano Rincón:** Sí, pero en cámara es relativamente más sencillo porque en cámara literalmente uno ve la cámara lo que mide, lo que les va a entregar a ustedes es cómo se mueve el joint, es decir, el como la cómo decir, sí, el joint, no sé, no sé cómo decirlo.

### **00:25:33** {#00:25:33}

**Domiciano Rincón:** Eh, muestra como el joint se mueve en el espacio en el espacio tridimensional. Entonces, lo que uno recibe es la distancia, la distancia a la cámara. Entonces, cuando la persona arranca la prueba, está como en la distancia mayor y cuando se levanta, entonces uno puede ver que el spine B se levantó. Entonces, eso gráficamente eh uno lo puede hacer incluso hasta con un filtro de umbral y es relativamente sencillo esa segmentación, o sea, la más compleja es la de la de la de imun y pues bueno, o sea, digamos como que una vez que tengamos esa respuesta, entonces lo que tenemos que hacer es eh hacer un plan de cuáles van a ser las variables biomecánicas que vamos a extraer en este primer en este primer PDG como lo hacían eh o sea, al finalizar el semestre tendríamos entonces que extraer unas variables y la extracción de las variables sería extraer las variables y posteriormente someter eh esas variables a a una verificación de diferencias significativas. Si vemos que son diferencias, si son diferentes significativamente, cualquiera que, o sea, por ejemplo, lo normal es que no sean diferentes, ¿cierto?

### **00:26:45**

**Domiciano Rincón:** Pero los hallazgos son los que sí diferentes. Entonces, cada vez que tengamos un hallazgo, entonces eso nos sirve para e el capítulo de resultados de una vez del trabajo de grado. Yeah. Lo que uno debe hacer es literal ponerse a a digamos procesar las señales, eh sacar los datos eh que podemos ver en papers antecedentes, verificar ante nuestros datos si efectivamente tenemos diferencias significativas entre pacientes y controles para finalmente entonces dar una explicación del por qué son diferentes. Por ejemplo, fíjense que para uno de los PDG2, no sé si conocen a a Jean Paul, a Vidales, a Daniel Mejía,

**Esteban Guarin Valencia:** Sí, sí,

**Domiciano Rincón:** los conocemos e y el otro es Andrés.

**Esteban Guarin Valencia:** profe.

**Domiciano Rincón:** Bueno, ellos hicieron lo mismo eh con Pero las pruebas que ellos están analizando son unas pruebas eh de a mano alzada, digamos, dibujo a mano alzada y las personas lo que dibujan son relojes y cubos, literal relojes y cubos. A eso es una prueba eh de cognición, pues que se llama Moca eh o bueno, parte de de ellas, pues.

### **00:27:54**

**Domiciano Rincón:** Entonces, lo que es muy interesante es que ellos sacaron una diferencia significativa de algo que me parece increíble y es hay algo que ellos les llaman el cisallamiento y es hagan de cuenta que cuando yo dibujo un cubo, yo lo dibujo un poquito torcido. Eh, bueno, pues se encontró que los pacientes eh dibujan el cubo torcido. estadísticamente más que las que los controles y la diferencia es significativa estadísticamente. Eso significa que ya podemos encontrar un patrón de comportamiento. Literalmente las personas sanas dibujan el cubo más normal que las personas eh enfermadas que o diagnosticadas pues que eh dibujan el cubo un poco torcido.

**Esteban Guarin Valencia:** Ahora sí va a entrar.

**Domiciano Rincón:** Entonces eso digamos como que para poder llegar a eso pues hubo un procesamiento gigante porque pues el cubo, digámoslo así, está, o sea, nosotros no tenemos la señal, nosotros no tenemos el recorrido, sino que únicamente tenemos el dibujo. Entonces, ellos hicieron una técnica en donde pusieron un cubo, un cubo tridimensional y el y entonces encontraban el cubo tridimensional que mejor se ajustaba y luego entonces encontrar el cubo que mejor se ajustaba.

### **00:29:06**

**Domiciano Rincón:** Entonces sobre ese cubo es que se hacía el análisis, ¿sí? O sea, todo una proeza, pues de de de procesamiento de imágenes, señales y y espacios 3D, algo muy muy bacano. Entonces, yo esperaría, digamos, como algo así, teniendo en cuenta pues de que nosotros no tenemos dibujos ni nada, sino que tenemos señales, pero pues tenemos señales en también en un espacio 3D versus algo que acompaña continuamente al paciente, algo así se podrá sacar. Ahora, la idea no fue que no fue nuestra, digámoslo así. O sea, hemos visto cualquier cantidad de papers en donde sugerían que el dibujo se distorsionaba. Ahora, ¿dónde nosotros ya lo hemos encontrado? Asimismo, pues ustedes pueden llegar y decir, "Bueno, no, los pasos del, por ejemplo, a Navarro le interesaba mucho en el en el en TUG1, le interesaba mucho, por ejemplo, el hecho de cuál es la característica acá. de los pasos que la persona da durante el giro. Entonces, eh uno también podría encontrar o uno podría hipotetizar cosas, ¿no? Como por ejemplo, uno puede llegar y decir, el paciente eh da pasos más cortic más y más corticos de más corta duración que un control.

### **00:30:19**

**Domiciano Rincón:** El control yo puedo hipotizar que da dos pasos y listo y ya está girado. Entonces, si uno si nosotros llegamos, por ejemplo, a demostrar estadísticamente eso, eso y que pues la prueba Z nos dé un R menor a 0.01, eso significaría pues que eh hemos encontrado hecho un hallazgo sobre los datos. ¿Sí me hago entender? Entonces, para poder llegar a ese estado de hipotetizar para luego probar, pero basado en la literatura, necesitamos eh pues digamos como que la la diferenciar las fases. Diferenciar las fases definitivamente.

**Esteban Guarin Valencia:** Listo. Sí, profe. Pues más que todo lo que yo he visto los papers y más que todo lo que también nos dijo Navarro Ped hace ya como la semana pasada,

**Domiciano Rincón:** Sí.

**Esteban Guarin Valencia:** me parece es más que todo la parte de los giros que se notaba como esa diferencia que también pues no había recomendado molero motero, pues que investigamos pues losers

**Domiciano Rincón:** Cierto, ustedes me alcaldaron a comentar, creo, la semana antepasada,

**Esteban Guarin Valencia:** Sí.

**Domiciano Rincón:** ¿no? No, eso está super bien, o sea, hay unas cosas muy bacanas, sino que para poder llegar a eso, pues primero uno tiene que hacer el preprocesamiento.

### **00:31:30** {#00:31:30}

**Domiciano Rincón:** Cuando ya hemos acabado el bloque de preprocesamiento, pues el procesamiento ahorita sí es para sacar las variables que que nos interesan, las de molero, no sé qué.

**Esteban Guarin Valencia:** Listo. Entonces, pues lo único pues ya con eso sería ya revisar pues el cronograma para definitivamente ya ver qué cambiamos o no.

**Domiciano Rincón:** Vale, aunque yo, o sea, digamos como que el ese cronograma funciona, o sea, digamos como que el cronograma funciona porque sigue básicamente de por de idea general lo que necesitamos, pero eh no nos centremos tanto en la en la documentación del PDG, digámoslo. O sea, es importante, más adelante se puede ajustar, pero lo más importante es el proyecto en sí. Entonces, digamos, como que podemos estar de pronto pecando de de de de ponerlos al mismo nivel, ¿cierto? La documentación de PDG versus el PDG en sí, pero no, el el el PDG es eh mucho más importante pues el el el hecho, digamos como de de de hacer lo que tenemos que hacer, o sea, resolver el objetivo. Entonces, digamos como que es esos temas de forma pueden esperar.

### **00:32:44**

**Esteban Guarin Valencia:** Listo. Entonces, ya con digamos ya tenemos el algimo pues para procesar los datos que nos hayas mandado.

**Domiciano Rincón:** Sí.

**Esteban Guarin Valencia:** to que ya edifica si ya est este algoritmo pues tanto el de cementación como para bueno es de cementación más que todo pues también sirve para el deb mod y ya comenzar a ver ahí mirar los datos, mirar algunas diferencias, pues también revisar los P reizar si más o menos qué hipótesis podríamos traer más que todo eso.

**Domiciano Rincón:** Exacto, exacto, exacto. Sí, pero digamos como que el objetivo antes como de validar si el algoritmo está bien o no es divid, o sea, el sí como que el debemos concentrarnos en dividir las fases. Eso es. Ahora, si por ejemplo y bueno, vamos como responder la pregunta si podemos tener entonces el equivalente en cámaras de cada uno de las de las de las muestras, sería lo ideal, ¿cierto? Pero hay que igual responderlo porque si la respuesta es sí, o sea, si para cualquier muestra tenemos su equivalente en cámaras, para cualquier muestra en IMO tenemos su equivalente en cámaras, significa que entonces nosotros podemos incluso hacer la segmentación fácil, es decir, podemos trabajar en nuestra propia segmentación utilizando cámaras y eso significa pues que podemos segmentarlo desde sí, es decir, vamos como que con la segmentación de uno la e la puedo traer a la a y que quede mucho más segmentado.

### **00:34:09** {#00:34:09}

**Domiciano Rincón:** Aunque yo presumo y y creo, espero, según lo que he visto, que esta segmentación es es muy precisa. La razón es que los dispositivos están eh puestos directamente sobre la persona, entonces uno puede sentir el la la mínima el mínimo movimiento y por ende uno puede saber la distribución de energía en todo momento. O sea, incluso antes de levantarse, cuando uno hace medio el gesto de levantarse, eso ya está siendo captado por por el por el por los sensores.

**Esteban Guarin Valencia:** Listo.

**Domiciano Rincón:** Pero sí, el objetivo, el objetivo en este momento es segmentar las señales, finalizar el reprocesamiento de de TUG, pues de TUG IMO.

**Esteban Guarin Valencia:** Listo, profe.

**Domiciano Rincón:** Listo. No sé si se nos queda algo más en temas de forma, muchachos. Eso realmente no se preocupen por el tema del cronograma, o sea, en en en contenido está bien, en en forma, digamos, es como que podría cambiar, pero en contenido está bien. Eh, de pronto pues y si eh lo o sea, nuevamente esto no es prioritario, pero lo pueden hacer el tema de que la metodología siempre pongan pues un grafiquito a toda esta yo estaba trabajando y creo que ya terminó un grafiquito pues que sea representativo de su metodología, ¿no?

### **00:35:29**

**Domiciano Rincón:** Esto esto es super bien. Sacó una cosa en un one shot increíble. Ya les voy a mostrar.

**Esteban Guarin Valencia:** Listo.

**Domiciano Rincón:** Ahí no me entendió que era BMO y puso bimok, pero bueno, se entiende lo va a mandar. Pero sí, eso es muy muy lo que nosotros estamos lo que nosotros queremos hacer. Si se fijan en el gráfico, entonces en el CL DM ahí aparecen todos los datos, ¿no? El problema, ¿qué queremos distinguir? Entender los datos, preparar los datos, probar las técnicas y la evaluación. Так. Entonces si todo bien, o sea, si tiene una, o sea, si si es importante para nosotros los datos biomecánicos que se extraen de allí, entonces se pasa al desarrollo y a la integración. Pero sí, tal cual eso es lo que estaba pensando, o sea, si saca unas cosas asombrosas con ese, pero eso lo pueden, o sea, lo pueden mejorar, obviamente o lo deben mejorar, pero sí, e ese es el ese es un skill pues de de de creación de diagramas con Ev.

### **00:36:32**

**Esteban Guarin Valencia:** Listo. Pues ahora pues la otra semana pues me pues ya nos enfoc de aquí en adelante nos enfocarían más que todos en en el no tanto en el documento, mejor dicho, dejar el documento allí a un ladito y comenzar ya toda la

**Domiciano Rincón:** O sea, ustedes miren, volteen a, o sea, eh, piénsenlo como dos tracks. conmigo se reúnen para el proyecto, para el proyecto proyecto, o sea, el proyecto de grado, el que tendría que tener más tiempo de su dedicación y con Navarro se reúnen para el PDG, o sea, elementos de documento. Si Navarro les pide hagan X en el documento, ustedes hacen X.

**Esteban Guarin Valencia:** Listo,

**Domiciano Rincón:** Sí,

**Esteban Guarin Valencia:** ¿no?

**Santiago Gomez Robledo:** M.

**Esteban Guarin Valencia:** El momento pues el documento lo podríamos dejar quieto porque igual con Navarros ya

**Domiciano Rincón:** no están viendo nada más todavía.

**Esteban Guarin Valencia:** no. De hecho, nos vamos a reunir con ella ya dentro de 15 días. La otra semana no nos vamos a reunir con él.

**Domiciano Rincón:** Okay, okay, okay. Eh, Navarro es como el stakeholder principal.

### **00:37:32**

**Domiciano Rincón:** Entonces, digamos, como que lo que él opina acerca del proyecto, pues obviamente es importante. Por ejemplo, él les recomendó un autor que pues siempre ha estado en el tema de TUG, entonces eh pues excelente porque pues es decir, digamos, como que uno lo puede olvidar en su momento, pero pues él eh tiene también la perspectiva completa del del proyecto. Eh, o sea, él ha estado presente en todos los Tug que hemos hecho,

**Esteban Guarin Valencia:** Listo, creo.

**Domiciano Rincón:** pero pues él es el que les da las que tiene que o no en el trabajo. Sí. hay unas revisiones y pues en las revisiones regularmente, digamos, como que es con un con un la primera vez con el con el tutor, yo pues digamos como que le hago el seguimiento e y la segunda es con un segundo lector, pues esa persona tendría que estar clara leerlo, que es lo que ustedes van a a intentar hacer, pero el documento anteproyecto o este PDG1, pues lo que busca responder es cuál es, o sea, ustedes qué van a hacer, eh, qué es lo que tienen presupuesto.

### **00:38:31** {#00:38:31}

**Domiciano Rincón:** estado lograr, eh, pero si ustedes se fijan, no mucho más, o sea, el tema del desarrollo, cómo lo están afrontando, cuáles van a ser los sprints, qué van a ustedes a entregar como valor, todo eso realmente se responde en el PG2. Entonces, lo mejor que podemos hacer es utilizar este tiempo, pues para, o sea, este tiempo me refiero PG1, eh, para avanzar lo más que se pueda, sobre todo Yeah. en fases que son largas pero necesarias, como por ejemplo el reprocesamiento.

**Esteban Guarin Valencia:** Listo.

**Domiciano Rincón:** Está vale, muchachos. Eh, ¿hay algo más que tengamos que que observar? Los dejo para que trabajen

**Esteban Guarin Valencia:** No, sí, ya comenzaremos a presentarlo todo. Esperamos la otra semana entre pues venir con grandes abates.

**Domiciano Rincón:** de una, de una, de una. Listo, listo. Cualquier cosa que necesiten, pues igual ahí tienen el acceso a la base de datos. Recuerden que cámaras no se puede, o sea, el script el el digo el el archivo parece que iba quedaría demasiado grande porque tiene esta video. Entonces, por eso se les ofreció pues el el acceso a la plataforma por este medio. Entonces, pues nada, ahí va a tocar uno por uno con cámara.

**Esteban Guarin Valencia:** No hay problema que nosotros metamos los datos dentro de un Gijad,

**Domiciano Rincón:** ¿Cómo así?

**Esteban Guarin Valencia:** o sea, digamos que nosotros tenemos ahora mismo un Gij donde tenemos todo como almacenado, pues para tenerlo ahí más organizado. Entonces, como no sé si podríamos, digamos, descargar los datos y meterlos dentro del Gu.

**Domiciano Rincón:** es privado. Sí, igual están anonimizados,

**Esteban Guarin Valencia:** Listo.

**Domiciano Rincón:** pero pues sí, digamos como que eviten que el repoale,

**Esteban Guarin Valencia:** Listo, profe. Muchas gracias.

**Domiciano Rincón:** muchachos. Listo, entonces estamos hablando. Muchas gracias. Ciao.

**Esteban Guarin Valencia:** Co?

### **La transcripción finalizó después de 00:40:41**

*Esta transcripción editable se generó por computadora y puede contener errores. Los usuarios también pueden cambiar el texto después de que se cree.*