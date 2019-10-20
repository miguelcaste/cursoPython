# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
class InvalidNameException(Exception):
    def __init__(self, valor):
        self.valor = valor
    
    def __str__(self):
        return "Error: " + str(self.valor)

nombres = ['Turing', 'Feynman', '', 'Tintin', 'G']
for n in nombres:
    try:
        if len(n) < 2:
            raise InvalidNameException(n)
        print(n)
    except InvalidNameException:
        pass
        