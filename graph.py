# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 18:27:47 2023

@author: Prathvish Shetty
"""

import networkx as nx
U=nx.Graph()#undirected graph
G=nx.DiGraph()
G.nodes()
G.add_nodes_from([i for i in range(5)])#[0,1,2]
G.nodes()
list(G.nodes())
G.edges()
G.out_edges()
G.in_edges()
G.add_edge(1,2)
G.out_edges(1)
G.in_edges(1)
G.add_edge(1,2)
G.add_edge(0,3)
G.add_edge(2,3)
G.add_edge(3,2)
G.add_edge(3,4)
G.add_edge(4,1)
list(G.out_edges(2))
list(G.out_edges(3))
list(G.in_edges(3))