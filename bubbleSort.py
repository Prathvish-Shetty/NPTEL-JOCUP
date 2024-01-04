# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 11:39:11 2023

@author: Prathvish Shetty
"""

def bubbleSort(a):
    n=len(a)
    for i in range(n):
        for j in range(n-i-1):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
    for i in a:
        print(i)
a=[10,9,8,7,6,5,4,3,2,1]
bubbleSort(a)     
    