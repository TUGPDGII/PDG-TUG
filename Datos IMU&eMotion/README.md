# Repositorio Bimodal: Datos IMU&eMotion (1:1)

## 1. Descripción General

Esta carpeta alberga el conjunto de datos bimodal sincronizado 1:1, concebido para la validación cruzada, calibración y contrastación cinemática directa entre dos tecnologías instrumentales complementarias:
1. **Sensores inerciales corporales (IMUs):** Acelerómetros y giróscopos triaxiales colocados en la espalda baja (`SpineBase`) y en ambos tobillos (`LeftAnkle`, `RightAnkle`).
2. **Visión artificial RGB-D (e-Motion):** Seguimiento óptico articular 3D mediante cámaras de profundidad Intel RealSense D455F.

El dataset reúne **53 pares de ensayos simultáneos confirmados (106 archivos JSON pareados)** correspondientes a la prueba motora *Timed Up and Go* (TUG) adquiridos en brigadas clínicas de campo en Santa Marta (pares 1 al 47) y La Victoria / Costa (pares 48 al 53). Cada par bimodal cuenta con marcas de tiempo cronológicas sincronizadas con un desfase absoluto admisible ($\Delta t \le 300\text{ s}$), permitiendo evaluar la correlación estadística ($r = 0.7458$, $p = 4.13 \times 10^{-9}$) y el acuerdo físico directo entre ambas modalidades.

---

## 2. Contenido y Función de Cada Archivo y Carpeta

| Elemento | Tipo | Función en el Proyecto |
| :--- | :---: | :--- |
| **`IMU&eMotion/`** | Directorio | Contiene los **106 archivos JSON** correspondientes a los 53 pares emparejados. Cada par comparte el mismo identificador numérico bimodal (`IDB{k}`) diferenciándose únicamente por el sufijo modal (`_I` para inercial y `_eM` para visión). |
| **`Inventario_1a1.csv`** | Archivo CSV | **Catálogo maestro inmutable de los 53 pares** (20 columnas). Registra: `persona_id`, `id_par` (`IDB1` a `IDB53`), `archivo_imu`, `archivo_emotion`, `codigo`, `fecha`, `patient_id`, `test_id_imu`, `test_id_emotion`, `tipo`, `sexo`, `nacimiento`, `edad`, `talla`, `sensor`, `sensor_imu`, `sensor_emotion`, `delta_s`, `hora_utc` e `imu_source_file` (nombre del archivo origen en `Datos IMUs/IMUS/`). |
| **`Inventario_Brigada_1a1.json`** | Archivo JSON | Manifiesto estructurado en formato JSON con la parametrización exhaustiva de los 53 pares bimodales exportado para consumo directo por scripts y módulos analíticos. |
| **`df_variables_1a1.csv`** | Archivo CSV | **Matriz comparativa multimodal** (39 columnas). Alinea horizontalmente para cada par las variables temporales y biomecánicas de ambas tecnologías (duraciones activas, tiempos de giro, cadencia, etc.) y computa las diferencias numéricas inter-modalidad (`diff_duracion_activa_s`, `diff_dur_giro_s`). |
| **`FichaTecnica_1a1.md`** | Archivo Markdown | Especificación metodológica del protocolo de emparejamiento bimodal: criterios de inclusión simultánea, tolerancia de sincronización de relojes, especificaciones del instrumental e inventario de los 53 pares con sus desfases $\Delta t$. |
| **`Analisis_1a1.md`** | Archivo Markdown | Informe formal de concordancia física y validación cinemática: correlación lineal de Pearson, análisis de sesgo y límites de concordancia de Bland-Altman, dispersión de residuos y evaluación de robustez del sensor inercial frente a oclusiones ópticas. |

---

## 3. Formato de Nomenclatura de Archivos JSON

Los 106 archivos de la subcarpeta `IMU&eMotion/` están nombrados de manera simétrica y unívoca empleando el prefijo de dominio **`IDB`** (*Identificador Bimodal*):

### A. Para el sensor inercial (IMU):
```text
{ORIGEN}_IDB{NUMERO}_I.json
```

### B. Para la cámara óptica (e-Motion):
```text
{ORIGEN}_IDB{NUMERO}_eM.json
```

### Desglose de Campos:
1. **`{ORIGEN}`:** Procedencia geográfica de la brigada clínica:
   * `SMR`: Ensayos bimodales capturados en Santa Marta (IDB 1 al 47).
   * `CST`: Ensayos bimodales capturados en Costa / La Victoria (IDB 48 al 53).
2. **`IDB{NUMERO}`:** Identificador secuencial único del par bimodal sincronizado (`IDB1` a `IDB53`), común tanto para el archivo IMU como para el archivo e-Motion del mismo ensayo.
3. **`_I`:** Sufijo reservado exclusivamente para la componente inercial (IMU).
4. **`_eM`:** Sufijo reservado exclusivamente para la componente óptica (e-Motion).

### Ejemplos Reales:
* Par 1:
  * Inercial: `PDG-TUG/Datos IMU&eMotion/IMU&eMotion/SMR_IDB1_I.json`
  * Óptico: `PDG-TUG/Datos IMU&eMotion/IMU&eMotion/SMR_IDB1_eM.json`
* Par 20:
  * Inercial: `PDG-TUG/Datos IMU&eMotion/IMU&eMotion/SMR_IDB20_I.json`
  * Óptico: `PDG-TUG/Datos IMU&eMotion/IMU&eMotion/SMR_IDB20_eM.json`
* Par 48:
  * Inercial: `PDG-TUG/Datos IMU&eMotion/IMU&eMotion/CST_IDB48_I.json`
  * Óptico: `PDG-TUG/Datos IMU&eMotion/IMU&eMotion/CST_IDB48_eM.json`
