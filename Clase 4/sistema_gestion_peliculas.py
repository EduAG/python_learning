# Author: Eduardo Alvarez
# mail: jesus.e.alvarez@gmail.com
# Date: 12/07/2024
# linkedin: www.linkedin.com/in/jesus-eduardo-alvarez-garcia
"""
Definir dos conjuntos vacíos para representar géneros de películas disponibles y géneros favoritos.
Implementar las siguientes funciones:
Agrega un nuevo género al conjunto de géneros disponibles.
Agrega un género al conjunto de géneros favoritos solo si está en el conjunto de géneros disponibles.
Imprime todos los géneros disponibles.
Imprime todos los géneros favoritos.
Elimina un género del conjunto de géneros favoritos si está presente.
Muestra los géneros disponibles que no están en el conjunto de géneros favoritos. 

"""

import unittest

generos_disponible = {'Acción','Aventura','Comedia','Drama','Terror','Ciencia Ficción','Fantasía','Suspenso','Romance','Musical','Animación','Documental','Bélico','Western','Noir','Biográfico'}
genero_favorito = {'Acción','Aventura','Comedia','Drama','Terror'}

def agregar_genero_disponible(genero):
    print('\nagregar_genero_disponible')
    generos_disponible.add(genero)

def agregar_genero_favorito(genero):
    print('\nagregar_genero_favorito')
    if genero in generos_disponible:
        genero_favorito.add(genero)
    else:
        print('El geneor no está disponible dentro de la lista de generos disponibles')

def agregar_género_favorito_no_encontrado(genero):
    if genero not in genero_favorito:
        agregar_genero_favorito(genero)
    else:
        print('Genero ya se encuentra dentro de conjunto genero favorito')

def extract_all_genero_disponible():
    print('\nextract_all_genero_disponible')
    for genero in generos_disponible:
        print(genero)

def extract_all_genero_favorito():
    print('\nextract_all_genero_favorito')
    for genero in genero_favorito:
        print(genero)
    
def delete_genero_favorito(genero):
    print('\ndelete_genero_favorito')
    if genero in genero_favorito:
        print('DENTRO')
        genero_favorito.discard(genero)

def muestra():
    print('\nmuestra')
    muestra = generos_disponible.difference(genero_favorito)
    print(muestra)

#'Deportes','Misterio','Policíaco','Histórico'
# agregar_genero_disponible('Deportes')
# agregar_genero_favorito('Deportes')
# extract_all_genero_disponible()
# extract_all_genero_favorito()
# delete_genero_favorito('Ciencia Ficción')
# muestra()


"""
Crear pruebas unitarias para asegurar que las funciones del Sistema de Gestión de Géneros de Películas funcionen correctamente.
Test a evaluar:
Test agregar géneros 
Test agregar géneros favoritos
Test agregar género favorito no encontrado
Test eliminar género favorito
***Test eliminar género favorito no encontrado : NO existe esta funcionalidad en el aplicativo 
Test mostrar géneros disponibles
Test mostrar géneros favoritos disponibles
Test mostrar géneros no favoritos
???Test agregar género duplicado  :  No se permiten elementos duplicados. Si los elementos aparecen varias veces, 
                                     sólo uno será reconocido en el conjunto. Los elementos de un conjunto no están ordenados.

"""


#Test agregar géneros 
def test_agregar_genero(generos_disponible):
    
   agregar_genero_disponible('TEST_Disponible_1')
   agregar_genero_disponible('TEST_Disponible_2')
   agregar_genero_disponible('TEST_Disponible_3')

   # Verificar que los géneros se hayan agregado correctamente
   assert 'TEST_Disponible_1' in generos_disponible
   assert 'TEST_Disponible_2' in generos_disponible
   assert 'TEST_Disponible_3' in generos_disponible
   generos_disponible.discard('TEST_Disponible_1')
   generos_disponible.discard('TEST_Disponible_2')
   generos_disponible.discard('TEST_Disponible_3')

   print("Todas las pruebas han pasado exitosamente.")

#Test agregar géneros 

def test_agregar_genero_favorito(genero_favorito):

    agregar_genero_favorito('TEST_Fav_1')
    agregar_genero_favorito('TEST_Fav_2')
    agregar_genero_favorito('TEST_Fav_3')

    # Verificar que los géneros se hayan agregado correctamente
    assert 'TEST_Fav_1' in genero_favorito
    assert 'TEST_Fav_2' in genero_favorito
    assert 'TEST_Fav_3' in genero_favorito
    genero_favorito.discard('TEST_Fav_1')
    genero_favorito.discard('TEST_Fav_2')
    genero_favorito.discard('TEST_Fav_3')

    print("Todas las pruebas han pasado exitosamente.")

def testagregar_género_favorito_no_encontrado():
    agregar_género_favorito_no_encontrado('Romance')
    assert 'Romance' in genero_favorito
    print("Todas las pruebas han pasado exitosamente.")
    genero_favorito.discard('Romance')

def test_delete_genero_favorito():
    delete_genero_favorito('Aventura')
    assert 'Aventura' not in genero_favorito
    print(genero_favorito)
    print("Todas las pruebas han pasado exitosamente.")
    agregar_genero_favorito('Aventura')

def test_extract_all_genero_disponible():
    extract_all_genero_disponible()

def test_extract_all_genero_favorito():
    extract_all_genero_favorito()

def test_delete_genero_favorito():
    delete_genero_favorito()


# Ejecutar la prueba
# test_agregar_genero(generos_disponible)
# test_agregar_genero_favorito(genero_favorito)
#testagregar_género_favorito_no_encontrado()
test_extract_all_genero_disponible()
test_extract_all_genero_favorito()