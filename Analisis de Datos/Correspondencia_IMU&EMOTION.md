# Correspondencia y Trazabilidad: Sensores IMU vs. Sistema de Cámaras e-Motion (VIMOV)

> **Propósito:** Responder al requerimiento del profesor Domiciano Rincón de auditar las fechas de los 78 archivos de datos IMU y contrastarlas con las grabaciones del sistema e-Motion / VIMOV para determinar con exactitud quiénes cuentan con su versión de cámara y quiénes no.
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
| Ensayos IMU descartados por discrepancia estricta de género | **5** | Cámara evaluaba paciente del sexo opuesto en ventana horaria cercana |
| Ensayos IMU en brigada sin par TUG en cámara (o con Gait Analysis) | **22** | Pacientes evaluados únicamente con IMU o en prueba de caminata libre |
| **Total Grabaciones e-Motion Estrictamente TUG en Carpeta Principal** | **132** | 103 de Santa Marta (`SMR_`) + 5 de CST (`CST_`) + 24 de Lab (`LAB_`) |
| Grabaciones de Marcha Continua Segregadas (`No_TUG_Gait_Analysis/`) | **137** | 98 `Gait Analysis` + 37 `GAIT_COMPLETE` + 2 archivos de métricas |

---

## 2. Ensayos Descartados por Discrepancia Estricta de Género

Siguiendo la directriz del proyecto: **si el género de la persona no coincide, el archivo no corresponde a la misma prueba ni al mismo paciente**.

A continuación se detallan los 5 casos donde, a pesar de existir una captura en VIMOV en un intervalo cercano de tiempo, la auditoría demográfica descartó el emparejamiento:

| Archivo IMU | Sujeto IMU | Género IMU | Sujeto Registrado en VIMOV | Género e-Motion | Motivo del Descarte |
|---|:---:|:---:|---|:---:|---|
| `20260625195406_temp_BR.json` | P17 | **MASCULINO** | `GEOREF411` (68 años) | **FEMENINO** | Discrepancia de género: cámara evaluaba a paciente mujer mientras IMU evaluaba a hombre. |
| `20260625195426_temp_AP.json` | P17 | **MASCULINO** | `GEOREF411` (68 años) | **FEMENINO** | Discrepancia de género en segunda repetición. |
| `20260625212453_temp_G.json` | P19 | **MASCULINO** | `GEOREF417` (72 años) | **FEMENINO** | Discrepancia de género: cámara evaluaba a paciente mujer mientras IMU evaluaba a hombre. |
| `20260626141246_temp_AC.json` | P23 | **FEMENINO** | `LARGE_PD_862` | **MASCULINO** | Discrepancia de género: IMU femenino vs VIMOV masculino. |
| `20260626153637_temp_AJ.json` | P29 | **FEMENINO** | `GEOREF425` | **MASCULINO** | Discrepancia de género: IMU femenino vs VIMOV masculino. |

---

## 3. Tabla de Coincidencias Confirmadas y Variables Auditadas (42 Pares Bimodales TUG)

En esta tabla se listan exclusivamente los pares bimodales **estrictamente TUG** validados y confirmados con sus nombres de archivo vigentes en disco:

| # | Archivo IMU | Sujeto | Código | Archivo e-Motion Confirmado (en disco) | $\Delta t$ (s) | Género (IMU / VIMOV) | Diagnóstico | Sensor Cámara |
|---:|---|:---:|:---:|---|---:|:---:|:---:|---|
| 1 | `20260625140746_temp_BF.json` | P06 | BF | `SMR_20260625_P06_BF_4cd523b7_raw.json` | 122.0 | MALE / MALE | PATIENT | Intel RealSense |
| 2 | `20260625144044_temp_D.json` | P07 | D | `SMR_20260625_P07_D_c71c489e_raw.json` | 164.0 | MALE / MALE | PATIENT | Intel RealSense |
| 3 | `20260625145018_temp_AB.json` | P08 | AB | `SMR_20260625_P08_AB_ff5603a4_raw.json` | 302.0 | MALE / MALE | PATIENT | intel |
| 4 | `20260625150353_temp_AK.json` | P09 | AK | `SMR_20260625_P09_AK_2adb11ee_raw.json` | 323.0 | MALE / MALE | PATIENT | intel |
| 5 | `20260625152019_temp_AA.json` | P10 | AA | `SMR_20260625_P10_AA_bf709abb_raw.json` | 151.0 | MALE / MALE | PATIENT | intel |
| 6 | `20260625153756_temp_V.json` | P11 | V | `SMR_20260625_P11_V_7ed2f2de_raw.json` | 77.0 | MALE / MALE | PATIENT | Intel RealSense |
| 7 | `20260625171352_temp_BW.json` | P13 | BW | `SMR_20260625_P13_BW_5eeb5a37_raw.json` | 127.0 | MALE / MALE | PATIENT | intel |
| 8 | `20260625183434_temp_BK.json` | P15 | BK | `SMR_20260625_P15_BK_b8317644_raw.json` | 103.0 | MALE / MALE | PATIENT | intel |
| 9 | `20260625193811_temp_BD.json` | P16 | BD | `SMR_20260625_P16_BD_f16693f6_raw.json` | 70.0 | MALE / MALE | PATIENT | intel |
| 10 | `20260625204358_temp_BN.json` | P18 | BN | `SMR_20260625_P18_BN_1f325d38_raw.json` | 81.0 | MALE / MALE | PATIENT | intel |
| 11 | `20260625214518_temp_S.json` | P20 | S | `SMR_20260625_P20_S_dde1028c_raw.json` | 106.0 | MALE / M | PATIENT | intel |
| 12 | `20260625215046_temp_X.json` | P21 | X | `SMR_20260625_P21_X_28ac951e_raw.json` | 84.0 | MALE / MALE | PATIENT | intel |
| 13 | `20260626133915_temp_BA.json` | P22 | BA | `SMR_20260625_P22_BA_a22ff952_raw.json` | 77.0 | MALE / MALE | PATIENT | intel |
| 14 | `20260626133916_temp_BA.json` | P22 | BA | `SMR_20260625_P22_BA_a22ff952_raw.json` | 77.0 | MALE / MALE | PATIENT | intel |
| 15 | `20260626144433_temp_AV.json` | P24 | AV | `SMR_20260626_P24_AV_fc8711e0_raw.json` | 196.0 | MALE / MALE | PATIENT | intel |
| 16 | `20260626145512_temp_AO.json` | P25 | AO | `SMR_20260626_P25_AO_ce5691b9_raw.json` | 282.0 | FEMALE / FEMALE | PATIENT | intel |
| 17 | `20260626150532_temp_M.json` | P26 | M | `SMR_20260626_P26_M_0ec82be7_raw.json` | 170.0 | FEMALE / FEMALE | PATIENT | intel |
| 18 | `20260626151711_temp_BQ.json` | P27 | BQ | `SMR_20260626_P27_BQ_156f5309_raw.json` | 91.0 | FEMALE / FEMALE | PATIENT | intel |
| 19 | `20260626154758_temp_O.json` | P30 | O | `SMR_20260626_P30_O_5432070f_raw.json` | 290.0 | FEMALE / FEMALE | PATIENT | intel |
| 20 | `20260626160554_temp_BU.json` | P31 | BU | `SMR_20260626_P31_BU_f89f97d0_raw.json` | 162.0 | FEMALE / FEMALE | PATIENT | intel |
| 21 | `20260626160620_temp_K.json` | P31 | K | `SMR_20260626_P31_K_4e5316e1_raw.json` | 78.0 | FEMALE / FEMALE | PATIENT | intel |
| 22 | `20260626170733_temp_AZ.json` | P32 | AZ | `SMR_20260626_P32_AZ_fbe58f01_raw.json` | 260.0 | MALE / MALE | PATIENT | Intel RealSense |
| 23 | `20260626170919_temp_J.json` | P32 | J | `SMR_20260626_P32_J_dabe0112_raw.json` | 141.0 | MALE / MALE | PATIENT | Intel RealSense |
| 24 | `20260626170956_temp_AQ.json` | P32 | AQ | `SMR_20260626_P32_AQ_22f0ff21_raw.json` | 109.0 | MALE / MALE | PATIENT | intel |
| 25 | `20260626194407_temp_BM.json` | P33 | BM | `SMR_20260626_P33_BM_ed61ac9f_raw.json` | 108.0 | FEMALE / FEMALE | PATIENT | intel |
| 26 | `20260626202515_temp_BS.json` | P34 | BS | `SMR_20260626_P34_BS_87a49c65_raw.json` | 163.0 | MALE / MALE | PATIENT | intel |
| 27 | `20260626204728_temp_AW.json` | P35 | AW | `SMR_20260626_P35_AW_452eaaa1_raw.json` | 62.0 | MALE / MALE | PATIENT | intel |
| 28 | `20260626211937_temp_AH.json` | P36 | AH | `SMR_20260626_P36_AH_b622b020_raw.json` | 129.0 | MALE / MALE | PATIENT | intel |
| 29 | `20260626213214_temp_AT.json` | P37 | AT | `SMR_20260626_P37_AT_0dcde044_raw.json` | 265.0 | FEMALE / FEMALE | PATIENT | intel |
| 30 | `20260626215053_temp_AE.json` | P38 | AE | `SMR_20260626_P38_AE_80c945b3_raw.json` | 188.0 | FEMALE / FEMALE | PATIENT | intel |
| 31 | `20260626222007_temp_BL.json` | P39 | BL | `SMR_20260626_P39_BL_294c3933_raw.json` | 89.0 | MALE / MALE | PATIENT | intel |
| 32 | `20260627133637_temp_AS.json` | P40 | AS | `SMR_20260627_P40_AS_4df833f1_raw.json` | 80.0 | MALE / MALE | PATIENT | intel |
| 33 | `20260627135720_temp_AD.json` | P42 | AD | `SMR_20260627_P42_AD_25f298d4_raw.json` | 174.0 | MALE / MALE | PATIENT | intel |
| 34 | `20260627143518_temp_BB.json` | P43 | BB | `SMR_20260627_P43_BB_580b902a_raw.json` | 83.0 | MALE / MALE | PATIENT | intel |
| 35 | `20260627150939_temp_R.json` | P44 | R | `SMR_20260627_P44_R_89d757d6_raw.json` | 114.0 | FEMALE / FEMALE | PATIENT | intel |
| 36 | `20260627155804_temp_I.json` | P46 | I | `SMR_20260627_P46_I_ba2c6e63_raw.json` | 57.0 | MALE / MALE | PATIENT | intel |
| 37 | `20260627161148_temp_Q.json` | P47 | Q | `SMR_20260627_P47_Q_907121bd_raw.json` | 249.0 | MALE / MALE | PATIENT | intel |
| 38 | `20260627162118_temp_AU.json` | P48 | AU | `SMR_20260627_P48_AU_4781f6d7_raw.json` | 167.0 | MALE / MALE | PATIENT | intel |
| 39 | `20260627163836_temp_L.json` | P49 | L | `SMR_20260627_P49_L_6943624b_raw.json` | 299.0 | MALE / MALE | PATIENT | intel |
| 40 | `20260627171353_temp_H.json` | P50 | H | `SMR_20260627_P50_H_d3efbdfa_raw.json` | 58.0 | MALE / MALE | PATIENT | Intel RealSense |
| 41 | `20260627180847_temp_AI.json` | P51 | AI | `SMR_20260627_P51_AI_18c58989_raw.json` | 124.0 | FEMALE / FEMALE | PATIENT | Intel RealSense |
| 42 | `20260627205326_temp_C.json` | P52 | C | `SMR_20260627_P52_C_029c450a_raw.json` | 65.0 | FEMALE / FEMALE | PATIENT | intel |
| 43 | `20260704155929_temp_BE.json` | P54 | BE | `CST_20260704_P54_BE_c1b8493f_raw.json` | 16.0 | MALE / MALE | PATIENT | Intel RealSense |

---

## 4. Cuadro de Auditoría Completa de los 78 Registros IMU

A continuación se audita el estado de cada una de las 78 grabaciones inerciales del dataset frente al sistema de cámaras e-Motion estrictamente TUG:

| # | Archivo IMU | Sujeto | Grupo | Fecha UTC | ¿Tiene e-Motion TUG? | Archivo e-Motion Asignado | Observación / Criterio |
|---:|---|:---:|:---:|:---:|:---:|---|---|
| 1 | `20260208022404_temp_BV.json` | P01 | SIN_ETIQUETA | 2026-02-08 02:24:03 | **NO** | - | Prueba piloto previa a brigadas (sin cámara) |
| 2 | `20260303043120_temp_N.json` | P02 | SIN_ETIQUETA | 2026-03-03 04:31:19 | **NO** | - | Prueba piloto previa a brigadas (sin cámara) |
| 3 | `20260303043532_temp_BO.json` | P02 | SIN_ETIQUETA | 2026-03-03 04:35:31 | **NO** | - | Prueba piloto previa a brigadas (sin cámara) |
| 4 | `20260303044505_temp_BX.json` | P02 | SIN_ETIQUETA | 2026-03-03 04:45:05 | **NO** | - | Prueba piloto previa a brigadas (sin cámara) |
| 5 | `20260303134630_temp_BJ.json` | P02 | SIN_ETIQUETA | 2026-03-03 13:46:28 | **NO** | - | Prueba piloto previa a brigadas (sin cámara) |
| 6 | `20260307234249_temp_F.json` | P03 | SIN_ETIQUETA | 2026-03-07 23:42:30 | **NO** | - | Prueba piloto previa a brigadas (sin cámara) |
| 7 | `20260308232420_temp_AX.json` | P04 | SIN_ETIQUETA | 2026-03-08 23:23:46 | **NO** | - | Prueba piloto previa a brigadas (sin cámara) |
| 8 | `20260611235032_temp_AL.json` | P05 | CONTROL | 2026-06-11 23:50:03 | **NO** | - | Prueba piloto previa a brigadas (sin cámara) |
| 9 | `20260618075259_temp_BC.json` | P05 | CONTROL | 2026-06-18 07:52:44 | **NO** | - | Prueba piloto previa a brigadas (sin cámara) |
| 10 | `20260625140746_temp_BF.json` | P06 | PATIENT | 2026-06-25 14:06:19 | **SÍ** | `SMR_20260625_P06_BF_4cd523b7_raw.json` | TUG confirmado: género idéntico y $\Delta t = 122.0$ s |
| 11 | `20260625140851_temp_AR.json` | P06 | PATIENT | 2026-06-25 14:07:54 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |
| 12 | `20260625144044_temp_D.json` | P07 | PATIENT | 2026-06-25 14:38:59 | **SÍ** | `SMR_20260625_P07_D_c71c489e_raw.json` | TUG confirmado: género idéntico y $\Delta t = 164.0$ s |
| 13 | `20260625145018_temp_AB.json` | P08 | PATIENT | 2026-06-25 14:49:24 | **SÍ** | `SMR_20260625_P08_AB_ff5603a4_raw.json` | TUG confirmado: género idéntico y $\Delta t = 302.0$ s |
| 14 | `20260625150353_temp_AK.json` | P09 | PATIENT | 2026-06-25 15:02:19 | **SÍ** | `SMR_20260625_P09_AK_2adb11ee_raw.json` | TUG confirmado: género idéntico y $\Delta t = 323.0$ s |
| 15 | `20260625152019_temp_AA.json` | P10 | PATIENT | 2026-06-25 15:19:18 | **SÍ** | `SMR_20260625_P10_AA_bf709abb_raw.json` | TUG confirmado: género idéntico y $\Delta t = 151.0$ s |
| 16 | `20260625153756_temp_V.json` | P11 | PATIENT | 2026-06-25 15:36:33 | **SÍ** | `SMR_20260625_P11_V_7ed2f2de_raw.json` | TUG confirmado: género idéntico y $\Delta t = 77.0$ s |
| 17 | `20260625164351_temp_A.json` | P12 | PATIENT | 2026-06-25 16:42:13 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |
| 18 | `20260625171352_temp_BW.json` | P13 | PATIENT | 2026-06-25 17:11:39 | **SÍ** | `SMR_20260625_P13_BW_5eeb5a37_raw.json` | TUG confirmado: género idéntico y $\Delta t = 127.0$ s |
| 19 | `20260625180613_temp_AG.json` | P14 | CONTROL | 2026-06-25 18:04:44 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |
| 20 | `20260625183434_temp_BK.json` | P15 | PATIENT | 2026-06-25 18:32:43 | **SÍ** | `SMR_20260625_P15_BK_b8317644_raw.json` | TUG confirmado: género idéntico y $\Delta t = 103.0$ s |
| 21 | `20260625193811_temp_BD.json` | P16 | PATIENT | 2026-06-25 19:36:58 | **SÍ** | `SMR_20260625_P16_BD_f16693f6_raw.json` | TUG confirmado: género idéntico y $\Delta t = 70.0$ s |
| 22 | `20260625195406_temp_BR.json` | P17 | PATIENT | 2026-06-25 19:51:46 | **NO (DESCARTADO)** | - | Descartado por discrepancia de género (IMU MALE vs VIMOV FEMALE) |
| 23 | `20260625195426_temp_AP.json` | P17 | PATIENT | 2026-06-25 19:54:10 | **NO (DESCARTADO)** | - | Descartado por discrepancia de género (IMU MALE vs VIMOV FEMALE) |
| 24 | `20260625204358_temp_BN.json` | P18 | PATIENT | 2026-06-25 20:42:52 | **SÍ** | `SMR_20260625_P18_BN_1f325d38_raw.json` | TUG confirmado: género idéntico y $\Delta t = 81.0$ s |
| 25 | `20260625212453_temp_G.json` | P19 | PATIENT | 2026-06-25 21:23:38 | **NO (DESCARTADO)** | - | Descartado por discrepancia de género (IMU MALE vs VIMOV FEMALE) |
| 26 | `20260625214451_temp_BH.json` | P20 | PATIENT | 2026-06-25 20:13:35 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |
| 27 | `20260625214518_temp_S.json` | P20 | PATIENT | 2026-06-25 20:16:06 | **SÍ** | `SMR_20260625_P20_S_dde1028c_raw.json` | TUG confirmado: género idéntico y $\Delta t = 106.0$ s |
| 28 | `20260625215046_temp_X.json` | P21 | PATIENT | 2026-06-25 21:49:31 | **SÍ** | `SMR_20260625_P21_X_28ac951e_raw.json` | TUG confirmado: género idéntico y $\Delta t = 84.0$ s |
| 29 | `20260626133915_temp_BA.json` | P22 | PATIENT | 2026-06-25 22:55:59 | **SÍ** | `SMR_20260625_P22_BA_a22ff952_raw.json` | TUG confirmado: género idéntico y $\Delta t = 77.0$ s |
| 30 | `20260626133916_temp_BA.json` | P22 | PATIENT | 2026-06-25 22:55:59 | **SÍ (DUPLICADO)** | `SMR_20260625_P22_BA_a22ff952_raw.json` | TUG confirmado: género idéntico y $\Delta t = 77.0$ s |
| 31 | `20260626141246_temp_AC.json` | P23 | PATIENT | 2026-06-26 14:11:42 | **NO (DESCARTADO)** | - | Descartado por discrepancia de género (IMU FEMALE vs VIMOV MALE) |
| 32 | `20260626144433_temp_AV.json` | P24 | PATIENT | 2026-06-26 14:43:00 | **SÍ** | `SMR_20260626_P24_AV_fc8711e0_raw.json` | TUG confirmado: género idéntico y $\Delta t = 196.0$ s |
| 33 | `20260626145512_temp_AO.json` | P25 | PATIENT | 2026-06-26 14:53:43 | **SÍ** | `SMR_20260626_P25_AO_ce5691b9_raw.json` | TUG confirmado: género idéntico y $\Delta t = 282.0$ s |
| 34 | `20260626150532_temp_M.json` | P26 | PATIENT | 2026-06-26 15:03:48 | **SÍ** | `SMR_20260626_P26_M_0ec82be7_raw.json` | TUG confirmado: género idéntico y $\Delta t = 170.0$ s |
| 35 | `20260626151711_temp_BQ.json` | P27 | PATIENT | 2026-06-26 15:15:48 | **SÍ** | `SMR_20260626_P27_BQ_156f5309_raw.json` | TUG confirmado: género idéntico y $\Delta t = 91.0$ s |
| 36 | `20260626152553_temp_U.json` | P28 | PATIENT | 2026-06-26 15:25:04 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |
| 37 | `20260626153637_temp_AJ.json` | P29 | PATIENT | 2026-06-26 15:35:39 | **NO (DESCARTADO)** | - | Descartado por discrepancia de género (IMU FEMALE vs VIMOV MALE) |
| 38 | `20260626154758_temp_O.json` | P30 | PATIENT | 2026-06-26 15:46:43 | **SÍ** | `SMR_20260626_P30_O_5432070f_raw.json` | TUG confirmado: género idéntico y $\Delta t = 290.0$ s |
| 39 | `20260626160554_temp_BU.json` | P31 | PATIENT | 2026-06-26 16:04:24 | **SÍ** | `SMR_20260626_P31_BU_f89f97d0_raw.json` | TUG confirmado: género idéntico y $\Delta t = 162.0$ s |
| 40 | `20260626160620_temp_K.json` | P31 | PATIENT | 2026-06-26 16:05:55 | **SÍ** | `SMR_20260626_P31_K_4e5316e1_raw.json` | TUG confirmado: género idéntico y $\Delta t = 78.0$ s |
| 41 | `20260626170623_temp_BT.json` | P32 | PATIENT | 2026-06-26 17:04:37 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |
| 42 | `20260626170733_temp_AZ.json` | P32 | PATIENT | 2026-06-26 17:06:53 | **SÍ** | `SMR_20260626_P32_AZ_fbe58f01_raw.json` | TUG confirmado: género idéntico y $\Delta t = 260.0$ s |
| 43 | `20260626170919_temp_J.json` | P32 | PATIENT | 2026-06-26 17:08:58 | **SÍ** | `SMR_20260626_P32_J_dabe0112_raw.json` | TUG confirmado: género idéntico y $\Delta t = 141.0$ s |
| 44 | `20260626170956_temp_AQ.json` | P32 | PATIENT | 2026-06-26 17:09:37 | **SÍ** | `SMR_20260626_P32_AQ_22f0ff21_raw.json` | TUG confirmado: género idéntico y $\Delta t = 109.0$ s |
| 45 | `20260626194407_temp_BM.json` | P33 | PATIENT | 2026-06-26 19:43:07 | **SÍ** | `SMR_20260626_P33_BM_ed61ac9f_raw.json` | TUG confirmado: género idéntico y $\Delta t = 108.0$ s |
| 46 | `20260626202515_temp_BS.json` | P34 | PATIENT | 2026-06-26 20:22:35 | **SÍ** | `SMR_20260626_P34_BS_87a49c65_raw.json` | TUG confirmado: género idéntico y $\Delta t = 163.0$ s |
| 47 | `20260626204728_temp_AW.json` | P35 | PATIENT | 2026-06-26 20:46:42 | **SÍ** | `SMR_20260626_P35_AW_452eaaa1_raw.json` | TUG confirmado: género idéntico y $\Delta t = 62.0$ s |
| 48 | `20260626211937_temp_AH.json` | P36 | PATIENT | 2026-06-26 21:18:37 | **SÍ** | `SMR_20260626_P36_AH_b622b020_raw.json` | TUG confirmado: género idéntico y $\Delta t = 129.0$ s |
| 49 | `20260626213214_temp_AT.json` | P37 | PATIENT | 2026-06-26 21:31:18 | **SÍ** | `SMR_20260626_P37_AT_0dcde044_raw.json` | TUG confirmado: género idéntico y $\Delta t = 265.0$ s |
| 50 | `20260626215053_temp_AE.json` | P38 | PATIENT | 2026-06-26 21:49:58 | **SÍ** | `SMR_20260626_P38_AE_80c945b3_raw.json` | TUG confirmado: género idéntico y $\Delta t = 188.0$ s |
| 51 | `20260626222007_temp_BL.json` | P39 | PATIENT | 2026-06-26 22:18:47 | **SÍ** | `SMR_20260626_P39_BL_294c3933_raw.json` | TUG confirmado: género idéntico y $\Delta t = 89.0$ s |
| 52 | `20260627133637_temp_AS.json` | P40 | PATIENT | 2026-06-27 13:35:40 | **SÍ** | `SMR_20260627_P40_AS_4df833f1_raw.json` | TUG confirmado: género idéntico y $\Delta t = 80.0$ s |
| 53 | `20260627135010_temp_BP.json` | P41 | PATIENT | 2026-06-27 13:47:37 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |
| 54 | `20260627135720_temp_AD.json` | P42 | PATIENT | 2026-06-27 13:55:54 | **SÍ** | `SMR_20260627_P42_AD_25f298d4_raw.json` | TUG confirmado: género idéntico y $\Delta t = 174.0$ s |
| 55 | `20260627143518_temp_BB.json` | P43 | PATIENT | 2026-06-27 14:34:21 | **SÍ** | `SMR_20260627_P43_BB_580b902a_raw.json` | TUG confirmado: género idéntico y $\Delta t = 83.0$ s |
| 56 | `20260627150939_temp_R.json` | P44 | PATIENT | 2026-06-27 15:08:47 | **SÍ** | `SMR_20260627_P44_R_89d757d6_raw.json` | TUG confirmado: género idéntico y $\Delta t = 114.0$ s |
| 57 | `20260627152358_temp_W.json` | P45 | PATIENT | 2026-06-27 15:23:02 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |
| 58 | `20260627155804_temp_I.json` | P46 | PATIENT | 2026-06-27 15:57:15 | **SÍ** | `SMR_20260627_P46_I_ba2c6e63_raw.json` | TUG confirmado: género idéntico y $\Delta t = 57.0$ s |
| 59 | `20260627161148_temp_Q.json` | P47 | PATIENT | 2026-06-27 16:10:39 | **SÍ** | `SMR_20260627_P47_Q_907121bd_raw.json` | TUG confirmado: género idéntico y $\Delta t = 249.0$ s |
| 60 | `20260627162118_temp_AU.json` | P48 | PATIENT | 2026-06-27 16:19:41 | **SÍ** | `SMR_20260627_P48_AU_4781f6d7_raw.json` | TUG confirmado: género idéntico y $\Delta t = 167.0$ s |
| 61 | `20260627163836_temp_L.json` | P49 | PATIENT | 2026-06-27 16:37:29 | **SÍ** | `SMR_20260627_P49_L_6943624b_raw.json` | TUG confirmado: género idéntico y $\Delta t = 299.0$ s |
| 62 | `20260627171353_temp_H.json` | P50 | PATIENT | 2026-06-27 17:13:05 | **SÍ** | `SMR_20260627_P50_H_d3efbdfa_raw.json` | TUG confirmado: género idéntico y $\Delta t = 58.0$ s |
| 63 | `20260627180847_temp_AI.json` | P51 | PATIENT | 2026-06-27 18:06:45 | **SÍ** | `SMR_20260627_P51_AI_18c58989_raw.json` | TUG confirmado: género idéntico y $\Delta t = 124.0$ s |
| 64 | `20260627205326_temp_C.json` | P52 | PATIENT | 2026-06-27 20:52:35 | **SÍ** | `SMR_20260627_P52_C_029c450a_raw.json` | TUG confirmado: género idéntico y $\Delta t = 65.0$ s |
| 65 | `20260704154505_temp_AF.json` | P53 | PATIENT | 2026-07-04 15:44:08 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |
| 66 | `20260704155929_temp_BE.json` | P54 | PATIENT | 2026-07-04 15:58:15 | **SÍ** | `CST_20260704_P54_BE_c1b8493f_raw.json` | TUG confirmado: género idéntico y $\Delta t = 16.0$ s |
| 67 | `20260704165749_temp_E.json` | P55 | PATIENT | 2026-07-04 16:56:59 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |
| 68 | `20260704172020_temp_Y.json` | P56 | PATIENT | 2026-07-04 17:19:11 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |
| 69 | `20260704194015_temp_AY.json` | P57 | CONTROL | 2026-07-04 19:00:00 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |
| 70 | `20260704194635_temp_BG.json` | P58 | PATIENT | 2026-07-04 19:44:43 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |
| 71 | `20260715052203_temp_B.json` | P59 | CONTROL | 2026-07-04 14:50:22 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |
| 72 | `20260820141830_temp_AM.json` | P60 | PATIENT | 2026-07-04 15:50:31 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |
| 73 | `20260820141849_temp_P.json` | P61 | CONTROL | 2026-07-04 16:14:25 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |
| 74 | `20260820141919_temp_BI.json` | P62 | PATIENT | 2026-07-04 16:50:45 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |
| 75 | `20260820142005_temp_Z.json` | P63 | PATIENT | 2026-07-04 17:49:13 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |
| 76 | `20260820142006_temp_Z.json` | P63 | PATIENT | 2026-07-04 17:49:13 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |
| 77 | `20260820142037_temp_T.json` | P64 | CONTROL | 2026-07-04 18:08:52 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |
| 78 | `20260820142101_temp_AN.json` | P65 | CONTROL | 2026-07-04 18:49:43 | **NO** | - | Sin captura TUG de cámara en esta ventana horaria (evaluado en marcha continua o solo IMU) |

---

## 5. Inventario General de la Brigada Santa Marta TUG (103 Archivos e-Motion)

De la brigada de Santa Marta (25, 26 y 27 de junio de 2026), se conservan en la carpeta principal **103 grabaciones que corresponden estrictamente al protocolo Timed Up and Go (TUG)**:

- **40 grabaciones** cuentan con par IMU confirmado bajo estricta correspondencia demográfica y temporal (`SMR_YYYYMMDD_Pxx_COD_hash_raw.json`).
- **63 grabaciones** corresponden a pruebas TUG de visión independientes (`SMR_YYYYMMDD_NO_IMU_hash_raw.json`).
- Todas las grabaciones se encuentran 100% anonimizadas, sin nombres ni cédulas, listas para análisis de longitud de zancada y velocidad lineal en marcha recta.
- Las 137 grabaciones de caminata continua (`Gait Analysis` y `GAIT_COMPLETE`) se encuentran preservadas en `Datos e-Motion/No_TUG_Gait_Analysis/`.
