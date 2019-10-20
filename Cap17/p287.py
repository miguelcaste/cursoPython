# -*- coding: utf-8 -*-
"""
Created on Fri May 10 07:32:09 2019

@author: Arturo Sendero
"""

class Dispositivo:
    """ Clase dispositivo, para objetos conectados a la red """
        
    def __init__(self, IP):
        """ Constructor """
        self.__IP = IP        # Atributo con valor definido 
        self.__encendido = False   # Atributo con  valor por defecto
        
    def __del__(self):
        """ Destructor """
        print("Destruyendo dispositivo en", self.__IP)
        
    def encender(self):
        """ Enciende el dispositivo """
        self.__encendido = True
        
    def apagar(self):
        """ Apaga el dispositivo """
        self.__encendido = False
        
    def estado(self):
        """Genera una cadena con el estado actual del dispositivo """
        mensaje = f"IP: {self.__IP}\n"
        if self.__encendido:
            mensaje += 'Estado: encendido'
        else:
            mensaje += 'Estado: apagado'
        return mensaje
        
class Bombilla(Dispositivo):
    
    def __init__(self, IP):
        super().__init__(IP) # llamada al constructor de la superclase
        self.__intensidad = 1
    
    def mas_intensidad(self):
        self.__intensidad = min(5, self.__intensidad+1)
        
    def menos_intensidad(self):
        self.__intensidad = max(1, self.__intensidad-1)

    def __str__(self):
        mensaje = super().estado()
        mensaje += f"\nIntensidad: {self.__intensidad}"
        return mensaje
            
class Tableta(Dispositivo):
    
    def __init__(self, IP):
        super().__init__(IP)
        self.__bateria = 0

    def cargar(self):
        self.__bateria = 100
        
    def encender(self):
        if self.__bateria > 0:
            super().encender()
        
    def __str__(self):
        mensaje = super().estado()
        mensaje += f"\nBatería: {self.__bateria}"
        return mensaje
    