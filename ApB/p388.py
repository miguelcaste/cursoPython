# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
ejemplos = [('Juan', 23), ('María', 56), ('Darío', 7)]	

def mayor_edad(a, b):
    if a[1] > b[1]:
        return a
    return b

def mayor_nombre(a, b):
    if len(a[0]) > len(b[0]):
        return a
    return b

def test_mayor_edad():
    assert mayor_edad(ejemplos[0], ejemplos[1]) == ejemplos[1] 
 
def test_mayor_nombre():
    assert mayor_nombre(ejemplos[0], ejemplos[2]) == ejemplos[2] 
