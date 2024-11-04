# Author: Eduardo Alvarez
# mail: jesus.e.alvarez@gmail.com
# Date: 12/07/2024
# linkedin: www.linkedin.com/in/jesus-eduardo-alvarez-garcia
"""
Definir dos diccionarios vacíos para representar las recetas disponibles y las recetas favoritas. agrega función para:
Agrega una nueva receta al diccionario de recetas disponibles.
Agrega una receta al diccionario de recetas favoritas solo si está en el diccionario de recetas disponibles.
Imprime todas las recetas disponibles.
Imprime todas las recetas favoritas.
Elimina una receta del diccionario de recetas favoritas si está presente.
Muestra las recetas disponibles que no están en el diccionario de recetas favoritas.

"""
recetas_disponibles = {}
recetas_favoritas = {}

def agregar_receta_disponible(nombre_receta, ingredientes):
    recetas_disponibles[nombre_receta] = ingredientes

def agregar_recetas_favoritas(nombre_receta, ingredientes):
    if nombre_receta in recetas_disponibles:
        recetas_favoritas[nombre_receta] = ingredientes
        print(f"Receta '{nombre_receta}' ha sido agregada a las recetas favoritas.")

    else:
        print(f"Receta '{nombre_receta}' no está disponible, no se puede agregar a las recetas favoritas. ")

def eliminar_receta_favorita(nombre_receta):
    if nombre_receta in recetas_favoritas:
        recetas_favoritas.pop(nombre_receta)
    else:
        print(f"Receta '{nombre_receta}' no está disponible, no se puede eliminar de las recetas favoritas.")
 
def diff_recetas_favoritas_disponibles():
    for receta in recetas_disponibles.keys():
        if receta not in recetas_favoritas:
            print(f"- {receta}")

agregar_receta_disponible('Pollo a la cerverza', ["pollo", "cerveza", "sal", "pimienta", "cebolla"])
agregar_receta_disponible('Sorbete de limón', ["4 limones", "1 litro de agua", "1 kg de azúcar", "hielo"])

agregar_recetas_favoritas('Pollo a la cerverza', ["pollo", "cerveza", "sal", "pimienta", "cebolla"])

print('Recetas disponibles')
print(recetas_disponibles)
print('\nRecetas favoritas')
print(recetas_favoritas)


print('\ndiff_recetas_favoritas_disponibles')
diff_recetas_favoritas_disponibles()
