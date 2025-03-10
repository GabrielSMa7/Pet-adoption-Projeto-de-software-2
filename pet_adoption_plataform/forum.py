import os
from pet_adoption_plataform import user_account
from pet_adoption_plataform import events
from pet_adoption_plataform import community
from pet_adoption_plataform import stories
from pet_adoption_plataform import education

def menu():
    while True:
        os.system("cls")
        if user_account.user != None:
            if user_account.user.getlogin() == True:
                print(f"Welcome {user_account.user.name} to our forum")
            else:
                print(f"Welcome quest to our forum")
        else:
            print(f"Welcome quest to our forum")
        print("--Events (1)\n--Community (2)\n--Help and tips(3)\n--Successful stories(4)\n--Return (5)")
        choice = input()
        if choice == "1":
            os.system("cls")
            events.show_events()
        if choice == "2":
            os.system("cls")
            community.showcommunity()
        if choice == "3":
            education.showhelp()
        if choice == "4":
            stories.showstorie()
        if choice == "5":
            os.system("cls")

            break