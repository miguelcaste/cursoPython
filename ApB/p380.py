# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
from nltk.corpus import cess_esp as cess
from nltk import UnigramTagger as ut

# Leemos un corpus etiquetado en español
cess_sents = cess.tagged_sents()

# Entrenamos el etiquetador
uni_tag = ut(cess_sents)

texto = """Tanto conocimiento me asombra, Sir Bedevere. Explicadme de nuevo cómo puede evitarse un cataclismo con la vejiga de una oveja"""

tokens = nltk.word_tokenize(texto)
print(tokens)
tagged = uni_tag.tag(tokens)
print(tagged[0:6])


