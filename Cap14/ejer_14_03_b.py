# -*- coding: utf-8 -*-

"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""

import pickle

lista_capitulos = [("Capítulo 1", "Los niños y la programación de ordenadores"), ("Capítulo 2", "Introducción a la programación"), ("Capítulo 3", "El lenguaje Python y por qué debemos aprenderlo")]

# Abrimos el archivo binario en modo escritura
with open("archivo_apartado_b.p", "wb") as f:
    # Escribimos en él el objeto lista_capitulo
    # haciendo uso del método dump del módulo pickle
    pickle.dump(lista_capitulos, f)

# Abrimos el archivo binario en modo lectura
with open("archivo_apartado_b.p", "rb") as f:
    # Cargamos el objeto que contiene en la lista que tenemos que generar
    lista_generada = pickle.load(f)
# Mostramos la lista generada para comprobar que su contenido es el mismo 
# que el de la lista lista_capitulos
print(lista_generada)