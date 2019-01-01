from math import *
from random import *
#calcul les carre des nombres entre 1 et la valeure passée en paramètre
def Carre(val):
    i = 1
    while i < val:
        print(i*i)
        i += 1

Carre(5)
#lance un de tant que celui-ci ne sort pas de 2
de = 0
while de != 2:
    de = randint(1,6)
    print(de)

