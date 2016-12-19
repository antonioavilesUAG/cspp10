import random


def roll2dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print("Roll was {} and {}. Equal to {}".format(dice1, dice2, dice_sum))
    return dice_sum

#function name: bank 
#agurment: none
#purpose :how much money the player has.
#return a amount. 
def get_player_bank():
    bank = 100
    return bank
#function name: get_bets 
#agurment: bank 
#purpose to be able to place a bet with money the player has
#return: the amount of money they bet
def get_bet(bank):
    bet = (int(input("Place your bet: ")))
    if bet <= bank:
        return("Your bet was {}".format(bet))
    elif bet != bank:
        print(int(input("You don't have that amount place another bet: ")))

#function name: get_first_phase
#argument:
#purpose: to set the wining numbers
#returns: the wining number for phase one.
def get_first_phase(dice_sum):
    if dice_sum == 7 or dice_sum == 11:
        print("Player wins")
    elif dice_sum == 2 or dice_sum == 3 or dice_sum == 12:
        print("Computer wins")
    else:
        return point_number
get_first_phase()

def get_point_number(point_number):
    if dice_sum = point_number:
        print ("player wins")
    elif 