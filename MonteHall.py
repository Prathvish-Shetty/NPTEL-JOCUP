import random
doors = [0] * 3
goatDoor = []
swap = 0  # Number of swap wins
noswap = 0  # Number of noswap wins
j=0
while j<10:
    x = random.randint(0,2)  # xth box will comprise of BMW
    doors[x] = "BMW"
    for i in range(0,3):
        if i == x:
            continue
        else:
            doors[i] = "Goat"  # Assign "Goat" to doors that don't have BMW
            goatDoor.append(i)
    choice = int(input("Enter your choice: "))
    doorOpen = random.choice(goatDoor)  # Open a door that contains a goat
    while doorOpen == choice:  # Ensure the opened door is not the participant's choice
        doorOpen = random.choice(goatDoor)
    ch = input("Do you want to swap? 'y' or 'n': ")
    if ch == 'y':
        if doors[choice] == "Goat":  # Check if the chosen door contains a goat
            print("Player Wins")
            swap += 1
        else:
            print("Player Lost")
    else:
        if doors[choice] == "Goat":  # Check if the chosen door contains a goat
            print("Player Lost")
        else:
            print("Player Wins")
            noswap += 1
    j+=1

print("Swap wins =", swap)
print("Noswap wins =", noswap)
