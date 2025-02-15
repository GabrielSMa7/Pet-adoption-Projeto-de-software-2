import os
from pet_adoption_plataform import search

class Event:
    def __init__(self, name, local, date, open, close, type):
        self.name = name
        self.local = local
        self.date = date
        self.open = open
        self.close = close
        self.type = type

    def show_info(self):
        print(f"Event name: {self.name}")
        print(f"Local: {self.local}")
        print(f"Date: {self.date}")
        print(f"Open: {self.open}")
        print(f"Close: {self.close}")
        print(f"Type: {self.type}")

event1 = Event('Feira de adoção', 'Parque da cidade', '12/02', '13:00', '17:00', 'adoption')
event2 = Event('Feira de adoção 2', 'Parque da cidade', '13/02', '10:00', '20:00', 'adoption')
event3 = Event('Feira de vacinação', 'Parque da cidade', '15/02', '7:00', '17:00', 'vaccination')
event4 = Event('Feira de vacinação 2', 'Parque da cidade', '12/02', '8:00', '10:00', 'vaccination')

events = [event1, event2, event3, event4]

def searchevent(nome, lista):
    for i in lista:
        if i.name.lower() == nome.lower():
            return i
    return None

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
            fltrs = input().lower().strip()

            if fltrs.lower() == "type":
                os.system("cls")
                print("What kind of type?\n--Adoption\n--Vaccination")
                spc = input().lower().strip()
                break
            else:
                os.system("cls")
                print("Filter don't found, try again!")

        events = search.filtr(events, fltrs, spc)
        print("Apply another filter? y/n")
        choice = input()

    while True:
        
        os.system("cls")

        for event in events:
            print(f"Name: {event.name}")

        print("See more informations? y/n")
        info = input().lower()

        if info == "y":
            print("Enter the name of the pet you want to see: ")
            event_choiced = input().lower().capitalize()
            event_info = searchevent(event_choiced, events)
            
            if not event_info:
                continue

            os.system("cls")

            event_info.show_info()

            print("--Return (1)\n--Exit (2)")
            
            choice = input()
            
            if choice == "1":
                continue

            elif choice == "2":
                break
        
        else:
            break