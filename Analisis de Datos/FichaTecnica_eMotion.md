# FICHA TÉCNICA DEL DATASET DE CÁMARA (e-Motion / VIMOV)

> **Documento Técnico de Evaluación, Caracterización y Control de Muestras de Video y Pose 3D**
> **Fecha de consolidación:** 02 de noviembre de 2026
> **Filtro de Protocolo:** Dataset estandarizado para pruebas **Timed Up and Go (TUG)**.

---

## 1. Resumen Ejecutivo del Dataset de Cámaras TUG

| Indicador | Valor Total | Observación Metodológica |
|---|---:|---|
| **Total Archivos TUG en `Datos e-Motion/`** | **132** | Totalidad de capturas estrictamente TUG estandarizadas |
| **Capturas Brigada Santa Marta (`SMR_`)** | **103** | **100% de las pruebas TUG de Santa Marta** (25, 26 y 27 de junio 2026) |
| **Capturas Brigada CST / La Victoria (`CST_`)** | **6** | Capturas TUG con cámara Orbbec Astra 2 |
| **Capturas de Laboratorio / Pilotos (`LAB_`)** | **23** | Capturas de validación técnica previas (octubre 2024 / 2026) |
| **Pares Bimodales IMU ↔ e-Motion Confirmados** | **42** | 100% de coincidencia temporal, de género y protocolo TUG |
| **Grabaciones No-TUG Segregadas (`No_TUG_Gait_Analysis/`)** | **137** | Pruebas de marcha continua de 10 m preservadas aparte |
| **Anonimización Ética** | **100% Verificada** | Despersonalización total (sin nombres propios ni números de cédula) |

---

## 2. Convención de Nomenclatura Estandarizada

Todos los archivos en `Datos e-Motion/` siguen la convención formal:

1. **Capturas Bimodales con IMU:**
   `SMR_YYYYMMDD_Pxx_CODIGO_hash_raw.json` o `CST_YYYYMMDD_Pxx_CODIGO_hash_raw.json`
   *(ej. `SMR_20260625_P06_BF_c75d8bcd_raw.json`)*
2. **Capturas TUG de Brigada sin IMU:**
   `SMR_YYYYMMDD_NO_IMU_hash_raw.json` o `CST_YYYYMMDD_NO_IMU_hash_raw.json`
   *(ej. `SMR_20260626_NO_IMU_98184b25_raw.json`)*
3. **Capturas de Laboratorio / Calibración:**
   `LAB_YYYYMMDD_INTEL_hash_raw.json`
   *(ej. `LAB_20261002_INTEL_09a4dc83_raw.json`)*

---

## 3. Delimitación de Alcance y Criterio de Utilidad Biomecánica

- **Longitud de Zancada y Velocidad:** Todas las capturas TUG son útiles y válidas para medir la longitud del paso/zancada (distancia euclidiana inter-tobillo en los planos de apoyo sagital) y la velocidad lineal del centro de masa (`Hip Center`) durante los tramos de marcha recta de ida y vuelta.
- **Segmentación de Giro y Sentado:** Las cámaras presentan descalibración y oclusión en giros cerrados a 3 metros y durante la flexión de sentado. Por tanto, **la segmentación temporal de los giros y el conteo de pasos en el giro quedan a cargo exclusivo de los sensores IMU**.
