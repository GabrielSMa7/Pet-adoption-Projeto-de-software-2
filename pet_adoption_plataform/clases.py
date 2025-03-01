class Base:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print(f"Name:{self.name}")
    
    @staticmethod
    def search_name_in_list(nome, lista):
        for i in lista:
            if i.name.lower() == nome.lower():
                return i
        return None

    @staticmethod
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
    
    @classmethod
    def creat(cls):
        name = input("Type your name: ").capitalize()
        age = int(input("Type your age: "))
        while age == 0 or age > 99:
            age = int(input("Type a valid age: "))
        address = input("Type your adress: ")
        email = input("Type your email: ")

        return cls(name, age, address, email)

    def changers(self):
        if input("Change your name? y/n: ").lower() == "y":
            self.name = input("Type your name: ").capitalize()
        if input("Change your age? y/n: ").lower() == "y":
            self.age = int(input("Type your age: "))
            while self.age == 0 or self.age > 99:
                    self.age = int(input("Type a valid age: "))
        if input("Change adress? y/n: ").lower() == "y":
            self.address = input("Type your adress:")
        if input("Change email? y/n: ").lower() == "y":
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