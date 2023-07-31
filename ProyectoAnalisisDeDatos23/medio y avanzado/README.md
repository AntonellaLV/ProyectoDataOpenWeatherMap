# Trabajo Final

Este es el proyecto de nivel inicial, medio y difícil de analisis de datos, que obtiene 
los datos del clima de los ultimos 5 días en la lista de ciudades y 
coordenadas solicitadas en formato JSON y CSV los cuales son almacenados en una base de datos y desplegados con el framework Flask como trabajo final. 

# Instrucciones de instalación y ejecución

Para ejecutar este proyecto, necesitarás tener Python instalado en tu sistema.
1. Clona o descarga este repositorio en tu máquina.
2. Crea un entorno virtual (venv) para el proyecto. Abre una terminal y navega 
al directorio raíz del proyecto. Ejecuta los siguientes comandos:

# Windows
```bash
    python -m venv venv
    venv\Scripts\activate
```
# macOS y Linux
```bash
    python -m venv venv
    source venv/bin/activate
```
3. A continuación, instala las dependencias necesarias utilizando `pip` y el archivo `requirements.txt`:
```bash
    pip install -r requirements.txt
```
4. Para crear la base de datos modificar los datos en config.py y ejecutar el scriptdb.py
```bash
    python scriptdb.py
```
5. Ejecuta el proyecto. En la terminal, estando en el directorio raíz del proyecto, ejecuta el siguiente comando:
```bash
    python main.py
```
6. 
**Instalar Flask y Requests**

```bash
    pip install Flask
```
```
pip install requests
```

mantener un archivo **`requirements.txt`** actualizado con el siguiente comando:

```bash
pip freeze > requirements.txt
```

Y luego, al configurar un nuevo entorno virtual, puede instalar todas las dependencias desde el archivo **`requirements.txt`** con el siguiente comando:

```bash

pip install -r requirements.txt
```
- **`app.py`**: archivo principal donde escribiremos nuestra aplicación Flask.
- **`templates`**: aquí almacenaremos nuestras plantillas HTML.
- **`static`**: en este directorio, colocaremos nuestros archivos estáticos, como hojas de estilo CSS.

**Flask**

- Intenta obtener la clave de API de OpenWeatherMap desde las variables de entorno del sistema.
- Si la clave de API no se encuentra, se generará una excepción para indicar que la configuración es incorrecta.
- Define una ruta para la página de inicio de la aplicación, que muestra la plantilla **`'index.html'`**.

**Obtener datos climáticos de OpenWeatherMap**

Obtiene los datos climáticos de la API de OpenWeatherMap cuando el usuario realice una búsqueda.
El código comentado número 1 en app.py es la primera opción para desplegar la app en el navegador. El código comentado número 2, es para ejecutar el motor para la API en formato JSON.

```bash
python app.py
```

Abrir el navegador web e ingresar **`http://127.0.0.1:5000/`**. Se verá la página de inicio de la aplicación, donde se puede ingresar el nombre de una ciudad y obtener los datos climáticos en tiempo real utilizando la API de OpenWeatherMap.

## Utilizacion REST Api:

**Configuración del entorno**

Si aún no se ha creado el entorno virtual y configurado Flask y Requests, seguir los pasos mencionados anteriormente.

**Estructura del proyecto**

Estructura de proyecto para la REST API.

- **`app.py`**: Este archivo será el punto de entrada de la aplicación Flask, contendrá la configuración y la inicialización de la aplicación.
- **`api.py`**: Aquí se definen las rutas y las funciones que maneja las solicitudes HTTP y proporciona los datos climáticos a través de la API RESTful.
- **`utils.py`**: En este archivo, se escriben funciones de utilidad que interactuarán con la API de OpenWeatherMap.

**Funciones de utilidad**


```bash
python api.py
```

**API en JSON**

REST API utilizando herramientas como **`curl`**, **`httpie`** o un cliente REST como Postman. Aquí hay un ejemplo de cómo probar la API con **`httpie`**:

```bash
# Obtener datos climáticos para una ciudad específica (por ejemplo, Londres)
http://127.0.0.1:5000/api/weather?city=London
```

Deberías recibir una respuesta JSON con los datos climáticos para la ciudad de Londres o cualquier otra ciudad que hayas proporcionado.
