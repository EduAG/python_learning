# Author: Eduardo Alvarez
# mail: jesus.e.alvarez@gmail.com
# Date: 12/07/2024
# linkedin: www.linkedin.com/in/jesus-eduardo-alvarez-garcia

"""
Desarrollar un sistema simple para gestionar los pedidos de los clientes en un restaurante. 
El sistema debe permitir agregar pedidos, mostrar la lista de pedidos actuales, 
eliminar un pedido específico y calcular el total de ingresos generados por los pedidos.
"""

class Pedido:
    def __init__(self, total, mesa, num_pedido, disponible):
        self.__total = total
        self.__mesa = mesa
        self.__num_pedido = num_pedido
        self.__disponible = disponible

    #TOTAL
    @property
    def total(self):
        return self.__total #GET
    
    @total.setter
    def total(self, cantidad_total):
        self.__total = cantidad_total
    
    #MESA
    @property
    def mesa(self):
        return self.__mesa #GET
    
    @mesa.setter
    def mesa(self, numero):
        self.__mesa = numero
    
    #Numero de pedido
    @property
    def num_pedido(self):
        return self.__num_pedido #GET

    @num_pedido.setter
    def num_pedido(self, numero):
        self.__num_pedido = numero
    
    #Disponible
    @property
    def disponible(self):
        return self.__disponble #GET
    
    @disponible.setter
    def disponible(self, estado):
        self.__disponble = estado

    def __str__(self):
        return f"Total : {self.total}, Mesa : {self.mesa}, Numero de pedido : {self.num_pedido}"


class Pedidos:

    def __init__(self):
        self.__lista_pedidos = [] # Lita privada de pedidos

    def agregar_pedido(self, pedido):
        print(pedido)
        self.__lista_pedidos.append(pedido)

    def eliminar_pedido(self, num_pedido):
        pedido = pedidos.buscar_pedido(num_pedido)
        self.__lista_pedidos.remove(pedido)

    def buscar_pedido(self, num_pedido):
        for pedido in self.__lista_pedidos:
            if pedido.num_pedido == num_pedido:
                return pedido

    def mostrat_todos_pedidos(pedidos):
        return pedidos.__lista_pedidos
    
    def total_ingresos_pedidos(self):
        total = 0
        for pedido in self.__lista_pedidos:
            total += pedido.total
        print(f"El total es :  {total}")

pedido1 = Pedido(0, '01', '001', False)
pedido2 = Pedido(150, '02', '002', True)
pedido3 = Pedido(0, '03', '003', False)
pedido4 = Pedido(200, '04', '004', True)
pedido5 = Pedido(0, '05', '005', False)

pedidos = Pedidos()

pedidos.agregar_pedido(pedido1)
pedidos.agregar_pedido(pedido2)
pedidos.agregar_pedido(pedido3)
pedidos.agregar_pedido(pedido4)
pedidos.agregar_pedido(pedido5)

print("Todas las pedidos")

lista_pedidos = pedidos.mostrat_todos_pedidos()
for pedido in lista_pedidos:
    print(pedido)

pedidos.eliminar_pedido('003')

print("Se elimina pedido...  003")

lista_pedidos = pedidos.mostrat_todos_pedidos()
for pedido in lista_pedidos:
    print(pedido)

pedidos.total_ingresos_pedidos()
