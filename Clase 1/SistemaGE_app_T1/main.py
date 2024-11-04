# Author: Eduardo Alvarez
# mail: jesus.e.alvarez@gmail.com
# Date: 12/07/2024
# linkedin: www.linkedin.com/in/jesus-eduardo-alvarez-garcia

"""
Desarrolla un sistema de gestión de estudiantes que permita agregar, eliminar y actualizar información de los estudiantes. Utiliza herencia múltiple, composición y métodos de clase.
Requisitos:
- Crea una clase Persona con atributos nombre, apellido y edad.
- Crea una clase Estudiante que herede de Persona y tenga atributos adicionales como matricula y cursos.
- Crea una clase Profesor que herede de Persona y tenga atributos adicionales como departamento y asignaturas.
- Implementa una clase Curso que tenga atributos nombre, codigo y profesor (composición).
- Utiliza métodos de clase para contar el número de estudiantes y profesores.
- Implementa métodos para agregar y eliminar cursos de un estudiante.

"""

class Persona:
    def __init__(self, nombre: str, apellido: str, edad: int) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

class Estudiante(Persona):
    num_estudiante = 0
    def __init__(self, nombre: str, apellido: str, edad: int, matricula: str) -> None:
        super().__init__(nombre, apellido, edad)
        self.matricula = matricula
        self.cursos = []

        Estudiante.contar()
        

    def agregar_curso(self, curso):
        self.cursos.append(curso)

    def eliminar_curso(self, curso):
        if curso in self.cursos:
            self.cursos.remove(curso)
    
    def contar():
        Estudiante.num_estudiante +=1

class Profesor(Persona):
    numero_profesores = 0
    def __init__(self, nombre: str, apellido: str, edad: int, departamento: str, asignaturas: str) -> None:
        super().__init__(nombre, apellido, edad)
        self.departament = departamento
        self.asignatura = asignaturas

        Profesor.contar()

    def contar():
        Profesor.numero_profesores +=1

class Curso():
    def __init__(self, nombre:str, codigo:str, profesor:str) -> None:
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor #Hacemos la Composicion



if __name__ == '__main__':
    # Crear profesores
    profesor1 = Profesor("Pedro", "Martinez", 35, "Ciencias", "Ciencias Natrales")
    profesor2 = Profesor("Ana", "Lopez", 40, "Matematicas", "Matemaicas")
    profesor3 = Profesor("José Manuel", "Nah", 18, "Programacion", "Programacion")

    # Crear cursos
    curso1 = Curso("Programación Avanzada", "PA101", profesor1)
    curso2 = Curso("Matemáticas Discretas", "MD202", profesor2)

       # Crear estudiantes
    estudiante1 = Estudiante("Juan", "Perez", 20, "001")
    estudiante2 = Estudiante("Juan", "Perez", 20, "001")

    estudiante1.agregar_curso(curso1)
    estudiante1.agregar_curso(curso2)

    estudiante2.agregar_curso(curso1)

    print("\n----------- Estudiante 1 -----------")
    for curso in estudiante1.cursos:
        print(f"El curso es :\nNombre:{curso.nombre}\nCodigo:{curso.codigo}\nProfesor:{curso.profesor.nombre}")

    print("\n----------- Estudiante 2 -----------")
    for curso in estudiante2.cursos:
        print(f"El curso es :\nNombre:{curso.nombre}\nCodigo:{curso.codigo}\nProfesor:{curso.profesor.nombre}")

    estudiante1.eliminar_curso(curso1)

    for curso in estudiante1.cursos:
        print("\n----------- Eliminar clase estudiante 1 -----------")
        print(f"El curso es :\nNombre:{curso.nombre}\nCodigo:{curso.codigo}\nProfesor:{curso.profesor.nombre}")

    print(f"\n\nNumero de estudiantes: {Estudiante.num_estudiante}")
    print(f"\n\nNumero de estudiantes: {Profesor.numero_profesores}\n\n")