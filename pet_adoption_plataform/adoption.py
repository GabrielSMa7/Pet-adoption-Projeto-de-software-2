from pet_adoption_plataform import user_account

def adoption(pet, rescue):

    if user_account.users == ['']:
        print("You need have a account to adopt a pet")
        input("Press any key to return")
    elif user_account.user.age < 21:
        print("You need be a adult to adopt a pet")
        input("Press any key to return")
    else:
        print(f"Adoption process for {user_account.user.name}")
        print("User info")
        user_account.user.show_info()

        print("Are this informations correct? y/n")
        control = input()
        
        if control == "n":
            user_account.changers()

        else:
            print(f"Hi {user_account.user.name}. Tell us a little about yourself, your home and your family's routine")
            input()
            print(f"Thank you for your request to adopt {pet}, us from {rescue.name} will analisy your request and send a email for {user_account.user.email} to aprove\nContact us\nPhone:{rescue.phone}\nEmail:{rescue.email}")
            input("\nPress any key to return")