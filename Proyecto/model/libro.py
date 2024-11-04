class Libro:
     def __init__(self, nombre, sku, autor, ano, categoria, disponibles):
          self.__nombre = nombre
          self.__sku = sku
          self.__autor = autor
          self.__ano = ano
          self.__categoria = categoria
          self.__disponibles = disponibles
     
     @property    
     def nombre(self):
          return self.__nombre # Get Method

     @nombre.setter 
     def nombre(self, nombre):
          self.__nombre = nombre

     @property
     def sku(self):
          return self.__sku # Get Method

     @sku.setter    
     def sku(self, sku):
          self.__sku = sku
     
     @property
     def autor(self):
          return self.__autor # Get Method

     @autor.setter     
     def autor(self, autor):
          self.__autor = autor

     @property
     def ano(self):
          return self.__ano # Get Method
           
     @ano.setter
     def ano(self, ano):
          self.__ano = ano
     
     @property
     def categoria(self):
          return self.__categoria # Get Method
          
     @categoria.setter
     def categoria(self, categoria):
          self.__categoria = categoria
     
     @property
     def disponibles(self):
          return self.__disponibles # Get Method
          
     @disponibles.setter
     def disponibles(self, disponibles):
          self.__disponibles = disponibles

     def __str__(self):
        return f"{self.nombre} - {self.sku} - {self.autor} - {self.ano} - {self.categoria} - {self.disponibles}"
