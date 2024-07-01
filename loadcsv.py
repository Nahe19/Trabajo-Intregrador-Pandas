import pandas as pd
import os

class DataLoader:
    def __init__(self, filepath):
        self.filepath = filepath
        try:
            self.df = pd.read_csv(filepath, delimiter=';', encoding='latin1')
            print(f"Archivo '{filepath}' cargado exitosamente.")
        except FileNotFoundError:
            print(f"Archivo '{filepath}' no encontrado.")
        except pd.errors.ParserError:
            print(f"Error al parsear el archivo '{filepath}'. Verifica el delimitador y la codificación.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")
    
    def load_data(self):
        return self.df
    
    def modify_csv(self, columna_para_remover=None, col1=None, col2=None, col3=None, nombre_columna_nueva=None, columna_objetivo=None, nombre_columna=None, nuevo_nombre=None, valor_relleno=0):
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
    
    def borrar_columna(self, columna_para_remover):
        if columna_para_remover in self.df.columns:
            self.df.drop(columns=[columna_para_remover], inplace=True)
            print(f"Columna '{columna_para_remover}' eliminada.")
        else:
            print(f"Columna '{columna_para_remover}' no encontrada.")
    
    def rellenar_na(self, valor_relleno=0):
        self.df.fillna(valor_relleno, inplace=True)
        print("Valores NA rellenados.")
    
        for col in self.df.select_dtypes(include=['float']).columns:
            if self.df[col].apply(float.is_integer).all():
                self.df[col] = self.df[col].astype(int)
        print("Columnas numéricas convertidas a enteros si es aplicable.")
    
    def crear_columna(self, col1, col2, col3, nombre_columna_nueva):
        if col1 in self.df.columns and col2 in self.df.columns and col3 in self.df.columns:
            self.df[nombre_columna_nueva] = self.df[col1] + self.df[col2] + self.df[col3]
            print(f"Columna '{nombre_columna_nueva}' creada sumando '{col1}', '{col2}' y '{col3}'.")
        else:
            print("Alguna de las columnas no fue encontrada.")
    
    def mover_columna(self, nombre_columna_nueva, columna_objetivo):
        columns = list(self.df.columns)
        if columna_objetivo in columns:
            pos = columns.index(columna_objetivo) + 1
            columns.insert(pos, columns.pop(columns.index(nombre_columna_nueva)))
            self.df = self.df[columns]
            print(f"Columna '{nombre_columna_nueva}' movida después de '{columna_objetivo}'.")
        else:
            print(f"Columna de destino '{columna_objetivo}' no encontrada.")
    
    def renombrar_columna(self, nombre_columna, nuevo_nombre):
        if nombre_columna in self.df.columns:
            self.df.rename(columns={nombre_columna: nuevo_nombre}, inplace=True)
            print(f"Columna '{nombre_columna}' renombrada a '{nuevo_nombre}'.")
        else:
            print(f"Columna '{nombre_columna}' no encontrada.")
    
    def save_to_csv(self, output_filepath):
        try:
            self.df.to_csv(output_filepath, index=False, sep=';')
            print(f"Archivo guardado como '{output_filepath}'.")
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")

if __name__ == "__main__":
    folder_path = 'datos'  # Carpeta donde se encuentran los archivos
    filepath = os.path.join(folder_path, 'raw_datos.csv')
    output_filepath = os.path.join(folder_path, 'clean_data.csv')
    
    columna_para_remover = 'cantidad_victimas'
    col1 = 'cantidad_victimas_masc'
    col2 = 'cantidad_victimas_fem'
    col3 = 'cantidad_victimas_sd'
    nombre_columna_nueva = 'cantidad_victimas_totales'
    columna_objetivo = 'cantidad_hechos'
    nombre_columna = 'codigo_delito_snic_nombre'
    nuevo_nombre = 'codigo_delito'
    
    loader = DataLoader(filepath)
    
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
    
    loader.save_to_csv(output_filepath)
