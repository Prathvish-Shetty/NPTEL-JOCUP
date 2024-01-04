# -*- coding: utf-8 -*-
"""
Given a string S, write a function replaceV that accepts a string and replace the occurrences of 3 consecutive vowels with _ in that string. Make sure to return the answer string.

Input:

aaahellooo

Output:

_hell_

Explanation:

Since aaa and ooo are consecutive 3 vowels therefor replaced by _ .
"""

def replaceV(str):
  if "aaa" or "eee" or "iii" or "ooo" or "uuu" in str:
    str=str.replace("aaa",'_')
    str=str.replace("eee",'_')
    str=str.replace("iii",'_')
    str=str.replace("ooo",'_')
    str=str.replace("uuu",'_')
  return str
S = input()
print(replaceV(S))


'''
Given a list L, write a program to shift all zeroes in list L towards the right by maintaining the order of the list. Also print the new list.

Input:

[0,1,0,3,12]

Output:

[1,3,12,0,0]

Explanation:

There are two zeroes in the list which are shifted to the right and the order of the list is also maintained. (1,3,12 are in order as in the old list.)

for item in L:
  if item==0:
    L.remove(0)
    L.append(0)
print(L,end='')

'''