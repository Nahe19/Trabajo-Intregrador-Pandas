# Proyecto Pandas

Este proyecto fue realizado en Python con las bibliotecas Pandas y Matplotlib para la Universidad Nacional de Almirante Brown. El objetivo principal no es solo analizar un dataset o archivo CSV, sino también mostrar cómo se pueden modificar, alterar y corregir un dataset para poder realizar o sacar conclusiones útiles. 
A continuación, mostraremos un pantallazo general y luego nos meteremos más a fondo en el código y cómo utilizarlo.

## Integrantes

- Nahuel Nicolas Alvarez
- Fabiana Valentina Gomez
- Alexander Molina
- Catalina Mozotegui

## Tecnologías Usadas

- Python
- Pandas
- Matplotlib

## Instrucciones de Uso

1. Clona este repositorio en tu máquina local.
    ```bash
    git clone https://github.com/Nahe19/Trabajo-Intregrador-Pandas.git
    ```
2. Instala las dependencias necesarias ejecutando:
    ```bash
    pip install -r requirements.txt
    ```
    O instala manualmente cada dependencia con:
    ```bash
    pip install pandas==1.3.3
    pip install matplotlib==3.4.3
    ```
3. Ejecuta el script `loadcsv.py` para cargar los datos, y modificar esos datos.
    ```bash
    python loadcsv.py
    ```
4. Ejecuta el script `main.py` para que se realicen todos los graficos correspondientes.
    ```bash
    python main.py
    ```

## Estructura del Proyecto

- **loadcsv.py**: Contiene la clase `DataLoader` para cargar datos desde un archivo CSV.
- **analytics.py**: Contiene la clase `CrimeAnalytics` para realizar análisis de datos.
- **datavisualizer.py**: Contiene la clase `DataVisualizer` para generar visualizaciones de datos en forma de histogramas.
- **main.py**: Script principal que carga los datos, realiza análisis y genera visualizaciones.
- **readme.md**: Archivo con documentación e información necesaria para comprender el script.
- **datos/raw_datos.csv**: Archivo CSV que contiene los datos sin regularizar.
- **datos/clean_data.csv**: Archivo CSV que contiene los datos ya arreglados.

## Descripción del Proyecto

Este proyecto tiene como objetivo principal analizar datos criminales y generar visualizaciones útiles para comprender patrones y tendencias. El flujo de trabajo del proyecto es el siguiente:

1. **Cargar Datos**: Utilizando la clase `DataLoader`, se cargan los datos desde el archivo `raw_datos.csv` en la carpeta `datos`.
2. **Limpiar y Procesar Datos**: Los datos se limpian y se guardan en `clean_data.csv` para asegurar que el análisis sea preciso.
3. **Análisis de Datos**: Con la clase `CrimeAnalytics`, se realizan diversos análisis sobre los datos limpios.
4. **Visualización de Datos**: Se generan histogramas y otras visualizaciones con la clase `DataVisualizer` para facilitar la interpretación de los datos.

## Dependencias

- pandas==1.3.3
- matplotlib==3.4.3

