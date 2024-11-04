class Prestamos:
    def __init__(self, id_prestamo: str, id_usuario: str, sku_libro: str, fecha_prestamo: str, fecha_devolucion: str) -> None:
        self.__id_prestamo = id_prestamo
        self.__id_usuario = id_usuario
        self.__sku_libro = sku_libro
        self.__fecha_prestamo = fecha_prestamo
        self.__fecha_devolucion = fecha_devolucion

    @property
    def id_prestamo(self):
        return self.__id_prestamo

    @id_prestamo.setter
    def id_prestamo(self, id_prestamo):
        self.__id_prestamo = id_prestamo
    
    @property 
    def id_usuario(self):
        return self.__id_usuario
    
    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self.__id_usuario = id_usuario
    
    @property
    def sku_libro(self):
        return self.__sku_libro
    
    @sku_libro.setter
    def sku_libro(self, sku_libro):
        self.__sku_libro = sku_libro
    
    @property
    def fecha_prestamo(self):
        return self.__fecha_prestamo
    @fecha_prestamo.setter
    def fecha_prestamo(self, fecha_prestamo):
        self.__fecha_prestamo = fecha_prestamo

    @property
    def fecha_devolucion(self):
        return self.__fecha_devolucion
    
    @fecha_devolucion.setter
    def fecha_devolucion(self, fecha_devolucion):
        self.__fecha_devolucion = fecha_devolucion

    def __str__(self) -> str:
        return f"{self.id_prestamo} - {self.id_usuario} - {self.sku_libro} - {self.fecha_prestamo} - {self.fecha_devolucion}"
    