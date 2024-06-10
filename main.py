from cargar_csv import CargarCSV
from analisis import Analisis
from histograma import Histograma

# Ruta del archivo CSV
ruta_archivo = "C:/Users/Nahe/Desktop/Proyecto Pandas 2/datos/raw_datos.csv"

# Cargar el CSV
cargador = CargarCSV(ruta_archivo)
datos = cargador.cargar_datos()

# Realizar análisis
analizador = Analisis(datos)

# Calcular medias de delitos totales por año
media_delitos_totales_por_año = analizador.calcular_medias_delitos_totales_por_año()

# Calcular medias de cantidad de hechos por año
medias_por_año = analizador.calcular_medias_por_año()

# Comparar víctimas por delito seleccionado
delito_seleccionado = "Homicidios dolosos"
datos_delito = analizador.comparar_victimas_por_delito(delito_seleccionado)

# Generar histograma de la media de delitos totales por año
histogramador = Histograma(datos)
histogramador.histograma_media_delitos_totales_por_año(media_delitos_totales_por_año)

# Generar histograma de la cantidad de homicidios dolosos por género y año
histogramador.histograma_homicidios_por_genero(datos_delito[["cantidad_victimas_masc", "cantidad_victimas_fem"]])

# Generar histograma de la cantidad de cada delito por año, utilizar como ejemplo porque son muchos
'''
delitos = datos['codigo_delito'].unique()
for delito in delitos:
    datos_delito = datos[datos['codigo_delito'] == delito]
    histogramador.histograma_delitos_por_año(datos_delito, delito)
'''

# Mostrar la media de delitos totales por año
print("Media de delitos totales por año:")
print(media_delitos_totales_por_año)
