Proyecto: Biblioteca virtual
Desarrollar un sistema de gestión para una biblioteca utilizando Python, que permita manejar información sobre libros, usuarios y préstamos, integrando todos los conceptos fundamentales que se han enseñado en el curso.
Descripción del Problema:
La biblioteca necesita almacenar información sobre sus libros, usuarios y el historial de préstamos en una base de datos. Actualmente, la información se gestiona en tres archivos Excel, pero el objetivo es migrar esta información a una base de datos SQLite y crear un sistema que permita gestionar estos datos de manera eficiente.
Requisitos a evaluar:
Tipos de Variables y Estructuras de Control:
Definir variables para representar los atributos de libros, usuarios y préstamos.
Utilizar estructuras de control (if, loops) para procesar y validar datos, como comprobar la disponibilidad de un libro antes de realizar un préstamo.
Funciones:
Crear funciones que realicen las siguientes operaciones:
Agregar un nuevo libro a la base de datos.
Registrar un nuevo usuario.
Registrar un préstamo.
Devolver un libro.
Listar todos usuarios guardados en la base de datos
Listar todos libros guardados en la base de datos
Listar todos los préstamos guardados en la base de datos
puntos extra (Consultar historial de usuario)
Listas y Tuplas:
Usar listas para almacenar múltiples registros de libros y usuarios antes de migrarlos a la base de datos.
Utilizar tuplas para representar cada libro y usuario de manera inmutable.
Diccionarios y Conjuntos:
Implementar diccionarios para organizar la información por categorías (e.g., libros por autor, usuarios por fecha de registro).
Utilizar conjuntos para manejar listas únicas, como las categorías de libros o los autores.
Archivos y Módulos:
Leer los datos de los archivos Excel y escribirlos en la base de datos.
SQLite:
Crear una base de datos SQLite que contenga tablas para los libros, usuarios y préstamos.
Migrar los datos desde los archivos Excel a la base de datos SQLite.
Realizar consultas para verificar el historial de préstamos de un usuario.
Entregables:
Código del Sistema: Implementación en Python que cumpla con los requisitos mencionados (archivo de migración.py y menu.py)
Base de Datos SQLite: Archivo de la base de datos SQLite con los datos migrados desde los archivos Excel.
