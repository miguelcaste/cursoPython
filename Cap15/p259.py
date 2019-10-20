# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
def comparaciones(tipo):
    
    def mayor(a, b):
        if a > b:
            return a
        return b
    
    if tipo == 'mayor':
        return mayor
    
    if tipo == 'menor':
        return lambda x, y: x if x < y else y
    
f = comparaciones('mayor')
print(f(10, 7))
f = comparaciones('menor')
print(f(10, 7))