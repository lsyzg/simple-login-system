userp = {}
counter = 3
num_people = int(input("How many people do you want to enter into the database?: "))
for i in range(num_people):
    user = input("Enter new username: ")
    password = input("Enter your new password:")
    userp[user] = password
print("User update complete!")

print("Welcome to the company login page!")
for i in range(3):
    nuser = input("Enter username: ")
    counter = counter - 1
    if counter == 0:
        print("Access denied")
        break
    if nuser in userp:
        npassword = input("Enter your password: ")
        if npassword == userp.get(nuser):
            print(f"Access granted, welcome {nuser}!")
        else:
            print(f"Wrong password, {counter} attempts left")
    else:
        print("Username not in database, please try again")