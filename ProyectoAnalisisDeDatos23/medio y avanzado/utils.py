#utils.py
import os
import requests

def get_weather_data(city):
    API_KEY = os.environ.get('OPENWEATHERMAP_API_KEY')

    if not API_KEY:
        raise ValueError("No se encontró la clave de API de OpenWeatherMap. "
                         "Asegúrate de configurar la variable de entorno 'OPENWEATHERMAP_API_KEY'.")

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data['cod'] == 200:
        weather = {
            'city': data['name'],
            'description': data['weather'][0]['description'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
        }
        return weather

    return None
