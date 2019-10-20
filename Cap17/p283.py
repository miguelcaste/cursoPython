# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
class Televisor():
    
    __num_canales = 55

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
