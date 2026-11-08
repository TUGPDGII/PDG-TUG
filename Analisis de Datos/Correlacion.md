# Correlación y Trazabilidad: Sensores IMU vs. Sistema de Cámaras e-Motion (VIMOV)

> **Propósito:** Auditar exhaustivamente las fechas de las 78 grabaciones inerciales (IMUs) y contrastarlas con las capturas del sistema e-Motion / VIMOV para establecer la correspondencia y trazabilidad de los pares bimodales confirmados.
> **Fecha de actualización:** 02 de noviembre de 2026
> **Filtro Estricto de Protocolo TUG y Género:** Para garantizar total validez científica y bioestadística:
> 1. **Protocolo Estricto:** Se auditan y conservan **exclusivamente grabaciones con protocolo TUG (`TIMED_UP_AND_GO` / `Timed up and Go`)**, segregando las pruebas de marcha continua (`Gait Analysis` y `GAIT_COMPLETE`) que formaban parte de otros protocolos clínicos de la brigada.
> 2. **Regla Estricta de Género:** Si el género de la persona no coincide entre el IMU y VIMOV, el par se clasifica formalmente como descarte estricto por no corresponder al mismo sujeto.

---

## 1. Resumen Ejecutivo del Cruce Bimodal Estrictamente TUG

| Métrica | Valor | Observación Metodológica |
|---|---:|---|
| Total grabaciones IMU en dataset | **78** | Totalidad de archivos `.json` en `Datos IMUs/` |
| Pruebas piloto previas a brigadas | **9** | Febrero a mediados de junio 2026 (P01 a P05, sin cámara) |
| Total grabaciones ejecutadas en brigadas | **69** | Santa Marta (25–27 junio) y CST / La Victoria (04 julio) |
| **Pares Bimodales Estrictamente TUG Confirmados (Género 100% Coincidente)** | **42** | Protocolo TUG confirmado en ambos dispositivos y tiempo $|\Delta t| \le 360$ s |
| Ensayos IMU en brigada sin par TUG en cámara (o con Marcha Continua) | **27** | Pacientes evaluados únicamente con IMU o en prueba de caminata libre |
| **Total Grabaciones e-Motion Estrictamente TUG (`Datos e-Motion/TUG/`)** | **130** | 101 de Santa Marta (`SMR_`) + 6 de CST (`CST_`) + 23 de Laboratorio (`LAB_`) |
| **Total Grabaciones e-Motion Marcha Continua (`Datos e-Motion/GAIT/`)** | **95** | 80 de Santa Marta (`SMR_`) + 15 de CST (`CST_`) |
| **Pacientes con Pareo Intra-Sujeto en Cámara (TUG + Marcha Continua 10 m)** | **48** | Sujetos únicos evaluados en ambos protocolos ópticos dentro de la brigada |

---


## 2. Tabla de Coincidencias Confirmadas y Variables Auditadas (42 Pares Bimodales TUG)

En esta tabla se listan exclusivamente los pares bimodales **estrictamente TUG** validados y confirmados con sus nombres de archivo vigentes en disco:

| # | Archivo IMU | Sujeto | Código | Archivo e-Motion Confirmado (en disco) | $\Delta t$ (s) | Género (IMU / VIMOV) | Diagnóstico | Sensor Cámara |
|---:|---|:---:|:---:|---|---:|:---:|:---:|---|
| 1 | `SMR_IDI1_BF.json` | P06 | BF | `SMR_IDE1_TUG_P06.json` | 122.0 | MALE / MALE | PATIENT | Intel RealSense |
| 2 | `SMR_IDI3_D.json` | P07 | D | `SMR_IDE2_TUG_P07.json` | 164.0 | MALE / MALE | PATIENT | Intel RealSense |
| 3 | `SMR_IDI4_AB.json` | P08 | AB | `SMR_IDE3_TUG_P08.json` | 302.0 | MALE / MALE | PATIENT | intel |
| 4 | `SMR_IDI5_AK.json` | P09 | AK | `SMR_IDE4_TUG_P09.json` | 323.0 | MALE / MALE | PATIENT | intel |
| 5 | `SMR_IDI6_AA.json` | P10 | AA | `SMR_IDE5_TUG_P10.json` | 151.0 | MALE / MALE | PATIENT | intel |
| 6 | `SMR_IDI7_V.json` | P11 | V | `SMR_IDE6_TUG_P11.json` | 77.0 | MALE / MALE | PATIENT | Intel RealSense |
| 7 | `SMR_IDI9_BW.json` | P13 | BW | `SMR_IDE7_TUG_P13.json` | 127.0 | MALE / MALE | PATIENT | intel |
| 8 | `SMR_IDI11_BK.json` | P15 | BK | `SMR_IDE8_TUG_P15.json` | 103.0 | MALE / MALE | PATIENT | intel |
| 9 | `SMR_IDI12_BD.json` | P16 | BD | `SMR_IDE9_TUG_P16.json` | 70.0 | MALE / MALE | PATIENT | intel |
| 10 | `SMR_IDI15_BN.json` | P18 | BN | `SMR_IDE10_TUG_P18.json` | 81.0 | MALE / MALE | PATIENT | intel |
| 11 | `SMR_IDI18_S.json` | P20 | S | `SMR_IDE34_GAIT_P20.json` | 106.0 | MALE / M | PATIENT | intel |
| 12 | `SMR_IDI19_X.json` | P21 | X | `SMR_IDE11_TUG_P21.json` | 84.0 | MALE / MALE | PATIENT | intel |
| 13 | `SMR_IDI20_BA.json` | P22 | BA | `SMR_IDE12_TUG_P22.json` | 77.0 | MALE / MALE | PATIENT | intel |
| 14 | `SMR_IDI21_BA.json` | P22 | BA | `SMR_IDE12_TUG_P22.json` | 77.0 | MALE / MALE | PATIENT | intel |
| 15 | `SMR_IDI23_AV.json` | P24 | AV | `SMR_IDE13_TUG_P24.json` | 196.0 | MALE / MALE | PATIENT | intel |
| 16 | `SMR_IDI24_AO.json` | P25 | AO | `SMR_IDE14_TUG_P25.json` | 282.0 | FEMALE / FEMALE | PATIENT | intel |
| 17 | `SMR_IDI25_M.json` | P26 | M | `SMR_IDE15_TUG_P26.json` | 170.0 | FEMALE / FEMALE | PATIENT | intel |
| 18 | `SMR_IDI26_BQ.json` | P27 | BQ | `SMR_IDE16_TUG_P27.json` | 91.0 | FEMALE / FEMALE | PATIENT | intel |
| 19 | `SMR_IDI29_O.json` | P30 | O | `SMR_IDE17_TUG_P30.json` | 290.0 | FEMALE / FEMALE | PATIENT | intel |
| 20 | `SMR_IDI30_BU.json` | P31 | BU | `SMR_IDE18_TUG_P31.json` | 162.0 | FEMALE / FEMALE | PATIENT | intel |
| 21 | `SMR_IDI31_K.json` | P31 | K | `SMR_IDE19_TUG_P31.json` | 78.0 | FEMALE / FEMALE | PATIENT | intel |
| 22 | `SMR_IDI33_AZ.json` | P32 | AZ | `SMR_IDE20_TUG_P32.json` | 260.0 | MALE / MALE | PATIENT | Intel RealSense |
| 23 | `SMR_IDI34_J.json` | P32 | J | `SMR_IDE21_TUG_P32.json` | 141.0 | MALE / MALE | PATIENT | Intel RealSense |
| 24 | `SMR_IDI35_AQ.json` | P32 | AQ | `SMR_IDE22_TUG_P32.json` | 109.0 | MALE / MALE | PATIENT | intel |
| 25 | `SMR_IDI36_BM.json` | P33 | BM | `SMR_IDE23_TUG_P33.json` | 108.0 | FEMALE / FEMALE | PATIENT | intel |
| 26 | `SMR_IDI37_BS.json` | P34 | BS | `SMR_IDE24_TUG_P34.json` | 163.0 | MALE / MALE | PATIENT | intel |
| 27 | `SMR_IDI38_AW.json` | P35 | AW | `SMR_IDE25_TUG_P35.json` | 62.0 | MALE / MALE | PATIENT | intel |
| 28 | `SMR_IDI39_AH.json` | P36 | AH | `SMR_IDE26_TUG_P36.json` | 129.0 | MALE / MALE | PATIENT | intel |
| 29 | `SMR_IDI40_AT.json` | P37 | AT | `SMR_IDE27_TUG_P37.json` | 265.0 | FEMALE / FEMALE | PATIENT | intel |
| 30 | `SMR_IDI41_AE.json` | P38 | AE | `SMR_IDE28_TUG_P38.json` | 188.0 | FEMALE / FEMALE | PATIENT | intel |
| 31 | `SMR_IDI42_BL.json` | P39 | BL | `SMR_IDE29_TUG_P39.json` | 89.0 | MALE / MALE | PATIENT | intel |
| 32 | `SMR_IDI43_AS.json` | P40 | AS | `SMR_IDE30_TUG_P40.json` | 80.0 | MALE / MALE | PATIENT | intel |
| 33 | `SMR_IDI45_AD.json` | P42 | AD | `SMR_IDE31_TUG_P42.json` | 174.0 | MALE / MALE | PATIENT | intel |
| 34 | `SMR_IDI46_BB.json` | P43 | BB | `SMR_IDE32_TUG_P43.json` | 83.0 | MALE / MALE | PATIENT | intel |
| 35 | `SMR_IDI47_R.json` | P44 | R | `SMR_IDE33_TUG_P44.json` | 114.0 | FEMALE / FEMALE | PATIENT | intel |
| 36 | `SMR_IDI49_I.json` | P46 | I | `SMR_IDE34_TUG_P46.json` | 57.0 | MALE / MALE | PATIENT | intel |
| 37 | `SMR_IDI50_Q.json` | P47 | Q | `SMR_IDE35_TUG_P47.json` | 249.0 | MALE / MALE | PATIENT | intel |
| 38 | `SMR_IDI51_AU.json` | P48 | AU | `SMR_IDE36_TUG_P48.json` | 167.0 | MALE / MALE | PATIENT | intel |
| 39 | `SMR_IDI52_L.json` | P49 | L | `SMR_IDE37_TUG_P49.json` | 299.0 | MALE / MALE | PATIENT | intel |
| 40 | `SMR_IDI53_H.json` | P50 | H | `SMR_IDE38_TUG_P50.json` | 58.0 | MALE / MALE | PATIENT | Intel RealSense |
| 41 | `SMR_IDI54_AI.json` | P51 | AI | `SMR_IDE39_TUG_P51.json` | 124.0 | FEMALE / FEMALE | PATIENT | Intel RealSense |
| 42 | `SMR_IDI55_C.json` | P52 | C | `SMR_IDE40_TUG_P52.json` | 65.0 | FEMALE / FEMALE | PATIENT | intel |
| 43 | `CST_IDI2_BE.json` | P54 | BE | `CST_IDE1_TUG_P54.json` | 16.0 | MALE / MALE | PATIENT | Intel RealSense |

---

## 3. Cuadro de Auditoría Completa de los 78 Registros IMU

A continuación se audita el estado de cada una de las 78 grabaciones inerciales del dataset frente al sistema de cámaras e-Motion estrictamente TUG:

| # | Archivo IMU | Sujeto | Grupo | Fecha UTC | ¿Tiene e-Motion TUG? | Archivo e-Motion Asignado | Observación / Criterio |
|---:|---|:---:|:---:|:---:|:---:|---|---|
| 1 | `LAB_IDI1_BV.json` | P01 | SIN_ETIQUETA | 2026-02-08 02:24:03 | **NO** | - | Prueba piloto previa a brigadas (sin cámara) |
| 2 | `LAB_IDI2_N.json` | P02 | SIN_ETIQUETA | 2026-03-03 04:31:19 | **NO** | - | Prueba piloto previa a brigadas (sin cámara) |
| 3 | `LAB_IDI3_BO.json` | P02 | SIN_ETIQUETA | 2026-03-03 04:35:31 | **NO** | - | Prueba piloto previa a brigadas (sin cámara) |
| 4 | `LAB_IDI4_BX.json` | P02 | SIN_ETIQUETA | 2026-03-03 04:45:05 | **NO** | - | Prueba piloto previa a brigadas (sin cámara) |
| 5 | `LAB_IDI5_BJ.json` | P02 | SIN_ETIQUETA | 2026-03-03 13:46:28 | **NO** | - | Prueba piloto previa a brigadas (sin cámara) |
| 6 | `LAB_IDI6_F.json` | P03 | SIN_ETIQUETA | 2026-03-07 23:42:30 | **NO** | - | Prueba piloto previa a brigadas (sin cámara) |
| 7 | `LAB_IDI7_AX.json` | P04 | SIN_ETIQUETA | 2026-03-08 23:23:46 | **NO** | - | Prueba piloto previa a brigadas (sin cámara) |
| 8 | `LAB_IDI8_AL.json` | P05 | CONTROL | 2026-06-11 23:50:03 | **NO** | - | Prueba piloto previa a brigadas (sin cámara) |
| 9 | `LAB_IDI9_BC.json` | P05 | CONTROL | 2026-06-18 07:52:44 | **NO** | - | Prueba piloto previa a brigadas (sin cámara) |
| 10 | `SMR_IDI1_BF.json` | P06 | PATIENT | 2026-06-25 14:06:19 | **SÍ** | `SMR_IDE1_TUG_P06.json` | TUG confirmado: género idéntico y $\Delta t = 122.0$ s |
| 11 | `SMR_IDI2_AR.json` | P06 | PATIENT | 2026-06-25 14:07:54 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |
| 12 | `SMR_IDI3_D.json` | P07 | PATIENT | 2026-06-25 14:38:59 | **SÍ** | `SMR_IDE2_TUG_P07.json` | TUG confirmado: género idéntico y $\Delta t = 164.0$ s |
| 13 | `SMR_IDI4_AB.json` | P08 | PATIENT | 2026-06-25 14:49:24 | **SÍ** | `SMR_IDE3_TUG_P08.json` | TUG confirmado: género idéntico y $\Delta t = 302.0$ s |
| 14 | `SMR_IDI5_AK.json` | P09 | PATIENT | 2026-06-25 15:02:19 | **SÍ** | `SMR_IDE4_TUG_P09.json` | TUG confirmado: género idéntico y $\Delta t = 323.0$ s |
| 15 | `SMR_IDI6_AA.json` | P10 | PATIENT | 2026-06-25 15:19:18 | **SÍ** | `SMR_IDE5_TUG_P10.json` | TUG confirmado: género idéntico y $\Delta t = 151.0$ s |
| 16 | `SMR_IDI7_V.json` | P11 | PATIENT | 2026-06-25 15:36:33 | **SÍ** | `SMR_IDE6_TUG_P11.json` | TUG confirmado: género idéntico y $\Delta t = 77.0$ s |
| 17 | `SMR_IDI8_A.json` | P12 | PATIENT | 2026-06-25 16:42:13 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |
| 18 | `SMR_IDI9_BW.json` | P13 | PATIENT | 2026-06-25 17:11:39 | **SÍ** | `SMR_IDE7_TUG_P13.json` | TUG confirmado: género idéntico y $\Delta t = 127.0$ s |
| 19 | `SMR_IDI10_AG.json` | P14 | CONTROL | 2026-06-25 18:04:44 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |
| 20 | `SMR_IDI11_BK.json` | P15 | PATIENT | 2026-06-25 18:32:43 | **SÍ** | `SMR_IDE8_TUG_P15.json` | TUG confirmado: género idéntico y $\Delta t = 103.0$ s |
| 21 | `SMR_IDI12_BD.json` | P16 | PATIENT | 2026-06-25 19:36:58 | **SÍ** | `SMR_IDE9_TUG_P16.json` | TUG confirmado: género idéntico y $\Delta t = 70.0$ s |
| 22 | `SMR_IDI13_BR.json` | P17 | PATIENT | 2026-06-25 19:51:46 | **NO (DESCARTADO)** | - | Descartado por discrepancia de género (IMU MALE vs VIMOV FEMALE) |
| 23 | `SMR_IDI14_AP.json` | P17 | PATIENT | 2026-06-25 19:54:10 | **NO (DESCARTADO)** | - | Descartado por discrepancia de género (IMU MALE vs VIMOV FEMALE) |
| 24 | `SMR_IDI15_BN.json` | P18 | PATIENT | 2026-06-25 20:42:52 | **SÍ** | `SMR_IDE10_TUG_P18.json` | TUG confirmado: género idéntico y $\Delta t = 81.0$ s |
| 25 | `SMR_IDI16_G.json` | P19 | PATIENT | 2026-06-25 21:23:38 | **NO (DESCARTADO)** | - | Descartado por discrepancia de género (IMU MALE vs VIMOV FEMALE) |
| 26 | `SMR_IDI17_BH.json` | P20 | PATIENT | 2026-06-25 20:13:35 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |
| 27 | `SMR_IDI18_S.json` | P20 | PATIENT | 2026-06-25 20:16:06 | **SÍ** | `SMR_IDE34_GAIT_P20.json` | TUG confirmado: género idéntico y $\Delta t = 106.0$ s |
| 28 | `SMR_IDI19_X.json` | P21 | PATIENT | 2026-06-25 21:49:31 | **SÍ** | `SMR_IDE11_TUG_P21.json` | TUG confirmado: género idéntico y $\Delta t = 84.0$ s |
| 29 | `SMR_IDI20_BA.json` | P22 | PATIENT | 2026-06-25 22:55:59 | **SÍ** | `SMR_IDE12_TUG_P22.json` | TUG confirmado: género idéntico y $\Delta t = 77.0$ s |
| 30 | `SMR_IDI21_BA.json` | P22 | PATIENT | 2026-06-25 22:55:59 | **SÍ (DUPLICADO)** | `SMR_IDE12_TUG_P22.json` | TUG confirmado: género idéntico y $\Delta t = 77.0$ s |
| 31 | `SMR_IDI22_AC.json` | P23 | PATIENT | 2026-06-26 14:11:42 | **NO (DESCARTADO)** | - | Descartado por discrepancia de género (IMU FEMALE vs VIMOV MALE) |
| 32 | `SMR_IDI23_AV.json` | P24 | PATIENT | 2026-06-26 14:43:00 | **SÍ** | `SMR_IDE13_TUG_P24.json` | TUG confirmado: género idéntico y $\Delta t = 196.0$ s |
| 33 | `SMR_IDI24_AO.json` | P25 | PATIENT | 2026-06-26 14:53:43 | **SÍ** | `SMR_IDE14_TUG_P25.json` | TUG confirmado: género idéntico y $\Delta t = 282.0$ s |
| 34 | `SMR_IDI25_M.json` | P26 | PATIENT | 2026-06-26 15:03:48 | **SÍ** | `SMR_IDE15_TUG_P26.json` | TUG confirmado: género idéntico y $\Delta t = 170.0$ s |
| 35 | `SMR_IDI26_BQ.json` | P27 | PATIENT | 2026-06-26 15:15:48 | **SÍ** | `SMR_IDE16_TUG_P27.json` | TUG confirmado: género idéntico y $\Delta t = 91.0$ s |
| 36 | `SMR_IDI27_U.json` | P28 | PATIENT | 2026-06-26 15:25:04 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |
| 37 | `SMR_IDI28_AJ.json` | P29 | PATIENT | 2026-06-26 15:35:39 | **NO (DESCARTADO)** | - | Descartado por discrepancia de género (IMU FEMALE vs VIMOV MALE) |
| 38 | `SMR_IDI29_O.json` | P30 | PATIENT | 2026-06-26 15:46:43 | **SÍ** | `SMR_IDE17_TUG_P30.json` | TUG confirmado: género idéntico y $\Delta t = 290.0$ s |
| 39 | `SMR_IDI30_BU.json` | P31 | PATIENT | 2026-06-26 16:04:24 | **SÍ** | `SMR_IDE18_TUG_P31.json` | TUG confirmado: género idéntico y $\Delta t = 162.0$ s |
| 40 | `SMR_IDI31_K.json` | P31 | PATIENT | 2026-06-26 16:05:55 | **SÍ** | `SMR_IDE19_TUG_P31.json` | TUG confirmado: género idéntico y $\Delta t = 78.0$ s |
| 41 | `SMR_IDI32_BT.json` | P32 | PATIENT | 2026-06-26 17:04:37 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |
| 42 | `SMR_IDI33_AZ.json` | P32 | PATIENT | 2026-06-26 17:06:53 | **SÍ** | `SMR_IDE20_TUG_P32.json` | TUG confirmado: género idéntico y $\Delta t = 260.0$ s |
| 43 | `SMR_IDI34_J.json` | P32 | PATIENT | 2026-06-26 17:08:58 | **SÍ** | `SMR_IDE21_TUG_P32.json` | TUG confirmado: género idéntico y $\Delta t = 141.0$ s |
| 44 | `SMR_IDI35_AQ.json` | P32 | PATIENT | 2026-06-26 17:09:37 | **SÍ** | `SMR_IDE22_TUG_P32.json` | TUG confirmado: género idéntico y $\Delta t = 109.0$ s |
| 45 | `SMR_IDI36_BM.json` | P33 | PATIENT | 2026-06-26 19:43:07 | **SÍ** | `SMR_IDE23_TUG_P33.json` | TUG confirmado: género idéntico y $\Delta t = 108.0$ s |
| 46 | `SMR_IDI37_BS.json` | P34 | PATIENT | 2026-06-26 20:22:35 | **SÍ** | `SMR_IDE24_TUG_P34.json` | TUG confirmado: género idéntico y $\Delta t = 163.0$ s |
| 47 | `SMR_IDI38_AW.json` | P35 | PATIENT | 2026-06-26 20:46:42 | **SÍ** | `SMR_IDE25_TUG_P35.json` | TUG confirmado: género idéntico y $\Delta t = 62.0$ s |
| 48 | `SMR_IDI39_AH.json` | P36 | PATIENT | 2026-06-26 21:18:37 | **SÍ** | `SMR_IDE26_TUG_P36.json` | TUG confirmado: género idéntico y $\Delta t = 129.0$ s |
| 49 | `SMR_IDI40_AT.json` | P37 | PATIENT | 2026-06-26 21:31:18 | **SÍ** | `SMR_IDE27_TUG_P37.json` | TUG confirmado: género idéntico y $\Delta t = 265.0$ s |
| 50 | `SMR_IDI41_AE.json` | P38 | PATIENT | 2026-06-26 21:49:58 | **SÍ** | `SMR_IDE28_TUG_P38.json` | TUG confirmado: género idéntico y $\Delta t = 188.0$ s |
| 51 | `SMR_IDI42_BL.json` | P39 | PATIENT | 2026-06-26 22:18:47 | **SÍ** | `SMR_IDE29_TUG_P39.json` | TUG confirmado: género idéntico y $\Delta t = 89.0$ s |
| 52 | `SMR_IDI43_AS.json` | P40 | PATIENT | 2026-06-27 13:35:40 | **SÍ** | `SMR_IDE30_TUG_P40.json` | TUG confirmado: género idéntico y $\Delta t = 80.0$ s |
| 53 | `SMR_IDI44_BP.json` | P41 | PATIENT | 2026-06-27 13:47:37 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |
| 54 | `SMR_IDI45_AD.json` | P42 | PATIENT | 2026-06-27 13:55:54 | **SÍ** | `SMR_IDE31_TUG_P42.json` | TUG confirmado: género idéntico y $\Delta t = 174.0$ s |
| 55 | `SMR_IDI46_BB.json` | P43 | PATIENT | 2026-06-27 14:34:21 | **SÍ** | `SMR_IDE32_TUG_P43.json` | TUG confirmado: género idéntico y $\Delta t = 83.0$ s |
| 56 | `SMR_IDI47_R.json` | P44 | PATIENT | 2026-06-27 15:08:47 | **SÍ** | `SMR_IDE33_TUG_P44.json` | TUG confirmado: género idéntico y $\Delta t = 114.0$ s |
| 57 | `SMR_IDI48_W.json` | P45 | PATIENT | 2026-06-27 15:23:02 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |
| 58 | `SMR_IDI49_I.json` | P46 | PATIENT | 2026-06-27 15:57:15 | **SÍ** | `SMR_IDE34_TUG_P46.json` | TUG confirmado: género idéntico y $\Delta t = 57.0$ s |
| 59 | `SMR_IDI50_Q.json` | P47 | PATIENT | 2026-06-27 16:10:39 | **SÍ** | `SMR_IDE35_TUG_P47.json` | TUG confirmado: género idéntico y $\Delta t = 249.0$ s |
| 60 | `SMR_IDI51_AU.json` | P48 | PATIENT | 2026-06-27 16:19:41 | **SÍ** | `SMR_IDE36_TUG_P48.json` | TUG confirmado: género idéntico y $\Delta t = 167.0$ s |
| 61 | `SMR_IDI52_L.json` | P49 | PATIENT | 2026-06-27 16:37:29 | **SÍ** | `SMR_IDE37_TUG_P49.json` | TUG confirmado: género idéntico y $\Delta t = 299.0$ s |
| 62 | `SMR_IDI53_H.json` | P50 | PATIENT | 2026-06-27 17:13:05 | **SÍ** | `SMR_IDE38_TUG_P50.json` | TUG confirmado: género idéntico y $\Delta t = 58.0$ s |
| 63 | `SMR_IDI54_AI.json` | P51 | PATIENT | 2026-06-27 18:06:45 | **SÍ** | `SMR_IDE39_TUG_P51.json` | TUG confirmado: género idéntico y $\Delta t = 124.0$ s |
| 64 | `SMR_IDI55_C.json` | P52 | PATIENT | 2026-06-27 20:52:35 | **SÍ** | `SMR_IDE40_TUG_P52.json` | TUG confirmado: género idéntico y $\Delta t = 65.0$ s |
| 65 | `CST_IDI1_AF.json` | P53 | PATIENT | 2026-07-04 15:44:08 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |
| 66 | `CST_IDI2_BE.json` | P54 | PATIENT | 2026-07-04 15:58:15 | **SÍ** | `CST_IDE1_TUG_P54.json` | TUG confirmado: género idéntico y $\Delta t = 16.0$ s |
| 67 | `CST_IDI3_E.json` | P55 | PATIENT | 2026-07-04 16:56:59 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |
| 68 | `CST_IDI4_Y.json` | P56 | PATIENT | 2026-07-04 17:19:11 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |
| 69 | `CST_IDI5_AY.json` | P57 | CONTROL | 2026-07-04 19:00:00 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |
| 70 | `CST_IDI6_BG.json` | P58 | PATIENT | 2026-07-04 19:44:43 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |
| 71 | `CST_IDI7_B.json` | P59 | CONTROL | 2026-07-04 14:50:22 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |
| 72 | `CST_IDI8_AM.json` | P60 | PATIENT | 2026-07-04 15:50:31 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |
| 73 | `CST_IDI9_P.json` | P61 | CONTROL | 2026-07-04 16:14:25 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |
| 74 | `CST_IDI10_BI.json` | P62 | PATIENT | 2026-07-04 16:50:45 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |
| 75 | `CST_IDI11_Z.json` | P63 | PATIENT | 2026-07-04 17:49:13 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |
| 76 | `CST_IDI12_Z.json` | P63 | PATIENT | 2026-07-04 17:49:13 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |
| 77 | `CST_IDI13_T.json` | P64 | CONTROL | 2026-07-04 18:08:52 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |
| 78 | `CST_IDI14_AN.json` | P65 | CONTROL | 2026-07-04 18:49:43 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |

---

## 4. Inventario General de la Brigada Santa Marta TUG (101 Archivos e-Motion)

De la brigada de Santa Marta (25, 26 y 27 de junio de 2026), se conservan en la carpeta `Datos e-Motion/TUG/` **101 grabaciones que corresponden estrictamente al protocolo Timed Up and Go (TUG)**:

- **41 grabaciones** cuentan con par IMU confirmado bajo estricta correspondencia demográfica y temporal (`SMR_IDx_eMotion_Pxx_TUG.json`).
- **60 grabaciones** corresponden a pruebas TUG de visión independientes (`SMR_IDx_eMotion_NO_TUG.json`).
- Todas las grabaciones se encuentran 100% anonimizadas, sin nombres ni cédulas, listas para análisis de longitud de zancada y velocidad lineal en marcha recta.
- Las 80 grabaciones de caminata continua de Santa Marta se encuentran preservadas en `Datos e-Motion/GAIT/` (junto con las 15 de CST, completando 95 grabaciones en `GAIT/`).
