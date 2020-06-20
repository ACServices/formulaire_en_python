#!/usr/bin/python3.7
from donnees import *
from pickle import Pickler,Unpickler
def enregistrer(*args):
    users = {}
    users["nom"] = nomVar.get()
    users["prenom"] = prenomVar.get()
    users["email"] = emailVar.get()
    users["age"] = ageVar.get()
    users["faculty"] = facultyVar.get()
    users["pays"] = paysVar.get()
    users["sexe"] = sexeVar.get()
    with open("users","wb") as userFile:
         userFilePickler = Pickler(userFile)
         userFilePickler.dump(users)
def afficher(*args):
    print("nom:{}, prenom:{}, email:{}, age:{}, faculty:{}, pays:{}, sexe:{}"\
          .format(nomVar.get(),prenomVar.get(),emailVar.get(),ageVar.get(),facultyVar.get(),paysVar.get(),sexeVar.get()))

