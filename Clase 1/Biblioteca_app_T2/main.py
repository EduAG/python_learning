# Author: Eduardo Alvarez
# mail: jesus.e.alvarez@gmail.com
# Date: 12/07/2024
# linkedin: www.linkedin.com/in/jesus-eduardo-alvarez-garcia
"""
Crea una biblioteca virtual que permita agregar, buscar y prestar libros. Utiliza conceptos de POO, herencia, polimorfismo, encapsulamiento y más.

Requisitos:

- Crea una clase Libro con atributos titulo, autor, genero y disponible (booleano).
- Crea una clase Biblioteca que contenga una lista de libros y métodos para agregar, buscar y prestar libros.
- Implementa un método estático para buscar libros por género.
- Utiliza encapsulamiento para proteger el acceso directo a la lista de libros.
- Utiliza propiedades para obtener y establecer el estado de disponibilidad de los libros.
"""

class Libro:
    def __init__(self, titulo: str, autor: str, genero: str, disponible: bool):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.__disponible = disponible # atributo privado, accesible mediante propiedad

    @property
    def disponible(self):
        return self.__disponible # Get Method
         
        
    @disponible.setter
    def disponible(self, estado):
        self.__disponible = estado

    def __str__(self):
        return f"{self.titulo} - {self.autor}"

class Biblioteca:
    def __init__(self):
        self.__lista_libros = [] # Lita privada de libros
    
    def agregar_libro(self, libro):
        self.__lista_libros.append(libro)

    def buscar_libro(self, titulo):
        for libro in self.__lista_libros:
            if libro.titulo == titulo:
                return libro
        return None
    
    def prestar_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        if libro and libro.disponible:
            libro.disponible = False
            return libro
        else:
            return None
    
    @staticmethod
    def buscar_por_genero(biblioteca, genero):
        lista_libros_genero = []
        for libro in biblioteca.__lista_libros:
            if libro.genero == genero:
                lista_libros_genero.append(libro)
        return lista_libros_genero


if __name__ == '__main__':

    libro1 = Libro("Harry Potter y la piedra filosofal", "J.K. Rowling", "Fantasía", False)
    libro2 = Libro("1984", "George Orwell", "Ciencia Ficción", True)
    libro3 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", False)
    libro4 = Libro("El nombre del viento", "Patrick Rothfuss", "Fantasía ", True)

    biblioteca = Biblioteca()

    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)
    biblioteca.agregar_libro(libro4)

    libro_buscar = biblioteca.buscar_libro("1984")
    print("**** Buscar libro por titulo ****")
    print(f"Titulo: {libro_buscar.titulo}\nAutor: {libro_buscar.autor}\nGenero: {libro_buscar.genero}\nDisponible: {libro_buscar.disponible}")

    print("**** Prestar libro por titulo ****")
    libro_prestar = biblioteca.prestar_libro("El nombre del viento")
    if libro_prestar:
        print(f"Se prestó el libro :\nTitulo: {libro_prestar.titulo}\nAutor: {libro_prestar.autor}\nGenero: {libro_prestar.genero}\nDisponible: {libro_prestar.disponible}")
    else: 
        print("El libro no está disponible para prestar.")

    libro_genero_buscar = biblioteca.buscar_por_genero(biblioteca, "Ciencia Ficción")
    for libro in libro_genero_buscar:
        print("**** Buscar libro por genero ****")
        print(f"Titulo: {libro.titulo}\nAutor: {libro.autor}\nGenero: {libro.genero}\nDisponible: {libro_prestar.disponible}")
