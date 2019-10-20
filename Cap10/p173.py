# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
ensalada = {'lechuga', 'tomate', 'cebolla', 'aceite', 'vinagre', 'sal'}
verduras = {'brócoli', 'tomate', 'cebolla', 'apio', 'lechuga'}
condimentos = {'pimienta', 'curcuma', 'aceite', 'vinagre', 'sal'}
print('La ensalada se hace con', len(ensalada), 'ingredientes:')
print(len(verduras & ensalada), 'verduras y', len(condimentos & ensalada), 'condimentos')

