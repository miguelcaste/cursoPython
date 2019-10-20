# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
import numpy as np
from scipy import special, optimize
import matplotlib.pyplot as plt

f = lambda x: -special.jv(3, x)
sol = optimize.minimize(f, 1.0)
x = np.linspace(0, 10, 5000)
plt.plot(x, special.jv(3, x), '-', sol.x, -sol.fun, 'o')
plt.savefig('plot.tif', dpi=96)




