import random


def roll2dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print("Roll was {} and {}. Equal to {}".format(dice1, dice2, dice_sum))
    return dice_sum

#function name: get_bets 
#agurment: bank 
#purpose to be able to place a bet with money the player has
#return: the amount of money they bet
def get_bet(bank):
    bet = (int(input("Place your bet: ")))
    if bet <= bank:
        print (bet)
    elif bet != bank:
        print(int(input("You don't have that amount place another bet: ")))

#function name: get_first_phase
#argument:
#purpose: to set the wining numbers
#returns: the wining number for phase one.
def get_first_phase(dice_sum):
    if dice_sum == 7 or dice_sum == 11:
        return("player wins")
    elif dice_sum == 2 or dice_sum == 3 or dice_sum == 12:
        return("computer wins")
    else:
        return point_number

def get_point_number(dice_sum, point_number):
    if dice_sum == point_number:
        return ("player wins")
    elif dice_sum == 7:
        return("computer wins")
    else:
        return("reroll")

def craps():
    bank = 100
    roll = roll2dice()
    bet = get_bet(bank)
    while bank >= 0:
        bet = get_bet(bank)
        phase_one = get_first_phase()   
        if phase_one == "player wins":
            print("you win")
        elif phase_one == "computer wins":
            print ("computer wins")
        else:
            get_point_number(dice_sum)
            

craps()