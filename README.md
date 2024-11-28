# Predicción de Abandono de Clientes

Este proyecto tiene como objetivo predecir la probabilidad de que un cliente abandone un servicio o producto utilizando técnicas de Machine Learning. El modelo entrenado identifica patrones y características que podrían indicar que un cliente está en riesgo de abandonar, lo que permite a las empresas tomar medidas preventivas.

## Tabla de Contenidos

- [Descripción](#descripción)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Instalación](#instalación)
- [Uso](#uso)
- [Resultados](#resultados)
- [Conclusión](#conclusión)
- [Licencia](#licencia)

## Descripción

El objetivo de este proyecto es predecir el abandono de clientes mediante el uso de datos históricos. El conjunto de datos incluye diversas variables como características del cliente (edad, contrato, método de pago, etc.) y las interacciones con la empresa.

Para resolver este problema, se han probado varios algoritmos de clasificación, tales como:

- Regresión logística
- Árboles de decisión
- Random Forest
- XGBoost

Se ha evaluado el rendimiento de los modelos utilizando métricas como la precisión, la exactitud, el recall y la F1-score.

## Tecnologías Utilizadas

- **Lenguaje de Programación**: Python
- **Librerías y Frameworks**:
  - `pandas`: para el procesamiento y análisis de datos.
  - `numpy`: para manipulación numérica.
  - `matplotlib` y `seaborn`: para visualización de datos.
  - `scikit-learn`: para modelos de Machine Learning y evaluación.
  - `xgboost`: para el modelo XGBoost.
- **Entorno de Desarrollo**:
  - Jupyter Notebooks para la implementación interactiva.
  - Git para el control de versiones.

## Estructura del Proyecto

```bash
.
├── data/
│   └── clientes.csv                # Datos de clientes (input)
├── notebooks/
│   └── predicción_abandono.ipynb   # Notebook con el análisis y entrenamiento del modelo
├── src/
│   ├── preprocessing.py            # Funciones para el procesamiento de datos
│   └── model.py                    # Código para entrenar y evaluar los modelos
├── requirements.txt                # Dependencias del proyecto
├── README.md                       # Documentación del proyecto
```

## Instalación
Sigue estos pasos para instalar las dependencias y configurar el entorno de desarrollo.
1. Clona este repositorio:
```bash
git clone https://github.com/usuario/repositorio.git
```
2. Navega al directorio del proyecto:
```bash
cd telco-churn-prediction
```
3. Crea un entorno virtual (opcional pero recomendado):
```bash
python -m venv venv
source venv/bin/activate  # En Linux/macOS
venv\Scripts\activate     # En Windows
```
4. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Uso
Para reproducir los experimentos y entrenar el modelo de predicción de abandono de clientes, sigue estos pasos:

1. Abre el archivo notebooks/predicción_abandono.ipynb en Jupyter Notebook.
2. Ejecuta las celdas secuenciales para cargar los datos, preprocesarlos, entrenar los modelos y evaluar el rendimiento.
3. O bien, si prefieres ejecutar el código desde la línea de comandos, puedes usar los scripts de Python dentro de la carpeta src:

## Resultados
Los modelos entrenados fueron evaluados usando diversas métricas de rendimiento, y los resultados mostraron que el modelo XGBoost logró el mejor rendimiento en cuanto a precisión y recall. A continuación, se presentan algunas métricas clave:

* Regresión Logística:
  * Precisión: 0.85
  * Recall: 0.80
  * F1-score: 0.82

* Random Forest:
  * Precisión: 0.88
  * Recall: 0.83
  * F1-score: 0.85

* XGBoost:
  * Precisión: 0.90
  * Recall: 0.87
  * F1-score: 0.88

 ## Conclusión
Este proyecto demuestra cómo se pueden aplicar técnicas de Machine Learning para predecir el abandono de clientes, lo que permite a las empresas tomar decisiones informadas para retener a los clientes en riesgo. El modelo XGBoost fue el más efectivo, pero se pueden seguir mejorando los resultados con más datos y pruebas de diferentes técnicas.
