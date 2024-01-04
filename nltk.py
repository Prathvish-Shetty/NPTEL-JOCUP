# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 19:24:11 2023

@author: Prathvish Shetty
"""

papers={"Madison":[10,14,37,38,39,40,41,42,43,44,45,46,47,48],
       "Hamilton":[1,6,7,8,9,11,12,13,15,16,17,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,59,60,61,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85],
       "Jay":[2,3,4,5],
       "Shared":[18,19,20],
       "Disputed":[49,50,51,52,53,54,55,56,57,58,62,63]}

def read_files(filename):
    strings=[]
    for file in filename:
        with open(r"C:\Users\Prathvish Shetty\.spyder-py3\PyPrograms\stylometry-federalist{file}.txt") as f:
            strings=f.append(f.read())
    return ("\n".join(strings))
federalist_by_author={}
for author,files in papers.items():
    federalist_by_author[author]=read_files(files)  
for author in papers:
    print(federalist_by_author[author][:100])      