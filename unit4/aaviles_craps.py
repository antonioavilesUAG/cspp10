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
        return dice_sum

def get_point_number(dice_sum):
    dice3 = random.randint(1,6)
    dice4 = random.randint(1,6)
    point_number = dice3 + dice4
    print("Roll was {} and {}.".format(dice3,dice4))
    if point_number == dice_sum:
        return("player wins")
    elif point_number == 7:
        return("computer wins")
    else:
        return("reroll")
def craps():
    bank = 100
    while bank >= 0:
        roll = roll2dice()
        bet = get_bet(bank)
        dice_sum = roll
        phase_one = get_first_phase(dice_sum)
        second_phase = get_point_number(dice_sum)
        if phase_one == "player wins":
            print("player win")
            bank = bank + bet
            print("Your bank is {}".format(bank))
        elif phase_one == "computer wins":
            print("computer wins")
            bank = bank - bet
            print("Your bank is {}".format(bank))
        elif phase_one == "reroll":
            print("going to point number phase")
        elif second_phase == "player wins":
            print("Player won")
            bank = bank + bet
            print("Your bank is {}".format(bank))
        elif second_phase == "computer wins":
            print("Computer won")
            bank = bank - bet
            print("Your bank is {}".format(bank))
craps()



