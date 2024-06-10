import pandas as pd

class CargarCSV:
    def __init__(self, ruta):
        self.ruta = ruta

    def cargar_datos(self):
        #Acá cargamos los datos y especificamos la separación que tiene entre cada columna
        try:
            datos = pd.read_csv(self.ruta, sep=';')
            return datos
        except FileNotFoundError:
            print("El archivo no se encontró en la ruta especificada.")
            return None
