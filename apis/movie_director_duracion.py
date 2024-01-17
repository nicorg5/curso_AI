import requests
from dotenv import load_dotenv
import os
import tkinter as tk

# Cargar variables de entorno desde .env
load_dotenv()

url_omdb = os.getenv("API_URL") + os.getenv("OMDB_API_KEY") + "&t="

def get_movie_info(movie):
    """
    Obtiene información sobre una pelicula

    Args:
        movie (str): El título de la película
    """
    result = requests.get(url_omdb + movie)
    result_json = result.json()
    return result_json

def show_movie_info(movie, ventana):
    # Obtener información de la película
    movie_info = get_movie_info(movie)

    # Crear un widget de etiqueta y asignar la información
    etiqueta = tk.Label(ventana, text=f"Título: {movie_info['Title']}\n"
                                     f"Director: {movie_info['Director']}\n"
                                     f"Duración: {movie_info['Runtime']}\n")
    
    etiqueta.pack()

# Se crea la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Información de películas")

# Se muestra la información de la película Avatar
show_movie_info('Avatar', ventana_principal)

# Mostrar información de la película "The Godfather"
show_movie_info('The Godfather', ventana_principal)

ventana_principal.mainloop()