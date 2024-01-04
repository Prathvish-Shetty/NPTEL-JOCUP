# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 10:13:09 2023

@author: Prathvish Shetty
"""

import random
year=random.randint(1999,2023)
print(year)
if year%4==0 and year%100!=0 or year%400==0:
    print("Leap year")
else:
    print("Not a Leap Year")