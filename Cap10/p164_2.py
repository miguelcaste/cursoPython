# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
edades = [23, 32, 19, 22, 25, 30, 27]
mayores = [x for x in edades if x > 25]
print('Hay', len(mayores), 'mayores de 25 años')