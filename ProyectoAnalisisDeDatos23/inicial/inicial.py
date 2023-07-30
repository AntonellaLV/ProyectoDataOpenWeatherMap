from datetime import datetime
import requests
import pandas as pd
from pandas import json_normalize
import json

def obtener_datos_climaticos(ciudad, coords):
    # Definir la URL base de la API de OpenWeatherMap
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    API_KEY = "cf9cc3cd9216d61286cb5b7ffa89d392"

    # Construir la URL completa con la ciudad y coordenadas
    url = f"{BASE_URL}{coords}&q={ciudad}&appid={API_KEY}"

    # Realizar la solicitud HTTP a la API y obtener los datos en formato JSON
    response = requests.get(url)
    data = response.json()

    # Convertir los datos JSON a un DataFrame de pandas
    df = json_normalize(data)

    # Obtener la fecha actual para utilizarla en el nombre del archivo CSV
    fecha_actual = datetime.now().strftime('%Y%m%d')

    # Definir la ruta y nombre del archivo CSV donde se almacenarán los datos y creo el archivo CSV a partir del DF
    ruta_archivo = f"inicial/data/{ciudad.lower()}_{fecha_actual}.csv".replace(" ", "_")
    with open(ruta_archivo, "w") as archivo_salida:
        df.to_csv(ruta_archivo, index=False)
    
# Ciudades y coordenadas
ciudades = ["Londres", "Nueva York", "Córdoba", "Taipei", "Buenos Aires", "Ciudad de México", "Dublín", "Tilfis", "Bogotá", "Tokio"]
coordenadas = ["lat=31&lon=64", "lat=40&lon=-73", "lat=-31&lon=-64", "lat=25&lon=64", "lat=-34&lon=-58", "lat=19&lon=-99", "lat=53&lon=6", "lat=41&lon=44", "lat=4&lon=74", "lat=35&lon=139"]

# Ejecucion
if __name__ == "__main__":
    for ciudad, coords in zip(ciudades, coordenadas):
        obtener_datos_climaticos(ciudad, coords)
