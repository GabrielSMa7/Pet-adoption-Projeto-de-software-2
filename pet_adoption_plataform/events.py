import os
from pet_adoption_plataform import search

events = {
    'Feira de adoção' : {
        'local' : 'Parque da cidade',
        'date' : '12/02',
        'open' : '13:00',
        'close' : '17:00',
        'type' : 'adoption'
    },
    'Feira de adoção 2' : {
        'local' : 'Parque da cidade',
        'date' : '13/02',
        'open' : '10:00',
        'close' : '20:00',
        'type' : 'adoption'
    },
    'Feira de vacinação' : {
        'local' : 'Parque da cidade',
        'date' : '15/02',
        'open' : '7:00',
        'close' : '17:00',
        'type' : 'vaccination'
    },
    'Feira de vacinação 2' : {
        'local' : 'Parque da cidade',
        'date' : '12/02',
        'open' : '8:00',
        'close' : '10:00',
        'type' : 'vaccination'
    },
}

def show_events():
    global events
    os.system("cls")
    
    print(f"{len(events)} events available!")
    print("Apply filters? y/n")
    choice = input()

    while choice == "y":
    
        os.system("cls")

        while True:  
        
            print("What kind of filter?\n--Type")
            fltrs = input().lower()

            if fltrs.lower() == "type":
                os.system("cls")
                print("What kind of type?\n--Adoption\n--Vaccination")
                spc = input().lower()
                break
            else:
                os.system("cls")
                print("Filter don't found, try again!")

        events = search.filtr(events, fltrs, spc)
        print("Apply another filter? y/n")
        choice = input()

    while True:
        
        os.system("cls")

        for event in events.keys():
            print(f"Name: {event}")

        print("See more informations? y/n")
        info = input().lower()

        if info == "y":
            print("Enter the name of the pet you want to see: ")
            event_choiced = input()
            event_choiced = event_choiced.lower().capitalize()
            event_info = events.get(event_choiced)
            
            if not event_info:
                continue

            os.system("cls")

            print(f"\nPet Name: {event_choiced}")

            print(f"Local: {event_info['local']}")
            print(f"Date: {event_info['date']}")
            print(f"Open: {event_info['open']}")
            print(f"Close: {event_info['close']}")
            print(f"Type: {event_info['type']}")

            print("--Return (1)\n--Exit (2)")
            
            choice = input()
            
            if choice == "1":
                continue

            elif choice == "2":
                break
        
        else:
            break