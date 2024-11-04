# Author: Eduardo Alvarez
# mail: jesus.e.alvarez@gmail.com
# Date: 16/07/2024
# linkedin: www.linkedin.com/in/jesus-eduardo-alvarez-garcia
"""
Importar Datos de Coches desde un Archivo de Texto a SQLite
Requisitos:
Usar biblioteca estándar sqlite3 para interactuar con SQLite y csv para manejar archivos CSV.
Uso del csv proporcionado en la clase
Crear una tabla en SQLite llamada coches_qa.db
Leer el archivo csv y por cada coche agregar los campos a la tabla coches de la base de datos. La tabla debe contener los campos id (autoincremental), marca (texto), modelo (texto), año (entero), precio (entero)
verificar con SELECT el guardado de coches y finalizar la conexión a la base de datos. 

"""
import csv
import sqlite3
import os
connection = sqlite3.connect('coches_qa.db')
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS example (id INTEGER PRIMARY KEY AUTOINCREMENT, marca  TEXT, modelo TEXT, ano INTEGER, precio INTEGER)")

sql_query = "INSERT INTO example VALUES (NULL, ?, ?, ?, ?)"


with open('coches.csv', 'r') as archive_csv:
    lector = csv.DictReader(archive_csv) #Diccionario
    for fila in lector:
       print(fila['marca'], fila['modelo'], fila['aÃ±o'], fila['precio'])
       sql_data = (fila['marca'], fila['modelo'], fila['aÃ±o'], fila['precio'])
       try:
            cursor.execute(sql_query, sql_data)
            connection.commit()
       except sqlite3.Error as er:
        print(er.sqlite_errorcode)  # Prints 275
        print(er.sqlite_errorname)  # Prints SQLITE_CONSTRAINT_CHECK

        
cursor.close()
connection.close()