import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Cargar los datos desde el archivo JSON
df = pd.read_json('StreamingHistory0.json')

# Convertir la columna 'endTime' a datetime
df['endTime'] = pd.to_datetime(df['endTime'])

# Agrupar por artista y sumar los milisegundos reproducidos
artist_hours = df.groupby('artistName')['msPlayed'].sum() / (1000 * 60 * 60)  # Convertir ms a horas
top_artists = artist_hours.nlargest(10)  # Obtener los 10 principales artistas

# Crear la figura y el eje
fig, ax = plt.subplots(figsize=(10, 6))

# Lista para almacenar las barras de cada artista
bars = []

# Función de inicialización de la gráfica
def init():
    ax.set_xlabel('Horas Escuchadas')
    ax.set_title('Top 10 Artistas - Todo el Año')
    return bars

# Función para actualizar la gráfica en cada cuadro de la animación
def update(frame):
    ax.clear()
    ax.set_xlabel('Horas Escuchadas')
    ax.set_title('Top 10 Artistas - Todo el Año')
    
    # Filtrar datos hasta el frame actual
    filtered_df = df[df['endTime'] <= frame]
    
    # Obtener las horas reproducidas por artista en el frame actual
    artist_hours_frame = filtered_df.groupby('artistName')['msPlayed'].sum() / (1000 * 60 * 60)
    
    # Ordenar artistas de mayor a menor horas reproducidas en el frame actual
    top_artists_frame = artist_hours_frame.nlargest(5)
    
    # Obtener los artistas ordenados por horas escuchadas en este frame
    sorted_artists = top_artists_frame.index[::-1]  # Invertir el orden
    
    # Actualizar el orden de las barras y artistas
    ax.clear()
    for i, artist_name in enumerate(sorted_artists):
        height = top_artists_frame[artist_name]
        bar = ax.barh(artist_name, height, color='skyblue')  # Usar color 'skyblue' para todas las barras
        bars.append(bar)
    
    # Agregar una leyenda con el mes del frame en la parte inferior derecha del gráfico
    ax.text(0.95, 0.05, frame.strftime("%B"), ha='right', va='bottom', transform=ax.transAxes, fontsize=12, color='gray')
    
    # Agregar nombre del eje x
    ax.set_xlabel('Horas Escuchadas')

# Crear la animación
ani = FuncAnimation(fig, update, frames=pd.date_range(start=df['endTime'].min(), end=df['endTime'].max()), init_func=init)

# Guardar la animación como un archivo mp4
ani.save('top_artists_year_sorted_horizontal.mp4', writer='ffmpeg')

plt.show()