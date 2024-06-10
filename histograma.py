import matplotlib.pyplot as plt

# Este script nos proporciona métodos para crear histogramas de manera organizada y reutilizable.

class Histograma:
    def __init__(self, datos):
        self.datos = datos

    def histograma_media_delitos_totales_por_año(self, delitos_totales_por_año):
        # Crea un histograma de la media de delitos totales por año
        ax = delitos_totales_por_año.plot(kind='bar')
        plt.xlabel('Año')
        plt.ylabel('Suma de Delitos Totales (Millones)')
        plt.title('Suma de Delitos Totales por Año')
        plt.show()
    
    def histograma_homicidios_por_genero(self, datos_delito):
        # Crea un histograma de la cantidad de homicidios dolosos por género y año
        ax = datos_delito.plot(kind='bar')
        ax.set_xlabel('Año')  # Cambia la etiqueta del eje x
        ax.set_ylabel('Cantidad de Homicidios Dolosos')  # Cambia la etiqueta del eje y
        ax.legend(['Hombres', 'Mujeres'], loc='upper right')  # Cambia las leyendas de los colores
        plt.title('Cantidad de Homicidios Dolosos por Género y Año')
        plt.show()
    
    def histograma_delitos_por_año(self, datos_delito, delito):
        # Crea un histograma de la cantidad de un delito específico por año
        ax = datos_delito.groupby('anio')['cantidad_hechos'].sum().plot(kind='bar')
        plt.xlabel('Año')
        plt.ylabel('Cantidad de ' + delito)
        plt.title('Cantidad de ' + delito + ' por Año')
        plt.show()
