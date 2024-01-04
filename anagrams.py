# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 09:57:09 2023

@author: Prathvish Shetty
"""

str1=input("Enter the First string: ")
str2=input("Enter the Second string: ")
print(sorted(str1))
print(sorted(str2))
if sorted(str1)==sorted(str2):
    print("These are Anagrams")
else:
    print("These are not Anagrams")