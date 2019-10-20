# -*- coding: utf-8 -*-

"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""

def fib(num):
    if num < 2:
        return num
    else:        
        return fib(num-1) + fib(num-2)

resultado = fib(0)    
assert resultado == 0

resultado = fib(1)    
assert resultado == 1

resultado = fib(2)    
assert resultado == 1

