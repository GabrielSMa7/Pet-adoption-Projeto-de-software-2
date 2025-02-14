import os
from pet_adoption_plataform import pet_profile
from pet_adoption_plataform import user_account
from pet_adoption_plataform import search
from pet_adoption_plataform import stories

shelters = {
    'Adocão': { 
        'local':'Maceio',
        'email': 'adoteme@org.com',
        'phone': '4949939052',
        'pets': '3',
        'us': 'O Lar dos Peludos é um abrigo dedicado ao resgate e acolhimento de animais em situação de abandono e maus-tratos. Nosso objetivo é proporcionar um ambiente seguro e acolhedor para cães e gatos que precisam de uma segunda chance.'
        },
    'Amigos de pata': {
        'local':'Penedo',
        'email': 'adocao@yahoo.com',
        'phone': '63348842',
        'pets': '3',
        'us': 'O Abrigo Esperança Animal é um espaço dedicado ao resgate, cuidado e reabilitação de animais abandonados, maltratados ou em situação de risco. Nossa missão é oferecer um lar temporário seguro, repleto de amor e atenção, enquanto trabalhamos para encontrar famílias responsáveis e amorosas para cada um de nossos resgatados.',
    },
}

def showshelter():
    while True:
        
        os.system("cls")

        for shelter in shelters.keys():
            print(f"Name: {shelter}")

        print("See more about the shelters? y/n")
        choice = input()

        if choice == "y":
            print("Enter the name of the shelter you want to see: ")
            shelter_choiced = input()
            shelter_choiced = shelter_choiced.lower().capitalize()
            shelter_info = shelters.get(shelter_choiced)
            
            if not shelter_info:
                continue

            os.system("cls")
            
            
            print(f"Shelter Name: {shelter_choiced}")
            local = shelter_info['local']
            email = shelter_info['email']
            phone = shelter_info['phone']
            pets = shelter_info['pets']
            us = shelter_info['us']

            print(f"Local: {local}")
            print(f"Email: {email}")
            print(f"Phone: {phone}")
            print(f"Pets: {pets}")
            print(f"About us: {us}")
            print(f"Adopted pets: {len(search.filtr(stories.stories, 'shelter', shelter_choiced))}")

            print("--See our availabels pets? (1)\n--Send a donation for this shelter? (2)\n--Return (3)\n--Exit (4)")
            
            choice = input()

            os.system("cls")

            if choice == "2":
                if user_account.user_age == "Unknown":
                    print("You need have a account to do a donation")   
                elif user_account.user_age > 18:
                    print("Send your tip")
                    donation = float(input())
                    print(f"Thanks {user_account.user_name}Our pets from {shelter_choiced} are pleased for your contribution of {donation:.2f}$")
                else:
                    print("You need be a adult to do a donation")
                input("\nPress any key to return")
                continue

            elif choice == "1":
                pets_availables = search.filtr(pet_profile.pets, "shelter", shelter_choiced)

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