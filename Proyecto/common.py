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

#Insert
sql_query_usuarios_insert = "INSERT INTO example VALUES (?, ?, ?, ?, ?)"
sql_query_libros_insert = "INSERT INTO example VALUES (?, ?, ?, ?, ?, ?)"
sql_query_prestamos_insert = "INSERT INTO example VALUES (?, ?, ?, ?, ?)"
#Select
sql_query_get_all = "SELECT * FROM example"
#Update values
sql_query_update_1_disponibles = "UPDATE example SET disponibles = disponibles + 1 WHERE sku = ?"
sql_query_update_2_disponibles = "UPDATE example SET disponibles = disponibles + - WHERE sku = ?"


def guardar_db(cursor, connection, sql_query, sql_data):
    try:
     cursor.execute(sql_query, sql_data)
     connection.commit()
     print(' guardar_db Operacion completada')
    except sqlite3.Error as er:
     print(er.sqlite_errorcode)  # Prints 275
     print(er.sqlite_errorname)  # Prints SQLITE_CONSTRAINT_CHECK

def update_column_database(cursor, connection, sql_query, data):
    try:
     cursor.execute(sql_query, (data,))
     connection.commit()
     updated_book = cursor.fetchone() # returns a list of tuples
     print('get_all Operacion completada')
     return updated_book
    except sqlite3.Error as er:
     print(er.sqlite_errorcode)  # Prints 275
     print(er.sqlite_errorname)  # Prints SQLITE_CONSTRAINT_CHECK

def get_all(cursor, sql_query):
    try:
     cursor.execute(sql_query)
     rows = cursor.fetchall() # returns a list of tuples
     print('get_all Operacion completada')
     return rows
    except sqlite3.Error as er:
     print(er.sqlite_errorcode)  # Prints 275
     print(er.sqlite_errorname)  # Prints SQLITE_CONSTRAINT_CHECK

def agregar_libro(libro):
    sql_data = (libro.nombre,libro.sku,libro.autor,libro.ano,libro.categoria,libro.disponibles)
    guardar_db(cursor_libros, connection_libros, sql_query_libros_insert, sql_data)
    cursor_libros.close()
    connection_libros.close()

def agregar_usuario(usuario):
    sql_data = (usuario.id_usuario,usuario.nombre,usuario.correo,usuario.telefono,usuario.fecha_registro)
    guardar_db(cursor_usuarios, connection_usuarios, sql_query_usuarios_insert, sql_data)
    cursor_usuarios.close()
    connection_usuarios.close()  

def usuarios_existency_validation(id_usuario):
    usuarios = get_all(cursor_usuarios, sql_query_get_all)
    for usuario in usuarios:
        if usuario[0] == id_usuario:
            print(f'usuarios_existency True')
            return True
    return False

def retornar_libro(id_prestamo):
    prestamos = get_all(cursor_prestamos, sql_query_get_all)
    for prestamo in prestamos:
        if prestamo[0] == id_prestamo:
            prestamo_update_disponibilidad(prestamo[2], sql_query_update_1_disponibles)
    return ()

def prestamo_update_disponibilidad(sku, sql_query):
    libros = get_all(cursor_libros, sql_query_get_all)
    for libro in libros:
        if libro[0] == sku:

            updated_book = update_column_database(cursor_libros, connection_libros, sql_query, libro[0])

def libros_existency_validation(sku_libro):
    libros = get_all(cursor_libros, sql_query_get_all)
    for libro in libros:
        print(libro[0])
        print(sku_libro)
        if libro[0] == sku_libro and libro[5] > 0:
            print(f'libros_existency True')
            return  True
    return False
            
def agregar_prestamo(prestamos):   
    #id_prestamo,id_usuario,sku_libro,fecha_prestamo,fecha_devolucion
    if libros_existency_validation(prestamos.sku_libro) == True and usuarios_existency_validation(prestamos.id_usuario) == True:
        sql_data = (prestamos.id_prestamo, prestamos.id_usuario,prestamos.sku_libro,prestamos.fecha_prestamo, prestamos.fecha_devolucion)
        guardar_db(cursor_prestamos,connection_prestamos,sql_query_prestamos_insert,sql_data)
        cursor_prestamos.close()
        connection_prestamos.close()
        prestamo_update_disponibilidad(prestamos.sku_libro, sql_query_update_2_disponibles)

def retornar_historial_usuario(id_usuario):
    historial = set()
    prestamos = get_all(cursor_prestamos, sql_query_get_all)
    for prestamo in prestamos:
        if prestamo[1] == id_usuario:
            historial.add(prestamo)
    return historial