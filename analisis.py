class Analisis:
    def __init__(self, datos):
        self.datos = datos

    def calcular_medias_delitos_totales_por_año(self):
        # Calcula la suma de la cantidad de delitos totales por año utilizando el método groupby, puede ser usada más adelante
        delitos_totales_por_año = self.datos.groupby('anio')['cantidad_hechos'].sum()
        return delitos_totales_por_año
    
    def calcular_medias_por_año(self):
        # Calcula la media de la cantidad de delitos por año utilizando el método groupby, puede ser usada más adelante
        medias_por_año = self.datos.groupby('anio')['cantidad_hechos'].mean()
        return medias_por_año
    
    def comparar_victimas_por_delito(self, delito_seleccionado):
        # Filtra los datos para el delito seleccionado y luego agrupa por año, sumando las víctimas masculinas y femeninas
        datos_delito = self.datos[self.datos['codigo_delito'] == delito_seleccionado]
        return datos_delito.groupby('anio')[['cantidad_victimas_masc', 'cantidad_victimas_fem']].sum()
