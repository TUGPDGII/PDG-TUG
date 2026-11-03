# Análisis de Datos de la Prueba TUG en Pacientes con Enfermedad de Parkinson (PDG-TUG)

**Universidad ICESI**  
*Ingeniería Telemática e Ingeniería de Sistemas*  
**Proyecto de Grado**

---

## 📌 Resumen del Proyecto

Este proyecto está enfocado en la adquisición, procesamiento y análisis de datos de sensores inerciales (**IMU**) capturados durante la realización de la prueba **Timed Up and Go (TUG)**. El objetivo principal es extraer **variables espaciotemporales** significativas de la marcha y la movilidad corporal para asistir en la clasificación, caracterización y evaluación biomecánica de pacientes con **Enfermedad de Parkinson (EP)** en comparación con un grupo de control.

La prueba **TUG** consiste en evaluar el tiempo y la cinemática de un individuo al levantarse de una silla, caminar una distancia de 3 metros, girar 180°, regresar a la silla y sentarse de nuevo. Los datos recolectados permiten analizar distintas fases del movimiento mediante técnicas de procesamiento de señales y modelos de aprendizaje automático (*Machine Learning*).

---

## 📂 Estructura del Repositorio

```text
PDG-TUG-V2/
├── Analisis de Datos/            # Código de exploración, clasificación y procesamiento
│   ├── PDGI_Colab.ipynb          # Notebook de análisis con pipeline de procesamiento de señales
│   ├── PDGI_Colab copy.ipynb     # Cuaderno actualizado con equivalencia al predecesor y módulos 1 a 9
│   ├── Datos_IMUs.csv            # Metadatos clínicos y anonimización de las 78 grabaciones IMU
│   ├── Datos_eMotion.csv         # Metadatos del dataset de cámaras y pose esquelética
│   ├── df_variables_tug.csv      # Biomarcadores cinemáticos y temporales calculados (66 válidos)
│   ├── Analisis_IMUs.md          # Auditoría técnica exhaustiva de datos inerciales
│   ├── Analisis_eMotion.md       # Evaluación de capturas de video y pose esquelética
│   ├── FichaTecnica_IMUs.md      # Ficha técnica oficial de control de calidad IMU (descartes y aceptados)
│   ├── FichaTecnica_eMotion.md   # Ficha técnica y delimitación de alcance de cámaras
│   └── Correlacion.md                 # Trazabilidad temporal IMU frente a e-Motion
├── Datos IMUs/                   # Grabaciones en formato JSON de las sesiones de pruebas TUG
│   └── *.json                    # Lecturas de acelerometría y giroscopio (~50 Hz) de 5 sensores IMU
├── Datos e-Motion/               # Grabaciones de cámaras RGB-D y articulaciones esqueléticas
├── Notas_Reuniones/              # Minutas y notas de avance de las reuniones de seguimiento
├── OverLeaf/                     # Fuentes LaTeX y compilación del documento académico (PDFs, .tex)
└── README.md                     # Este archivo
```

---

## ⚙️ Características de los Datos

* **Sensores IMU**: 5 sensores colocados en posiciones estratégicas (`L5/Espalda Baja`, `Tobillo Izquierdo`, `Tobillo Derecho`, `Mano Izquierda`, `Mano Derecha`).
* **Variables registradas**: Acelerometría (g) y Giroscopio (°/s) muestreados a frecuencia de ~50 Hz.
* **Sujetos de prueba**: Registros correspondientes a pacientes con Enfermedad de Parkinson y sujetos del grupo Control.

---

## 👥 Equipo del Proyecto

### Autores
* Juan José Arias Gallego
* Esteban Guarin Valencia
* Santiago Gómez Robledo
* Heiner Danit Rincón Carrillo

### Tutores
* Domiciano Rincón
* Andrés Navarro
