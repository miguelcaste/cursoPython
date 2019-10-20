# -*- coding: utf-8 -*-

"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""

import re

# Listamos los componentes del módulo re
componentes = dir(re)
# Creamos una expresión regular para buscar al final de una cadena la subcadena ch
regex_ch = re.compile(r'ch$')
# Lista de componentes terminados en ch
componentes_ch = []

for componente in componentes:
    # Si el componente termina en ch
    if(re.search(regex_ch, componente)):
        # Lo añadimos a la lista
        componentes_ch.append(componente)

# Mostramos la lista resultante
print("La lista de componentes del módulo re terminados en ch es la siguiente:", componentes_ch)
