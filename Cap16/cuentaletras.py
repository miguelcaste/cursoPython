# -*- coding: utf-8 -*-

"""Módulo que permite contar las vocales y consonantes de una cadena"""

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

import re

def contar_vocales(texto):
    """Calcula el total de vocales que tiene un texto"""
    return len(re.findall("[aeiouáéíóíúü]", texto, re.IGNORECASE))

def contar_consonantes(texto):
    """Calcula el total de consonantes que tiene un texto"""
    return len(re.findall("[bcdfghjklmnñpqrstvwxyz]", texto, re.IGNORECASE))

if __name__ == "__main__":
    cadena = input("Escribe una cadena: ")
    vocales = contar_vocales(cadena)
    consonantes = contar_consonantes(cadena)
    print("La cadena", cadena, "tiene", vocales, "vocales y", consonantes, "consonantes.")
