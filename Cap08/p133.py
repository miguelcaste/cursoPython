# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
num = 811
test = 'es primo'

for i in range(1000):
    for div in range(2, num):
        if num % div == 0:
            test = 'no es primo'
            break

print(num, test)

