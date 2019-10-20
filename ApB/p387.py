# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
from pymongo import MongoClient
import datetime

# definimos los parámetros de conexión al servidor MongoDB
client = MongoClient('mongodb://localhost:27017/')

# abrimos la base de datos "hoteles"
db = client.hoteles

# accedemos a la colección "opiniones"
empleados = db.opiniones

# creamos una nueva opinión
opinion = {"autor": "Perico Martos",
           "texto": "Un lugar fantástico para disfrutar en familia.",
           "hotel": "Parador nacional",
           "lugar": "Cazalla de la Sierra",
           "creacion": datetime.datetime.utcnow()}

# la añadimos a la colección y obtenemos el ID asignado
opinion_id = opiniones.insert_one(opinion).inserted_id
