# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 21:09:41 2023

@author: Prathvish Shetty
"""
'''
F-Friendship
L-Love
A-Affection
M-Marrage
E-Enemy
S-Siblings

compare 2 names
eliminate common letters
count number of letters remaining
count the number through flames and eliminate the letters untill one letter remains always start from the eliminated one
modular counting-clockwise
'''

'''
import string
s="Raj"
print(s.lower())
//raj
print(s.upper())
//RAJ
sl=list(s)
print(sl)
['R', 'a', 'j']
print(s.replace('j','#'))
Ra#
print(s.replace("aj",'#'))
R#
//replace function is case sensitive

'''

'''
l=['a','b','c','d','e'.'f']
l[1:4]//slicing
print(l.index('d'))//gives index of first occurence of an element
'''


import string

def remove_matching_letter(l1,l2):
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i]==l2[j]:
                l1.remove(l1[i])
                l2.remove(l2[j])
                l=l1+['*']+l2
                return [l,True]
    l=l1+['*']+l2
    return [l,False]
    
p1=input("Enter first person name: ")
p1=p1.lower()
p1=p1.replace(' ','')
p2=input("Enter second person name: ")
p2=p2.lower()
p2=p2.replace(' ','')
l1=list(p1) 
l2=list(p2)
proceed=True
while proceed:
    ret_list=remove_matching_letter(l1,l2)
    con_list=ret_list[0]
    proceed=ret_list[1]
    star_index=con_list.index('*')
    l1=con_list[:star_index]
    l2=con_list[star_index+1:]
    
count=len(l1)+len(l2)
result=["Friends","Love","Affection","Marrage","Enemy","Siblings"]

while len(result)>1:
    split_index=(count%(len(result)))-1
    if split_index>=0:
        right=result[split_index+1:]
        left=result[:split_index]
        result=right+left
    else:
        result=result[:len(result)-1]
print(result[0])