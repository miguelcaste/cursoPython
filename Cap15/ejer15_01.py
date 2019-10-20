# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
def cifrar(mensaje):
    desp = 4
    cif = "".join([chr(ord(c)+desp) for c in mensaje])
    return cif

def descifrar(mensaje):
    desp = 4
    desc = "".join([chr(ord(c)-desp) for c in mensaje])
    return desc

mensaje = "tomate"
print('Original:', mensaje)
cifrado = cifrar(mensaje)
print('Cifrado:', cifrado)
descifrado = descifrar(cifrado) 
print('Descifrado:', descifrado)