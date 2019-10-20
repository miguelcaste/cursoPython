# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
from sympy import *

# polinomio
x, y = symbols('x y')
expr = x + 2*y
print("Polinomio:", expr)

# resolución de una integral
expr = exp(x)*sin(x) + exp(x)*cos(x)
sol = integrate(expr, x)
print("Solución integral:", sol)


