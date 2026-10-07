sept 15, 2026

## **Reunión del 15 sept 2026 a las 08:58 GMT-05:00**

Registros de la reunión [Transcripción](https://docs.google.com/document/d/1ZiNnkG7djs26KBxmpT8Hzf6XaYtX3YfVLCay2yo_Q2Y/edit?usp=drive_web&tab=t.x9gy133ulzjn) [Grabación](https://drive.google.com/file/d/16iYXJ7CcWex867HaxOcRHC-nf4o_Jlu6/view?usp=drive_web) 

### **Resumen**

Revisión de marco teórico y discusión de literatura con estructuración de variables

**Avance del curso**  
Revisión de entregables pendientes del curso PDG con corrección de documentos.

**Marco teórico**  
Separación de marco teórico y antecedentes con inclusión de referencias bibliográficas.

**Variables analizadas**  
Discusión de variables espaciotemporales y adición de tabla descriptiva.

### **Decisiones**

## **Acordada**

* **Separación del marco teórico y antecedentes** Se estableció la obligación de mantener separados el marco teórico y el estado del arte en el documento de trabajo, requiriendo incluir definiciones clave de la prueba y los dispositivos de medición.

### **Próximos pasos**

- [ ] \[Domiciano Rincón\] Solicitar acceso: Presionar a la persona encargada para obtener los permisos de acceso lo antes posible.  
- [ ] \[El grupo\] Incluir marco teórico: Ajustar el documento para separar el marco teórico del estado del arte e incluir las definiciones solicitadas sobre los dispositivos y pruebas.  
- [ ] \[El grupo\] Enviar documentos: Enviar el documento de anexos al profesor antes de la próxima reunión.  
- [ ] \[El grupo\] Extraer variables: Identificar y extraer las variables significativas reportadas en los resúmenes de la literatura consultada.  
- [ ] \[El grupo\] Crear tabla descriptores: Incluir una tabla en el documento con las variables que presentan diferencias significativas según los artículos consultados, añadiendo la descripción de cada variable y su referencia bibliográfica.  
- [ ] \[El grupo\] Enviar documento actualizado: Entregar el documento con los agregados de variables para revisión antes de la próxima semana.  
- [ ] \[Domiciano Rincón\] Leer artículo: Analizar el artículo sobre pacientes con Parkinson enviado por Esteban Guarin Valencia para identificar nuevas variables de interés.  
- [ ] \[Domiciano Rincón\] Compartir datos: Enviar los datos de Parkinson y control al grupo una vez estén disponibles para iniciar la fase de organización.

### **Detalles**

* **Avance en el curso y estado de entregas**: Domiciano Rincón informó que gestionará el acceso pendiente y recomendó continuar avanzando en los entregables del curso PDG y en el análisis de literatura como insumo inicial para comprender las soluciones previas al problema de estudio. Por su parte, Esteban Guarin Valencia indicó que presentaron el documento en la sesión anterior y que deben realizar las correcciones señaladas, sin que se haya asignado aún un cronograma específico ([00:01:19](#00:01:19)).  
* **Estructura del marco teórico y antecedentes**: Domiciano Rincón señaló que el marco teórico y el estado del arte deben mantenerse separados, corrigiendo la recomendación previa de combinarlos ([00:02:41](#00:02:41)). Domiciano Rincón especificó que el marco teórico debe incluir conceptos generales y definiciones clave como la prueba TUG (\*Timed Up and Go\*), cámaras RGBD y unidades de medición inercial (acelerómetros y giroscopios), empleando referencias de campos como medicina o biomecánica ([00:05:07](#00:05:07)). Asimismo, Domiciano Rincón indicó que los antecedentes deben estructurarse como una línea de tiempo selectiva que abarque desde las pruebas iniciales sin tecnología hasta las intervenciones tecnológicas actuales ([00:16:28](#00:16:28)).  
* **Revisión del documento del marco teórico**: Durante la revisión en pantalla dirigida por Esteban Guarin Valencia, Domiciano Rincón destacó que al tratar sobre la enfermedad de Parkinson, dado que el grupo no es de personal médico, la mayoría de las afirmaciones y juicios de valor deben estar respaldados por referencias bibliográficas, incluyendo datos como la prevalencia de 6.2 millones de casos mundiales o la incidencia de 8 a 18.6 casos nuevos por cada 100,000 habitantes ([00:09:51](#00:09:51)). Domiciano Rincón aclaró la jerarquía de los conceptos en el marco teórico, situando la enfermedad de Parkinson en primer lugar, seguida por el análisis motor, la prueba TUG y los instrumentos de medición ([00:13:11](#00:13:11)) ([00:16:28](#00:16:28)).  
* **Consideración de artículos con aprendizaje automático**: Esteban Guarin Valencia consultó sobre la inclusión de artículos recientes basados en aprendizaje automático. Domiciano Rincón recomendó tenerlos en cuenta para entender los enfoques de los estudios y el tamaño muestral (\$N\$), pero advirtió en contra del uso de aumento de datos (\*data augmentation\*) en señales biológicas por su alta variabilidad, sugiriendo en su lugar alternativas como tratar cada paso individual como una unidad de observación \$N\$ en lugar de la marcha completa ([00:22:36](#00:22:36)).  
* **Variables y diferencias significativas en la literatura**: Esteban Guarin Valencia compartió hallazgos de artículos sobre cámaras optoelectrónicas y cinéticas que muestran mayores diferencias entre pacientes y controles durante la fase de giro. Domiciano Rincón y Esteban Guarin Valencia discutieron variables temporales y espaciotemporales evaluadas en la literatura, tales como el tiempo de doble soporte (\*double support time\*), el tamaño de la zancada (\*stride length\*), la velocidad de marcha (\*walking speed\*), el control en el plano frontal y las excursiones del tronco ([00:28:37](#00:28:37)) ([00:32:40](#00:32:40)). Domiciano Rincón explicó que las unidades de medición inercial permiten medir variables de tiempo (como el tiempo de soporte mediante acelerómetros en los tobillos), mientras que las cámaras RGBD permiten calcular variables espaciales como el tamaño de la zancada ([00:37:38](#00:37:38)).  
* **Uso de tecnologías de captura y herramientas de análisis**: Juan José Arias Gallego mencionó la revisión de artículos que emplean cámaras Kinect y coeficientes de correlación intraclase con valores superiores a 0.90 para evaluar la fiabilidad en pacientes con accidentes cerebrovasculares. Domiciano Rincón aclaró que, aunque comercialmente el sistema Microsoft Kinect está descontinuado, las técnicas y herramientas de análisis de esqueletización corporal siguen siendo útiles para nutrir el trabajo actual ([00:41:04](#00:41:04)). Además, se discutió el uso de Matlab para la extracción de variables cinemáticas ([00:38:47](#00:38:47)).  
* **Análisis estadístico en la literatura y nueva asignación de entregables**: Domiciano Rincón destacó la importancia de reportar pruebas estadísticas y valores de probabilidad (\$p \< 0.05\$ o \$p \< 0.001\$), citando un artículo de la revista MDPI de 2026 evaluado con 38 pacientes con Parkinson y 41 controles que resalta al giro como un descriptor clave en estadios tempranos ([00:44:50](#00:44:50)). Como nueva asignación solicitada por Domiciano Rincón, el equipo debe agregar al documento una pequeña tabla descriptiva de las variables que presenten diferencias significativas en los artículos consultados, la cual incluirá columnas para el descriptor o variable, su descripción y la referencia bibliográfica, con miras a tener el documento listo para la siguiente semana ([00:51:10](#00:51:10)).  
* **Organización de anexos y cierre de la reunión**: Esteban Guarin Valencia indicó que los anexos con las referencias recolectadas se compartieron en el chat de WhatsApp y se colocaron en la descripción del grupo ([00:55:45](#00:55:45)). Finalmente, Santiago Gomez Robledo informó sobre la necesidad de retirarse junto con Juan José Arias Gallego para asistir a un reto de computación, concluyendo la sesión .

*Revisa las notas de Gemini para asegurarte de que sean precisas. [Obtén sugerencias y descubre cómo Gemini toma notas](https://support.google.com/meet/answer/14754931)*

*Cómo es la calidad de **estas notas específicas?** [Responde una breve encuesta](https://google.qualtrics.com/jfe/form/SV_5bXzKQfylMIhSXc?confid=r8Z0F9DKeRarlNnzoYREDxITOBEBMgUIigIgABgBCA&detailLevel=standard&hasImages=False&entryPoint=footerMain&isGoogler=False) para darnos tu opinión; por ejemplo, cuán útiles te resultaron las notas.*

sept 15, 2026

## **Reunión del 15 sept 2026 a las 08:58 GMT-05:00 \- Transcripción**

### **00:00:01**

**Domiciano Rincón:** Eso pues, o sea, yo lo pedí la semana pasada, pues él digamos como que igual está como como en esa tarea, pero entiendo yo que eh tiene como unas prioridades, pues lo que les decía, o sea, para Espiral se nos demoraron como unos 15 días. Ojalá que por ser un tema de acceso, pues eso esté lo más pronto posible, pero pues eh hoy se cumplen pues 8 días, yo lo veo mañana, entonces voy a intentar como presionar ahí para que para que nos lo den lo antes posible, pero igual digamos como que podemos seguir avanzando en el track de la materia, o sea, me refiero a PDG y lo que les han pedido, que seguramente es el tema de de entiendo yo que ya tenían como unos como unas eh como unos entregables, ¿cierto? Y a la par también tenemos que avanzar en el tema de la del análisis de las de las técnicas de la literatura porque pues ese es como el insumo inicial, o sea, al final digamos como que uno se puede dar una muy buena idea. hecho el la semana pasada pues con con el otro grupo, eh creo que ellos ya están bastante bien contextualizados y ha servido bastante el tema de encontrar en la literatura cosas, no para satisfacer la página o las dos páginas que tiene la materia, sino para entrar ya directamente pues en la en la materia e en el en el tema pues del trabajo de grado, pero ya desde un punto de vista bueno de que ha hecho la gente pues para solucionar el problema.

### **00:01:19** {#00:01:19}

**Domiciano Rincón:** Primero, ¿cuál es el problema, no? pues eh que las personas reportan en esos en esos papers. ¿Cuál es la siguiente entrega o qué les han dicho ustedes en PDG? ¿Qué deben entregar?

**Esteban Guarin Valencia:** Pues profe, ayer lo que se hizo fue revisar el documento que teníamos hecho y pues

**Domiciano Rincón:** Ajá.

**Esteban Guarin Valencia:** presentarlo. En sí, ese ya no nos dijeron qué teníamos que hacer después, sino más que todo pues corregir lo que pues nos señalaron que teníamos que corregir y prácticamente eso fue todo. Pues todos allí nos presentamos, nos dijeron que tenías que corregir y eso fue todo.

**Domiciano Rincón:** Okay. Okay. Y dentro del documento que ustedes tienen, tienen marco teórico, porque creo que el anterior grupo me había comentado que les habían pedido un tema como el cronograma, marco teórico, antecedentes, ¿qué es lo que estamos haciendo? Pues eso lo eso lo pidieron

**Esteban Guarin Valencia:** Sí, sí, profe.

**Domiciano Rincón:** y lo tienen y lo tienen desarrollado o o sea ya ya lo hicieron o está o es algo por hacer.

**Esteban Guarin Valencia:** Estamos corrigiendo pues las cosas que nos dijeron que pues tenemos que corregir, pero por la parte del cronograma no no nos han dicho nada de eso,

### **00:02:41** {#00:02:41}

**Domiciano Rincón:** ¿Y qué le dijeron? que tenían que corregir. Yo tengo acceso a ese a ese documento.

**Esteban Guarin Valencia:** ¿eh? No, si quieres ahora lo pasamos más.

**Domiciano Rincón:** Sí, muchachos, yo creo que tengo que ver eso, pero pues no estoy seguro si por ejemplo cuál eh sabemos cuál es la diferencia entre el entre el marco teórico y la y de los antecedentes o el estado del arte, pues.

**Esteban Guarin Valencia:** Pues nosotros pues decidimos combinar tanto el marco teórico como el estado del arte. Vamos tener los dos en el mismo. Ahí ya se lo está mostrando mi compañero.

**Domiciano Rincón:** Sí, sí, sí. Ahí lo ahí lo veo. E y por y cuál es la la justificación de mezclarlos. O se le escucha, se te escucha mal, Santiago, creo.

**Esteban Guarin Valencia:** No se te escucha.

**Heiner Danit Rincon:** Peor.

**Domiciano Rincón:** menos.

**Juan José Arias Gallego:** Eh, pues profe, básicamente nosotros decidimos combinar marco teórico con estado alarte. Creo que ha sido por una recomendación de Navarra en en sí en principio, pero pues sí tenemos diferenciado en qué marco teórico es como los conceptos necesarios para que el lector del documento pues pueda entender eh todo el desarrollo pues del proyecto.

### **00:05:07** {#00:05:07}

**Domiciano Rincón:** Sí,

**Juan José Arias Gallego:** Y ya el estado del arte son estudios relacionados o proyectos que se han hecho relacionados al nuestro. Yeah.

**Domiciano Rincón:** que le puedo preguntar a Navarro si pues hemos abolido el marco teórico. Yo sí creo que tiene que haber marco teórico en cualquier trabajo, ingeniería. e no los podemos mezclar, o sea, responden a a las dos, justamente a las dos cosas que vos acabaste de decir. Sí, creo que uno puede tener como una definición en general, por ejemplo, una descripción completa de la prueba puede ir perfectamente en el marco teórico, pero la descripción de la prueba probablemente para ya cuando el lector lea el estado del arte, pues ya sabe de qué se trata y por ende entonces ya ya podemos hablar todos en un lenguaje común de la prueba, ¿sí? Las fases, por ejemplo, de la prueba, ¿sí? Es decir, es un tema como de coherencia. Entonces, eh debe estar debe estar, o sea, digamos como que pueden ser unos conceptos básicos acerca de lo que se han se han encontrado, digamos, en la literatura, pero pues eh son como justo justo los las definiciones de de las palabras claves que hemos buscado, pues en este caso, por ejemplo, la prueba de TUG o ese assessment, digamos, como que uno lo puede describir.

### **00:06:24**

**Domiciano Rincón:** Obviamente para describirlo tendrán que haber digamos como referencias, pero eso es realmente lo único que los une, ¿no? El tema de las referencias, o sea, que yo para poder definir algo y y tenerlo, digamos, ahí en el marco teórico, pues yo voy a tener que referenciar claramente, pero en el marco teórico nosotros buscamos es justamente lo que lo que dijiste y es responder qué se qué se está haciendo, qué fue lo último que se hizo pues en la historia de la humanidad acerca del problema. Sí, pero pero sí, o sea, digamos como que yo veo muy claro el hecho de que en el marco teórico mínimo tiene que estar la prueba de TUG. Mínimo tienen que estar las cámaras RGBD y mínimo tienen que estar los sensores, los acelerómetros y giroscopios, o sea, los los las unidades inerciales en general. Entonces, sí, es decir, digamos como que eso lo lo como que lo tenemos que tener. ¿Listo? Eh, es importante en general porque de hecho en artículo y triple ustedes se dan cuenta que siempre también hay una sección de marco teórico y state of art diferenciados. Entonces, pues no estoy seguro de la de de es como de de lo que hayan hablado con Navarro o no, pero yo sí se los voy a pedir.

### **00:07:26**

**Domiciano Rincón:** Entonces, por favor, inclúyanlo. Eh, y nuevamente pues puede ser, digamos, como el tema de de de las de las mismas palabras claves que estamos buscando para hacer esta búsqueda en anchura. Pueden ser esas mismas definiciones. O sea, que necesito que el lector sepa mínimo, mínimo, mínimo los dispositivos de medición e y la prueba que estamos haciendo. Ya, eso es eso es todo. O sea, no tiene que ser una cosa larguísima. Pero sí tiene que estar bien referenciada. Entonces, si yo voy a hablar de la prueba de de de Tug, yo puedo, por ejemplo, perfectamente citar una referencia de medicina, no tiene que ser ni siquiera ingeniería. Si yo voy a citar las cámaras RGBD y su uso en digamos como en Asmenor, pues también uno lo puede obtener de algún libro, digamos, como de biomecánica o bioingeniería. O sea, no es necesario que digamos como que sea del del campo particular de de nuestro campo, pues, sino cualquier referencia que tenga como las definiciones está es suficiente, pero eso debe estar. Sí. Entonces, digamos como que ya sabemos mínimo lo que tiene que tener, ¿cierto? Igual queda en la grabación.

### **00:08:31**

**Santiago Gomez Robledo:** Profe,

**Domiciano Rincón:** Eso es def

**Santiago Gomez Robledo:** ahorita ya se me escucha. Listo. Eh, pues te iba a decir, profe, si podemos revisar entonces, pero ya no me está dejando compartir pantalla. Maravilloso. Eh,

**Domiciano Rincón:** la búsqueda que hicieron.

**Santiago Gomez Robledo:** sí, te quería mostrar pues lo que tenemos en el marco teórico. Muchachos, ¿alguno puede compartir pantalla y marco teórico, por favor?

**Domiciano Rincón:** ¿Tienen o no tienen marco teórico?

**Santiago Gomez Robledo:** pues el que presentamos ayer. Conor.

**Esteban Guarin Valencia:** Profe,

**Domiciano Rincón:** Ya no entiendo.

**Esteban Guarin Valencia:** es que en sí tenemos el marco teórico separado de las antecedentes, sino es que lo único que que hace que no estén separados es un título, pero sí están separados, por decirlo así.

**Domiciano Rincón:** Okay. Si quieren lo miramos, miremos el el documento y lo y lo vamos y lo vamos mirando. No se te escucha, Santiago, por si acaso.

**Santiago Gomez Robledo:** Se me bloqueó la opción para presentar, entonces estoy mirando cómo la compartir permitido.

**Domiciano Rincón:** Cer

**Santiago Gomez Robledo:** Sí, no, muchachos, si alguno de ustedes puede presentar el documento, porfa, que no me está dejando, se me puso gris el botón de presentar.

### **00:09:51** {#00:09:51}

**Santiago Gomez Robledo:** No me deja presentar.

**Heiner Danit Rincon:** Listo, man.

**Domiciano Rincón:** la evaluación.

**Esteban Guarin Valencia:** Ya estoy mostrando

**Heiner Danit Rincon:** Sí, sí, sí, ahí se ve. Yeah.

**Domiciano Rincón:** Okay. Enfermed Parkinson como primera está bien, supongo. Sí, es como el concepto más general.

**Esteban Guarin Valencia:** una cosa pues que nos dijo Navarro es que tenemos que añadir como una referencia como para darle peso a lo que estamos diciendo.

**Domiciano Rincón:** Sí, absolutamente, muchachos. O sea, por ejemplo, ¿cuándo ustedes saben que tienen que meter una referencia? Cuando lo que ustedes están no es tanto por el peso, obviamente le da peso, si es cuando ustedes hacen un un insight informativo o un o un juicio de valor que ustedes no lo pueden hacer porque pues no somos Aristóteles, digamos. Entonces, uno lo que debe hacer es decir, por ejemplo, no sé, la enfermedad de Parkinson es el enfermedad neurogenerativa más extendida, yo no sé qué. Sí, sí. Sí, o sea, yo lo digo, pero qué, o sea, basado en qué, en qué estudio, en dónde. Entonces, digamos, como que ahí es donde uno tiene que utilizar la referencia.

### **00:11:13**

**Domiciano Rincón:** Si yo voy a decir algo sobre la enfermedad de parquison, dado que nosotros no somos médicos, la mayoría de de de frases o de oraciones que nosotros hagamos tienen que ir referenciadas. Ahora, una puede utilizar una sola referencia para decir la mayoría de cosas, pero se nutre de una mejor manera en la medida en la que ustedes encuentren dos artículos que dijeron dos cosas diferentes e interesantes acerca de de lo que ustedes del punto al que ustedes quieren llegar. Entonces ustedes aquí, por ejemplo, la intención de comunicación, según lo que leo es darle por sentado al lector de que el es que la enfermedad de pino es muy importante porque afecta a muchas personas, ¿sí? O sea, es básicamente eso.

**Esteban Guarin Valencia:** Sí.

**Domiciano Rincón:** Ahora, los argumentos pues los vas a encontrar seguramente en la literatura. Entonces ahí es donde uno tiene, por ejemplo, es el segundo trastorno neuregenerativo más común,

**Esteban Guarin Valencia:** M.

**Domiciano Rincón:** eh, ¿Quién lo dice?

**Esteban Guarin Valencia:** He.

**Domiciano Rincón:** Sí, en el mundo aproximadamente hay 6.2 millones de esa, por ejemplo, se podría unir con la con la anterior frase y ser una sola una sola eh referencia. Actualmente se diagnostican 8 a 18.6 casos nuevos por cada 100,000 habitantes.

### **00:12:15**

**Domiciano Rincón:** Sí, claro. Digamos como que ahí, por ejemplo, se se dicen datos, pero no se dicen de dónde se tomaron. Sí. Entonces, pues por eso es importante, digamos, como ahí la referencia. Sigamos. Entonces, el primer concepto que tienen es enfermedad de Parkinson. Está bien, o sea, referencias hay que tener TUG, eh, okay. Bueno, digamos como el TUG en qué consiste y demás. Okay. Eh, aprobado. Nuevamente eso pues digamos como que requerirá referencia. Ahí hacen algo de 2022 que no sé qué es. Analítica datos 2022 EP como una pandemia. No entendí el 2022 entre paréntesises, pero bueno.

**Esteban Guarin Valencia:** No, es que como Ah, ya es que que tener el micrófono apagado. Es que como estamos modificándolo, entonces pues que ahora mismo pues haya algunas cosas como medio raras,

**Domiciano Rincón:** Okay, okay, okay. Lo del antecedente está bien. digamos, como de citar a sus compañeros eh inmediatamente anteriores. ¿Está bien?

### **00:13:11** {#00:13:11}

**Domiciano Rincón:** Eh, sí,

**Esteban Guarin Valencia:** si no es que ahí sí tengo una pequeña duda.

**Domiciano Rincón:** pero

**Esteban Guarin Valencia:** Esta parte como ya es como un antecedente, no se pondría en el marco teórico.

**Domiciano Rincón:** no se debe poner el marco teórico, ¿no? No. Eh, de hecho, digamos como que la estructura del marco teórico es únicamente, o sea, es es un nivel, si eso es, digamos, como que no no se no se da mucho la profundidad excepto, pues si se necesita. Entonces, digamos, como que hay unos como que uno va de lo general a lo específico, ¿sí? Y nuevamente responde a yo qué quiero o qué necesito pues que el lector sepa para poder entender de lo que le voy a hablar más adelante. Entonces, me gusta pues que enfermedad de Parkins no sea como el primer concepto que sale en el marco teórico.

**Esteban Guarin Valencia:** Sí.

**Domiciano Rincón:** Ese es como el más general. Ya, luego sigue TUG, puede ser, digamos, un asesmen biomecánico de la persona, incluso podría podría, no estoy diciendo que tiene que estar,

**Esteban Guarin Valencia:** Ok.

**Domiciano Rincón:** pero podría entre enfermedad de Parkinson y asesmen de TUG podría ir el análisis motor eh en general. Sí. O sea, entonces yo llego y paso de Parkinson y luego digo el análisis motor, ¿qué qué técnicas hay?

### **00:14:14**

**Domiciano Rincón:** ¿Cómo se hace y demás? No es un antecedente. Simplemente estoy diciendo que se hacen análisis motores porque pues el Parkinson afecta la marcha, yo no sé qué cosa. Sí. Entonces, digamos, como que uno puede en el marco teórico poner qué es la enfermedad de Parkinson, cómo eh cómo se cómo se mide, digámoslo así, eh y posteriormente eh la prueba y los instrumentos de medición. Eso es lo que yo necesito que que el lector sepa, digámoslo, acerca del trabajo. Pero ahí nosotros estamos contestando es qué es, ¿no?, qué ha pasado con ese estudio ni históricamente pues cómo se ha abordado pues los estudios acerca de esto, ¿no? Simplemente son como definiciones. Entonces, nuevamente, o sea, yo digamos como que yo pondría los siguientes conceptos. enfermedad paraon como primera, eh análisis biomecánico, análisis motor en general, eh qué es, o sea, ¿por qué se hace? ¿Qué qué luces da? Eh, puede ser, digamos, como una conexión con el Parkinson, puede ser como que, no sé, pues el Parkinson afecta al sistema motor, entonces se hacen assessments de X y Y tipos. Entonces ahí introduzco la prueba de TUG, digo, ¿cuál es el protocolo de TUG?

### **00:15:21**

**Domiciano Rincón:** Es decir, se tiene una silla, la persona se sienta, se para, tan, gira, eh, se devuelve y se sienta. Sí. Entonces ahí defino las fases y o seaamente en el marco teórico pueden entonces ya quedar definidas las fases. Es algo que seguramente no va a estar en el en los antecedentes, porque en los antecedentes vamos a hablar es más de cuáles son los descriptores más importantes acerca de de de cada una de las fases. Sí, bueno, entonces ya quedaron las fases. Luego entonces hablamos de formas de medir el análisis, el digamos como la la sí, ¿cómo decir? La SESM motor, cómo se hace. Entonces nosotros podemos directamente introducir, independientemente de si se hace por 16,000 medios, porque también hay unas cámaras que se llaman, eh, se me se me se me fue el nombre, Bacon, no se me fue el nombre. Eh, bueno, hay unas cámaras que se utilizan para para hacer las películas en tres dimensiones y entonces han visto, digamos, como el típico persona con una licra y con unos marcadores en todos los puntos del cuerpo y entonces que eso le dan como el movimiento pues al al muñeco en 3D y bueno, digamos como que es esa cámara eso también se utiliza como sistema eh de medición.

### **00:16:28** {#00:16:28}

**Domiciano Rincón:** Lo que pasa es que ese sería como nuestro gold standard y nosotros lo estamos intentando hacer con unos medios diferentes. Entonces, el marco teórico no puede definir que pues se puede medir con imus y se puede medir con cámaras RGBD y luego se procede a describir las cámaras y demás. Hasta ahí llegaría para mí el marco teórico. No necesitamos más. No necesitamos, por ejemplo, algoritmos de clasificación, no necesitamos algoritmos de búsqueda porque eso eso realmente, digamos, como que lo va a decir el tiempo, pero sí al menos quedamos con qué es la marcha, qué es eh qué es el Parkinson, qué es la marcha, qué es el la prueba de TUG, qué es eh pues los IMU y qué son las cámaras RGBD, nada más. Sí, nuevamente responde qué es qué es qué es cada cosa. Luego ya en el en el en el en los antecedentes eh la estructura puede ser ahorita sí digamos como

**Esteban Guarin Valencia:** A ver.

**Domiciano Rincón:** en profundidad y sería algo similar a digamos como que yo tengo que describir una línea de tiempo, pero eh digamos selectiva. Entonces, en la línea de tiempo yo puedo, por ejemplo, decir la forma en la que se mide actualmente, ¿cierto? eh cómo nació la prueba de TUG y demás.

### **00:17:41**

**Domiciano Rincón:** La prueba de TUG originalmente no está digitalizada ni está medida de forma electrónica ni nada por el estilo. Por ende, entonces ahí podemos también entender, digamos, como que hay un sesuel observador y demás. Entonces ya luego eh uno puede pasar con Bueno, entonces eh se han intentado hacer eh digamos, assesment de bajo costo basado en IMU, basado en cámaras RGBD de la prueba. Eh, luego entonces los resultados que se presentan es que se puede oamos como que para poder hacer un screening eh o un lo llama un tamizaje, pues eh si digamos como que para poder hacer el tamizaje. Entonces yo digamos como que he podido utilizar, no sé, eh ciertos descriptores o ciertos tiempos al hacer la división de la marcha. ¿Sí? Entonces, digamos, como que yo ya empiezo a explorar qué es lo que ha hecho las personas por el problema que nos que nos compete a nosotros. Pero para poder llegar a ese problema, pues en el mismo estado del arte, pues yo tuve que haber pasado históricamente de cómo es que se ha hecho, ¿cierto? Entonces, uno puede hablar como antecedente nuevamente eh cómo es que las cómo se reporta si es que se si es que se encuentra pruebas de de de TUG, pero eh puras, digámoslo, sin la intervención de la tecnología.

### **00:18:55**

**Domiciano Rincón:** Luego, entonces uno puede decir, bueno, y se intervino con la tecnología de esta manera. Entonces, obviamente no vamos a poner las cámaras estas que le digo que les digo de de los muñecos en 3D, sino pues lo que pues digamos como que hemos consultado en la en la literatura, espero esta semana y es eh cómo cómo se aportó al problema desde sistemas de mediciones similares al al nuestro y es con cámara RGBD y con y con IMU. Y entonces uno empieza, digamos, como a hacer esa exploración y entonces uno lo puede ir haciendo eh por línea de tiempo incluso. Sí. Entonces, digamos como que uno puede partir de algo que se hizo en 2012 y cómo se está haciendo hoy en 2024, 25, 26\. Y el último puede ser entonces este antecedente que yo es un antecedente local, ¿cierto? ¿Por qué para mí es el último? porque pues probablemente dentro de la literatura no se vaya a encontrar algo de 2026 respecto a esta prueba, pero pues este sería como el antecedente directo que pasamos digamos como de describir toda la línea de tiempo de cómo empezó el asesment motor basado en en en la en la prueba y qué es lo que se ha hecho por solucionar el problema hasta el trabajo de esos compañeros.

### **00:20:07**

**Domiciano Rincón:** ¿Sí? Entonces, ese es como el como la estructura que tendría que llevar este este documento. Eh, bueno, esa esa sección. Eh, vale.

**Esteban Guarin Valencia:** Listo, profe. Las cámaras que captura el cuarpon 3D son laseléctricas, me parece.

**Domiciano Rincón:** No estoy seguro de la tecnología del sensor, pero son, o sea, el sensor de dept, pero se llaman así, cámaras RGBD, o sea, el AD es de deft, como de profundidad. Eh,

**Esteban Guarin Valencia:** Sim.

**Domiciano Rincón:** y les digo directamente los los dispositivos que se utilizaron eh o que se utilizan es el Intel Intel Real Sense, es el primero y el segundo es eh una cámara que se llama Orbec. No pues no tengo la especificación particular de eso, pero pues ambas son cámaras RGBD. Yeah. Ah, bueno, hace tiempo, lo que pasa es que pues ya no se utiliza porque ya se cambiaron esas cámaras, pero eso se inició con con el Microsoft Kinect, con el sistema este de videojuegos que sacó Xbox hace años,

**Esteban Guarin Valencia:** Sí,

**Domiciano Rincón:** pero pues

**Esteban Guarin Valencia:** yo he visto yo he visto que con esos también han detectado que a veces te avisas si tenés algo cosas así.

### **00:21:21**

**Domiciano Rincón:** eso entonces digamos como que eso, por ejemplo, ya está como descontinuado, ya está como descontinuado, ¿no? Está descontinuado. Entonces, si ustedes se consiguen, digamos, alguna referencia, las referencias van a ser relativamente antiguas, 2010, 2012, ¿sí? Entonces, eso también puede ser un buen punto central para poder empezar a buscar, porque igual eso se acaba lo mismo, o sea, sacaba la esqueletización del cuerpo, se hace el análisis de los joints como señal y pues seguramente se tuvo que haber hecho algún tipo de de de fraccionamiento de las fases, pero es ese es el tema, digamos. O sea, el tema es eh encontrar en la literatura, pues eh pues sí, o sea, cómo cómo ellos digamos cómo cómo se hace para poder hacer esa comparativa o hacer ese tamizaje y por ende entonces nos que buscar los descriptores. Nosotros tenemos una tarea para la recuerdan. Era la búsqueda natural.

**Esteban Guarin Valencia:** Sí, profe, nosotros hemos estado buscando bastantes artículos.

**Heiner Danit Rincon:** Ok.

**Esteban Guarin Valencia:** Nosotros sí hemos estado buscando bastantes artículos. Una cosa que yo he llegado a notar de que pues se han notado bastantes artículos de machine learning, pues que son más los más recientes que están dando,

### **00:22:36** {#00:22:36}

**Domiciano Rincón:** Aha.

**Esteban Guarin Valencia:** pues en sí yo no decidí en meterme en esos artículos, pues por el hecho que pues aquí no estamos mostrando tanto mach learning, pero no sé si también me pregunté si también debería pues incluirlos o tenerlos en cuenta o algo así. Ok.

**Domiciano Rincón:** Yo yo creo que es bueno tenerlos en cuenta para el tema de los antecedentes, pero la razón es la siguiente y es que e a ver, o sea, hay hay personas que lo que pasa es que eso Eso eso depende tanto como del digamos como de la dirección eh del del digamos como de los investigadores principales sobre todo y es y es lo siguiente, muchachos. O sea, ustedes seguramente van a encontrar esos artículos y ustedes lo que pueden verificar es ellos cómo hacen el tratamiento de pocos datos, ¿sí? O sea, por ejemplo, si yo me encuentro en el artículo que hay un N similar al nuestro, un N70, entonces uno dice,"Uy, okay, o sea, le aplicar maquill a un N70, por ende, entonces es posible eh utilizar esa técnica. Pero yo me he encontrado con artículos que hacen data augmentation sobre datos clínicos. Eso a mí no me parece correcto porque en el data augmentation, o sea, las señales biológicas son unas señales que que son alta eh digamos no son repetibles.

### **00:23:53**

**Domiciano Rincón:** Sí. Eh, si yo mido a una persona en este momento el temblor y lo mido 5 minutos después puede que no sea lo mismo. No sé si ustedes de pronto digamos como que con esos relojes inteligentes se miden la el ritmo cardíaco, pero el ritmo cardíaco viene en rangos, no es que ustedes siempre tengan eh 90 60 o como se o como se mida esa esa variable, pero eso se mide como por rangos, no sé si lo si lo si lo han notado, pero todo en general es así. Entonces, y sobre todo, digamos, como cosas tan tan, o sea, que cumplen un patrón, pero que realmente son, o sea, entran dentro del campo estadístico y es eh yo camino, pero yo no yo no siempre voy a dar los mismos pasos, no voy a tener la misma energía, seguramente no va a tener la misma inclinación, o sea, van a haber muy pequeñas variaciones y esas pequeñas variaciones pues puede hacer que nuestro descriptor presente una variabilidad grande, una varianza grande. Entonces, teniendo en cuenta eso, pues el data augmentation me parece que es lo peor que uno puede hacer para señales que uno consigue en campo, sobre todo para aumentar el n de pacientes. Sí, si yo, por ejemplo, tengo, no sé, algo algo generado, pues eh o algo que me esté generando, digamos, una variable eh diferente, no biológica, eh pues pues todo bien.

### **00:25:05**

**Domiciano Rincón:** Pero si mi enfoque es, ah, no, pues miramos 10 pacientes y hacemos un data augmentation, entonces tenemos 100 pacientes. Parece que no. pues que realmente no pues termina por no corresponder a la realidad. Eh, nosotros lo intentamos en el pasado y bueno, vamosamos como que por eso les les comento. Entonces, sí los podemos tener en cuenta para saber ellos cuál ha sido el enfoque que han recorrido. Por ejemplo, si el enfoque es podemos utilizar machine learning y en lugar de hacer data aumentation, por ejemplo, eh multiplicamos la cantidad de observaciones. A ver, vamos como que se puede hacer de diferentes formas, pero por ejemplo, imagínense que la marcha en sí, eh, a ver, pensemos nuevamente en la prueba de TUG y hay un levantamiento, una marcha uno, un giro y una marcha dos, ¿cierto? Pero ustedes saben que en la marcha uno, en el giro y en la marcha dos hay pasos, hay pasos de paciente. Entonces, yo yo he visto, digamos, como e antecedentes que lo que intentan hacer es tratar el paso como el N en lugar de la de la marcha completa. Entonces, ya no tienen la marcha completa como un N, o sea, ya no tienen 70 observaciones, sino ya tendrían la cantidad de pasos multiplicado por 70\. ¿Sí me hago entender?

### **00:26:14**

**Domiciano Rincón:** Es decir, digamos, como que cada elevación y golpe con el con el con el piso la toman como una observación. Entonces, si un paciente hizo, no sé, si un paciente hizo cinco cinco, por decirlo así, cinco pasos en toda su en toda en todo ese evento, entonces digamos como que ya tenemos para ese paciente un n \= a 5\. Entonces, se puede como maximizar de esa manera. Todos los pasos no son iguales, los pasos sobre todo que cuando la persona se está medio levantando son diferentes, los pasos del giro también son diferentes, pero yo he visto, digamos, como estrategias para no hacer un data augmentation estadístico, sino simplemente minimizar la unidad de observación. Pero eso es, digamos, como que perfectamente posible. Si nosotros dentro del estudio vemos, ah, no, pues eso sí se puede hacer o los pasos o o puede ser que los pasos sean muy eh variables, muy muy diferentes entre sí, entonces no se puede hacer. Sí, pero yo sí los tendría en cuenta, al menos los leería para entender cómo es, o sea, primero, cuál es el n de esos estudios, segundo, si hacen un data augmentation o no y y cómo lo hacen, pues, y el tercero, pues para verificar justamente que se pueda, o sea, que sea factible, por ejemplo, aplicar ese tipo de técnicas en pues en un n igual que el nuestro.

### **00:27:27**

**Domiciano Rincón:** Entonces, si por ejemplo en la literatura reportan que hicieron un un clasificador con machine learning, digamos, y lo hicieron, no sé, 30 pacientes y 30 controles, ¿ya? O sea, eh con ese nos podemos ir y además puede ser también un artículo importante para una técnica futura que nosotros tengamos porque pues tenemos el suficiente N como para poder también tener un un conjunto de validación. ¿Sí? Entonces es es eso lo que lo que les quiero comentar, o sea, que sí, sí, tengámos en cuenta. Yo sé que el enfoque es muy de señales, claro, o sea, muchas de las de la de la literatura que van a encontrar es acerca de señales, pero de todas maneras miremos el tema de machine learning porque primero es lo nuevo. Segundo, digamos como que probablemente pues hayan algunas técnicas que nosotros podamos eh aprovechar con nenes bajitos, digámoslo así, y ya quedaría. Lo que pasa es que yo sé que esas técnicas funcionan mucho mejor cuando el N es es gigante, pues, pero el N gigante. Entonces, por eso hay que al menos darle la oportunidad al artículo de decir, bueno, en el abstract lo dice, ¿no? Como que se comparó un n \= a 45 y controles y n \= 45 pacientes y se hizo y los resultados fueron tales.

### **00:28:37** {#00:28:37}

**Domiciano Rincón:** Entonces, uno puede desde el abstract directamente verificar pues cuál fue el tamaño muestreal y por ende pues uno puede hacerse una idea de si es compatible o no con nuestro estudio. Sí.

**Esteban Guarin Valencia:** Sí, profe. Otra cosa es que yo encontré como un artículo, bueno, no me parece que son dos, que tratan sobre, precisamente es lo que yo quería hablar sobre una cámara autoeléctrica como kinética, como la que has estado hablando. digamos que toma como unas partes del cuerpo y como que las grafica para hacer como un esqueleto en 3D. En esas pues también se tuvieron como la prueba de la clasificación esta de joven job y es y tomaron como lo que yo

**Domiciano Rincón:** Sí.

**Esteban Guarin Valencia:** noté en esos dos artículos es que se notaban mucha más diferencia en las partes donde se hacía el giro, o sea, notaba más diferencia entre los pacientes que estaban normales y un poquito pues con esta enfermedad en más que todo en la parte del giro.

**Domiciano Rincón:** Sí. ¿Y qué?

**Esteban Guarin Valencia:** Incluso ellos decidieron, digamos, añadir otra fase más en donde es otra vez el giro y sentarse. No giro y sentarse, sino separarlos. Vamos.

**Domiciano Rincón:** Oh. Yeah. Okay.

### **00:29:59**

**Domiciano Rincón:** Respecto a eso, digamos como que nosotros tenemos pues sí, pues como la, es decir, seguramente lo digamos como que gracias a los videos lo podamos ver, pero en el protocolo la doctora pues que hace la prueba de TUG, o sea, que que es que digamos como que está intentando digitalizar pues la prueba de TUG y demás o al menos digamos como volver un poco automática esa esa segmentación, e ella lo hace así, o sea, es decir, digamos, como que la persona va hasta la silla pero gira y se sienta directamente, pero nosotros podemos encontrar seguramente, mejor dicho, o sea, eso es una fase un poco un poco nebuloso, porque hay pacientes que, o sea, como que se sientan y se y se voltean de una, o sea, hay gente que, o sea, digamos como que hay muchas hay muchos ejemplos, ¿no? O sea, digamos como que hay gente que se da la vuelta y se sienta directamente o hay gente que separa las dos fases, o sea, primero da un giro y luego sí se siente, ¿no? digamos como que en el protocolo de diseño, en el protocolo, perdón, de experimental, o sea, para tomar los datos, no se le especifica realmente al paciente, se se deja libre porque también es algo a analizar.

### **00:31:07**

**Domiciano Rincón:** Entonces, probablemente también, por ejemplo, hayan incompatibilidad con nuestro protocolo. No significa que nosotros tengamos entonces que descartar el artículo, pero sí podemos, por ejemplo, eh verificar qué indicadores. Por ejemplo, en el en el en el en el que mencionas eh eh tú, Esteban, eh ese artículo, o sea, ese artículo que mencionas, me dices, digamos, como que hay diferencias en el giro, pero diferencias en cuál descriptor, en qué variable lo la hace diferente. Lo lo tienes claro.

**Esteban Guarin Valencia:** No, exactamente no, porque como me vaer un poco y un poquito más allá, pues no alcancé comociar exactamente en qué se diferencia. Pues sí muestran los datos, pero pues por el momento no servía como tanto leerlos. Pues igual aquí tengo un documento como para mostrarlo así al por encima.

**Domiciano Rincón:** Dale, dale porémos. Es el documento de tarea, ¿no? Ese no es el que podría ser un anexo luego.

**Esteban Guarin Valencia:** Sí, este sería el documento aquí como está el astro.

**Domiciano Rincón:** Ah, ya pensé que era el otro. A ver.

**Esteban Guarin Valencia:** Pues igual tenemos el un anexo donde está ya como un resumen, digamos, donde tenemos todas las referencias que hemos ido sacando entre todos.

### **00:32:40** {#00:32:40}

**Domiciano Rincón:** Un momentico. Perdón, perdón. Estoy intentando mirar a ver. Voy por la mitad, perdón.

**Esteban Guarin Valencia:** M.

**Domiciano Rincón:** Listo. Ahí están los descriptores, ¿no? O sea, dice que, o sea, lo primero es que lo dividen en seis fases. No sé si sea para nosotros lo mismo, porque esa fase última no es tan clara, no importa, porque igual nosotros tenemos un giro, o sea, tenemos tenemos un giro, o sea, tenemos un giro parado, así que pues un giro allí, un giro sentado, probablemente digamos como que pues nada, o sea, simplemente el el diseño experimental es diferente, pero sí habla de que tienen variables temporales, espaciotemporales y variabilidades y eh multisegmental kinic parameters e Pero abajo lo dicen, dicen que utilizaron, o sea, que encontraron diferencias en el double support time, ¿no? En el shorter stride length, en el lower walking speed, eh, reduce frontal plane control, ah, reduce trunk elbook. Ah, bueno, no estoy seguro si esos ya son, digamos, como las variables que están que están reportando. Habría que leerse el artículo que pues ya escribe como movimientos pues de partes específicas del cuerpo, pero creo que ahí tenemos digamos como unas variables candidatas, digámoslo, a componer el grupo de variables que nosotros vamos a a tener, digamos, como que en en en el primer estudio, o sea, en el primer en la primera tesis de grado, digamos, lo que se logró fue hacer ese algoritmo de de de de de separación de las fases.

### **00:34:28**

**Esteban Guarin Valencia:** Mhm.

**Domiciano Rincón:** Ahora, ese algoritmo pues falta probarlo con pacientes porque pues eso se hizo con pues mayoritariamente con controles, pero pues los controles, o sea, partimos de que o sea partimos de la suposición de que todos así estén enfermos o no, el patrón de movimiento pues continúa siendo el mismo. Es decir, es una persona que igual se pudo levantar, una persona que igual pudo caminar, girar, volver a caminar y girarse y sentarse. ¿Cierto? Entonces, teniendo en cuenta eso, pues el patrón el patrón está, así que lo más probable es que el algoritmo tenga un rendimiento X. Pero lo que no se pudo hacer nunca, pero que sí se puede hacer porque tenemos como todas las visiones completas de cámaras máximus esos tiempos que señalan ahí. Por ejemplo, Navarro ha estado, digamos como que en todo el tema de marcha siempre ha estado muy interesado en esa en esa prueba, sobre todo por estas variables que se presentan allí. Entonces, hay una double support time. Esa double support time e o sea, tengo que recordarlo, pero les puedo decir que de hecho, no sé por qué se por qué dices eh Bueno, sí. No me importa, pero la marcha, la marcha tiene dos fases.

### **00:35:33**

**Domiciano Rincón:** Entonces, la primera fase, la de, perdón, el el zapateo, digamos, cuando la persona está caminando, hay dos fases, ¿no? Cuando está en el aire y cuando aterriza. Y sí. Entonces, digamos, como que cuando aterriza, digamos, como que se queda en el piso y se queda quieta. Y cuando vuela, ese es el swing time y el support time. Sí. Entonces, pues digamos como que una persona con TUG, con Parkinson, perdón, va a presentar una alteración en esas fases. Sí. Entonces, una persona sana, de de alguna manera tiene como una proporción entre esos tiempos, una proporción diferente. Sí, lo de String Length es como el tamaño de la zancada. Entonces, por ejemplo, el tamaño de la sancada lo podemos verificar dado que como es una cámara RGBD y nosotros podemos ver un poco los pasos, no sé, no estoy seguro que podamos ver todos los pasos, pero vamos a poder ver x pasos. Nosotros también podemos calcular para cada paciente cuál es su promedio o incluso cada stride l que hizo. El striight l es qué, o sea, por ejemplo, Navarro tiene un stride l gigante porque él es gigante. Sí. Eh, pero por ejemplo, no sé quién conocen que sea bajito.

### **00:36:33**

**Domiciano Rincón:** Bueno, pero esa persona bajita, Dexter, no sé, eh, tiene un stadline cortico porque eh pues digamos como que está Sí, es decir,

**Esteban Guarin Valencia:** Ah.

**Domiciano Rincón:** digamos como que cada paso de él va a significar 30 cm más o lo que sea, pero Navarro puede tener un stri de 1 met y medio. Entonces, es esas variables espaciotemporales, digamos, como que son las que nos interesan más a nosotros en este en este estudio, ¿sí? Entonces, aquí, por ejemplo, en este estudio lo presentan, creo que está que que pues es que que es grandioso, digámoslo, pero sí digamos como que debemos seguramente hacer el ejercicio que les pedía la vez pasada, ¿sí lo recuerdan, cierto? es eh extraer del abstract eh pues cuáles son preliminarmente las variables que en las que se fijaron para poder hacer las diferencias significativas entre pacientes y controles. Pero esto digamos como que me me deja como una sensación de como decir de, o sea, por aquí es, ¿no? O sea, si yo me elevo el PDF, pues probablemente le digan a uno bien cómo medir y todo. Por ejemplo, con IMUS no lo no. A ver, el artículo antecedente que ustedes tienen, la tesis antecedente que ustedes tienen, no se no se puede medir el straight lend.

### **00:37:38** {#00:37:38}

**Domiciano Rincón:** Eh, de pronto sí, la el el el tiempo de soporte, que creo que debe estar por ahí en en alguna parte del estudio, eso lo intentamos hacer, pues, pero eh el foco no era ese, pero el el el support time, el double support time y el swing time, la proporción entre el swing time y el support time, eso lo seguramente lo lo digamos como que lo podemos sacar sin problemas con la sim, pero el straight length no lo no lo pudimos sacar porque a pesar de que tengamos todas las matemáticas de la vida y demás, pues yo no puedo calcular realmente eh que partió de x y que y que llegó a x \+ 1 m, no, eso no lo puedo calcular con la sim, pero sí con la cámara. Entonces, como tenemos las dos visiones, pues lo más probable es que se puedan sacar todas las variables que que pues que reportan en la literatura, ¿no?

**Esteban Guarin Valencia:** Nosotros pues también tenemos el el documento de los anexos que nos habías pedido.

**Domiciano Rincón:** Sí.

**Esteban Guarin Valencia:** Lo único que nos faltó pues mandarlo al grupo para que lo pudieras ver.

**Domiciano Rincón:** Sí, sí, vale, muchachos. Si si ustedes lo pueden enviar un poco antes de la reunión, vamos, como que eh quizá puede ser más provechoso porque ya tendríamos el mismo contexto todos.

### **00:38:47** {#00:38:47}

**Domiciano Rincón:** Lo que también podemos hacer es esto, digamos, o sea, como mirar los highlights. Lo que pasa es que pues tendríamos siempre, digamos, como estaríamos como una semana detrás, pero no importa, digamos. O sea, sea como sea, igual estamos en el seman una semana verificándolo, pero eso me pareció me pareció bien chévere. Eh, seguimiento tridimensional. Okay. Ah, bueno, lapiew, o sea, lapiew es de Matlab, ¿no? Extrajer siete variables cinemáticas. Ahí ahí tendríamos que verificar es cuáles, ¿no? Cuáles variables cinemáticas extrajeron, o sea, como que empecemos a nombrarlas. Ustedes van a ver que straight leng va a aparecer siempre, double support time va a aparecer siempre, eh swing time, a pesar de que en este estudio no apareció, va a aparecer también. Entonces puede ser como también seguramente anotar e pues sí, es esas variables que que van que van apareciendo. Hay más, o sea, hay más, o sea, las de distancia las podemos seguramente medir con la cámara, pero las que son de tiempos, o sea, por ejemplo, el double support, eso, eso lo podemos seguramente verificar con el accelenómetro de de dado que se ponen en los tobillos.

### **00:39:45**

**Domiciano Rincón:** Literalmente cada paso está marcadito exactamente tal cual como fue. Entonces uno puede saber cuál es el landing time, es tiempo del aterrizaje del del del tobillo y cuándo se volvió a levantar. Entonces, la diferencia entre esos dos tiempos ya me da el support time. Sí, sí, sí. Se la pillan. O sea, es básicamente eso. El número de pasos, por ejemplo, también fue un descriptor que intentamos hacer en la tesis pasada, pero el número de pasos es relativamente sencillo, pero igual se extrajo como para pues porque eso era realmente como una un un un primer acercamiento, pero en este acercamiento nosotros podemos no solamente contar los pasos, sino caracterizar los pasos, que eso es por donde nos está llevando el pues esos esos artículos que aparecen allí. ¿Tienes otro que haya parecido interesante?

**Esteban Guarin Valencia:** Sí, me pareció otro interesante, pero ahora mismo no me acuerdo cuál era.

**Domiciano Rincón:** Vale, vale.

**Esteban Guarin Valencia:** No sé no sé si mis compañeros tienen otros ahí pues para presentar.

**Domiciano Rincón:** Esos dos primeros están son de defas, pero tienen para imu, para unidades inerciales.

**Esteban Guarin Valencia:** en sí no sé porque ese no no fui yo y que lo lo agregué, pues ahí es como todos intentamos buscar, entonces cada uno pues intentó leerlo, pues lo agregó y todo.

### **00:41:04** {#00:41:04}

**Domiciano Rincón:** Bueno, entonces los demás entonces los demás los demás que qué

**Esteban Guarin Valencia:** ¿Cómo?

**Domiciano Rincón:** leyeron así digamos como de de cómo se hizo la prueba, o sea, esto entonces Esteban estuvo con el tema de cámaras, alguien estuvo con el tema de IMOS.

**Juan José Arias Gallego:** Eh, pues, profe, yo en lo personal exploré el tema de RGBD y esos primeros creo que cuatro o cinco papers que hay allí son todos acerca de lo mismo, aunque la verdad recuerdo que que pues en algún momento dijiste que lo de Kines ya está un poquito descontinuado para y pues allí hay creo que uno uno de que habla acerca del del análisis de la marcha con Kinx.

**Domiciano Rincón:** O sea, A pesar de que de que el Chinag está desinuado. No, o sea, comercialmente ya pues es difícil encontrarlo. Pues eh justamente por esa dificultad comercial fue que nosotros nos pasamos a unas cámaras que sí se consigan comercialmente, pues esta adásicos fiesta de de Orbec. Hm. Sin embargo, las técnicas seguramente nos siguen sirviendo porque eh al final las dos cámaras hacen lo mismo, ¿sí? Que es esqueletizar el cuerpo. El cuerpo. Eh, con esqueletizar ya ya sabemos a qué nos referimos, ¿cierto?

### **00:42:23**

**Domiciano Rincón:** O sea, como que él pone unos puntos como que, o sea, como que yo si yo estoy así, él superpone, pues, pone unos puntos aquí como en los en los en los joints, entonces él sabe más o menos cómo se está moviendo el cuerpo y demás. Y entonces cuando camino el el el esqueleto se se mueve con el con la extremidad y demás en tiempo real. Entonces, pues eso es básicamente lo que lo que hace el trabajo. O sea, que digamos como que a nivel de adquisición sí está descontinuado, pero a nivel de análisis puede ser que esas mismas herramientas de análisis nos sirvan para nutrir el trabajo. Entonces, está bien, o sea, que tengan ustedes, digamos, como técnicas de ese de de de digamos como esa época, pues en la que se hacían análisis con Kinet. Está buenísimo porque igual eh pues nos va a servir, No.

**Juan José Arias Gallego:** Y pues lo otro es que también en la mayoría de estos de estos papers se encontró como que hablan mucho de un ISC, que es como el coeficiente de correlación intraclase para dar como fiabilidad después de realizar barre repeticiones. en qué tanto puede puede fallar el el instrumento de medición o dar, digamos, los mismos los mismos resultados después de varios testes. Entonces, en el primero, pues se usa la Kinect y habla ahí del ISS por encima del 090, o sea, que según eso hay una buena fiabilidad.

### **00:43:45**

**Juan José Arias Gallego:** Y creo que este primero se hace con pacientes de eh que tuvieron cerebrovascular.

**Domiciano Rincón:** Okay. Okay. Pero igual al final al cabo pues la prueba de TUG, ¿no? O sea, pues vemos que igual eso no es como exclusivo al Parkinson.

**Juan José Arias Gallego:** Mhm.

**Domiciano Rincón:** eh metodología seguimiento digamos como que yo les

**Juan José Arias Gallego:** Eh, M.

**Domiciano Rincón:** pediría digamos como como añadir adicionalmente digamos eh las variables y una pequeña descripción de las variables que se sacan. Por ejemplo, ustedes ustedes ya se fijaron que en esos estudios lo que hacen es extraen un descriptor, lo someten a una prueba estadística y entonces intentan verificar siempre si hay un R o un P, pues un RO menor a 0.05 porque eso daría el 99% de diferencia. digamos como que cada vez que uno va a verificar un artículo de esos casi siempre es lo que reportan, ¿no? No sé si lo lo han leído y les y les suena lo que les estoy diciendo. Eso de R menor a igual a, perdón, R menor a 0.01. Cuando se hace una prueba estadística, por ejemplo, de prueba Z,

### **00:44:50** {#00:44:50}

**Heiner Danit Rincon:** Ah,

**Domiciano Rincón:** regularmente,

**Heiner Danit Rincon:** sí,

**Domiciano Rincón:** digamos,

**Heiner Danit Rincon:** profe.

**Domiciano Rincón:** como si le suena si le suena eso.

**Heiner Danit Rincon:** Sí, sí, señor. Sí, señor. Eso lo trabajamos en inferencia estadística más o menos cuando Sí, eso es puro para probar hipóteses. Y sí más cosas, ¿cierto?

**Domiciano Rincón:** Eh, tal cual, tal cual, pero lo lo han visto en los en los artículos que han encontrado,

**Heiner Danit Rincon:** Ah.

**Esteban Guarin Valencia:** Por mi parte me parece que no.

**Domiciano Rincón:** por ejemplo, ese que tenías allí, ahorita puedes volver a poner el abstract, ahí hablaba justamente de de esas diferencias con reportando el RAW. Lo que pasa es que en en en los artículos científicos lo que se hace es reportar algún tipo de prueba estadística que justamente lo que lo que dice Heiner es que pues se se diga eh con prueba estadística una afirmación rechazando la hipótesis nula, digámoslo. Eso es algo de estadística, pues, pero se utiliza se utiliza bastante. Entonces, a ver, eh sí, fíjense que ahí dice RAW 0.015 015 eh, y R 0.009.

### **00:45:53**

**Domiciano Rincón:** Esa letra P es una es una R. Es la eso sí digamos como que en este momento no tengo el nombre de ese de ese estadístico, pero cuando uno hace las diferencias significativas lo que uno obtiene es ese índice R. Pero fíjense que ahí aparecen todos los elementos que que que analizaron y que tienen diferencias significativas. Dice, a ver, un momento, dice participantes con PD, ¿qué? Ah, ya modified. Dicen que, o sea, como que pacientes y controles, o sea, lo primero que dice allí acerca del R es como en la mitad del párrafo, ¿no? Que dice participant pd modified andar stage two performes more slow trans controls. Entonces ahí dicen ro menor que 0.001. O sea, ahí están diciendo que hicieron una prueba estadística y la prueba estadística para poder hacer una prueba Z, pues se tienen que tener 30 datos o más. es como el tema de lo de las observaciones, pero el hecho de que estén reportándolo significa que seguramente en el paper sacan una tabla en donde dicen que efectivamente eh estadísticamente son la diferencia significativa entre pacientes y controles. Entonces, ese es el tiempo total de la prueba, imagino yo. Y lo reportan porque pues eso es algo que es evidente, no es que no es que sea el descubrimiento, eso también lo descubrimos nosotros, digámoslo, en el en la tesis pasada.

### **00:47:23**

**Domiciano Rincón:** Luego dice, e mainly do to impairments during walking and turning. O sea, que también hay diferencias significativas, por ejemplo, en el giro. Habrá que mirar dentro del artículo bien, pues, cuál es la variable descriptora. Eh, turning was de only face. A ver, no alcanzo a leer bien. Ah, ya. Que dice que el giro es Gracias. que el giro fue la única variable que deci distingue entre pacientes y controles y eh dejó deillar en estado Dios un a 1.5 no significa que las de arriba sean eh que tengan mal diferencia significativa, sino que en el stage two de joven andar eh las diferencias significativas se pronuncian en otras variables, pero las únicas que en early stages eh sí eh son buenos descriptores es el tema del giro, pero ahí dice el giro, la fase del giro, o sea, ¿qué habrán verificado ellos? Habrá que leerse el artículo para saber cuál es la variable que sí, porque pues digamos como que para poder sacar esa frase pues claramente uno tiene que decir el giro en respecto a qué, o sea, a tiempo, a número de pasos dentro del giro, a no sé, complejidad del movimiento en el giro, energía gastada en el giro, eh no sé, frecuencias altas eh en el giro, ¿sí?

### **00:48:41**

**Domiciano Rincón:** O sea, habrá que verificar pues lo lo del giro, pero el hecho de que ellos reportan que en estadios tempranos está bien chévere el giro, es porque pues seguramente haya que entrar al artículo y verificar efectivamente pues cuáles son las variables de giro que eh sirven para esto. E a ver, sí, dice que para estadiodos que los pacientes se expusieron, digamos, como es esas variables que estábamos hablando ahorita, que básicamente parece que parecen ser que no sí, o sea, que que es que que son unas variables que pues ellos tomaron y demás y que pues seguramente eh pues hay una diferencia, pero habrá que verificar en la tabla pues cuál es la diferencia, si está marcado o no, si es significativa o no. seguramente lo tenga internamente el paper. Me me pueden mandar ese enlace. Ese es interesante. O sea, es es interesante porque pues básicamente habla de ya unas variables particulares y además miren que lo hicieron con 38 e Parkinson DC Spion pues y 41 control, o sea, que es similar a la muestra que tenemos nosotros. ¿Quién está compartiendo? ¿Me puede mandar el link de la persona que esté compartiendo?

**Esteban Guarin Valencia:** al yo lo compartí por el WhatsApp o lo comparto también por la reunión,

### **00:50:02**

**Domiciano Rincón:** Ah, okay. No, ahí está bien, ahí está bien. MDPI, ¿no? Encima eso MDPI está es super buena revista.

**Esteban Guarin Valencia:** incluso pues es de 2026, así que es bastante reciente.

**Domiciano Rincón:** Es esa y ustedes me haban mostrado una de Plus la reunión pasada también. Buenísima. Claro, ellos tienen seis fases, o sea, el diseño experimental de ellos es seis fases. Y es que seguramente las indicaciones al paciente tuvieron que haberle dicho,"Vea, primero gire y luego se sienta." Pero en los videos nosotros vamos a verificar si esa fase se seis o cinco de ese artículo que que mandaste si está diferenciada, si no habrá que mezclarla como una sola fase como hicimos en el primer en el primer trabajo. Eh, bueno, me quedo con la tarea de leerme. Está, yo creo que está muy bueno este este artículo, muchachos. Incluso hay unas buenas. De hecho, hasta me la la cinemática en miembros superiores y todo, eh, cosa que está absolutamente a nuestro alcance, ¿no? Pues por el hecho de que tenemos los mismos instrumentos de medición y pues tenemos a nivel temporal el movimiento de cada joint.

### **00:51:10** {#00:51:10}

**Domiciano Rincón:** O sea, que variable es lo que tenemos. Lo que pasa es que pues al tener tanta tantos datos, pues habrá que seguramente hacer un plan de cuáles son los que vamos a implementar para evidenciar lo que evidencian las las revistas. Eh, discussion, no, eso realmente es un megaartículo, está está super bueno eso. Voy a leer este como para tener más ideas de las variables que tenemos, pero les voy a pedir entonces un agregado y es una pequeña descripción de las variables que presenten diferencias significativas en los artículos que ustedes eh han consultado. Y entonces, por ejemplo, si Double Support si presentó diferencias significativas en este artículo, no no lo sé hasta que lo lea, pues, o no lo sabremos hasta que lo leamos, e, pues entonces habrá que decir, bueno, doble support es el tiempo que transcurre entre tan tan tan. Sí, es estoy casi seguro que el el tiempo de doble soporte es entre, por ejemplo, si yo solamente miro una pierna y aterrizo la la pierna, ahí arranca el el tiempo A y luego entonces se mueve la otra pierna y demás. Y luego cuando vuelvo a dar el otro paso, o sea, el tiempo entre aterrizaje y aterrizaje, creo que tiene que ser el double support time. Entonces puede ser que si ese diferencias significativas, entonces uno puede llegar y reportarlo seguramente en la tablita que estamos haciendo como objetivo de implementación, porque al final digamos como que si nosotros empezamos a analizar los datos de esa manera,

### **00:52:37**

**Domiciano Rincón:** sacamos los descriptores, sacamos para pacientes y para controles y vamos a, por ejemplo, no sé, a mostrar el el el dos de las variables diferencias significativas más importantes o tres y hacemos un un gráfico de dispersión probablemente nos vamos a encontrar con unos clústers bastante interesantes. Entonces, uno puede ahí sacar unas discusiones bien chéveres, unas conclusiones bien bacanas y sobre todo lo que necesitamos un clasificador, ¿no? Entonces el clasificador pues ya se puede hacer luego a nivel estadístico, incluso sin recurrir, digamos, al machine learning si es que eh no tenemos el suficiente N para para lograrlo. Pero sí, sí, sí, sí si lo si lo sí creo que lo mejor sería como hacer una breve descripción de las diferencias significativas que se que se han hecho. O sea, yo lo que esperaría, a ver, lo voy a poner en WhatsApp, es como una tabla, a ver, eh, estamos una pequeña tabla de descriptor descriptor sabemos que es, ¿cierto? O la variable en este caso, no sé, global el support, eh, no sé cómo hacer tablas, pero a ver, voy a poner más bien como columna uno, porque aquí no lo puedo representar. Columna dos. la descripción la referencia algo algo como por el estilo de eso.

### **00:54:02**

**Domiciano Rincón:** Entonces allí tendríamos entonces ah bueno, y eso solo para las variables que en los estudios hayan dado diferencias significativas. ¿Listo? Entonces, eso sería como el agregado a ese documento que que están ustedes montando. Listo. Bueno, muchachos, y ya para finalizar, entonces, ¿qué asignación tenemos adicional? Pues creo que los dejaron libre, o sea, no les dejaron como algo adicional, pero bueno, podemos mejorar las partes que tenemos que mejorar en el en el en el documento y sobre todo lo que me interesa es el tema de de de encontrar los descriptores basados pues en las en las referencias que tienes. ¿Listo? Que ese artículo seguramente tiene ese artículo, ese documento tendría que estar listo para la siguiente semana y me lo mandan para yo poder hacerle pues una revisión.

**Heiner Danit Rincon:** Listo, profe.

**Domiciano Rincón:** Ah, eso ya lo vi que lo compartiste, Esteban. Gracias. Vale, s, entonces quedamos cuap, ¿cierto? Estamos a la espera de los datos. Apenas los tenga se los paso para que ahí iniciaríamos una siguiente fase que es e pues sí, organizar seguramente todos los datos que tenemos en en las dos clases que tenemos, o sea, Parkinson y y Control.

### **00:55:45** {#00:55:45}

**Domiciano Rincón:** para tener, digamos, como los datos de una y la otra.

**Esteban Guarin Valencia:** Lo que mandé ahí fueron los anexos, los que hemos ido recolectando hasta el momento.

**Domiciano Rincón:** Vale, de uno. Listo.

**Esteban Guarin Valencia:** De una vez comparto el documento.

**Domiciano Rincón:** Sí, yo creo, yo creo, de hecho ponerlo, yo creo, como descripción del grupo para que nos quede ahí siempre.

**Esteban Guarin Valencia:** Sí, que queda mejor. Listo, ahí ya quedó. Y los anexos también los anesteso, los pongo en la descripción.

**Domiciano Rincón:** Eh, los anexos los pongo, ¿no? Esos. Ah, bueno, sí, creo que la descripción cubre bastante. Sí, sí, podemos ponerlo también.

**Esteban Guarin Valencia:** Listo. Pues no sé si algún compañero quiera decir algún artículo o ya estaría.

**Santiago Gomez Robledo:** Eh, hola, profe. Qué pena. Pues por parte de Arias y Mía eh, tenemos que irnos ya porque Gonzalo va a empezar un reto de computación en la no. Entonces,

**Domiciano Rincón:** Meor dicho.

**Santiago Gomez Robledo:** tenemos que asistir. Qué pena.

**Domiciano Rincón:** No, no, tranquilos, igual creo que la Reu se está por culminar.

**Santiago Gomez Robledo:** Okay. Okay. Entonces,

**Domiciano Rincón:** hasta la tienda.

**Santiago Gomez Robledo:** voy ya. Sí, no, la otra vez duro está un poquito más de una hora. igual ya va a dejar de transcribir y de grabar.

**Domiciano Rincón:** Listo.

### **La transcripción finalizó después de 00:57:25**

*Esta transcripción editable se generó por computadora y puede contener errores. Los usuarios también pueden cambiar el texto después de que se cree.*