# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""class Perro():
    
    especie = "Canis lupus"

    def __init__(self, nombre):
        self.nombre = nombre

    def traer_palo(self):
        print(self.nombre, "trae el palo")
        
    def ladrar():
        print("¡guau!") 