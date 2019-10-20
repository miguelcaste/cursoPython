# -*- coding: utf-8 -*-

"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""

import re

#\d{3} indica que deben aparecer 3 números seguidos
regex_telefono = re.compile(r'\d{3}-\d{3}-\d{3}')

texto = '''
Cliente: Antonio Martínez - Contacto: 678-376-290\n
Cliente: María Pérez - Contacto: 654-910-243\n
Cliente: Sara Merino - Contacto: 696-973-510\n
'''

texto_reemplazado = re.sub(regex_telefono, "teléfono", texto)

print(texto_reemplazado)
