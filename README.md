# Proyecto Pandas 

Este proyecto utiliza la biblioteca Pandas de Python para realizar análisis de datos criminales.

## Instrucciones de Uso

1. Clona este repositorio en tu máquina local.
2. Instala las dependencias necesarias ejecutando `pip install -r requirements.txt`.
3. Ejecuta el script `main.py` para cargar los datos, realizar análisis y generar visualizaciones.
4. Consulta los resultados en la consola o los archivos de visualización generados.

## Estructura del Proyecto

- **loadcsv.py**: Contiene la clase `DataLoader` para cargar datos desde un archivo CSV.
- **analytics.py**: Contiene la clase `CrimeAnalytics` para realizar análisis de datos.
- **datavisualizer.py**: Contiene la clase `DataVisualizer` para generar visualizaciones de datos en forma de histogramas.
- **main.py**: Script principal que carga los datos, realiza análisis y genera visualizaciones.
- **raw_datos.csv**: Archivo CSV que contiene los datos criminales.
- **clean_data.csv**: Archivo CSV que contiene los datos criminales.

## Dependencias

- pandas==1.3.3
- matplotlib==3.4.3
