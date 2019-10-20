# -*- coding: utf-8 -*-

"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""

print("Programa para calcular el área de un rectángulo.")
base = float(input("Introduce la base: "))
altura = float(input("Introduce la altura: "))
area = base * altura

# Salida con paso de valores como parámetros
print("El área del rectángulo de base ", base, " y altura ", altura, " es: ", area)

# Salida mediante concatenación de cadenas de texto
print("El área del rectángulo de base " + str(base) + " y altura " + str(altura) + " es: " + str(area))

# Salida utilizando el operador %
print("El área del rectángulo de base %.2f y altura %.2f es: %.2f" % (base, altura, area))

# Salida empleando la función str.format()
print("El área del rectángulo de base {0} y altura {1} es: {2}".format(base, altura, area))

# Salida utilizando F-strings
print(f"El área del rectángulo de base {base} y altura {altura} es: {area}")

