from loadcsv import DataLoader
from analytics import CrimeAnalytics
from datavisualizer import DataVisualizer
import os

def main():
    folder_path = 'datos'  # Carpeta donde se encuentran los archivos
    filepath = os.path.join(folder_path, 'clean_data.csv')  # Ruta completa al archivo clean_data.csv
    
    data_loader = DataLoader(filepath)
    df = data_loader.load_data()
    
    analytics = CrimeAnalytics(df)
    means_per_crime = analytics.calculate_means()
    sum_victimas_por_anio = analytics.calculate_sum_victimas_por_anio()
    sum_hechos_por_anio = analytics.calculate_sum_hechos_por_anio()  # Calcular la suma de hechos por año
    
    # Definir el directorio de salida
    output_dir = os.path.join(os.getcwd(), 'output')  # Directorio de salida relativo a la ubicación actual
    
    # Crear una instancia de DataVisualizer
    visualizer = DataVisualizer(means_per_crime, sum_victimas_por_anio, sum_hechos_por_anio, output_dir)  # Añadir output_dir
    
    # Graficar histogramas para víctimas masculinas
    visualizer.plot_histograms('cantidad_victimas_masc', 'histograms_masc')
    
    # Graficar histogramas para víctimas femeninas
    visualizer.plot_histograms('cantidad_victimas_fem', 'histograms_fem')
    
    # Graficar histogramas para víctimas con género desconocido
    visualizer.plot_histograms('cantidad_victimas_sd', 'histograms_sd')
    
    # Graficar histogramas comparativos
    visualizer.plot_comparison_histograms('comparison_histograms')
    
    # Graficar gráficos de pastel para el total de víctimas por delito
    visualizer.plot_pie_charts('pie_charts')
    
    # Graficar la suma de víctimas por año para cada delito
    visualizer.plot_victimas_anio('sum_victimas_anio')
    
    # Graficar histogramas comparativos de hechos y víctimas
    visualizer.plot_comparison_histograms_victima_hechos('victimas_hechos')

if __name__ == "__main__":
    main()
