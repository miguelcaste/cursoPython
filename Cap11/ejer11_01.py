# -*- coding: utf-8 -*-

"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""

# Solicitamos una cadena por teclado y la almacenamos
cadena = input("Escriba una cadena de caracteres: ")
# Pasamos la cadena a minúscula
cadena = cadena.lower()
# Si el carácter inicial es igual al final
if cadena[0] == cadena[-1]:
    # Calculamos el número de caracteres distintos a ellos
    caracteres_distintos = len(cadena) - cadena.count(cadena[0])
    # Creamos una cadena con el mensaje a imprimir
    mensaje = f"La cadena introducida tiene {caracteres_distintos} caracteres distintos a los caracteres inicial y final."
else: # Si el carácter inicial es distinto al final
    # Calculamos el número de caracteres iguales al carácter inicial (sin incluirlo)
    caracteres_iguales_inicio = cadena.count(cadena[0])-1
    # Calculamos el número de caracteres iguales al carácter final (sin incluirlo)
    caracteres_iguales_fin = cadena.count(cadena[-1])-1
    # Calculamos el número de caracteres iguales al carácter inicial y al final (sin incluirlos)
    total_caracteres_iguales = caracteres_iguales_inicio + caracteres_iguales_fin
    # Creamos una cadena con el mensaje a imprimir
    mensaje = f"La cadena introducida tiene {total_caracteres_iguales} caracteres iguales a los caracteres inicial y final."
# Imprimimos por pantalla el mensaje adecuado    
print(mensaje)
