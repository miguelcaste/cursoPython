# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
alumnos = [('David', 5), ('Irene', 9), ('María', 6.5), ('Antonio', 4.2), ('Marta', 3.7)]
	
suma, aprobados, suspensos = 0, 0, 0
for nombre, nota in alumnos:
    suma += nota
    if nota >= 5:
        aprobados += 1
    else:
        suspensos += 1
print('Media:', suma/len(alumnos))
print(aprobados, 'aprobados')
print(suspensos, 'suspensos')
