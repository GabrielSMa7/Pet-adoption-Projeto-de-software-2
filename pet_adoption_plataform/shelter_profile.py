import os
from pet_adoption_plataform import pet_profile
from pet_adoption_plataform import user_account
from pet_adoption_plataform import search
from pet_adoption_plataform import clases

shelter1 = clases.Shelter(
        'Adocão',
        'Maceio',
        'endereço',
        'adoteme@org.com',
        '4949939052',
        3,
        'O Lar dos Peludos é um abrigo dedicado ao resgate e acolhimento de animais em situação de abandono e maus-tratos. Nosso objetivo é proporcionar um ambiente seguro e acolhedor para cães e gatos que precisam de uma segunda chance.'
    )
shelter2 = clases.Shelter(
        'Amigo de pata',
        'Penedo',
        'Endereço',
        'adocao@yahoo.com',
        '63348842',
        3,
        'O Abrigo Esperança Animal é um espaço dedicado ao resgate, cuidado e reabilitação de animais abandonados, maltratados ou em situação de risco. Nossa missão é oferecer um lar temporário seguro, repleto de amor e atenção, enquanto trabalhamos para encontrar famílias responsáveis e amorosas para cada um de nossos resgatados.'
    )
shelters = [
    shelter1,
    shelter2
]

def searchshelter(nome, lista):
    for i in lista:
        if i.name.lower() == nome.lower():
            return i
    return None

def showshelter():
    while True:
        
        os.system("cls")

        for i in shelters:
            print(f"{i.name}")

        print("See more about the shelters? y/n")
        choice = input()

        if choice == "y":
            print("Enter the name of the shelter you want to see: ")
            shelter_choiced = input()

            shelter_info = searchshelter(shelter_choiced, shelters) 

            if shelter_info is None:
                print("Shelter dont found")
                return
            
            if not shelter_info:
                continue

            os.system("cls")
            
            
            shelter_info.show_info()

            print("--See our availabels pets? (1)\n--Send a donation for this shelter? (2)\n--Return (3)\n--Exit (4)")
            
            choice = input()

            os.system("cls")

            if choice == "2":
                if user_account.user.age == "Unknown":
                    print("You need have a account to do a donation")   
                elif user_account.user.age > 18:
                    print("Send your tip")
                    donation = float(input())
                    print(f"Thanks {user_account.user.name}Our pets from {shelter_info.name} are pleased for your contribution of {donation:.2f}$")
                else:
                    print("You need be a adult to do a donation")
                input("\nPress any key to return")
                continue

            elif choice == "1":
                pets_availables = search.filtr(pet_profile.pets, "shelter", shelter_info.name)

                for pet in pets_availables.keys():
                    print(f"Name: {pet}")

                input("\nPress any key to return")
                continue
            elif choice == "3":
                continue
            elif choice == "4":
                break
        elif choice == "n":
            break