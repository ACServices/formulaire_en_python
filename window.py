#!/usr/bin/python3.7
# -*-coding:UTF-8 -*-"
import tkinter as tk

#root/main wiget
root = tk.Tk()
from fonctions import *

"""====Centralize the root window====="""
screenX = int(root.winfo_screenwidth())
screenY = int(root.winfo_screenheight())
rootX = 490 
rootY = 180
positionX = (screenX // 2)-(rootX // 2)
positionY = (screenY // 2) - (rootY // 2)
geo = "{}x{}+{}+{}".format(rootX,rootY,positionX,positionY)
root.geometry(geo)
"""======================================"""
"""===========THE MENU==================="""
#menu bar
menuBar = tk.Menu(root)

#menus
fileMenu = tk.Menu(menuBar,tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Quit",command=root.quit)

helpMenu = tk.Menu(menuBar,tearoff=0)
helpMenu.add_command(label="contact")
helpMenu.add_command(label="about")

menuBar.add_cascade(label="File",menu=fileMenu)
menuBar.add_cascade(label="Help",menu=helpMenu)

"""===========FORMS WIDGETS================"""
nameLabel = tk.Label(root,text="Nom: ")
nameLabel.grid(row=0,column=0)
nameField = tk.Entry(root,textvariable=nomVar)
nameField.grid(row=0,column=1,padx=5)

prenomLabel = tk.Label(root,text="Prenom: ")
prenomLabel.grid(row=1,column=0)
prenomField = tk.Entry(root,textvariable=prenomVar)
prenomField.grid(row=1,column=1,padx=5)

emailLabel = tk.Label(root,text="Email: ")
emailLabel.grid(row=0,column=2)
emailField = tk.Entry(root,textvariable=emailVar)
emailField.grid(row=0,column=3,padx=5)

ageLabel = tk.Label(root,text="Age: ")
ageLabel.grid(row=2,column=0)
ageField = tk.Spinbox(root,from_=18,to=85,textvariable=ageVar,width=18)
ageField.grid(row=2,column=1,padx=5)

facultyLabel = tk.Label(root,text="Faculty: ")
facultyLabel.grid(row=1,column=2)
facultyField = tk.Listbox(root,height=2)
facultyField.insert(0,"Informatique")
facultyField.insert(1,"Medecine")
facultyField.insert(2,"Droit")
facultyField.grid(row=1,column=3,padx=5)

paysLabel = tk.Label(root,text="Pays: ")
paysLabel.grid(row=2,column=2,padx=5)
paysField = tk.Listbox(root,height=2)
paysField.insert(0,"Burkina")
paysField.insert(1,"Mali")
paysField.insert(2,"Niger")
paysField.grid(row=2,column=3)

sexeLabel = tk.Label(root,text="Sexe: ")
sexeLabel.grid(row=3,column=0)
homme = tk.Radiobutton(root,text="homme",variable=sexeVar,value="homme")
femme = tk.Radiobutton(root,text="femme",variable=sexeVar,value="femme")
homme.grid(row=3,column=1,sticky="w")
femme.grid(row=3,column=1,sticky="e")

btn_envoyer = tk.Button(root,text="ENVOYER",command=afficher)
btn_envoyer.grid(row=5,column=1,columnspan=3,ipadx=75,pady=10)

#root laucher
root["bg"] = "purple"
root.title("formulaire")
root.config(menu=menuBar)
root.mainloop()
