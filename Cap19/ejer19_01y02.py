# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
from tkinter import *
import tkinter.ttk as ttk
from webfrec import *

max_frec = 20

def descargar(*args):
    """ Esta función se invoca al pulsar en el botón 'Descargar' """
    text = descargar_pagina(url.get())
    textcomp.replace(1.0, END, text)
    
def contar(*args):
    frec_items = contar_palabras(textcomp.get(1.0, END))
    for entry in tree.get_children():
        tree.delete(entry)
    for k,v in frec_items[:max_frec]:
        tree.insert("", "end", values=(k, v))
    
root = Tk()
root.title("Analizador de páginas web")

# Marco principal
mainframe = ttk.Frame(root, padding="5 5 5 5")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

#
# Marco para dirección web y botón de descarga
#
urlframe = ttk.Frame(mainframe)
urlframe.grid(column=1, row=1, sticky=W, pady="5 0")

# Etiqueta
ttk.Label(urlframe, text="Dirección:").grid(column=1, row=1, sticky=W)

# Campo de dirección web
url = StringVar()
urlentry = ttk.Entry(urlframe, width=83, textvariable=url)
urlentry.grid(column=2, row=1, sticky=W, padx="5 0")

# Botón de descarga
button = ttk.Button(urlframe, text="Descargar", command=descargar)
button.grid(column=3, row=1, sticky=W, padx="5 0")

# Botón de cuenta
button = ttk.Button(urlframe, text="Contar", command=contar)
button.grid(column=4, row=1, sticky=W, padx="5 0")

#
# Marco para mostrar datos de la página
#
showframe = ttk.Frame(mainframe)
showframe.grid(column=1, row=2, pady="5 0")

ttk.Label(showframe, text="Texto:").grid(column=1, row=1, sticky=W)
ttk.Label(showframe, text="Tabla de frecuencias:").grid(column=3, row=1, sticky=W)

# Lienzo de texto donde mostrar contenido
content = StringVar()
textcomp = Text(showframe, width=80, height=26)
textcomp.grid(column=1, row=2, sticky=W)

# Barra de desplazamiento para el área de texto
scrollbar = ttk.Scrollbar(showframe, command=textcomp.yview)
scrollbar.grid(column=2, row=2, sticky="wns")
textcomp['yscrollcommand'] = scrollbar.set

# Tabla donde se muestran las palabras más frecuentes
tree = ttk.Treeview(showframe, height=max_frec, columns=("pal", "frec"))
tree.grid(column=3 , row=2, sticky=(W, N), padx="5 0")
tree.column("#0", width=0, minwidth=0, stretch=NO)
tree.column("pal", width=100, minwidth=100, stretch=NO)
tree.column("frec", width=70, minwidth=70, stretch=NO)
tree.heading("pal", text="Palabra",anchor=W)
tree.heading("frec", text="Frecuencia",anchor=W)

# Configuración final
urlentry.focus()
root.bind('<Return>', descargar)
root.resizable(width=False, height=False)
root.mainloop()