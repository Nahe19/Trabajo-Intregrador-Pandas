import pandas as pd
import os

class DataLoader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.df = pd.read_csv(filepath, delimiter=';', encoding='latin1')

    def load_data(self):
        #Cargar el CSV como un dataframe de Pandas
        return self.df

    def modify_csv(self, columna_para_remover=None, col1=None, col2=None, col3=None, nombre_columna_nueva=None, columna_objetivo=None, nombre_columna=None, nuevo_nombre=None, valor_relleno=0):
        #Modificar el Dataframe
        if columna_para_remover:
            self.borrar_columna(columna_para_remover)

        if valor_relleno is not None:
            self.rellenar_na(valor_relleno)

        if col1 and col2 and col3 and nombre_columna_nueva:
            self.crear_columna(col1, col2, col3, nombre_columna_nueva)

        if nombre_columna_nueva and columna_objetivo:
            self.mover_columna(nombre_columna_nueva, columna_objetivo)

        if nombre_columna and nuevo_nombre:
            self.renombrar_columna(nombre_columna, nuevo_nombre)

    def borrar_columna(self, columna_para_remover): #Quitar una columna en especifico del Dataframe
        if columna_para_remover in self.df.columns:
            self.df.drop(columns=[columna_para_remover], inplace=True)
        else:
            print(f"Columna '{columna_para_remover}' no fué encontrada.")

    def rellenar_na(self, valor_relleno=0): #Completar las celdas vacias con un valor especifico
        self.df.fillna(valor_relleno, inplace=True)

        # Convertir columnas numéricas de float a int si los valores son enteros
        for col in self.df.select_dtypes(include=['float']).columns:
            if self.df[col].apply(float.is_integer).all():
                self.df[col] = self.df[col].astype(int)

    def crear_columna(self, col1, col2, col3, nombre_columna_nueva): #Crear una columna nueva con una especifica petición
        if col1 in self.df.columns and col2 in self.df.columns and col3 in self.df.columns:
            self.df[nombre_columna_nueva] = self.df[col1] + self.df[col2] + self.df[col3]
        else:
            print(f"Alguna de las columnas no fué encontrada.")

    def mover_columna(self, nombre_columna_nueva, columna_objetivo): #Mover una columna en especifico a una parte del Dataframe
        columns = list(self.df.columns)
        if columna_objetivo in columns:
            pos = columns.index(columna_objetivo) + 1
            columns.insert(pos, columns.pop(columns.index(nombre_columna_nueva)))
            self.df = self.df[columns]
        else:
            print(f"Target column '{columna_objetivo}' not found.")

    def renombrar_columna(self, nombre_columna, nuevo_nombre): #Renombrar una columna
        if nombre_columna in self.df.columns:
            self.df.rename(columns={nombre_columna: nuevo_nombre}, inplace=True)
        else:
            print(f"Column '{nombre_columna}' not found.")

    def save_to_csv(self, output_filepath): #Guardar el Dataframe en el nuevo CSV
        self.df.to_csv(output_filepath, index=False, sep=';')

if __name__ == "__main__":
    # Definir los parámetros
    filepath = 'raw_datos.csv'              # Path del archivo CSV original
    output_filepath = 'clean_data.csv'  # Path del archivo CSV modificado
    columna_para_remover = 'cantidad_victimas'     # Nombre de la columna a eliminar
    col1 = 'cantidad_victimas_masc'         # Primera columna para la suma
    col2 = 'cantidad_victimas_fem'          # Segunda columna para la suma
    col3 = 'cantidad_victimas_sd'           # Tercera columna para la suma
    nombre_columna_nueva = 'cantidad_victimas_totales'  # Nombre de la nueva columna creada
    columna_objetivo = 'cantidad_hechos'           # Nombre de la columna de destino para mover nombre_columna_nueva
    nombre_columna = 'codigo_delito_snic_nombre'  # Nombre de la columna actual
    nuevo_nombre = 'codigo_delito'               # Nuevo nombre para la columna
    
    # Crear una instancia de DataLoader
    loader = DataLoader(filepath)
    
    # Aplicar las modificaciones
    loader.modify_csv(
        columna_para_remover=columna_para_remover,
        col1=col1,
        col2=col2,
        col3=col3,
        nombre_columna_nueva=nombre_columna_nueva,
        columna_objetivo=columna_objetivo,
        nombre_columna=nombre_columna,
        nuevo_nombre=nuevo_nombre
    )
    
    # Guardar el DataFrame modificado en un nuevo archivo CSV
    loader.save_to_csv(output_filepath)
