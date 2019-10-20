# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
from bokeh.plotting import figure, output_file, show

# preparamos los datos
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 3, 5]

# la visualización irá a un archivo HTML
output_file("lineas.html")

# creamos la gráfica
p = figure(title="ejemplo simple", x_axis_label='x', y_axis_label='y')

# dibujamos una línea con los datos
p.line(x, y, legend="Temp.", line_width=2)

# lanzamos el navegador para ver e interactuar con la gráfica
show(p)

