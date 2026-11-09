# Matriz de Análisis de Riesgos — Proyecto PDG-TUG

Matriz estructurada por objetivo general, productos y actividades de cada objetivo específico del proyecto.

<table>
  <thead>
    <tr>
      <th align="center">Tipo de riesgo</th>
      <th align="center">Descripción del riesgo</th>
      <th align="center">Probabilidad</th>
      <th align="center">Impacto</th>
      <th align="center">Efecto</th>
      <th align="center">Medidas de mitigación</th>
      <th align="center">Supuestos</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="7"><b>Objetivo General:</b> Desarrollar un algoritmo de clasificación para diferenciar pacientes con enfermedad de Parkinson y sujetos de control a partir de variables biomecánicas extraídas de cada fase de la prueba Timed Up and Go (TUG) mediante el análisis conjunto de señales inerciales (IMU) y cámaras de profundidad (RGB-D), integrándolo en la plataforma VIMOV como herramienta de apoyo al diagnóstico clínico objetivo.</td>
    </tr>
    <tr valign="top">
      <td>Operacionales</td>
      <td>Menor cantidad de sujetos de control frente al número de pacientes capturados durante las brigadas médicas.</td>
      <td align="center">Probable</td>
      <td align="center">Mayor</td>
      <td>Puede generar sesgo en las pruebas estadísticas y en el entrenamiento del modelo de clasificación.</td>
      <td>Programar sesiones adicionales de toma de datos con participantes sanos en laboratorio e incorporar controles compatibles del repositorio del grupo.</td>
      <td>Se logra completar una muestra suficiente de participantes de control bajo el mismo protocolo de la prueba.</td>
    </tr>
    <tr valign="top">
      <td>Asociados a fenómenos de origen tecnológico: químicos, eléctricos, mecánicos, térmicos</td>
      <td>Diferencias en el alcance visual, frecuencia de muestreo y sincronización entre los sensores inerciales y las cámaras de profundidad.</td>
      <td align="center">Probable</td>
      <td align="center">Moderado</td>
      <td>Pérdida de seguimiento de las articulaciones en cámara durante los giros y dificultad para cruzar registros entre ambos equipos.</td>
      <td>Utilizar las cámaras para estimar distancias y velocidad en línea recta, y delegar a los sensores inerciales la segmentación de fases y los giros.</td>
      <td>Ambos sistemas funcionan de acuerdo con sus especificaciones técnicas durante las jornadas de captura.</td>
    </tr>
    <tr valign="top">
      <td>De calendario</td>
      <td>Cruces de horario o acumulación de entregas académicas de los integrantes del equipo en cierres de semestre.</td>
      <td align="center">Moderado</td>
      <td align="center">Moderado</td>
      <td>Puede ocasionar retrasos en los tiempos estipulados para las entregas semanales del proyecto.</td>
      <td>Realizar seguimiento semanal los martes con el tutor y dividir las tareas técnicas por subgrupos de trabajo.</td>
      <td>El equipo dispone del tiempo previsto en el cronograma para el desarrollo de las actividades.</td>
    </tr>
    <tr valign="top">
      <td>Legales</td>
      <td>Restricciones asociadas al manejo de datos clínicos y confidencialidad de la información de los participantes.</td>
      <td align="center">Improbable</td>
      <td align="center">Mayor</td>
      <td>Limitaciones para el uso o publicación de los registros si contienen datos personales sin anonimizar.</td>
      <td>Anonimizar todos los archivos antes de subirlos al repositorio, reemplazando datos personales por códigos internos de estudio.</td>
      <td>El tratamiento de los datos cumple con los lineamientos del comité de ética de las instituciones participantes.</td>
    </tr>
    <tr>
      <td colspan="7"><b>Producto 1:</b> Conjunto de datos bimodal (sensores inerciales y cámara de profundidad) depurado, anonimizado y documentado en fichas técnicas.</td>
    </tr>
    <tr valign="top">
      <td>Asociados a fenómenos de origen tecnológico: químicos, eléctricos, mecánicos, térmicos</td>
      <td>Debido a cortes de conexión en campo o desconexión de sensores durante las pruebas, podrían presentarse archivos duplicados o grabaciones incompletas.</td>
      <td align="center">Probable</td>
      <td align="center">Moderado</td>
      <td>Inclusión de muestras repetidas o sin las señales mínimas necesarias para calcular las variables del estudio.</td>
      <td>Revisar la integridad de cada archivo antes del análisis, descartando duplicados y grabaciones que no cuenten con los sensores principales.</td>
      <td>La mayoría de las pruebas recolectadas en las brigadas cuentan con las señales completas en tronco y tobillos.</td>
    </tr>
    <tr valign="top">
      <td>Operacionales</td>
      <td>Omisión o errores de digitación en los datos demográficos registrados manualmente durante las brigadas.</td>
      <td align="center">Probable</td>
      <td align="center">Moderado</td>
      <td>Dificultad para identificar qué grabaciones corresponden a repeticiones de una misma persona.</td>
      <td>Agrupar los registros por fecha de captura y datos demográficos, verificando la correspondencia entre sensores y cámara.</td>
      <td>Los registros cuentan con información base suficiente para identificar a cada participante del estudio.</td>
    </tr>
    <tr>
      <td colspan="7"><b>Producto 2:</b> Algoritmo de segmentación automática de las cinco fases de la prueba TUG validado y ajustado al sistema de captura actual.</td>
    </tr>
    <tr valign="top">
      <td>Asociados a fenómenos de origen tecnológico: químicos, eléctricos, mecánicos, térmicos</td>
      <td>Debido a cambios en la ubicación u orientación de los sensores respecto al proyecto anterior, podrían presentarse errores en la detección de las fases.</td>
      <td align="center">Probable</td>
      <td align="center">Mayor</td>
      <td>Cálculo incorrecto de los tiempos de inicio y fin de levantamiento, caminata, giro o sentado.</td>
      <td>Revisar la orientación de los ejes en los sensores utilizados y ajustar la lectura de datos antes de ejecutar la segmentación.</td>
      <td>Las señales de aceleración y giroscopio reflejan de forma consistente cada transición de la prueba.</td>
    </tr>
    <tr>
      <td colspan="7"><b>Producto 3:</b> Matriz de variables biomecánicas por fase e informe de análisis estadístico y modelos de clasificación.</td>
    </tr>
    <tr valign="top">
      <td>Asociados a fenómenos de origen tecnológico: químicos, eléctricos, mecánicos, térmicos</td>
      <td>Debido a la variabilidad motora entre pacientes en etapas tempranas y al tamaño reducido del grupo control, algunas variables podrían no mostrar diferencias claras entre grupos.</td>
      <td align="center">Probable</td>
      <td align="center">Moderado</td>
      <td>Resultados estadísticos con menor capacidad de separación en variables individuales.</td>
      <td>Priorizar las variables reportadas en la literatura para las fases de giro y marcha, y evaluar distintos modelos de clasificación.</td>
      <td>Las variables extraídas por fase aportan mayor detalle sobre el movimiento que el tiempo total de la prueba.</td>
    </tr>
    <tr>
      <td colspan="7"><b>Producto 4:</b> Módulo funcional de clasificación e ingesta de métricas biomecánicas integrado en la plataforma VIMOV.</td>
    </tr>
    <tr valign="top">
      <td>Asociados a fenómenos de origen tecnológico: químicos, eléctricos, mecánicos, térmicos</td>
      <td>Debido a posibles fallas o incompatibilidades al integrar el módulo de análisis con la plataforma VIMOV, podrían presentarse retrasos en el despliegue.</td>
      <td align="center">Moderado</td>
      <td align="center">Mayor</td>
      <td>Demora en la puesta en operación del cálculo automático y almacenamiento de métricas en la plataforma.</td>
      <td>Definir el formato de entrada y salida de datos antes del desarrollo y realizar pruebas de integración previas al cierre del proyecto.</td>
      <td>Los servicios de almacenamiento y base de datos de la plataforma VIMOV se mantienen operativos para las pruebas.</td>
    </tr>
    <tr>
      <td colspan="7"><b>Producto 5:</b> Informes de avance y documento final de Proyecto de Grado.</td>
    </tr>
    <tr valign="top">
      <td>De calendario</td>
      <td>Incumplimiento en los tiempos internos de redacción y consolidación de los resultados obtenidos en las pruebas.</td>
      <td align="center">Improbable</td>
      <td align="center">Moderado</td>
      <td>Retraso en la entrega del documento para revisión de los tutores y jurados.</td>
      <td>Adelantar la documentación en paralelo con los avances técnicos y revisarla semanalmente con los directores del proyecto.</td>
      <td>Las entregas de documentación se realizan de acuerdo con las fechas definidas por la universidad.</td>
    </tr>
    <tr>
      <td colspan="7"><b>OE1.A1.</b> Explorar y depurar el conjunto de datos bimodal (sensores inerciales y cámara), elaborando las fichas técnicas de las muestras válidas.</td>
    </tr>
    <tr valign="top">
      <td>Asociados a fenómenos de origen tecnológico: químicos, eléctricos, mecánicos, térmicos</td>
      <td>Debido a la mezcla de pruebas de calibración de laboratorio con pruebas clínicas de brigada, podría alterarse el conteo de muestras válidas.</td>
      <td align="center">Probable</td>
      <td align="center">Moderado</td>
      <td>Inclusión de grabaciones de prueba técnica que no corresponden a pacientes ni a controles reales.</td>
      <td>Definir criterios de descarte claros y documentar en una ficha técnica el listado de muestras aceptadas y excluidas.</td>
      <td>Se dispone de las etiquetas y observaciones de campo para distinguir las pruebas clínicas de las pruebas técnicas.</td>
    </tr>
    <tr>
      <td colspan="7"><b>OE1.A2.</b> Recolectar muestras adicionales de sujetos de control sanos para reducir el desbalance entre grupos.</td>
    </tr>
    <tr valign="top">
      <td>Operacionales</td>
      <td>Dificultades logísticas para coordinar voluntarios y equipos de medición en las sesiones complementarias de captura.</td>
      <td align="center">Probable</td>
      <td align="center">Moderado</td>
      <td>Retraso en la ampliación del grupo de control para los análisis comparativos.</td>
      <td>Gestionar con tiempo los permisos de laboratorio, la asistencia a nuevas brigadas y la convocatoria de participantes voluntarios.</td>
      <td>Se cuenta con disponibilidad de los equipos de captura y participación de voluntarios en las fechas programadas.</td>
    </tr>
    <tr>
      <td colspan="7"><b>OE2.A1.</b> Validar y adecuar el algoritmo de segmentación de fases del proyecto anterior sobre las muestras recolectadas en brigadas.</td>
    </tr>
    <tr valign="top">
      <td>Asociados a fenómenos de origen tecnológico: químicos, eléctricos, mecánicos, térmicos</td>
      <td>Debido a variaciones en la tasa de muestreo de los equipos y movimientos previos de los pacientes antes de iniciar la prueba, el algoritmo podría desfasar los cortes de cada fase.</td>
      <td align="center">Probable</td>
      <td align="center">Mayor</td>
      <td>Necesidad de repetir el ajuste de preprocesamiento y validación visual de las señales segmentadas.</td>
      <td>Estandarizar la frecuencia de las señales mediante interpolación antes del filtrado y corroborar gráficamente los cortes de las cinco fases.</td>
      <td>Las señales acondicionadas conservan los patrones de energía necesarios para identificar cada transición.</td>
    </tr>
    <tr>
      <td colspan="7"><b>OE3.A1.</b> Extraer las variables biomecánicas por fase y entrenar los modelos de clasificación supervisada.</td>
    </tr>
    <tr valign="top">
      <td>Asociados a fenómenos de origen tecnológico: químicos, eléctricos, mecánicos, térmicos</td>
      <td>Debido a resultados inferiores a los esperados en el ajuste de los clasificadores o exceso de variables frente al número de muestras, podría presentarse sobreajuste en los modelos.</td>
      <td align="center">Moderado</td>
      <td align="center">Moderado</td>
      <td>Disminución en el desempeño del clasificador al evaluar muestras de nuevos participantes.</td>
      <td>Seleccionar las variables con mayor respaldo estadístico y clínico, utilizando modelos interpretables ajustados al tamaño de la base de datos.</td>
      <td>Los datos disponibles y las variables seleccionadas permiten entrenar y evaluar los modelos de clasificación propuestos.</td>
    </tr>
    <tr>
      <td colspan="7"><b>OE3.A2.</b> Integrar el módulo de procesamiento y clasificación con el almacenamiento y base de datos de la plataforma VIMOV.</td>
    </tr>
    <tr valign="top">
      <td>Administrativos</td>
      <td>Demoras en la asignación de accesos, credenciales o configuración del entorno de servidor por parte de los encargados de la plataforma.</td>
      <td align="center">Moderado</td>
      <td align="center">Moderado</td>
      <td>Aplazamiento de las pruebas finales de ingesta y persistencia de datos en la plataforma VIMOV.</td>
      <td>Solicitar con antelación las credenciales y especificaciones técnicas del servidor, adelantando pruebas en entorno local.</td>
      <td>El equipo técnico de la plataforma facilita oportunamente el acceso y la documentación de integración.</td>
    </tr>
    <tr>
      <td colspan="7"><b>OE4.A1.</b> Evaluar el desempeño del algoritmo de clasificación a nivel de grupos de pacientes y controles mediante métricas de exactitud y sensibilidad.</td>
    </tr>
    <tr valign="top">
      <td>Operacionales</td>
      <td>Debido a que algunos participantes realizaron más de una repetición de la prueba, mezclar grabaciones de una misma persona en entrenamiento y validación sesgaría la evaluación.</td>
      <td align="center">Improbable</td>
      <td align="center">Mayor</td>
      <td>Obtención de métricas de desempeño poco representativas de la capacidad real del algoritmo.</td>
      <td>Agrupar todas las repeticiones por participante para que sus muestras queden siempre en un mismo subconjunto de evaluación.</td>
      <td>El catálogo de datos identifica correctamente todas las grabaciones que pertenecen a cada participante.</td>
    </tr>
  </tbody>
</table>
