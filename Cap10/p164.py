# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
precios = [200.0, 125.99, 19.90, 37.50]
for i in range(len(precios)):
    precios[i] = precios[i] * 0.5
print(precios)

# Variante con comprensioón de listas
   
precios = [200.0, 125.99, 19.90, 37.50]
precios = [x*0.5 for x in precios]
print(precios)