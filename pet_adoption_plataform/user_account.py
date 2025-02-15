import os

user_name = "User"
user_age = 00
user_adress = "Unknown"
user_email = "Unknown"


class User:
    def __init__(self, name, age, address, email):
        self.name = name
        self.age = int(age)
        self.address = address
        self.email = email
    
    def show_info(self):
        print(f"Name: {self.name}\nAge: {self.age}\nAdress: {self.address}\nEmail: {self.email}")

user = User(user_name, user_age, user_adress, user_email)

def user_profile():
    while True:
        global user

        os.system("cls")

        if user.age != 0:
            user.show_info()

        else:
            print("You need creat a account!")

        escolha = input("--Creat account (1)\n--Change account (2)\n--Return (3)\n")

        if escolha == "1":
            user.name = input("Type your name: ").capitalize()
            user.age = int(input("Type your age: "))
            while user.age == 0 or user.age > 99:
                user.age = int(input("Type a valid age: "))
            user.address = input("Type your adress: ")
            user.email = input("Type your email: ")

        elif escolha == "2":
            if user.age != 0:
                changers()
            else:
                while True:
                    print("You need creat a account!")
                    input("Type enter to continue")
                    break
        
        elif escolha == "3":
            break
        print("\n")

def changers():

    global user

    print("Change your name? y/n: ")
    control = input()
    if control == "y":
        user.name = input("Type your name: ").capitalize()
    print("Change your age? y/n: ")
    control = input()
    if control == "y":
        user.age = int(input("Type your age: "))
        while user.age == 0 or user_age > 99:
                user.age = int(input("Type a valid age: "))
    print("Change adress? y/n: ")
    control = input()
    if control == "y":
        user.address = input("Type your adress:")
    print("Change email? y/n: ")
    control = input()
    if control == "y":
        user.email = input("Type your email: ")