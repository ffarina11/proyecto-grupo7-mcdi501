#  Proyecto Grupo 7 — MCDI501
### *Predicción de la deserción y el éxito académico de los estudiantes*

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Jupyter-Lab-orange?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter">
  <img src="https://img.shields.io/badge/Curso-MCDI500-green?style=for-the-badge" alt="MCDI501">
</p>

---

##  Descripción

Este repositorio contiene el proyecto transversal del curso **MCDI500 — Programación para la ciencia de datos** del **Magíster en Ciencias de Datos e Inteligencia Artificial** de la *Universidad Andrés Bello (UNAB)*.

El objetivo principal de esta investigación es analizar el **Student Performance Dataset** [(Cortez & Silva, 2008)](https://archive.ics.uci.edu/dataset/320/student+performance) para identificar y evaluar qué factores socioeconómicos y de preparación previa explican de mejor manera las diferencias en el rendimiento académico entre estudiantes de dos establecimientos educacionales portugueses.

---

=======
Este repositorio contiene el proyecto transversal del curso **MCDI501: Estadística Computacional para la Toma de Decisiones** del **Magíster en Ciencias de Datos e Inteligencia Artificial** de la *Universidad Andrés Bello (UNAB)*.

El objetivo principal de esta investigación es analizar el **Predict Students' Dropout and Academic Success (UCI, 2021)** 


##  Integrantes — Grupo 7

| Nombre | Rol | GitHub / Contacto |
| :--- | :---: | :---: |
| **Juan de Dios Díaz Ríos** | Integrante | [@juandiazr513](https://github.com/juandiazr513) |
| **Francisco Fariña Molina** | Integrante | [@ffarina11](https://github.com/ffarina11)|
| **Constanza Moreno Giacometto** | Integrante | [@ConstanzaM0](https://github.com/ConstanzaM0) |
| **Yenne Sepúlveda Jerez** | Integrante | [@yennesepulveda](https://github.com/yennesepulveda) |


* **Docente:** Jean Paul Maidana


##  Estructura del Repositorio

```text
proyecto-grupo7-mcdi501/
├── 📂 data/
│   ├── 📂 raw/                      # Datos originales sin modificar 
│   │   ├── data_original.csv
│   ├── 📂 processed/ 
│        ├── data_predict_binario.csv      # Dataset binarizado (Graduate vs Dropout) 
├── 📂 notebooks/
│   ├── S1_Predict_v4_formativa.ipynb                        # Definición del problema
│   ├── S1_abandono_academico_grupo_7.ipynb                  # Análisis Exploratorio e Inferencial
├── 📂 src/                        # Scripts reutilizables
│   ├── functions.py               # Pipeline funcional 
│   ├── librerias.py              
├── 📂 docs/                       # Documentación complementaria e informes
├── 📄 .gitignore                  # Archivos ignorados por Git
├── 📄 README.md                   # Descripción general del proyecto
└── 📄 requirements.txt            # Dependencias del entorno de desarrollo
```

---

##  Cómo Reproducir el Entorno

Sigue estos pasos en tu terminal (por ejemplo, **Git Bash**) para clonar el repositorio e instalar todas las dependencias necesarias:

### 1. Clonar el repositorio
```bash
git clone https://github.com/ffarina11/proyecto-grupo7-mcdi501
cd proyecto-grupo7-mcdi501
```

### 2. Configurar el entorno virtual
```bash
# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual
# En Windows (Git Bash):
source .venv/Scripts/activate

# En macOS/Linux:
source .venv/bin/activate
```

### 3. Instalar dependencias e iniciar
```bash
# Actualizar pip e instalar librerías
pip install --upgrade pip
pip install -r requirements.txt

# Abrir el entorno de Jupyter
jupyter lab
```

## Preparación de Datos

Para el desarrollo del proyecto se realizó la preparación inicial del conjunto de datos con el objetivo de asegurar su correcta carga y posterior análisis estadístico.

### 1. Descarga de datos

El conjunto de datos original se obtuvo desde el **UCI Machine Learning Repository**:

- `data_original.csv` (*Predict Students' Dropout and Academic Success*)

Se almacenó en:

```text
data/raw/
```

### 2. Carga y organización inicial

- El dataset se carga utilizando **pandas**, preservando el archivo original sin modificaciones.
- Se verifica la estructura del conjunto de datos mediante la inspección de dimensiones, tipos de variables y estadísticas descriptivas básicas.
- La variable objetivo se binariza conservando únicamente las clases **Graduate** y **Dropout**, eliminando los registros correspondientes a **Enrolled**.
- El conjunto de datos procesado se exporta para su utilización en las etapas posteriores del análisis.

### 3. Validación inicial

Como parte de la preparación de datos se realizaron las siguientes verificaciones:

- Inspección de valores faltantes.
- Identificación de registros duplicados.
- Revisión de tipos de datos y conversión de variables al formato adecuado (`category`, `int` y `float`).
- Verificación de la distribución de la variable objetivo.

Los datos procesados se almacenan en:

```text
data/processed/
├── data_predict_binario.csv      # Dataset binarizado (Graduate vs Dropout)
```

> **Nota:** El dataset original permanece sin modificaciones en `data/raw/`, garantizando la reproducibilidad del proceso de preparación de datos.

---

## Análisis Exploratorio de Datos

El análisis exploratorio tuvo como propósito comprender la estructura del conjunto de datos e identificar patrones asociados al abandono académico antes de realizar el análisis inferencial.

### 1. Análisis descriptivo

Se obtuvieron estadísticas descriptivas para las variables:

- Cuantitativas continuas.
- Cuantitativas discretas.
- Cualitativas nominales.
- Cualitativas ordinales.

### 2. Análisis gráfico

Se generaron distintas visualizaciones para caracterizar el comportamiento de las variables, entre ellas:

- Histogramas.
- Diagramas de caja (boxplots).
- Gráficos de barras.
- Matriz de correlación para variables numéricas.

Las visualizaciones permitieron comparar el comportamiento de las variables entre los estudiantes que **desertan** y aquellos que **se gradúan**.

### 3. Detección de valores atípicos

Se evaluó la presencia de valores atípicos mediante el criterio del rango intercuartílico (IQR). Debido a que corresponden a observaciones plausibles dentro del contexto académico, estos registros fueron conservados para el análisis posterior.

---

## Estimación de Parámetros

Se realizaron procedimientos de inferencia estadística para estimar parámetros poblacionales asociados al rendimiento y abandono académico.

Las principales estimaciones incluyeron:

- Estimación puntual de medias para variables numéricas de interés.
- Construcción de intervalos de confianza del 95 % para medias poblacionales.
- Estimación de la proporción de estudiantes que abandonan sus estudios mediante intervalos de confianza para proporciones.

Estas estimaciones permiten cuantificar la incertidumbre de los principales indicadores analizados.

---

## Pruebas de Hipótesis

Finalmente, se aplicaron pruebas de hipótesis con el objetivo de evaluar diferencias y asociaciones entre las variables del estudio y la condición académica del estudiante.

Se realizaron las siguientes pruebas:

- Verificación de supuestos de normalidad y homogeneidad de varianzas.
- Prueba **t de Welch** para comparar medias entre estudiantes **Graduate** y **Dropout**.
- Pruebas **Chi-cuadrado de independencia** para analizar la asociación entre variables categóricas y la variable objetivo.

Los resultados obtenidos permiten identificar las variables con evidencia estadística de asociación con el abandono académico y el éxito estudiantil.

##  Información del Dataset

| Atributo | Detalle |
| :--- | :--- |
| **Nombre** | Predict Students' Dropout and Academic Success |
| **Fuente** | UCI Machine Learning Repository |
| **Autores** | Realinho, V., Vieira Martins, M., Machado, J., & Baptista, L. (2021) |
| **URL Oficial** | [🔗 Acceder al Dataset](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success) |
| **Archivos Incluidos** | `data_original.csv` |
| **Dimensiones** | 4.424 registros y 37 variables demográficas, socioeconómicas, académicas y macroeconómicas |

---
<p align="center"><sub>Magíster en Ciencias de Datos e Inteligencia Artificial • UNAB • 2026</sub></p>