# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
alumnos = ['Juan', 'Mark', 'Arturo', 'Ana', 'Pilar', 'Salud']

parejas_posibles = [(alumnos[i], alumnos[j]) for i in range(len(alumnos)) for j in range(i, len(alumnos)) if alumnos[i] != alumnos[j]]
print(parejas_posibles)
print(len(parejas_posibles), 'en total')