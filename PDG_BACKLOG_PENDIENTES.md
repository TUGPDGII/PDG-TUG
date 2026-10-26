# 📋 BACKLOG TÉCNICO — PDG TUG-V2
### Panel de Control de Tareas Pendientes y Avances
> **Basado en:** Reuniones con Prof. Domiciano Rincón (Reuniones #3 al #7) + análisis del estado real del repositorio.
> **Generado:** 22 de octubre de 2026 · Semana 12 del semestre.
> **Responsable de revisión:** Equipo completo — Esteban, Santiago, JJ, Heiner.
> **PRIORIDAD MÁXIMA** del tutor: avanzar en desarrollo técnico / preprocesamiento. La documentación va en segundo plano.

---

## 🔴 ESTADO CRÍTICO — URGENTE (Esta semana, máx. semana 12–13)

> ⛔ **Advertencia:** Domi fue **muy enfático** en Reunión #7: estamos en semana 12, queda apenas un mes de semestre. El preprocesamiento de señales **debe completarse ya**, o el segundo semestre arranca corriendo sin insumos para el clasificador.

### BLOQUE A — Preprocesamiento Masivo de Señales IMU

- [x] **A1. Ejecutar el Módulo 1 del notebook sobre los 78 archivos reales de `Datos IMUs/`**
  - El módulo ya detecta la carpeta local automáticamente
  - Verificar que cargue los 78 JSON correctamente
  - **Estado actual:** La función `detectar_entorno()` existe pero el notebook solo tiene 7 celdas ejecutadas de 30 — **NO está corriendo sobre todos los datos**

- [x] **A2. Ejecutar el Módulo 2 (Identificación de Personas) y comparar con `personas.csv`**
  - `personas.csv` ya existe con 78 filas (79 contando el header)
  - Confirmar que `persona_id` esté bien asignado en todos los casos
  - Cruzar resultado con el resumen de Reunión #6: 61 PATIENT + 7 CONTROL + 7 SIN_ETIQUETA
  - **Estado actual:** El CSV fue generado con `identificar_personas.py` — ✅ base lista, pero no está integrada en el flujo del notebook

- [x] **A3. Ejecutar el Módulo 3 (Criterios de Descarte) sobre todos los archivos**
  - Los 5 criterios están implementados en `evaluar_criterios_descarte()`
  - Generar el cuadro de auditoría final con columnas: `archivo`, `persona_id`, `tipo`, `estado` (ACEPTADO / DESCARTADO), `motivo_principal`, `duracion_s`, `min_sensores_ok`, `tiene_warning`
  - **Estado actual:** La función existe en el código pero **NO se ha ejecutado sobre el dataset completo**

- [x] **A4. Ejecutar el Módulo 4 (Mapeo IMU a 50 Hz) sobre todas las muestras aceptadas**
  - Remuestreo a 50 Hz por interpolación lineal
  - Estandarización de nombres de sensores (`BASE-SPINE`, `LEFT-ANKLE`, `RIGHT-ANKLE`)
  - **Estado actual:** Función `_clave_sensor()` lista, pendiente ejecución masiva

- [ ] **A5. Ejecutar el Módulo 5 (Segmentación de Fases) sobre TODAS las muestras aceptadas**
  - La corrección del fallo de sentado ya fue implementada (umbral adaptativo)
  - ⚠️ Actualmente `muestra_archivo = "20260625140851_temp_AR.json"` — solo corre sobre **UNA sola muestra hardcodeada**
  - Convertir en loop sobre todas las muestras aceptadas por el Módulo 3
  - Guardar resultados: tiempos de inicio/fin de cada fase por archivo
  - **Estado actual:** ❌ Solo visualiza una muestra, no procesa el dataset completo

- [ ] **A6. Ejecutar el Módulo 6 (Detección de Giros) sobre TODAS las muestras aceptadas**
  - `muestra_giro = "20260627150939_temp_R.json"` — igual, solo una muestra hardcodeada
  - Expandir a loop masivo
  - Guardar métricas de giro por muestra: duración, pico de guiñada (yaw), número de pasos durante el giro
  - **Estado actual:** ❌ Solo visualiza una muestra

> 💡 **Sugerencia técnica:** Añadir un **Módulo 7** que ejecute el pipeline completo (M1 → M2 → M3 → M4 → M5 → M6) en loop sobre todos los archivos y genere un DataFrame consolidado `df_resultados.csv` con todas las variables extraídas por muestra. Esto es el insumo directo para el análisis estadístico.

---

### BLOQUE B — Ficha Técnica Formal del Dataset (✅ COMPLETADO)

> ℹ️ **Estado:** Generada mediante `Analisis de Datos/generar_ficha_tecnica.py`. Documento oficial disponible en `Analisis de Datos/FICHA_TECNICA_DATASET.md` y auditoría completa en `Analisis de Datos/auditoria_descartes.csv`.

- [x] **B1. Generar la Ficha Técnica oficial del dataset con los siguientes campos:**

| Campo | Valor Consolidado Oficial |
|-------|--------------------------|
| Total archivos JSON | **78** |
| PATIENT (antes de descarte) | **63** (54 personas únicas) |
| CONTROL (antes de descarte) | **8** (7 personas únicas) |
| SIN_ETIQUETA (pruebas técnicas) | **7** (4 personas aparentes, sin paciente real) |
| Duplicados exactos (MD5) | **2** (temp_BA_2, temp_Z_2) |
| PATIENT válidos (tras descarte) | **58 grabaciones** (54 personas únicas) |
| CONTROL válidos (tras descarte) | **8 grabaciones** (7 personas únicas) |
| Total grabaciones aceptadas | **66** (84.6% retención) |
| Total grabaciones descartadas | **12** (15.4%) |
| Muestras con < 3 sensores | **4** (subsumidas en pruebas técnicas) |
| Muestras con warnings técnicos | **0 en válidos** (desconexiones en pruebas técnicas) |
| Muestras de Doble Tarea (Dual Task) | **3** (temp_AZ, temp_J, temp_AQ — Paciente P17) |
| Kit K1 vs Kit Base en válidos | **42 con K1 / 24 con Base** |
| Rango de fechas de brigadas | Feb 2026 – Jul 2026 |
| Frecuencia de muestreo efectiva | ~49.4 Hz → normalizado a 50.0 Hz |

- [x] **B2. Incluir la ficha técnica en el repositorio como documento oficial Markdown y CSV**
- [x] **B3. Preparar presentación de la ficha técnica para la próxima reunión con Domi**

---

## 🟠 IMPORTANTE — Esta semana / próximas 2 semanas

### BLOQUE C — Verificación de Correspondencia IMU ↔ Cámara

> ℹ️ **Decisión clave acordada en Reunión #7:** Si existe correspondencia temporal entre IMU y cámara, se puede hacer análisis conjunto (y la segmentación por cámara será más sencilla). Si no, son dos análisis independientes.

- [x] **C1. Acceder a la plataforma/repositorio de datos de cámara RGB-D (brigada Santa Marta 24–28 julio)**
  - Domi envió acceso por WhatsApp al grupo
  - Inventario local: 30 archivos `*_raw.json`; 29 declaran TUG y uno `Gait Analysis`. Hay 25 archivos Intel RealSense y 5 Orbbec Astra 2.
  - Los RAW disponibles del 4 de julio incluyen cinco capturas TUG Orbbec y una captura `Gait Analysis`; no hay RAW fechado entre el 24 y el 28 de julio. La atribución a Santa Marta no se puede comprobar con los metadatos locales.

- [x] **C2. Comparar timestamps entre archivos JSON (IMU) y grabaciones de cámara**
  - Se compararon `timestamp`/`endTimestamp` de los seis IMU (`temp_AF`, `temp_BE`, `temp_E`, `temp_Y`, `temp_AY`, `temp_BG`) con `CaptureTest.Date` y el intervalo de `SkeletonLocation` de los RAW. Se asumió hora local Colombia para la cámara porque el RAW no declara zona horaria; falta confirmar la configuración de su reloj.
  - Los timestamps Unix de IMU se convirtieron de UTC a hora de Colombia (UTC-5). Resultado: solo `temp_BE` y `4849da67-9862-4f1a-b960-165cfa5306e7_raw.json` quedan dentro de ±60 s (diferencia entre inicios: +22.536 s); las ventanas observadas se solapan unos 18 s.
  - La coincidencia temporal identifica un candidato, no prueba identidad de persona ni equivalencia de ejecución. No integrar todavía ambas fuentes sin confirmar la correspondencia por una clave o evidencia adicional.

- [x] **C3. Documentar el resultado de la verificación**
  - Tabla de los seis pares y metodología de conversión: `Analisis de Datos/ANALISIS_EMOTION.md`, sección “Bloque C”.
  - La lista IMU corresponde al 4 de julio de 2026; la fecha de brigada indicada aquí es 24–28 de julio. No hay RAW de cámara local de esos días, así que los archivos disponibles no verifican la brigada descrita.
  - Decisión provisional: tratar las fuentes como pipelines independientes; revisar el candidato `temp_BE` únicamente después de confirmar que pertenece a la misma persona y ejecución.

> 💡 **Alcance:** Una coincidencia de timestamps dentro de ±60 s sirve para priorizar una revisión; por sí sola no acredita una muestra pareada.

---

### BLOQUE D — Ajuste del OE4 (✅ COMPLETADO)

> ℹ️ **Estado:** OE4 simplificado en `OverLeaf/PDG-II TUG.tex` (línea 226) conforme a las indicaciones de Domi en R#7 y documento PDF recompilado con éxito.

- [x] **D1. Actualizar el OE4 en `OverLeaf/PDG-II TUG.tex` (línea 226)**
  - **Texto actualizado:**
    > *"...verificando su capacidad de discriminación a través de las métricas de exactitud y sensibilidad."*
- [x] **D2. Recompilar el PDF y verificar compilación (0 errores, 33 páginas)**

---

### BLOQUE E — Diagrama de Metodología en el Documento LaTeX

- [x] **E1.** SVG del diagrama CRISP-DM generado ✅ (`OverLeaf/crispdm_metodologia.svg`)
- [x] **E2. Convertir el SVG a PDF o PNG para compatibilidad con `pdflatex`**
  - `pdflatex` **no soporta SVG nativo** — usar Inkscape o abrirlo en el navegador y exportar como PDF
  - Guardar en `OverLeaf/figures/crispdm_metodologia.pdf` (o `.png` a 300 DPI)
- [x] **E3. Agregar paquete `graphicx` al preámbulo del `.tex` si no existe**
- [x] **E4. Insertar la figura en la sección de Metodología del documento**
  ```latex
  \begin{figure}[htbp]
    \centering
    \includegraphics[width=\textwidth]{figures/crispdm_metodologia}
    \caption{Metodología híbrida del proyecto: ciclos CRISP-DM articulados con integración iterativa en VIMOV.}
    \label{fig:crispdm}
  \end{figure}
  ```
- [ ] **E5. Recompilar y verificar que la figura aparezca correctamente en el PDF**

---

### BLOQUE F — Cronograma (Diagrama de Gantt externo)

> ℹ️ **Domi en Reunión #7:** El Gantt actual con `pgfgantt` muestra rombitos/líneas raras. Generar la imagen por fuera e importarla.

- [x] **F1. Generar el diagrama de Gantt como imagen externa**
  - Herramientas: draw.io, GanttProject, Mermaid JS, o Python con `matplotlib.patches`
  - Basarse en las fechas exactas ya definidas en la Tabla 2 del documento LaTeX
- [x] **F2. Exportar el Gantt como PNG de alta resolución (300 DPI mínimo) o PDF**
- [x] **F3. Reemplazar el bloque `pgfgantt` en el documento por `\includegraphics{figures/cronograma}`**
- [x] **F4. Recompilar y hacer commit**

---

## 🟡 PARA ESTE MES (Semanas 13–15, antes de fin de semestre)

### BLOQUE G — Extracción Masiva de Variables Biomecánicas (OE3 núcleo)

> ℹ️ **Depende directamente del Bloque A**. Sin el pipeline masivo corriendo, no hay variables que analizar. Este es el objetivo técnico central del semestre.

- [ ] **G1. Crear el Módulo 7 en el notebook: Extracción de variables por fase**
  - Para cada muestra aceptada y segmentada, extraer al menos estas variables prioritarias:

| # | Variable | Fase | Sensor | Hipótesis (Domi + Molero) |
|---|---------|------|--------|---------------------------|
| 1 | Duración del giro 180° | F3 | BASE-SPINE | Aumenta en pacientes |
| 2 | Velocidad pico de guiñada (yaw) | F3 | BASE-SPINE | Disminuye en pacientes |
| 3 | Pasos durante el giro | F3 | Tobillos | Aumenta en pacientes |
| 4 | Velocidad de marcha | F2, F4 | Tobillos | Disminuye en pacientes |
| 5 | Duración total TUG | Global | BASE-SPINE | Aumenta en pacientes |
| 6 | Duración transición bípedo (STS) | F1 | BASE-SPINE | Aumenta en pacientes |
| 7 | Variabilidad tiempo de paso | F2, F4 | Tobillos | Aumenta en pacientes |

  - Guardar en `Analisis de Datos/df_variables.csv`

- [ ] **G2. Crear el Módulo 8: Análisis Estadístico de Diferencias Significativas**
  - Para cada variable:
    - Media ± desviación estándar por grupo (PATIENT vs. CONTROL)
    - Shapiro-Wilk → si normal: t-Student; si no: Mann-Whitney U
    - Valor p y decisión (significativo si p < 0.05, idealmente p < 0.01)
  - Guardar tabla de resultados para el capítulo de Resultados del documento
  - Generar boxplots de las variables con diferencias significativas

> 💡 **Frase clave de Domi (R#7):** *"Cuando tengamos un hallazgo con diferencia significativa, ese es el capítulo de resultados. Cada variable con p < 0.01 es un hallazgo."* — No hay que esperar a tener el clasificador completo para tener resultados.

---

### BLOQUE H — Variables de Cámara RGB-D (condicional)

> Solo aplica si el Bloque C confirma correspondencia temporal IMU ↔ Cámara.

- [ ] **H1. Explorar formato JSON de cámara y entender estructura de joints**
- [ ] **H2. Si timestamps NO coinciden: implementar algoritmo de segmentación independiente para cámara**
  - Umbral sobre posición Y del `BASE-SPINE` para detectar levantamiento y sentado
  - Más sencillo que el de IMU (según Domi R#7)
- [ ] **H3. Extraer variables espaciales de cámara**
  - Longitud de zancada (distancia entre `LEFT-ANKLE` y `RIGHT-ANKLE` en plano XZ)
  - Ancho de paso
  - Simetría de codo (si disponible — `LEFT-ELBOW` vs `RIGHT-ELBOW`)

---

### BLOQUE I — Recolección de ~20 Controles Adicionales

> ⚠️ **Acordado Reunión #6.** Dataset actual: **7 controles útiles vs. 61 pacientes** — desbalance severo que afecta cualquier clasificador.

- [ ] **I1. Coordinar con Domi fecha y logística del levantamiento**
  - Personas: estudiantes, profesores, investigadores
  - No requiere Comité de Ética (son controles sanos)
  - Protocolo idéntico al de brigadas (mismo hardware, mismos sensores)
  - Fecha objetivo en cronograma: **01/11/2026 – 15/12/2026**
- [ ] **I2. Ejecutar el mismo pipeline de identificación y descarte sobre datos nuevos**
- [ ] **I3. Consolidar nuevos controles en el dataset principal**

---

## 🟢 LO QUE YA ESTÁ HECHO ✅ (Referencia)

| Ítem | Estado | Archivo/Referencia |
|------|--------|--------------------|
| Documento LaTeX compilando sin errores | ✅ | `PDG-II TUG.tex` |
| OE1–OE3 bien formulados | ✅ | Líneas 222–225 |
| OE4 formulado (texto a simplificar — ver D1) | 🔄 | Línea 226 |
| Tablas cronograma alineadas con OE | ✅ | Tablas 1 y 2 del doc |
| Marco teórico y antecedentes | ✅ | Sección `sec:marco` |
| Tabla de 15 variables biomecánicas | ✅ con fórmulas | `tab:variables` |
| Metodología redactada (CRISP-DM + Ágil) | ✅ | Sección `sec:metodologia` |
| Script `identificar_personas.py` | ✅ | `Analisis de Datos/` |
| `personas.csv` — 78 muestras clasificadas | ✅ | 63 PAT, 8 CTRL, 7 SIN_ETQ |
| `RESUMEN_DATOS.md` — auditoría inicial | ✅ | `Analisis de Datos/` |
| Módulos 1–6 del notebook (funciones escritas) | ✅ código | `PDGI_Clasificación.ipynb` |
| Ejecución masiva del notebook | ❌ Solo 7 celdas ejecutadas | Pendiente — Bloque A |
| Diagrama CRISP-DM en SVG | ✅ generado | `crispdm_metodologia.svg` |
| SVG insertado en LaTeX | ❌ Solo existe el archivo | Pendiente — Bloque E |
| Criterios de descarte implementados (5 reglas) | ✅ código | Módulo 3 del notebook |
| Descarte ejecutado sobre todo el dataset | ❌ | Pendiente — Bloque A |
| Segmentación IMU corregida (1 muestra) | ✅ visualizable | Módulo 5 — AR.json |
| Segmentación masiva sobre todos los archivos | ❌ | Pendiente — A5 |
| Detección de giro (1 muestra) | ✅ visualizable | Módulo 6 — R.json |
| Detección de giro masiva | ❌ | Pendiente — A6 |
| Ficha técnica formal del dataset | ❌ | Pendiente — Bloque B |
| Análisis IMU ↔ Cámara (correspondencia) | ❌ No iniciado | Pendiente — Bloque C |
| Extracción de variables biomecánicas | ❌ No iniciado | Pendiente — Bloque G |
| Análisis estadístico (hipótesis) | ❌ No iniciado | Pendiente — G2 |
| Recolección de 20 controles adicionales | ❌ No iniciado | Pendiente — Bloque I |
| Diagrama Gantt externo | ❌ | Pendiente — Bloque F |
| Repositorio GitHub privado con datos | ✅ autorizado por Domi | Repo actual |

---

## 📌 NOTAS Y ADVERTENCIAS CLAVE

**Reunión #7 — Frase textual de Domi:**
> *"Dos tracks: conmigo trabajan el proyecto técnico; con Navarro trabajan el documento PDG. No los mezclen ni les asignen el mismo peso de esfuerzo. El proyecto es lo primero."*

**Sobre el análisis estadístico:**
> *"Lo peor que podemos hacer para el objetivo es poner 'nuestro clasificador dará más del 80% de precisión'. No lo podemos saber."* — No comprometerse con umbrales numéricos en el OE4.

**Sobre la urgencia:**
> *"Estamos en semana 12, ya estamos cerca del final del semestre, estamos a un mes más o menos. No quisiera que solamente hiciéramos algoritmo de corte hasta el final del semestre."* — Reunión #7

**Hipótesis principal de la literatura:**
> Fase de giro de 180° es la más sensible para diferenciar pacientes de controles (Molero-Mateo et al., 2026). El paciente da más pasos y tarda más. Empezar análisis estadístico por ahí.

**Data leakage en clasificador:**
> Usar **GroupKFold** en lugar de KFold simple para evitar que tomas del mismo paciente aparezcan en train y test simultáneamente.

---

## 🗓️ HITOS Y FECHAS CLAVE

| Hito | Fecha objetivo | Bloque |
|------|---------------|--------|
| Ficha técnica del dataset | **Inmediato** | B |
| Pipeline masivo ejecutado (M1–M6) | Semana 12–13 | A |
| Verificación IMU ↔ Cámara | Semana 12–13 | C |
| OE4 simplificado en LaTeX | **Esta semana** | D |
| SVG metodología en LaTeX | Próximas 2 semanas | E |
| Gantt externo en LaTeX | Próximas 2 semanas | F |
| Extracción de variables biomecánicas | Semana 13–14 | G |
| Análisis estadístico basal | Semana 14–15 | G |
| Inicio recolección controles (+20) | 01/11/2026 | I |
| Fin recolección controles | 15/12/2026 | I |
| Reunión con Navarro | ~finales Oct / inicio Nov | — |
| Cierre PDG-I | Enero 2027 | — |
| Inicio PDG-II — Modelado y clasificación | 01/02/2027 | — |
| Sustentación pública de grado | 31/05/2027 | — |

---

## 📂 ESTADO DEL REPOSITORIO

```
PDG-TUG-V2/
├── Analisis de Datos/
│   ├── PDGI_Clasificación.ipynb   ← 6 módulos escritos, PENDIENTE ejecución masiva
│   ├── RESUMEN_DATOS.md           ✅ completo
│   ├── identificar_personas.py    ✅ completo
│   └── personas.csv               ✅ 78 filas
├── Datos IMUs/
│   └── [78 archivos .json]        ✅ Dataset completo disponible localmente
├── Notas_Reuniones/
│   └── Reunion3.md–Reunion7.md    ✅ Documentadas
├── OverLeaf/
│   ├── PDG-II TUG.tex             ✅ Compilando (OE4 pendiente simplificación — Bloque D)
│   ├── PDG-II TUG.pdf             ✅ 33 páginas, sin errores
│   ├── crispdm_metodologia.svg    ✅ Generado (pendiente inserción en LaTeX — Bloque E)
│   └── [archivos aux, log…]
├── crispdm_metodologia.svg        ← Duplicado en raíz (mover a OverLeaf/figures/)
├── README.md                      ✅ Existe
└── PDG_BACKLOG_PENDIENTES.md      ← Este documento
```

---

*Documento de gestión temporal — actualizar en cada reunión o al completar ítems.*
*Última actualización: 22 octubre 2026.*
