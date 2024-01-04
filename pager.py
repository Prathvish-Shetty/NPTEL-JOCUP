# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 21:13:45 2023

@author: Prathvish Shetty
"""

import networkx as nx
import matplotlib.pyplot as plt
G=nx.read_edgelist("filelocation",create_using=nx.DiGraph(),nodetype=int)
nx.draw(G,with_labels=True)
plt.show()