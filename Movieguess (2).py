movies=[
    "Sholay",
    "Mughal-e-Azam",
    "Dilwale Dulhania Le Jayenge",
    "3 Idiots",
    "Lagaan",
    "Bahubali: The Beginning",
    "Kabhi Khushi Kabhie Gham",
    "Gangs of Wasseypur",
    "PK",
    "Koi Mil Gaya",
    "Dangal",
    "Bajrangi Bhaijaan",
    "Chakde! India",
    "Gully Boy",
    "Slumdog Millionaire"
]
def play():
    p1name=input("Player 1,Enter your name: ")
    p2name=input("Player 2,Enter your name: ")
    score1=0
    score2=0
    turn=0
    willing=True
    while willing:
        if turn%2==0:
            #player1
            print(p1name,",your Turn")
            pickedMovie=random.choice(movies)
            qn=createquestion(picked)
            print(qn)
            
    
play()