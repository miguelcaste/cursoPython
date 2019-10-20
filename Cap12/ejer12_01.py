# -*- coding: utf-8 -*-

"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""

import re

# ^patron$ coincide con la cadena exacta patrón
# '28/10/1985' coincide con patrón
# 'El día 28/10/1985' no coincide con patrón puesto que la cadena completa no es una fecha,
# sino que la fecha forma parte de ella
regex_fecha_valida = re.compile(
        '''
        ^                           # Metacarácter ^ para asegurar que la fecha aparece al principio de la cadena
        (0[1-9]|[12][0-9]|3[01])    # Día en formato dd
        /                           # Barra /
        (0[1-9]|1[012])             # Mes en formato mm
        /                           # Barra /
        (19\d\d|20[0-1][0-9])       # Año en formato aaaa comprendido entre 1900 y 2019
        $                           # Metacarácter $ para asegurar que la fecha aparece al final de la cadena
        '''                         
        ,
        re.X)

# Lista de prueba
lista_fechas = ['22/03/1985', '0y/12/2000', '15/04/0985', '12/08/2019']

# Comprobamos si las fechas de la lista son válidas o no
for fecha in lista_fechas:
    if re.search(regex_fecha_valida, fecha): #Si la fecha cumple el patrón 
        print(fecha, "es una fecha válida.")
    else:
        print(fecha, "no es una fecha válida.")
    

