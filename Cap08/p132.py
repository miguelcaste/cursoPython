# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
sabores = ['chocolate', 'vainilla', 'fresa']
for s1 in range(len(sabores)):
    for s2 in range(s1+1, len(sabores)):
        print('Helado de', sabores[s1], 'con', sabores[s2])
