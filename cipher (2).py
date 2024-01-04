# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 15:13:33 2023

@author: Prathvish Shetty
"""

import string
dict={}
for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]]=string.ascii_letters[i-1]
print(dict)