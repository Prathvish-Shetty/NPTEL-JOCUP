# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 15:13:33 2023

@author: Prathvish Shetty
"""

import string
dict={}
data=""
file=open("opcipher.txt","w")
for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]]=string.ascii_letters[i-1]
with open("ipcipher.txt") as f:
    while True:
        c=f.read(1)
        if not c:
            print("End of file.")
            break
        if c in dict:
            data=dict[c]
        else:
            data=c
        file.write(data)
        print(data)
file.close()