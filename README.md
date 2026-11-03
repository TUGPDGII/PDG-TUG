# Análisis de Datos de la Prueba TUG en Pacientes con Enfermedad de Parkinson (PDG-TUG)

**Universidad ICESI**  
*Facultad de Ingeniería, Diseño y Ciencias Aplicadas*  
*Ingeniería Telemática e Ingeniería de Sistemas*  
**Proyecto de Grado**

---

## Resumen del Proyecto

Este proyecto está enfocado en la adquisición, acondicionamiento, segmentación y análisis biomecánico de datos cinemáticos capturados durante la realización de la prueba **Timed Up and Go (TUG)** y pruebas complementarias de marcha continua. El objetivo principal es extraer variables espaciotemporales cuantitativas y espectrales para asistir en la clasificación, caracterización funcional y evaluación de la movilidad corporal en pacientes con **Enfermedad de Parkinson (EP)** en contraste con participantes de control.

El sistema implementa una arquitectura de análisis bimodal:
1. **Unidades de Medición Inercial (IMUs):** Sensores triaxiales colocados en columna lumbar (L5) y extremidades (tobillos y muñecas) a 50 Hz, especializados en la detección de transiciones posturales (levantamiento y sentado), dinámica de giros cerrados de 180° y micro-fases de zancada (*Swing* / *Stance*).
2. **Cámaras Ópticas RGB-D (e-Motion / VIMOV):** Dispositivos de profundidad (Intel RealSense D455 y Orbbec Astra 2) a 30 Hz nominal, procesados mediante remuestreo monótono PCHIP, análisis espectral FFT y wavelets continuas (CWT Ricker) para la estimación de longitud de zancada, velocidad lineal de avance, porcentaje de doble apoyo y asimetría de braceo.

---

## Estructura del Repositorio

```text
PDG-TUG/
├── Analisis de Datos/            # Pipeline de procesamiento, modelado cinemático y documentación
│   ├── PDGI_Colab copy.ipynb     # Cuaderno principal interactivo en Google Colab (Módulos 1 a 13)
│   ├── PDGI_Colab.ipynb          # Cuaderno base de análisis exploratorio inicial
│   ├── Datos_IMUs.csv            # Inventario y metadatos clínicos de las 78 grabaciones IMU
│   ├── Datos_eMotion.csv         # Catálogo maestro de 12 metadatos clave para las 225 tomas e-Motion
│   ├── df_variables_tug.csv      # Matriz de biomarcadores cinemáticos inerciales (66 grabaciones válidas)
│   ├── df_variables_emotion.csv  # Matriz de 53 variables biomecánicas y clínicas ópticas (223 series)
│   ├── Analisis_IMUs.md          # Auditoría técnica e inferencial detallada del sistema inercial
│   ├── Analisis_eMotion.md       # Evaluación de calidad, segmentación y análisis biomecánico 3D
│   ├── Guia_Maestra_Pipeline_eMotion.md # Guía metodológica y conceptual del procesamiento óptico
│   ├── FichaTecnica_IMUs.md      # Ficha técnica oficial de control de calidad inercial
│   ├── FichaTecnica_eMotion.md   # Ficha técnica oficial del conjunto de datos ópticos (225 archivos)
│   ├── Correlacion.md            # Trazabilidad y validación bimodal (42 pares TUG confirmados)
│   └── Script/                   # Scripts de soporte, mapeos de renombramiento y resúmenes JSON
├── Datos IMUs/                   # Grabaciones inerciales en formato JSON (78 grabaciones)
│   └── *.json                    # Acelerometría y giroscopio triaxial (~50 Hz)
├── Datos e-Motion/               # Grabaciones de cámaras RGB-D y secuencias esqueléticas (225 archivos)
│   ├── TUG/                      # 130 grabaciones del protocolo Timed Up and Go (SMR, LAB, CST)
│   └── GAIT/                     # 95 grabaciones del protocolo de marcha continua de 10 m (SMR, CST)
├── Notas_Reuniones/              # Minutas de seguimiento técnico y metodológico
├── OverLeaf/                     # Manuscrito académico en LaTeX y figuras metodológicas
└── README.md                     # Documento principal del repositorio
```

---

## Características de los Datos y Sensores

### 1. Sistema Inercial (IMUs)
* **Sensores Utilizados:** 5 unidades IMU triaxiales (Acelerómetro ±16g, Giróscopo ±2000 °/s).
* **Topología Corporal:** `BASE-SPINE` (L5 / Sacro), `LEFT-ANKLE`, `RIGHT-ANKLE` (caras laterales externas de tobillos) como indispensables; `LEFT-HAND` y `RIGHT-HAND` como accesorios.
* **Frecuencia de Muestreo:** Nominal 50 Hz (remuestreada a cuadrícula uniforme de 50.0 Hz).
* **Hardware de Brigadas:** Kit Base (24 pruebas válidas) y Kit K1 con corrección de orientación (42 pruebas válidas).
* **Volumen:** 78 grabaciones (66 válidas para análisis clínico: 58 pacientes con EP y 8 controles).

### 2. Sistema Óptico (e-Motion / VIMOV)
* **Dispositivos:** Cámaras RGB-D Intel RealSense D455 / D455F y Orbbec Astra 2.
* **Frecuencia de Muestreo:** Nominal 30.0 Hz, acondicionada mediante interpolación hermítica monótona PCHIP y filtrado Butterworth paso bajas a 3.0 Hz de fase cero.
* **Topología Esquelética:** Esquemas de 19 articulaciones (`v1.2.0`, 75 archivos) y 15 articulaciones (`v1.3.0`, 148 archivos), con `SpineBase` como nodo articular pélvico universal.
* **Volumen:** 225 grabaciones físicas en disco (130 TUG y 95 Marcha Continua; 223 series cinemáticas articulares evaluadas).

### 3. Bimodalidad y Trazabilidad Temporal
* **Pares Bimodales Estrictamente TUG:** 42 parejas de registros (IMU + e-Motion) coincidentes en sujeto, protocolo TUG y ventana temporal ($|\Delta t| \le 360$ s).
* **Trazabilidad Intra-Sujeto en Cámara:** 48 pacientes evaluados de manera consecutiva tanto en prueba TUG como en marcha continua de 10 m.

---

## Equipo del Proyecto

### Autores
* Esteban Guarin Valencia
* Juan José Arias Gallego
* Santiago Gómez Robledo
* Heiner Danit Rincón Carrillo

### Tutores
* Prof. Domiciano Rincón
* Prof. Andrés Navarro
