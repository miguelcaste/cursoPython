# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
def primos(limite):
    for x in range(limite):
        primo = True
        for y in range(2,x):
            if x % y == 0:
                primo = False
        if primo:
            yield x

print(primos(100))

for p in primos(100):
    print(p)
