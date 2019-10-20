# -*- coding: utf-8 -*-

"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""

# Definimos las variables con los valores del problema
saldo_inicial = 3000
salario_mensual = 1100
gastos_fijos_mensuales = 435
saldo_final = 6000
# Calculamos los gastos extra correspondientes al año
gastos_extra = saldo_inicial + salario_mensual*12 - gastos_fijos_mensuales*12 - saldo_final
# Calculamos los gastos extra mensuales
gastos_extra_mensuales = gastos_extra/12
# Mostramos por pantalla los gastos extra mensuales = 415€
print(gastos_extra_mensuales)