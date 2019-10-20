# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
from gensim.corpora import WikiCorpus
from gensim.models.word2vec import  Word2Vec
from gensim.utils import deaccent

# Leemos el volcado descargado de Wikipedia
corpus = WikiCorpus('eswiki-latest-pages-articles.xml.bz2', dictionary=False)
 
# Quitamos tildes
texts = [deaccent(t) for t in corpus.get_texts()]
 
# Definimos el algoritmo a utilizar y sus hiperparámetros
model = Word2Vec(size=400, window=5, min_count=5)
 
# Generamos el vocabulario
model.build_vocab(texts)
 
# Entrenamos el modelo
model.train(texts, chunksize=500)
 
# Lo guardamos en disco para su uso posterior
model.save('eswikipedia_w2v_model')
