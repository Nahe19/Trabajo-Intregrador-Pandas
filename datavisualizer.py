import matplotlib.pyplot as plt
import os
import re

class DataVisualizer:
    def __init__(self, means_per_crime, sum_victimas_por_anio, sum_hechos_por_anio, output_dir):
        self.means_per_crime = means_per_crime
        self.sum_victimas_por_anio = sum_victimas_por_anio
        self.sum_hechos_por_anio = sum_hechos_por_anio
        self.output_dir = output_dir

    def plot_histograms(self, victim_column, subfolder):
        crime_types = self.means_per_crime['codigo_delito'].unique()
        
        output_path = os.path.join(self.output_dir, 'histograma', subfolder)
        os.makedirs(output_path, exist_ok=True)
        
        for crime in crime_types:
            crime_data = self.means_per_crime[self.means_per_crime['codigo_delito'] == crime]
            
            if crime_data[victim_column].sum() > 0:
                plt.figure(figsize=(10, 6))
                plt.bar(crime_data['anio'], crime_data[victim_column], color='skyblue')
                plt.xlabel('Año')
                plt.ylabel(f'Número Medio de Víctimas {victim_column.split("_")[-1].capitalize()}')
                plt.title(f'Número Medio de Víctimas {victim_column.split("_")[-1].capitalize()} por Año para el Delito: {crime}')
                plt.xticks(crime_data['anio'], rotation=45)
                plt.tight_layout()
                safe_crime = re.sub(r'[^\w\s-]', '', crime).replace(' ', '_')
                plt.savefig(os.path.join(output_path, f'histogramas_{safe_crime}.png'))
                plt.close()

    def plot_comparison_histograms(self, subfolder):
        crime_types = self.means_per_crime['codigo_delito'].unique()

        output_path = os.path.join(self.output_dir, 'histograma', subfolder)
        os.makedirs(output_path, exist_ok=True)

        for crime in crime_types:
            crime_data = self.means_per_crime[self.means_per_crime['codigo_delito'] == crime]
            
            if crime_data['cantidad_victimas_masc'].sum() > 0 or crime_data['cantidad_victimas_fem'].sum() > 0 or crime_data['cantidad_victimas_sd'].sum() > 0:
                plt.figure(figsize=(10, 6))
                plt.bar(crime_data['anio'] - 0.2, crime_data['cantidad_victimas_masc'], width=0.2, label='Víctimas Masculinas', color='blue')
                plt.bar(crime_data['anio'] + 0.2, crime_data['cantidad_victimas_fem'], width=0.2, label='Víctimas Femeninas', color='pink')
                plt.bar(crime_data['anio'], crime_data['cantidad_victimas_sd'], width=0.2, label='Víctimas SD', color='red')
                plt.xlabel('Año')
                plt.ylabel('Número Medio de Víctimas')
                plt.title(f'Comparación de Víctimas por Año para el Delito: {crime}')
                plt.xticks(crime_data['anio'], rotation=45)
                plt.legend()
                plt.tight_layout()
                safe_crime = re.sub(r'[^\w\s-]', '', crime).replace(' ', '_')
                plt.savefig(os.path.join(output_path, f'histograma_comparativo_{safe_crime}.png'))
                plt.close()

    def plot_pie_charts(self, subfolder):
        crime_types = self.means_per_crime['codigo_delito'].unique()

        output_path = os.path.join(self.output_dir, 'histograma', subfolder)
        os.makedirs(output_path, exist_ok=True)

        for crime in crime_types:
            crime_data = self.means_per_crime[self.means_per_crime['codigo_delito'] == crime]
            
            total_masc = crime_data['cantidad_victimas_masc'].sum()
            total_fem = crime_data['cantidad_victimas_fem'].sum()
            total_sd = crime_data['cantidad_victimas_sd'].sum()

            if total_masc > 0 or total_fem > 0 or total_sd > 0:
                plt.figure(figsize=(8, 8))
                plt.pie([total_masc, total_fem, total_sd], labels=['Víctimas Masculinas', 'Víctimas Femeninas', 'Víctimas SD'], autopct='%1.1f%%', colors=['blue', 'pink', 'red'])
                plt.title(f'Víctimas Totales para el Delito: {crime}\nTotal Masculinas: {total_masc}, Total Femeninas: {total_fem}, Total SD: {total_sd}')
                safe_crime = re.sub(r'[^\w\s-]', '', crime).replace(' ', '_')
                plt.savefig(os.path.join(output_path, f'diagrama_pastel_{safe_crime}.png'))
                plt.close()
    
    def plot_victimas_anio(self, subfolder):
        output_path = os.path.join(self.output_dir, 'histograma', subfolder)
        os.makedirs(output_path, exist_ok=True)

        crime_types = self.sum_victimas_por_anio['codigo_delito'].unique()

        for crime in crime_types:
            crime_data = self.sum_victimas_por_anio[self.sum_victimas_por_anio['codigo_delito'] == crime]
            
            if 'cantidad_victimas_totales' in crime_data.columns:
                if crime_data['cantidad_victimas_totales'].sum() > 0:
                    plt.figure(figsize=(10, 6))
                    plt.bar(crime_data['anio'], crime_data['cantidad_victimas_totales'], color='skyblue')
                    plt.xlabel('Año')
                    plt.ylabel('Número Total de Víctimas')
                    plt.title(f'Suma de Víctimas por Año para el Delito: {crime}')
                    plt.xticks(crime_data['anio'], rotation=45)
                    plt.tight_layout()
                    safe_crime = re.sub(r'[^\w\s-]', '', crime).replace(' ', '_')
                    plt.savefig(os.path.join(output_path, f'suma_victimas_anio_{safe_crime}.png'))
                    plt.close()

    def plot_comparison_histograms_victima_hechos(self, subfolder):
        crime_types = self.means_per_crime['codigo_delito'].unique()

        output_path = os.path.join(self.output_dir, 'histograma', subfolder)
        os.makedirs(output_path, exist_ok=True)

        for crime in crime_types:
            crime_data_hechos = self.sum_hechos_por_anio[self.sum_hechos_por_anio['codigo_delito'] == crime]
            crime_data_victimas = self.sum_victimas_por_anio[self.sum_victimas_por_anio['codigo_delito'] == crime]

            if not crime_data_hechos.empty and not crime_data_victimas.empty:
                if 'cantidad_hechos' in crime_data_hechos.columns and 'cantidad_victimas_totales' in crime_data_victimas.columns:
                    if crime_data_hechos['cantidad_hechos'].sum() > 0 or crime_data_victimas['cantidad_victimas_totales'].sum() > 0:
                        plt.figure(figsize=(10, 6))
                        plt.bar(crime_data_hechos['anio'] - 0.2, crime_data_hechos['cantidad_hechos'], width=0.4, label='Hechos', color='blue')
                        plt.bar(crime_data_victimas['anio'] + 0.2, crime_data_victimas['cantidad_victimas_totales'], width=0.4, label='Víctimas', color='pink')
                        plt.xlabel('Año')
                        plt.ylabel('Número de Incidentes y Víctimas')
                        plt.title(f'Comparación de Hechos y Víctimas por Año para el Delito: {crime}')
                        plt.xticks(crime_data_hechos['anio'], rotation=45)
                        plt.legend()
                        plt.tight_layout()
                        safe_crime = re.sub(r'[^\w\s-]', '', crime).replace(' ', '_')
                        plt.savefig(os.path.join(output_path, f'histograma_comparativo_{safe_crime}.png'))
                        plt.close()
