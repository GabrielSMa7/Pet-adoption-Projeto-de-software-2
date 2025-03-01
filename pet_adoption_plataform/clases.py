class Base:
    def __init__(self, name, age, email, address):
        self.name = name
        self.age = int(age)
        self.email = email
        self.address = address
class Shelter(Base):
    def __init__(self, name, local, address, email, phone, pets, us):
     self.local = local
     self.phone = phone
     self.pets = int(pets)
     self.us = us   
     super().__init__(name, address, email)
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