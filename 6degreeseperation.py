# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 16:35:08 2023

@author: Prathvish Shetty
"""

import networkx as nx
import numpy as np

G=nx.read_edgelist("filename")
#to find length of shortest path
N=list(G.nodes())
#shortestpathlengthlist
spll=[]
for u in N:
    for v in N:
        if u!=v:
            l=nx.shortest_path_length(G,u,v)
            print("Shortest path between",u,"and",v,"is of length",l)
            spll.append(l)
#minimum shortest path length
min_spl=min(spll)
max_spl=max(spll)
#average shortest path length
avg_spl=np.average(spll)
print("Minimum shortest path length",min_spl)
print("Maximum shortest path length",max_spl)
print("Average shortest path length",avg_spl)
