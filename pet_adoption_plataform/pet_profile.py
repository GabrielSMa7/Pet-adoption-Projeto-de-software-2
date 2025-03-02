from pet_adoption_plataform import adoption
from pet_adoption_plataform import shelter_profile
from pet_adoption_plataform import clases
import os 

pet1 = clases.Pet("Bethoven",7, "male", "brown and white", "big", "dog", shelter_profile.shelter1)
pet2 = clases.Pet("Garfiel", 4, "male", "orange", "medium", "cat", shelter_profile.shelter1)
pet3 = clases.Pet("Snoop", 2, "male", "black and white", "small", "dog", shelter_profile.shelter1)
pet4 = clases.Pet("Lady", 2, "female", "brown", "small", "dog", shelter_profile.shelter2)
pet5 = clases.Pet("Scooby", 10, "male", "brown", "big", "dog", shelter_profile.shelter2)
pet6 = clases.Pet("Marrie", 1, "female", "white", "small", "cat", shelter_profile.shelter2)
pet7 = clases.Pet("Clebinho", 7462, "male", "Red", "big", "dragon", shelter_profile.shelter3)
pet8 = clases.Pet("Jonas", 17, "male", "brown", "big", "pig", shelter_profile.shelter2)
pet9 = clases.Pet("Pong", 11, "male", "orange", "small", "orangotango", shelter_profile.shelter4)
pet10 = clases.Pet("Perrita", 8, "female", "pink", "small", "spider", shelter_profile.shelter4)
pet11 = clases.Pet("Marta", 674, "female", "brown", "big", "terrasque", shelter_profile.shelter3)
pet12 = clases.Pet("Jorel", 17, "male", "brown", "big", "anteater", shelter_profile.shelter4)
pet13 = clases.Pet("Tati", 9, "female", "green", "big", "armadillo", shelter_profile.shelter4)

pets = [pet1, pet2, pet3, pet4, pet5, pet6, pet7, pet8, pet9, pet10, pet11, pet12, pet13]        

def showpets():
    global pets
    os.system("cls")
    while True:
        
        os.system("cls")

        filter_pets = clases.Pet.search(pets)

        os.system("cls")

        clases.Pet.showlist(filter_pets)

        print("See more informations? y/n")
        info = input().lower()

        if info == "y":
            print("Enter the name of the pet you want to see: ")
            pet_choiced = input().lower().capitalize()
            paw_info = clases.Pet.search_name_in_list(pet_choiced, pets)
            
            if paw_info == None:
                input("Pet dont found")
                continue
            
            os.system("cls")

            paw_info.show_info()

            print("--Want to adopt this pet? (1)\n--Return (2)\n--Exit (3)")
            
            choice = input()
            
            if choice == "2":
                continue

            elif choice == "1":
                adoption.adoption(paw_info.name, paw_info.shelter)
                break
            elif choice == "3":
                break
        else:
            break