# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
import numpy as np 

print('Primer array:')
a = np.arange(9, dtype = np.float_).reshape(3,3) 
print(a) 
print('\n')

print('Segundo array:')
b = np.array([10,10,10]) 
print(b)
print('\n')

print('Suma dos arrays:')
print(np.add(a,b))
print('\n')  

print('Resta dos arrays:')
print(np.subtract(a,b))
print('\n')  

print('Multiplica dos arrays:')
print(np.multiply(a,b))
print('\n')  

print('Dividie dos arrays:')
print(np.divide(a,b))

