# Author: Eduardo Alvarez
# mail: jesus.e.alvarez@gmail.com
# Date: 16/07/2024
# linkedin: www.linkedin.com/in/jesus-eduardo-alvarez-garcia

"""
Objetivo es migrar esta información a una base de datos SQLite.

"""

import csv
import sqlite3
import os

# #usuarios DB
# connection_usuarios = sqlite3.connect('usuarios.db')
# cursor_usuarios = connection_usuarios.cursor()
# cursor_usuarios.execute("CREATE TABLE IF NOT EXISTS example (id_usuario TEXT PRIMARY KEY, nombre  TEXT, correo TEXT, telefono INTEGER, fecha_registro TEXTO)")

#libros DB
# connection_libros = sqlite3.connect('libros.db')
# cursor_libros = connection_libros.cursor()
# cursor_libros.execute("CREATE TABLE IF NOT EXISTS example (sku TEXT PRIMARY KEY, nombre  TEXT, autor TEXT, ano INTEGER, categoria TEXT, disponibles INTEGER)")

## prestamos DB
# connection_prestamos = sqlite3.connect('prestamos.db')
# cursor_prestamos = connection_prestamos.cursor()
# cursor_prestamos.execute("CREATE TABLE IF NOT EXISTS example (id_prestamo TEXT PRIMARY KEY, id_usuario TEXT, sku TEXT, fecha_prestamo TEXT, fecha_devolucion TEXT, FOREIGN KEY(id_usuario) REFERENCES usuarios(id_usuario), FOREIGN KEY(sku) REFERENCES libros(sku))")

# sql_query_usuarios = "INSERT INTO example VALUES (?, ?, ?, ?, ?)"
# sql_query_libros = "INSERT INTO example VALUES (?, ?, ?, ?, ?, ?)"
# sql_query_prestamos = "INSERT INTO example VALUES (?, ?, ?, ?, ?)"

# with open('usuarios.csv', 'r') as archive_csv:
#     lector = csv.DictReader(archive_csv) #Diccionario
#     for fila in lector:
#     #    print(fila['ID de Usuario'], fila['Nombre'], fila['Correo ElectrÃ³nico'], fila['TelÃ©fono'], fila['Fecha de Registro'])
#        sql_data = (fila['ID de Usuario'], fila['Nombre'], fila['Correo ElectrÃ³nico'], fila['TelÃ©fono'], fila['Fecha de Registro'])
#        try:
#             cursor_usuarios.execute(sql_query_usuarios, sql_data)
#             connection_usuarios.commit()
#        except sqlite3.Error as er:
#         print(er.sqlite_errorcode)  # Prints 275
#         print(er.sqlite_errorname)  # Prints SQLITE_CONSTRAINT_CHECK
    
# print('---------------------------------------------------------------')

# with open('libros.csv', 'r') as archive_csv:
#     lector = csv.DictReader(archive_csv) #Diccionario
#     for fila in lector:
#     #    print(fila['Nombre'], fila['SKU'], fila['Autor'], fila['AÃ±o'], fila['CategorÃ\xada'], fila['Disponibles'])
#        sql_data = (fila['SKU'], fila['Nombre'], fila['Autor'], fila['AÃ±o'], fila['CategorÃ\xada'], fila['Disponibles'])
#        try:
#             cursor_libros.execute(sql_query_libros, sql_data)
#             connection_libros.commit()
#        except sqlite3.Error as er:
#         print(er.sqlite_errorcode)  # Prints 275
#         print(er.sqlite_errorname)  # Prints SQLITE_CONSTRAINT_CHECK

# print('---------------------------------------------------------------')

# with open('prestamos.csv', 'r') as archive_csv:
#     lector = csv.DictReader(archive_csv) #Diccionario
#     for fila in lector:
#     #   print(fila['ID de PrÃ©stamo'], fila['ID de Usuario'], fila['SKU del Libro'], fila['Fecha de PrÃ©stamo'], fila['Fecha de DevoluciÃ³n'])
#       sql_data = (fila['ID de PrÃ©stamo'], fila['ID de Usuario'], fila['SKU del Libro'], fila['Fecha de PrÃ©stamo'], fila['Fecha de DevoluciÃ³n'])
#       try:
#         cursor_prestamos.execute(sql_query_prestamos, sql_data)
#         connection_prestamos.commit()
#       except sqlite3.Error as er:
#         print(er.sqlite_errorcode)  # Prints 275
#         print(er.sqlite_errorname)  # Prints SQLITE_CONSTRAINT_CHECK


# cursor_usuarios.close()
# connection_usuarios.close()        

# cursor_libros.close()
# connection_libros.close()

# cursor_prestamos.close()
# connection_prestamos.close()

