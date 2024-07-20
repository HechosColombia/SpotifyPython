import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Cargar los datos desde el archivo JSON
df = pd.read_json('StreamingHistory0.json')

# Convertir la columna 'endTime' a datetime
df['endTime'] = pd.to_datetime(df['endTime'])


# Filtrar los datos para obtener solo las canciones del artista "YourArtist"
YourArtist_songs = df[df['artistName'] == 'YourArtist']

# Obtener las 10 principales canciones del artista "YourArtist"
top_songs = YourArtist_songs['trackName'].value_counts().nlargest(10)

# Crear la figura y el eje
fig, ax = plt.subplots(figsize=(10, 6))

# Diccionario para almacenar las líneas de cada canción
lines = {}

# Función de inicialización de la gráfica
def init():
    ax.set_xlabel('Fecha')
    ax.set_ylabel('Horas Escuchadas')
    ax.set_title('Top 10 Canciones de YourArtist - Todo el Año')
    return lines.values()

# Función para actualizar la gráfica en cada cuadro de la animación
def update(frame):
    ax.clear()
    ax.set_xlabel('Fecha')
    ax.set_ylabel('Horas Escuchadas')
    ax.set_title('Top 10 Canciones de YourArtist - Todo el Año')
    for song_name in top_songs.index:
        song_data = YourArtist_songs[YourArtist_songs['trackName'] == song_name]
        daily_hours = song_data[song_data['endTime'] <= frame].groupby(song_data['endTime'].dt.date)['msPlayed'].sum().cumsum() / (1000 * 60 * 60)
        ax.plot(daily_hours.index, daily_hours.values, label=song_name)
    ax.legend()

# Crear la animación
ani = FuncAnimation(fig, update, frames=pd.date_range(start=df['endTime'].min(), end=df['endTime'].max()), init_func=init)

# Guardar la animación como un archivo mp4
ani.save('top_songs_YourArtist_year.mp4', writer='ffmpeg')

plt.show()