# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
def reservar(destino, precio=1000):
    print('Ha reservado un viaje a %s por %d euros' % (destino, precio))

reservar('Sevilla')                      # 1 argumento por posición
reservar('Sevilla', 500)                 # 2 argumentos por posición
reservar('Sevilla', precio=800)          # 1 por posición y 1 por clave
reservar(destino='París')                # 1 por clave
reservar(destino='Londres', precio=900)  # 2 por clave
