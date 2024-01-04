# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 13:16:02 2023

@author: Prathvish Shetty
"""

#basecase=anchor value
'''
0th fibo no=0
1st fibo no=1
2nd fibo no=1
3nd fibo no=2
4th fibo no=3
5th fibo no=5
......
'''
def fibonacci(n):
    if n<2:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input("Enter a positive number: "))
if n<0:
    print("Fibonacci numbers are undefined for negative numbers: ")
else:
    print("Fibonacci number at position",n,"is",fibonacci(n))