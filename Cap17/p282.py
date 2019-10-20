# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
class Televisor():
    
    __canal = 0
    __num_canales = 55

    def __ajusta_canal(self, canal):
        self.__canal = canal % self.__num_canales
            
    def siguiente_canal(self):
        self.__ajusta_canal(self.__canal + 1)      
        
    def anterior_canal(self):
        self.__ajusta_canal(self.__canal - 1)
        
    def cambia_canal(self, canal):
        if canal > self.__num_canales:
            self.__canal = self.__num_canales - 1
        elif canal < 0:
            self.__canal = 0
        else:
            self.__canal = canal
        
    def canal_actual(self):
        return self.__canal

    