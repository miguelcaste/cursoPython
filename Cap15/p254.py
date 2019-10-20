# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
def reserva(origen, destino, *viajeros, **detalles):
    print(f'Se ha reservado el vuelo de {origen} a {destino} para:')
    for viajero in viajeros:
        print(viajero)
    print('Con los siguientes detalles:')
    for k in detalles:
        print(k, ':', detalles[k])
    
reserva('Granada', 'México', 'Pedro', 'Juani', 'Luisa', 
        comida='vegana', asientos='ventanilla', precio=350)