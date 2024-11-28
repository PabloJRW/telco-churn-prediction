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
- K Nearest Neighbors

Se ha evaluado el rendimiento de los modelos utilizando métricas como la precisión, la exactitud, el recall y la F1-score.
Aunque prioricé el recall (sensibilidad) sobre las otras métricas, debido a que es más importante identificar la mayor cantidad posible de clientes en riesgo de abandonar, incluso si implica algunos falsos positivos.

## Tecnologías Utilizadas

- **Lenguaje de Programación**: Python
- **Librerías y Frameworks**:
  - `pandas`: para el procesamiento y análisis de datos.
  - `numpy`: para manipulación numérica.
  - `scipy`: para el análisis estadístico.
  - `matplotlib` y `seaborn`: para visualización de datos.
  - `scikit-learn`: para modelos de Machine Learning y evaluación.
  - `xgboost`: para el modelo XGBoost.
- **Entorno de Desarrollo**:
  - Jupyter Notebooks para la implementación interactiva.
  - Git para el control de versiones.

## Estructura del Proyecto

```bash
telco-churn-prediction
├── datasets/
│   ├── raw                          # Datos originales
│   └── prepared_data                # Datos procesados
├── img/                             # Imágenes 
├── notebooks/
│   ├── 1-EDA.ipynb                  # Análisis exploratorio de datos
│   ├── 2-data_preparation.ipynb     # Preparación de los datos
│   ├── 3-evaluating_model_scores    # Probando rendimiento de modelos
│   ├── 4-pca.ipynb                  # Reducción de dimensionalidad
│   ├── 5-evaluating_after_pca.ipynb     # Probando rendimietos de modelos después de PCA
│   ├── 6-0-evaluating_random_forest.ipynb           
│   ├── 6-1-evaluating_xgboosting.ipynb
│   ├── 6-2-evaluating_knn.ipynb
│   ├── 6-3-evaluating_logistic_regression.ipynb
│   ├── 6-4-evaluating_naive_bayes.ipynb
│   └── 6-5-voting-classifier.ipynb
├── trained_models/                  # Modelos entrenados
│   ├── knn.joblib
│   ├── naive_bayes.joblib
│   ├── random_forest.joblib
│   ├── xgboosting.joblib          
│   └── logistic_regression.joblib           
├── requirements.txt                # Dependencias del proyecto
├── README.md                       # Documentación del proyecto
```

## Instalación
Sigue estos pasos para instalar las dependencias y configurar el entorno de desarrollo.
1. Clona este repositorio:
```bash
git clone git@github.com:PabloJRW/telco-churn-prediction.git
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
Los modelos entrenados fueron evaluados usando diversas métricas de rendimiento, y los resultados mostraron que el modelo Naive Bayes logró el mejor rendimiento en cuanto a recall. A continuación, se presentan algunas métricas clave:

* Naive Bayes:
  * Precisión: 0.47
  * Recall: 0.82
  * F1-score: 0.60
    
* Regresión Logística:
  * Precisión: 0.50
  * Recall: 0.77
  * F1-score: 0.61

* Random Forest:
  * Precisión: 0.55
  * Recall: 0.75
  * F1-score: 0.63

* XGBoost:
  * Precisión: 0.55
  * Recall: 0.74
  * F1-score: 0.63
 
* K Nearest Neighbors:
  * Precisión: 0.48
  * Recall: 0.69
  * F1-score: 0.57

* Voting Classifier:
  * Precisión: 0.52
  * Recall: 0.78
  * F1-score: 0.62


 ## Conclusión
Este proyecto demuestra cómo se pueden aplicar técnicas de Machine Learning para predecir el abandono de clientes, lo que permite a las empresas tomar decisiones informadas para retener a los clientes en riesgo. El modelo Naive Bayes fue el más efectivo, pero se pueden seguir mejorando los resultados con más datos y pruebas de diferentes técnicas.
