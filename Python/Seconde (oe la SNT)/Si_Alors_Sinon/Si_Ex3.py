from gturtle import *
import random

joe=Turtle()

for i in range(4) :
    if (i%2==0) : # i est pair
        joe.setColor(Color.red)
        joe.setPenColor(Color.red)
    else :
        joe.setColor(Color.green) 
        joe.setPenColor(Color.green) 

    r =random.random()
    joe.forward(50)

    if (r<0.5) :
        joe.right(90)
    else :
        joe.left(90)
