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
        └── (temp_AZ, temp_J, temp_AQ — Paciente P17)
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
*Ficha técnica generada automáticamente por `generar_ficha_tecnica.py`.*
