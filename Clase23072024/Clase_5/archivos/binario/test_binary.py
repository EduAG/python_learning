archivo_original = 'deadpool_song.mp3'

# Abrir el archivo en modo binario de lectura
with open(archivo_original, 'rb') as archivo_binario:
    # Leer todo el contenido del archivo
    contenido = archivo_binario.read()

# Calcular el tamaño del archivo
tamaño = len(contenido)

# Dividir el contenido en dos partes
mitad = tamaño // 2
primera_mitad = contenido[:mitad]
segunda_mitad = contenido[mitad:]

# Guardar la primera mitad en un nuevo archivo
with open('parte1.mp3', 'wb') as archivo_parte1:
    archivo_parte1.write(primera_mitad)

# Guardar la segunda mitad en otro nuevo archivo
with open('parte2.mp3', 'wb') as archivo_parte2:
    archivo_parte2.write(segunda_mitad)
