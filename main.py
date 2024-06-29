from loadcsv import DataLoader
from analytics import CrimeAnalytics
from datavisualizer import DataVisualizer
import os

def main():
    filepath = 'clean_data.csv'
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

    # Plot histograms for male victims
    visualizer.plot_histograms('cantidad_victimas_masc', 'histograms_masc')

    # Plot histograms for female victims
    visualizer.plot_histograms('cantidad_victimas_fem', 'histograms_fem')
    
    # Plot histograms for victims with unknown gender
    visualizer.plot_histograms('cantidad_victimas_sd', 'histograms_sd')

    # Plot comparison histograms
    visualizer.plot_comparison_histograms('comparison_histograms')

    # Plot pie charts for total victims per crime
    visualizer.plot_pie_charts('pie_charts')
    
    # Plot sum of victims per year for each crime
    visualizer.plot_victimas_anio('sum_victimas_anio')

    # Plot comparison histograms for hechos and victimas
    visualizer.plot_comparison_histograms_victima_hechos('victimas_hechos')

if __name__ == "__main__":
    main()
