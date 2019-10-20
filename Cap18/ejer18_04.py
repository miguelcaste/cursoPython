# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
import unittest

def formatea_nombre(nombre):
    return " ".join([x[0].upper() + x[1:] for x in nombre.split()])

class Test(unittest.TestCase):

    def test_nombre_apellido(self):
        self.assertEqual(formatea_nombre('theon greyjoy'), 'Theon Greyjoy')
    def test_nombre_2apellido(self):
        self.assertEqual(formatea_nombre('antonio muñoz molina'), 'Antonio Muñoz Molina')
    def test_puntos(self):
        self.assertEqual(formatea_nombre('ursula k. le guin'), 'Ursula K. Le Guin')
    def test_nombre_castizo(self):
        self.assertEqual(formatea_nombre('calderón de la barca'), 'Calderón de la Barca')
    def test_nombre_guion(self):
        self.assertEqual(formatea_nombre('alberto vázquez-figueroa'), 'Alberto Vázquez-Figueroa')

if __name__ == '__main__':
    unittest.main()
