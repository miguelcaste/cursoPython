# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
lista = [6, 3, 7, 8, 2, 4]
	
a = reduce(lambda x, y: x+y, lista)

b = lista[0]
for x in lista[1:]:
    b = b + x

print(a == b)
