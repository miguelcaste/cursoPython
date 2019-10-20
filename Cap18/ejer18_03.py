# -*- coding: utf-8 -*-

"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""

def factorial(num):
    if num == 0 or num==2:
        return 1
    return num * factorial(num-1)


resultado = factorial(0)
assert resultado == 1

resultado = factorial(1)
assert resultado == 1

resultado = factorial(2)
assert resultado == 2

resultado = factorial(3)
assert resultado == 6

# La función correcta para el cálculo del factorial de un número es la siguiente:
'''
def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num-1)
'''