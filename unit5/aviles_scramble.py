import random

def scramble_word():
#Allow user to put in there word that they want to scramble#
    player1 = input("Write in a word: ")
#Get the first and last letter by thereselves by using string indexs do that#
    word = player1[0]
    word2 = player1[-1]
    firstlastletter = player1[1:-1]
    print(firstlastletter)
#Put the rest of the word into a list.# 
    a = list(firstlastletter)
    print(a)
#Scumble the list# 
    random.shuffle(a)
    print(a)
#combine the first and last letter with the words you scrumble# 
    word3 = word + a + word2
scramble_word()