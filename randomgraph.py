# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 16:32:40 2023

@author: Prathvish Shetty
"""

import networkx as nx
import matplotlib.pyplot as plt
G=nx.gnp_random_graph(50,.3) 
nx.draw(G)
plt.show()
print(G.nodes())
print(G.edges)
print(G.degree(0))
Gb=nx.barabasi_albert_graph(50,2)
nx.draw(Gb)
plt.show()
nx.write_gexf(Gb,"analysis1.gexf ")
