from pet_adoption_plataform import pet_profile 
from pet_adoption_plataform import user_account
from pet_adoption_plataform import shelter_profile
import os



while True:
    os.system("cls")

    print(f"Welcome to our Pet Adoption Platform!!!")

    print("--View and adopt our pets type (1)\n--View your profile type (2)\n--See shelters and rescue information type (3)\n--Exit (4)")
    choice = input()
    if choice == "1":
        pet_profile.showpets()
    if choice == "2":
        user_account.user_profile()
    if choice == "3":
        shelter_profile.showshelter()
    if choice == "4":
        os.system("cls")
        break