# -*- coding: utf-8 -*-

"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""

lista_capitulos = [("Capítulo 1", "Los niños y la programación de ordenadores"), ("Capítulo 2", "Introducción a la programación"), ("Capítulo 3", "El lenguaje Python y por qué debemos aprenderlo")]

# Abrimos el archivo de texto en modo escritura
with open("archivo_apartado_a.txt", "w") as f:
    # Escribimos cada capítulo junto con su título en una línea, 
    # separando ambos por un guión
    for cap, titulo in lista_capitulos:
        f.write(cap + "-" + titulo + "\n")

# Creamos la lista que tenemos que generar a partir del archivo
lista_generada = []
# Abrimos el archivo de texto en modo lectura
with open("archivo_apartado_a.txt", "r") as f:
    # Recorremos todas las líneas del archivo
    for linea in f.readlines():
        # Eliminamos de cada línea el \n final y después separamos su contenido
        # en capítulo y título utilizando el carácter guión
        cap, titulo = linea.strip().split("-")
        # Añadimos la tupla (cap, titulo) a la lista
        lista_generada.append((cap, titulo))
# Mostramos la lista generada para comprobar que su contenido es el mismo 
# que el de la lista lista_capitulos
print(lista_generada)