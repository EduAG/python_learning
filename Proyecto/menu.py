# Author: Eduardo Alvarez
# mail: jesus.e.alvarez@gmail.com
# Date: 17/07/2024
# linkedin: www.linkedin.com/in/jesus-eduardo-alvarez-garcia

"""
Descripción del Problema:
La biblioteca necesita almacenar información sobre sus libros, 
usuarios y el historial de préstamos en una base de datos, crear un sistema que permita gestionar estos datos de manera eficiente.


- Crear funciones que realicen las siguientes operaciones:
- Agregar un nuevo libro a la base de datos.
- Registrar un nuevo usuario.
- Registrar un préstamo.
- Devolver un libro.
- Listar todos usuarios guardados en la base de datos
- Listar todos libros guardados en la base de datos
- Listar todos los préstamos guardados en la base de datos
- puntos extra (Consultar historial de usuario)

"""
from model.libro import Libro
from model.usuario import Usuario
from model.prestamos import Prestamos
import common

import sqlite3

#usuarios DB
connection_usuarios = sqlite3.connect('usuarios.db')
cursor_usuarios = connection_usuarios.cursor()

#libros DB
connection_libros = sqlite3.connect('libros.db')
cursor_libros = connection_libros.cursor()

# prestamos DB
connection_prestamos = sqlite3.connect('prestamos.db')
cursor_prestamos = connection_prestamos.cursor()

#Select
sql_query_get_all = "SELECT * FROM example"

def display_menu():
    print("Menu:")
    print("1. Agregar un nuevo libro.")
    print("2. Registrar un nuevo usuario.")
    print("3. Registrar un préstamo.")
    print("4. Devolver un libro.")
    print("5. Listar todos usuarios guardados en la base de datos.")
    print("6. Listar todos libros guardados en la base de datos.")
    print("7. Listar todos los préstamos guardados en la base de datos.")
    print("8. Consultar historial de usuario.")
    print("9. Exit.")

def handle_option(option):
    if option == "1":
        nombre = input('Introduce nombre del libro : ')  
        sku = input('Introduce sku del libro : ') 
        autor = input('Introduce autor del libro : ') 
        ano = int(input('Introduce año del libro : ')) 
        categoria = input('Introduce categoria del libro : ') 
        disponibles = int(input('Introduce cantidad de copias disponibles del libro : '))   
        libro = Libro(nombre,sku,autor,ano,categoria,disponibles)
        common.agregar_libro(libro)
    elif option == "2":
        id_usuario = input('Introduce id usuario : ')  
        nombre = input('Introduce nombre del usuario : ') 
        correo = input('Introduce correo del usuario : ') 
        telefono = int(input('Introduce telefono del usuario : '))
        fecha_registro = input('Introduce fecha_registro del usuario : ') 
        usuario = Usuario(id_usuario, nombre, correo, telefono, fecha_registro)
        common.agregar_usuario(usuario)
    elif option == "3":
        id_prestamo = input('Introduce id prestamo :')
        id_usuario = input('Introduce id usuario :')
        sku_libro = input('Introduce sku libro :')
        fecha_prestamo = input('Introduce fecha prestamo :')
        fecha_devolucion = input('Introduce fecha devolucion :')
        prestamos = Prestamos(id_prestamo,id_usuario,sku_libro,fecha_prestamo,fecha_devolucion)
        common.agregar_prestamo(prestamos)
    elif option == "4":
        id_prestamo = input('Introduce id prestamo :')
        common.retornar_libro(id_prestamo)
    elif option == "5":
        usuarios = common.get_all(cursor_usuarios, sql_query_get_all)
        for usuario in usuarios:
            print(usuario)
    elif option == "6":
        libros = common.get_all(cursor_libros, sql_query_get_all)
        for libro in libros:
            print(libro)
    elif option == "7":
        prestamos = common.get_all(cursor_prestamos, sql_query_get_all)
        for prestamo in prestamos:
            print(prestamo)
    elif option == "8":
        id_usuario = input('Proporciona el id del usuario : ')
        historial = common.retornar_historial_usuario(id_usuario)
        print(f"{'id_prestamo':<40} {'id_usuario':<45} {'sku':<10} {'fecha_prestamo':<15} {'fecha_devolucion':<15}")
        for row in historial:
            print(f"{row[0]:<40} {row[1]:<40} {row[2]:<15} {row[3]:<15} {row[4]:<20}")
    elif option == "9":
        print("Exiting...")
        return False
    else:
        print("Invalid option. Please try again.")
    return True

def main():
    while True:
        display_menu()
        option = input("Select an option: ")
        if not handle_option(option):
            break

if __name__ == "__main__":
    main()


