# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
import requests

url = 'https://github.com'
r = requests.get(url)
for c in r.cookies.items():
    print(c[0], ":", c[1])
