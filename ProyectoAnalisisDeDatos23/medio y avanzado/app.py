# app.py número 2: REST API
'''from flask import Flask
app = Flask(__name__)

if __name__ == '__main__':
    app.run()'''

#app.py número 1: Enrutamiento en Flask
import os
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Configuración de la clave de API
API_KEY = os.environ.get('OPENWEATHERMAP_API_KEY')
if not API_KEY:
    raise ValueError("No se encontró la clave de API de OpenWeatherMap. "
                     "Asegúrate de configurar la variable de entorno 'OPENWEATHERMAP_API_KEY'.")

# Ruta de inicio
@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None

    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather_data(city)

    return render_template('index.html', weather_data=weather_data)

# Función para obtener datos climáticos de OpenWeatherMap
def get_weather_data(city):
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

if __name__ == '__main__':
    app.run()