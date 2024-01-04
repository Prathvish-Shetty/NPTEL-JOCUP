# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 19:49:11 2023

@author: Prathvish Shetty
"""
#define infinity float('inf')
#print("string"*n)
'''
import this
print(this)

import random
bet=int(input("Your Bet from 1 to 10: "))
luckyDraw=random.randint(1,10)
print("Lucky Draw: ",luckyDraw)
account=0
if bet==luckyDraw:
    account=account+900-100
else:
    account=account-100
print(account)
'''
import matplotlib.pyplot as plt
import random

x=[]
y=[]
account=0
for i in range(7):
    x.append(i+1)
    bet=random.randint(1,10)
    luckyDraw=random.randint(1,10)
    print("Bet: ",bet)
    print("Lucky Draw: ",luckyDraw)
    if bet==luckyDraw:
        account=account+900-100
    else:
        account=account-100
    y.append(account)
    print("Amount in your game account is",account)
plt.plot(x,y)
plt.show()
