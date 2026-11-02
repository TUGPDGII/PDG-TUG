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
- **Dataset local:** 30 archivos `*_raw.json` (25 Intel RealSense D455/D455F y 5 Orbbec Astra 2) + 2 archivos procesados en `Datos e-Motion/`.
- **Delimitación de alcance (Acuerdo Reunión #8):** Las cámaras pierden el seguimiento esquelético durante los giros de 180° y en la aproximación de sentado; **no se usarán para segmentar el giro ni para el conteo de pasos en el giro**. Se destinarán exclusivamente a medir la **longitud de zancada** y la **velocidad lineal de desplazamiento** en las fases de marcha recta (ida y vuelta).

### C. Correspondencia IMU ↔ e-Motion
- **Auditoría completa ejecutada:** Documentada en `Analisis de Datos/Correspondencia_IMU&EMOTION.md`.
- **Hallazgo principal:** Existen **6 grabaciones IMU con par temporal exacto ($\le 60$ s)** en e-Motion, todas correspondientes a la brigada del 04 de julio de 2026 (`temp_BE`, `temp_AM`, `temp_P`, `temp_Z` x2, `temp_AN`).
- **Nomenclatura vs. Timestamp:** Se demostró que los archivos con prefijo de nombre `20260820...` contienen internamente estampas Unix de captura del 04 de julio de 2026.
- Las 72 grabaciones IMU restantes no cuentan con par de video en los archivos RAW locales actuales (pendientes de descargas adicionales de VIMOV / Bod).

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
- **Último punto de control:** 01 de noviembre de 2026 (post-Reunión #8).

