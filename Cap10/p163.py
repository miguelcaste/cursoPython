# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
from collections import deque

# iniciamos la cola
cola = deque()

# llegan 5 clientes a la cola
for i in range(5):
    cliente = 'cliente ' + str(i+1)
    print('Llega', cliente)
    cola.append(cliente)
    print('Cola:', cola)
        
# salen todos los clientes de la cola
while len(cola) > 0:
    print('Sale', cola.popleft())
    print('Quedan:', cola)