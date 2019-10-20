# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
def nuevo_pedido(producto, precio, descuento=0):
    print('Pedido de', producto, 'por valor de', precio, 'y descuento de', descuento*100, '%')

nuevo_pedido('probeta', 5, 0.25)
#	Correcto.

nuevo_pedido()
#	Incorrecto. Los dos primeros parámetros son obligatorios (no tienen valor por defecto asociado). 

nuevo_pedido('libro')
#	Incorrecto. Solo se indica el primero de los dos parámetros obligatorios.

nuevo_pedido('lupa', 12)
#	Correcto.

nuevo_pedido(producto='pinzas', 10)
#	Incorrecto. Después de un argumento por clave no puede ir uno sin clave.

nuevo_pedido(producto='láser', precio=25)
#	Correcto.

nuevo_pedido(producto='telescopio', descuento=0.2, precio=25)
#	Correcto.

pedido = ('laptop', 1200, 0.6)
nuevo_pedido(pedido)
#	Incorrecto.

pedido = {'producto': 'calculadora', 'valor': 19.99, 'descuento': 0}
nuevo_pedido(pedido)
# Incorrecto
