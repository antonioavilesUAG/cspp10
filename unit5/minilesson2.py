num_list = []
number_choice = 1
while number_choice != "exited":
    number_choice = input("Enter in your command: ")
    if number_choice == "length":
        print(len(num_list))
    elif number_choice == "clear":
        num_list = []
    elif number_choice == "sum":
        sum(num_list) 
    elif number_choice == "print":
        print(num_list)
    else:
        int(number_choice)
        num_list.insert(0,number_choice)
        
        