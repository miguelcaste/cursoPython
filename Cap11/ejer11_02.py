# -*- coding: utf-8 -*-

"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""

# Cadena a modificar
cadena = "Mi nombre es Paula"
# Las cadenas son inmutables y no se pueden modificar
# Las listas sí son mutables
# Generamos una lista resultante de dividir la cadena por espacios
lista_cadenas = cadena.split()
# Modificamos el cuarto elemento por nuestro nombre
lista_cadenas[3] = "Pepita"
# Utilizamos el método join para unir las cadenas de la lista utilizando espacios
cadena = " ".join(lista_cadenas)
# Mostramos la cadena
print(cadena)
