# 📋 BACKLOG TÉCNICO — PDG TUG-V2
### Panel de Control de Tareas Pendientes y Avances
> **Basado en:** Reuniones con Prof. Domiciano Rincón (Reuniones #3 al #8) + análisis del estado real del repositorio.
> **Última actualización:** 01 de noviembre de 2026 (Incorporación exhaustiva de la Reunión #8 del 27 de octubre).
> **Responsable de revisión:** Equipo completo — Esteban, Santiago, JJ, Heiner.
> **PRIORIDAD MÁXIMA** del tutor: avanzar en desarrollo técnico, preprocesamiento y resultados estadísticos basales.

---

## 🔴 ESTADO CRÍTICO — URGENTE (Esta semana, entrega de martes / Semanas 12–13)

> ⛔ **Directriz Central de Reunión #8:** 
> 1. El algoritmo de segmentación IMU logró procesar **63 de 66 muestras** de forma robusta.
> 2. Las cámaras no son aptas para giros ni para la fase completa de sentado, pero son la fuente primaria para **tamaño de zancada** y **velocidad** (fases de marcha 1 y 2).
> 3. Se debe generar la gráfica compuesta superpuesta y la clasificación de fases por paso en la tabla CSV.
> 4. Se debe auditar el cruce temporal IMU ↔ e-Motion y consolidar la ficha técnica de video.

---

### BLOQUE A — Preprocesamiento y Segmentación Masiva de Señales IMU

- [x] **A1. Carga masiva sobre los 78 archivos de `Datos IMUs/`**
  - Implementado y verificado en scripts del repositorio.
- [x] **A2. Identificación de Personas (`Datos_IMUs.csv`)**
  - Consolidado en `Analisis de Datos/Datos_IMUs.csv` (78 filas: 63 PAT, 8 CTRL, 7 SIN_ETIQUETA).
- [x] **A3. Ejecución de Criterios de Descarte Clínicos y Técnicos**
  - 66 muestras aceptadas (84.6% retención) y 12 descartadas (7 técnicas, 2 duplicados, 3 doble tarea).
- [x] **A4. Mapeo y Normalización a 50 Hz**
  - Interpolación y estandarización de nombres de sensores (`BASE-SPINE`, `LEFT-ANKLE`, `RIGHT-ANKLE`).
- [x] **A5. Ejecución del Algoritmo de Segmentación de Fases IMU Masivo**
  - **Avance presentado en R#8 por JJ Arias:** Segmentación completada con éxito en **63 de las 66 grabaciones válidas** (95.5% de éxito operativo). Las 3 muestras restantes presentaron ausencia de dinámica de tronco.
- [ ] **A6. Implementar Tareas Específicas solicitadas en R#8:**
  - [x] **A6.1. Gráfica Compuesta Superpuesta:** Implementada en el Módulo 7 (`segmentar_cinco_fases_tug` y `graficar_fases_superpuestas_tug`) de `Analisis de Datos/PDGI_Colab copy.ipynb`, superponiendo la señal de energía de flexo-extensión de tronco (`espina_base`, canal `b`) y la señal de energía de guiñada (`espina_base`, canal `a`) con líneas verticales discontinuas y franjas de delimitación de las 5 fases TUG.
  - [x] **A6.2. Clasificación de Fases por Paso en el CSV:** Implementada en el Módulo 8 (`detectar_pasos_registro_completo` y `detectar_pasos_intervalo`) de `Analisis de Datos/PDGI_Colab copy.ipynb`, añadiendo la columna `fase_tug` a la tabla de eventos `STANCE`/`SWING` de ambos tobillos y cuantificando los eventos de paso ejecutados durante el giro de 180°.
  - [ ] **A6.3. Fusión de Rama (`merge`):** Fusionar la rama `refactor` hacia `main` en el repositorio remoto.

---

### BLOQUE B — Fichas Técnicas Formales del Dataset (✅ COMPLETADO)

- [x] **B1. Ficha Técnica Oficial de Datos IMU**
  - Generada y disponible en `Analisis de Datos/FichaTecnica_IMUs.md`.
- [x] **B2. Ficha Técnica Oficial de Cámaras e-Motion (VIMOV)**
  - Generada y actualizada en `Analisis de Datos/FichaTecnica_eMotion.md`. Documenta exhaustivamente las 269 capturas (132 TUG y 137 Marcha Continua), 0 duplicados (SHA-256), 0 corruptos, su aptitud para distancias/velocidades lineales (fases 1 y 2) y su delimitación metodológica formal respecto a giros y sentado acordada con el tutor en R#8.

---

### BLOQUE C — Correspondencia y Trazabilidad IMU ↔ e-Motion (✅ COMPLETADO)

> ℹ️ **Requerimiento expreso de Reunión #8:** Auditar las fechas de los 78 archivos IMU y cruzarlas con e-Motion / VIMOV para verificar quiénes cuentan con su versión e-Motion.

- [x] **C1. Documento de Correspondencia y Trazabilidad Temporal:**
  - Creado y actualizado en `Analisis de Datos/Correspondencia_IMU&EMOTION.md`.
  - Contiene la tabla auditora de las **78 grabaciones IMU**.
- [x] **C2. Resolución de Fechas de la Brigada Santa Marta:**
  - Se descubrió que la brigada en Santa Marta se realizó entre el **25 y el 27 de junio de 2026** (no a finales de julio).
- [x] **C3. Descarga Masiva, Anonimización y Pareo Bimodal (VIMOV):**
  - **Dataset e-Motion estrictamente TUG:** 132 grabaciones TUG consolidadas en `Datos e-Motion/TUG/` (103 Santa Marta, 5 CST, 24 Lab).
  - **Segregación de pruebas No-TUG:** 137 grabaciones de marcha continua libre segregadas en `Datos e-Motion/No_TUG_Gait_Analysis/`.
  - **Regla Estricta de Género:** Descartados formalmente 5 candidatos por discrepancia de sexo (`P17`, `P19`, `P23`, `P29`), consolidando **42 pares bimodales estrictamente TUG con 100% de sexo coincidente** vinculados a las grabaciones IMU.
  - **Estandarización Global de Nombres:** 100% de los archivos renombrados formalmente bajo los prefijos `SMR_`, `CST_` y `LAB_`.
  - **Sincronización en Cuaderno:** Actualizado el Módulo 2 de `Analisis de Datos/PDGI_Colab copy.ipynb` para consumir `Datos_eMotion.csv` y reportar la correspondencia bimodal auditada.
  - Aplicada anonimización estricta (limpieza de nombres propios y cédulas).
  - Validación multivariable confirmada y documentada en `Analisis de Datos/Correspondencia_IMU&EMOTION.md`.

---

## 🟠 IMPORTANTE — Próximas 2 semanas (Semanas 13–14)

### BLOQUE D — Ajuste del OE4 y Documento Académico LaTeX

- [x] **D1. Simplificación de OE4 en `OverLeaf/PDG-II TUG.tex`**
  - Ajustado conforme a la instrucción de no prometer exactitud superior al 80%.
- [x] **D2. Diagramas Metodológico y Cronograma**
  - Metodología CRISP-DM y Gantt externo insertados como figuras en LaTeX.
- [x] **D3. Integración de Conclusiones de Cámaras en el Documento:**
  - Redactado e integrado en la Sección 3.2 de `OverLeaf/PDG-II TUG.tex`: *"las cámaras se emplean para longitud de zancada y velocidad lineal de desplazamiento del centro de masa (Hip Center); las IMUs asumen la segmentación temporal completa, la dinámica de giro de 180° y las transiciones posturales"*.

---

### BLOQUE G — Extracción Masiva de Variables y Análisis Estadístico (OE3)

> ℹ️ **Meta clave de fin de semestre (Domi R#8):** *"Lograr al menos un hallazgo estadístico con diferencia significativa entre pacientes y controles antes de cerrar PDG-I."*

- [x] **G1. Extracción de Variables Biomecánicas Prioritarias (`Analisis de Datos/df_variables_tug.csv`):**
  - Implementado el flujo de procesamiento masivo en el Módulo 9 (`procesar_pipeline_masivo_tug`) de `Analisis de Datos/PDGI_Colab copy.ipynb` sobre las 66 grabaciones válidas, corrigiendo el canal de extracción (`b` con filtro Butterworth orden 20 a 3 Hz) e incorporando variables de giro, marcha, transiciones y conteo de pasos en giro.
- [x] **G2. Aplicación de Pruebas Estadísticas para Grupos Desbalanceados:**
  - Implementada la función `ejecutar_contraste_estadistico_tug` en el Módulo 9 de `Analisis de Datos/PDGI_Colab copy.ipynb` con prueba de normalidad de Shapiro-Wilk, prueba **t de Welch (`equal_var=False`)** y prueba **U de Mann-Whitney**, junto con paneles de diagramas de caja (*boxplots*) comparativos y partición estratificada por sujeto (`GroupKFold` por `persona_id`).

---

### BLOQUE I — Levantamiento de Controles Adicionales (+20)

- [ ] **I1. Convocatoria a Brigada en La Victoria (22–26 Noviembre):**
  - Invitación abierta por el Prof. Navarro y Prof. Domiciano. Cupo para un estudiante de PDG (Juan José interesado; gestionar permisos académicos).
- [ ] **I2. Búsqueda y Aprovechamiento de Controles en Bod / Valle del Lili:**
  - Domiciano autorizó incorporar datos tomados por fuera de la brigada (ej. Valle del Lili) siempre y cuando compartan el mismo diseño experimental.
- [ ] **I3. Jornada de Captura en Laboratorio con Docentes:**
  - Meta: alcanzar al menos ~30 controles pareados por grupo etario.

---

## 🟢 LO QUE YA ESTÁ HECHO ✅ (Referencia Rápida)

| Entregable / Tarea | Estado | Ubicación |
|---|:---:|---|
| Regla Maestra del Proyecto | ✅ | `GEMINI.md` |
| Tabla de correspondencia IMU ↔ e-Motion (78 archivos) | ✅ | `Analisis de Datos/Correspondencia_IMU&EMOTION.md` |
| Ficha Técnica de Cámaras e-Motion | ✅ | `Analisis de Datos/FichaTecnica_eMotion.md` |
| Ficha Técnica de Datos IMU | ✅ | `Analisis de Datos/FichaTecnica_IMUs.md` |
| Segmentación IMU de 63/66 grabaciones | ✅ | Notebook / Scripts en `Analisis de Datos/` |
| Limpieza y clasificación clínica de personas | ✅ | `Analisis de Datos/Datos_IMUs.csv` |
| Documento LaTeX compilando (OE4 ajustado, figuras integradas) | ✅ | `OverLeaf/PDG-II TUG.pdf` |
| Minuta completa de Reunión #8 | ✅ | `Notas_Reuniones/Reunion8.md` |

---

## 🗓️ PRÓXIMAS FECHAS Y ENTREGAS

| Hito | Fecha | Responsable |
|---|:---:|:---:|
| **Entrega / Avance de Martes** (Cruce e-Motion, Ficha de cámaras y Gráfica compuesta) | **Martes 03/11/2026** | Equipo |
| Fusión de rama `refactor` a `main` | Inmediato | JJ Arias |
| Salida a Brigada La Victoria | 22–26 Nov 2026 | Delegado de equipo / Domi |
| Cierre PDG-I con hallazgo estadístico basal | Diciembre 2026 | Equipo |
