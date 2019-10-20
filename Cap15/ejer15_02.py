# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
def ordenar(l):
    def intercambia(l, a, b):
        x = l[a]
        l[a] = l[b]
        l[b] = x
    
    for i in range(len(l)-1,1,-1):
        for j in range(i):
            if l[j] > l[j+1]:
                intercambia(l, j, j+1)
    

l = [7, 3, 9, 5, 4, 2, 8, 10]
ordenar(l)
print(l)
