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
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"address: {self.address}")
        print(f"email: {self.email}")

user = User(user_name, user_age, user_adress, user_email)

def user_profile():
    while True:
        global user_name
        global user_age
        global user_adress
        global user_email
        global user

        os.system("cls")

        print(f"Name: {user.user_name}\nAge: {user.user_age}\nAdress: {user.user_adress}\nEmail: {user.user_email}")

        escolha = input("--Creat account (1)\n--Change account (2)\n--Return (3)\n")

        if escolha == "1":
            user_name = input("Type your name: ")
            user_name = user_name.capitalize()
            user_age = int(input("Type your age: "))
            user_adress = input("Type your adress: ")
            user_email = input("Type your email: ")
            user = User(user_name, user_age, user_adress, user_email)

        elif escolha == "2":
            changers()
        elif escolha == "3":
            break
        print("\n")

def changers():

    global user_name
    global user_age
    global user_adress
    global user_email
    global user

    print("Change your name? y/n: ")
    control = input()
    if control == "y":
        user_name = input("Type your name: ")
        user_name = user_name.capitalize()
    print("Change your age? y/n: ")
    control = input()
    if control == "y":
        user_age = int(input("Digite sua idade: "))
    print("Change adress? y/n: ")
    control = input()
    if control == "y":
        user_adress = input("Type your adress:")
    print("Change email? y/n: ")
    control = input()
    if control == "y":
        user_email = input("Type your email: ")
    user = User(user_name, user_age, user_adress, user_email)