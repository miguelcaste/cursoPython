# -*- coding: utf-8 -*-

"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""

# Importamos la clase math para el cálculo del factorial
import math
 
# Lista de prueba
lista = [5,7,-9,'cadena']

# Recorremos la lista y mostramos el factorial de cada elemento siempre que sea posible
# En caso de que no sea posible, capturamos la excepción y mostramos un mensaje informativo 
for valor in lista:
    try:
        factorial = math.factorial(valor)
    except TypeError:
        print("Excepción TypeError: no se puede calcular el factorial para el tipo de dato", type(valor))
    except ValueError:
        print("Excepción ValueError: Factorial solo acepta valores enteros positivos", valor, "no es un valor entero positivo")
    else:
        print("El factorial de" ,valor, "es", factorial)
    finally:
        print("Valor", valor, "procesado")
