# -*- coding: utf-8 -*-

"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""

# Crea un archivo de texto con cualquier contenido y llámalo prueba.txt
# Después ejecuta este código y deja que Python muestre su contenido
f = open('prueba.txt', 'r')
print(f.read())
f.close()