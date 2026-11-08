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
| **Archivos Inerciales (`{ORIGEN}_ID{k}_IMU_TUG.json (SMR_ID1..47, CST_ID48..53)`)** | **53 archivos** | 5 sensores sincronizados (Espina lumbar, tobillos I/D, muñecas I/D) a 50.0 Hz |
| **Archivos Ópticos (`{ORIGEN}_ID{k}_eMotion_TUG.json (SMR_ID1..47, CST_ID48..53)`)** | **53 archivos** | Series cinemáticas de profundidad RGB-D interpoladas PCHIP a 30.0 Hz |
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

3. **Alineación Temporal con Compensación de Huso Horario (UTC vs. Colombia UTC-5):**
   - **Sensores Inerciales (IMUs):** La marca de tiempo raíz (`timestamp`) se registra en milisegundos Unix Epoch (ej. `1782398964864` ms). Por definición estándar internacional (POSIX), este valor mide el tiempo exacto transcurrido desde el 1 de enero de 1970 a las 00:00:00 UTC (meridiano de Greenwich), con independencia de la región geográfica.
   - **Sistema de Visión e-Motion:** La estación de cómputo en brigada corre una aplicación de escritorio Windows que estampa la fecha del sistema operativo en hora local en el campo `CaptureTest.Date` (ej. `"25-06-2026 09:49:20.197"`).
   - **Corrección y Alineación:** Dado que todas las brigadas se realizaron en Colombia (huso horario legal **UTC-5**, `America/Bogota`), se implementó la compensación formal:
     $$\text{Hora}_{\text{IMU (Colombia)}} = \text{datetime.fromtimestamp}(\text{timestamp}_{\text{IMU}} / 1000.0, \text{tz}=\text{UTC}) - 5\text{ h}$$
     $$|\Delta t| = |\text{Hora}_{\text{IMU (Colombia)}} - \text{Hora}_{\text{e-Motion}}|$$
   - Se estableció como umbral máximo $|\Delta t| \le 120\text{ s}$, obteniendo una mediana de discrepancia de apenas 3.0 segundos entre ambos sistemas.

4. **Biyección Unívoca (Emparejamiento 1:1):**
   En participantes con múltiples repeticiones consecutivas, se aplicó optimización por mínima distancia temporal, asignando a cada archivo de cámara un único archivo de IMU y viceversa, descartando asociaciones duplicadas o redundantes.

---

## 3. Auditoría de Variabilidad y Anomalías Cinemáticas en Pruebas TUG

Durante la inspección algorítmica y visual de las series temporales inerciales y ópticas, se constató que no todas las grabaciones corresponden a un TUG de libro de texto (un solo levantamiento, marcha rectilínea, un único giro de 180° y sentado). En la práctica clínica de campo se presentan **dos fenómenos operacionales característicos**:

1. **Grabaciones con Doble Intento o Ensayo Previo (Pausas Estáticas Prolongadas):**
   - En varios ensayos, el evaluador inició la grabación inercial mientras instruía al paciente o permitía un ensayo preliminar. Tras este primer movimiento, el paciente regresó al reposo y permaneció inmóvil en la silla durante un intervalo estático prolongado ($8\text{ a }35\text{ s}$, donde el giroscopio lumbar marca reposo absoluto $\approx 0^\circ/\text{s}$ y la aceleración es gravitatoria pura $1.0\text{ g}$).
   - Posteriormente, cuando la cámara e-Motion comenzó a grabar, el paciente ejecutó la prueba TUG definitiva y sincronizada.
   - **Caso representativo:** `IDB3` (`SMR_IDB3_I.json` de $44.0\text{ s}$ vs `SMR_IDB3_eM.json` de $18.2\text{ s}$), con 15.1 s de reposo estático absoluto intermedio y dos eventos motores diferenciados.
2. **Grabaciones con Múltiples Giros Detectados:**
   - Pacientes con Enfermedad de Parkinson con festinación, titubeo o giros fragmentados en múltiples pasos (*en bloc* o en varios semicírculos) presentan más de un pico prominente de velocidad angular de guiñada (*yaw*), o bien realizaron un giro exploratorio previo.
   - **Pares bimodales con múltiples picos de giro identificados:** `IDB5`, `IDB7`, `IDB10`, `IDB20` y `IDB30`.

> **Registro de Auditoría Detallada:** La totalidad de los 53 pares bimodales se encuentra clasificada con sus duraciones individuales, número de giros, tiempos de reposo y diagnóstico en el archivo complementario:  
> [`Datos IMU&eMotion/Auditoria_Anomalias_Bimodales.csv`](file:///home/guarinve/Documentos/PDG-TUG/Datos%20IMU&eMotion/Auditoria_Anomalias_Bimodales.csv).

---

## 3. Estructura de Nomenclatura del Repositorio Bimodal

Dentro del directorio `Datos IMU&eMotion/IMU&eMotion/`, cada ensayo está vinculado inequívocamente a través de su identificador numérico secuencial `ID{k}`:

- **Sensor Inercial:** `{ORIGEN}_ID{k}_IMU_TUG.json (SMR_ID1..47, CST_ID48..53)`
- **Cámara Óptica:** `{ORIGEN}_ID{k}_eMotion_TUG.json (SMR_ID1..47, CST_ID48..53)`

Donde `{k}` abarca los números correlativos del 1 al 53, ordenados cronológicamente por momento de ejecución.

---

## 4. Catálogo Completo de Ensayos Sincronizados 1:1

| ID Bimodal | Archivo IMU | Archivo e-Motion | Sujeto VIMOV | Fecha | Hora UTC | $|\Delta t|$ (s) | Sensor e-Motion | Sexo | Edad | Clase Clínica |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **ID1** | `SMR_IDB1_I.json` | `SMR_IDB1_eM.json` | `GEOREF403` | 2026-06-25 | 14:07:54 | 41.0 | Intel RealSense | M | 71.0 | PATIENT |
| **ID2** | `SMR_IDB2_I.json` | `SMR_IDB2_eM.json` | `GEOREF400` | 2026-06-25 | 14:38:59 | 26.0 | Intel RealSense | M | 60.0 | PATIENT |
| **ID3** | `SMR_IDB3_I.json` | `SMR_IDB3_eM.json` | `GEOREF406` | 2026-06-25 | 14:49:24 | 4.0 | Intel RealSense | M | 61.0 | PATIENT |
| **ID4** | `SMR_IDB4_I.json` | `SMR_IDB4_eM.json` | `GEOREF408` | 2026-06-25 | 16:42:13 | 4.0 | Intel RealSense | F | 63.0 | PATIENT |
| **ID5** | `SMR_IDB5_I.json` | `SMR_IDB5_eM.json` | Control `93e09117` | 2026-06-25 | 18:04:44 | 8.0 | Intel RealSense | M | 70.0 | CONTROL |
| **ID6** | `SMR_IDB6_I.json` | `SMR_IDB6_eM.json` | `GEOREF413` | 2026-06-25 | 19:36:58 | 3.0 | Intel RealSense | M | 77.0 | PATIENT |
| **ID7** | `SMR_IDB7_I.json` | `SMR_IDB7_eM.json` | `GEOREF411` | 2026-06-25 | 19:54:10 | 73.0 | Intel RealSense | F | 68.0 | PATIENT |
| **ID8** | `SMR_IDB8_I.json` | `SMR_IDB8_eM.json` | `GEOREF_416` (E1) | 2026-06-25 | 20:13:35 | 20.0 | Intel RealSense | M | 56.0 | PATIENT |
| **ID9** | `SMR_IDB9_I.json` | `SMR_IDB9_eM.json` | `GEOREF_416` (E2) | 2026-06-25 | 20:16:06 | 5.0 | Intel RealSense | M | 56.0 | PATIENT |
| **ID10** | `SMR_IDB10_I.json` | `SMR_IDB10_eM.json` | `GEOREF412` | 2026-06-25 | 20:42:52 | 5.0 | Intel RealSense | M | 62.0 | PATIENT |
| **ID11** | `SMR_IDB11_I.json` | `SMR_IDB11_eM.json` | `GEOREF417` | 2026-06-25 | 21:23:38 | 4.0 | Intel RealSense | F | 72.0 | PATIENT |
| **ID12** | `SMR_IDB12_I.json` | `SMR_IDB12_eM.json` | `GEOREF415` | 2026-06-25 | 21:49:31 | 1.0 | Intel RealSense | M | 64.0 | PATIENT |
| **ID13** | `SMR_IDB13_I.json` | `SMR_IDB13_eM.json` | `GEOREF_418` | 2026-06-25 | 22:55:59 | 16.0 | Intel RealSense | M | 73.0 | PATIENT |
| **ID14** | `SMR_IDB14_I.json` | `SMR_IDB14_eM.json` | `LARGE_PD_864` | 2026-06-26 | 14:11:42 | 5.0 | Intel RealSense | F | 74.0 | PATIENT |
| **ID15** | `SMR_IDB15_I.json` | `SMR_IDB15_eM.json` | `LARGE_PD_865` | 2026-06-26 | 14:43:00 | 13.0 | Intel RealSense | M | 74.0 | PATIENT |
| **ID16** | `SMR_IDB16_I.json` | `SMR_IDB16_eM.json` | `LARGE_PD_862` | 2026-06-26 | 14:53:43 | 19.0 | Intel RealSense | F | 73.0 | PATIENT |
| **ID17** | `SMR_IDB17_I.json` | `SMR_IDB17_eM.json` | `LARGE_PD_867` | 2026-06-26 | 15:03:48 | 1.0 | Intel RealSense | F | 70.0 | PATIENT |
| **ID18** | `SMR_IDB18_I.json` | `SMR_IDB18_eM.json` | `LARGE_PD_866` | 2026-06-26 | 15:15:48 | 3.0 | Intel RealSense | F | 50.0 | PATIENT |
| **ID19** | `SMR_IDB19_I.json` | `SMR_IDB19_eM.json` | `GEOREF420` | 2026-06-26 | 15:25:04 | 0.0 | Intel RealSense | M | 47.0 | PATIENT |
| **ID20** | `SMR_IDB20_I.json` | `SMR_IDB20_eM.json` | `GEOREF421` | 2026-06-26 | 15:35:39 | 1.0 | Intel RealSense | F | 64.0 | PATIENT |
| **ID21** | `SMR_IDB21_I.json` | `SMR_IDB21_eM.json` | `LARGE_PD_860` | 2026-06-26 | 15:46:43 | 3.0 | Intel RealSense | F | 73.0 | PATIENT |
| **ID22** | `SMR_IDB22_I.json` | `SMR_IDB22_eM.json` | `LARGE_PD_863` (E1) | 2026-06-26 | 16:04:24 | 3.0 | Intel RealSense | F | 67.0 | PATIENT |
| **ID23** | `SMR_IDB23_I.json` | `SMR_IDB23_eM.json` | `LARGE_PD_863` (E2) | 2026-06-26 | 16:05:55 | 4.0 | Intel RealSense | F | 67.0 | PATIENT |
| **ID24** | `SMR_IDB24_I.json` | `SMR_IDB24_eM.json` | `LARGE_PD_861` (E1) | 2026-06-26 | 17:04:37 | 1.0 | Intel RealSense | M | 71.0 | PATIENT |
| **ID25** | `SMR_IDB25_I.json` | `SMR_IDB25_eM.json` | `LARGE_PD_861` (E2) | 2026-06-26 | 17:06:53 | 13.0 | Intel RealSense | M | 71.0 | PATIENT |
| **ID26** | `SMR_IDB26_I.json` | `SMR_IDB26_eM.json` | `LARGE_PD_861` (E3) | 2026-06-26 | 17:08:58 | 5.0 | Intel RealSense | M | 71.0 | PATIENT |
| **ID27** | `SMR_IDB27_I.json` | `SMR_IDB27_eM.json` | `LARGE_PD_861` (E4) | 2026-06-26 | 17:09:37 | 2.0 | Intel RealSense | M | 71.0 | PATIENT |
| **ID28** | `SMR_IDB28_I.json` | `SMR_IDB28_eM.json` | `LARGE_PD_868` | 2026-06-26 | 19:43:07 | 4.0 | Intel RealSense | F | 55.0 | PATIENT |
| **ID29** | `SMR_IDB29_I.json` | `SMR_IDB29_eM.json` | `LARGE_PD_869` | 2026-06-26 | 20:22:35 | 31.0 | Intel RealSense | M | 69.0 | PATIENT |
| **ID30** | `SMR_IDB30_I.json` | `SMR_IDB30_eM.json` | `LARGE_PD_870` | 2026-06-26 | 20:46:42 | 14.0 | Intel RealSense | M | 66.0 | PATIENT |
| **ID31** | `SMR_IDB31_I.json` | `SMR_IDB31_eM.json` | `LARGE_PD_873` | 2026-06-26 | 21:18:37 | 1.0 | Intel RealSense | M | 68.0 | PATIENT |
| **ID32** | `SMR_IDB32_I.json` | `SMR_IDB32_eM.json` | `LARGE_PD_875` | 2026-06-26 | 21:31:18 | 2.0 | Intel RealSense | F | 62.0 | PATIENT |
| **ID33** | `SMR_IDB33_I.json` | `SMR_IDB33_eM.json` | `LARGE_PD_878` | 2026-06-26 | 21:49:58 | 4.0 | Intel RealSense | F | 57.0 | PATIENT |
| **ID34** | `SMR_IDB34_I.json` | `SMR_IDB34_eM.json` | `LARGE_PD_871` | 2026-06-26 | 22:18:47 | 19.0 | Intel RealSense | M | 59.0 | PATIENT |
| **ID35** | `SMR_IDB35_I.json` | `SMR_IDB35_eM.json` | `LARGE_PD_880` | 2026-06-27 | 13:35:40 | 7.0 | Intel RealSense | M | 76.0 | PATIENT |
| **ID36** | `SMR_IDB36_I.json` | `SMR_IDB36_eM.json` | `LARGE_PD_883` | 2026-06-27 | 13:47:37 | 10.0 | Intel RealSense | M | 44.0 | PATIENT |
| **ID37** | `SMR_IDB37_I.json` | `SMR_IDB37_eM.json` | `LARGE_PD_879` | 2026-06-27 | 13:55:54 | 27.0 | Intel RealSense | M | 53.0 | PATIENT |
| **ID38** | `SMR_IDB38_I.json` | `SMR_IDB38_eM.json` | `LARGE_PD_882` | 2026-06-27 | 14:34:21 | 3.0 | Intel RealSense | M | 68.0 | PATIENT |
| **ID39** | `SMR_IDB39_I.json` | `SMR_IDB39_eM.json` | `LARGE_PD_885` | 2026-06-27 | 15:08:47 | 1.0 | Intel RealSense | F | 52.0 | PATIENT |
| **ID40** | `SMR_IDB40_I.json` | `SMR_IDB40_eM.json` | `LARGE_PD_891` | 2026-06-27 | 15:23:02 | 3.0 | Intel RealSense | M | 58.0 | PATIENT |
| **ID41** | `SMR_IDB41_I.json` | `SMR_IDB41_eM.json` | `LARGE_PD_888` | 2026-06-27 | 15:57:15 | 4.0 | Intel RealSense | M | 59.0 | PATIENT |
| **ID42** | `SMR_IDB42_I.json` | `SMR_IDB42_eM.json` | `LARGE_PD_884` | 2026-06-27 | 16:10:39 | 12.0 | Intel RealSense | M | 54.0 | PATIENT |
| **ID43** | `SMR_IDB43_I.json` | `SMR_IDB43_eM.json` | Control `ebc986d7` | 2026-06-27 | 16:19:41 | 1.0 | Intel RealSense | M | 72.0 | CONTROL |
| **ID44** | `SMR_IDB44_I.json` | `SMR_IDB44_eM.json` | `LARGE_PD_892` | 2026-06-27 | 16:37:29 | 4.0 | Intel RealSense | M | 72.0 | PATIENT |
| **ID45** | `SMR_IDB45_I.json` | `SMR_IDB45_eM.json` | `LARGE_PD_890` | 2026-06-27 | 17:13:05 | 2.0 | Intel RealSense | M | 50.0 | PATIENT |
| **ID46** | `SMR_IDB46_I.json` | `SMR_IDB46_eM.json` | `LARGE_PD_894` | 2026-06-27 | 18:06:45 | 13.0 | Intel RealSense | F | 71.0 | PATIENT |
| **ID47** | `SMR_IDB47_I.json` | `SMR_IDB47_eM.json` | `large_pd_896` | 2026-06-27 | 20:52:35 | 2.0 | Intel RealSense | F | 47.0 | PATIENT |
| **ID48** | `CST_IDB48_I.json` | `CST_IDB48_eM.json` | `large_pd_898` | 2026-07-04 | 14:50:22 | 0.0 | Orbbec Astra 2 | F | 64.0 | PATIENT |
| **ID49** | `CST_IDB49_I.json` | `CST_IDB49_eM.json` | `LARGE_PD_902` | 2026-07-04 | 15:44:08 | 3.0 | Orbbec Astra 2 | M | 63.0 | PATIENT |
| **ID50** | `CST_IDB50_I.json` | `CST_IDB50_eM.json` | `LARGE_PD_901` | 2026-07-04 | 15:58:15 | 3.0 | Orbbec Astra 2 | M | 63.0 | PATIENT |
| **ID51** | `CST_IDB51_I.json` | `CST_IDB51_eM.json` | `LARGE_PD_911` | 2026-07-04 | 16:56:59 | 6.0 | Orbbec Astra 2 | M | 40.0 | PATIENT |
| **ID52** | `CST_IDB52_I.json` | `CST_IDB52_eM.json` | Control `62843ff4` | 2026-07-04 | 17:19:11 | 0.0 | Orbbec Astra 2 | M | 58.0 | CONTROL |
| **ID53** | `CST_IDB53_I.json` | `CST_IDB53_eM.json` | Control `64bc7d94` | 2026-07-04 | 19:00:00 | 5.0 | Orbbec Astra 2 | F | 61.0 | CONTROL |

---

## 5. Control de Calidad y Verificación de Integridad

- **Integridad Sintáctica:** El 100% de los 106 archivos JSON son legibles y válidos según la norma RFC 8259.
- **Persistencia Tabular:** Los metadatos de trazabilidad se encuentran respaldados en `Datos IMU&eMotion/Inventario_1a1.csv` y `Datos IMU&eMotion/Inventario_Brigada_1a1.csv`.
- **Variables Cinemáticas:** La matriz de biomarcadores cruzados se encuentra consolidada en `Datos IMU&eMotion/df_variables_1a1.csv`.
