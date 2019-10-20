# -*- coding: utf-8 -*-

"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""

import cadenas

if __name__ == "__main__":
    cadena1 = "coche,"
    cadena2 = "moto,"
    cadena3 = "bicicleta"
    
    cadena_concatenada = cadenas.concatenar(cadena1, cadena2)
    cadena_concatenada = cadenas.concatenar(cadena_concatenada, cadena3)
    
    cadenas_resultantes = cadenas.dividir(cadena_concatenada, ",")
    
    print("Las cadenas resultantes son:\n" + '\n'.join(cadenas_resultantes))
    