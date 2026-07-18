<div align="center">

# Prediccion de Costos Medicos

## MediCare Plus — Aseguradora de Salud

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Pandas](https://img.shields.io/badge/Pandas-2.0-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![NumPy](https://img.shields.io/badge/NumPy-1.24-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](https://opensource.org/licenses/MIT)



**Un modelo de Machine Learning para predecir costos medicos anuales, optimizar primas y mejorar la rentabilidad de la cartera de clientes.**

[Dataset](#dataset) | [Objetivo del Negocio](#objetivo-del-negocio) | [Resultados Esperados](#resultados-esperados) | [Instalacion](#instalacion-y-uso) | [Contribuir](#contribuciones)

</div>

## Tabla de Contenidos

- [Descripcion del Proyecto](#descripcion-del-proyecto)
- [Objetivo del Negocio](#objetivo-del-negocio)
- [Dataset](#dataset)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instalacion y Uso](#instalacion-y-uso)
- [Resultados Esperados](#resultados-esperados)
- [Roadmap](#roadmap)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)
- [Autor](#autor)

## Descripcion del Proyecto

Este proyecto desarrolla un modelo de **Regresion Lineal Multiple** para predecir los costos medicos anuales (`charges`) de los asegurados de **MediCare Plus**. A partir de variables demograficas y habitos de salud, el modelo permite:

| Fijacion precisa de primas personalizadas | Identificacion temprana de clientes de alto riesgo | Optimizacion de la rentabilidad de la cartera |
|:------------------------------------------:|:---------------------------------------------------:|:----------------------------------------------:|

El proyecto sigue las mejores practicas de MLOps: pipeline de preprocesamiento reproducible, serializacion de modelos con `joblib`, y experimentacion documentada en Jupyter Notebooks.



## Objetivo del Negocio

### Contexto

Como Cientifico de Datos en **MediCare Plus**, una aseguradora de salud lider en el mercado, se nos ha encomendado el desarrollo de un modelo predictivo que estime los costos medicos anuales de nuestros asegurados en funcion de sus caracteristicas demograficas y habitos de salud.

### Problema

Las primas actuales se calculan con criterios genericos que **no reflejan adecuadamente los factores de riesgo individuales**, generando tres consecuencias criticas:

| Consecuencia | Impacto |
|:-------------|:--------|
| Perdidas economicas | Clientes de alto riesgo mal evaluados generan siniestros que superan la prima cobrada |
| Primas injustas | Clientes de bajo riesgo pagan de mas, creando insatisfaccion y riesgo de fuga |
| Desventaja competitiva | La competencia atrae a nuestros mejores clientes con ofertas mas ajustadas a su perfil |

### Solucion

Un modelo de **Regresion Lineal** que:

1. Calcule primas personalizadas y justas basadas en el perfil real de cada asegurado
2. Identifique clientes de alto riesgo para disenar programas preventivos y de bienestar
3. Optimice la rentabilidad de la cartera equilibrando riesgo y competitividad



## Dataset

**Medical Cost Personal Dataset** — [Descargar de Kaggle](https://www.kaggle.com/mirichoi0218/insurance)

El conjunto de datos contiene **1,338 registros** con 7 columnas que capturan informacion demografica y de salud de los asegurados, junto con su costo medico anual facturado.

### Diccionario de Datos

| Columna | Tipo | Descripcion | Rango / Valores |
|:--------|:-----|:------------|:----------------|
| `age` | Numerica | Edad del beneficiario principal | 18 – 64 anos |
| `sex` | Categorica | Genero del asegurado | `male`, `female` |
| `bmi` | Numerica | Indice de Masa Corporal | 15.96 – 53.13 |
| `children` | Numerica | Numero de hijos/dependientes cubiertos | 0 – 5 |
| `smoker` | Categorica | El asegurado es fumador? | `yes`, `no` |
| `region` | Categorica | Region geografica de residencia | `southwest`, `southeast`, `northwest`, `northeast` |
| `charges` | Numerica | **Target:** Costo medico anual facturado | $1,121 – $63,770 |

### Estadisticas Descriptivas

| Variable | Media | Mediana | Desv. Est. | Min | Max |
|:---------|:-----:|:-------:|:----------:|:---:|:---:|
| age | 39.2 | 39.0 | 14.0 | 18 | 64 |
| bmi | 30.7 | 30.4 | 6.1 | 15.96 | 53.13 |
| children | 1.09 | 1.0 | 1.20 | 0 | 5 |
| charges | $13,270 | $9,382 | $12,110 | $1,121 | $63,770 |



## Estructura del Proyecto

```
MedicalCostPrediction/
│
├── data/
│   ├── raw/                    # Datos originales (insurance.csv)
│   └── processed/              # Datos preprocesados listos para modelado
│
├── models/                     # Modelos entrenados y pipelines (.pkl / .joblib)
│
├── notebooks/                  # Jupyter Notebooks
│   ├── 01_EDA.ipync           # Analisis exploratorio de datos
│   ├── 02_Modeling.ipynb      # Entrenamiento y validacion del modelo
│   └── 03_Evaluation.ipynb    # Evaluacion y metricas finales
│
├── requirements.txt            # Dependencias del proyecto
├── LICENSE                     # Licencia MIT
└── README.md                   # Documentacion del proyecto
```



## Tecnologias Utilizadas

| Tecnologia | Version | Proposito |
|:-----------|:-------:|:----------|
| Python | 3.9+ | Lenguaje principal |
| Pandas | 2.0+ | Manipulacion y analisis de datos |
| NumPy | 1.24+ | Computo numerico |
| Matplotlib | 3.6+ | Visualizacion de datos |
| Seaborn | 0.12+ | Visualizacion estadistica |
| scikit-learn | 1.3+ | Preprocesamiento, pipelines y modelado |
| Joblib | 1.2+ | Serializacion de modelos |
| Jupyter | — | Entorno interactivo de desarrollo |



## Instalacion y Uso

### Prerrequisitos

- Python 3.9 o superior
- Git
- (Opcional) Entorno virtual

### Pasos de Instalacion

```bash
# 1. Clonar el repositorio
git clone https://github.com/MHAlberto/MedicalCostPrediction.git
cd MedicalCostPrediction

# 2. Crear y activar entorno virtual
python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate

# 3. Instalar dependencias
pip install --upgrade pip
pip install -r requirements.txt

# 4. Descargar el dataset
# Coloca insurance.csv en data/raw/

# 5. Iniciar Jupyter Notebook
jupyter notebook
```

> Nota: Los notebooks estan numerados para seguir el flujo de trabajo: `01_EDA` → `02_Modeling` → `03_Evaluation`.



## Resultados Esperados

Tras un preprocesamiento adecuado (escalado de variables numericas, codificacion *one-hot* de categoricas, y transformacion logaritmica de la variable objetivo para normalizar su distribucion), el modelo de Regresion Lineal deberia alcanzar las siguientes metricas:

| Metrica | Valor Esperado | Interpretacion |
|:--------|:--------------:|:---------------|
| **R²** (Coeficiente de determinacion) | **> 0.75** | El modelo explica mas del 75% de la varianza en costos medicos |
| **MAE** (Error Absoluto Medio) | **< $2,500** | El error promedio de prediccion es menor a $2,500 USD |
| **RMSE** (Raiz del Error Cuadratico Medio) | **< $4,000** | Penaliza errores grandes; indica robustez del modelo |

### Impacto de Negocio Esperado

```
Modelo R² > 0.75  →  Segmentacion precisa de riesgos
                          ├── Primas personalizadas  →  Retencion de clientes
                          │                         →  Competitividad en el mercado
                          └── Programas preventivos  →  Reduccion de siniestralidad
                                                      →  Rentabilidad general
```


## Roadmap

- [x] Definicion del problema de negocio
- [x] Adquisicion y analisis exploratorio de datos
- [ ] Entrenamiento del modelo de Regresion Lineal
- [ ] Evaluacion y validacion cruzada
- [ ] Optimizacion de hiperparametros
- [ ] Implementacion de pipeline completo
- [ ] Despliegue del modelo (API REST)



## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto:

1. Haz un **fork** del repositorio
2. Crea una rama con tu feature:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
3. Realiza tus cambios y haz commit:
   ```bash
   git commit -m 'feat: agrega nueva funcionalidad'
   ```
4. Sube tu rama:
   ```bash
   git push origin feature/nueva-funcionalidad
   ```
5. Abre un **Pull Request** describiendo tus cambios

> Asegurate de que tu codigo sigue las convenciones del proyecto e incluye pruebas cuando sea relevante.



## Licencia

Este proyecto esta bajo la licencia **MIT**. Consulta el archivo [`LICENSE`](./LICENSE) para mas detalles.

```
MIT License
Copyright (c) 2026 Mario H. Alberto
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...
```



## Autor

<div align="center">

**Mario H. Alberto**  
*Data Scientist & Machine Learning Engineer*

[GitHub](https://github.com/MHAlberto)

</div>



## Agradecimientos

- **Kaggle** por proporcionar el Medical Cost Personal Dataset.
- **Equipo de MediCare Plus** por la definicion del problema de negocio y el acompanamiento en el proyecto.
- Comunidad **open-source** por las herramientas que hacen posible este trabajo.



<div align="center">

**Hecho con ❤️ y Python**  
*Predicting health, improving lives.*

</div>
