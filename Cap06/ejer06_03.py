# -*- coding: utf-8 -*-

"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""

# Definimos las variables con los valores del problema
efectivo_inicial = 50
precio_camisa = 35
descuento = 10
# Calculamos el precio final de la camisa
precio_final_camisa = precio_camisa - (precio_camisa*descuento/100)
# Calculamos el dinero que nos quedará después de comprar la camisa
efectivo_final = efectivo_inicial - precio_final_camisa
# Mostramos por pantalla el dinero que nos quedará = 18.5€
print(efectivo_final)