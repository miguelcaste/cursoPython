# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
# inicializamos la pila
acciones = []

# guardamos las acciones del usuario
acciones.append("escribir 'h'")
acciones.append("escribir 'o'")
acciones.append("escribir 'y'")
acciones.append("negrita 'hoy'")

# mostramos el contenido de la pila
print(acciones)

# deshacemos el último cambio y ponemos en cursiva
print("sacamos:", acciones.pop())
acciones.append("cursiva 'hoy'")

# mostramos estado final de la pila
print(acciones)