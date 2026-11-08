# 📄 FICHA TÉCNICA OFICIAL DEL DATASET — PROYECTO TUG-V2
> **Documento Oficial de Auditoría y Control de Calidad**
> **Fecha de Consolidación:** Octubre 2026 · Semana 12
> **Metodología:** CRISP-DM (Fase de Data Understanding y Data Preparation)
> **Directrices Clínicas:** Tutor Prof. Domiciano Rincón (Reuniones #6 y #7)

---

## 1. Resumen Ejecutivo del Conjunto de Datos

| Indicador | Valor Bruto | Valor Tras Descarte (Válidos) | Tasa de Retención |
|:---|:---:|:---:|:---:|
| **Total Grabaciones JSON** | **78** | **66** | **84.6%** |
| **Grabaciones Pacientes (EP)** | 63 | **58** | 92.1% |
| **Grabaciones Sujetos Control** | 8 | **8** | 100.0% |
| **Pruebas Técnicas (Sin etiqueta)** | 7 | **0** | 0.0% (Descartadas) |
| **Participantes Únicos (Personas)** | 65 | **61** (54 Pacientes / 7 Controles) | 93.8% |
| **Razón de Desbalance de Clases** | 7.9 : 1 | **7.25 : 1** (58 tomas EP vs 8 tomas Control) | Requiere +20 controles |

---

## 2. Desglose Riguroso de Descartes (Criterios Reunión #6)

Se evaluaron de forma determinística las 5 reglas fijadas por el tutor metodológico:

```
Total Grabaciones: 78
├── Aceptadas para el Pipeline: 66 (84.6%)
│   ├── Pacientes Parkinson: 58 grabaciones (54 personas únicas)
│   └── Controles Sanos:      8 grabaciones ( 7 personas únicas)
│
└── Descartadas Metodológicamente: 12 (15.4%)
    ├── Pruebas técnicas internas (sin etiqueta clínica): 7 grabaciones
    │   └── (temp_BV, temp_N, temp_BO, temp_BX, temp_BJ, temp_F, temp_AX)
    ├── Duplicados exactos por colisión MD5 de red:       2 grabaciones
    │   └── (temp_BA_2, temp_Z_2)
    └── Pruebas de Doble Tarea (Dual Task cognitiva):     3 grabaciones
        └── (temp_AZ, temp_J, temp_AQ — Paciente P32)
```

### Tabla Resumen de Descartes por Motivo Principal:

| Motivo de Descarte | Muestras Afectadas | Justificación Clínica / Metodológica |
|---|:---:|---|
| **Prueba técnica sin etiqueta** | 7 | Archivos de prueba previa de conexión o calibración (`patientType` vacío). No corresponden a participantes del estudio. |
| **Doble Tarea (Dual Task)** | 3 | Pruebas con exigencia cognitiva añadida (restas sucesivas, ciudades). Al ser solo 3 tomas, carecen de poder estadístico y sesgan la marcha basal. |
| **Duplicado exacto (MD5)** | 2 | Reintentos automáticos de sincronización a la nube generados por fallas intermitentes de red en brigada. Su inclusión sesgaría la varianza. |
| **Falta de sensores mínimos** | *Subsumido* | 4 de las pruebas técnicas también carecían de los 3 sensores indispensables (`BASE-SPINE`, `LEFT-ANKLE`, `RIGHT-ANKLE`). |
| **Duración insuficiente (<5s)**| *Subsumido* | 2 de las pruebas técnicas duraron 2.5s y 3.7s, indicando tomas abortadas. |

---

## 3. Especificaciones Técnicas de las Grabaciones Aceptadas

* **Instrumentación:** Unidades de Medición Inercial (IMUs) triaxiales (Acelerómetro ±16g, Giróscopo ±2000 deg/s).
* **Frecuencia de Muestreo:** Nominal 50 Hz (Efectiva 49.4 ± 0.8 Hz, remuestreada a cuadrícula regular de 50.0 Hz por interpolación lineal).
* **Configuración Anatómica Requerida:** Mínimo 3 sensores obligatorios:
  1. `BASE-SPINE` (Región lumbar L5 / Sacro).
  2. `LEFT-ANKLE` (Tobillo izquierdo, cara lateral externa).
  3. `RIGHT-ANKLE` (Tobillo derecho, cara lateral externa).
  *(Sensores en muñecas `LEFT-HAND` / `RIGHT-HAND` presentes en el 90% de las tomas como accesorios).*
* **Hardware de Brigadas:**
  - Kit `Base` (Prototipo 1): 24 grabaciones válidas.
  - Kit `K1` (Prototipo 2 con reorientación de ejes): 42 grabaciones válidas.
* **Duración Media de la Prueba TUG:** 55.35 ± 8.4 s (Rango: 8.2 s a 57.2 s).

---

## 4. Auditoría Detallada de Muestras Descartadas

| Archivo JSON | Código | Tipo Original | Duración | Causa Exacta del Descarte |
|---|:---:|:---:|:---:|---|
| `20260208022404_temp_BV.json` | `BV` | SIN_ETIQUETA | 18.6 s | Sin etiqueta clínica; falta tobillos (solo 1 sensor) |
| `20260303043120_temp_N.json` | `N` | SIN_ETIQUETA | 5.0 s | Prueba técnica interna de calibración sin paciente |
| `20260303043532_temp_BO.json` | `BO` | SIN_ETIQUETA | 3.7 s | Sin etiqueta clínica; prueba incompleta abortada (<5s) |
| `20260303044505_temp_BX.json` | `BX` | SIN_ETIQUETA | 2.5 s | Sin etiqueta clínica; duración insuficiente (2.5s) |
| `20260303134630_temp_BJ.json` | `BJ` | SIN_ETIQUETA | 6.7 s | Sin etiqueta clínica; faltan sensores mínimos |
| `20260307234249_temp_F.json` | `F` | SIN_ETIQUETA | 15.0 s | Sin etiqueta clínica; prueba técnica |
| `20260308232420_temp_AX.json` | `AX` | SIN_ETIQUETA | 30.4 s | Sin etiqueta clínica; faltan sensores mínimos |
| `20260626133916_temp_BA.json` | `BA` | PATIENT | 50.2 s | Duplicado exacto byte a byte (MD5 idéntico a temp_BA_1) |
| `20260626170733_temp_AZ.json` | `AZ` | PATIENT | 31.5 s | Condición experimental: Dual Task (restas sucesivas) |
| `20260626170919_temp_J.json` | `J` | PATIENT | 14.4 s | Condición experimental: Dual Task (cuenta regresiva) |
| `20260626170956_temp_AQ.json` | `AQ` | PATIENT | 15.6 s | Condición experimental: Dual Task (nombrar ciudades) |
| `20260820142006_temp_Z.json` | `Z` | PATIENT | 57.2 s | Duplicado exacto byte a byte (MD5 idéntico a temp_Z_1) |

---

## 5. Auditoría Detallada de Muestras Aceptadas para el Pipeline (66 Grabaciones)

| # | Archivo JSON | Código | Sujeto ID | Clase | Sexo | Fecha Nacimiento | Talla (cm) | Hardware Kit | Duración | Observaciones Clínicas / Medicación |
|---:|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 1 | `20260611235032_temp_AL.json` | `AL` | `P05` | CONTROL | FEMALE | 10/02/2003 | 155 | Base | 22.4 s | Sin observaciones |
| 2 | `20260618075259_temp_BC.json` | `BC` | `P05` | CONTROL | FEMALE | 10/02/2003 | 156 | K1 | 13.1 s | control |
| 3 | `20260625140746_temp_BF.json` | `BF` | `P06` | PATIENT | MALE | 12/09/1955 | 173 | Base | 22.8 s | paciente DBS |
| 4 | `20260625140851_temp_AR.json` | `AR` | `P06` | PATIENT | MALE | 12/09/1955 | 173 | Base | 41.6 s | paciente DBS |
| 5 | `20260625144044_temp_D.json` | `D` | `P07` | PATIENT | MALE | 25/12/1965 | 160 | Base | 89.3 s | Sin observaciones |
| 6 | `20260625145018_temp_AB.json` | `AB` | `P08` | PATIENT | MALE | 12/02/2026 | 180 | Base | 44.9 s | Paciente |
| 7 | `20260625150353_temp_AK.json` | `AK` | `P09` | PATIENT | MALE | 22/12/1948 | 166 | Base | 73.7 s | paciente amantadina 7am |
| 8 | `20260625152019_temp_AA.json` | `AA` | `P10` | PATIENT | MALE | 24/10/1963 | 175 | Base | 41.4 s | paciente 2016, levodopa y amantadina 6am |
| 9 | `20260625153756_temp_V.json` | `V` | `P11` | PATIENT | MALE | 26/10/1960 | 177 | Base | 69.2 s | Paciente levodopa 8am |
| 10 | `20260625164351_temp_A.json` | `A` | `P12` | PATIENT | FEMALE | 16/11/1962 | 153 | Base | 81.4 s | paciente |
| 11 | `20260625171352_temp_BW.json` | `BW` | `P13` | PATIENT | MALE | 03/08/1960 | 170 | Base | 60.2 s | paciente en on toma 10am |
| 12 | `20260625180613_temp_AG.json` | `AG` | `P14` | CONTROL | MALE | 11/11/1955 | 165 | Base | 70.6 s | Sin observaciones |
| 13 | `20260625183434_temp_BK.json` | `BK` | `P15` | PATIENT | MALE | 30/12/1957 | 160 | Base | 66.8 s | paciente levodopa 2pm |
| 14 | `20260625193811_temp_BD.json` | `BD` | `P16` | PATIENT | MALE | 16/09/1949 | 185 | Base | 60.8 s | paciente |
| 15 | `20260625195406_temp_BR.json` | `BR` | `P17` | PATIENT | MALE | 29/03/1958 | 150 | Base | 50.6 s | DBS / dbs |
| 16 | `20260625195426_temp_AP.json` | `AP` | `P17` | PATIENT | MALE | 29/03/1958 | 150 | Base | 12.2 s | DBS |
| 17 | `20260625204358_temp_BN.json` | `BN` | `P18` | PATIENT | MALE | 31/01/1964 | 170 | Base | 54.6 s | paciente, levodopa. estado off. toma a las 3pm |
| 18 | `20260625212453_temp_G.json` | `G` | `P19` | PATIENT | MALE | 27/03/1954 | 165 | Base | 63.9 s | paciente levodopa, dosis a las 3pm. estado on |
| 19 | `20260625214451_temp_BH.json` | `BH` | `P20` | PATIENT | MALE | 30/11/1969 | 173 | K1 | 66.0 s | paciente amantadina. |
| 20 | `20260625214518_temp_S.json` | `S` | `P20` | PATIENT | MALE | 30/11/1969 | 173 | K1 | 101.8 s | paciente amantadina. |
| 21 | `20260625215046_temp_X.json` | `X` | `P21` | PATIENT | MALE | 21/01/1962 | 168 | K1 | 53.9 s | levodopa. 10am, estado on |
| 22 | `20260626133915_temp_BA.json` | `BA` | `P22` | PATIENT | MALE | 01/05/1953 | 167 | K1 | 50.1 s | paciente levodopa 5pm |
| 23 | `20260626141246_temp_AC.json` | `AC` | `P23` | PATIENT | FEMALE | 09/04/1952 | 148 | Base | 53.8 s | paciente. amantadina, 4.30am |
| 24 | `20260626144433_temp_AV.json` | `AV` | `P24` | PATIENT | MALE | 04/06/1947 | 165 | Base | 73.2 s | paciente. levodopa 8:30 |
| 25 | `20260626145512_temp_AO.json` | `AO` | `P25` | PATIENT | FEMALE | 24/07/1953 | 166 | K1 | 76.5 s | levodopa. 7am |
| 26 | `20260626150532_temp_M.json` | `M` | `P26` | PATIENT | FEMALE | 31/01/1946 | 172 | Base | 82.0 s | levodopa. 9pm día anterior |
| 27 | `20260626151711_temp_BQ.json` | `BQ` | `P27` | PATIENT | FEMALE | 12/02/1976 | 154 | K1 | 70.9 s | levodopa, 8am |
| 28 | `20260626152553_temp_U.json` | `U` | `P28` | PATIENT | MALE | 03/07/1979 | 170 | Base | 41.6 s | paciente, diagnosticado ayer |
| 29 | `20260626153637_temp_AJ.json` | `AJ` | `P29` | PATIENT | FEMALE | 22/11/1961 | 162 | Base | 49.2 s | paciente. levodopa 10am |
| 30 | `20260626154758_temp_O.json` | `O` | `P30` | PATIENT | FEMALE | 20/10/1953 | 163 | Base | 63.3 s | paciente, levodopa. 10am |
| 31 | `20260626160554_temp_BU.json` | `BU` | `P31` | PATIENT | FEMALE | 23/05/1959 | 158 | Base | 62.5 s | Dbs, paciente. levodopa 9am. |
| 32 | `20260626160620_temp_K.json` | `K` | `P31` | PATIENT | FEMALE | 23/05/1959 | 158 | Base | 19.6 s | Dbs, paciente. levodopa 9am. |
| 33 | `20260626170623_temp_BT.json` | `BT` | `P32` | PATIENT | MALE | 23/06/1955 | 166 | K1 | 89.7 s | paciente. No medicado |
| 34 | `20260626194407_temp_BM.json` | `BM` | `P33` | PATIENT | FEMALE | 05/10/1949 | 150 | K1 | 49.3 s | paciente, no toma levodopa. |
| 35 | `20260626202515_temp_BS.json` | `BS` | `P34` | PATIENT | MALE | 21/02/1957 | 157 | K1 | 133.7 s | paciente, levodopa, amantadina. 10am levo |
| 36 | `20260626204728_temp_AW.json` | `AW` | `P35` | PATIENT | MALE | 28/09/1960 | 171 | K1 | 38.4 s | levodopa, 10am, siguiente 4pm |
| 37 | `20260626211937_temp_AH.json` | `AH` | `P36` | PATIENT | MALE | 30/09/1958 | 165 | K1 | 51.0 s | paciente, amantadina, viperidel. tomado 12m |
| 38 | `20260626213214_temp_AT.json` | `AT` | `P37` | PATIENT | FEMALE | 06/12/1963 | 163 | K1 | 47.4 s | levodopa, 3pm, media de 250mg |
| 39 | `20260626215053_temp_AE.json` | `AE` | `P38` | PATIENT | FEMALE | 06/01/1969 | 157 | K1 | 46.0 s | paciente. no toma levodopa, tenía stalevo y amantadina. |
| 40 | `20260626222007_temp_BL.json` | `BL` | `P39` | PATIENT | MALE | 24/12/1966 | 173 | K1 | 66.8 s | levodopa, amantadina, mirapex. 2pm levo |
| 41 | `20260627133637_temp_AS.json` | `AS` | `P40` | PATIENT | MALE | 28/06/1950 | 167 | K1 | 48.5 s | paciente, levodopa 7am |
| 42 | `20260627135010_temp_BP.json` | `BP` | `P41` | PATIENT | MALE | 28/03/1982 | 170 | Base | 64.8 s | paciente levodopa, amantadina. 9am |
| 43 | `20260627135720_temp_AD.json` | `AD` | `P42` | PATIENT | MALE | 24/12/1972 | 165 | K1 | 73.7 s | paciente, levodopa 6am. |
| 44 | `20260627143518_temp_BB.json` | `BB` | `P43` | PATIENT | MALE | 03/05/1958 | 175 | K1 | 48.4 s | paciente, no medicado. |
| 45 | `20260627150939_temp_R.json` | `R` | `P44` | PATIENT | FEMALE | 30/01/1974 | 160 | K1 | 43.9 s | paciente. levodopa 6am |
| 46 | `20260627152358_temp_W.json` | `W` | `P45` | PATIENT | MALE | 18/01/1968 | 170 | K1 | 47.1 s | amantadina, vipiridene. 5am, 9am |
| 47 | `20260627155804_temp_I.json` | `I` | `P46` | PATIENT | MALE | 26/07/1967 | 175 | K1 | 41.1 s | paciente, levodopa 8am |
| 48 | `20260627161148_temp_Q.json` | `Q` | `P47` | PATIENT | MALE | 25/12/1971 | 165 | Base | 58.2 s | levodopa, 8am |
| 49 | `20260627162118_temp_AU.json` | `AU` | `P48` | PATIENT | MALE | 04/04/1954 | 182 | K1 | 77.1 s | paciente, levodopa 125, 10am / dbs activo |
| 50 | `20260627163836_temp_L.json` | `L` | `P49` | PATIENT | MALE | 23/08/1954 | 179 | Base | 56.5 s | paciente, no levodopa. DBS dos electrodos |
| 51 | `20260627171353_temp_H.json` | `H` | `P50` | PATIENT | MALE | 11/10/1976 | 175 | K1 | 39.4 s | levodopa, 10am |
| 52 | `20260627180847_temp_AI.json` | `AI` | `P51` | PATIENT | FEMALE | 04/12/1954 | 153 | K1 | 102.2 s | levodopa, 11am |
| 53 | `20260627205326_temp_C.json` | `C` | `P52` | PATIENT | FEMALE | 17/02/1979 | 153 | K1 | 43.2 s | paciente, 3:30pm |
| 54 | `20260704154505_temp_AF.json` | `AF` | `P53` | PATIENT | MALE | 28/03/1963 | 173 | Base | 44.2 s | paciente, levodopa 6:30am |
| 55 | `20260704155929_temp_BE.json` | `BE` | `P54` | PATIENT | MALE | 28/05/1963 | 163 | Base | 40.5 s | paciente, levodopa, 6am |
| 56 | `20260704165749_temp_E.json` | `E` | `P55` | PATIENT | MALE | 17/12/1985 | 180 | Base | 39.3 s | Sin observaciones |
| 57 | `20260704172020_temp_Y.json` | `Y` | `P56` | PATIENT | MALE | 21/09/1968 | 170 | Base | 42.0 s | Por confirmar |
| 58 | `20260704194015_temp_AY.json` | `AY` | `P57` | CONTROL | FEMALE | 23/06/1965 | 165 | Base | 31.3 s | Sin observaciones |
| 59 | `20260704194635_temp_BG.json` | `BG` | `P58` | PATIENT | MALE | 19/10/1971 | 175 | Base | 68.1 s | paciente, levodopa 6am |
| 60 | `20260715052203_temp_B.json` | `B` | `P59` | CONTROL | FEMALE | 03/07/1962 | 147 | K1 | 26.0 s | Control |
| 61 | `20260820141830_temp_AM.json` | `AM` | `P60` | PATIENT | MALE | 04/04/1960 | 158 | K1 | 43.3 s | Sin observaciones |
| 62 | `20260820141849_temp_P.json` | `P` | `P61` | CONTROL | FEMALE | 03/02/1962 | 159 | K1 | 46.3 s | Sin observaciones |
| 63 | `20260820141919_temp_BI.json` | `BI` | `P62` | PATIENT | FEMALE | 18/04/1964 | 160 | K1 | 54.5 s | Por confirmar |
| 64 | `20260820142005_temp_Z.json` | `Z` | `P63` | PATIENT | MALE | 14/01/1943 | 160 | K1 | 57.2 s | Levodopa Día anterior 12 pm |
| 65 | `20260820142037_temp_T.json` | `T` | `P64` | CONTROL | FEMALE | 11/08/1956 | 150 | K1 | 24.6 s | Sin observaciones |
| 66 | `20260820142101_temp_AN.json` | `AN` | `P65` | CONTROL | FEMALE | 08/11/1963 | 158 | K1 | 65.3 s | Por confirmar diagnóstico |

---
*Ficha técnica oficial de datos inerciales (IMUs) — Control de calidad y trazabilidad.*