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
| 1 | `CST_IDE1_TUG_P54.json` | ID1 | 2026-07-04 | CST | TUG | **SÍ** | P54 | PATIENT | 63 | MALE | Orbbec Orbbec Astra 2 | `LARGE_PD_902` |
| 2 | `CST_IDE2_TUG_NO.json` | ID2 | 2026-07-04 | CST | TUG | NO | - | CONTROL | 64 | F | Orbbec Orbbec Astra 2 | `LARGE_PD_899` |
| 3 | `CST_IDE3_TUG_NO.json` | ID3 | 2026-07-04 | CST | TUG | NO | - | PATIENT | 63 | M | Orbbec Orbbec Astra 2 | `LARGE_PD_901` |
| 4 | `CST_IDE4_TUG_NO.json` | ID4 | 2026-07-04 | CST | TUG | NO | - | PATIENT | 66 | M | Orbbec Orbbec Astra 2 | `LARGE_PD_900` |
| 5 | `CST_IDE5_TUG_NO.json` | ID5 | 2026-07-04 | CST | TUG | NO | - | CONTROL | 62 | F | Orbbec Orbbec Astra 2 | `a1a5bc1b-ca92-4c95-9a09-03b5a5638cb5` |
| 6 | `CST_IDE6_TUG_NO.json` | ID6 | 2026-07-04 | CST | TUG | NO | - | SIN_ETIQUETA | 83 | - | Orbbec Orbbec Astra 2 | `4e68a4a8-0151-4f1c-aaa5-7902a1f23e7f` |
| 7 | `LAB_IDE10_TUG_NO.json` | ID10 | 2026-10-14 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455F | `` |
| 8 | `LAB_IDE11_TUG_NO.json` | ID11 | 2026-10-14 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455F | `` |
| 9 | `LAB_IDE12_TUG_NO.json` | ID12 | 2026-10-14 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455F | `` |
| 10 | `LAB_IDE13_TUG_NO.json` | ID13 | 2026-10-14 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455F | `` |
| 11 | `LAB_IDE14_TUG_NO.json` | ID14 | 2026-10-15 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455F | `` |
| 12 | `LAB_IDE15_TUG_NO.json` | ID15 | 2026-10-15 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455F | `` |
| 13 | `LAB_IDE16_TUG_NO.json` | ID16 | 2026-10-15 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455F | `` |
| 14 | `LAB_IDE17_TUG_NO.json` | ID17 | 2026-10-15 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455F | `` |
| 15 | `LAB_IDE18_TUG_NO.json` | ID18 | 2026-10-15 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455F | `` |
| 16 | `LAB_IDE19_TUG_NO.json` | ID19 | 2026-10-15 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455F | `` |
| 17 | `LAB_IDE1_TUG_NO.json` | ID1 | 2024-10-16 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel RealSense D455 | `` |
| 18 | `LAB_IDE20_TUG_NO.json` | ID20 | 2026-10-15 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455F | `` |
| 19 | `LAB_IDE21_TUG_NO.json` | ID21 | 2026-10-15 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455F | `` |
| 20 | `LAB_IDE22_TUG_NO.json` | ID22 | 2026-10-16 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455 | `` |
| 21 | `LAB_IDE23_TUG_NO.json` | ID23 | 2026-10-16 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455 | `` |
| 22 | `LAB_IDE2_TUG_NO.json` | ID2 | 2026-10-02 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455F | `` |
| 23 | `LAB_IDE3_TUG_NO.json` | ID3 | 2026-10-02 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455F | `` |
| 24 | `LAB_IDE4_TUG_NO.json` | ID4 | 2026-10-02 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455F | `` |
| 25 | `LAB_IDE5_TUG_NO.json` | ID5 | 2026-10-02 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455F | `` |
| 26 | `LAB_IDE6_TUG_NO.json` | ID6 | 2026-10-02 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455F | `` |
| 27 | `LAB_IDE7_TUG_NO.json` | ID7 | 2026-10-14 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455F | `` |
| 28 | `LAB_IDE8_TUG_NO.json` | ID8 | 2026-10-14 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455F | `` |
| 29 | `LAB_IDE9_TUG_NO.json` | ID9 | 2026-10-14 | LAB | TUG | NO | - | CONTROL_LAB | - | - | Intel Intel RealSense D455F | `` |
| 30 | `SMR_IDE100_TUG_NO.json` | ID100 | 2026-06-27 | SMR | TUG | NO | - | PATIENT | 50 | M | Intel Intel RealSense D455F | `LARGE_PD_890` |
| 31 | `SMR_IDE101_TUG_NO.json` | ID101 | 2026-06-27 | SMR | TUG | NO | - | PATIENT | 59 | M | Intel Intel RealSense D455F | `LARGE_PD_888` |
| 32 | `SMR_IDE10_TUG_P18.json` | ID10 | 2026-06-25 | SMR | TUG | **SÍ** | P18 | PATIENT | 62 | MALE | Intel Intel RealSense D455F | `LARGE_PD_849` |
| 33 | `SMR_IDE11_TUG_P21.json` | ID11 | 2026-06-25 | SMR | TUG | **SÍ** | P21 | PATIENT | 64 | MALE | Intel Intel RealSense D455F | `LARGE_PD_852` |
| 34 | `SMR_IDE12_TUG_P22.json` | ID12 | 2026-06-25 | SMR | TUG | **SÍ** | P22 | PATIENT | 73 | MALE | Intel Intel RealSense D455F | `LARGE_PD_855` |
| 35 | `SMR_IDE13_TUG_P24.json` | ID13 | 2026-06-26 | SMR | TUG | **SÍ** | P24 | PATIENT | -74 | MALE | Intel Intel RealSense D455F | `LARGE_PD_865` |
| 36 | `SMR_IDE14_TUG_P25.json` | ID14 | 2026-06-26 | SMR | TUG | **SÍ** | P25 | PATIENT | 73 | FEMALE | Intel Intel RealSense D455F | `LARGE_PD_862` |
| 37 | `SMR_IDE15_TUG_P26.json` | ID15 | 2026-06-26 | SMR | TUG | **SÍ** | P26 | PATIENT | 70 | FEMALE | Intel Intel RealSense D455F | `LARGE_PD_867` |
| 38 | `SMR_IDE16_TUG_P27.json` | ID16 | 2026-06-26 | SMR | TUG | **SÍ** | P27 | PATIENT | 50 | FEMALE | Intel Intel RealSense D455F | `LARGE_PD_866` |
| 39 | `SMR_IDE17_TUG_P30.json` | ID17 | 2026-06-26 | SMR | TUG | **SÍ** | P30 | PATIENT | 64 | FEMALE | Intel Intel RealSense D455F | `LARGE_PD_858` |
| 40 | `SMR_IDE18_TUG_P31.json` | ID18 | 2026-06-26 | SMR | TUG | **SÍ** | P31 | PATIENT | 67 | FEMALE | Intel Intel RealSense D455F | `LARGE_PD_863` |
| 41 | `SMR_IDE19_TUG_P31.json` | ID19 | 2026-06-26 | SMR | TUG | **SÍ** | P31 | PATIENT | 67 | FEMALE | Intel Intel RealSense D455F | `LARGE_PD_863` |
| 42 | `SMR_IDE1_TUG_P06.json` | ID1 | 2026-06-25 | SMR | TUG | **SÍ** | P06 | PATIENT | 71 | MALE | Intel Intel RealSense D455F | `large_pd_839` |
| 43 | `SMR_IDE20_TUG_P32.json` | ID20 | 2026-06-26 | SMR | TUG | **SÍ** | P32 | PATIENT | 71 | MALE | Intel Intel RealSense D455F | `LARGE_PD_861` |
| 44 | `SMR_IDE21_TUG_P32.json` | ID21 | 2026-06-26 | SMR | TUG | **SÍ** | P32 | PATIENT | 71 | MALE | Intel Intel RealSense D455F | `LARGE_PD_861` |
| 45 | `SMR_IDE22_TUG_P32.json` | ID22 | 2026-06-26 | SMR | TUG | **SÍ** | P32 | PATIENT | 71 | MALE | Intel Intel RealSense D455F | `LARGE_PD_861` |
| 46 | `SMR_IDE23_TUG_P33.json` | ID23 | 2026-06-26 | SMR | TUG | **SÍ** | P33 | PATIENT | 55 | FEMALE | Intel Intel RealSense D455F | `LARGE_PD_868` |
| 47 | `SMR_IDE24_TUG_P34.json` | ID24 | 2026-06-26 | SMR | TUG | **SÍ** | P34 | PATIENT | 69 | MALE | Intel Intel RealSense D455F | `LARGE_PD_869` |
| 48 | `SMR_IDE25_TUG_P35.json` | ID25 | 2026-06-26 | SMR | TUG | **SÍ** | P35 | PATIENT | 66 | MALE | Intel Intel RealSense D455F | `LARGE_PD_870` |
| 49 | `SMR_IDE26_TUG_P36.json` | ID26 | 2026-06-26 | SMR | TUG | **SÍ** | P36 | PATIENT | 68 | MALE | Intel Intel RealSense D455F | `LARGE_PD_873` |
| 50 | `SMR_IDE27_TUG_P37.json` | ID27 | 2026-06-26 | SMR | TUG | **SÍ** | P37 | PATIENT | 62 | FEMALE | Intel Intel RealSense D455F | `LARGE_PD_875` |
| 51 | `SMR_IDE28_TUG_P38.json` | ID28 | 2026-06-26 | SMR | TUG | **SÍ** | P38 | PATIENT | 57 | FEMALE | Intel Intel RealSense D455F | `LARGE_PD_878` |
| 52 | `SMR_IDE29_TUG_P39.json` | ID29 | 2026-06-26 | SMR | TUG | **SÍ** | P39 | PATIENT | 59 | MALE | Intel Intel RealSense D455F | `LARGE_PD_871` |
| 53 | `SMR_IDE2_TUG_P07.json` | ID2 | 2026-06-25 | SMR | TUG | **SÍ** | P07 | PATIENT | 60 | MALE | Intel Intel RealSense D455F | `LARGE_PD_836` |
| 54 | `SMR_IDE30_TUG_P40.json` | ID30 | 2026-06-27 | SMR | TUG | **SÍ** | P40 | PATIENT | 76 | MALE | Intel Intel RealSense D455F | `LARGE_PD_880` |
| 55 | `SMR_IDE31_TUG_P42.json` | ID31 | 2026-06-27 | SMR | TUG | **SÍ** | P42 | PATIENT | 44 | MALE | Intel Intel RealSense D455F | `LARGE_PD_883` |
| 56 | `SMR_IDE32_TUG_P43.json` | ID32 | 2026-06-27 | SMR | TUG | **SÍ** | P43 | PATIENT | 68 | MALE | Intel Intel RealSense D455F | `LARGE_PD_882` |
| 57 | `SMR_IDE33_TUG_P44.json` | ID33 | 2026-06-27 | SMR | TUG | **SÍ** | P44 | PATIENT | 52 | FEMALE | Intel Intel RealSense D455F | `LARGE_PD_885` |
| 58 | `SMR_IDE34_TUG_P46.json` | ID34 | 2026-06-27 | SMR | TUG | **SÍ** | P46 | PATIENT | 59 | MALE | Intel Intel RealSense D455F | `LARGE_PD_888` |
| 59 | `SMR_IDE35_TUG_P47.json` | ID35 | 2026-06-27 | SMR | TUG | **SÍ** | P47 | PATIENT | 54 | MALE | Intel Intel RealSense D455F | `LARGE_PD_884` |
| 60 | `SMR_IDE36_TUG_P48.json` | ID36 | 2026-06-27 | SMR | TUG | **SÍ** | P48 | PATIENT | 72 | MALE | Intel Intel RealSense D455F | `ebc986d7-f6ae-4bda-8e7f-cbefbbdaf435` |
| 61 | `SMR_IDE37_TUG_P49.json` | ID37 | 2026-06-27 | SMR | TUG | **SÍ** | P49 | PATIENT | 72 | MALE | Intel Intel RealSense D455F | `LARGE_PD_892` |
| 62 | `SMR_IDE38_TUG_P50.json` | ID38 | 2026-06-27 | SMR | TUG | **SÍ** | P50 | PATIENT | 50 | MALE | Intel Intel RealSense D455F | `LARGE_PD_890` |
| 63 | `SMR_IDE39_TUG_P51.json` | ID39 | 2026-06-27 | SMR | TUG | **SÍ** | P51 | PATIENT | 71 | FEMALE | Intel Intel RealSense D455F | `LARGE_PD_894` |
| 64 | `SMR_IDE3_TUG_P08.json` | ID3 | 2026-06-25 | SMR | TUG | **SÍ** | P08 | PATIENT | 61 | MALE | Intel Intel RealSense D455F | `LARGE_PD_842` |
| 65 | `SMR_IDE40_TUG_P52.json` | ID40 | 2026-06-27 | SMR | TUG | **SÍ** | P52 | PATIENT | 47 | FEMALE | Intel Intel RealSense D455F | `large_pd_896` |
| 66 | `SMR_IDE41_TUG_NO.json` | ID41 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 62 | M | Intel Intel RealSense D455F | `LARGE_PD_849` |
| 67 | `SMR_IDE42_TUG_NO.json` | ID42 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 72 | F | Intel Intel RealSense D455F | `LARGE_PD_854` |
| 68 | `SMR_IDE43_TUG_NO.json` | ID43 | 2026-06-25 | SMR | TUG | NO | - | SIN_ETIQUETA | 39 | M | Intel Intel RealSense D455F | `i2t_staff` |
| 69 | `SMR_IDE44_TUG_NO.json` | ID44 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 56 | M | Intel Intel RealSense D455F | `LARGE_PD_853` |
| 70 | `SMR_IDE45_TUG_NO.json` | ID45 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 66 | M | Intel Intel RealSense D455F | `LARGE_PD_840` |
| 71 | `SMR_IDE46_TUG_NO.json` | ID46 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 68 | F | Intel Intel RealSense D455F | `large_pd_848` |
| 72 | `SMR_IDE47_TUG_NO.json` | ID47 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 60 | M | Intel Intel RealSense D455F | `LARGE_PD_836` |
| 73 | `SMR_IDE48_TUG_NO.json` | ID48 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 77 | M | Intel Intel RealSense D455F | `LARGE_PD_837` |
| 74 | `SMR_IDE49_TUG_NO.json` | ID49 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 63 | F | Intel Intel RealSense D455F | `LARGE_PD_844` |
| 75 | `SMR_IDE4_TUG_P09.json` | ID4 | 2026-06-25 | SMR | TUG | **SÍ** | P09 | PATIENT | 77 | MALE | Intel Intel RealSense D455F | `LARGE_PD_837` |
| 76 | `SMR_IDE50_TUG_NO.json` | ID50 | 2026-06-25 | SMR | TUG | NO | - | CONTROL | 70 | M | Intel Intel RealSense D455F | `93e09117-cee1-421d-93a2-4aab91930b43` |
| 77 | `SMR_IDE51_TUG_NO.json` | ID51 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 72 | F | Intel Intel RealSense D455F | `LARGE_PD_854` |
| 78 | `SMR_IDE52_TUG_NO.json` | ID52 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 64 | M | Intel Intel RealSense D455F | `LARGE_PD_852` |
| 79 | `SMR_IDE53_TUG_NO.json` | ID53 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 68 | F | Intel Intel RealSense D455F | `LARGE_PD_846` |
| 80 | `SMR_IDE54_TUG_NO.json` | ID54 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 66 | M | Intel Intel RealSense D455F | `LARGE_PD_840` |
| 81 | `SMR_IDE55_TUG_NO.json` | ID55 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 61 | M | Intel Intel RealSense D455F | `LARGE_PD_842` |
| 82 | `SMR_IDE56_TUG_NO.json` | ID56 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 68 | F | Intel Intel RealSense D455F | `large_pd_848` |
| 83 | `SMR_IDE57_TUG_NO.json` | ID57 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 66 | M | Intel Intel RealSense D455F | `LARGE_PD_843` |
| 84 | `SMR_IDE58_TUG_NO.json` | ID58 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 56 | M | Intel Intel RealSense D455F | `LARGE_PD_853` |
| 85 | `SMR_IDE59_TUG_NO.json` | ID59 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 73 | M | Intel Intel RealSense D455F | `LARGE_PD_855` |
| 86 | `SMR_IDE5_TUG_P10.json` | ID5 | 2026-06-25 | SMR | TUG | **SÍ** | P10 | PATIENT | 63 | MALE | Intel Intel RealSense D455F | `LARGE_PD_841` |
| 87 | `SMR_IDE60_TUG_NO.json` | ID60 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 68 | F | Intel Intel RealSense D455F | `large_pd_848` |
| 88 | `SMR_IDE61_TUG_NO.json` | ID61 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 68 | F | Intel Intel RealSense D455F | `LARGE_PD_846` |
| 89 | `SMR_IDE62_TUG_NO.json` | ID62 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 63 | M | Intel Intel RealSense D455F | `LARGE_PD_841` |
| 90 | `SMR_IDE63_TUG_NO.json` | ID63 | 2026-06-25 | SMR | TUG | NO | - | PATIENT | 77 | M | Intel Intel RealSense D455F | `LARGE_PD_850` |
| 91 | `SMR_IDE64_TUG_NO.json` | ID64 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 74 | F | Intel Intel RealSense D455F | `LARGE_PD_864` |
| 92 | `SMR_IDE65_TUG_NO.json` | ID65 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 47 | M | Intel Intel RealSense D455F | `LARGE_PD_857` |
| 93 | `SMR_IDE66_TUG_NO.json` | ID66 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 55 | F | Intel Intel RealSense D455F | `LARGE_PD_868` |
| 94 | `SMR_IDE67_TUG_NO.json` | ID67 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 64 | F | Intel Intel RealSense D455F | `LARGE_PD_858` |
| 95 | `SMR_IDE68_TUG_NO.json` | ID68 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 57 | F | Intel Intel RealSense D455F | `LARGE_PD_878` |
| 96 | `SMR_IDE69_TUG_NO.json` | ID69 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 73 | F | Intel Intel RealSense D455F | `LARGE_PD_860` |
| 97 | `SMR_IDE6_TUG_P11.json` | ID6 | 2026-06-25 | SMR | TUG | **SÍ** | P11 | PATIENT | 66 | MALE | Intel Intel RealSense D455F | `LARGE_PD_840` |
| 98 | `SMR_IDE70_TUG_NO.json` | ID70 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 50 | F | Intel Intel RealSense D455F | `LARGE_PD_866` |
| 99 | `SMR_IDE71_TUG_NO.json` | ID71 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 73 | F | Intel Intel RealSense D455F | `LARGE_PD_862` |
| 100 | `SMR_IDE72_TUG_NO.json` | ID72 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 67 | F | Intel Intel RealSense D455F | `LARGE_PD_863` |
| 101 | `SMR_IDE73_TUG_NO.json` | ID73 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 74 | F | Intel Intel RealSense D455F | `LARGE_PD_864` |
| 102 | `SMR_IDE74_TUG_NO.json` | ID74 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 73 | F | Intel Intel RealSense D455F | `LARGE_PD_860` |
| 103 | `SMR_IDE75_TUG_NO.json` | ID75 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 71 | M | Intel Intel RealSense D455F | `LARGE_PD_861` |
| 104 | `SMR_IDE76_TUG_NO.json` | ID76 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 71 | M | Intel Intel RealSense D455F | `LARGE_PD_861` |
| 105 | `SMR_IDE77_TUG_NO.json` | ID77 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 62 | F | Intel Intel RealSense D455F | `LARGE_PD_875` |
| 106 | `SMR_IDE78_TUG_NO.json` | ID78 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 71 | M | Intel Intel RealSense D455F | `LARGE_PD_861` |
| 107 | `SMR_IDE79_TUG_NO.json` | ID79 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 70 | F | Intel Intel RealSense D455F | `LARGE_PD_867` |
| 108 | `SMR_IDE7_TUG_P13.json` | ID7 | 2026-06-25 | SMR | TUG | **SÍ** | P13 | PATIENT | 66 | MALE | Intel Intel RealSense D455F | `LARGE_PD_843` |
| 109 | `SMR_IDE80_TUG_NO.json` | ID80 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 47 | M | Intel Intel RealSense D455F | `LARGE_PD_857` |
| 110 | `SMR_IDE81_TUG_NO.json` | ID81 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | -74 | M | Intel Intel RealSense D455F | `LARGE_PD_865` |
| 111 | `SMR_IDE82_TUG_NO.json` | ID82 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 66 | M | Intel Intel RealSense D455F | `LARGE_PD_870` |
| 112 | `SMR_IDE83_TUG_NO.json` | ID83 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 69 | M | Intel Intel RealSense D455F | `LARGE_PD_869` |
| 113 | `SMR_IDE84_TUG_NO.json` | ID84 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 59 | M | Intel Intel RealSense D455F | `LARGE_PD_871` |
| 114 | `SMR_IDE85_TUG_NO.json` | ID85 | 2026-06-26 | SMR | TUG | NO | - | PATIENT | 68 | M | Intel Intel RealSense D455F | `LARGE_PD_873` |
| 115 | `SMR_IDE86_TUG_NO.json` | ID86 | 2026-06-27 | SMR | TUG | NO | - | PATIENT | 52 | F | Intel Intel RealSense D455F | `LARGE_PD_885` |
| 116 | `SMR_IDE87_TUG_NO.json` | ID87 | 2026-06-27 | SMR | TUG | NO | - | PATIENT | 47 | F | Intel Intel RealSense D455F | `large_pd_896` |
| 117 | `SMR_IDE88_TUG_NO.json` | ID88 | 2026-06-27 | SMR | TUG | NO | - | PATIENT | 68 | M | Intel Intel RealSense D455F | `LARGE_PD_882` |
| 118 | `SMR_IDE89_TUG_NO.json` | ID89 | 2026-06-27 | SMR | TUG | NO | - | PATIENT | 71 | F | Intel Intel RealSense D455F | `LARGE_PD_894` |
| 119 | `SMR_IDE8_TUG_P15.json` | ID8 | 2026-06-25 | SMR | TUG | **SÍ** | P15 | PATIENT | 70 | MALE | Intel Intel RealSense D455F | `93e09117-cee1-421d-93a2-4aab91930b43` |
| 120 | `SMR_IDE90_TUG_NO.json` | ID90 | 2026-06-27 | SMR | TUG | NO | - | PATIENT | 58 | M | Intel Intel RealSense D455F | `LARGE_PD_891` |
| 121 | `SMR_IDE91_TUG_NO.json` | ID91 | 2026-06-27 | SMR | TUG | NO | - | PATIENT | 76 | M | Intel Intel RealSense D455F | `LARGE_PD_880` |
| 122 | `SMR_IDE92_TUG_NO.json` | ID92 | 2026-06-27 | SMR | TUG | NO | - | PATIENT | 54 | M | Intel Intel RealSense D455F | `LARGE_PD_884` |
| 123 | `SMR_IDE93_TUG_NO.json` | ID93 | 2026-06-27 | SMR | TUG | NO | - | PATIENT | 72 | M | Intel Intel RealSense D455F | `ebc986d7-f6ae-4bda-8e7f-cbefbbdaf435` |
| 124 | `SMR_IDE94_TUG_NO.json` | ID94 | 2026-06-27 | SMR | TUG | NO | - | PATIENT | 53 | M | Intel Intel RealSense D455F | `LARGE_PD_879` |
| 125 | `SMR_IDE95_TUG_NO.json` | ID95 | 2026-06-27 | SMR | TUG | NO | - | PATIENT | 72 | M | Intel Intel RealSense D455F | `LARGE_PD_892` |
| 126 | `SMR_IDE96_TUG_NO.json` | ID96 | 2026-06-27 | SMR | TUG | NO | - | PATIENT | 53 | M | Intel Intel RealSense D455F | `LARGE_PD_879` |
| 127 | `SMR_IDE97_TUG_NO.json` | ID97 | 2026-06-27 | SMR | TUG | NO | - | PATIENT | 58 | M | Intel Intel RealSense D455F | `LARGE_PD_891` |
| 128 | `SMR_IDE98_TUG_NO.json` | ID98 | 2026-06-27 | SMR | TUG | NO | - | PATIENT | 72 | M | Intel Intel RealSense D455F | `ebc986d7-f6ae-4bda-8e7f-cbefbbdaf435` |
| 129 | `SMR_IDE99_TUG_NO.json` | ID99 | 2026-06-27 | SMR | TUG | NO | - | PATIENT | 44 | M | Intel Intel RealSense D455F | `LARGE_PD_883` |
| 130 | `SMR_IDE9_TUG_P16.json` | ID9 | 2026-06-25 | SMR | TUG | **SÍ** | P16 | PATIENT | 77 | MALE | Intel Intel RealSense D455F | `LARGE_PD_850` |
| 131 | `CST_IDE10_GAIT_P64.json` | ID10 | 2026-07-04 | CST | GAIT | NO | P64 | CONTROL | 70 | F | Intel RealSense D455 | `LARGE_PD_904` |
| 132 | `CST_IDE11_GAIT_P65.json` | ID11 | 2026-07-04 | CST | GAIT | NO | P65 | CONTROL | 62 | F | Intel RealSense D455 | `a1a5bc1b-ca92-4c95-9a09-03b5a5638cb5` |
| 133 | `CST_IDE12_GAIT_P57.json` | ID12 | 2026-07-04 | CST | GAIT | NO | P57 | CONTROL | 61 | F | Intel RealSense D455 | `64bc7d94-bf67-4cbc-ba25-55bcc222a8fb` |
| 134 | `CST_IDE13_GAIT_P58.json` | ID13 | 2026-07-04 | CST | GAIT | NO | P58 | PATIENT | 55 | M | Intel RealSense D455 | `2e1ac92b-ef7d-4acd-b39d-70b2ceac6798` |
| 135 | `CST_IDE1_GAIT_NO.json` | ID1 | 2026-07-04 | CST | GAIT | NO | - | PATIENT | 69 | M | Intel RealSense D455 | `LARGE_PD_903` |
| 136 | `CST_IDE2_GAIT_P59.json` | ID2 | 2026-07-04 | CST | GAIT | NO | P59 | CONTROL | 64 | F | Intel RealSense D455 | `large_pd_898` |
| 137 | `CST_IDE3_GAIT_P53.json` | ID3 | 2026-07-04 | CST | GAIT | NO | P53 | PATIENT | 63 | M | Intel RealSense D455 | `LARGE_PD_902` |
| 138 | `CST_IDE4_GAIT_P60.json` | ID4 | 2026-07-04 | CST | GAIT | NO | P60 | PATIENT | 66 | M | Intel RealSense D455 | `LARGE_PD_900` |
| 139 | `CST_IDE5_GAIT_P61.json` | ID5 | 2026-07-04 | CST | GAIT | NO | P61 | CONTROL | 64 | F | Intel RealSense D455 | `LARGE_PD_899` |
| 140 | `CST_IDE6_GAIT_P62.json` | ID6 | 2026-07-04 | CST | GAIT | NO | P62 | PATIENT | 62 | U | Intel RealSense D455 | `large_pd_914` |
| 141 | `CST_IDE7_GAIT_P55.json` | ID7 | 2026-07-04 | CST | GAIT | NO | P55 | PATIENT | 40 | M | Intel RealSense D455 | `LARGE_PD_911` |
| 142 | `CST_IDE8_GAIT_P56.json` | ID8 | 2026-07-04 | CST | GAIT | NO | P56 | PATIENT | 58 | M | Intel RealSense D455 | `62843ff4-c9bc-4513-a152-1d414091b270` |
| 143 | `CST_IDE9_GAIT_P63.json` | ID9 | 2026-07-04 | CST | GAIT | NO | P63 | PATIENT | 83 | M | Intel RealSense D455 | `LARGE_PD_909` |
| 144 | `CST_IDEM1_GAIT_NO.json` | M1 | 2026-07-04 | CST | GAIT | NO | - | SIN_ETIQUETA | - | - | Intel RealSense vs Orbbec Astra 2 | `` |
| 145 | `CST_IDEM2_GAIT_NO.json` | M2 | 2026-07-04 | CST | GAIT | NO | - | SIN_ETIQUETA | - | - | Intel RealSense vs Orbbec Astra 2 | `` |
| 146 | `SMR_IDE10_GAIT_NO.json` | ID10 | 2026-06-25 | SMR | GAIT | NO | - | PATIENT | 68 | F | Intel RealSense D455 | `large_pd_848` |
| 147 | `SMR_IDE11_GAIT_P20.json` | ID11 | 2026-06-25 | SMR | GAIT | NO | P20 | PATIENT | 56 | M | Intel RealSense D455 | `LARGE_PD_853` |
| 148 | `SMR_IDE12_GAIT_P18.json` | ID12 | 2026-06-25 | SMR | GAIT | NO | P18 | PATIENT | 62 | M | Intel RealSense D455 | `LARGE_PD_849` |
| 149 | `SMR_IDE13_GAIT_NO.json` | ID13 | 2026-06-25 | SMR | GAIT | NO | - | PATIENT | 72 | F | Intel RealSense D455 | `LARGE_PD_854` |
| 150 | `SMR_IDE14_GAIT_P21.json` | ID14 | 2026-06-25 | SMR | GAIT | NO | P21 | PATIENT | 64 | M | Intel Intel RealSense D455F | `LARGE_PD_852` |
| 151 | `SMR_IDE15_GAIT_P22.json` | ID15 | 2026-06-25 | SMR | GAIT | NO | P22 | PATIENT | 73 | M | Intel RealSense D455 | `LARGE_PD_855` |
| 152 | `SMR_IDE16_GAIT_P24.json` | ID16 | 2026-06-26 | SMR | GAIT | NO | P24 | PATIENT | -74 | M | Intel Intel RealSense D455F | `LARGE_PD_865` |
| 153 | `SMR_IDE17_GAIT_P25.json` | ID17 | 2026-06-26 | SMR | GAIT | NO | P25 | PATIENT | 73 | F | Intel Intel RealSense D455F | `LARGE_PD_862` |
| 154 | `SMR_IDE18_GAIT_P26.json` | ID18 | 2026-06-26 | SMR | GAIT | NO | P26 | PATIENT | 70 | F | Intel Intel RealSense D455F | `LARGE_PD_867` |
| 155 | `SMR_IDE19_GAIT_P31.json` | ID19 | 2026-06-26 | SMR | GAIT | NO | P31 | PATIENT | 67 | F | Intel Intel RealSense D455F | `LARGE_PD_863` |
| 156 | `SMR_IDE1_GAIT_P06.json` | ID1 | 2026-06-25 | SMR | GAIT | NO | P06 | PATIENT | 71 | M | Intel RealSense D455 | `large_pd_839` |
| 157 | `SMR_IDE20_GAIT_P32.json` | ID20 | 2026-06-26 | SMR | GAIT | NO | P32 | PATIENT | 71 | M | Intel Intel RealSense D455F | `LARGE_PD_861` |
| 158 | `SMR_IDE21_GAIT_P35.json` | ID21 | 2026-06-26 | SMR | GAIT | NO | P35 | PATIENT | 66 | M | Intel Intel RealSense D455F | `LARGE_PD_870` |
| 159 | `SMR_IDE22_GAIT_P39.json` | ID22 | 2026-06-26 | SMR | GAIT | NO | P39 | PATIENT | 59 | M | Intel Intel RealSense D455F | `LARGE_PD_871` |
| 160 | `SMR_IDE23_GAIT_P43.json` | ID23 | 2026-06-27 | SMR | GAIT | NO | P43 | PATIENT | 68 | M | Intel Intel RealSense D455F | `LARGE_PD_882` |
| 161 | `SMR_IDE24_GAIT_P44.json` | ID24 | 2026-06-27 | SMR | GAIT | NO | P44 | PATIENT | 52 | F | Intel Intel RealSense D455F | `LARGE_PD_885` |
| 162 | `SMR_IDE25_GAIT_P47.json` | ID25 | 2026-06-27 | SMR | GAIT | NO | P47 | PATIENT | 54 | M | Intel RealSense D455 | `LARGE_PD_884` |
| 163 | `SMR_IDE26_GAIT_P52.json` | ID26 | 2026-06-27 | SMR | GAIT | NO | P52 | PATIENT | 47 | F | Intel RealSense D455 | `large_pd_896` |
| 164 | `SMR_IDE27_GAIT_NO.json` | ID27 | 2026-06-25 | SMR | GAIT | NO | - | PATIENT | 66 | F | Intel Intel RealSense D455F | `GEOREF409` |
| 165 | `SMR_IDE28_GAIT_NO.json` | ID28 | 2026-06-25 | SMR | GAIT | NO | - | SIN_ETIQUETA | 21 | M | Intel RealSense D455F | `7f8d3734-9ccf-4a82-8f2b-76b18d82aef0` |
| 166 | `SMR_IDE29_GAIT_NO.json` | ID29 | 2026-06-25 | SMR | GAIT | NO | - | SIN_ETIQUETA | 21 | M | Intel RealSense D455F | `7f8d3734-9ccf-4a82-8f2b-76b18d82aef0` |
| 167 | `SMR_IDE2_GAIT_P08.json` | ID2 | 2026-06-25 | SMR | GAIT | NO | P08 | PATIENT | 61 | M | Intel RealSense D455 | `LARGE_PD_842` |
| 168 | `SMR_IDE30_GAIT_NO.json` | ID30 | 2026-06-25 | SMR | GAIT | NO | - | PATIENT | 66 | M | Intel RealSense D455 | `GEOREF404` |
| 169 | `SMR_IDE31_GAIT_NO.json` | ID31 | 2026-06-25 | SMR | GAIT | NO | - | PATIENT | 66 | F | Intel RealSense D455 | `GEOREF409` |
| 170 | `SMR_IDE32_GAIT_NO.json` | ID32 | 2026-06-25 | SMR | GAIT | NO | - | PATIENT | 73 | M | Intel Intel RealSense D455F | `GEOREF_418` |
| 171 | `SMR_IDE33_GAIT_NO.json` | ID33 | 2026-06-25 | SMR | GAIT | NO | - | PATIENT | 72 | F | Intel Intel RealSense D455F | `GEOREF417` |
| 172 | `SMR_IDE34_GAIT_P20.json` | ID34 | 2026-06-25 | SMR | GAIT | **SÍ** | P20 | PATIENT | 56 | M | Intel Intel RealSense D455F | `GEOREF_416` |
| 173 | `SMR_IDE35_GAIT_NO.json` | ID35 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 74 | F | Intel RealSense D455 | `LARGE_PD_864` |
| 174 | `SMR_IDE36_GAIT_NO.json` | ID36 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 55 | F | Intel Intel RealSense D455F | `LARGE_PD_868` |
| 175 | `SMR_IDE37_GAIT_NO.json` | ID37 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 55 | F | Intel RealSense D455 | `LARGE_PD_868` |
| 176 | `SMR_IDE38_GAIT_NO.json` | ID38 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 62 | F | Intel RealSense D455 | `LARGE_PD_875` |
| 177 | `SMR_IDE39_GAIT_NO.json` | ID39 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 69 | F | Intel RealSense D455 | `LARGE_PD_874` |
| 178 | `SMR_IDE3_GAIT_P09.json` | ID3 | 2026-06-25 | SMR | GAIT | NO | P09 | PATIENT | 77 | M | Intel RealSense D455 | `LARGE_PD_837` |
| 179 | `SMR_IDE40_GAIT_NO.json` | ID40 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 57 | F | Intel RealSense D455 | `LARGE_PD_878` |
| 180 | `SMR_IDE41_GAIT_NO.json` | ID41 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 69 | M | Intel Intel RealSense D455F | `LARGE_PD_869` |
| 181 | `SMR_IDE42_GAIT_NO.json` | ID42 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 69 | F | Intel Intel RealSense D455F | `LARGE_PD_874` |
| 182 | `SMR_IDE43_GAIT_NO.json` | ID43 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 71 | M | Intel RealSense D455 | `LARGE_PD_861` |
| 183 | `SMR_IDE44_GAIT_NO.json` | ID44 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 50 | F | Intel Intel RealSense D455F | `LARGE_PD_866` |
| 184 | `SMR_IDE45_GAIT_NO.json` | ID45 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 47 | M | Intel RealSense D455 | `GEOREF420` |
| 185 | `SMR_IDE46_GAIT_NO.json` | ID46 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 73 | F | Intel Intel RealSense D455F | `LARGE_PD_860` |
| 186 | `SMR_IDE47_GAIT_NO.json` | ID47 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 66 | M | Intel RealSense D455 | `LARGE_PD_870` |
| 187 | `SMR_IDE48_GAIT_NO.json` | ID48 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 47 | M | Intel Intel RealSense D455F | `GEOREF420` |
| 188 | `SMR_IDE49_GAIT_NO.json` | ID49 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 46 | U | Intel RealSense D455 | `5e33b641-8ae3-43fe-a74c-539a4d38b829` |
| 189 | `SMR_IDE4_GAIT_P10.json` | ID4 | 2026-06-25 | SMR | GAIT | NO | P10 | PATIENT | 63 | M | Intel RealSense D455 | `LARGE_PD_841` |
| 190 | `SMR_IDE50_GAIT_NO.json` | ID50 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 74 | F | Intel Intel RealSense D455F | `LARGE_PD_864` |
| 191 | `SMR_IDE51_GAIT_NO.json` | ID51 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 73 | F | Intel RealSense D455 | `LARGE_PD_860` |
| 192 | `SMR_IDE52_GAIT_NO.json` | ID52 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 67 | F | Intel Intel RealSense D455F | `LARGE_PD_863` |
| 193 | `SMR_IDE53_GAIT_NO.json` | ID53 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 57 | F | Intel Intel RealSense D455F | `LARGE_PD_878` |
| 194 | `SMR_IDE54_GAIT_NO.json` | ID54 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 64 | F | Intel Intel RealSense D455F | `GEOREF421` |
| 195 | `SMR_IDE55_GAIT_NO.json` | ID55 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 64 | F | Intel RealSense D455 | `GEOREF421` |
| 196 | `SMR_IDE56_GAIT_NO.json` | ID56 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 68 | M | Intel RealSense D455 | `LARGE_PD_873` |
| 197 | `SMR_IDE57_GAIT_NO.json` | ID57 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 68 | M | Intel Intel RealSense D455F | `LARGE_PD_873` |
| 198 | `SMR_IDE58_GAIT_NO.json` | ID58 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 62 | F | Intel Intel RealSense D455F | `LARGE_PD_875` |
| 199 | `SMR_IDE59_GAIT_NO.json` | ID59 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 67 | F | Intel RealSense D455 | `LARGE_PD_863` |
| 200 | `SMR_IDE5_GAIT_P12.json` | ID5 | 2026-06-25 | SMR | GAIT | NO | P12 | PATIENT | 63 | F | Intel RealSense D455 | `LARGE_PD_844` |
| 201 | `SMR_IDE60_GAIT_NO.json` | ID60 | 2026-06-26 | SMR | GAIT | NO | - | PATIENT | 50 | F | Intel RealSense D455 | `LARGE_PD_866` |
| 202 | `SMR_IDE61_GAIT_NO.json` | ID61 | 2026-06-27 | SMR | GAIT | NO | - | PATIENT | 53 | M | Intel RealSense D455 | `LARGE_PD_879` |
| 203 | `SMR_IDE62_GAIT_NO.json` | ID62 | 2026-06-27 | SMR | GAIT | NO | - | PATIENT | 76 | M | Intel RealSense D455 | `LARGE_PD_880` |
| 204 | `SMR_IDE63_GAIT_NO.json` | ID63 | 2026-06-27 | SMR | GAIT | NO | - | PATIENT | 44 | M | Intel Intel RealSense D455F | `LARGE_PD_883` |
| 205 | `SMR_IDE64_GAIT_NO.json` | ID64 | 2026-06-27 | SMR | GAIT | NO | - | PATIENT | 59 | M | Intel Intel RealSense D455F | `LARGE_PD_888` |
| 206 | `SMR_IDE65_GAIT_NO.json` | ID65 | 2026-06-27 | SMR | GAIT | NO | - | PATIENT | 72 | M | Intel Intel RealSense D455F | `ebc986d7-f6ae-4bda-8e7f-cbefbbdaf435` |
| 207 | `SMR_IDE66_GAIT_NO.json` | ID66 | 2026-06-27 | SMR | GAIT | NO | - | PATIENT | 44 | M | Intel RealSense D455 | `LARGE_PD_883` |
| 208 | `SMR_IDE67_GAIT_NO.json` | ID67 | 2026-06-27 | SMR | GAIT | NO | - | PATIENT | 62 | M | Intel Intel RealSense D455F | `LARGE_PD_886` |
| 209 | `SMR_IDE68_GAIT_NO.json` | ID68 | 2026-06-27 | SMR | GAIT | NO | - | PATIENT | 44 | M | Intel RealSense D455 | `LARGE_PD_883` |
| 210 | `SMR_IDE69_GAIT_NO.json` | ID69 | 2026-06-27 | SMR | GAIT | NO | - | SIN_ETIQUETA | 91 | M | Intel RealSense D455 | `488d71ce-4448-488d-bf7c-a638f8e9f299` |
| 211 | `SMR_IDE6_GAIT_P13.json` | ID6 | 2026-06-25 | SMR | GAIT | NO | P13 | PATIENT | 66 | M | Intel RealSense D455 | `LARGE_PD_843` |
| 212 | `SMR_IDE70_GAIT_NO.json` | ID70 | 2026-06-27 | SMR | GAIT | NO | - | PATIENT | 44 | M | Intel Intel RealSense D455F | `LARGE_PD_883` |
| 213 | `SMR_IDE71_GAIT_NO.json` | ID71 | 2026-06-27 | SMR | GAIT | NO | - | PATIENT | 72 | M | Intel RealSense D455 | `LARGE_PD_892` |
| 214 | `SMR_IDE72_GAIT_NO.json` | ID72 | 2026-06-27 | SMR | GAIT | NO | - | PATIENT | 62 | M | Intel RealSense D455 | `LARGE_PD_886` |
| 215 | `SMR_IDE73_GAIT_NO.json` | ID73 | 2026-06-27 | SMR | GAIT | NO | - | PATIENT | 62 | M | Intel Intel RealSense D455F | `LARGE_PD_886` |
| 216 | `SMR_IDE74_GAIT_NO.json` | ID74 | 2026-06-27 | SMR | GAIT | NO | - | SIN_ETIQUETA | 91 | M | Intel Intel RealSense D455F | `488d71ce-4448-488d-bf7c-a638f8e9f299` |
| 217 | `SMR_IDE75_GAIT_NO.json` | ID75 | 2026-06-27 | SMR | GAIT | NO | - | PATIENT | 72 | M | Intel Intel RealSense D455F | `LARGE_PD_892` |
| 218 | `SMR_IDE76_GAIT_NO.json` | ID76 | 2026-06-27 | SMR | GAIT | NO | - | PATIENT | 58 | M | Intel RealSense D455 | `LARGE_PD_891` |
| 219 | `SMR_IDE77_GAIT_NO.json` | ID77 | 2026-06-27 | SMR | GAIT | NO | - | PATIENT | 59 | U | Intel RealSense D455 | `9f0538b6-a833-46e9-955c-d77f70d33d82` |
| 220 | `SMR_IDE78_GAIT_NO.json` | ID78 | 2026-06-27 | SMR | GAIT | NO | - | PATIENT | 76 | M | Intel Intel RealSense D455F | `LARGE_PD_880` |
| 221 | `SMR_IDE79_GAIT_NO.json` | ID79 | 2026-06-27 | SMR | GAIT | NO | - | PATIENT | 58 | M | Intel Intel RealSense D455F | `LARGE_PD_891` |
| 222 | `SMR_IDE7_GAIT_P14.json` | ID7 | 2026-06-25 | SMR | GAIT | NO | P14 | CONTROL | 70 | M | Intel RealSense D455 | `93e09117-cee1-421d-93a2-4aab91930b43` |
| 223 | `SMR_IDE80_GAIT_NO.json` | ID80 | 2026-06-27 | SMR | GAIT | NO | - | PATIENT | 47 | F | Intel Intel RealSense D455F | `large_pd_896` |
| 224 | `SMR_IDE8_GAIT_P15.json` | ID8 | 2026-06-25 | SMR | GAIT | NO | P15 | PATIENT | 45 | U | Intel RealSense D455 | `3e142b0a-9c60-476d-9588-ef96ce9c080c` |
| 225 | `SMR_IDE9_GAIT_P16.json` | ID9 | 2026-06-25 | SMR | GAIT | NO | P16 | PATIENT | 77 | M | Intel RealSense D455 | `LARGE_PD_850` |

---
*Ficha técnica oficial del dataset óptico (e-Motion / VIMOV) — Control de calidad y trazabilidad.*
