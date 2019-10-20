# -*- coding: utf-8 -*-

"""Módulo que permite concatenar cadenas y dividir una cadena en subcadenas"""

"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""

__author__ = "Arturo y Salud"
__copyright__ = "Curso de programación Python"
__credits__ = "Arturo y Salud"
__license__ = "GPL"
__version__ = "1.0"
__email__ = "libropython@gmail.com"
__status__ = "Development"

def concatenar(cadena1, cadena2):
    """Concatena dos cadenas"""
    return cadena1 + cadena2

def dividir(cadena, separador):
    """Divide una cadena en subcadenas utilizando el separador indicado"""
    return cadena.split(separador)   