class Usuario:
    def __init__(self, id_usuario: str, nombre: str, correo: str, telefono: int, fecha_registro: str) -> None:
        self.__id_usuario = id_usuario
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono
        self.__fecha_registro = fecha_registro

    @property
    def id_usuario(self):
        return self.__id_usuario

    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self.__id_usuario = id_usuario
    
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, correo):
        self.__correo = correo

    @property
    def telefono(self):
        self.__correo
    
    @correo.setter
    def correo(self, correo):
        self.__correo = correo
    
    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, telefono):
        self.__telefono = telefono
    
    @property
    def fecha_registro(self):
        return self.__fecha_registro
    
    @fecha_registro.setter
    def fecha_registro(self, fecha_registro):
        self.fecha_registro = fecha_registro
    
    def __str__(self) -> str:
        return f"{self.id_usuario} - {self.nombre} - {self.correo} - {self.telefono} - {self.fecha_registro}"
