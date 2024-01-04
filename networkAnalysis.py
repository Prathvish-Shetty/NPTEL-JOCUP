# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 19:48:39 2023

@author: Prathvish Shetty
"""

import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()
l=[1,2,3]
#G.add_node(1)
#G.add_node(2)
#G.add_node(3)
'''
G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(3,1)
print(G.nodes())
print(G.edges())
nx.draw(G)
plt.show()
'''
#G=nx.complete_graph(10)
G=nx.gnp_random_graph(20,0.5)
nx.draw(G)
plt.show()