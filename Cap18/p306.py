# -*- coding: utf-8 -*-

"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""

class MiExcepcion(Exception):
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return "Error: " + str(self.valor)

try:
    fin = False
    while not fin:
        entrada = input("Introduzca c para continuar o f para finalizar:")
        if entrada != "f" and entrada != "c":
            raise MiExcepcion(entrada + " no es un valor válido.")
        elif entrada == "f":
            fin = True
except MiExcepcion as e:
    print (e)