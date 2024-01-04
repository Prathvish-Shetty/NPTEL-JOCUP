import random
def choose():
    words=['computer','mouse','keyboard','printer','monitor','wire','information','technology','english','science']
    word=random.choice(words)
    return word
def jumble(word):
    jumbledword="".join(random.sample(word,len(word)))
    return jumbledword
    
def play():
    player1=input("Player 1,Enter your name : ")
    player2=input("Player 2,Enter your name : ")
    score1=0
    score2=0
    turn=0
    choice=1
    while choice==1:
        pickedword=choose()
        jumbledword=jumble(pickedword)
        print("Guess the word:",jumbledword)
        if turn%2==0:
            guess1=input(player1+" Your turn: ")
            if guess1==pickedword:
                print("You are Right")
                score1+=1
            else:
                print("You are wrong")
            choice=int(input("Enter '1' to continue and '0' to discontinue : "))
            if choice==0:
                print(player1,",Your score is",score1,'\n',player2,"Score is",score2)
                break
        else:
            guess2=input(player2+" Your turn: ")
            if guess2==pickedword:
                print("You are Right")
                score1+=1
            else:
                print("You are wrong")
            choice=int(input("Enter '1' to continue and '0' to discontinue : "))
            if choice==0:
                print(player1,",Your score is",score1,'\n'+player2,"Score is",score2)
                break
        turn+=1

    
play()