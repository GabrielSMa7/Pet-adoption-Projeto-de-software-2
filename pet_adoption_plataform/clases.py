import os

class Base:
    def __init__(self, name):
        self.name = name
    
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
        newlist = []

        for i in list:
            if str(getattr(i, fltrs)).lower() == sps.lower():
                newlist.append(i)

        #printa quantos itens tem no dicionario
        print(f"{len(newlist)} pets available!")
        
        #retorna o novo dicionario
        return newlist
class Shelter(Base):
    def __init__(self, name, local, email, phone, pets, us):
     self.name = name
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
        super().__init__(name)
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
            print(f"Name:{self.name}")
            print(f"Age: {self.age}")
            print(f"Email: {self.email}")
            print(f"Address: {self.address}")
    
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
    def __init__(self, name, age, gender, color, size, type, shelter, adopted: bool):
        super().__init__(name)
        self.age = age
        self.gender = gender
        self.color = color
        self.size = size        
        self.type = type
        self.shelter = shelter
        shelter.pets += 1
        self.adopted = adopted

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
        print("Apply filters? y/n")
        choice = input().lower()
        while choice != "n" and choice != "y":
            print("Wrong comand try again:")
            choice = input().lower()
        while choice == "y":
            os.system("cls")

            while True:  
            
                print("What kind of filter?\n--Type\n--Color\n--Size\n--Gender")
                fltrs = input()

                if fltrs.lower() == "color":
                    os.system("cls")
                    print("What kind of color?")
                    color = []
                    for i in list:
                        color.append(getattr(i, "color").capitalize())
                        
                    color = set(color)
                    for j in color:
                        print(f"--{j}")

                    
                    spc = input().capitalize()
                    while spc not in color:
                        spc = input("Filter don't found, try again!")
                    break

                if fltrs.lower() == "type":
                    os.system("cls")
                    print("What kind of type?")
                    tpe = []
                    for i in list:
                        tpe.append(getattr(i, "type").capitalize())
                        
                    tpe = set(tpe)
                    for j in tpe:
                        print(f"--{j}")

                    
                    spc = input().capitalize()
                    while spc not in tpe:
                        spc = input("Filter don't found, try again!")
                    break
                if fltrs.lower() == "size":
                    os.system("cls")
                    print("What kind of Size?")
                    size = []
                    for i in list:
                        size.append(getattr(i, "size").capitalize())
                    size = set(size)
                    for j in size:
                        print(f"--{j}")
                    
                    spc = input().capitalize()
                    while spc not in size:
                        spc = input("Filter don't found, try again!")
                    break
                if fltrs.lower() == "gender":
                    os.system("cls")
                    print("What kind of gender?")
                    gender = []
                    for i in list:
                        gender.append(getattr(i, "gender").capitalize())
                        
                    gender = set(gender)
                    for j in gender:
                        print(f"--{j}")
                    
                    spc = input().capitalize()
                    while spc not in gender:
                        spc = input("Filter don't found, try again!")
                    break
                else:
                    os.system("cls")
                    print("Filter don't found, try again!")

                spc = spc.strip().lower()
                fltrs = fltrs.strip().lower()

            list = Pet.filters(list, fltrs, spc)
            if len(list) > 1:
                print("Apply another filter? y/n")
                choice = input().lower()
                while choice != "n" and choice != "y":
                    print("Wrong comand try again:")
                    choice = input().lower()
            elif len(list) == 0:
                print("No results")
                break
            elif len(list) == 1:
                choice == "n"
                break
        return list
    
    def stories(self, storie):
        self.storie = storie
class Event(Base):
    def __init__(self, name, local, date, open, close, type):
        super().__init__(name)
        self.local = local
        self.date = date
        self.open = open
        self.close = close
        self.type = type

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Local: {self.local}")
        print(f"Date: {self.date}")
        print(f"Open: {self.open}")
        print(f"Close: {self.close}")
        print(f"Type: {self.type}")

    @staticmethod
    def search(list):
        print(f"{len(list)} events available!")
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

            list = Base.filters(list, fltrs, spc)
            list = Pet.filters(list, fltrs, spc)
            if len(list) > 1:
                print("Apply another filter? y/n")
                choice = input().lower()
                while choice != "n" and choice != "y":
                    print("Wrong comand try again:")
                    choice = input().lower()
            elif len(list) == 0:
                print("No results")
        return list
class Message:
    def __init__(self, owner, message):
        self.owner = owner
        self.messages = []
        self.messages.append(message)

    
    def show_comment(self):
        for i in self.messages:
            print(f"Owner: {self.owner}")
            print(f"Mensage: {i}")

    def add(self, comment):
        self.messages.append(comment)
class Topic(Base, Message):
    def __init__(self, name, owner, title, message):
        self.name = name
        self.owner = owner
        self.title = title
        self.message = message
        self.comments = {}

    def create(owner):
        name = input("Topic name:")
        title = input("Post's title:")
        message = input("Decrible your post:")
        name = Topic(name, owner, title, message)
        return name

    def coment(self, owner, coment):
        if owner not in self.comments:
            self.comments[owner] = Message(owner, coment)
        else:
            self.comments[owner].add(coment)
            

    def show_info(self):
        print(f"User: {self.owner}")
        print(f"Title: {self.title}")
        print(f"Message: {self.message}")
        print(f"Coments: {len(self.comments)}")

    def show_comments(self):
        for user in self.comments:
            self.comments[user].show_comment()