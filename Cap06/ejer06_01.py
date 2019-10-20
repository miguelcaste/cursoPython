# -*- coding: utf-8 -*-

"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""

# Calculamos los km recorridos
# distancia = 2 viajes/día * 15 km/viaje * 20 días = 600 km
distancia = 2*15*20
# Calculamos los litros consumidos
# litros = 600 km * 5.5 litros/100 km = 33 litros
litros = distancia/100*5.5
# Calculamos el gasto
# gasto = 33 litros * 1.12€/litro = 36.96€
gasto = litros * 1.12
# Mostramos el gasto por pantalla
print(gasto)