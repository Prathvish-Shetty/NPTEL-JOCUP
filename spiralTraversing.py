# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 19:26:27 2023

@author: Prathvish Shetty
"""

def spiral(m,n,a):
    k=0
    l=0
    '''
    m and n are number of rows and columns
    k=index of starting row
    l=index of starting column
    '''
    while(k<m and l<n):
        #printing the first row 
        for i in range(l,n):
            print(a[k][i],end=' ')
        k+=1
        #printing the last column
        for i in range(k,m):
            print(a[i][n-1],end=' ')
        n-=1
        if k<m:
            #printing the last row
            for i in range(n-1,l-1,-1):
                print(a[m-1][i],end=' ')
            m-=1
        if n<n:
            #printing the first column
            for i in range(m-1,k-1,-1):
                print(a[i][l],end=' ')
                l+=1
                
a=[]
count=1
for i in range(4):
    l=[]
    for j in range(4):
        l.append(count)
        count+=1
    a.append(l)
spiral(4,4,a)     