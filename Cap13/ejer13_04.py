# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
texto = 'abracadabra'

frecuencias = {}
for l in texto:
    frecuencias[l] = frecuencias.get(l, 0) + 1
print(frecuencias)