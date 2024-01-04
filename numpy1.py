# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 19:21:54 2023

@author: Prathvish Shetty
"""

import numpy as np
a=np.array([1,2,3])
print(a)
print(type(a))
print(a.shape)
print(a[0],a[1],a[2])
a[1]=6
print(a)

b=np.array([[1,2,3],[4,5,6]])
print(b)
print(b.shape)

c=np.zeros((2,2))
print(c)

d=np.ones((2,2))
print(d)

e=np.full((2,2),6)
print(e)

f=np.random.random((2,2))
print(f)#random values from 0 to 1