# Correspondencia y Trazabilidad: Sensores IMU vs. Sistema de Cámaras e-Motion (VIMOV)

> **Propósito:** Responder al requerimiento del profesor Domiciano Rincón de auditar las fechas de los 78 archivos de datos IMU y contrastarlas con las grabaciones del sistema e-Motion / VIMOV para determinar con exactitud quiénes cuentan con su versión de cámara y quiénes no.
> **Fecha de generación:** Noviembre 2026
> **Criterio de Pareo Temporal:** Tolerancia de inicio menor o igual a 60 segundos (tras convertir el timestamp Unix UTC del IMU a hora local de Colombia UTC-5).

## 1. Resumen Ejecutivo del Cruce

| Métrica | Valor |
|---|---:|
| Total grabaciones IMU en dataset | **78** |
| Total archivos en `Datos e-Motion/` | **32** (30 RAW + 2 procesados) |
| Grabaciones IMU con versión e-Motion confirmada (<= 60 s) | **6** (7.7%) |
| Grabaciones IMU sin versión e-Motion en el repositorio local | **72** (92.3%) |
| Fecha común detectada con correspondencia | **04 de julio de 2026** (Brigada) |

### Hallazgos Principales:
1. **Diferencia de Nomenclatura vs. Timestamp Real:** Siete archivos IMU tienen nombres con prefijo `20260820...` (20 de agosto), pero su timestamp interno real (`timestamp` Unix en milisegundos) corresponde en realidad al **04 de julio de 2026** (hora local Colombia 10:50 a 13:49). Al corregir la estampa real a hora colombiana, se descubrió que **5 de ellos coinciden exactamente (a menos de 4 segundos)** con capturas de cámara Orbbec Astra 2 de e-Motion.
2. **Pareos Confirmados (6 grabaciones):**
   - `temp_BE` (P54 - Paciente) <-> `4849da67-9862-4f1a-b960-165cfa5306e7_raw.json` (diff: 22.5 s)
   - `temp_AM` (P60 - Paciente) <-> `93b689a7-dfc2-4069-a935-efdde29de98a_raw.json` (diff: 1.9 s)
   - `temp_P` (P61 - Control) <-> `b6487716-3d2f-4728-b000-cd71ccc723c2_raw.json` (diff: 4.0 s)
   - `temp_Z` (P63 - Paciente) <-> `56108fef-0268-4f6f-920e-97787068b311_raw.json` (diff: 0.2 s)
   - `temp_Z` (duplicado) <-> `56108fef-0268-4f6f-920e-97787068b311_raw.json` (diff: 0.2 s)
   - `temp_AN` (P65 - Control) <-> `0cce5b72-f8d0-458e-b576-64c138fd2b53_raw.json` (diff: 52.6 s)
3. **Grabaciones sin e-Motion:** Las 72 grabaciones restantes (tomadas en febrero, marzo, junio y otras horas de julio) **no tienen registro de cámara en el repositorio local**. Tal como se discutió en la Reunión #8, estas grabaciones corresponden a brigadas o tomas anteriores donde no se utilizó cámara o cuyos videos/RAW se encuentran aún pendientes de descarga del sistema VIMOV / Bod.

--- 

## 2. Cuadro de Auditoría Completa (78 Grabaciones IMU)

A continuación se lista cada uno de los 78 archivos IMU, su sujeto clínico asignado en `Datos_IMUs.csv`, su estampa de tiempo local calculada, su estado de coincidencia y el archivo e-Motion asociado.

| # | Archivo IMU | Sujeto | Grupo | Fecha y Hora Local (COL) | ¿Tiene e-Motion? | Archivo e-Motion Candidato | Dif. Inicio (s) |
|---:|---|:---:|:---:|:---:|:---:|:---:|---:|
| 1 | `20260208022404_temp_BV.json` | P01 | SIN_ETIQUETA | 2026-02-07 21:24:03 | **NO** | `-` | - |
| 2 | `20260303043120_temp_N.json` | P02 | SIN_ETIQUETA | 2026-03-02 23:31:19 | **NO** | `-` | - |
| 3 | `20260303043532_temp_BO.json` | P02 | SIN_ETIQUETA | 2026-03-02 23:35:31 | **NO** | `-` | - |
| 4 | `20260303044505_temp_BX.json` | P02 | SIN_ETIQUETA | 2026-03-02 23:45:05 | **NO** | `-` | - |
| 5 | `20260303134630_temp_BJ.json` | P02 | SIN_ETIQUETA | 2026-03-03 08:46:28 | **NO** | `-` | - |
| 6 | `20260307234249_temp_F.json` | P03 | SIN_ETIQUETA | 2026-03-07 18:42:30 | **NO** | `-` | - |
| 7 | `20260308232420_temp_AX.json` | P04 | SIN_ETIQUETA | 2026-03-08 18:23:46 | **NO** | `-` | - |
| 8 | `20260611235032_temp_AL.json` | P05 | CONTROL | 2026-06-11 18:50:03 | **NO** | `-` | - |
| 9 | `20260618075259_temp_BC.json` | P05 | CONTROL | 2026-06-18 02:52:44 | **NO** | `-` | - |
| 10 | `20260625140746_temp_BF.json` | P06 | PATIENT | 2026-06-25 09:06:19 | **NO** | `-` | - |
| 11 | `20260625140851_temp_AR.json` | P06 | PATIENT | 2026-06-25 09:07:54 | **NO** | `-` | - |
| 12 | `20260625144044_temp_D.json` | P07 | PATIENT | 2026-06-25 09:38:59 | **NO** | `-` | - |
| 13 | `20260625145018_temp_AB.json` | P08 | PATIENT | 2026-06-25 09:49:24 | **NO** | `-` | - |
| 14 | `20260625150353_temp_AK.json` | P09 | PATIENT | 2026-06-25 10:02:19 | **NO** | `-` | - |
| 15 | `20260625152019_temp_AA.json` | P10 | PATIENT | 2026-06-25 10:19:18 | **NO** | `-` | - |
| 16 | `20260625153756_temp_V.json` | P11 | PATIENT | 2026-06-25 10:36:33 | **NO** | `-` | - |
| 17 | `20260625164351_temp_A.json` | P12 | PATIENT | 2026-06-25 11:42:13 | **NO** | `-` | - |
| 18 | `20260625171352_temp_BW.json` | P13 | PATIENT | 2026-06-25 12:11:39 | **NO** | `-` | - |
| 19 | `20260625180613_temp_AG.json` | P14 | CONTROL | 2026-06-25 13:04:44 | **NO** | `-` | - |
| 20 | `20260625183434_temp_BK.json` | P15 | PATIENT | 2026-06-25 13:32:43 | **NO** | `-` | - |
| 21 | `20260625193811_temp_BD.json` | P16 | PATIENT | 2026-06-25 14:36:58 | **NO** | `-` | - |
| 22 | `20260625195406_temp_BR.json` | P17 | PATIENT | 2026-06-25 14:51:46 | **NO** | `-` | - |
| 23 | `20260625195426_temp_AP.json` | P17 | PATIENT | 2026-06-25 14:54:10 | **NO** | `-` | - |
| 24 | `20260625204358_temp_BN.json` | P18 | PATIENT | 2026-06-25 15:42:52 | **NO** | `-` | - |
| 25 | `20260625212453_temp_G.json` | P19 | PATIENT | 2026-06-25 16:23:38 | **NO** | `-` | - |
| 26 | `20260625214451_temp_BH.json` | P20 | PATIENT | 2026-06-25 15:13:35 | **NO** | `-` | - |
| 27 | `20260625214518_temp_S.json` | P20 | PATIENT | 2026-06-25 15:16:06 | **NO** | `-` | - |
| 28 | `20260625215046_temp_X.json` | P21 | PATIENT | 2026-06-25 16:49:31 | **NO** | `-` | - |
| 29 | `20260626133915_temp_BA.json` | P22 | PATIENT | 2026-06-25 17:55:59 | **NO** | `-` | - |
| 30 | `20260626133916_temp_BA.json` | P22 | PATIENT | 2026-06-25 17:55:59 | **NO** | `-` | - |
| 31 | `20260626141246_temp_AC.json` | P23 | PATIENT | 2026-06-26 09:11:42 | **NO** | `-` | - |
| 32 | `20260626144433_temp_AV.json` | P24 | PATIENT | 2026-06-26 09:43:00 | **NO** | `-` | - |
| 33 | `20260626145512_temp_AO.json` | P25 | PATIENT | 2026-06-26 09:53:43 | **NO** | `-` | - |
| 34 | `20260626150532_temp_M.json` | P26 | PATIENT | 2026-06-26 10:03:48 | **NO** | `-` | - |
| 35 | `20260626151711_temp_BQ.json` | P27 | PATIENT | 2026-06-26 10:15:48 | **NO** | `-` | - |
| 36 | `20260626152553_temp_U.json` | P28 | PATIENT | 2026-06-26 10:25:04 | **NO** | `-` | - |
| 37 | `20260626153637_temp_AJ.json` | P29 | PATIENT | 2026-06-26 10:35:39 | **NO** | `-` | - |
| 38 | `20260626154758_temp_O.json` | P30 | PATIENT | 2026-06-26 10:46:43 | **NO** | `-` | - |
| 39 | `20260626160554_temp_BU.json` | P31 | PATIENT | 2026-06-26 11:04:24 | **NO** | `-` | - |
| 40 | `20260626160620_temp_K.json` | P31 | PATIENT | 2026-06-26 11:05:55 | **NO** | `-` | - |
| 41 | `20260626170623_temp_BT.json` | P32 | PATIENT | 2026-06-26 12:04:37 | **NO** | `-` | - |
| 42 | `20260626170733_temp_AZ.json` | P32 | PATIENT | 2026-06-26 12:06:53 | **NO** | `-` | - |
| 43 | `20260626170919_temp_J.json` | P32 | PATIENT | 2026-06-26 12:08:58 | **NO** | `-` | - |
| 44 | `20260626170956_temp_AQ.json` | P32 | PATIENT | 2026-06-26 12:09:37 | **NO** | `-` | - |
| 45 | `20260626194407_temp_BM.json` | P33 | PATIENT | 2026-06-26 14:43:07 | **NO** | `-` | - |
| 46 | `20260626202515_temp_BS.json` | P34 | PATIENT | 2026-06-26 15:22:35 | **NO** | `-` | - |
| 47 | `20260626204728_temp_AW.json` | P35 | PATIENT | 2026-06-26 15:46:42 | **NO** | `-` | - |
| 48 | `20260626211937_temp_AH.json` | P36 | PATIENT | 2026-06-26 16:18:37 | **NO** | `-` | - |
| 49 | `20260626213214_temp_AT.json` | P37 | PATIENT | 2026-06-26 16:31:18 | **NO** | `-` | - |
| 50 | `20260626215053_temp_AE.json` | P38 | PATIENT | 2026-06-26 16:49:58 | **NO** | `-` | - |
| 51 | `20260626222007_temp_BL.json` | P39 | PATIENT | 2026-06-26 17:18:47 | **NO** | `-` | - |
| 52 | `20260627133637_temp_AS.json` | P40 | PATIENT | 2026-06-27 08:35:40 | **NO** | `-` | - |
| 53 | `20260627135010_temp_BP.json` | P41 | PATIENT | 2026-06-27 08:47:37 | **NO** | `-` | - |
| 54 | `20260627135720_temp_AD.json` | P42 | PATIENT | 2026-06-27 08:55:54 | **NO** | `-` | - |
| 55 | `20260627143518_temp_BB.json` | P43 | PATIENT | 2026-06-27 09:34:21 | **NO** | `-` | - |
| 56 | `20260627150939_temp_R.json` | P44 | PATIENT | 2026-06-27 10:08:47 | **NO** | `-` | - |
| 57 | `20260627152358_temp_W.json` | P45 | PATIENT | 2026-06-27 10:23:02 | **NO** | `-` | - |
| 58 | `20260627155804_temp_I.json` | P46 | PATIENT | 2026-06-27 10:57:15 | **NO** | `-` | - |
| 59 | `20260627161148_temp_Q.json` | P47 | PATIENT | 2026-06-27 11:10:39 | **NO** | `-` | - |
| 60 | `20260627162118_temp_AU.json` | P48 | PATIENT | 2026-06-27 11:19:41 | **NO** | `-` | - |
| 61 | `20260627163836_temp_L.json` | P49 | PATIENT | 2026-06-27 11:37:29 | **NO** | `-` | - |
| 62 | `20260627171353_temp_H.json` | P50 | PATIENT | 2026-06-27 12:13:05 | **NO** | `-` | - |
| 63 | `20260627180847_temp_AI.json` | P51 | PATIENT | 2026-06-27 13:06:45 | **NO** | `-` | - |
| 64 | `20260627205326_temp_C.json` | P52 | PATIENT | 2026-06-27 15:52:35 | **NO** | `-` | - |
| 65 | `20260704154505_temp_AF.json` | P53 | PATIENT | 2026-07-04 10:44:08 | **NO** | `-` | - |
| 66 | `20260704155929_temp_BE.json` | P54 | PATIENT | 2026-07-04 10:58:15 | **SÍ** | `4849da67-9862-4f1a-b960-165cfa5306e7_raw.json` | 22.5 |
| 67 | `20260704165749_temp_E.json` | P55 | PATIENT | 2026-07-04 11:56:59 | **NO** | `-` | - |
| 68 | `20260704172020_temp_Y.json` | P56 | PATIENT | 2026-07-04 12:19:11 | **NO** | `-` | - |
| 69 | `20260704194015_temp_AY.json` | P57 | CONTROL | 2026-07-04 14:00:00 | **NO** | `-` | - |
| 70 | `20260704194635_temp_BG.json` | P58 | PATIENT | 2026-07-04 14:44:43 | **NO** | `-` | - |
| 71 | `20260715052203_temp_B.json` | P59 | CONTROL | 2026-07-04 09:50:22 | **NO** | `-` | - |
| 72 | `20260820141830_temp_AM.json` | P60 | PATIENT | 2026-07-04 10:50:31 | **SÍ** | `93b689a7-dfc2-4069-a935-efdde29de98a_raw.json` | 1.9 |
| 73 | `20260820141849_temp_P.json` | P61 | CONTROL | 2026-07-04 11:14:25 | **SÍ** | `b6487716-3d2f-4728-b000-cd71ccc723c2_raw.json` | 4.0 |
| 74 | `20260820141919_temp_BI.json` | P62 | PATIENT | 2026-07-04 11:50:45 | **NO** | `-` | - |
| 75 | `20260820142005_temp_Z.json` | P63 | PATIENT | 2026-07-04 12:49:13 | **SÍ** | `56108fef-0268-4f6f-920e-97787068b311_raw.json` | 0.2 |
| 76 | `20260820142006_temp_Z.json` | P63 | PATIENT | 2026-07-04 12:49:13 | **SÍ** | `56108fef-0268-4f6f-920e-97787068b311_raw.json` | 0.2 |
| 77 | `20260820142037_temp_T.json` | P64 | CONTROL | 2026-07-04 13:08:52 | **NO** | `-` | - |
| 78 | `20260820142101_temp_AN.json` | P65 | CONTROL | 2026-07-04 13:49:43 | **SÍ** | `0cce5b72-f8d0-458e-b576-64c138fd2b53_raw.json` | 52.6 |
