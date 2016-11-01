result = input("What math problem you want ")  
a = "+" 
s = "-"
m = "*" 
mo ="%"
num = int(result[0])
num1= int(result[2])
if (result[1]) == a: 
    print ("The result is {}" .format(num + num1)) 
elif result[1]== s:
    print ("The result is {}" .format(num - num1)) 
elif result[1]== m: 
    print ("The result is {}" .format(num * num1)) 
elif result[1]== mo: 
    print ("The result is {}" .format(num % num1))  