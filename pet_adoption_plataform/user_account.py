import os
from pet_adoption_plataform import clases

user_name = "User"
user_age = 00
user_adress = "Unknown"
user_email = "Unknown"

user = clases.User(user_name, user_age, user_adress, user_email)

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
            clases.User.creat()
        elif escolha == "2":
            if user.age != 0:
                clases.User.changers()
            else:
                while True:
                    print("You need creat a account!")
                    input("Type enter to continue")
                    break 
        elif escolha == "3":
            break
        print("\n")
    