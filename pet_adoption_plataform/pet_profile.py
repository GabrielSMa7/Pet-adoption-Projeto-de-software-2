from pet_adoption_plataform import search
from pet_adoption_plataform import adoption
from pet_adoption_plataform import shelter_profile
from pet_adoption_plataform import clases
import os 

class Pet:
    def __init__(self, name, age, gender, color, size, type, shelter):
        self.name = name
        self.age = age
        self.gender = gender
        self.color = color
        self.size = size        
        self.type = type
        self.shelter = shelter

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"color: {self.color}")
        print(f"type: {self.type}")
        print(f"Size: {self.size}")
        print(f"shelter: {self.shelter.name}\n")

pet1 = Pet("Bethoven",7, "male", "brown and white", "big", "dog", shelter_profile.shelter1)
pet2 = Pet("Garfiel", 4, "male", "orange", "medium", "cat", shelter_profile.shelter1)
pet3 = Pet("Snoop", 2, "male", "black and white", "small", "dog", shelter_profile.shelter1)
pet4 = Pet("Lady", 2, "female", "brown", "small", "dog", shelter_profile.shelter2)
pet5 = Pet("Scooby", 10, "male", "brown", "big", "dog", shelter_profile.shelter2)
pet6 = Pet("Marrie", 1, "female", "white", "small", "cat", shelter_profile.shelter2)

pets = [pet1, pet2, pet3, pet4, pet5, pet6]        

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

        spc = spc.strip().lower()
        fltrs = fltrs.strip().lower()

        filter_pets = search.filtr(filter_pets, fltrs, spc)
        print("Apply another filter? y/n")
        choice = input()

    while True:
        
        os.system("cls")

        for pet in filter_pets:
            print(f"Name: {pet.name}")

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