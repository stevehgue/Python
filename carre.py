#!/usr/bin/env python3
from turtle import *
import sys
def carre(x):
        listen()
        forward(x)
        left(90)
        forward(x)
        left(90)
        forward(x)
        left(90)
        forward(x)
        mainloop()
        
number = (int(sys.argv[1]))
carre(number)
    
