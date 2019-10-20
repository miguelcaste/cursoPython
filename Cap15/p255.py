# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
def colores(paredes, techo, suelo):
    print('El color de las paredes es', paredes)
    print('El color del techo es', techo)
    print('El color del suelo es', suelo)
    
estilo1 = ('blanco', 'blanco', 'nogal')
colores(*estilo1)

estilo2 = {'paredes': 'naranja', 'techo': 'gris', 'suelo': 'negro'}
colores(**estilo2)