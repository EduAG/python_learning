"""
Supongamos que tenemos una lista de números y queremos buscar la posición de un número específico dentro de la lista. 
La tarea involucra utilizar tanto un bucle for como un bucle while y dentro de cada uno manejar casos específicos usando continue, 
break y else si se requiere.

"""
listaNumeros = [11,12,13,4,5,6,7,1,2,3]
find = 5
count = 0
print(f"El elemento se encuentra en la posicion {listaNumeros.index(5)}")

for elemento in listaNumeros:
    count += 1
    if elemento == find:
        print(f"El numero se encuentra en la posicion  {count-1}")
        break

n = len(listaNumeros)

while n > len(listaNumeros):
    n -=1
    if n == count:
        print(f"El numero se encuentra en la posicion {n}")
        continue
   
    