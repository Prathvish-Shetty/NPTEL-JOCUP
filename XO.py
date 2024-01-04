# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 16:12:20 2023

@author: Prathvish Shetty
"""

import numpy
board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
p1s='X'
p2s='O'

def place(symbol):
    print(numpy.matrix(board))
    while 1:
        row=int(input("Enter row-1/2/3: "))
        col=int(input("Enter column-1/2/3: "))
        if row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='-':
            break
        else:
            print("Invalid Input,Please Enter again.")
    board[row-1][col-1]=symbol

def checkRows(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if board[r][c]==symbol:
                count+=1
        if count==3:
            print(symbol,"Won")
            return True
    return False

def checkCols(symbol):
    for c in range(3):
        count=0
        for r in range(3):
            if board[r][c]==symbol:
                count+=1
        if count==3:
            print(symbol,"Won")
            return True
    return False
        
def checkDiag(symbol):
    if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[2][0]==symbol:
        print(symbol,"Won")
        return True
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[2][2]==symbol:
        print(symbol,"Won")
        return True
    return False

def won(symbol):
    return checkRows(symbol) or checkCols(symbol) or checkDiag(symbol)
    
def play():
   for turn in range(9):
       if turn%2==0:
           print("X turn")
           place(p1s)
           if won(p1s):
               break
       else:
           print("O turn")
           place(p2s)
           if won(p2s):
               break
   if not(won(p1s)) and not(won(p2s)):
         print("Draw")
    
play()