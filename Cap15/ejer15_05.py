# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
casas = ['stark', 'lannister', 'bolton', 'greyjoy', 'targaryen']

print(list(map(lambda x: x[0].upper() + x[1:], casas)))