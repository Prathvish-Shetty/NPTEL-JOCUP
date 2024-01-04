# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 11:41:30 2023

@author: Prathvish Shetty
"""
#recursion
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

#iteration
def fact(n):
    product=1
    for i in range(1,n+1):
        product=product*i
    return product
n=int(input("Enter any positive integer: "))
if n<0:
    print("Factorial is not defined on negative numbers.")
else:
    f=factorial(n)
    print("Factorial of n is",factorial(n))