class Televisor():
    
    __num_canales = 55
    modelo = "Samsung 123"

    def __init__(self):
        self.__canal = 0

    @property
    def canal(self):
        return self.__canal
    
    @canal.setter
    def canal(self, valor):
        self.__canal = valor
        if self.__canal == self.__num_canales:
            self.__canal = 0
        elif self.__canal == -1:
            self.__canal = self.__num_canales - 1
        elif self.__canal > self.__num_canales:
            self.__canal = self.__num_canales - 1
        elif self.__canal < 0:
            self.__canal = 0
        
    @canal.deleter
    def canal(self):
        del self.__canal
        
    def __str__(self):
        """ Devuelve una descripción del televisor """
        return f"Televisor en canal {self.__canal} de {self.__num_canales} posibles"
    
    