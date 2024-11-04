#--------------------------TXT---------------------------------------


#with open('texto.txt','r') as archive:
#    contenido = archive.read()
#    print(contenido)

#with open('texto.txt', 'r') as archive:
#    for line in archive:
#        print(line, end="")

#with open('texto.txt', 'r') as archive:
#    print(archive.readlines())

#----------------------------------CSV---------------------------------

"""
import csv

with open('lenguajes.csv', 'r') as archive_csv:
    #lector = csv.DictReader(archive_csv) #Diccionario
    #for fila in lector:
    #    print(fila)
    lector = csv.reader(archive_csv) # listas con los valores din las claves
    for fila in lector:
        print(fila)
"""

#--------------------------------JSON-----------------------------------------

import json

with open('lenguaje.json') as archive_json:
    #datos = json.load(archive_json)
    file_contents = archive_json.read()
    file = json.loads(file_contents)
    print(type(file))
    print(file["nombre"])

