# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
import matplotlib.pyplot as plt
import networkx as nx

# Creamos un grafo aleatorio
G = nx.fast_gnp_random_graph(10, 0.5)

# Calculamos el grado de cada nodo
d = dict(nx.degree(G))
sizes = [v * 100 for v in d.values()]

# Calculamos agrupamientos
c = nx.clustering(G)
colors = [c[n] for n in G]

# Mostramos el grafo, con tamaño de nodo proporcional al grado
# y color según agrupamiento
nx.draw(G, nodelist=d.keys(), cmap=plt.get_cmap('viridis'), node_color=colors, node_size=sizes, with_labels=True)
plt.show()


