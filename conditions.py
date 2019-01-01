#!/usr/bin/env python3
from random import*;
nombre = float(input("Choisissez un nombre : "))
if nombre > 10 :
    print("Le nombre choisi est plus grand que 10")
#vérifie que le nombre saisi est supérieur a 10

age = int(input("Saisir votre age"))
if age < 18 :
    print("Vous êtes mineur")
else:
    print("Vous êtes majeur")
#verifie si l'utilisateur est majeur

nb = int(input("Veuillez saisir un nombre"))
if nb % 6 == 0:
    print("Le nombre est un multiple de 6")
elif nb % 3 == 0:
    print("Le nombre est un multiple de 3 mais pas de 6")
elif nb % 2 == 0:
    print("Le nombre est un multiple de 2 mais pas de 6")
else:
    print("Le nombre n'est ni un multiple de 2, ni de 3")
#regarde si un nombre est un multiple de 6,3 et pas 6, 2 mais pas 6, ni 2, ni 3

temperature = int(input("choisir la temperature"))
if temperature > 0 and temperature < 100:
    print("L'eau est liquide")
#il regarde si la temperature saisie correspond a la plage des temperature de l'eau liquide

eau = int(input("Choisir temperature eau"))
air = int(input("Choisir temperature air"))

if air > 25 or eau > 20:
    print("Tu peux aller a la plage")
else:
    print("Tu ne peux pas aller a la plage")
#verifie si avec les temperatures saisies la personne peut aller a la plage

def maximum(a, b):
    if a > b:
        return a
    else:
        return b

mdp = input("Entrez un mot de passe")
if mdp== "James-Bob":
    print("Bon mot de passe")
else:
    print("BIP")

#verifie le mot de passe rentré
def cinema(age):
    if age < 10:
        print("Le prix sera de 6€")
    elif age < 10 and age < 18:
        print("Le prix sera de 5€")
    else:
        print("Le prix sera de 8€")

#regarde les tarifs par rapport à l'âge
