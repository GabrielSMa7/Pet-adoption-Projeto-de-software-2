import os
from pet_adoption_plataform import clases

user = None

def user_profile():
    while True:
        global user

        os.system("cls")

        if user == None:
            print("You need creat a account!")
        else:
            user.show_info()

        escolha = input("--Creat account (1)\n--Login (2)\n--Change account (3)\n--Return (4)\n")

        if escolha == "1":
            user = clases.User.creat()
        if escolha == "2":
            username = input("Your username:").capitalize()
            password = input("Your password: ")
            user.login(username, password)
        elif escolha == "3":
            if user.age != 0:
                user.changers()
            else:
                while True:
                    print("You need creat a account!")
                    input("Type enter to continue")
                    break 
        elif escolha == "4":
            break
        print("\n")
    