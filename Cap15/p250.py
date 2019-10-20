# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
def apuntar(nombre, miembros=[]):
    miembros.append(nombre)
    return miembros
    
print(apuntar('Juan'))
print(apuntar('Ana'))
print(apuntar('Salud'))

# ejemplo adicional

print(apuntar('Jorgito', []))
print(apuntar('Juanito'))
