# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
class Dispositivo:
    """ Clase dispositivo, para objetos conectados a la red """
    
    # Atributo con valor por defecto
    encendido = False
    
    def __init__(self, IP):
        """ Constructor """
        # Atributo con valor definido al crear el objeto
        self.IP = IP
        
    def __del__(self):
        """ Destructor """
        print("Destruyendo dispositivo en", self.IP)
        
    def encender(self):
        """ Enciende el dispositivo """
        self.encendido = True
        
    def apagar(self):
        """ Apaga el dispositivo """
        self.encendido = False
        
    def estado(self):
        """Genera una cadena con el estado actual del dispositivo """
        mensaje = f"IP: {self.IP}\n"
        if self.encendido:
            mensaje += 'Estado: encendido'
        else:
            mensaje += 'Estado: apagado'
        return mensaje
    
    def enciende_dispositivos(lista_dispositivos):
        for d in lista_dispositivos:
            d.encender()
        

    