from random import *
##ex 27, tables de multiplications de 1 à 10 d'un nombre passe en parametre
for i in range(1,11) :
    print("3 * ", i, " = ", 3*i)

#ex 28, carreu du nombre passe en parametre
def carre(val):
     i = 1
     while i < val :
         carre = i * i
         print(carre)
         i = i + 1
     for i in range(1, val + 1) :
        carre = i * i
        print(carre)

#ex 29, simulation de lancé de tant que celui-ci ne sort pas de 2
number = random.randint(1, 6)
while number != 2 :
    number = random.randint(1, 6)
