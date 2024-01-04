# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 10:41:52 2023

@author: Prathvish Shetty
"""

import random

movies=["sholay","anand","drishyam","nayakan","lagaan","golmaal","vikram vedha","black friday","pk","koi mil gaya","dangal",
        "bajrangi bhaijaan","chakde india","gully boy","slumdog millionaire"]

def createqn(movie):
    n=len(movie)
    letters=list(movie)
    temp=[]
    for l in movie:
        if l==' ':
            temp.append(' ')
        else:
            temp.append('*')
    qn=''.join(str(x) for x in temp)
    return qn

def ispresent(letter,pickedMovie):
    c=pickedMovie.count(letter)
    if c==0:
        return False
    else:
        return True

def unlock(qn,movie,letter):
    n=len(movie)
    ref=list(movie)
    qnlist=list(qn)
    temp=[]
    for i in range(n):
        if ref[i]==' ' or ref[i]==letter:
            temp.append(ref[i])
        else:
            if qnlist[i]=='*':
                temp.append('*')
            else:
                temp.append(ref[i])
    qnnew=''.join(str(x) for x in temp)
    return qnnew
        

def play():
    pl1=input("Player1,Enter your name:")
    pl2=input("Player2,Enter your name:")
    point1=0
    point2=0
    turn=0
    
    willing=True
    while willing:
        if turn%2==0:
            print(pl1,"your turn")
            pickedMovie=random.choice(movies)
            qn=createqn(pickedMovie)
            print(qn)
            
            modifiedqn=qn
            notsaid=True
            while notsaid:
                letter=input("Enter letter:")
                if(ispresent(letter,pickedMovie)):
                    #unlock
                    modifiedqn=unlock(modifiedqn,pickedMovie,letter)
                    print(modifiedqn)
                    decision=input("Press '1' to guess the movie and '2' to unlock another character: ")
                    if decision=='1':
                        ans=input("Your answer: ")
                        if ans==pickedMovie:
                            point1+=1
                            print("Correct")
                            notsaid=False
                            print(pl1,"your score: ",point1)
                        else:
                            print("Wrong answer,Try again")
                else:
                    print("Letter not found")
            c=input("Press '1' to continue and '0' to quit: ")  
            if c=='0':
                print(pl1,"your score: ",point1)
                print(pl2,"your score: ",point2)
                input("Thanks for playing")
                willing=False
        else:
            print(pl2,"your turn")
            pickedMovie=random.choice(movies)
            qn=createqn(pickedMovie)
            print(qn)
            
            modifiedqn=qn
            notsaid=True
            while notsaid:
                letter=input("Enter letter:")
                if(ispresent(letter,pickedMovie)):
                    #unlock
                    modifiedqn=unlock(modifiedqn,pickedMovie,letter)
                    print(modifiedqn)
                    decision=input("Press '1' to guess the movie and '2' to unlock another character: ")
                    if decision=='1':
                        ans=input("Your answer: ")
                        if ans==pickedMovie:
                            point2+=1
                            print("Correct")
                            notsaid=False
                            print(pl2,"your score: ",point2)
                        else:
                            print("Wrong answer,Try again")
                else:
                    print("Letter not found")
            c=input("Press '1' to continue and '0' to quit")  
            if c=='0':
                print(pl1,"your score: ",point1)
                print(pl2,"your score: ",point2)
                input("Thanks for playing")
                willing=False
        turn+=1
    
  
play()



'''
import random

movies = [
    "sholay", "anand", "drishyam", "nayakan", "lagaan", "golmaal",
    "vikram vedha", "black friday", "pk", "koi mil gaya", "dangal",
    "bajrangi bhaijaan", "chakde india", "gully boy", "slumdog millionaire"
]

def create_question(movie):
    return ''.join([char if char == ' ' else '*' for char in movie])

def is_present(letter, picked_movie):
    return letter in picked_movie

def unlock(question, movie, letter):
    return ''.join([char if char == ' ' or char == letter else question[idx] for idx, char in enumerate(movie)])

def play():
    player1 = input("Player 1, Enter your name: ")
    player2 = input("Player 2, Enter your name: ")
    point1 = point2 = 0
    turn = 0

    while True:
        player = player1 if turn % 2 == 0 else player2
        print(player, "your turn")
        picked_movie = random.choice(movies)
        question = create_question(picked_movie)
        print(question)

        while True:
            letter = input("Enter letter: ")
            if is_present(letter, picked_movie):
                question = unlock(question, picked_movie, letter)
                print(question)
                decision = input("Press '1' to guess the movie and '2' to unlock another character: ")
                if decision == '1':
                    answer = input("Your answer: ")
                    if answer == picked_movie:
                        if player == player1:
                            point1 += 1
                        else:
                            point2 += 1
                        print("Correct!")
                        print(player, "your score:", point1 if player == player1 else point2)
                        break
                    else:
                        print("Wrong answer. Try again.")
            else:
                print("Letter not found.")
        
        continue_playing = input("Press '1' to continue and '0' to quit: ")
        if continue_playing == '0':
            print(player1, "your score:", point1)
            print(player2, "your score:", point2)
            print("Thanks for playing!")
            break
        
        turn += 1

play()
'''