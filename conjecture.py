# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 21:54:42 2023

@author: Prathvish Shetty
"""

def checkNum(num):
    iterations=1
    while(num!=1):
        if num%2==0:
            num=num//2
            iterations+=1
        else:
            num=(num*3)+1
            iterations+=1
    print(num,iterations)
    
checkNum(20)