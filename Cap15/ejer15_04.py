# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
def suma(L):
    if len(L) == 0:
        return 0
    return L[0] + suma(L[1:])

print(suma(range(10)))