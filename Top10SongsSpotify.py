import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Load the data from the JSON file / CARGAR LOS DATOS DESDE EL ARCHIVO JSON
df = pd.read_json('StreamingHistory0.json')

# Convert the 'endTime' column to datetime / CONVERTIR LA COLUMNA 'endTime' A DATETIME
df['endTime'] = pd.to_datetime(df['endTime'])

# Filter the data to get only the songs of the artist "YourArtist" / FILTRAR LOS DATOS PARA OBTENER SOLO LAS CANCIONES DEL ARTISTA "YourArtist"
YourArtist_songs = df[df['artistName'] == 'YourArtist']

# Get the top 10 songs of the artist "YourArtist" / OBTENER LAS 10 PRINCIPALES CANCIONES DEL ARTISTA "YourArtist"
top_songs = YourArtist_songs['trackName'].value_counts().nlargest(10)

# Create the figure and axis / CREAR LA FIGURA Y EL EJE
fig, ax = plt.subplots(figsize=(10, 6))

# Dictionary to store the lines for each song / DICCIONARIO PARA ALMACENAR LAS LÍNEAS DE CADA CANCIÓN
lines = {}

# Initialization function for the plot / FUNCIÓN DE INICIALIZACIÓN DE LA GRÁFICA
def init():
    ax.set_xlabel('Date')  # X-axis label: Date / ETIQUETA DEL EJE X: FECHA
    ax.set_ylabel('Hours Listened')  # Y-axis label: Hours Listened / ETIQUETA DEL EJE Y: HORAS ESCUCHADAS
    ax.set_title('Top 10 Songs of YourArtist - All Year')  # Plot title: Top 10 Songs of YourArtist - All Year / TÍTULO DEL GRÁFICO: TOP 10 CANCIONES DE YourArtist - TODO EL AÑO
    return lines.values()

# Function to update the plot for each frame of the animation / FUNCIÓN PARA ACTUALIZAR LA GRÁFICA EN CADA CUADRO DE LA ANIMACIÓN
def update(frame):
    ax.clear()
    ax.set_xlabel('Date')  # X-axis label: Date / ETIQUETA DEL EJE X: FECHA
    ax.set_ylabel('Hours Listened')  # Y-axis label: Hours Listened / ETIQUETA DEL EJE Y: HORAS ESCUCHADAS
    ax.set_title('Top 10 Songs of YourArtist - All Year')  # Plot title: Top 10 Songs of YourArtist - All Year / TÍTULO DEL GRÁFICO: TOP 10 CANCIONES DE YourArtist - TODO EL AÑO
    for song_name in top_songs.index:
        song_data = YourArtist_songs[YourArtist_songs['trackName'] == song_name]
        daily_hours = song_data[song_data['endTime'] <= frame].groupby(song_data['endTime'].dt.date)['msPlayed'].sum().cumsum() / (1000 * 60 * 60)
        ax.plot(daily_hours.index, daily_hours.values, label=song_name)
    ax.legend()

# Create the animation / CREAR LA ANIMACIÓN
ani = FuncAnimation(fig, update, frames=pd.date_range(start=df['endTime'].min(), end=df['endTime'].max()), init_func=init)

# Save the animation as an mp4 file / GUARDAR LA ANIMACIÓN COMO UN ARCHIVO MP4
ani.save('top_songs_YourArtist_year.mp4', writer='ffmpeg')

plt.show()
