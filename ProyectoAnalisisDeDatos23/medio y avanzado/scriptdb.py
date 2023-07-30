import psycopg2
from config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

def create_database():
    try:
        # Conectarse al servidor PostgreSQL
        conn = psycopg2.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
        )

        # Crear un objeto de conexión para ejecutar comandos SQL
        conn.autocommit = True
        cursor = conn.cursor()

        # Crear la base de datos
        cursor.execute(f"CREATE DATABASE {DB_NAME};")

        print(f"Base de datos '{DB_NAME}' creada exitosamente.")

    except psycopg2.Error as e:
        print(f"Error al crear la base de datos: {e}")
    finally:
        # Cerrar la conexión
        if conn:
            conn.close()

if __name__ == "__main__":
    create_database()