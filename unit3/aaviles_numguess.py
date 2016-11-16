import random 
num = (random.randint(1,100)) 
guess = int(input("number of guess: "))
attempt = 0
while num != guess:
    if num > guess:
        guess = (int(input("too low try again: ")))
        attempt = attempt + 1
    elif num < guess:
        guess = (int(input("too high try again: ")))
        attempt = attempt + 1
    elif num == guess:
        break
print("you tried {}, number is {}".format(attempt, num))