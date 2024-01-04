# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 12:51:56 2023

@author: Prathvish Shetty
"""

def binarySearch(n,x):
    a=[]
    for i in range(1,n+1):
        a.append(i)
    firstPosition=0
    lastPosition=len(a)-1
    flag=0
    count=0
    while(firstPosition<=lastPosition and flag==0):
        count+=1
        midPosition=(firstPosition+lastPosition)//2
        if x==a[midPosition]:
            flag=1
            print("The element is present at position"+str(midPosition))
            print("The number of iterations are:",count)
            return
        else:
            if x<a[midPosition]:
                lastPosition=midPosition-1
            else:
                firstPosition=midPosition+1
    print("The number is not present.")

    
    