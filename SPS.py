# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 13:33:43 2023

@author: Prathvish Shetty
"""

def RockPaperScissor(num1,num2,bit1,bit2):
    p1=int(num1[bit1])%3
    p2=int(num2[bit2])%3
    if pl1[p1]==pl2[p2]:
        print("Draw")
    elif pl1[p1]=="Rock" and pl2[p2]=="Scissor":
        print("Player 1 wins")
    elif pl1[p1]=="Rock" and pl2[p2]=="Paper":
        print("Player 2 wins")
    elif pl1[p1]=="Paper" and pl2[p2]=="Scissor":
        print("Player 2 wins")
    elif pl1[p1]=="Paper" and pl2[p2]=="Rock":
        print("Player 1 wins")
    elif pl1[p1]=="Scissor" and pl2[p2]=="Rock":
        print("Player 2 wins")
    elif pl1[p1]=="Scissor" and pl2[p2]=="Paper":
        print("Player 1 wins")
        
pl1={0:"Rock",1:"Paper",2:"Scissor"}
pl2={0:"Scissor",1:"Rock",2:"Paper"}
while 1:
    num1=input("Player1,Enter your choice: ")
    num2=input("Player2,Enter your choice: ")
    bit1=int(input("Player1,Enter your secret bit position: "))
    bit2=int(input("Player1,Enter your secret bit position: "))
    RockPaperScissor(num1,num2,bit1,bit2)
    ch=input("Do you want to continue? y/n : ")
    if ch=='n':
        break
