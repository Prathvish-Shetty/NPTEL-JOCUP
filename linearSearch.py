# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 12:16:26 2023

@author: Prathvish Shetty
"""

def linearSearch(n,x):
    list=[]
    for i in range(1,n):
        list.append(i)
    flag=0
    count=0
    for i in list:
        count+=1
        if i==x:

            print("Given number found at position:",i)
            flag=1
            break
    if flag==0:
        print("Number not found.")
    print("Number of iterations:",count)