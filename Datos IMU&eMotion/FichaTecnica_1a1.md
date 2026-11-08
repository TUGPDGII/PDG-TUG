# FICHA TÉCNICA OFICIAL DEL DATASET BIMODAL SINCRONIZADO 1:1 (IMU & e-Motion) — PROYECTO TUG-V2
> **Documento Oficial de Auditoría, Verificación Temporal y Control de Calidad**
> **Fecha de Consolidación:** Noviembre 2026
> **Metodología:** CRISP-DM (Fases de Data Understanding y Data Preparation)
> **Directorio de Almacenamiento:** `Datos IMU&eMotion/`

---

## 1. Resumen Ejecutivo del Conjunto de Datos Bimodales 1:1

| Indicador | Magnitud / Métrica | Observación y Respaldo Metodológico |
|:---|:---:|---|
| **Total Ensayos Bimodales 1:1** | **53 pares (106 archivos JSON)** | Emparejamiento biyectivo unívoco verificado en el backend de VIMOV |
| **Archivos Inerciales (`Brigada_ID{k}_IMU_TUG.json`)** | **53 archivos** | 5 sensores sincronizados (Espina lumbar, tobillos I/D, muñecas I/D) a 50.0 Hz |
| **Archivos Ópticos (`Brigada_ID{k}_eMotion_TUG.json`)** | **53 archivos** | Series cinemáticas de profundidad RGB-D interpoladas PCHIP a 30.0 Hz |
| **Protocolo Clínico Auditado** | **TIMED_UP_AND_GO (100%)** | Validación estricta: ambos sensores ejecutaron la prueba TUG completa |
| **Ventana Temporal de Brigada** | **15 Jun 2026 – 15 Jul 2026** | Brigadas de campo en Santa Marta (`SMR`) y CST / La Victoria (`CST`) |
| **Brigada Santa Marta (`SMR`)** | **47 pares** | Fechas: 25, 26 y 27 de junio de 2026 (Cámara Intel RealSense D455F) |
| **Brigada CST / La Victoria (`CST`)** | **6 pares** | Fecha: 04 de julio de 2026 (Cámara Orbbec Astra 2) |
| **Distribución Clínica** | **47 Pacientes EP / 6 Controles** | 88.7% participantes con Enfermedad de Parkinson, 11.3% controles sanos |
| **Distribución por Sexo** | **37 Masculino / 16 Femenino** | 69.8% participantes masculinos, 30.2% participantes femeninos |
| **Desfase Temporal ($|\Delta t|$)** | **Mediana: 3.0 s (Máx: 73.0 s)** | Coincidencia de disparo entre cámara y tablet IMU compensando UTC-5 |

---

## 2. Criterios de Selección y Verificación 1:1 Estricta

Para garantizar que cada par de archivos corresponda al mismo ensayo físico de un participante, se ejecutó un algoritmo de validación cruzada sobre la base de datos centralizada de VIMOV:

1. **Filtro de Cohorte y Fecha:**
   Se consultaron los pacientes registrados en el mes de las brigadas $\pm 10$ días (del 15 de junio al 15 de julio de 2026), obteniendo 95 sujetos con registros simultáneos en los módulos de sensores inerciales y de visión artificial (`has_imus: true` y `has_emotion: true`).

2. **Homologación de Protocolo Clínico:**
   Se excluyeron todas las pruebas de marcha continua de 10 metros (`Gait Analysis` / `GAIT`), tapping digital y praxis motora, reteniendo únicamente registros catalogados formalmente como `TIMED_UP_AND_GO`.

3. **Alineación Temporal con Compensación de Huso Horario:**
   - La aplicación móvil de captura IMU almacena la estampa temporal en Tiempo Universal Coordinado (UTC).
   - El sistema de visión e-Motion registra la estampa temporal en hora local colombiana (UTC-5).
   - Aplicando la corrección horaria ($t_{\text{UTC}} = t_{\text{local}} + 5\text{ h}$), se calculó la discrepancia temporal $|\Delta t| = |t_{\text{inicio\_IMU}} - t_{\text{inicio\_cámara\_UTC}}|$.
   - Se estableció como umbral máximo de coincidencia simultánea $|\Delta t| \le 120\text{ s}$, logrando una mediana de discrepancia de apenas 3.0 segundos entre ambos sistemas.

4. **Biyección Unívoca (Emparejamiento 1:1):**
   En participantes con múltiples repeticiones consecutivas, se aplicó optimización por mínima distancia temporal, asignando a cada archivo de cámara un único archivo de IMU y viceversa, descartando asociaciones duplicadas o redundantes.

---

## 3. Estructura de Nomenclatura del Repositorio Bimodal

Dentro del directorio `Datos IMU&eMotion/IMU&eMotion/`, cada ensayo está vinculado inequívocamente a través de su identificador numérico secuencial `ID{k}`:

- **Sensor Inercial:** `Brigada_ID{k}_IMU_TUG.json`
- **Cámara Óptica:** `Brigada_ID{k}_eMotion_TUG.json`

Donde `{k}` abarca los números correlativos del 1 al 53, ordenados cronológicamente por momento de ejecución.

---

## 4. Catálogo Completo de Ensayos Sincronizados 1:1

| ID Bimodal | Archivo IMU | Archivo e-Motion | Sujeto VIMOV | Fecha | Hora UTC | $|\Delta t|$ (s) | Sensor e-Motion | Sexo | Edad | Clase Clínica |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **ID1** | `Brigada_ID1_IMU_TUG.json` | `Brigada_ID1_eMotion_TUG.json` | `GEOREF403` | 2026-06-25 | 14:07:54 | 41.0 | Intel RealSense | M | 71.0 | PATIENT |
| **ID2** | `Brigada_ID2_IMU_TUG.json` | `Brigada_ID2_eMotion_TUG.json` | `GEOREF400` | 2026-06-25 | 14:38:59 | 26.0 | Intel RealSense | M | 60.0 | PATIENT |
| **ID3** | `Brigada_ID3_IMU_TUG.json` | `Brigada_ID3_eMotion_TUG.json` | `GEOREF406` | 2026-06-25 | 14:49:24 | 4.0 | Intel RealSense | M | 61.0 | PATIENT |
| **ID4** | `Brigada_ID4_IMU_TUG.json` | `Brigada_ID4_eMotion_TUG.json` | `GEOREF408` | 2026-06-25 | 16:42:13 | 4.0 | Intel RealSense | F | 63.0 | PATIENT |
| **ID5** | `Brigada_ID5_IMU_TUG.json` | `Brigada_ID5_eMotion_TUG.json` | Control `93e09117` | 2026-06-25 | 18:04:44 | 8.0 | Intel RealSense | M | 70.0 | CONTROL |
| **ID6** | `Brigada_ID6_IMU_TUG.json` | `Brigada_ID6_eMotion_TUG.json` | `GEOREF413` | 2026-06-25 | 19:36:58 | 3.0 | Intel RealSense | M | 77.0 | PATIENT |
| **ID7** | `Brigada_ID7_IMU_TUG.json` | `Brigada_ID7_eMotion_TUG.json` | `GEOREF411` | 2026-06-25 | 19:54:10 | 73.0 | Intel RealSense | F | 68.0 | PATIENT |
| **ID8** | `Brigada_ID8_IMU_TUG.json` | `Brigada_ID8_eMotion_TUG.json` | `GEOREF_416` (E1) | 2026-06-25 | 20:13:35 | 20.0 | Intel RealSense | M | 56.0 | PATIENT |
| **ID9** | `Brigada_ID9_IMU_TUG.json` | `Brigada_ID9_eMotion_TUG.json` | `GEOREF_416` (E2) | 2026-06-25 | 20:16:06 | 5.0 | Intel RealSense | M | 56.0 | PATIENT |
| **ID10** | `Brigada_ID10_IMU_TUG.json` | `Brigada_ID10_eMotion_TUG.json` | `GEOREF412` | 2026-06-25 | 20:42:52 | 5.0 | Intel RealSense | M | 62.0 | PATIENT |
| **ID11** | `Brigada_ID11_IMU_TUG.json` | `Brigada_ID11_eMotion_TUG.json` | `GEOREF417` | 2026-06-25 | 21:23:38 | 4.0 | Intel RealSense | F | 72.0 | PATIENT |
| **ID12** | `Brigada_ID12_IMU_TUG.json` | `Brigada_ID12_eMotion_TUG.json` | `GEOREF415` | 2026-06-25 | 21:49:31 | 1.0 | Intel RealSense | M | 64.0 | PATIENT |
| **ID13** | `Brigada_ID13_IMU_TUG.json` | `Brigada_ID13_eMotion_TUG.json` | `GEOREF_418` | 2026-06-25 | 22:55:59 | 16.0 | Intel RealSense | M | 73.0 | PATIENT |
| **ID14** | `Brigada_ID14_IMU_TUG.json` | `Brigada_ID14_eMotion_TUG.json` | `LARGE_PD_864` | 2026-06-26 | 14:11:42 | 5.0 | Intel RealSense | F | 74.0 | PATIENT |
| **ID15** | `Brigada_ID15_IMU_TUG.json` | `Brigada_ID15_eMotion_TUG.json` | `LARGE_PD_865` | 2026-06-26 | 14:43:00 | 13.0 | Intel RealSense | M | 74.0 | PATIENT |
| **ID16** | `Brigada_ID16_IMU_TUG.json` | `Brigada_ID16_eMotion_TUG.json` | `LARGE_PD_862` | 2026-06-26 | 14:53:43 | 19.0 | Intel RealSense | F | 73.0 | PATIENT |
| **ID17** | `Brigada_ID17_IMU_TUG.json` | `Brigada_ID17_eMotion_TUG.json` | `LARGE_PD_867` | 2026-06-26 | 15:03:48 | 1.0 | Intel RealSense | F | 70.0 | PATIENT |
| **ID18** | `Brigada_ID18_IMU_TUG.json` | `Brigada_ID18_eMotion_TUG.json` | `LARGE_PD_866` | 2026-06-26 | 15:15:48 | 3.0 | Intel RealSense | F | 50.0 | PATIENT |
| **ID19** | `Brigada_ID19_IMU_TUG.json` | `Brigada_ID19_eMotion_TUG.json` | `GEOREF420` | 2026-06-26 | 15:25:04 | 0.0 | Intel RealSense | M | 47.0 | PATIENT |
| **ID20** | `Brigada_ID20_IMU_TUG.json` | `Brigada_ID20_eMotion_TUG.json` | `GEOREF421` | 2026-06-26 | 15:35:39 | 1.0 | Intel RealSense | F | 64.0 | PATIENT |
| **ID21** | `Brigada_ID21_IMU_TUG.json` | `Brigada_ID21_eMotion_TUG.json` | `LARGE_PD_860` | 2026-06-26 | 15:46:43 | 3.0 | Intel RealSense | F | 73.0 | PATIENT |
| **ID22** | `Brigada_ID22_IMU_TUG.json` | `Brigada_ID22_eMotion_TUG.json` | `LARGE_PD_863` (E1) | 2026-06-26 | 16:04:24 | 3.0 | Intel RealSense | F | 67.0 | PATIENT |
| **ID23** | `Brigada_ID23_IMU_TUG.json` | `Brigada_ID23_eMotion_TUG.json` | `LARGE_PD_863` (E2) | 2026-06-26 | 16:05:55 | 4.0 | Intel RealSense | F | 67.0 | PATIENT |
| **ID24** | `Brigada_ID24_IMU_TUG.json` | `Brigada_ID24_eMotion_TUG.json` | `LARGE_PD_861` (E1) | 2026-06-26 | 17:04:37 | 1.0 | Intel RealSense | M | 71.0 | PATIENT |
| **ID25** | `Brigada_ID25_IMU_TUG.json` | `Brigada_ID25_eMotion_TUG.json` | `LARGE_PD_861` (E2) | 2026-06-26 | 17:06:53 | 13.0 | Intel RealSense | M | 71.0 | PATIENT |
| **ID26** | `Brigada_ID26_IMU_TUG.json` | `Brigada_ID26_eMotion_TUG.json` | `LARGE_PD_861` (E3) | 2026-06-26 | 17:08:58 | 5.0 | Intel RealSense | M | 71.0 | PATIENT |
| **ID27** | `Brigada_ID27_IMU_TUG.json` | `Brigada_ID27_eMotion_TUG.json` | `LARGE_PD_861` (E4) | 2026-06-26 | 17:09:37 | 2.0 | Intel RealSense | M | 71.0 | PATIENT |
| **ID28** | `Brigada_ID28_IMU_TUG.json` | `Brigada_ID28_eMotion_TUG.json` | `LARGE_PD_868` | 2026-06-26 | 19:43:07 | 4.0 | Intel RealSense | F | 55.0 | PATIENT |
| **ID29** | `Brigada_ID29_IMU_TUG.json` | `Brigada_ID29_eMotion_TUG.json` | `LARGE_PD_869` | 2026-06-26 | 20:22:35 | 31.0 | Intel RealSense | M | 69.0 | PATIENT |
| **ID30** | `Brigada_ID30_IMU_TUG.json` | `Brigada_ID30_eMotion_TUG.json` | `LARGE_PD_870` | 2026-06-26 | 20:46:42 | 14.0 | Intel RealSense | M | 66.0 | PATIENT |
| **ID31** | `Brigada_ID31_IMU_TUG.json` | `Brigada_ID31_eMotion_TUG.json` | `LARGE_PD_873` | 2026-06-26 | 21:18:37 | 1.0 | Intel RealSense | M | 68.0 | PATIENT |
| **ID32** | `Brigada_ID32_IMU_TUG.json` | `Brigada_ID32_eMotion_TUG.json` | `LARGE_PD_875` | 2026-06-26 | 21:31:18 | 2.0 | Intel RealSense | F | 62.0 | PATIENT |
| **ID33** | `Brigada_ID33_IMU_TUG.json` | `Brigada_ID33_eMotion_TUG.json` | `LARGE_PD_878` | 2026-06-26 | 21:49:58 | 4.0 | Intel RealSense | F | 57.0 | PATIENT |
| **ID34** | `Brigada_ID34_IMU_TUG.json` | `Brigada_ID34_eMotion_TUG.json` | `LARGE_PD_871` | 2026-06-26 | 22:18:47 | 19.0 | Intel RealSense | M | 59.0 | PATIENT |
| **ID35** | `Brigada_ID35_IMU_TUG.json` | `Brigada_ID35_eMotion_TUG.json` | `LARGE_PD_880` | 2026-06-27 | 13:35:40 | 7.0 | Intel RealSense | M | 76.0 | PATIENT |
| **ID36** | `Brigada_ID36_IMU_TUG.json` | `Brigada_ID36_eMotion_TUG.json` | `LARGE_PD_883` | 2026-06-27 | 13:47:37 | 10.0 | Intel RealSense | M | 44.0 | PATIENT |
| **ID37** | `Brigada_ID37_IMU_TUG.json` | `Brigada_ID37_eMotion_TUG.json` | `LARGE_PD_879` | 2026-06-27 | 13:55:54 | 27.0 | Intel RealSense | M | 53.0 | PATIENT |
| **ID38** | `Brigada_ID38_IMU_TUG.json` | `Brigada_ID38_eMotion_TUG.json` | `LARGE_PD_882` | 2026-06-27 | 14:34:21 | 3.0 | Intel RealSense | M | 68.0 | PATIENT |
| **ID39** | `Brigada_ID39_IMU_TUG.json` | `Brigada_ID39_eMotion_TUG.json` | `LARGE_PD_885` | 2026-06-27 | 15:08:47 | 1.0 | Intel RealSense | F | 52.0 | PATIENT |
| **ID40** | `Brigada_ID40_IMU_TUG.json` | `Brigada_ID40_eMotion_TUG.json` | `LARGE_PD_891` | 2026-06-27 | 15:23:02 | 3.0 | Intel RealSense | M | 58.0 | PATIENT |
| **ID41** | `Brigada_ID41_IMU_TUG.json` | `Brigada_ID41_eMotion_TUG.json` | `LARGE_PD_888` | 2026-06-27 | 15:57:15 | 4.0 | Intel RealSense | M | 59.0 | PATIENT |
| **ID42** | `Brigada_ID42_IMU_TUG.json` | `Brigada_ID42_eMotion_TUG.json` | `LARGE_PD_884` | 2026-06-27 | 16:10:39 | 12.0 | Intel RealSense | M | 54.0 | PATIENT |
| **ID43** | `Brigada_ID43_IMU_TUG.json` | `Brigada_ID43_eMotion_TUG.json` | Control `ebc986d7` | 2026-06-27 | 16:19:41 | 1.0 | Intel RealSense | M | 72.0 | CONTROL |
| **ID44** | `Brigada_ID44_IMU_TUG.json` | `Brigada_ID44_eMotion_TUG.json` | `LARGE_PD_892` | 2026-06-27 | 16:37:29 | 4.0 | Intel RealSense | M | 72.0 | PATIENT |
| **ID45** | `Brigada_ID45_IMU_TUG.json` | `Brigada_ID45_eMotion_TUG.json` | `LARGE_PD_890` | 2026-06-27 | 17:13:05 | 2.0 | Intel RealSense | M | 50.0 | PATIENT |
| **ID46** | `Brigada_ID46_IMU_TUG.json` | `Brigada_ID46_eMotion_TUG.json` | `LARGE_PD_894` | 2026-06-27 | 18:06:45 | 13.0 | Intel RealSense | F | 71.0 | PATIENT |
| **ID47** | `Brigada_ID47_IMU_TUG.json` | `Brigada_ID47_eMotion_TUG.json` | `large_pd_896` | 2026-06-27 | 20:52:35 | 2.0 | Intel RealSense | F | 47.0 | PATIENT |
| **ID48** | `Brigada_ID48_IMU_TUG.json` | `Brigada_ID48_eMotion_TUG.json` | `large_pd_898` | 2026-07-04 | 14:50:22 | 0.0 | Orbbec Astra 2 | F | 64.0 | PATIENT |
| **ID49** | `Brigada_ID49_IMU_TUG.json` | `Brigada_ID49_eMotion_TUG.json` | `LARGE_PD_902` | 2026-07-04 | 15:44:08 | 3.0 | Orbbec Astra 2 | M | 63.0 | PATIENT |
| **ID50** | `Brigada_ID50_IMU_TUG.json` | `Brigada_ID50_eMotion_TUG.json` | `LARGE_PD_901` | 2026-07-04 | 15:58:15 | 3.0 | Orbbec Astra 2 | M | 63.0 | PATIENT |
| **ID51** | `Brigada_ID51_IMU_TUG.json` | `Brigada_ID51_eMotion_TUG.json` | `LARGE_PD_911` | 2026-07-04 | 16:56:59 | 6.0 | Orbbec Astra 2 | M | 40.0 | PATIENT |
| **ID52** | `Brigada_ID52_IMU_TUG.json` | `Brigada_ID52_eMotion_TUG.json` | Control `62843ff4` | 2026-07-04 | 17:19:11 | 0.0 | Orbbec Astra 2 | M | 58.0 | CONTROL |
| **ID53** | `Brigada_ID53_IMU_TUG.json` | `Brigada_ID53_eMotion_TUG.json` | Control `64bc7d94` | 2026-07-04 | 19:00:00 | 5.0 | Orbbec Astra 2 | F | 61.0 | CONTROL |

---

## 5. Control de Calidad y Verificación de Integridad

- **Integridad Sintáctica:** El 100% de los 106 archivos JSON son legibles y válidos según la norma RFC 8259.
- **Persistencia Tabular:** Los metadatos de trazabilidad se encuentran respaldados en `Datos IMU&eMotion/Inventario_1a1.csv` y `Datos IMU&eMotion/Inventario_Brigada_1a1.csv`.
- **Variables Cinemáticas:** La matriz de biomarcadores cruzados se encuentra consolidada en `Datos IMU&eMotion/df_variables_1a1.csv`.
