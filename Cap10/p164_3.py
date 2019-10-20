# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
chicos = ['Juan', 'Mark', 'Arturo']
chicas = ['Ana', 'Pilar', 'Salud']

parejas_posibles = [(x, y) for x in chicas for y in chicos]
print(parejas_posibles)