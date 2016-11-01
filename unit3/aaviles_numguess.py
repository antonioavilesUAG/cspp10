import random  
num = (random.randint(100)) 
guess = int(input("number of guess"))
for x in range(100):
    while x != num:
        print ("x")
    if x < num:
        print("too low try again")
    elif x > 50:
        print ("too high try again")
    elif x == num:
        print("you got it") 
print("you tried {}")