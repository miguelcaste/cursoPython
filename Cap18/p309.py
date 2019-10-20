# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
import unittest

def tokenizar(texto):
    return texto.split()

class Test(unittest.TestCase):

    def test_espacios(self):
        self.assertEqual(len(tokenizar('uno dos tres')), 3)
    def test_punto(self):
        self.assertEqual(len(tokenizar('uno.dos tres')), 3)
    def test_coma(self):
        self.assertEqual(len(tokenizar('uno dos,tres')), 3)

if __name__ == '__main__':
    unittest.main()