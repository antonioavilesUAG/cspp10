import random



def get_p1_move():
    p1= input("what is your move rock,scizzors,paper: ")
    if p1 == "rock":
        return ("r")
    elif p1 == "scizzors":
        return ("s")
    elif p1 == "paper":
        return ("p")
get_p1_move() 
def get_comp_move():
    comp = 