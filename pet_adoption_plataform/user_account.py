import os
from pet_adoption_plataform import clases

users = [""]

def user_profile():
    while True:
        global users

        os.system("cls")

        if users == ['']:
            print("You need creat a account!")
        else:
            user.show_info()

        escolha = input("--Creat account (1)\n--Change account (2)\n--Return (3)\n")

        if escolha == "1":
            user.creat()
            users.append(user)
        elif escolha == "2":
            if user.age != 0:
                user = clases.User.changers()
            else:
                while True:
                    print("You need creat a account!")
                    input("Type enter to continue")
                    break 
        elif escolha == "3":
            break
        print("\n")
    