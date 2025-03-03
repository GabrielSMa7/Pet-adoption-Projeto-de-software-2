from pet_adoption_plataform import pet_profile 
from pet_adoption_plataform import user_account
from pet_adoption_plataform import shelter_profile
from pet_adoption_plataform import forum
import os
import tkinter as tk

windows = tk.Tk()
windows.title("Pet Adoption")
windows.geometry("1000x500")


if user_account.user != None and user_account.user.logged == True:
    message = f"Welcome {user_account.user.name} to our Pet Adoption Platform!!!"
else:
    message = "Welcome quest to our Pet Adoption Platform!!!"
lable = tk.Label(windows, text=message, font=("Arial", 14), fg="blue")
lable.pack(pady=20)

def open_pet():
    pet_profile.showpets()
    windows.update()
def open_profile():
    user_account.user_profile()
    windows.update()
def open_shelter():
    shelter_profile.showshelter()
    windows.update()
def open_forum():
    forum.menu()
    windows.update()
def exit():
    windows.destroy()

btn1 = tk.Button(windows, text="See our pet avaible", command=open_pet)
btn1.pack(pady=15)
btn1 = tk.Button(windows, text="View your profile type", command=open_profile)
btn1.pack(pady=15)
btn1 = tk.Button(windows, text="See shelters and rescue information", command=open_shelter)
btn1.pack(pady=15)
btn1 = tk.Button(windows, text="Forum", command=open_forum)
btn1.pack(pady=15)
btn1 = tk.Button(windows, text="EXIT", command=exit)
btn1.pack(pady=5)

windows.mainloop()