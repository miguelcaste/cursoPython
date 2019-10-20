# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
def nombre(e):
    return e['nombre']

def edad(e):
    return e['edad']

l = [{'nombre': 'Pili', 'edad': 12}, {'nombre': 'Mili', 'edad':14}, {'nombre': 'Beorn', 'edad': 300}]

print(sorted(l, key=nombre))
print(sorted(l, key=edad))
print(l)
l.sort(key=edad)
print(l)