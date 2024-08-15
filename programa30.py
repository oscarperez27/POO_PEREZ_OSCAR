import os
import mysql.connector
from mysql.connector import Error

def limpiar_pantalla():
    "Limpia la pantalla de la terminal."
    os.system('cls')  # Usa 'clear' en sistemas Unix/Linux y macOS.

def base():
    "Establece la conexión a la base de datos MySQL."
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='12345',
            database='utd'
        )
def consultas(connection):
    "Ejecuta consultas básicas en la base de datos."
    try:
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM alumnos")
        resultados = cursor.fetchall()
        print("Registros en la tabla 'alumnos':")
        for fila in resultados:
            print(fila)

        cursor.execute("INSERT INTO alumnos (nombre, edad, direccion, id_maestro) VALUES (%s, %s, %s, %s)", ('Prueba', 25, 'Calle Inventada', 3))
        connection.commit()
        print("Registro insertado exitosamente.")

    except Error as e:
        print(f"Error al ejecutar consultas: {e}")
    finally:
        cursor.close()