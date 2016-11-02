import random 
num = (random.randint(1,100)) 
guess = int(input("number of guess: "))
while num != guess:
    if guess < num:
        print (int(input("too low try again: ")))
        guess = guess + 1
    elif guess > num:
        print (int(input("too high try again: ")))
        guess = guess + 1 
    elif num == guess:
        break
print("you tried {}, number is {}".format(guess,num))