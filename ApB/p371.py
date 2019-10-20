# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
from keras.models import Sequential
from keras.layers import Dense

# nuestra red neuronal apilará capas de manera secuencial
model = Sequential()

# añadimos una capa densa, con activación ReLU y 64  neuronas
model.add(Dense(units=64, activation='relu', input_dim=100))

# capa final para clasificación multiclase sobre 10 categorías
model.add(Dense(units=10, activation='softmax'))

# compilamos el modelo
model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])

# entrenamos con ejemplos de entrenamiento ya etiquetados
model.fit(x_train, y_train, epochs=5, batch_size=32)

# ya podemos clasificar nuevos ejemplos
classes = model.predict(x_test, batch_size=128)



