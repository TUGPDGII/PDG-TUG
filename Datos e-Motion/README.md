# Repositorio Óptico: Datos e-Motion

## 1. Descripción General

Esta carpeta aloja las capturas cinemáticas tridimensionales adquiridas mediante sistemas de visión artificial por cámaras RGB-D (Intel RealSense D435 y D455F) integradas en el ecosistema e-Motion / VIMOV. Cada registro contiene las trayectorias espaciales cartesianas $(X, Y, Z)$ en metros de articulaciones clave del cuerpo humano muestreadas a una frecuencia nominal de 30 Hz.

El repositorio alberga un total de 225 grabaciones físicas divididas en dos protocolos motores esenciales de evaluación neurológica:
1. **Timed Up and Go (`TUG`):** 130 grabaciones que capturan el ciclo motor compuesto por levantarse de una silla, caminar 3 metros lineales, girar 180°, regresar a la silla y volver a sentarse.
2. **Marcha Continua de 10 metros (`GAIT`):** 95 grabaciones que evalúan la marcha lineal continua a paso cómodo a lo largo de un pasillo de 10 metros, orientada a cuantificar simetría, cadencia, longitud de paso y doble apoyo.

---

## 2. Contenido y Función de Cada Archivo y Carpeta

| Elemento | Tipo | Función en el Proyecto |
| :--- | :---: | :--- |
| **`TUG/`** | Directorio | Contiene las **130 grabaciones ópticas JSON** correspondientes al protocolo *Timed Up and Go*. |
| **`GAIT/`** | Directorio | Contiene las **95 grabaciones ópticas JSON** correspondientes al protocolo de Marcha Continua de 10 metros. |
| **`Inventario_eMotion.csv`** | Archivo CSV | **Catálogo:** (225 registros, 18 columnas). Contiene la caracterización de cada ensayo óptico: `persona_id`, `archivo`, `codigo`, `fecha`, `patient_id`, `test_id`, `tipo`, `sexo`, `nacimiento`, `edad`, `talla`, `sensor`, `tiene_imu`, `archivo_imu`, `id_emotion` (como `IDE{k}`), `subcarpeta`, `protocolo` y `brigada`. |
| **`df_variables_emotion.csv`** | Archivo CSV | **Matriz cinemática de biomarcadores espaciotemporales** (53 columnas). Contiene las variables calculadas a partir del esqueleto 3D: duraciones activas, velocidades lineales de marcha (ida y regreso), cadencia por FFT, longitud media de paso y zancada calculadas mediante descomposición CWT Ricker sobre tobillos, amplitudes de braceo y porcentajes de doble apoyo. |
| **`FichaTecnica_eMotion.md`** | Archivo Markdown | Especificación formal del sistema de visión: resolución y frecuencias de los sensores RGB-D, soporte para esquemas articulares v1.2.0 (19 nodos) y v1.3.0/v0.3.6 (15 nodos), uso de `SpineBase` como ancla pélvica e índices de oclusión articular durante los giros. |
| **`Analisis_eMotion.md`** | Archivo Markdown | Reporte analítico, biomecánico y estadístico formal. Presenta el contraste inferencial mediante pruebas paramétricas (*t* de Welch) y no paramétricas (*U* de Mann-Whitney) entre pacientes con Enfermedad de Parkinson y controles sanos, detallando los biomarcadores con significancia estadística ($p < 0.05$). |
| **`Guia_Pipeline_eMotion.md`** | Archivo Markdown | Documento de fundamentación matemática y metodológica del pipeline de visión artificial: criterios de filtrado digital, algoritmos de detección de pasos mediante CWT Ricker, cálculo de cadencia y derivación cinemática. |

---

## 3. Formato de Nomenclatura de Archivos JSON

Cada grabación óptica dentro de `TUG/` y `GAIT/` sigue una convención estandarizada y unívoca construida a partir del prefijo de dominio **`IDE`** (*Identificador e-Motion*):

### A. Para la prueba Timed Up and Go (`TUG/`):
```text
{ORIGEN}_IDE{NUMERO}_TUG_{IMU_MATCH}.json
```

### B. Para la prueba de Marcha Continua (`GAIT/`):
```text
{ORIGEN}_IDE{NUMERO}_GAIT_{IMU_MATCH}.json
```

### Desglose de Campos:
1. **`{ORIGEN}`:** Procedencia geográfica de la brigada (`LAB`, `SMR` o `CST`).
2. **`IDE{NUMERO}`:** Identificador secuencial de la sesión óptica precedido por `IDE` (ej. `IDE1`, `IDE40`). En las pruebas preliminares de marcha de Costa se utiliza `IDEM1` e `IDEM2`.
3. **`TUG` / `GAIT`:** Protocolo clínico motor evaluado en la sesión.
4. **`{IMU_MATCH}`:** Indica la correspondencia con el inventario inercial:
   * `P{ID}`: Identificador normalizado de la persona (`persona_id`, ej. `P06`, `P52`, `P10`) si la prueba cuenta con registro o ensayo simultáneo en IMUs.
   * `NO`: Indica que la captura óptica se ejecutó como una prueba de visión independiente sin registro inercial sincronizado.

### Ejemplos Reales:
* TUG con par IMU: `PDG-TUG/Datos e-Motion/TUG/SMR_IDE1_TUG_P06.json`
* TUG sin par IMU: `PDG-TUG/Datos e-Motion/TUG/LAB_IDE9_TUG_NO.json`
* GAIT con correspondencia: `PDG-TUG/Datos e-Motion/GAIT/SMR_IDE4_GAIT_P10.json`
* GAIT independiente: `PDG-TUG/Datos e-Motion/GAIT/SMR_IDE73_GAIT_NO.json`
