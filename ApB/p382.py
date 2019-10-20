# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
import spacy

texto = """Tanto conocimiento me asombra, Sir Bedevere. Explicadme de nuevo cómo puede evitarse un cataclismo con la vejiga de una oveja"""
nlp = spacy.load('es_core_news_sm')
doc = nlp(texto)
for token in doc:
    print(token.text, token.pos_, token.dep_)
