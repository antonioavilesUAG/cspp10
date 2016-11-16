word = input("Any word: ")
num = int(input("Any number: "))

if word[-2:] == "fe" and num > 1 or num == 0: 
    print ("{}{}".format(num , word[:-2]+"ves"))
elif word[-2:] == "ay"or word[-2:] == "oy" or word[-2:] == "ey" or word[-2:] == "uy" and num > 1 or num == 0:    
    print ("{}{}".format(num, word +"s"))
elif word[-1:] == "y" and num > 1 or num == 0: 
    print ("{}{}".format(num ,word[:-1]+"ies"))
elif word[-2:]== "sh" or word[-2:] == "ch" and num >= 1 or num == 0:
    print ("{}{}".format(num , word +"es"))
elif word[-2:] == "us" and num > 1 or num == 0:
    print ("{}{}".format(num , word[:-2]+ "i"))
elif num == 1:
    print("{}{}".format(num, word))
else:
     print ("{}{}".format(num, word +"s"))