# -*- coding: utf-8 -*-

"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""

# Pedimos al usuario que introduzca un número entero
numero = int(input("Introduce un número entero: "))
# Mostramos los 5 números siguientes justificados a la derecha
print("Los 5 números siguientes son: ")
justificacion = numero + 5
for i in range(5):
    numero += 1
    print(str(numero).rjust(justificacion))
