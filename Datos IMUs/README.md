# Repositorio Inercial: Datos IMUs

## 1. Descripción General

Esta carpeta constituye el repositorio central de series temporales inerciales adquiridas mediante sistemas de unidades de medición inercial corporal (IMUs) durante la ejecución del protocolo clínico motor *Timed Up and Go* (TUG). Cada registro captura aceleraciones lineales triaxiales ($\text{m/s}^2$), velocidades angulares de giro ($\text{rad/s}$ y $\text{deg/s}$) y orientación espacial muestreadas a una frecuencia nominal de 50 Hz.

El conjunto abarca un total de 78 grabaciones crudas obtenidas en campañas de evaluación clínica en Bogotá (Laboratorio), Santa Marta y La Victoria (Costa), orientadas al análisis cinemático cuantitativo de la marcha, transferencias posturales y detección de biomarcadores discriminantes en pacientes con Enfermedad de Parkinson frente a controles sanos.

---

## 2. Contenido y Función de Cada Archivo y Carpeta

| Elemento | Tipo | Función en el Proyecto |
| :--- | :---: | :--- |
| **`IMUS/`** | Directorio | Contiene los **78 archivos JSON crudos** con las series temporales inerciales completas de cada prueba TUG. |
| **`Inventario_IMUs.csv`** | Archivo CSV | **Catálogo maestro inmutable** (78 registros, 26 columnas). Contiene los metadatos clínicos y demográficos normalizados (`persona_id`, `archivo`, `codigo`, `fecha`, `patient_id`, `test_id`, `tipo`, `sexo`, `nacimiento`, `edad`, `talla`, `sensor`, kit y observaciones). No es sobreescrito por cuadernos de análisis. |
| **`df_variables_IMUs.csv`** | Archivo CSV | **Matriz técnica consolidada y de control de calidad** (29 columnas). Aloja los dictámenes determinísticos (`criterio_calidad`, `motivo_descarte`, `detalle_motivos`), parámetros técnicos de la señal (`duracion_s`, `pausa_ms`, `inicio_ms`, `fin_ms`, `md5`) y biomarcadores cinemáticos extraídos tras la segmentación de fases. Es actualizada por el pipeline de análisis en `Analisis de Datos/PDGI_Colab.ipynb`. |
| **`SegmentacionFases_IMUs.csv`** | Archivo CSV | **Matriz de segmentación temporal** (33 columnas). Registra marcas de tiempo absolutas y duraciones de las 5 fases cinemáticas del TUG (Sit-to-Stand, Caminata Ida, Giro 180°, Caminata Vuelta, Stand-to-Sit), junto con las fases de apoyo (*stance*) y balanceo (*swing*) para ambos tobillos. |
| **`Cruce_VIMOV_IMUs.csv`** | Archivo CSV | **Matriz de auditoría y trazabilidad clínica**. Corrobora de forma exhaustiva los 78 archivos locales contra los registros de la plataforma central VIMOV mediante correspondencia temporal exacta al segundo (69 archivos) o ternas demográficas clínicas unívocas. |
| **`FichaTecnica_IMUs.md`** | Archivo Markdown | Especificación técnica formal del instrumental inercial, topología de colocación corporal de los sensores (espina dorsal base y tobillos), frecuencias de muestreo y fundamentación de los 5 criterios determinísticos de descarte de calidad. |
| **`Analisis_IMUs.md`** | Archivo Markdown | Reporte técnico y clínico exhaustivo sobre la cohorte inercial: tasas de retención (66 aceptadas / 12 descartadas), caracterización demográfica, análisis de pausas de adquisición y resultados del contraste estadístico preliminar entre clases. |

---

## 3. Formato de Nomenclatura de Archivos JSON

Todos los archivos de datos inerciales alojados en la subcarpeta `IMUS/` siguen una estructura de nomenclatura uniforme, compacta y desambiguada mediante el prefijo de dominio **`IDI`** (*Identificador Inercial*):

```text
{ORIGEN}_IDI{NUMERO}_{CODIGO}.json
```

### Desglose de Campos:
1. **`{ORIGEN}`:** Código de tres letras que indica la procedencia geográfica y logística de la prueba:
   * `LAB`: Ensayos adquiridos en el Laboratorio de Bogotá (ID 1 al 9).
   * `SMR`: Capturas obtenidas en la brigada clínica de Santa Marta (ID 1 al 55).
   * `CST`: Capturas realizadas en la brigada de Costa / La Victoria (ID 1 al 14).
2. **`IDI{NUMERO}`:** Identificador secuencial numérico dentro de cada sede de origen precedido por `IDI` para distinguirlo de otras modalidades sensoriales (ej. `IDI1`, `IDI10`).
3. **`{CODIGO}`:** Alias o código clínico alfanumérico original asignado en la aplicación de campo al momento de la captura (ej. `BF`, `AR`, `Z`, `BI`, `AL`).

### Ejemplos Reales:
* `PDG-TUG/Datos IMUs/IMUS/SMR_IDI1_BF.json`
* `PDG-TUG/Datos IMUs/IMUS/LAB_IDI8_AL.json`
* `PDG-TUG/Datos IMUs/IMUS/CST_IDI10_BI.json`
