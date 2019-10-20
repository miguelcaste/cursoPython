# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
# estos son los datos que vamos a solicitar para cada contacto
campos = ('nombre', 'apellidos', 'email', 'teléfono')

# esta lista contendrá todos los contactos
contactos = []

# inicialimos la variable 'seguir'
seguir = 's'

# mientras el valor de seguir sea 's' o 'S' introducimos contactos
while seguir in ('s', 'S'):
    
    # este diccionario almacena los valores de un contacto
    contacto = {}    
    
    # con este bucle preguntamos campo a campo
    for campo in campos:
        valor = input(campo + ': ')
        
        # si el usuario introduce algo, se almacena
        if len(valor) > 0:
            contacto[campo] = valor
    
    # añadimos el contacto a la lista
    contactos.append(contacto)
    
    # preguntamos si seguimos añadiendo contactos
    seguir = input('¿Introducir otro contacto? s/n:')
    
# mostramos todos los contactos
for contacto in contactos:
    
    for k, v in contacto.items():
        print(k + ': ' + v)
        
    # mostramos esto para facilitar la lectura
    print('------')

# solución 1    
contador = 0
for contacto in contactos:
    if 'email' in contacto:
        contador += 1
print(len(contactos), 'contactos en total')
print(contador, 'contactos tienen email')

# solución 2
contador = len([c for c in contactos if 'email' in c])
print(len(contactos), 'contactos en total')
print(contador, 'contactos tienen email')