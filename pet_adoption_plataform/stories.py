import os

stories = {
    'Cristal' : {
        'shelter' : 'Adocão',
        'story' : 'A Cristal foi adotada após o primeiro dia de anúncio. Estamos muito felizes em fazer parte dessa história 🤍'
    },
    'Marley' : {
        'shelter' : 'Amigos de pata',
        'story' : 'A quinta casa depois do abrigo um guerreirinho'
    },
    'Luna' : {
        'shelter' : 'Adocão',
        'story' : 'Um rapaz de bom coração levou ela'
    }
}

def showstorie():
    global stories
    while True:
        os.system("cls")
        for pet in stories.keys():
            print(f"Pet: {pet}")

        choice_pet = input("Choice one pet to see they story: ").lower().capitalize()

        pet_choiced = stories.get(choice_pet)

        if not pet_choiced:
            continue

        print(f"Name: {choice_pet}\nAdopt from: {pet_choiced["shelter"]}\nStory: {pet_choiced["story"]}")

        choice = input("--Return (1)\n--Exit (2)\n")

        if choice == "1":
            continue
        if choice == "2":
            break