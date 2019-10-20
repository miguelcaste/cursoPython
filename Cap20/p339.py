# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
import sys
import functools

def ayuda():
    print("Uso: opera <operación> valor1 valor2 valor3...")
    print("<operación> puede ser 'suma' o 'producto'")
    exit()

if __name__ == "__main__":
    resultado = 0
    try:
        if len(sys.argv) < 3:
            ayuda()
        else:
            valores = [int(x) for x in sys.argv[2:]]
            if sys.argv[1] == "suma":
                resultado = sum(valores)
            elif sys.argv[1] == "producto":
                resultado = functools.reduce(lambda x, y: x*y, valores)
            else:
                print("Operación inválida")
                ayuda()
    except ValueError:
        print("Dato inválido")
        ayuda()
    print(sys.argv[1], ':', resultado)
