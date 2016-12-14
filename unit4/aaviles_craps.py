import random


def roll2dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    return("The roll is {}+{}".format(dice1,dice2))
    
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
        return bet
    elif bet != bank:
        print(int(input("You don't have that amount place another bet: ")))
get_bet(100)
        
#function name: get_first_phase
#argument: point_number
#purpose: to set the wining numbers
#returns: the wining number for phase one.
def get_first_phase():
    if dice_sum == 2 or dice_sum == 7:
        return("Player wins")
    elif dice_sum == 2 or dice_sum == 3 or dice_sum == 12:
        return("Computer wins")
#OPTION 2
# function name: roll_result
#   purpose: get the result of the roll
#   arguments: 
#       roll - the sum of the two dice rolled
#       is_first_roll - true/false depending on which roll it is
#   returns: the result
#       if player wins: return "win"
#       if player lost: return "lose"

