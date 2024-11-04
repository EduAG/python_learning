lista = []
lista2 = list([1,2,3,"TEST", 2.3,False])
print(lista2)
lista2[3] = "AHORA es Hola"
print(lista2)

print(f"Info : {lista2[3]}")

lista2.append(True)
print(f"After append")
print(lista2)

lista2.extend([6,7])
print(f"After extend")
print(lista2)

lista2.insert(-2,"Perru")
print(f"After insert")
print(lista2)

lista3 = list([1,2,3,"TEST", 2.3,False])

lista3.remove(False)
print(lista3)

lista3.pop()
print(lista3)

lista3.reverse()
print(lista3)

lista3