import random
 
# function for rolling 2 dice
# name: roll2dice
# arguments: none
# returns: the sum
def roll2dice():
    # generate a random number from 1 to 6
    dice1 = random.randint(1,6)  
    # generate another random number from 1 to 6
    dice2 = random.randint(1,6)
    # get the sum of the two rolls
    dice_sum = dice1 + dice2
    # print the sum
    print("Roll was a {} and {}. And the some is {}") 
    # return the sum
    return(dice_sum)
# function for getting a user's bet
# name: get_bet
# arguments: bank - current player balance
# returns: the bet
def get_bet(bank):
    # ask the player how much they want to bet
    bet = (int(input("How much do you want to bet: ")))
    # if player's bet is more than they have
    #   available in bank, then get new bet
    if bet <= bank:
        print(bet)
    # if player's bet is valid, then return
    #   the bet
    elif bet != bank:
        print(int(input("You don't have that amount of money. place another bet: ")))
    # if player's bet is valid, then return
get_bet()
# function that finds the range given a dice roll
# name: get_range
# arguments: sum of dice
# returns: the range:
#           "over7" if over 7
#           "under7" if under 7
#           "equal7" if equal to 7
def get_range(dice_sum):
    # if the sum is over 7, return "over7"
   
    # if the sum is under 7, return "under7"
   
    # if the sum is 7, return "equal7"
 
# function for getting the user's choice of range
# name: choose_range
# arguments: none
# returns: player's choice of range
#       "over7", "under7", or "equal7"
def choose_range():
    # present user with choices "over7", "under7",
    #   or "equal7"
   
    # return their choice
 
# function for the main game