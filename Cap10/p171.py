# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
texto = "ja ja ja ja ja qué gracioso eres"
palabras = set(texto.split())
print('El texto "', texto, '" contiene', len(palabras), 'palabras diferentes:')
for p in palabras:
    print(p)