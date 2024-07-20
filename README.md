This read me is in english in the first part and in spanish en in lowerpart
Este readme está en ingles en la primer parte y en español en la parte de abajo


# Ingles

# Introduction

This repository contains Python scripts designed to analyze Spotify listening history data and generate animated visualizations of artists, songs, and listening hours over time. The scripts utilize the Pandas library for data manipulation and Matplotlib for creating visualizations.

## Repository Structure

- **data**: Folder to store JSON files with listening history.
- **scripts**: Folder containing Python scripts:
  - `Top5ArtistBarsHorizontalSpotify.py`: Creates a horizontal bar chart animation showing the top 5 artists at each moment in the year.
  - `Top10ArtistSpotify.py`: Generates a line animation showing the evolution of listening hours for the top 10 artists throughout the year.
  - `Top10SongsSpotify.py`: Creates a similar animation as the previous one, but focused on the top 10 songs of a specific artist.

## Prerequisites

- **Python**: Python 3.6 or later is recommended.
- **Libraries**:
  - `pandas`: For data manipulation and analysis.
  - `matplotlib`: For creating visualizations.
  - `matplotlib.animation`: For creating animations.

## Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/HechosColombia/SpotifyPython](https://github.com/HechosColombia/SpotifyPython)
## Installation

**Bash**
pip install pandas matplotlib
**Bash**


## Usage

1. Place the JSON file with your listening history in the **data** folder.
2. Modify the artist or song names in the scripts if necessary.
3. Run the desired script:

   ```bash
   python scripts/Top5ArtistBarsHorizontalSpotify.py
## Customization

- **Specific artist**: Modify the artist name in the `Top10SongsSpotify.py` script.
- **Date range**: Adjust the date range in the animation creation.
- **Graph style**: Customize colors, titles, legends, and other aesthetic elements of the graphs.
- **Output format**: Change the output format of the animation (e.g., GIF, MP4).

## Considerations

- **JSON file size**: For large datasets, it is recommended to process the data in parts or use more efficient tools for visualization.
- **Performance**: Generating animations can be time-consuming, especially for large datasets.
- **Data cleaning**: You may need to clean the data before analysis, such as removing outliers or correcting errors in the data.

## Contributions

Contributions are welcome. If you find any bugs or want to add new features, please create an issue or a pull request.


# ESPAÑOL
# Introducción

Este repositorio contiene scripts Python diseñados para analizar datos de historial de escucha de Spotify y generar visualizaciones animadas de los artistas, canciones y horas de escucha a lo largo del tiempo. Los scripts utilizan la biblioteca Pandas para manipular los datos y Matplotlib para crear las visualizaciones.

## Estructura del Repositorio

- **data**: Carpeta para almacenar los archivos JSON con el historial de escucha.
- **scripts**: Carpeta que contiene los scripts Python:
    - `Top5ArtistBarsHorizontalSpotify.py`: Crea una animación de barras horizontales que muestra los 5 principales artistas en cada momento del año.
    - `Top10ArtistSpotify.py`: Genera una animación de líneas que muestra la evolución de las horas de escucha de los 10 principales artistas a lo largo del año.
    - `Top10SongsSpotify.py`: Crea una animación similar a la anterior, pero enfocada en las 10 canciones principales de un artista específico.

## Requisitos Previos

- **Python**: Se recomienda utilizar Python 3.6 o superior.
- **Bibliotecas**:
    - `pandas`: Para manipulación y análisis de datos.
    - `matplotlib`: Para crear visualizaciones.
    - `matplotlib.animation`: Para crear animaciones.

## Instalación

1. Clonar el repositorio:
    ```sh
    git clone https://github.com/HechosColombia/SpotifyPython
    ```

2. Instalar las dependencias:
    ```sh
    pip install pandas matplotlib
    ```

## Uso

1. Colocar el archivo JSON con el historial de escucha en la carpeta **data**.
2. Modificar los nombres de los artistas o canciones en los scripts si es necesario.
3. Ejecutar el script deseado:
    ```sh
    python scripts/Top5ArtistBarsHorizontalSpotify.py
    ```

## Personalización

- **Artista específico**: Modifica el nombre del artista en el script `Top10SongsSpotify.py`.
- **Rango de fechas**: Ajusta el rango de fechas en la creación de la animación.
- **Estilo de la gráfica**: Personaliza los colores, títulos, leyendas y otros elementos estéticos de las gráficas.
- **Formato de salida**: Cambia el formato de salida de la animación (e.g., GIF, MP4).

## Consideraciones

- **Tamaño del archivo JSON**: Para grandes conjuntos de datos, se recomienda procesar los datos por partes o utilizar herramientas más eficientes para la visualización.
- **Performance**: La generación de animaciones puede llevar tiempo, especialmente para conjuntos de datos grandes.
- **Limpieza de datos**: Es posible que sea necesario limpiar los datos antes de analizarlos, por ejemplo, eliminar valores atípicos o corregir errores en los datos.

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún error o deseas agregar nuevas funcionalidades, por favor, crea un issue o un pull request.

