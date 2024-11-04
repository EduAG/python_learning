class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario

    def mostrar_salario(self):
        return f"{self.nombre} tiene un salario de {self.salario} dólares."
    
empleado1 = Empleado("Ana", 28, 5000)
print(empleado1)

#Polimorfismo

class Animal:
    def hacer_sonido(self):
        return "hola"

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"
    
def imprimir_sonido(animal):
    print(animal.hacer_sonido())

perro = Perro()
gato = Gato()

imprimir_sonido(perro)
imprimir_sonido(gato)

####################

class Circulo:
    pi = 3.14159

    def __init__(self, radio):
        self.radio = radio

    @classmethod
    def crear_con_diametro(cls, diametro):
        return cls(diametro / 2)

    def area(self):
        return Circulo.pi * (self.radio ** 2)

circulo = Circulo.crear_con_diametro(10)
print(circulo.area())  # Salida: 78.53975