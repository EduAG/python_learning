# Author: Eduardo Alvarez
# mail: jesus.e.alvarez@gmail.com
# Date: 12/07/2024
# linkedin: www.linkedin.com/in/jesus-eduardo-alvarez-garcia

"""
Desarrollar un sistema simple para gestionar las citas de los clientes en una clínica veterinaria. 
El sis tema debe permitir agregar citas, 
mostrar la lista de citas actuales, 
eliminar una cita específica y buscar citas por el nombre del dueño de la mascota.
"""

class Cita:
    def __init__(self, nombre_propietario:str, nombre_mascota:str, raza:str, numero_cita:int):
        self.__nombre_propietario = nombre_propietario
        self.__nombre_mascota = nombre_mascota
        self.__raza = raza
        self.__numero_cita = numero_cita

    #nombre_propietario
    @property
    def nombre_propietario(self):
        return self.__nombre_propietario #GET
    
    @nombre_propietario.setter
    def nombre_propietario(self, nombre_propietario):
        self.__nombre_propietario = nombre_propietario
    
    #nombre_mascota
    @property
    def nombre_mascota(self):
        return self.__nombre_mascota #GET
    
    @nombre_mascota.setter
    def nombre_mascota(self, nombre_mascota):
        self.__nombre_mascota = nombre_mascota
    
    #raza
    @property
    def raza(self):
        return self.__raza #GET

    @raza.setter
    def raza(self, raza):
        self.__raza = raza
    
    #numero_cita
    @property
    def numero_cita(self):
        return self.__numero_cita #GET

    @numero_cita.setter
    def numero_cita(self, numero_cita):
        self.__numero_cita = numero_cita
    
    def __str__(self) -> str:
        return f"{self.__nombre_propietario} {self.nombre_mascota} {self.numero_cita} {self.raza}"

    def __repr__(self) -> str: # este método
        return f"{self.__nombre_propietario} {self.nombre_mascota} {self.numero_cita} {self.raza}"



class Citas:

    def __init__(self):
        self.__lista_citas = [] # Lita privada de citas

    def agregar_cita(self, cita):
        self.__lista_citas.append(cita)

    def eliminar_cita(self, numero_cita):
        cita = citas.buscar_cita_id(numero_cita)
        self.__lista_citas.remove(cita)

    def buscar_cita(self, nombre_propietario):
        for cita in self.__lista_citas:
            if cita.nombre_propietario == nombre_propietario:
                return cita
            
    def buscar_cita_id(self, numero_cita):
        for cita in self.__lista_citas:
            if cita.numero_cita == numero_cita:
                return cita

    def mostrat_todos_citas(citas):
        return citas.__lista_citas

cita1 = Cita('Arturo','tom','AAA',1)
cita2 = Cita('Beto','pulga','BBB',2)
cita3 = Cita('Ceci','chiquis','CCC',3)
cita4 = Cita('Dany','Masha','DDD',4)
cita5 = Cita('Eduardo','Camilo','EEE',5)

citas = Citas()

citas.agregar_cita(cita1)
citas.agregar_cita(cita2)
citas.agregar_cita(cita3)
citas.agregar_cita(cita4)
citas.agregar_cita(cita5)

print("Todos los citas")

lista_citas = citas.mostrat_todos_citas()
for cita in lista_citas:
    print(cita)

citas.eliminar_cita(1)

print("Se elimina cita... 1")

lista_citas = citas.mostrat_todos_citas()
for cita in lista_citas:
    print(cita)

print('Se muestra la busqueda por nombre de propietario: Eduardo')

cita_cliente = citas.buscar_cita('Eduardo')
print(cita_cliente)