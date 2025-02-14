from pet_adoption_plataform import user_account
from pet_adoption_plataform import shelter_profile

def adoption(pet, rescue):

    rescue_info = shelter_profile.shelters.get(rescue)

    if user_account.user_age == "Unknown":
        print("You need have a account to adopt a pet")
        input("Press any key to return")
    elif user_account.user_age < 21:
        print("You need be a adult to adopt a pet")
        input("Press any key to return")
    else:
        print(f"Adoption process for {user_account.user_name}")
        print("User info")
        user_account.information()

        print("Are this informations correct? y/n")
        control = input()
        
        if control == "n":
            user_account.changers()

        else:
            print(f"Hi {user_account.user_name}. Tell us a little about yourself, your home and your family's routine")
            input()
            print(f"Thank you for your request to adopt {pet}, us from {rescue} will analisy your request and send a email for {user_account.user_email} to aprove\nContact us\nPhone:{rescue_info['phone']}\nEmail:{rescue_info['email']}")
            input("\nPress any key to return")