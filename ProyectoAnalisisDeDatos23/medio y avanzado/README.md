# Trabajo Final

Este es el proyecto de nivel medio de analisis de datos, que obtiene 
los datos del clima de los ultimos 5 dias en la lista de ciudades y 
coordenadas solicitadas en el trabajo final.

# Instrucciones de instalación y ejecución

Para ejecutar este proyecto, necesitarás tener Python 3 instalado en tu sistema.
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
