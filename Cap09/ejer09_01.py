# -*- coding: utf-8 -*-

"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""

# Solicitamos al usuario su edad
edad_usuario = int(input("Introduce tu edad: "))
# Solicitamos al usuario la edad de su mejor amigo
edad_mejor_amigo = int(input("Introduce la edad de tu mejor amigo: "))

# Comprobamos quién de los dos es mayor y mostramos por pantalla un mensaje informativo
if edad_usuario > edad_mejor_amigo:
    print("Tú eres mayor que tu amigo.")
elif edad_usuario < edad_mejor_amigo:
    print("Tu mejor amigo es mayor que tú.")
else:
    print("Tu mejor amigo y tú tenéis la misma edad.")
