num_list = []

number_choice = 1
while number_choice != 0:
    number_choice = int(input("Any number other than 0: "))
    
    if number_choice >= 1:
         num_list.insert(0,number_choice)
         print(num_list)
    
    elif number_choice <= -1:
        if num_list.remove(number_choice * -1) in num_list:
            print(num_list)
            
    else:
        print("You exited from the code.")
        break