# -*- coding: utf-8 -*-

"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""

try:
    # Definimos una lista con 10 elementos
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
    # Mostramos la lista
    print(lista) 
    # Bucle infinito hasta error
    while True:
        print('Elemento a borrar',lista[-1])
        # La lista debe tener al menos 3 elementos
        assert len(lista) > 2        
        # Borramos el último elemento de la lista
        lista.pop()        
        # Mostramos la lista después del borrado
        print(lista)
# Excepción para assert
except AssertionError:  
    print('Error al intentar borrar un elemento  ')
    print('La lista debe contener al menos 3 elementos')
