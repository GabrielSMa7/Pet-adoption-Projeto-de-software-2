class Base:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print(f"Name:{self.name}")
    
    def search_name_in_list(nome, lista):
        for i in lista:
            if i.name.lower() == nome.lower():
                return i
        return None

    def showlist(list):
        for i in list:
            print(f"{i.name}")

class Shelter(Base):
    def __init__(self, name, local, email, phone, pets, us):
     super().__init__(name)
     self.local = local
     self.email = email
     self.phone = phone
     self.pets = int(pets)
     self.us = us   

    def show_info(self):
        print(f"Name:{self.name}")
        print(f"Local:{self.local}")
        print(f"Email:{self.email}")
        print(f"Phone:{self.phone}")
        print(f"Pets:{self.pets}")
        print(f"Us:{self.us}\n")

class User(Base):
    def __init__(self, name, age, address, email):
        self.name = name
        self.age = int(age)
        self.address = address
        self.email = email
    
    def show_info(self):
        print(f"Name: {self.name}\nAge: {self.age}\nAdress: {self.address}\nEmail: {self.email}")
    
    def creat(self):
        self.name = input("Type your name: ").capitalize()
        self.age = int(input("Type your age: "))
        while self.age == 0 or self.age > 99:
            self.age = int(input("Type a valid age: "))
        self.address = input("Type your adress: ")
        self.email = input("Type your email: ")

    def changers(self):
        print("Change your name? y/n: ")
        control = input()
        if control == "y":
            self.name = input("Type your name: ").capitalize()
        print("Change your age? y/n: ")
        control = input()
        if control == "y":
            self.age = int(input("Type your age: "))
            while self.age == 0 or self.age > 99:
                    self.age = int(input("Type a valid age: "))
        print("Change adress? y/n: ")
        control = input()
        if control == "y":
            self.address = input("Type your adress:")
        print("Change email? y/n: ")
        control = input()
        if control == "y":
            self.email = input("Type your email: ")

class Pet(Base):
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