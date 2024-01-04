# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:50:53 2023

@author: Prathvish Shetty
"""

import networkx as nx
import random
import matplotlib.pyplot as plt

def add_edges():
    nodes=list(G.nodes())
    for s in nodes:
        for t in nodes:
            if s!=t:
                r=random.random()
                if r<=0.5:
                    G.add_edges(s,t)      
    return G

def assign_points(G):
    nodes=list(G.nodes())
    p=[]
    for each in nodes:
        p.append(100)
    return p
    
def distribute_points(G,points):
    nodes=list(G.nodes())
    new_points=[]
    for i in range(len(nodes)):
        new_points.append(0)
    for n in nodes:
        out=list(G.out_edges(n))
        if len(out)==0:
            new_points[n]=new_points[n]+points[n]
        else:
            share=points[n]/len[out]
            for(src,tgt) in out:
                new_points[tgt]=new_points[tgt]+share
    return new_points

def keep_distributing(points,G):
    while(1):
        new_points=distribute_points(G,points)
        print(new_points)
        points=new_points
        stop=input("Press # to stop and any other key to continue: ")
        if stop=='#':
            break
        return new_points
    
def rank_by_points(final_points):
    d={}
    for i in range(len(points)):
        d[i]=points[i]
        print(sorted(d.items(),key=lamda f:f[1]))
        
#create a directed graph
G=nx.DiGraph()
G.add_nodes_from([i for i in range(10)])
G=add_edges()
#visualise the graph
nx.draw(G,with_labels=True)
plt.show()
#assign initial points
points=assign_points(G)
#keep distributing the points
final_points=keep_distributing(points,G)
#rank the nodes by points
rank_by_points(final_points)
#default networkx function
result=nx.pagerank(G)
print(sorted(result.items(),key=lamda f:f[1]))
