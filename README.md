Introducción
Este repositorio contiene scripts Python diseñados para analizar datos de historial de escucha de Spotify y generar visualizaciones animadas de los artistas, canciones y horas de escucha a lo largo del tiempo. Los scripts utilizan la biblioteca Pandas para manipular los datos y Matplotlib para crear las visualizaciones.

Estructura del Repositorio
data: Carpeta para almacenar los archivos JSON con el historial de escucha.
scripts: Carpeta que contiene los scripts Python:
Top5ArtistBarsHorizontalSpotify.py: Crea una animación de barras horizontales que muestra los 5 principales artistas en cada momento del año.
Top10ArtistSpotify.py: Genera una animación de líneas que muestra la evolución de las horas de escucha de los 10 principales artistas a lo largo del año.
Top10SongsSpotify.py: Crea una animación similar a la anterior, pero enfocada en las 10 canciones principales de un artista específico.
Requisitos Previos
Python: Se recomienda utilizar Python 3.6 o superior.
Bibliotecas:
pandas: Para manipulación y análisis de datos.
matplotlib: Para crear visualizaciones.
matplotlib.animation: Para crear animaciones.
Instalación
Clonar el repositorio:
git clone (https://github.com/HechosColombia/SpotifyPython)
Instalar las dependencias
pandas
matplotlib
Uso
Colocar el archivo JSON con el historial de escucha en la carpeta data.
Modificar los nombres de los artistas o canciones en los scripts si es necesario.
Ejecutar el script deseado:
python scripts/Top5ArtistBarsHorizontalSpotify.py

Personalización
Artista específico: Modifica el nombre del artista en el script Top10SongsSpotify.py.
Rango de fechas: Ajusta el rango de fechas en la creación de la animación.
Estilo de la gráfica: Personaliza los colores, títulos, leyendas y otros elementos estéticos de las gráficas.
Formato de salida: Cambia el formato de salida de la animación (e.g., GIF, MP4).
Consideraciones
Tamaño del archivo JSON: Para grandes conjuntos de datos, se recomienda procesar los datos por partes o utilizar herramientas más eficientes para la visualización.
Performance: La generación de animaciones puede llevar tiempo, especialmente para conjuntos de datos grandes.
Limpieza de datos: Es posible que sea necesario limpiar los datos antes de analizarlos, por ejemplo, eliminar valores atípicos o corregir errores en los datos.
Contribuciones
Las contribuciones son bienvenidas. Si encuentras algún error o deseas agregar nuevas funcionalidades, por favor, crea un issue o un pull request.
