# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 18:08:00 2023

@author: Prathvish Shetty
"""

from PIL import Image
import random
end=100
def showBoard():
    img=Image.open("snakesNladders.jpg")
    img.show()
    
def checkLadder(points):
    if points==4:
        print("Ladder")
        return 14
    elif points==9:
        print("Ladder")
        return 31        
    elif points==20:
        print("Ladder")
        return 38        
    elif points==28:
        print("Ladder")
        return 84        
    elif points==40:
        print("Ladder")
        return 59        
    elif points==51:
        print("Ladder")
        return 67        
    elif points==63:
        print("Ladder")
        return 81        
    else:#not a ladder
        return points

def checkSnake(points):
    if points==17:
        print("Ladder")
        return 7
    elif points==64:
        print("Ladder")
        return 60        
    elif points==89:
        print("Ladder")
        return 26        
    elif points==95:
        print("Ladder")
        return 73        
    elif points==99:
        print("Ladder")
        return 78            
    else:#not a snake
        return points
   
def reachedEnd(points):
    if points==end:
        return True
    else:
        return False

def play():
    #input player1 name
    p1_name=input("Player1,Enter your name")
    #input player2 name
    p2_name=input("Player2,Enter your name")
    #initial points of player1
    pp1=0
    #initial points of player2
    pp2=0
    turn=0
    while(1):
        if turn==0:
            #player1 turn
            print(p1_name,"your turn")
            #ask player1 to choice to continue
            c=input("Press 1 to continue and 0 to quit:")
            if c=='0':
                print(p1_name,"scored",pp1)
                print(p2_name,"scored",pp2)
                print("Quitting the game.")
                break
            #generate a random number from 1 to 6
            dice=random.randint(1,6)
            print("dice showed:",dice)
            #add points
            pp1+=dice
            pp1=checkLadder(pp1)
            pp1=checkSnake(pp1)
            #check if the player goes beyond the board
            if pp1>end:
                pp1=end
                print(p1_name,"your score is ",pp1)
            if reachedEnd(pp1):
                print(p1_name,"won")
                break
        else:
            #player2 turn
            print(p2_name,"your turn")
            #ask player2 to choice to continue
            c=input("Press 1 to continue and 0 to quit:")
            if c=='0':
                print(p1_name,"scored",pp1)
                print(p2_name,"scored",pp2)
                print("Quitting the game.")
                break
            #generate a random number from 1 to 6
            dice=random.randint(1,6)
            print("dice showed:",dice)
            #add points
            pp2+=dice
            pp2=checkLadder(pp2)
            pp2=checkSnake(pp2)
            #check if the player goes beyond the board
            if pp2>end:
                pp2=end
            print(p2_name,"your score is ",pp2)
            if reachedEnd(pp2):
                print(p2_name,"won")
                break
        turn+=1
            

showBoard()
play()