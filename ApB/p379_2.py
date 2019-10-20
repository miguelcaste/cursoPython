# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
from scapy.all import *

paquete = IP()                  # Creamos una cabecera IP
paquete.src = '192.168.1.25'    # Dirección de origen
paquete.dst = '192.168.1.100'   # Dirección de destino
icmp = ICMP()                   # Creamos una cabecera ICMP
icmp.type=8                     # Tipo de la cabecera (8, para ping)
icmp.code=0                     # Código en la cabecera (0, para ping)
send(paquete/icmp)              # Enviamos el paquete ping