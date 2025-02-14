from pet_adoption_plataform import search
from pet_adoption_plataform import adoption
import os 

pets = {
        'Bethoven': { 
            'age': 7, 
            'gender': 'male',
            'color': 'brown and white',
            'size' : 'big',
            'type' : 'dog',
            'shelter' : 'Adocão'
            },
        'Garfiel': {
            'age': 4, 
            'gender': 'male',
            'color': 'orange',
            'size' : 'medium',
            'type' : 'cat',
            'shelter' : 'Adocão'
        },
        'Snoop': { 
            'age': 2, 
            'gender': 'male',
            'color': 'black and white',
            'size' : 'small',
            'type' : 'dog',
            'shelter' : 'Adocão'
            },
        'Lady': { 
            'age': 2, 
            'gender': 'female',
            'color': 'brown',
            'size' : 'small',
            'type' : 'dog',
            'shelter' : 'Amigos de pata'
            },
        'Scooby': { 
            'age': 10, 
            'gender': 'male',
            'color': 'brown',
            'size' : 'big',
            'type' : 'dog',
            'shelter' : 'Amigos de pata'
            },
        'Marrie': {
            'age': 1, 
            'gender': 'female',
            'color': 'white',
            'size' : 'small',
            'type' : 'cat',
            'shelter' : 'Amigos de pata'
        },
    }  

def showpets():
    global pets
    filter_pets = pets
    os.system("cls")
    
    print(f"{len(filter_pets)} pets available!")
    print("Apply filters? y/n")
    choice = input()

    while choice == "y":
    
        os.system("cls")

        while True:  
        
            print("What kind of filter?\n--Type\n--Size\n--Gender")
            fltrs = input() 

            if fltrs.lower() == "type":
                os.system("cls")
                print("What kind of type?\n--Cat\n--Dog")
                spc = input()
                break
            if fltrs.lower() == "size":
                os.system("cls")
                print("What kind of Size?\n--Small\n--Medium\n--Big")
                spc = input()
                break
            if fltrs.lower() == "gender":
                os.system("cls")
                print("What kind of gender?\n--Female\n--Male")
                spc = input()
                break
            else:
                os.system("cls")
                print("Filter don't found, try again!")

        spc = spc.lower()
        fltrs = fltrs.lower()

        filter_pets = search.filtr(filter_pets, fltrs, spc)
        print("Apply another filter? y/n")
        choice = input()

    while True:
        
        os.system("cls")

        for pet in filter_pets.keys():
            print(f"Name: {pet}")

        print("See more informations? y/n")
        info = input().lower()

        if info == "y":
            print("Enter the name of the pet you want to see: ")
            pet_choiced = input().lower().capitalize()
            paw_info = filter_pets.get(pet_choiced)
            
            if not paw_info:
                continue
            
            os.system("cls")

            print(f"Pet Name: {pet_choiced}")
            age = paw_info['age']
            color = paw_info['color']
            gender = paw_info['gender']
            size = paw_info['size']
            tpe = paw_info['type']
            shelter = paw_info['shelter']

            print(f"Age: {age}")
            print(f"Color: {color}")
            print(f"Gender: {gender}")
            print(f"Size: {size}")
            print(f"Type: {tpe}")

            print("--Want to adopt this pet? (1)\n--Return (2)\n--Exit (3)")
            
            choice = input()
            
            if choice == "2":
                continue

            elif choice == "1":
                adoption.adoption(pet_choiced, shelter)
                break
            elif choice == "3":
                break
        else:
            break