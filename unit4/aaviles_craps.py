import random


def roll2dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print("The roll is {} {}".format(dice1,dice2))
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
    bank = (int(input("Place your bet: ")))
    if bank <= 100:
        return bank:
    elif bank != 100:
        print(int(input("You don't have that amount place another bet: ")
get_bet(bank)
        
#function name: get_first_roll
#agurment: point_number
#purpose: de
#returns: 


#OPTION 2
# function name: roll_result
#   purpose: get the result of the roll
#   arguments: 
#       roll - the sum of the two dice rolled
#       is_first_roll - true/false depending on which roll it is
#   returns: the result
#       if player wins: return "win"
#       if player lost: return "lose"

