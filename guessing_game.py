import random

round = 0
compscore=0
playerscore=0

def guessing_game(n):
    global round,compscore,playerscore
    if round < 5:
        round += 1
        computer = random.randint(1,5)
    
        if n==computer:
            playerscore+=1
            return round,"Win",computer,playerscore,compscore
        else:
            compscore+=1
            return round,"Lost",computer,playerscore,compscore
    elif round >=5:
        round = 0