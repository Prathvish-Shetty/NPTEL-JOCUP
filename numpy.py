# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 14:06:17 2023

@author: Prathvish Shetty
"""

import numpy as np

x=np.array([1,2])
print(x.dtype)

y=np.array([1.0,2.0])
print(y.dtype)

z=np.array([[1,2],[3,4]],dtype=np.int64)
a=np.array([[5,6],[7,8]],dtype=np.int64)
print(np.add(z,a))

print(a-z)
print(np.subtract(a,z))
print(a*z)
print(np.divide(a,z))
print(np.multiply(a,z))
print(np.sqrt(a))

print(a.T)
print(np.sum(a,axis=0))#column wise
print(np.sum(a,axis=1))#row wise
