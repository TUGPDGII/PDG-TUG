# 📄 FICHA TÉCNICA OFICIAL DEL DATASET ÓPTICO (e-Motion / VIMOV) — PROYECTO TUG-V2
> **Documento Oficial de Auditoría y Control de Calidad**
> **Fecha de Consolidación:** Noviembre 2026
> **Metodología:** CRISP-DM (Fases de Data Understanding y Data Preparation)

---

## 1. Resumen Ejecutivo del Conjunto de Datos Ópticos

| Indicador | Valor Bruto Descargado | Valor Vigente en Disco | Observación y Respaldo Técnico |
|:---|:---:|:---:|---|
| **Total Grabaciones JSON** | **269** | **225** | **100% de archivos vigentes en el repositorio local** |
| **Protocolo TUG (`Datos e-Motion/TUG/`)** | 132 | **130** | 101 Santa Marta (`SMR`), 23 Laboratorio (`LAB`), 6 CST (`CST`) |
| **Protocolo Marcha Continua (`Datos e-Motion/GAIT/`)** | 137 | **95** | 80 Santa Marta (`SMR`), 15 CST (`CST` [13 cinemáticos + 2 métricas]) |
| **Grabaciones Cinemáticas Válidas en Pipeline** | 223 | **223** | 130 TUG + 93 Marcha Continua (excluye 2 métricas tabulares precalculadas) |
| **Participantes Únicos Identificados** | 71 | **70** | Cohortes `LARGE_PD` y `GEOREF` (70 participantes clínicos + controles) |
| **Participantes con Bimodalidad Intra-Sujeto (TUG + GAIT)** | 48 | **48** | Pacientes con prueba TUG y prueba de marcha continua de 10 m |
| **Pares Bimodales Estrictos Confirmados (IMU ↔ e-Motion)** | 42 | **42** | Coincidencia temporal estricta ($|\Delta t| \le 360$ s), protocolo TUG y sexo 100% idéntico |

---

## 2. Desglose Riguroso de Descartes Físicos (44 Archivos Eliminados)

Se auditaron y eliminaron físicamente del disco las 44 muestras que no correspondían a participantes reales o constituían duplicados exactos:

```
Total Grabaciones Iniciales Descargadas: 269
├── Conservadas Físicamente en Disco: 225 (83.6%)
│   ├── Pruebas TUG (Datos e-Motion/TUG/):       130 archivos (101 SMR + 23 LAB + 6 CST)
│   └── Marcha Continua (Datos e-Motion/GAIT/):   95 archivos (80 SMR + 15 CST)
│
└── Eliminadas Físicamente del Disco: 44 (16.4%)
    ├── Pruebas técnicas de personal interno (i2t_staff):   2 archivos
    └── Réplicas exactas de re-sincronización en nube:     42 archivos
```

### Tabla de Justificación Metodológica de Descartes:

| Motivo de Descarte | Muestras | Justificación Metodológica |
|---|:---:|---|
| **Pruebas de Personal Interno (`i2t_staff`)** | 2 | Pruebas técnicas de ingenieros de soporte para calibrar la cámara al encender el equipo. No corresponden a pacientes ni controles. |
| **Réplicas de Sincronización en Nube** | 42 | Reintentos automáticos generados por cortes de conectividad wifi en la brigada de Santa Marta. Contenían exactamente la misma secuencia esquelética que la prueba del día anterior. |

---

## 3. Especificaciones Técnicas del Sistema Óptico

* **Instrumentación:** Cámaras RGB-D de profundidad Intel RealSense D455 / D455F y Orbbec Astra 2.
* **Frecuencia de Muestreo:** Nominal 30.0 Hz (remuestreada a rejilla equitemporal de 30.0 Hz mediante interpolación hermítica monótona PCHIP y filtrada con Butterworth paso bajas a 3.0 Hz).
* **Esquemas Articulares:**
  - **Versión `v1.2.0` (75 archivos en disco):** 19 articulaciones 3D.
  - **Versión `v1.3.0` / `v0.3.6` (148 archivos en disco):** 15 articulaciones 3D.
  - **Centro Pélvico Universal (`SpineBase`):** Presente en el 100% de las 223 series cinemáticas como equivalente biomecánico de `Hip Center`.

---

## 4. Inventario Oficial de Grabaciones en Disco (225 Archivos)

| # | Archivo | ID e-Motion | Fecha | Brigada | Protocolo | ¿Tiene IMU? | Sujeto IMU | Clase | Edad | Sexo | Sensor | ID VIMOV |
|---:|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|---|
| 1 | `CST_ID1_eMotion_P54_TUG.json` | ID1 | 2026-07-04 | CST | TUG | **SÍ** | P54 | PATIENT | 63 | MALE | Orbbec Orbbec Astra 2 | `LARGE_PD_902` |
| 2 | `CST_ID2_eMotion_NO_TUG.json` | ID2 | 2026-07-04 | CST | TUG | NO | - | CONTROL | 64 | F | Orbbec Orbbec Astra 2 | `LARGE_PD_899` |
| 3 | `CST_ID3_eMotion_NO_TUG.json` | ID3 | 2026-07-04 | CST | TUG | NO | - | PATIENT | 63 | M | Orbbec Orbbec Astra 2 | `LARGE_PD_901` |
| 4 | `CST_ID4_eMotion_NO_TUG.json` | ID4 | 2026-07-04 | CST | TUG | NO | - | PATIENT | 66 | M | Orbbec Orbbec Astra 2 | `LARGE_PD_900` |
| 5 | `CST_ID5_eMotion_NO_TUG.json` | ID5 | 2026-07-04 | CST | TUG | NO | - | CONTROL | 62 | F | Orbbec Orbbec Astra 2 | `a1a5bc1b-ca92-4c95-9a09-03b5a5638cb5` |
| 6 | `CST_ID6_eMotion_NO_TUG.json` | ID6 | 2026-07-04 | CST | TUG | NO | - | SIN_ETIQUETA | 83 | - | Orbbec Orbbec Astra 2 | `4e68a4a8-0151-4f1c-aaa5-7902a1f23e7f` |
| 7 | `LAB_ID10_eMotion_NO_TUG.json` | ID10 | 2026-10-14 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455F | `` |
| 8 | `LAB_ID11_eMotion_NO_TUG.json` | ID11 | 2026-10-14 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455F | `` |
| 9 | `LAB_ID12_eMotion_NO_TUG.json` | ID12 | 2026-10-14 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455F | `` |
| 10 | `LAB_ID13_eMotion_NO_TUG.json` | ID13 | 2026-10-14 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455F | `` |
| 11 | `LAB_ID14_eMotion_NO_TUG.json` | ID14 | 2026-10-15 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455F | `` |
| 12 | `LAB_ID15_eMotion_NO_TUG.json` | ID15 | 2026-10-15 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455F | `` |
| 13 | `LAB_ID16_eMotion_NO_TUG.json` | ID16 | 2026-10-15 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455F | `` |
| 14 | `LAB_ID17_eMotion_NO_TUG.json` | ID17 | 2026-10-15 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455F | `` |
| 15 | `LAB_ID18_eMotion_NO_TUG.json` | ID18 | 2026-10-15 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455F | `` |
| 16 | `LAB_ID19_eMotion_NO_TUG.json` | ID19 | 2026-10-15 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455F | `` |
| 17 | `LAB_ID1_eMotion_NO_TUG.json` | ID1 | 2024-10-16 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel RealSense D455 | `` |
| 18 | `LAB_ID20_eMotion_NO_TUG.json` | ID20 | 2026-10-15 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455F | `` |
| 19 | `LAB_ID21_eMotion_NO_TUG.json` | ID21 | 2026-10-15 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455F | `` |
| 20 | `LAB_ID22_eMotion_NO_TUG.json` | ID22 | 2026-10-16 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455 | `` |
| 21 | `LAB_ID23_eMotion_NO_TUG.json` | ID23 | 2026-10-16 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455 | `` |
| 22 | `LAB_ID2_eMotion_NO_TUG.json` | ID2 | 2026-10-02 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455F | `` |
| 23 | `LAB_ID3_eMotion_NO_TUG.json` | ID3 | 2026-10-02 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455F | `` |
| 24 | `LAB_ID4_eMotion_NO_TUG.json` | ID4 | 2026-10-02 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455F | `` |
| 25 | `LAB_ID5_eMotion_NO_TUG.json` | ID5 | 2026-10-02 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455F | `` |
| 26 | `LAB_ID6_eMotion_NO_TUG.json` | ID6 | 2026-10-02 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455F | `` |
| 27 | `LAB_ID7_eMotion_NO_TUG.json` | ID7 | 2026-10-14 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455F | `` |
| 28 | `LAB_ID8_eMotion_NO_TUG.json` | ID8 | 2026-10-14 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455F | `` |
| 29 | `LAB_ID9_eMotion_NO_TUG.json` | ID9 | 2026-10-14 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455F | `` |
| 30 | `SMR_ID100_eMotion_NO_TUG.json` | ID100 | 2026-06-27 | SMR | TUG | NO | - | PATIENT | 50 | M | Intel Intel RealSense D455F | `LARGE_PD_890` |
| 31 | `SMR_ID101_eMotion_NO_TUG.json` | ID101 | 2026-06-27 | SMR | TUG | NO | - | PATIENT | 59 | M | Intel Intel RealSense D455F | `LARGE_PD_888` |
| 32 | `SMR_ID10_eMotion_P18_TUG.json` | ID10 | 2026-06-25 | SMR | TUG | **SÍ** | P18 | PATIENT | 62 | MALE | Intel Intel RealSense D455F | `LARGE_PD_849` |
| 33 | `SMR_ID11_eMotion_P21_TUG.json` | ID11 | 2026-06-25 | SMR | TUG | **SÍ** | P21 | PATIENT | 64 | MALE | Intel Intel RealSense D455F | `LARGE_PD_852` |
| 34 | `SMR_ID12_eMotion_P22_TUG.json` | ID12 | 2026-06-25 | SMR | TUG | **SÍ** | P22 | PATIENT | 73 | MALE | Intel Intel RealSense D455F | `LARGE_PD_855` |
| 35 | `SMR_ID13_eMotion_P24_TUG.json` | ID13 | 2026-06-26 | SMR | TUG | **SÍ** | P24 | PATIENT | -74 | MALE | Intel Intel RealSense D455F | `LARGE_PD_865` |
| 36 | `SMR_ID14_eMotion_P25_TUG.json` | ID14 | 2026-06-26 | SMR | TUG | **SÍ** | P25 | PATIENT | 73 | FEMALE | Intel Intel RealSense D455F | `LARGE_PD_862` |
| 37 | `SMR_ID15_eMotion_P26_TUG.json` | ID15 | 2026-06-26 | SMR | TUG | **SÍ** | P26 | PATIENT | 70 | FEMALE | Intel Intel RealSense D455F | `LARGE_PD_867` |
| 38 | `SMR_ID16_eMotion_P27_TUG.json` | ID16 | 2026-06-26 | SMR | TUG | **SÍ** | P27 | PATIENT | 50 | FEMALE | Intel Intel RealSense D455F | `LARGE_PD_866` |
| 39 | `SMR_ID17_eMotion_P30_TUG.json` | ID17 | 2026-06-26 | SMR | TUG | **SÍ** | P30 | PATIENT | 64 | FEMALE | Intel Intel RealSense D455F | `LARGE_PD_858` |
| 40 | `SMR_ID18_eMotion_P31_TUG.json` | ID18 | 2026-06-26 | SMR | TUG | **SÍ** | P31 | PATIENT | 67 | FEMALE | Intel Intel RealSense D455F | `LARGE_PD_863` |
| 41 | `SMR_ID19_eMotion_P31_TUG.json` | ID19 | 2026-06-26 | SMR | TUG | **SÍ** | P31 | PATIENT | 67 | FEMALE | Intel Intel RealSense D455F | `LARGE_PD_863` |
| 42 | `SMR_ID1_eMotion_P06_TUG.json` | ID1 | 2026-06-25 | SMR | TUG | **SÍ** | P06 | PATIENT | 71 | MALE | Intel Intel RealSense D455F | `large_pd_839` |
| 43 | `SMR_ID20_eMotion_P32_TUG.json` | ID20 | 2026-06-26 | SMR | TUG | **SÍ** | P32 | PATIENT | 71 | MALE | Intel Intel RealSense D455F | `LARGE_PD_861` |
| 44 | `SMR_ID21_eMotion_P32_TUG.json` | ID21 | 2026-06-26 | SMR | TUG | **SÍ** | P32 | PATIENT | 71 | MALE | Intel Intel RealSense D455F | `LARGE_PD_861` |
| 45 | `SMR_ID22_eMotion_P32_TUG.json` | ID22 | 2026-06-26 | SMR | TUG | **SÍ** | P32 | PATIENT | 71 | MALE | Intel Intel RealSense D455F | `LARGE_PD_861` |
| 46 | `SMR_ID23_eMotion_P33_TUG.json` | ID23 | 2026-06-26 | SMR | TUG | **SÍ** | P33 | PATIENT | 55 | FEMALE | Intel Intel RealSense D455F | `LARGE_PD_868` |
| 47 | `SMR_ID24_eMotion_P34_TUG.json` | ID24 | 2026-06-26 | SMR | TUG | **SÍ** | P34 | PATIENT | 69 | MALE | Intel Intel RealSense D455F | `LARGE_PD_869` |
| 48 | `SMR_ID25_eMotion_P35_TUG.json` | ID25 | 2026-06-26 | SMR | TUG | **SÍ** | P35 | PATIENT | 66 | MALE | Intel Intel RealSense D455F | `LARGE_PD_870` |
| 49 | `SMR_ID26_eMotion_P36_TUG.json` | ID26 | 2026-06-26 | SMR | TUG | **SÍ** | P36 | PATIENT | 68 | MALE | Intel Intel RealSense D455F | `LARGE_PD_873` |
| 50 | `SMR_ID27_eMotion_P37_TUG.json` | ID27 | 2026-06-26 | SMR | TUG | **SÍ** | P37 | PATIENT | 62 | FEMALE | Intel Intel RealSense D455F | `LARGE_PD_875` |
| 51 | `SMR_ID28_eMotion_P38_TUG.json` | ID28 | 2026-06-26 | SMR | TUG | **SÍ** | P38 | PATIENT | 57 | FEMALE | Intel Intel RealSense D455F | `LARGE_PD_878` |
| 52 | `SMR_ID29_eMotion_P39_TUG.json` | ID29 | 2026-06-26 | SMR | TUG | **SÍ** | P39 | PATIENT | 59 | MALE | Intel Intel RealSense D455F | `LARGE_PD_871` |
| 53 | `SMR_ID2_eMotion_P07_TUG.json` | ID2 | 2026-06-25 | SMR | TUG | **SÍ** | P07 | PATIENT | 60 | MALE | Intel Intel RealSense D455F | `LARGE_PD_836` |
| 54 | `SMR_ID30_eMotion_P40_TUG.json` | ID30 | 2026-06-27 | SMR | TUG | **SÍ** | P40 | PATIENT | 76 | MALE | Intel Intel RealSense D455F | `LARGE_PD_880` |
| 55 | `SMR_ID31_eMotion_P42_TUG.json` | ID31 | 2026-06-27 | SMR | TUG | **SÍ** | P42 | PATIENT | 44 | MALE | Intel Intel RealSense D455F | `LARGE_PD_883` |
| 56 | `SMR_ID32_eMotion_P43_TUG.json` | ID32 | 2026-06-27 | SMR | TUG | **SÍ** | P43 | PATIENT | 68 | MALE | Intel Intel RealSense D455F | `LARGE_PD_882` |
| 57 | `SMR_ID33_eMotion_P44_TUG.json` | ID33 | 2026-06-27 | SMR | TUG | **SÍ** | P44 | PATIENT | 52 | FEMALE | Intel Intel RealSense D455F | `LARGE_PD_885` |
| 58 | `SMR_ID34_eMotion_P46_TUG.json` | ID34 | 2026-06-27 | SMR | TUG | **SÍ** | P46 | PATIENT | 59 | MALE | Intel Intel RealSense D455F | `LARGE_PD_888` |
| 59 | `SMR_ID35_eMotion_P47_TUG.json` | ID35 | 2026-06-27 | SMR | TUG | **SÍ** | P47 | PATIENT | 54 | MALE | Intel Intel RealSense D455F | `LARGE_PD_884` |
| 60 | `SMR_ID36_eMotion_P48_TUG.json` | ID36 | 2026-06-27 | SMR | TUG | **SÍ** | P48 | PATIENT | 72 | MALE | Intel Intel RealSense D455F | `ebc986d7-f6ae-4bda-8e7f-cbefbbdaf435` |
| 61 | `SMR_ID37_eMotion_P49_TUG.json` | ID37 | 2026-06-27 | SMR | TUG | **SÍ** | P49 | PATIENT | 72 | MALE | Intel Intel RealSense D455F | `LARGE_PD_892` |
| 62 | `SMR_ID38_eMotion_P50_TUG.json` | ID38 | 2026-06-27 | SMR | TUG | **SÍ** | P50 | PATIENT | 50 | MALE | Intel Intel RealSense D455F | `LARGE_PD_890` |
| 63 | `SMR_ID39_eMotion_P51_TUG.json` | ID39 | 2026-06-27 | SMR | TUG | **SÍ** | P51 | PATIENT | 71 | FEMALE | Intel Intel RealSense D455F | `LARGE_PD_894` |
| 64 | `SMR_ID3_eMotion_P08_TUG.json` | ID3 | 2026-06-25 | SMR | TUG | **SÍ** | P08 | PATIENT | 61 | MALE | Intel Intel RealSense D455F | `LARGE_PD_842` |
| 65 | `SMR_ID40_eMotion_P52_TUG.json` | ID40 | 2026-06-27 | SMR | TUG | **SÍ** | P52 | PATIENT | 47 | FEMALE | Intel Intel RealSense D455F | `large_pd_896` |
| 66 | `SMR_ID41_eMotion_NO_TUG.json` | ID41 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 62 | M | Intel Intel RealSense D455F | `LARGE_PD_849` |
| 67 | `SMR_ID42_eMotion_NO_TUG.json` | ID42 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 72 | F | Intel Intel RealSense D455F | `LARGE_PD_854` |
| 68 | `SMR_ID43_eMotion_NO_TUG.json` | ID43 | 2026-06-25 | SMR | TUG | NO | - | SIN_ETIQUETA | 39 | M | Intel Intel RealSense D455F | `i2t_staff` |
| 69 | `SMR_ID44_eMotion_NO_TUG.json` | ID44 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 56 | M | Intel Intel RealSense D455F | `LARGE_PD_853` |
| 70 | `SMR_ID45_eMotion_NO_TUG.json` | ID45 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 66 | M | Intel Intel RealSense D455F | `LARGE_PD_840` |
| 71 | `SMR_ID46_eMotion_NO_TUG.json` | ID46 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 68 | F | Intel Intel RealSense D455F | `large_pd_848` |
| 72 | `SMR_ID47_eMotion_NO_TUG.json` | ID47 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 60 | M | Intel Intel RealSense D455F | `LARGE_PD_836` |
| 73 | `SMR_ID48_eMotion_NO_TUG.json` | ID48 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 77 | M | Intel Intel RealSense D455F | `LARGE_PD_837` |
| 74 | `SMR_ID49_eMotion_NO_TUG.json` | ID49 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 63 | F | Intel Intel RealSense D455F | `LARGE_PD_844` |
| 75 | `SMR_ID4_eMotion_P09_TUG.json` | ID4 | 2026-06-25 | SMR | TUG | **SÍ** | P09 | PATIENT | 77 | MALE | Intel Intel RealSense D455F | `LARGE_PD_837` |
| 76 | `SMR_ID50_eMotion_NO_TUG.json` | ID50 | 2026-06-25 | SMR | TUG | NO | - | CONTROL | 70 | M | Intel Intel RealSense D455F | `93e09117-cee1-421d-93a2-4aab91930b43` |
| 77 | `SMR_ID51_eMotion_NO_TUG.json` | ID51 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 72 | F | Intel Intel RealSense D455F | `LARGE_PD_854` |
| 78 | `SMR_ID52_eMotion_NO_TUG.json` | ID52 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 64 | M | Intel Intel RealSense D455F | `LARGE_PD_852` |
| 79 | `SMR_ID53_eMotion_NO_TUG.json` | ID53 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 68 | F | Intel Intel RealSense D455F | `LARGE_PD_846` |
| 80 | `SMR_ID54_eMotion_NO_TUG.json` | ID54 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 66 | M | Intel Intel RealSense D455F | `LARGE_PD_840` |
| 81 | `SMR_ID55_eMotion_NO_TUG.json` | ID55 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 61 | M | Intel Intel RealSense D455F | `LARGE_PD_842` |
| 82 | `SMR_ID56_eMotion_NO_TUG.json` | ID56 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 68 | F | Intel Intel RealSense D455F | `large_pd_848` |
| 83 | `SMR_ID57_eMotion_NO_TUG.json` | ID57 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 66 | M | Intel Intel RealSense D455F | `LARGE_PD_843` |
| 84 | `SMR_ID58_eMotion_NO_TUG.json` | ID58 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 56 | M | Intel Intel RealSense D455F | `LARGE_PD_853` |
| 85 | `SMR_ID59_eMotion_NO_TUG.json` | ID59 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 73 | M | Intel Intel RealSense D455F | `LARGE_PD_855` |
| 86 | `SMR_ID5_eMotion_P10_TUG.json` | ID5 | 2026-06-25 | SMR | TUG | **SÍ** | P10 | PATIENT | 63 | MALE | Intel Intel RealSense D455F | `LARGE_PD_841` |
| 87 | `SMR_ID60_eMotion_NO_TUG.json` | ID60 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 68 | F | Intel Intel RealSense D455F | `large_pd_848` |
| 88 | `SMR_ID61_eMotion_NO_TUG.json` | ID61 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 68 | F | Intel Intel RealSense D455F | `LARGE_PD_846` |
| 89 | `SMR_ID62_eMotion_NO_TUG.json` | ID62 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 63 | M | Intel Intel RealSense D455F | `LARGE_PD_841` |
| 90 | `SMR_ID63_eMotion_NO_TUG.json` | ID63 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 77 | M | Intel Intel RealSense D455F | `LARGE_PD_850` |
| 91 | `SMR_ID64_eMotion_NO_TUG.json` | ID64 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 74 | F | Intel Intel RealSense D455F | `LARGE_PD_864` |
| 92 | `SMR_ID65_eMotion_NO_TUG.json` | ID65 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 47 | M | Intel Intel RealSense D455F | `LARGE_PD_857` |
| 93 | `SMR_ID66_eMotion_NO_TUG.json` | ID66 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 55 | F | Intel Intel RealSense D455F | `LARGE_PD_868` |
| 94 | `SMR_ID67_eMotion_NO_TUG.json` | ID67 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 64 | F | Intel Intel RealSense D455F | `LARGE_PD_858` |
| 95 | `SMR_ID68_eMotion_NO_TUG.json` | ID68 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 57 | F | Intel Intel RealSense D455F | `LARGE_PD_878` |
| 96 | `SMR_ID69_eMotion_NO_TUG.json` | ID69 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 73 | F | Intel Intel RealSense D455F | `LARGE_PD_860` |
| 97 | `SMR_ID6_eMotion_P11_TUG.json` | ID6 | 2026-06-25 | SMR | TUG | **SÍ** | P11 | PATIENT | 66 | MALE | Intel Intel RealSense D455F | `LARGE_PD_840` |
| 98 | `SMR_ID70_eMotion_NO_TUG.json` | ID70 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 50 | F | Intel Intel RealSense D455F | `LARGE_PD_866` |
| 99 | `SMR_ID71_eMotion_NO_TUG.json` | ID71 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 73 | F | Intel Intel RealSense D455F | `LARGE_PD_862` |
| 100 | `SMR_ID72_eMotion_NO_TUG.json` | ID72 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 67 | F | Intel Intel RealSense D455F | `LARGE_PD_863` |
| 101 | `SMR_ID73_eMotion_NO_TUG.json` | ID73 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 74 | F | Intel Intel RealSense D455F | `LARGE_PD_864` |
| 102 | `SMR_ID74_eMotion_NO_TUG.json` | ID74 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 73 | F | Intel Intel RealSense D455F | `LARGE_PD_860` |
| 103 | `SMR_ID75_eMotion_NO_TUG.json` | ID75 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 71 | M | Intel Intel RealSense D455F | `LARGE_PD_861` |
| 104 | `SMR_ID76_eMotion_NO_TUG.json` | ID76 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 71 | M | Intel Intel RealSense D455F | `LARGE_PD_861` |
| 105 | `SMR_ID77_eMotion_NO_TUG.json` | ID77 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 62 | F | Intel Intel RealSense D455F | `LARGE_PD_875` |
| 106 | `SMR_ID78_eMotion_NO_TUG.json` | ID78 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 71 | M | Intel Intel RealSense D455F | `LARGE_PD_861` |
| 107 | `SMR_ID79_eMotion_NO_TUG.json` | ID79 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 70 | F | Intel Intel RealSense D455F | `LARGE_PD_867` |
| 108 | `SMR_ID7_eMotion_P13_TUG.json` | ID7 | 2026-06-25 | SMR | TUG | **SÍ** | P13 | PATIENT | 66 | MALE | Intel Intel RealSense D455F | `LARGE_PD_843` |
| 109 | `SMR_ID80_eMotion_NO_TUG.json` | ID80 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 47 | M | Intel Intel RealSense D455F | `LARGE_PD_857` |
| 110 | `SMR_ID81_eMotion_NO_TUG.json` | ID81 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | -74 | M | Intel Intel RealSense D455F | `LARGE_PD_865` |
| 111 | `SMR_ID82_eMotion_NO_TUG.json` | ID82 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 66 | M | Intel Intel RealSense D455F | `LARGE_PD_870` |
| 112 | `SMR_ID83_eMotion_NO_TUG.json` | ID83 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 69 | M | Intel Intel RealSense D455F | `LARGE_PD_869` |
| 113 | `SMR_ID84_eMotion_NO_TUG.json` | ID84 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 59 | M | Intel Intel RealSense D455F | `LARGE_PD_871` |
| 114 | `SMR_ID85_eMotion_NO_TUG.json` | ID85 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 68 | M | Intel Intel RealSense D455F | `LARGE_PD_873` |
| 115 | `SMR_ID86_eMotion_NO_TUG.json` | ID86 | 2026-06-27 | SMR | TUG | NO | - | PATIENT | 52 | F | Intel Intel RealSense D455F | `LARGE_PD_885` |
| 116 | `SMR_ID87_eMotion_NO_TUG.json` | ID87 | 2026-06-27 | SMR | TUG | NO | - | PATIENT | 47 | F | Intel Intel RealSense D455F | `large_pd_896` |
| 117 | `SMR_ID88_eMotion_NO_TUG.json` | ID88 | 2026-06-27 | SMR | TUG | NO | - | PATIENT | 68 | M | Intel Intel RealSense D455F | `LARGE_PD_882` |
| 118 | `SMR_ID89_eMotion_NO_TUG.json` | ID89 | 2026-06-27 | SMR | TUG | NO | - | PATIENT | 71 | F | Intel Intel RealSense D455F | `LARGE_PD_894` |
| 119 | `SMR_ID8_eMotion_P15_TUG.json` | ID8 | 2026-06-25 | SMR | TUG | **SÍ** | P15 | PATIENT | 70 | MALE | Intel Intel RealSense D455F | `93e09117-cee1-421d-93a2-4aab91930b43` |
| 120 | `SMR_ID90_eMotion_NO_TUG.json` | ID90 | 2026-06-27 | SMR | TUG | NO | - | PATIENT | 58 | M | Intel Intel RealSense D455F | `LARGE_PD_891` |
| 121 | `SMR_ID91_eMotion_NO_TUG.json` | ID91 | 2026-06-27 | SMR | TUG | NO | - | PATIENT | 76 | M | Intel Intel RealSense D455F | `LARGE_PD_880` |
| 122 | `SMR_ID92_eMotion_NO_TUG.json` | ID92 | 2026-06-27 | SMR | TUG | NO | - | PATIENT | 54 | M | Intel Intel RealSense D455F | `LARGE_PD_884` |
| 123 | `SMR_ID93_eMotion_NO_TUG.json` | ID93 | 2026-06-27 | SMR | TUG | NO | - | PATIENT | 72 | M | Intel Intel RealSense D455F | `ebc986d7-f6ae-4bda-8e7f-cbefbbdaf435` |
| 124 | `SMR_ID94_eMotion_NO_TUG.json` | ID94 | 2026-06-27 | SMR | TUG | NO | - | PATIENT | 53 | M | Intel Intel RealSense D455F | `LARGE_PD_879` |
| 125 | `SMR_ID95_eMotion_NO_TUG.json` | ID95 | 2026-06-27 | SMR | TUG | NO | - | PATIENT | 72 | M | Intel Intel RealSense D455F | `LARGE_PD_892` |
| 126 | `SMR_ID96_eMotion_NO_TUG.json` | ID96 | 2026-06-27 | SMR | TUG | NO | - | PATIENT | 53 | M | Intel Intel RealSense D455F | `LARGE_PD_879` |
| 127 | `SMR_ID97_eMotion_NO_TUG.json` | ID97 | 2026-06-27 | SMR | TUG | NO | - | PATIENT | 58 | M | Intel Intel RealSense D455F | `LARGE_PD_891` |
| 128 | `SMR_ID98_eMotion_NO_TUG.json` | ID98 | 2026-06-27 | SMR | TUG | NO | - | PATIENT | 72 | M | Intel Intel RealSense D455F | `ebc986d7-f6ae-4bda-8e7f-cbefbbdaf435` |
| 129 | `SMR_ID99_eMotion_NO_TUG.json` | ID99 | 2026-06-27 | SMR | TUG | NO | - | PATIENT | 44 | M | Intel Intel RealSense D455F | `LARGE_PD_883` |
| 130 | `SMR_ID9_eMotion_P16_TUG.json` | ID9 | 2026-06-25 | SMR | TUG | **SÍ** | P16 | PATIENT | 77 | MALE | Intel Intel RealSense D455F | `LARGE_PD_850` |
| 131 | `CST_ID10_eMotion_P64_GAIT.json` | ID10 | 2026-07-04 | CST | GAIT | NO | P64 | CONTROL | 70 | F | Intel RealSense D455 | `LARGE_PD_904` |
| 132 | `CST_ID11_eMotion_P65_GAIT.json` | ID11 | 2026-07-04 | CST | GAIT | NO | P65 | CONTROL | 62 | F | Intel RealSense D455 | `a1a5bc1b-ca92-4c95-9a09-03b5a5638cb5` |
| 133 | `CST_ID12_eMotion_P57_GAIT.json` | ID12 | 2026-07-04 | CST | GAIT | NO | P57 | CONTROL | 61 | F | Intel RealSense D455 | `64bc7d94-bf67-4cbc-ba25-55bcc222a8fb` |
| 134 | `CST_ID13_eMotion_P58_GAIT.json` | ID13 | 2026-07-04 | CST | GAIT | NO | P58 | PATIENT | 55 | M | Intel RealSense D455 | `2e1ac92b-ef7d-4acd-b39d-70b2ceac6798` |
| 135 | `CST_ID1_eMotion_NO_GAIT.json` | ID1 | 2026-07-04 | CST | GAIT | NO | - | PATIENT | 69 | M | Intel RealSense D455 | `LARGE_PD_903` |
| 136 | `CST_ID2_eMotion_P59_GAIT.json` | ID2 | 2026-07-04 | CST | GAIT | NO | P59 | CONTROL | 64 | F | Intel RealSense D455 | `large_pd_898` |
| 137 | `CST_ID3_eMotion_P53_GAIT.json` | ID3 | 2026-07-04 | CST | GAIT | NO | P53 | PATIENT | 63 | M | Intel RealSense D455 | `LARGE_PD_902` |
| 138 | `CST_ID4_eMotion_P60_GAIT.json` | ID4 | 2026-07-04 | CST | GAIT | NO | P60 | PATIENT | 66 | M | Intel RealSense D455 | `LARGE_PD_900` |
| 139 | `CST_ID5_eMotion_P61_GAIT.json` | ID5 | 2026-07-04 | CST | GAIT | NO | P61 | CONTROL | 64 | F | Intel RealSense D455 | `LARGE_PD_899` |
| 140 | `CST_ID6_eMotion_P62_GAIT.json` | ID6 | 2026-07-04 | CST | GAIT | NO | P62 | PATIENT | 62 | U | Intel RealSense D455 | `large_pd_914` |
| 141 | `CST_ID7_eMotion_P55_GAIT.json` | ID7 | 2026-07-04 | CST | GAIT | NO | P55 | PATIENT | 40 | M | Intel RealSense D455 | `LARGE_PD_911` |
| 142 | `CST_ID8_eMotion_P56_GAIT.json` | ID8 | 2026-07-04 | CST | GAIT | NO | P56 | PATIENT | 58 | M | Intel RealSense D455 | `62843ff4-c9bc-4513-a152-1d414091b270` |
| 143 | `CST_ID9_eMotion_P63_GAIT.json` | ID9 | 2026-07-04 | CST | GAIT | NO | P63 | PATIENT | 83 | M | Intel RealSense D455 | `LARGE_PD_909` |
| 144 | `CST_M1_eMotion_NO_GAIT.json` | M1 | 2026-07-04 | CST | GAIT | NO | - | SIN_ETIQUETA | - | - | Intel RealSense vs Orbbec Astra 2 | `` |
| 145 | `CST_M2_eMotion_NO_GAIT.json` | M2 | 2026-07-04 | CST | GAIT | NO | - | SIN_ETIQUETA | - | - | Intel RealSense vs Orbbec Astra 2 | `` |
| 146 | `SMR_ID10_eMotion_NO_GAIT.json` | ID10 | 2026-06-25 | SMR | GAIT | NO | - | PATIENT | 68 | F | Intel RealSense D455 | `large_pd_848` |
| 147 | `SMR_ID11_eMotion_P20_GAIT.json` | ID11 | 2026-06-25 | SMR | GAIT | NO | P20 | PATIENT | 56 | M | Intel RealSense D455 | `LARGE_PD_853` |
| 148 | `SMR_ID12_eMotion_P18_GAIT.json` | ID12 | 2026-06-25 | SMR | GAIT | NO | P18 | PATIENT | 62 | M | Intel RealSense D455 | `LARGE_PD_849` |
| 149 | `SMR_ID13_eMotion_NO_GAIT.json` | ID13 | 2026-06-25 | SMR | GAIT | NO | - | PATIENT | 72 | F | Intel RealSense D455 | `LARGE_PD_854` |
| 150 | `SMR_ID14_eMotion_P21_GAIT.json` | ID14 | 2026-06-25 | SMR | GAIT | NO | P21 | PATIENT | 64 | M | Intel Intel RealSense D455F | `LARGE_PD_852` |
| 151 | `SMR_ID15_eMotion_P22_GAIT.json` | ID15 | 2026-06-25 | SMR | GAIT | NO | P22 | PATIENT | 73 | M | Intel RealSense D455 | `LARGE_PD_855` |
| 152 | `SMR_ID16_eMotion_P24_GAIT.json` | ID16 | 2026-06-26 | SMR | GAIT | NO | P24 | PATIENT | -74 | M | Intel Intel RealSense D455F | `LARGE_PD_865` |
| 153 | `SMR_ID17_eMotion_P25_GAIT.json` | ID17 | 2026-06-26 | SMR | GAIT | NO | P25 | PATIENT | 73 | F | Intel Intel RealSense D455F | `LARGE_PD_862` |
| 154 | `SMR_ID18_eMotion_P26_GAIT.json` | ID18 | 2026-06-26 | SMR | GAIT | NO | P26 | PATIENT | 70 | F | Intel Intel RealSense D455F | `LARGE_PD_867` |
| 155 | `SMR_ID19_eMotion_P31_GAIT.json` | ID19 | 2026-06-26 | SMR | GAIT | NO | P31 | PATIENT | 67 | F | Intel Intel RealSense D455F | `LARGE_PD_863` |
| 156 | `SMR_ID1_eMotion_P06_GAIT.json` | ID1 | 2026-06-25 | SMR | GAIT | NO | P06 | PATIENT | 71 | M | Intel RealSense D455 | `large_pd_839` |
| 157 | `SMR_ID20_eMotion_P32_GAIT.json` | ID20 | 2026-06-26 | SMR | GAIT | NO | P32 | PATIENT | 71 | M | Intel Intel RealSense D455F | `LARGE_PD_861` |
| 158 | `SMR_ID21_eMotion_P35_GAIT.json` | ID21 | 2026-06-26 | SMR | GAIT | NO | P35 | PATIENT | 66 | M | Intel Intel RealSense D455F | `LARGE_PD_870` |
| 159 | `SMR_ID22_eMotion_P39_GAIT.json` | ID22 | 2026-06-26 | SMR | GAIT | NO | P39 | PATIENT | 59 | M | Intel Intel RealSense D455F | `LARGE_PD_871` |
| 160 | `SMR_ID23_eMotion_P43_GAIT.json` | ID23 | 2026-06-27 | SMR | GAIT | NO | P43 | PATIENT | 68 | M | Intel Intel RealSense D455F | `LARGE_PD_882` |
| 161 | `SMR_ID24_eMotion_P44_GAIT.json` | ID24 | 2026-06-27 | SMR | GAIT | NO | P44 | PATIENT | 52 | F | Intel Intel RealSense D455F | `LARGE_PD_885` |
| 162 | `SMR_ID25_eMotion_P47_GAIT.json` | ID25 | 2026-06-27 | SMR | GAIT | NO | P47 | PATIENT | 54 | M | Intel RealSense D455 | `LARGE_PD_884` |
| 163 | `SMR_ID26_eMotion_P52_GAIT.json` | ID26 | 2026-06-27 | SMR | GAIT | NO | P52 | PATIENT | 47 | F | Intel RealSense D455 | `large_pd_896` |
| 164 | `SMR_ID27_eMotion_NO_GAIT.json` | ID27 | 2026-06-25 | SMR | GAIT | NO | - | PATIENT | 66 | F | Intel Intel RealSense D455F | `GEOREF409` |
| 165 | `SMR_ID28_eMotion_NO_GAIT.json` | ID28 | 2026-06-25 | SMR | GAIT | NO | - | SIN_ETIQUETA | 21 | M | Intel RealSense D455F | `7f8d3734-9ccf-4a82-8f2b-76b18d82aef0` |
| 166 | `SMR_ID29_eMotion_NO_GAIT.json` | ID29 | 2026-06-25 | SMR | GAIT | NO | - | SIN_ETIQUETA | 21 | M | Intel RealSense D455F | `7f8d3734-9ccf-4a82-8f2b-76b18d82aef0` |
| 167 | `SMR_ID2_eMotion_P08_GAIT.json` | ID2 | 2026-06-25 | SMR | GAIT | NO | P08 | PATIENT | 61 | M | Intel RealSense D455 | `LARGE_PD_842` |
| 168 | `SMR_ID30_eMotion_NO_GAIT.json` | ID30 | 2026-06-25 | SMR | GAIT | NO | - | PATIENT | 66 | M | Intel RealSense D455 | `GEOREF404` |
| 169 | `SMR_ID31_eMotion_NO_GAIT.json` | ID31 | 2026-06-25 | SMR | GAIT | NO | - | PATIENT | 66 | F | Intel RealSense D455 | `GEOREF409` |
| 170 | `SMR_ID32_eMotion_NO_GAIT.json` | ID32 | 2026-06-25 | SMR | GAIT | NO | - | PATIENT | 73 | M | Intel Intel RealSense D455F | `GEOREF_418` |
| 171 | `SMR_ID33_eMotion_NO_GAIT.json` | ID33 | 2026-06-25 | SMR | GAIT | NO | - | PATIENT | 72 | F | Intel Intel RealSense D455F | `GEOREF417` |
| 172 | `SMR_ID34_eMotion_P20_GAIT.json` | ID34 | 2026-06-25 | SMR | GAIT | **SÍ** | P20 | PATIENT | 56 | M | Intel Intel RealSense D455F | `GEOREF_416` |
| 173 | `SMR_ID35_eMotion_NO_GAIT.json` | ID35 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 74 | F | Intel RealSense D455 | `LARGE_PD_864` |
| 174 | `SMR_ID36_eMotion_NO_GAIT.json` | ID36 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 55 | F | Intel Intel RealSense D455F | `LARGE_PD_868` |
| 175 | `SMR_ID37_eMotion_NO_GAIT.json` | ID37 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 55 | F | Intel RealSense D455 | `LARGE_PD_868` |
| 176 | `SMR_ID38_eMotion_NO_GAIT.json` | ID38 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 62 | F | Intel RealSense D455 | `LARGE_PD_875` |
| 177 | `SMR_ID39_eMotion_NO_GAIT.json` | ID39 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 69 | F | Intel RealSense D455 | `LARGE_PD_874` |
| 178 | `SMR_ID3_eMotion_P09_GAIT.json` | ID3 | 2026-06-25 | SMR | GAIT | NO | P09 | PATIENT | 77 | M | Intel RealSense D455 | `LARGE_PD_837` |
| 179 | `SMR_ID40_eMotion_NO_GAIT.json` | ID40 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 57 | F | Intel RealSense D455 | `LARGE_PD_878` |
| 180 | `SMR_ID41_eMotion_NO_GAIT.json` | ID41 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 69 | M | Intel Intel RealSense D455F | `LARGE_PD_869` |
| 181 | `SMR_ID42_eMotion_NO_GAIT.json` | ID42 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 69 | F | Intel Intel RealSense D455F | `LARGE_PD_874` |
| 182 | `SMR_ID43_eMotion_NO_GAIT.json` | ID43 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 71 | M | Intel RealSense D455 | `LARGE_PD_861` |
| 183 | `SMR_ID44_eMotion_NO_GAIT.json` | ID44 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 50 | F | Intel Intel RealSense D455F | `LARGE_PD_866` |
| 184 | `SMR_ID45_eMotion_NO_GAIT.json` | ID45 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 47 | M | Intel RealSense D455 | `GEOREF420` |
| 185 | `SMR_ID46_eMotion_NO_GAIT.json` | ID46 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 73 | F | Intel Intel RealSense D455F | `LARGE_PD_860` |
| 186 | `SMR_ID47_eMotion_NO_GAIT.json` | ID47 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 66 | M | Intel RealSense D455 | `LARGE_PD_870` |
| 187 | `SMR_ID48_eMotion_NO_GAIT.json` | ID48 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 47 | M | Intel Intel RealSense D455F | `GEOREF420` |
| 188 | `SMR_ID49_eMotion_NO_GAIT.json` | ID49 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 46 | U | Intel RealSense D455 | `5e33b641-8ae3-43fe-a74c-539a4d38b829` |
| 189 | `SMR_ID4_eMotion_P10_GAIT.json` | ID4 | 2026-06-25 | SMR | GAIT | NO | P10 | PATIENT | 63 | M | Intel RealSense D455 | `LARGE_PD_841` |
| 190 | `SMR_ID50_eMotion_NO_GAIT.json` | ID50 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 74 | F | Intel Intel RealSense D455F | `LARGE_PD_864` |
| 191 | `SMR_ID51_eMotion_NO_GAIT.json` | ID51 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 73 | F | Intel RealSense D455 | `LARGE_PD_860` |
| 192 | `SMR_ID52_eMotion_NO_GAIT.json` | ID52 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 67 | F | Intel Intel RealSense D455F | `LARGE_PD_863` |
| 193 | `SMR_ID53_eMotion_NO_GAIT.json` | ID53 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 57 | F | Intel Intel RealSense D455F | `LARGE_PD_878` |
| 194 | `SMR_ID54_eMotion_NO_GAIT.json` | ID54 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 64 | F | Intel Intel RealSense D455F | `GEOREF421` |
| 195 | `SMR_ID55_eMotion_NO_GAIT.json` | ID55 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 64 | F | Intel RealSense D455 | `GEOREF421` |
| 196 | `SMR_ID56_eMotion_NO_GAIT.json` | ID56 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 68 | M | Intel RealSense D455 | `LARGE_PD_873` |
| 197 | `SMR_ID57_eMotion_NO_GAIT.json` | ID57 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 68 | M | Intel Intel RealSense D455F | `LARGE_PD_873` |
| 198 | `SMR_ID58_eMotion_NO_GAIT.json` | ID58 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 62 | F | Intel Intel RealSense D455F | `LARGE_PD_875` |
| 199 | `SMR_ID59_eMotion_NO_GAIT.json` | ID59 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 67 | F | Intel RealSense D455 | `LARGE_PD_863` |
| 200 | `SMR_ID5_eMotion_P12_GAIT.json` | ID5 | 2026-06-25 | SMR | GAIT | NO | P12 | PATIENT | 63 | F | Intel RealSense D455 | `LARGE_PD_844` |
| 201 | `SMR_ID60_eMotion_NO_GAIT.json` | ID60 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 50 | F | Intel RealSense D455 | `LARGE_PD_866` |
| 202 | `SMR_ID61_eMotion_NO_GAIT.json` | ID61 | 2026-06-27 | SMR | GAIT | NO | - | PATIENT | 53 | M | Intel RealSense D455 | `LARGE_PD_879` |
| 203 | `SMR_ID62_eMotion_NO_GAIT.json` | ID62 | 2026-06-27 | SMR | GAIT | NO | - | PATIENT | 76 | M | Intel RealSense D455 | `LARGE_PD_880` |
| 204 | `SMR_ID63_eMotion_NO_GAIT.json` | ID63 | 2026-06-27 | SMR | GAIT | NO | - | PATIENT | 44 | M | Intel Intel RealSense D455F | `LARGE_PD_883` |
| 205 | `SMR_ID64_eMotion_NO_GAIT.json` | ID64 | 2026-06-27 | SMR | GAIT | NO | - | PATIENT | 59 | M | Intel Intel RealSense D455F | `LARGE_PD_888` |
| 206 | `SMR_ID65_eMotion_NO_GAIT.json` | ID65 | 2026-06-27 | SMR | GAIT | NO | - | PATIENT | 72 | M | Intel Intel RealSense D455F | `ebc986d7-f6ae-4bda-8e7f-cbefbbdaf435` |
| 207 | `SMR_ID66_eMotion_NO_GAIT.json` | ID66 | 2026-06-27 | SMR | GAIT | NO | - | PATIENT | 44 | M | Intel RealSense D455 | `LARGE_PD_883` |
| 208 | `SMR_ID67_eMotion_NO_GAIT.json` | ID67 | 2026-06-27 | SMR | GAIT | NO | - | PATIENT | 62 | M | Intel Intel RealSense D455F | `LARGE_PD_886` |
| 209 | `SMR_ID68_eMotion_NO_GAIT.json` | ID68 | 2026-06-27 | SMR | GAIT | NO | - | PATIENT | 44 | M | Intel RealSense D455 | `LARGE_PD_883` |
| 210 | `SMR_ID69_eMotion_NO_GAIT.json` | ID69 | 2026-06-27 | SMR | GAIT | NO | - | SIN_ETIQUETA | 91 | M | Intel RealSense D455 | `488d71ce-4448-488d-bf7c-a638f8e9f299` |
| 211 | `SMR_ID6_eMotion_P13_GAIT.json` | ID6 | 2026-06-25 | SMR | GAIT | NO | P13 | PATIENT | 66 | M | Intel RealSense D455 | `LARGE_PD_843` |
| 212 | `SMR_ID70_eMotion_NO_GAIT.json` | ID70 | 2026-06-27 | SMR | GAIT | NO | - | PATIENT | 44 | M | Intel Intel RealSense D455F | `LARGE_PD_883` |
| 213 | `SMR_ID71_eMotion_NO_GAIT.json` | ID71 | 2026-06-27 | SMR | GAIT | NO | - | PATIENT | 72 | M | Intel RealSense D455 | `LARGE_PD_892` |
| 214 | `SMR_ID72_eMotion_NO_GAIT.json` | ID72 | 2026-06-27 | SMR | GAIT | NO | - | PATIENT | 62 | M | Intel RealSense D455 | `LARGE_PD_886` |
| 215 | `SMR_ID73_eMotion_NO_GAIT.json` | ID73 | 2026-06-27 | SMR | GAIT | NO | - | PATIENT | 62 | M | Intel Intel RealSense D455F | `LARGE_PD_886` |
| 216 | `SMR_ID74_eMotion_NO_GAIT.json` | ID74 | 2026-06-27 | SMR | GAIT | NO | - | SIN_ETIQUETA | 91 | M | Intel Intel RealSense D455F | `488d71ce-4448-488d-bf7c-a638f8e9f299` |
| 217 | `SMR_ID75_eMotion_NO_GAIT.json` | ID75 | 2026-06-27 | SMR | GAIT | NO | - | PATIENT | 72 | M | Intel Intel RealSense D455F | `LARGE_PD_892` |
| 218 | `SMR_ID76_eMotion_NO_GAIT.json` | ID76 | 2026-06-27 | SMR | GAIT | NO | - | PATIENT | 58 | M | Intel RealSense D455 | `LARGE_PD_891` |
| 219 | `SMR_ID77_eMotion_NO_GAIT.json` | ID77 | 2026-06-27 | SMR | GAIT | NO | - | PATIENT | 59 | U | Intel RealSense D455 | `9f0538b6-a833-46e9-955c-d77f70d33d82` |
| 220 | `SMR_ID78_eMotion_NO_GAIT.json` | ID78 | 2026-06-27 | SMR | GAIT | NO | - | PATIENT | 76 | M | Intel Intel RealSense D455F | `LARGE_PD_880` |
| 221 | `SMR_ID79_eMotion_NO_GAIT.json` | ID79 | 2026-06-27 | SMR | GAIT | NO | - | PATIENT | 58 | M | Intel Intel RealSense D455F | `LARGE_PD_891` |
| 222 | `SMR_ID7_eMotion_P14_GAIT.json` | ID7 | 2026-06-25 | SMR | GAIT | NO | P14 | CONTROL | 70 | M | Intel RealSense D455 | `93e09117-cee1-421d-93a2-4aab91930b43` |
| 223 | `SMR_ID80_eMotion_NO_GAIT.json` | ID80 | 2026-06-27 | SMR | GAIT | NO | - | PATIENT | 47 | F | Intel Intel RealSense D455F | `large_pd_896` |
| 224 | `SMR_ID8_eMotion_P15_GAIT.json` | ID8 | 2026-06-25 | SMR | GAIT | NO | P15 | PATIENT | 45 | U | Intel RealSense D455 | `3e142b0a-9c60-476d-9588-ef96ce9c080c` |
| 225 | `SMR_ID9_eMotion_P16_GAIT.json` | ID9 | 2026-06-25 | SMR | GAIT | NO | P16 | PATIENT | 77 | M | Intel RealSense D455 | `LARGE_PD_850` |

---
*Ficha técnica oficial del dataset óptico (e-Motion / VIMOV) — Control de calidad y trazabilidad.*
