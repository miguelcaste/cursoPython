# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
def extrae(valores, comp):
    a = valores[0]
    for x in valores[1:]:
        if comp(x, a):
            a = x
    return a

def mayor(a, b):
    return a > b

def menor(a, b):
    return a < b

print(extrae([2, 3, 6, 8, 10], mayor))
print(extrae([2, 3, 6, 8, 10], menor))
