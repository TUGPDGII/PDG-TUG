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

## 3. Estado Actual de los Componentes (Punto de Control: 02 de Noviembre de 2026)

### A. Datos y Sensores IMU
- **Dataset local:** 78 grabaciones JSON en `Datos IMUs/`.
- **Criterios de descarte aplicados:** 66 grabaciones aceptadas (58 pacientes con EP, 8 controles sanos) y 12 descartadas (7 pruebas técnicas sin etiqueta, 2 duplicados MD5, 3 registros de doble tarea cognitiva).
- **Segmentación de fases y equivalencia con código predecesor:** Completada exitosamente en **63 de las 66 grabaciones válidas** (95.5% de efectividad). En `Analisis de Datos/PDGI_Colab.ipynb` se auditó y restableció la equivalencia matemática y gráfica al 100% respecto al código del proyecto predecesor (filtro Butterworth orden 20 a 3 Hz, umbral de duración mínima de 0.5 s e indexación exacta por `np.diff`), verificada mediante el adaptador `exportar_json_formato_predecesor` con diferencia numérica de `0.000000e+00`.
- **Nuevos módulos de análisis (Reunión #8):** Se incorporaron en `Analisis de Datos/PDGI_Colab.ipynb` la gráfica compuesta superpuesta de las 5 fases TUG (Módulo 7), la detección de fases de paso (`SWING` / `STANCE`) en ambos tobillos con clasificación de fase TUG `fase_tug` y conteo de pasos en giro (Módulo 8), y la extracción masiva de biomarcadores con contraste estadístico mediante prueba *t* de Welch y *U* de Mann-Whitney (Módulo 9).
- **Resultados estadísticos basales (Módulo 9):** Procesamiento sobre las 66 muestras válidas extrajo biomarcadores preliminares donde los pacientes con EP exhiben una duración efectiva del TUG mayor ($18.20 \pm 11.27$ s vs $13.37 \pm 3.12$ s en controles, $+36.2\%$), un tiempo total de marcha superior ($10.44 \pm 8.82$ s vs $7.10 \pm 4.30$ s, $+47.0\%$) y mayor duración de balanceo de tobillo ($0.50 \pm 0.58$ s vs $0.36 \pm 0.18$ s, $+38.1\%$), cumpliendo la meta fijada por el tutor en R#8 de evidenciar contraste preliminar antes del cierre de semestre.

### B. Sistema de Cámaras e-Motion (VIMOV) — Pipeline Óptico y Segmentación Adaptada
- **Dataset local auditado y estandarizado (225 grabaciones físicas en disco $\to$ 223 series clínicas analizadas):**
  - **Pruebas TUG (`Datos e-Motion/TUG/`, 130 archivos):**
    - **Santa Marta (`SMR_`):** 101 grabaciones clínicas únicas.
    - **CST / La Victoria (`CST_`):** 6 grabaciones válidas (Orbbec Astra 2).
    - **Laboratorio Icesi (`LAB_`):** 23 grabaciones de calibración y validación técnica.
  - **Pruebas de Marcha Continua (`Datos e-Motion/GAIT/`, 95 archivos):**
    - **Santa Marta (`SMR_`):** 81 grabaciones clínicas (77 pacientes con EP, 4 controles).
    - **CST / La Victoria (`CST_`):** 15 grabaciones (13 cinemáticas: 8 pacientes con EP, 5 controles de brigada, más 2 archivos de métricas precalculadas excluidos del análisis cinemático articular).
  - **Estandarización y Depuración de Nomenclatura:** Se renombraron los 225 archivos de e-Motion siguiendo el estándar formal `{ORIGEN}_{ID_EMOTION}_eMotion_{IMU_MATCH}_{TIPO}.json` (ej. `LAB_ID1_eMotion_NO_TUG.json`, `SMR_ID1_eMotion_P06_TUG.json`, `CST_ID1_eMotion_P54_TUG.json`, `SMR_ID1_eMotion_P06_GAIT.json`, `CST_M1_eMotion_NO_GAIT.json`), eliminando fechas y asignando identificador secuencial propio y correspondencia unívoca (`NO` o `P#` del IMU pareado).
  - **Depuración Física de Duplicados y Pruebas Internas:** Se eliminaron físicamente del disco los 44 archivos descartados (2 pruebas de personal interno y 42 réplicas exactas de sincronización en nube), consolidando el inventario en 225 archivos y depurando íntegramente `Datos e-Motion/Analisis_eMotion.md`.
  - **Trazabilidad de Sujetos y Pareo Intra-Sujeto:** Se identificaron **71 sujetos únicos en VIMOV** (cohortes `LARGE_PD` y `GEOREF`), de los cuales **48 pacientes cuentan simultáneamente con prueba TUG y prueba de Marcha Continua de 10 m**.
  - **Dos Generaciones de Esquema Articular:**
    - `v1.2.0` (75 archivos en disco): 19 articulaciones (sin nodo `BodyCenter`).
    - `v1.3.0` / `v0.3.6` (148 archivos en disco): 15 articulaciones (con `BodyCenter`).
    - `SpineBase` presente en el 100% de las 223 grabaciones esqueléticas como nodo pélvico universal (`Hip Center`).
- **Cobertura Empírica Real de las 5 Fases TUG en Cámara ($n=130$):**
  - **Fase 1 (`Levantamiento`):** Capturada en el 96.9% de los archivos (88.5% completa con $\Delta Y \ge 0.18\text{ m}$ y 8.5% parcial).
  - **Fases 2 y 4 (`Marcha 1 Ida` y `Marcha 2 Regreso`):** Capturadas en el 100.0% de los archivos.
  - **Fase 3 (`Giro de 180°`):** Intervalo temporal $[t_{\text{fin\_ida}}, t_{\text{ini\_vuelta}}]$ 100% delimitable por inversión de signo de $v_z$, con oclusión transitoria de tobillos a $<1.2\text{ m}$, manteniendo el conteo de pasos en giro en los IMUs.
  - **Fase 5 (`Sentado`):** Capturada en el 100.0% de los archivos (84.6% completa y 15.4% parcial).
- **Algoritmo de Segmentación Adaptado e Implementación en Colab (`Módulos 10 a 13` de `Analisis de Datos/PDGI_Colab.ipynb`):**
  - Incorpora interpolación PCHIP a 30.0 Hz, validación espectral FFT (1.0–2.2 Hz), filtrado Butterworth paso bajas a 3.0 Hz (`filtfilt`), macro-segmentación de las 5 fases TUG ($E_z$, $E_y$), y micro-segmentación en tobillos (CWT Ricker 1.0–2.5 Hz, eventos `SWING`/`STANCE`, Doble Apoyo, longitud de paso/zancada, velocidad lineal y amplitud/asimetría de braceo).
- **Hallazgos Estadísticos Significativos en e-Motion (Prueba *t* de Welch):**
  - **En TUG ($n=130$):** Diferencias estadísticamente significativas entre pacientes con EP ($n=102$) y controles ($n=26$) en Longitud de Zancada ($0.839 \pm 0.167\text{ m}$ vs. $0.949 \pm 0.172\text{ m}$, $p = 0.0032$), Longitud de Paso vs. Controles de Brigada ($0.353\text{ m}$ vs. $0.422\text{ m}$, $p = 0.0034$), Amplitud de Braceo ($0.270\text{ m}$ vs. $0.315\text{ m}$, $p = 0.0065$), Duración Activa TUG ($15.91\text{ s}$ vs. $13.26\text{ s}$, $p = 0.0082$) y Asimetría de Braceo ($22.74\%$ vs. $16.71\%$, $p = 0.0347$).
  - **En Marcha Continua de 10 m (`GAIT`, $n=93$):** Incremento estadísticamente significativo en el Porcentaje de Doble Apoyo (`pct_doble_apoyo`) en pacientes con EP ($25.07 \pm 7.32\%$) frente a controles sanos ($18.23 \pm 6.96\%$, $t = +2.31, p = 0.0206$), además de mayor duración activa ($19.30\text{ s}$ vs. $14.27\text{ s}$, $p = 0.0099$).
- **Documentación y Matrices Actualizadas:** Consolidados `Datos e-Motion/Analisis_eMotion.md` (purgado de descartes), `Datos e-Motion/FichaTecnica_eMotion.md`, `Datos e-Motion/Inventario_eMotion.csv` (inventario y catálogo simplificado de 12 metadatos clave para los 225 archivos físicos) y `Datos e-Motion/df_variables_emotion.csv` (matriz exhaustiva de 53 columnas con biomarcadores biomecánicos, variables clínicas y demográficas de 223 grabaciones).

### C. Dataset Bimodal Sincronizado 1:1 (`Datos IMU&eMotion/`)
- **Búsqueda exhaustiva en VIMOV:** Conexión mediante token de investigación Auth0 sobre la cohorte de la brigada ($\pm 10$ días, del 15 de junio al 15 de julio de 2026). Se evaluaron 95 pacientes con registro bimodal (`has_emotion: true` y `has_imus: true`).
- **Verificación 1:1 Estricta:** Cotejo simultáneo de protocolo (ambos `TIMED_UP_AND_GO`), alineación temporal con compensación horaria Colombia UTC-5 ($|\Delta t| \le 73\text{ s}$, mediana $< 4\text{ s}$) y emparejamiento biyectivo estricto (un e-Motion por un IMU).
- **Consolidación en Disco (`Datos IMU&eMotion/`):**
  - **53 pares bimodales TUG sincronizados** (106 archivos JSON individuales):
    - 47 pares en la Brigada Santa Marta (25, 26 y 27 de junio de 2026, sensor Intel RealSense D455F).
    - 6 pares en la Brigada CST / La Victoria (04 de julio de 2026, sensor Orbbec Astra 2).
  - Nomenclatura unívoca pareada por ID:
    - IMU: `IMU&eMotion/Brigada_ID{k}_IMU_TUG.json`
    - e-Motion: `IMU&eMotion/Brigada_ID{k}_eMotion_TUG.json`
  - Estandarización de los 4 archivos fundamentales por carpeta de datos cumplida:
    - `Analisis_1a1.md`: Correlación de Pearson ($r = 0.7458, p = 4.13 \times 10^{-9}$) y concordancia cinemática.
    - `df_variables_1a1.csv`: Matriz bimodal de 39 columnas cruzando biomarcadores inerciales y ópticos.
    - `FichaTecnica_1a1.md`: Especificación técnica del protocolo bimodal y trazabilidad.
    - `Inventario_1a1.csv` e `Inventario_Brigada_1a1.json`: Catálogo unificado y manifiesto VIMOV.
- **Implementación de Módulo 14 en `Analisis de Datos/PDGI_Colab.ipynb`:**
  - Sección interactiva `@param par_bimodal_a_comparar` (selector de 1 a 53).
  - Procesamiento, alineación de origen en despegue de silla ($t_{\text{lift}} = 0$) y visualización bimodal:
    - Gráfica lado a lado (IMU yaw y 5 fases vs. e-Motion profundidad $Z$, velocidad $v_z$ y macrofases).
    - Gráfica combinada superpuesta en amplitud normalizada $[0, 1]$ con anotaciones explícitas de los 3 hitos de coincidencia biomecánica (Despegue, Giro 180° y Sentado).
    - Tabla cuantitativa de concordancia ($\Delta t_{\text{giro}}$, $\Delta T_{\text{activa}}$) y veredicto de sincronía.

### D. Estandarización Estructural de Carpetas de Datos
Cada uno de los tres repositorios de datos contiene ahora sus 4 archivos esenciales homogéneos:
1. `Datos e-Motion/`: `Analisis_eMotion.md`, `df_variables_emotion.csv`, `FichaTecnica_eMotion.md`, `Inventario_eMotion.csv`.
2. `Datos IMUs/`: `Analisis_IMUs.md`, `df_variables_IMUs.csv`, `FichaTecnica_IMUs.md`, `Inventario_IMUs.csv` (simplificado a 13 columnas esenciales).
3. `Datos IMU&eMotion/`: `Analisis_1a1.md`, `df_variables_1a1.csv`, `FichaTecnica_1a1.md`, `Inventario_1a1.csv`.

### E. Documento Académico (LaTeX en `OverLeaf/`)
- Compilando sin errores (33 páginas).
- OE4 simplificado de acuerdo a las observaciones del tutor (sin umbrales artificiales como >80%).
- Diagrama metodológico CRISP-DM y cronograma Gantt externo integrados como figuras.
- Formalizada la delimitación funcional bimodal en la Sección 3.2: cámaras RGB-D para longitud de zancada y velocidad lineal en marcha continua; IMUs para giros, pasos en giro y transiciones posturales.

## 4. Trabajos Pendientes Inmediatos (Entrega de Martes / Próximos Pasos)
1. Ejecutar en el entorno de Google Colab el cuaderno actualizado `Analisis de Datos/PDGI_Colab.ipynb` para exportar las figuras definitivas y la tabla `df_variables_IMUs.csv`.
2. Fusionar la rama `refactor` hacia `main` en el repositorio remoto.
3. Consultar con Leonardo / Bod la disponibilidad de datos de video para las fechas restantes de julio.

## 5. Control de Fechas
- **Última revisión integral:** 01 de noviembre de 2026.
- **Último punto de control:** 07 de noviembre de 2026 (Reorganización de carpetas de datos, estandarización de 4 archivos clave por carpeta, simplificación de Inventario IMUs, incorporación de Módulo 14 bimodal 1:1 en Colab).

