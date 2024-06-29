import pandas as pd

class CrimeAnalytics:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def calculate_means(self): #Calcular los valores medios de las columnas de víctimas por año y delito.
        means_per_crime = self.dataframe.groupby(['anio', 'codigo_delito']).agg({
            'cantidad_victimas_masc': 'mean',
            'cantidad_victimas_fem': 'mean',
            'cantidad_victimas_sd': 'mean'
        }).reset_index()
        return means_per_crime

    def calculate_sum_victimas_por_anio(self): #Calcular la suma de víctimas por año y delito.
        sum_victimas_por_anio = self.dataframe.groupby(['anio', 'codigo_delito']).agg({
            'cantidad_victimas_totales': 'sum'
        }).reset_index()
        return sum_victimas_por_anio

    def calculate_sum_hechos_por_anio(self): #Calcular la suma de hechos por año y delito.
        sum_hechos_por_anio = self.dataframe.groupby(['anio', 'codigo_delito']).agg({
            'cantidad_hechos': 'sum'
        }).reset_index()
        return sum_hechos_por_anio
