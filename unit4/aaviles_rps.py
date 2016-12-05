import random



def get_p1_move():
    p1move= input("what is your move rock,scissor,paper: ")
    if p1move == "rock":
        return ("r")
    elif p1move == "scissor":
        return ("s")   
    elif p1move == "paper":
        return ("p")
# print(get_p1_move())

def get_comp_move():
    cmove = random.randint(1,3)
    if cmove == 1:
        return ("r")
    elif cmove == 2:
        return ("s")
    elif cmove == 3:
        return ("p")
# print(get_comp_move())

def get_rounds():
    rounds = int(input("Pick a number between 1 to 9: "))
    return (rounds)
# print (get_rounds())  

def get_round_winner(p1move, cmove):
    if cmove == "p" and p1move == "r":
        return("computer")
    elif cmove == "s" and p1move == "p":
        return ("computer")
    elif cmove =="r" and p1move == "s":
        return ("computer")
    elif cmove == "p" and p1move == "s":
        return ("player")
    elif cmove == "s" and p1move == "r":
        return("player")
    elif cmove == "r" and p1move == "p":
        return("player")
    else: 
        return("tie")

def get_full_move(shortmove):
    if shortmove == "r":
        return ("rock")
    elif shortmove == "p":
        return ("paper")
    elif shortmove == "s":
        return ("scissor")

def print_score(pscore, cscore, ties): 
    print("Player score is {}".format(pscore))
    print("Computer score is {}".format(cscore))
    print("ties is {}".format(ties))

def rps():
    player = 0 
    computer = 0
    ties = 0
    round = get_rounds()
    for x in range(1, round):
        p1move = get_p1_move()
        cmove = get_comp_move()
    
        print("Player move is {}".format(p1move))
        print("Computer move is {}".format(cmove))
        winner = get_round_winner(p1move, cmove)
        if winner == "player":
            print("Player won!")
            player = player + 1
        elif winner == "computer":
            print("Computer won")
            computer = computer + 1
        else:
            print("tie")
            ties = ties + 1
        print("Players score is {}".format(player))
        print("Computer score is {}".format(computer))
        print("Ties are {}".format(ties))
        
rps()