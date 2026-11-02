# Correspondencia y Trazabilidad: Sensores IMU vs. Sistema de Cámaras e-Motion (VIMOV)

> **Propósito:** Responder al requerimiento del profesor Domiciano Rincón de auditar las fechas de los 78 archivos de datos IMU y contrastarlas con las grabaciones del sistema e-Motion / VIMOV para determinar con exactitud quiénes cuentan con su versión de cámara y quiénes no.
> **Fecha de actualización:** 02 de noviembre de 2026
> **Filtro Estricto de Protocolo TUG y Género:** Para garantizar total validez científica y bioestadística:
> 1. **Protocolo Estricto:** Se auditan y conservan **exclusivamente grabaciones con protocolo TUG (`TIMED_UP_AND_GO` / `Timed up and Go`)**, segregando las pruebas de marcha continua (`Gait Analysis` y `GAIT_COMPLETE`) que formaban parte de otros protocolos clínicos de la brigada.
> 2. **Regla Estricta de Género:** Si el género de la persona no coincide entre el IMU y VIMOV, el par se clasifica formalmente como descarte estricto por no corresponder al mismo sujeto.

---

## 1. Resumen Ejecutivo del Cruce Bimodal Estrictamente TUG

| Métrica Metodológica | Valor | Observación y Fundamento |
|:---|---:|:---|
| **Total grabaciones IMU en dataset** | **78** | Totalidad de archivos `.json` en `Datos IMUs/` |
| **Pruebas piloto previas a brigadas** | **9** | Febrero a mediados de junio 2026 (P01 a P05, sin cámara en sitio) |
| **Total grabaciones ejecutadas en brigadas** | **69** | Santa Marta (25–27 junio) y CST / La Victoria (04 julio) |
| **Pares Bimodales Estrictamente TUG Confirmados** | **42** | Protocolo TUG confirmado en ambos dispositivos y género 100% coincidente |
| **Ensayos IMU descartados por discrepancia de género** | **5** | Cámara evaluaba paciente del sexo opuesto en ventana horaria cercana |
| **Ensayos IMU en brigada sin par TUG en cámara** | **22** | Evaluados exclusivamente con IMU o en protocolo de caminata libre |
| **Total Grabaciones e-Motion TUG (`Datos e-Motion/`)** | **132** | 103 de Santa Marta (`SMR_`) + 6 de CST (`CST_`) + 23 de Lab (`LAB_`) |
| **Grabaciones de Marcha Segregadas (`No_TUG_Gait_Analysis/`)** | **137** | 122 Santa Marta + 14 CST + 1 Lab (135 esqueléticas + 2 métricas) |

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

| # | Archivo IMU | Sujeto | Código | Archivo e-Motion Confirmado (en disco) | Delta t (s) | Género | Clase | Sensor Cámara | Duración e-Motion |
|---:|---|:---:|:---:|---|---:|:---:|:---:|---|:---:|
| 1 | `20260625140746_temp_BF.json` | P06 | BF | `SMR_20260625_P06_BF_4cd523b7_raw.json` | +122.0 s | MALE | PATIENT | Intel Intel RealSens | 21.94 s |
| 2 | `20260625144044_temp_D.json` | P07 | D | `SMR_20260625_P07_D_c71c489e_raw.json` | +164.0 s | MALE | PATIENT | Intel Intel RealSens | 25.05 s |
| 3 | `20260625145018_temp_AB.json` | P08 | AB | `SMR_20260625_P08_AB_ff5603a4_raw.json` | +302.0 s | MALE | PATIENT | Intel Intel RealSens | 18.14 s |
| 4 | `20260625150353_temp_AK.json` | P09 | AK | `SMR_20260625_P09_AK_2adb11ee_raw.json` | +323.0 s | MALE | PATIENT | Intel Intel RealSens | 24.37 s |
| 5 | `20260625152019_temp_AA.json` | P10 | AA | `SMR_20260625_P10_AA_bf709abb_raw.json` | +151.0 s | MALE | PATIENT | Intel Intel RealSens | 13.63 s |
| 6 | `20260625153756_temp_V.json` | P11 | V | `SMR_20260625_P11_V_7ed2f2de_raw.json` | +77.0 s | MALE | PATIENT | Intel Intel RealSens | 15.24 s |
| 7 | `20260625171352_temp_BW.json` | P13 | BW | `SMR_20260625_P13_BW_5eeb5a37_raw.json` | +127.0 s | MALE | PATIENT | Intel Intel RealSens | 17.57 s |
| 8 | `20260625183434_temp_BK.json` | P15 | BK | `SMR_20260625_P15_BK_b8317644_raw.json` | +103.0 s | MALE | PATIENT | Intel Intel RealSens | 10.94 s |
| 9 | `20260625193811_temp_BD.json` | P16 | BD | `SMR_20260625_P16_BD_f16693f6_raw.json` | +70.0 s | MALE | PATIENT | Intel Intel RealSens | 16.5 s |
| 10 | `20260625204358_temp_BN.json` | P18 | BN | `SMR_20260625_P18_BN_1f325d38_raw.json` | +81.0 s | MALE | PATIENT | Intel Intel RealSens | 16.71 s |
| 11 | `20260625214518_temp_S.json` | P20 | S | `SMR_20260625_P20_S_dde1028c_raw.json` | 0.0 s | M | PATIENT | Intel Intel RealSens | 56.87 s |
| 12 | `20260625215046_temp_X.json` | P21 | X | `SMR_20260625_P21_X_28ac951e_raw.json` | +84.0 s | MALE | PATIENT | Intel Intel RealSens | 21.77 s |
| 13 | `20260626133916_temp_BA.json` | P22 | BA | `SMR_20260625_P22_BA_a22ff952_raw.json` | +77.0 s | MALE | PATIENT | Intel Intel RealSens | 12.5 s |
| 14 | `20260626144433_temp_AV.json` | P24 | AV | `SMR_20260626_P24_AV_fc8711e0_raw.json` | +196.0 s | MALE | PATIENT | Intel Intel RealSens | 25.8 s |
| 15 | `20260626145512_temp_AO.json` | P25 | AO | `SMR_20260626_P25_AO_ce5691b9_raw.json` | +282.0 s | MALE | PATIENT | Intel Intel RealSens | 21.67 s |
| 16 | `20260626150532_temp_M.json` | P26 | M | `SMR_20260626_P26_M_0ec82be7_raw.json` | +170.0 s | MALE | PATIENT | Intel Intel RealSens | 33.97 s |
| 17 | `20260626151711_temp_BQ.json` | P27 | BQ | `SMR_20260626_P27_BQ_156f5309_raw.json` | +91.0 s | MALE | PATIENT | Intel Intel RealSens | 20.57 s |
| 18 | `20260626154758_temp_O.json` | P30 | O | `SMR_20260626_P30_O_5432070f_raw.json` | +290.0 s | MALE | PATIENT | Intel Intel RealSens | 17.73 s |
| 19 | `20260626160554_temp_BU.json` | P31 | BU | `SMR_20260626_P31_BU_f89f97d0_raw.json` | +162.0 s | MALE | PATIENT | Intel Intel RealSens | 17.67 s |
| 20 | `20260626160620_temp_K.json` | P31 | K | `SMR_20260626_P31_K_4e5316e1_raw.json` | +78.0 s | MALE | PATIENT | Intel Intel RealSens | 16.27 s |
| 21 | `20260626170733_temp_AZ.json` | P32 | AZ | `SMR_20260626_P32_AZ_fbe58f01_raw.json` | +260.0 s | MALE | PATIENT | Intel Intel RealSens | 18.93 s |
| 22 | `20260626170919_temp_J.json` | P32 | J | `SMR_20260626_P32_J_dabe0112_raw.json` | +141.0 s | MALE | PATIENT | Intel Intel RealSens | 13.83 s |
| 23 | `20260626170956_temp_AQ.json` | P32 | AQ | `SMR_20260626_P32_AQ_22f0ff21_raw.json` | +109.0 s | MALE | PATIENT | Intel Intel RealSens | 13.86 s |
| 24 | `20260626194407_temp_BM.json` | P33 | BM | `SMR_20260626_P33_BM_ed61ac9f_raw.json` | +108.0 s | MALE | PATIENT | Intel Intel RealSens | 17.61 s |
| 25 | `20260626202515_temp_BS.json` | P34 | BS | `SMR_20260626_P34_BS_87a49c65_raw.json` | +163.0 s | MALE | PATIENT | Intel Intel RealSens | 24.21 s |
| 26 | `20260626204728_temp_AW.json` | P35 | AW | `SMR_20260626_P35_AW_452eaaa1_raw.json` | +62.0 s | MALE | PATIENT | Intel Intel RealSens | 28.55 s |
| 27 | `20260626211937_temp_AH.json` | P36 | AH | `SMR_20260626_P36_AH_b622b020_raw.json` | +129.0 s | MALE | PATIENT | Intel Intel RealSens | 16.6 s |
| 28 | `20260626213214_temp_AT.json` | P37 | AT | `SMR_20260626_P37_AT_0dcde044_raw.json` | +265.0 s | MALE | PATIENT | Intel Intel RealSens | 14.9 s |
| 29 | `20260626215053_temp_AE.json` | P38 | AE | `SMR_20260626_P38_AE_80c945b3_raw.json` | +188.0 s | MALE | PATIENT | Intel Intel RealSens | 13.8 s |
| 30 | `20260626222007_temp_BL.json` | P39 | BL | `SMR_20260626_P39_BL_294c3933_raw.json` | +89.0 s | MALE | PATIENT | Intel Intel RealSens | 16.2 s |
| 31 | `20260627133637_temp_AS.json` | P40 | AS | `SMR_20260627_P40_AS_4df833f1_raw.json` | +80.0 s | MALE | PATIENT | Intel Intel RealSens | 15.14 s |
| 32 | `20260627135720_temp_AD.json` | P42 | AD | `SMR_20260627_P42_AD_25f298d4_raw.json` | +174.0 s | MALE | PATIENT | Intel Intel RealSens | 21.47 s |
| 33 | `20260627143518_temp_BB.json` | P43 | BB | `SMR_20260627_P43_BB_580b902a_raw.json` | +83.0 s | MALE | PATIENT | Intel Intel RealSens | 14.37 s |
| 34 | `20260627150939_temp_R.json` | P44 | R | `SMR_20260627_P44_R_89d757d6_raw.json` | +114.0 s | MALE | PATIENT | Intel Intel RealSens | 15.7 s |
| 35 | `20260627155804_temp_I.json` | P46 | I | `SMR_20260627_P46_I_ba2c6e63_raw.json` | +57.0 s | MALE | PATIENT | Intel Intel RealSens | 12.47 s |
| 36 | `20260627161148_temp_Q.json` | P47 | Q | `SMR_20260627_P47_Q_907121bd_raw.json` | +249.0 s | MALE | PATIENT | Intel Intel RealSens | 13.7 s |
| 37 | `20260627162118_temp_AU.json` | P48 | AU | `SMR_20260627_P48_AU_4781f6d7_raw.json` | +167.0 s | MALE | PATIENT | Intel Intel RealSens | 12.63 s |
| 38 | `20260627163836_temp_L.json` | P49 | L | `SMR_20260627_P49_L_6943624b_raw.json` | +299.0 s | MALE | PATIENT | Intel Intel RealSens | 18.77 s |
| 39 | `20260627171353_temp_H.json` | P50 | H | `SMR_20260627_P50_H_d3efbdfa_raw.json` | +58.0 s | MALE | PATIENT | Intel Intel RealSens | 13.17 s |
| 40 | `20260627180847_temp_AI.json` | P51 | AI | `SMR_20260627_P51_AI_18c58989_raw.json` | +124.0 s | MALE | PATIENT | Intel Intel RealSens | 19.53 s |
| 41 | `20260627205326_temp_C.json` | P52 | C | `SMR_20260627_P52_C_029c450a_raw.json` | +65.0 s | MALE | PATIENT | Intel Intel RealSens | 14.97 s |
| 42 | `20260704155929_temp_BE.json` | P54 | BE | `CST_20260704_P54_BE_c1b8493f_raw.json` | +16.0 s | MALE | PATIENT | Orbbec Orbbec Astra  | 15.47 s |

---

## 4. Cuadro de Auditoría Completa de los 78 Registros IMU

A continuación se audita el estado de cada una de las 78 grabaciones inerciales del dataset frente al sistema de cámaras e-Motion estrictamente TUG:

| # | Archivo IMU | Sujeto | Grupo | Fecha UTC | ¿Tiene e-Motion TUG? | Archivo e-Motion Asignado | Observación / Criterio |
|---:|---|:---:|:---:|:---:|:---:|---|---|
| 1 | `20260208022404_temp_BV.json` | - | SIN_ETIQUETA | 2026-02-08 02:24:04 | **NO** | - | Prueba piloto previa a brigadas (sin cámara en sitio) |
| 2 | `20260303043120_temp_N.json` | - | SIN_ETIQUETA | 2026-03-03 04:31:20 | **NO** | - | Prueba piloto previa a brigadas (sin cámara en sitio) |
| 3 | `20260303043532_temp_BO.json` | - | SIN_ETIQUETA | 2026-03-03 04:35:32 | **NO** | - | Prueba piloto previa a brigadas (sin cámara en sitio) |
| 4 | `20260303044505_temp_BX.json` | - | SIN_ETIQUETA | 2026-03-03 04:45:05 | **NO** | - | Prueba piloto previa a brigadas (sin cámara en sitio) |
| 5 | `20260303134630_temp_BJ.json` | - | SIN_ETIQUETA | 2026-03-03 13:46:30 | **NO** | - | Prueba piloto previa a brigadas (sin cámara en sitio) |
| 6 | `20260307234249_temp_F.json` | - | SIN_ETIQUETA | 2026-03-07 23:42:49 | **NO** | - | Prueba piloto previa a brigadas (sin cámara en sitio) |
| 7 | `20260308232420_temp_AX.json` | - | SIN_ETIQUETA | 2026-03-08 23:24:20 | **NO** | - | Prueba piloto previa a brigadas (sin cámara en sitio) |
| 8 | `20260611235032_temp_AL.json` | - | SIN_ETIQUETA | 2026-06-11 23:50:32 | **NO** | - | Prueba piloto previa a brigadas (sin cámara en sitio) |
| 9 | `20260618075259_temp_BC.json` | - | SIN_ETIQUETA | 2026-06-18 07:52:59 | **NO** | - | Prueba piloto previa a brigadas (sin cámara en sitio) |
| 10 | `20260625140746_temp_BF.json` | - | SIN_ETIQUETA | 2026-06-25 14:07:46 | **SÍ** | `SMR_20260625_P06_BF_4cd523b7_raw.json` | Bimodal TUG validado (21.94 s) |
| 11 | `20260625140851_temp_AR.json` | - | SIN_ETIQUETA | 2026-06-25 14:08:51 | **NO** | - | Sin captura TUG en cámara (evaluado solo con IMU o en marcha pura) |
| 12 | `20260625144044_temp_D.json` | - | SIN_ETIQUETA | 2026-06-25 14:40:44 | **SÍ** | `SMR_20260625_P07_D_c71c489e_raw.json` | Bimodal TUG validado (25.05 s) |
| 13 | `20260625145018_temp_AB.json` | - | SIN_ETIQUETA | 2026-06-25 14:50:18 | **SÍ** | `SMR_20260625_P08_AB_ff5603a4_raw.json` | Bimodal TUG validado (18.14 s) |
| 14 | `20260625150353_temp_AK.json` | - | SIN_ETIQUETA | 2026-06-25 15:03:53 | **SÍ** | `SMR_20260625_P09_AK_2adb11ee_raw.json` | Bimodal TUG validado (24.37 s) |
| 15 | `20260625152019_temp_AA.json` | - | SIN_ETIQUETA | 2026-06-25 15:20:19 | **SÍ** | `SMR_20260625_P10_AA_bf709abb_raw.json` | Bimodal TUG validado (13.63 s) |
| 16 | `20260625153756_temp_V.json` | - | SIN_ETIQUETA | 2026-06-25 15:37:56 | **SÍ** | `SMR_20260625_P11_V_7ed2f2de_raw.json` | Bimodal TUG validado (15.24 s) |
| 17 | `20260625164351_temp_A.json` | - | SIN_ETIQUETA | 2026-06-25 16:43:51 | **NO** | - | Sin captura TUG en cámara (evaluado solo con IMU o en marcha pura) |
| 18 | `20260625171352_temp_BW.json` | - | SIN_ETIQUETA | 2026-06-25 17:13:52 | **SÍ** | `SMR_20260625_P13_BW_5eeb5a37_raw.json` | Bimodal TUG validado (17.57 s) |
| 19 | `20260625180613_temp_AG.json` | - | SIN_ETIQUETA | 2026-06-25 18:06:13 | **NO** | - | Sin captura TUG en cámara (evaluado solo con IMU o en marcha pura) |
| 20 | `20260625183434_temp_BK.json` | - | SIN_ETIQUETA | 2026-06-25 18:34:34 | **SÍ** | `SMR_20260625_P15_BK_b8317644_raw.json` | Bimodal TUG validado (10.94 s) |
| 21 | `20260625193811_temp_BD.json` | - | SIN_ETIQUETA | 2026-06-25 19:38:11 | **SÍ** | `SMR_20260625_P16_BD_f16693f6_raw.json` | Bimodal TUG validado (16.5 s) |
| 22 | `20260625195406_temp_BR.json` | - | SIN_ETIQUETA | 2026-06-25 19:54:06 | **NO (DESCARTADO)** | - | Descarte estricto por discrepancia de género (IMU vs Cámara) |
| 23 | `20260625195426_temp_AP.json` | - | SIN_ETIQUETA | 2026-06-25 19:54:26 | **NO (DESCARTADO)** | - | Descarte estricto por discrepancia de género (IMU vs Cámara) |
| 24 | `20260625204358_temp_BN.json` | - | SIN_ETIQUETA | 2026-06-25 20:43:58 | **SÍ** | `SMR_20260625_P18_BN_1f325d38_raw.json` | Bimodal TUG validado (16.71 s) |
| 25 | `20260625212453_temp_G.json` | - | SIN_ETIQUETA | 2026-06-25 21:24:53 | **NO (DESCARTADO)** | - | Descarte estricto por discrepancia de género (IMU vs Cámara) |
| 26 | `20260625214451_temp_BH.json` | - | SIN_ETIQUETA | 2026-06-25 21:44:51 | **NO** | - | Sin captura TUG en cámara (evaluado solo con IMU o en marcha pura) |
| 27 | `20260625214518_temp_S.json` | - | SIN_ETIQUETA | 2026-06-25 21:45:18 | **SÍ** | `SMR_20260625_P20_S_dde1028c_raw.json` | Bimodal TUG validado (56.87 s) |
| 28 | `20260625215046_temp_X.json` | - | SIN_ETIQUETA | 2026-06-25 21:50:46 | **SÍ** | `SMR_20260625_P21_X_28ac951e_raw.json` | Bimodal TUG validado (21.77 s) |
| 29 | `20260626133915_temp_BA.json` | - | SIN_ETIQUETA | 2026-06-26 13:39:15 | **NO** | - | Sin captura TUG en cámara (evaluado solo con IMU o en marcha pura) |
| 30 | `20260626133916_temp_BA.json` | - | SIN_ETIQUETA | 2026-06-26 13:39:16 | **SÍ** | `SMR_20260625_P22_BA_a22ff952_raw.json` | Bimodal TUG validado (12.5 s) |
| 31 | `20260626141246_temp_AC.json` | - | SIN_ETIQUETA | 2026-06-26 14:12:46 | **NO (DESCARTADO)** | - | Descarte estricto por discrepancia de género (IMU vs Cámara) |
| 32 | `20260626144433_temp_AV.json` | - | SIN_ETIQUETA | 2026-06-26 14:44:33 | **SÍ** | `SMR_20260626_P24_AV_fc8711e0_raw.json` | Bimodal TUG validado (25.8 s) |
| 33 | `20260626145512_temp_AO.json` | - | SIN_ETIQUETA | 2026-06-26 14:55:12 | **SÍ** | `SMR_20260626_P25_AO_ce5691b9_raw.json` | Bimodal TUG validado (21.67 s) |
| 34 | `20260626150532_temp_M.json` | - | SIN_ETIQUETA | 2026-06-26 15:05:32 | **SÍ** | `SMR_20260626_P26_M_0ec82be7_raw.json` | Bimodal TUG validado (33.97 s) |
| 35 | `20260626151711_temp_BQ.json` | - | SIN_ETIQUETA | 2026-06-26 15:17:11 | **SÍ** | `SMR_20260626_P27_BQ_156f5309_raw.json` | Bimodal TUG validado (20.57 s) |
| 36 | `20260626152553_temp_U.json` | - | SIN_ETIQUETA | 2026-06-26 15:25:53 | **NO** | - | Sin captura TUG en cámara (evaluado solo con IMU o en marcha pura) |
| 37 | `20260626153637_temp_AJ.json` | - | SIN_ETIQUETA | 2026-06-26 15:36:37 | **NO (DESCARTADO)** | - | Descarte estricto por discrepancia de género (IMU vs Cámara) |
| 38 | `20260626154758_temp_O.json` | - | SIN_ETIQUETA | 2026-06-26 15:47:58 | **SÍ** | `SMR_20260626_P30_O_5432070f_raw.json` | Bimodal TUG validado (17.73 s) |
| 39 | `20260626160554_temp_BU.json` | - | SIN_ETIQUETA | 2026-06-26 16:05:54 | **SÍ** | `SMR_20260626_P31_BU_f89f97d0_raw.json` | Bimodal TUG validado (17.67 s) |
| 40 | `20260626160620_temp_K.json` | - | SIN_ETIQUETA | 2026-06-26 16:06:20 | **SÍ** | `SMR_20260626_P31_K_4e5316e1_raw.json` | Bimodal TUG validado (16.27 s) |
| 41 | `20260626170623_temp_BT.json` | - | SIN_ETIQUETA | 2026-06-26 17:06:23 | **NO** | - | Sin captura TUG en cámara (evaluado solo con IMU o en marcha pura) |
| 42 | `20260626170733_temp_AZ.json` | - | SIN_ETIQUETA | 2026-06-26 17:07:33 | **SÍ** | `SMR_20260626_P32_AZ_fbe58f01_raw.json` | Bimodal TUG validado (18.93 s) |
| 43 | `20260626170919_temp_J.json` | - | SIN_ETIQUETA | 2026-06-26 17:09:19 | **SÍ** | `SMR_20260626_P32_J_dabe0112_raw.json` | Bimodal TUG validado (13.83 s) |
| 44 | `20260626170956_temp_AQ.json` | - | SIN_ETIQUETA | 2026-06-26 17:09:56 | **SÍ** | `SMR_20260626_P32_AQ_22f0ff21_raw.json` | Bimodal TUG validado (13.86 s) |
| 45 | `20260626194407_temp_BM.json` | - | SIN_ETIQUETA | 2026-06-26 19:44:07 | **SÍ** | `SMR_20260626_P33_BM_ed61ac9f_raw.json` | Bimodal TUG validado (17.61 s) |
| 46 | `20260626202515_temp_BS.json` | - | SIN_ETIQUETA | 2026-06-26 20:25:15 | **SÍ** | `SMR_20260626_P34_BS_87a49c65_raw.json` | Bimodal TUG validado (24.21 s) |
| 47 | `20260626204728_temp_AW.json` | - | SIN_ETIQUETA | 2026-06-26 20:47:28 | **SÍ** | `SMR_20260626_P35_AW_452eaaa1_raw.json` | Bimodal TUG validado (28.55 s) |
| 48 | `20260626211937_temp_AH.json` | - | SIN_ETIQUETA | 2026-06-26 21:19:37 | **SÍ** | `SMR_20260626_P36_AH_b622b020_raw.json` | Bimodal TUG validado (16.6 s) |
| 49 | `20260626213214_temp_AT.json` | - | SIN_ETIQUETA | 2026-06-26 21:32:14 | **SÍ** | `SMR_20260626_P37_AT_0dcde044_raw.json` | Bimodal TUG validado (14.9 s) |
| 50 | `20260626215053_temp_AE.json` | - | SIN_ETIQUETA | 2026-06-26 21:50:53 | **SÍ** | `SMR_20260626_P38_AE_80c945b3_raw.json` | Bimodal TUG validado (13.8 s) |
| 51 | `20260626222007_temp_BL.json` | - | SIN_ETIQUETA | 2026-06-26 22:20:07 | **SÍ** | `SMR_20260626_P39_BL_294c3933_raw.json` | Bimodal TUG validado (16.2 s) |
| 52 | `20260627133637_temp_AS.json` | - | SIN_ETIQUETA | 2026-06-27 13:36:37 | **SÍ** | `SMR_20260627_P40_AS_4df833f1_raw.json` | Bimodal TUG validado (15.14 s) |
| 53 | `20260627135010_temp_BP.json` | - | SIN_ETIQUETA | 2026-06-27 13:50:10 | **NO** | - | Sin captura TUG en cámara (evaluado solo con IMU o en marcha pura) |
| 54 | `20260627135720_temp_AD.json` | - | SIN_ETIQUETA | 2026-06-27 13:57:20 | **SÍ** | `SMR_20260627_P42_AD_25f298d4_raw.json` | Bimodal TUG validado (21.47 s) |
| 55 | `20260627143518_temp_BB.json` | - | SIN_ETIQUETA | 2026-06-27 14:35:18 | **SÍ** | `SMR_20260627_P43_BB_580b902a_raw.json` | Bimodal TUG validado (14.37 s) |
| 56 | `20260627150939_temp_R.json` | - | SIN_ETIQUETA | 2026-06-27 15:09:39 | **SÍ** | `SMR_20260627_P44_R_89d757d6_raw.json` | Bimodal TUG validado (15.7 s) |
| 57 | `20260627152358_temp_W.json` | - | SIN_ETIQUETA | 2026-06-27 15:23:58 | **NO** | - | Sin captura TUG en cámara (evaluado solo con IMU o en marcha pura) |
| 58 | `20260627155804_temp_I.json` | - | SIN_ETIQUETA | 2026-06-27 15:58:04 | **SÍ** | `SMR_20260627_P46_I_ba2c6e63_raw.json` | Bimodal TUG validado (12.47 s) |
| 59 | `20260627161148_temp_Q.json` | - | SIN_ETIQUETA | 2026-06-27 16:11:48 | **SÍ** | `SMR_20260627_P47_Q_907121bd_raw.json` | Bimodal TUG validado (13.7 s) |
| 60 | `20260627162118_temp_AU.json` | - | SIN_ETIQUETA | 2026-06-27 16:21:18 | **SÍ** | `SMR_20260627_P48_AU_4781f6d7_raw.json` | Bimodal TUG validado (12.63 s) |
| 61 | `20260627163836_temp_L.json` | - | SIN_ETIQUETA | 2026-06-27 16:38:36 | **SÍ** | `SMR_20260627_P49_L_6943624b_raw.json` | Bimodal TUG validado (18.77 s) |
| 62 | `20260627171353_temp_H.json` | - | SIN_ETIQUETA | 2026-06-27 17:13:53 | **SÍ** | `SMR_20260627_P50_H_d3efbdfa_raw.json` | Bimodal TUG validado (13.17 s) |
| 63 | `20260627180847_temp_AI.json` | - | SIN_ETIQUETA | 2026-06-27 18:08:47 | **SÍ** | `SMR_20260627_P51_AI_18c58989_raw.json` | Bimodal TUG validado (19.53 s) |
| 64 | `20260627205326_temp_C.json` | - | SIN_ETIQUETA | 2026-06-27 20:53:26 | **SÍ** | `SMR_20260627_P52_C_029c450a_raw.json` | Bimodal TUG validado (14.97 s) |
| 65 | `20260704154505_temp_AF.json` | - | SIN_ETIQUETA | 2026-07-04 15:45:05 | **NO** | - | Sin captura TUG en cámara (evaluado solo con IMU o en marcha pura) |
| 66 | `20260704155929_temp_BE.json` | - | SIN_ETIQUETA | 2026-07-04 15:59:29 | **SÍ** | `CST_20260704_P54_BE_c1b8493f_raw.json` | Bimodal TUG validado (15.47 s) |
| 67 | `20260704165749_temp_E.json` | - | SIN_ETIQUETA | 2026-07-04 16:57:49 | **NO** | - | Sin captura TUG en cámara (evaluado solo con IMU o en marcha pura) |
| 68 | `20260704172020_temp_Y.json` | - | SIN_ETIQUETA | 2026-07-04 17:20:20 | **NO** | - | Sin captura TUG en cámara (evaluado solo con IMU o en marcha pura) |
| 69 | `20260704194015_temp_AY.json` | - | SIN_ETIQUETA | 2026-07-04 19:40:15 | **NO** | - | Sin captura TUG en cámara (evaluado solo con IMU o en marcha pura) |
| 70 | `20260704194635_temp_BG.json` | - | SIN_ETIQUETA | 2026-07-04 19:46:35 | **NO** | - | Sin captura TUG en cámara (evaluado solo con IMU o en marcha pura) |
| 71 | `20260715052203_temp_B.json` | - | SIN_ETIQUETA | 2026-07-15 05:22:03 | **NO** | - | Sin captura TUG en cámara (evaluado solo con IMU o en marcha pura) |
| 72 | `20260820141830_temp_AM.json` | - | SIN_ETIQUETA | 2026-08-20 14:18:30 | **NO** | - | Sin captura TUG en cámara (evaluado solo con IMU o en marcha pura) |
| 73 | `20260820141849_temp_P.json` | - | SIN_ETIQUETA | 2026-08-20 14:18:49 | **NO** | - | Sin captura TUG en cámara (evaluado solo con IMU o en marcha pura) |
| 74 | `20260820141919_temp_BI.json` | - | SIN_ETIQUETA | 2026-08-20 14:19:19 | **NO** | - | Sin captura TUG en cámara (evaluado solo con IMU o en marcha pura) |
| 75 | `20260820142005_temp_Z.json` | - | SIN_ETIQUETA | 2026-08-20 14:20:05 | **NO** | - | Sin captura TUG en cámara (evaluado solo con IMU o en marcha pura) |
| 76 | `20260820142006_temp_Z.json` | - | SIN_ETIQUETA | 2026-08-20 14:20:06 | **NO** | - | Sin captura TUG en cámara (evaluado solo con IMU o en marcha pura) |
| 77 | `20260820142037_temp_T.json` | - | SIN_ETIQUETA | 2026-08-20 14:20:37 | **NO** | - | Sin captura TUG en cámara (evaluado solo con IMU o en marcha pura) |
| 78 | `20260820142101_temp_AN.json` | - | SIN_ETIQUETA | 2026-08-20 14:21:01 | **NO** | - | Sin captura TUG en cámara (evaluado solo con IMU o en marcha pura) |

