import random
#username = input("Set a username: ")#
#password = (int(input("Set a password that is numbers only: ")))#

#print("you must verify your self")#

#username2 = input("Put in your username: ")#
#password2 = (int(input("Put in your password: ")))# 
#if username == username2 and password == password2:#
    #print("You may enter your email")#
#else:
    #print("This email is not yours")#
def get_bet(bank):
    bet = (int(input("How much you want to bet: ")))
    if bet <= bank:
        return(bet)
    elif bet != bank:
        return(int(input("You dont have that. Place new bet: ")))
def get_guess(): 
    player1 = (int(input("What cap is the bottle in out of the 3 caps: ")))
    return player1
def get_comp_move():
    dealer = random.randint(1,4)
    if dealer == 1:
        return 1
    elif dealer == 2:
        return 2
    elif dealer == 3:
        return 3 
    elif dealer == 4:
        return 4 
def get_winner(player1, dealer):
    if player1 == dealer:
        return("player1") 
    elif player1 != dealer:
        return ("dealer") 
def fordham_game():
    bank = 100 
    while bank != 0:
        bet = get_bet(bank) 
        player1 = get_guess()
        dealer = get_comp_move() 
        winner = get_winner(player1, dealer)
        if winner == "player1":
            print("Player wins")
            bank = bank + bet * 2 
            print(bank) 
        elif winner == "dealer":
            print("Dealer wins")
            bank = bank - bet
            print(bank)
fordham_game()