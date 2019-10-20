# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
from sklearn import datasets, svm

# cargamos la colección de datos
digits = datasets.load_digits()

# creamos un clasificador con el algoritmo SVM
clf = svm.SVC(gamma=0.001, C=100.)

# entrenamos con todas las imágenes menos la última
clf.fit(digits.data[:-1], digits.target[:-1])

# predecimos el número que representa la última imagen
pred = clf.predict(digits.data[-1:])
print(pred)



