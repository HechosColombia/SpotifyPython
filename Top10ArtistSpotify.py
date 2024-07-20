import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Load the data from the JSON file / CARGAR DATOS DEL ARCHIVO JSON
df = pd.read_json('StreamingHistory0.json')

# Convert the 'endTime' column to datetime / CONVERTIR LA COLUMNA 'endTime' A DATETIME
df['endTime'] = pd.to_datetime(df['endTime'])

# Group by artist and sum the played milliseconds / AGRUPAR POR ARTISTA Y SUMAR LOS MILISEGUNDOS REPRODUCIDOS
artist_hours = df.groupby('artistName')['msPlayed'].sum() / (1000 * 60 * 60)  # Convert ms to hours / CONVERTIR MS A HORAS
top_artists = artist_hours.nlargest(10)  # Get the top 10 artists / OBTENER LOS 10 PRINCIPALES ARTISTAS

# Create the figure and axis / CREAR LA FIGURA Y EL EJE
fig, ax = plt.subplots(figsize=(10, 6))

# Dictionary to store the lines for each artist / DICCIONARIO PARA ALMACENAR LAS LÍNEAS DE CADA ARTISTA
lines = {}

# Initialization function for the plot / FUNCIÓN DE INICIALIZACIÓN DE LA GRÁFICA
def init():
    ax.set_xlabel('Date')  # X-axis label: Date / ETIQUETA DEL EJE X: FECHA
    ax.set_ylabel('Hours Listened')  # Y-axis label: Hours Listened / ETIQUETA DEL EJE Y: HORAS ESCUCHADAS
    ax.set_title('Top 10 Artists - All Year')  # Plot title: Top 10 Artists - All Year / TÍTULO DEL GRÁFICO: TOP 10 ARTISTAS - TODO EL AÑO
    return lines.values()

# Function to update the plot for each frame of the animation / FUNCIÓN PARA ACTUALIZAR LA GRÁFICA EN CADA CUADRO DE LA ANIMACIÓN
def update(frame):
    ax.clear()
    ax.set_xlabel('Date')  # X-axis label: Date / ETIQUETA DEL EJE X: FECHA
    ax.set_ylabel('Hours Listened')  # Y-axis label: Hours Listened / ETIQUETA DEL EJE Y: HORAS ESCUCHADAS
    ax.set_title('Top 10 Artists - All Year')  # Plot title: Top 10 Artists - All Year / TÍTULO DEL GRÁFICO: TOP 10 ARTISTAS - TODO EL AÑO
    for artist_name in top_artists.index:
        artist_data = df[df['artistName'] == artist_name]
        daily_hours = artist_data[artist_data['endTime'] <= frame].groupby(artist_comments['endTime'].dt.date)['msPlayed'].sum().cumsum() / (1000 * 60 * 60)
        ax.plot(daily_hours.index, daily_hours.values, label=artist_name)
    ax.legend()

# Create the animation / CREAR LA ANIMACIÓN
ani = FuncAnimation(fig, update, frames=pd.date_range(start=df['endTime'].min(), end=df['endTime'].max()), init_func=init)

# Save the animation as an mp4 file / GUARDAR LA ANIMACIÓN COMO UN ARCHIVO MP4
ani.save('top_artists_year.mp4', writer='ffmpeg')

plt.show()
