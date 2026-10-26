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
│   ├── PDGI_Clasificación.ipynb  # Notebook con modelos de clasificación y pipeline de datos
│   ├── identificar_personas.py   # Script de identificación y agrupación de pacientes
│   ├── RESUMEN_DATOS.md          # Documentación detallada del estado de los datos recabados
│   └── personas.csv              # Dataset de pacientes anonimizados y metadatos
├── Datos IMUs/                   # Grabaciones en formato JSON de las sesiones de pruebas TUG
│   └── *.json                    # Lecturas de acelerometría y giroscopio (~50 Hz) de 5 sensores IMU
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
