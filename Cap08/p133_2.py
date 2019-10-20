# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
for d in range(1,31):
    print('----')
    print('Día', d)
    if d % 7 == 6 or d % 7 == 0:
        print('Descansar')
        continue
    print('Levantarse temprano')
    print('Ir a trabajar')
