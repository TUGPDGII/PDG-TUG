# Estado del Proyecto: PDG-TUG (Timed Up and Go)

## 1. Descripción General y Objetivos
- **Institución:** Universidad ICESI — Proyecto de Grado en Ingeniería Telemática / Sistemas.
- **Equipo:** Esteban Guarin Valencia, Juan José Arias Gallego, Santiago Gómez Robledo, Heiner Danit Rincón Carrillo.
- **Tutores:** Prof. Domiciano Rincón (Track Técnico y Clínico), Prof. Andrés Navarro (Track Documental Académico).
- **Propósito:** Análisis de datos cinemáticos capturados con sensores inerciales (IMUs) y cámaras RGB-D (e-Motion / VIMOV) durante la prueba Timed Up and Go (TUG), extrayendo variables espaciotemporales para clasificar y caracterizar la marcha en pacientes con Enfermedad de Parkinson (EP) frente a controles.

## 2. Alcance y Requisitos
- **OE1:** Procesamiento y acondicionamiento de señales IMU y de pose de cámara.
- **OE2:** Algoritmos de segmentación temporal de las fases del TUG (levantamiento, marcha ida, giro 180°, marcha vuelta, sentado).
- **OE3:** Extracción de variables espaciotemporales biomecánicas.
- **OE4:** Evaluación preliminar de discriminación entre pacientes y controles mediante estadística inferencial (prueba t de Welch) y clasificadores supervisados (sin prometer umbrales fijos como >80%).

## 3. Estado Actual de los Componentes (Punto de Control: 01 de Noviembre de 2026)

### A. Datos y Sensores IMU
- **Dataset local:** 78 grabaciones JSON en `Datos IMUs/`.
- **Criterios de descarte aplicados:** 66 grabaciones aceptadas (58 pacientes con EP, 8 controles sanos) y 12 descartadas (7 pruebas técnicas sin etiqueta, 2 duplicados MD5, 3 registros de doble tarea cognitiva).
- **Segmentación de fases y equivalencia con código predecesor:** Completada exitosamente en **63 de las 66 grabaciones válidas** (95.5% de efectividad). En `Analisis de Datos/PDGI_Colab copy.ipynb` se auditó y restableció la equivalencia matemática y gráfica al 100% respecto al código del proyecto predecesor (filtro Butterworth orden 20 a 3 Hz, umbral de duración mínima de 0.5 s e indexación exacta por `np.diff`), verificada mediante el adaptador `exportar_json_formato_predecesor` con diferencia numérica de `0.000000e+00`.
- **Nuevos módulos de análisis (Reunión #8):** Se incorporaron en `Analisis de Datos/PDGI_Colab copy.ipynb` la gráfica compuesta superpuesta de las 5 fases TUG (Módulo 7), la detección de fases de paso (`SWING` / `STANCE`) en ambos tobillos con clasificación de fase TUG `fase_tug` y conteo de pasos en giro (Módulo 8), y la extracción masiva de biomarcadores con contraste estadístico mediante prueba *t* de Welch y *U* de Mann-Whitney (Módulo 9).

### B. Sistema de Cámaras e-Motion (VIMOV)
- **Dataset local estrictamente TUG (132 capturas en carpeta principal):**
  - **Brigada Santa Marta (`SMR_`):** **103 grabaciones TUG (100% de las pruebas TUG de la brigada)** descargadas de VIMOV correspondientes al 25, 26 y 27 de junio de 2026.
  - **Brigada CST / La Victoria (`CST_`):** **5 grabaciones TUG** capturadas con la cámara Orbbec Astra 2.
  - **Laboratorio y Calibración (`LAB_`):** **24 grabaciones TUG** históricas de validación técnica (octubre de 2024 y 2026).
  - **Segregación de pruebas No-TUG:** 137 archivos correspondientes a protocolos de caminata continua (`Gait Analysis` y `GAIT_COMPLETE`) fueron trasladados a `Datos e-Motion/No_TUG_Gait_Analysis/` para no contaminar el pipeline de segmentación y clasificación TUG.
- **Estandarización global de nomenclatura (100% completada):** Todo el repositorio de `Datos e-Motion/` sigue la convención formal:
  - Bimodales con IMU: `SMR_{FECHA}_{PERSONA_ID}_{CODIGO}_{VIMOV_TEST_ID_SHORT}_raw.json` o `CST_...`
  - Brigada sin IMU: `SMR_{FECHA}_NO_IMU_{VIMOV_TEST_ID_SHORT}_raw.json` o `CST_...`
  - Laboratorio: `LAB_{FECHA}_INTEL_{VIMOV_TEST_ID_SHORT}_raw.json`
- **Anonimización integral y ética:** Limpieza rigurosa de nombres propios y documentos de identidad (`Name`, `Lastname`, `NumberId`), inyectando el bloque `AnonymizedMetadata` con variables demográficas (`Age`, `Genre`, `Height`, `Weight`), sensor utilizado y etiquetas diagnósticas de VIMOV (`Paciente`, `Control`, `Hoehn & Yahr`, `DBS`, etc.).
- **Delimitación de alcance (Acuerdo Reunión #8):** Las cámaras pierden el seguimiento esquelético durante los giros de 180° y en la aproximación de sentado; **no se usarán para segmentar el giro ni para el conteo de pasos en el giro**. Se destinarán exclusivamente a medir la **longitud de zancada** y la **velocidad lineal de desplazamiento** en las fases de marcha recta (ida y vuelta).

### C. Correspondencia IMU ↔ e-Motion (Bimodalidad Confirmada y Reglas Estrictas)
- **Filtro Estricto de Protocolo TUG y Género:** Para certificar un par bimodal como genuino, se exige:
  1. Protocolo estrictamente TUG en ambos dispositivos.
  2. 100% de coincidencia en el sexo/género del participante.
  Se auditaron y descartaron formalmente 5 candidatos por discrepancia de género (incluyendo P17 y P19).
- **Pares Bimodales Validados:** **42 ensayos IMU únicos con par de cámara estrictamente TUG confirmado (100% sexo idéntico)**:
  - **41 pares en Santa Marta (`SMR`)** correspondientes al 25, 26 y 27 de junio de 2026.
  - **1 par en CST / La Victoria (`CST`)** (`temp_BE`, P54) con la cámara Orbbec Astra 2.
  - Las grabaciones restantes de IMU se ejecutaron mientras la cámara registraba marcha continua de 10 m (`Gait Analysis`) o sin activación de cámara.
- **Auditoría Documentada:** Actualizados `Analisis de Datos/Correspondencia_IMU&EMOTION.md`, `Analisis de Datos/Datos_eMotion.csv` y `Analisis de Datos/FichaTecnica_eMotion.md`.

### D. Documento Académico (LaTeX en `OverLeaf/`)
- Compilando sin errores (33 páginas).
- OE4 simplificado de acuerdo a las observaciones del tutor.
- Diagrama metodológico CRISP-DM y cronograma Gantt externo integrados como figuras.

## 4. Trabajos Pendientes Inmediatos (Entrega de Martes / Próximos Pasos)
1. Ejecutar en el entorno de Google Colab el cuaderno actualizado `Analisis de Datos/PDGI_Colab copy.ipynb` para exportar las figuras definitivas y la tabla `df_variables_tug.csv`.
2. Fusionar la rama `refactor` hacia `main`.
3. Consultar con Leonardo / Bod la disponibilidad de datos de video para las fechas restantes de julio.
4. Integrar las conclusiones de la delimitación funcional de cámaras e IMUs en el documento LaTeX (`OverLeaf/PDG-II TUG.tex`).

## 5. Control de Fechas
- **Última revisión integral:** 01 de noviembre de 2026.
- **Último punto de control:** 02 de noviembre de 2026 (Descarga masiva, anonimización y pareo bimodal VIMOV completado).

