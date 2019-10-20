# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
lluvia_mensual = [65, 70, 87, 62, 44, 14, 5, 5, 24, 50, 57, 69]
meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
max_lluvia = max(lluvia_mensual)
mes_max = lluvia_mensual.index(max_lluvia)
print('El mes más lluvioso ha sido', meses[mes_max], 'con', max_lluvia, 'litros')

