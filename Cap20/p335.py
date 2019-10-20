# -*- coding: utf-8 -*-
"""
Created on Sat May 18 14:34:14 2019

@author: Arturo Sendero
"""

def enc_sim(msj, key=7):
    enc = bytearray()
    for b in msj:
        c = b ^ key
        enc.append(c)
    return enc
    
msj = bytearray("Me van a encriptar, olé", "utf-8")
msj = enc_sim(msj)
print(msj)
msj = enc_sim(msj)
print(msj.decode("utf-8"))

