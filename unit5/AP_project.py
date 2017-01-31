username = input("Set a username: ")
password = (int(input("Set a password that is numbers only: ")))

print("you must verify your self")

username2 = input("Put in your username: ")
password2 = (int(input("Put in your password: "))) 
if username == username2 and password == password2:
    print("You may enter your email")
else:
    print("This email is not yours")
       