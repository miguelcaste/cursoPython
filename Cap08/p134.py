# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
for elemento in ['cerrado', 'cerrado', 'cerrado', 'cerrado', 'cerrado', 'cerrado', 'cerrado']:
    if elemento == 'abierto':
        print('Avisar a la policía')
        break
else:
    print('Todo en orden')