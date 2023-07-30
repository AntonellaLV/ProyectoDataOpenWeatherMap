# Importar las librerías necesarias
from datetime import datetime, timedelta
import requests
import pandas as pd
import sqlalchemy as db
from pandas import json_normalize
from config import API_KEY, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
from alive_progress import alive_bar

# Función para obtener los datos climáticos de los últimos 5 días para una ubicación
def obtener_datos_climaticos_ultimos_5_dias(coords, API_KEY):
    # URL base para la API del clima
    BASE_URL = "https://api.openweathermap.org/data/2.5/onecall/timemachine?"
    datos_climaticos = []
    fecha_actual = datetime.utcnow()
    for i in range(1, 6):
        # Calcular la fecha de consulta restando 'i' días a la fecha actual
        fecha_consulta = fecha_actual - timedelta(days=i)
        timestamp_consulta = int(fecha_consulta.timestamp())
        # Construir la URL de la API con las coordenadas y la fecha de consulta
        url = f"{BASE_URL}{coords}&dt={timestamp_consulta}&appid={API_KEY}"
        # Realizar la solicitud a la API y obtener los datos en formato JSON
        response = requests.get(url)
        data = response.json()
        # Agregar los datos obtenidos a la lista de datos climáticos
        datos_climaticos.append(data)
    return datos_climaticos

# Función para procesar los datos y convertirlos en un DataFrame de pandas
def procesar_datos(data):
    return json_normalize(data)

# Función para guardar los datos en una tabla de la base de datos
def guardar_en_base_de_datos(df, tabla, engine):
    # Convertir todas las columnas a cadenas (str)
    df = df.astype(str)
    # Reemplazar valores nan en la columna current.wind_gust con 0 por un error que tiraba al guardar los datos de wind_gust
    if 'current.wind_gust' in df.columns:
        df['current.wind_gust'] = df['current.wind_gust'].replace('nan', '0')
    # Guardar el DataFrame en la base de datos en la tabla especificada
    df.to_sql(tabla, engine, if_exists='replace', index=False)


# Función principal del programa
def main():
    # Definir la lista de ciudades y coordenadas para obtener los datos climáticos
    ciudades = [
        "Resistencia, AR",
        "City of London, GB",
        "New York, US",
        "Cordoba, ES",
        "Taipei, TW",
        "Ciudad Autónoma de Buenos Aires, AR",
        "Mexico City, MX", "Dublin City, IE (Ireland)",
        "Tbilisi, GE (Georgia)",
        "Bogotá, CO",
        "Tokyo, JP"]
    
    coordenadas = [
        "lat=-27.46056&lon=-58.983891",     # Resistencia, AR
        "lat=51.512791&lon=-0.09184",       # City of London, GB
        "lat=40.714272&lon=-74.005966",     # New York, US
        "lat=37.90448&lon=-4.77768",        # Cordoba, ES
        "lat=25.025881&lon=121.651611",     # Taipei, TW
        "lat=-34.599998&lon=-58.450001",    # Ciudad Autónoma de Buenos Aires, AR
        "lat=19.428471&lon=-99.127663",     # Mexico City, MX
        "lat=53.355122&lon=-6.24922",       # Dublin City, IE (Ireland)
        "lat=41.694111&lon=44.833679",      # Tbilisi, GE (Georgia)
        "lat=4.60971&lon=-74.081749",       # Bogotá, CO
        "lat=35.689499&lon=139.691711"      # Tokyo, JP
    ]
    # Establecer conexión a la base de datos
    engine = db.create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

    # Iterar sobre las ciudades y coordenadas para obtener y guardar los datos climáticos
    with alive_bar(len(ciudades), title='Processing', length=20, bar='bubbles') as bar:
        for ciudad, coords in zip(ciudades, coordenadas):
            # Convertir el nombre de ciudad a minúsculas y eliminar espacios y comas
            ciudad_id_standardized = ciudad.lower().replace(",", "").replace(" ", "_")
            # Verificar si la tabla ya existe en la base de datos
            inspector = db.inspect(engine)
            # Si la tabla no existe, obtener datos y guardar solo la estructura de la tabla en la base de datos
            if not inspector.has_table(ciudad_id_standardized):
                df_head = procesar_datos(obtener_datos_climaticos_ultimos_5_dias(coords, API_KEY))
                df_head.head(0).to_sql(ciudad_id_standardized, engine, if_exists='append', index=False)
            
            # Obtener datos y guardarlos en la tabla de la base de datos
            df = procesar_datos(obtener_datos_climaticos_ultimos_5_dias(coords, API_KEY))
            guardar_en_base_de_datos(df, ciudad_id_standardized, engine)
            bar()

# Función para guardar los datos en un archivo CSV
def guardar_en_csv(df, ciudad):
    # Reemplazar las comas en el nombre de la ciudad para evitar problemas en el nombre del archivo
    nombre_archivo = ciudad.replace(",", "_").replace(" ", "")
    # Guardar el DataFrame en un archivo CSV
    df.to_csv(f"{nombre_archivo}.csv", index=False)

# Función para guardar los datos en un archivo JSON
def guardar_en_json(df, ciudad):
    # Reemplazar las comas en el nombre de la ciudad para evitar problemas en el nombre del archivo
    nombre_archivo = ciudad.replace(",", "_").replace(" ", "")
    # Guardar el DataFrame en un archivo JSON
    df.to_json(f"{nombre_archivo}.json", orient='records')

# Ejecutar la función principal si el script se está ejecutando directamente
if __name__ == "__main__":
    main()
