# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 11:14:19 2023

@author: Prathvish Shetty
"""

def recursive(L):
    if not L:  # Base case: if the list is empty, return 1
        return 1
    else:
        return L[-1]*recursive(L[:-1])
print(recursive([1,2,3,4,5,6,7,8,9,10]))