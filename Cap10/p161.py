# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 06:31:49 2019

@author: Arturo Sendero
"""
pila_acciones = []
while programa_en_ejecución()
    accion = leer_acción()
    if accion = 'deshacer':
        accion = pila_acciones.pop()
        deshacer_accion(accion)
    else:
        pila_acciones.append(accion) 
        ejecutar_accion(accion)