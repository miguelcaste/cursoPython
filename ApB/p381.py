# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
from textblob import TextBlob

text = '''
The titular threat of The Blob has always struck me as the 
ultimate movie monster: an insatiably hungry, amoeba-like mass 
able to penetratevirtually any safeguard, capable of--as a doomed 
doctor chillingly describes it--"assimilating flesh on contact.
Snide comparisons to gelatin be damned, it's a concept with the 
most devastating of potential consequences, not unlike the grey 
goo scenario proposed by technological theorists fearful of
artificial intelligence run rampant.
'''

blob = TextBlob(text)
print("Etiquetas: ", blob.tags) 
print("Sintagmas nominales:", blob.noun_phrases) 
print("Polaridad:")
for sentence in blob.sentences:
    print(sentence, " = ", sentence.sentiment.polarity)

