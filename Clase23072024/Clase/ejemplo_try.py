"""
OSError: Error del sistema operativo.
BlockingIOError: Operación de E/S bloqueada.
ChildProcessError: Operación en un proceso hijo fallida.
ConnectionError: Error de conexión.
BrokenPipeError: Pipe roto.
ConnectionAbortedError: Conexión abortada.
ConnectionRefusedError: Conexión rechazada.
ConnectionResetError: Conexión reiniciada.
FileExistsError: Archivo ya existe.
FileNotFoundError: Archivo no encontrado.
InterruptedError: Operación interrumpida.
IsADirectoryError: Se esperaba un archivo pero
"""

numero = 10
denominador = 0

try:
    print(numero/denominador)
except Exception as e:
    print(f"Error : {e}")
