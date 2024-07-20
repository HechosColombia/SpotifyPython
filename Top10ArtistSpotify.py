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

# Diccionario para almacenar las líneas de cada artista
lines = {}

# Función de inicialización de la gráfica
def init():
    ax.set_xlabel('Fecha')
    ax.set_ylabel('Horas Escuchadas')
    ax.set_title('Top 10 Artistas - Todo el Año')
    return lines.values()

# Función para actualizar la gráfica en cada cuadro de la animación
def update(frame):
    ax.clear()
    ax.set_xlabel('Fecha')
    ax.set_ylabel('Horas Escuchadas')
    ax.set_title('Top 10 Artistas - Todo el Año')
    for artist_name in top_artists.index:
        artist_data = df[df['artistName'] == artist_name]
        daily_hours = artist_data[artist_data['endTime'] <= frame].groupby(artist_data['endTime'].dt.date)['msPlayed'].sum().cumsum() / (1000 * 60 * 60)
        ax.plot(daily_hours.index, daily_hours.values, label=artist_name)
    ax.legend()

# Crear la animación
ani = FuncAnimation(fig, update, frames=pd.date_range(start=df['endTime'].min(), end=df['endTime'].max()), init_func=init)

# Guardar la animación como un archivo mp4
ani.save('top_artists_year.mp4', writer='ffmpeg')

plt.show()