# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 12:49:08 2023

@author: Prathvish Shetty
"""

def binarySearch(l,x,start,end):
    #base case : 1 element present
    if start==end:
        if l[start]==x:
            return start
        else:
            return -1
    else:
        #divide the list into 2 halves
        mid=(start+end)//2
        if l[mid]==x:
            return mid
        elif l[mid]>x:
            #left half
            return binarySearch(l, x, start, mid-1)
        else:
            #right half
            return binarySearch(l, x, mid+1, end)
l=[10,20,30,40,50,60,70,80,90]
x=int(input("Enter search key: "))
index=binarySearch(l, x, 0, len(l)-1)
if index==-1:
    print(x,"not found.")
else:
    print(x,"found at index",index+1)