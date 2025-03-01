import os

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
    def showlist(lista):
        for i in lista:
            print(f"{i.name}")
    
    @staticmethod
    def search():
        pass

    @staticmethod
    def filters(list, fltrs, sps):
        #cria um dicionario novo para armazenar os itens selecionados
        newlist = [i for i in list if getattr(i, fltrs, "").lower() == sps.lower()]

        #printa quantos itens tem no dicionario
        print(f"{len(newlist)} pets available!")
        
        #retorna o novo dicionario
        return newlist

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
    def __init__(self, name, password, age, address, email):
        self.name = name
        self.password = password
        self.age = int(age)
        self.address = address
        self.email = email
        self.logged = False
    
    def login(self, name, password):
        if (name != self.name) | (password != self.password):
            self.logged == False
            print("Wrong username or password")
        else:
            self.logged = True

    def show_info(self):
        if self.logged == True:
            print(f"Name: {self.name}\nAge: {self.age}\nAdress: {self.address}\nEmail: {self.email}")
    
    @classmethod
    def creat(cls):
        name = input("Type your name: ").capitalize()
        password = input("Type your password: ")
        age = int(input("Type your age: "))
        while age == 0 or age > 99:
            age = int(input("Type a valid age: "))
        address = input("Type your adress: ")
        email = input("Type your email: ")

        return cls(name, password, age, address, email)

    def changers(self):
        if input("Change your name? y/n: ").lower() == "y":
            self.name = input("Type your name: ").capitalize()
        if input("Change your password? y/n").lower() == "y":
            self.password = input("Type your password")
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

    @staticmethod
    def search(list):
        print(f"{len(list)} pets available!")
        print("Apply filters? y/n")
        choice = input()

        while choice == "y":
        
            os.system("cls")

            while True:  
            
                print("What kind of filter?\n--Type\n--Size\n--Gender")
                fltrs = input()

                if fltrs.lower() == "type":
                    os.system("cls")
                    print("What kind of type?")
                    tpe = []
                    for i in list:
                        tpe.append(getattr(i, "type"))
                        
                    tpe = set(tpe)
                    for j in tpe:
                        print(f"--{j}")

                    spc = input()
                    break
                if fltrs.lower() == "size":
                    os.system("cls")
                    print("What kind of Size?")
                    size = []
                    for i in list:
                        size.append(getattr(i, "size"))
                    size = set(size)
                    for j in size:
                        print(f"--{j}")
                    spc = input()
                    break
                if fltrs.lower() == "gender":
                    os.system("cls")
                    print("What kind of gender?\n--Female\n--Male")
                    gender = []
                    for i in list:
                        gender.append(getattr(i, "gender"))
                        
                    gender = set(gender)
                    for j in gender:
                        print(f"--{j}")
                    spc = input()
                    break
                else:
                    os.system("cls")
                    print("Filter don't found, try again!")

            spc = spc.strip().lower()
            fltrs = fltrs.strip().lower()

            list = Pet.filters(list, fltrs, spc)
            print("Apply another filter? y/n")
            choice = input()
            return list
class Event(Base):
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