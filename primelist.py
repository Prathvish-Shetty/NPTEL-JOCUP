# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 19:47:48 2023

@author: Prathvish Shetty
"""


L = [int(i) for i in input().split()]
for i in L:
  c=0
  for j in range(1,i+1):
    if i%j==0:
      c+=1
  if c==2:
    print(i,end='')
    break
