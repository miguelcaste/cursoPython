# -*- coding: utf-8 -*-

"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""

import re

# La bandera re.I (IGNORECASE) permite realizar búsquedas sin distinguir entre mayúsculas y minúsculas
regex_palabras_terminadas_os_as = re.compile(r'\w*os|\w*as', re.I)

cad = "TodOS los días estoy deseando leer un nuevo capítulo del libro."

lista_palabras_terminadas_os_as = re.findall(regex_palabras_terminadas_os_as, cad)

print(lista_palabras_terminadas_os_as)