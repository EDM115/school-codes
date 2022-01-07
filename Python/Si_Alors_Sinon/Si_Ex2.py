from gturtle import *
import random

joe=Turtle()
for j in range(4):
    joe.forward(50)
    i =random.random()
    if (i<0.5): 
        joe.setColor(Color.red)
        joe.setPenColor(Color.red)
        joe.right(90)   
    else :
        joe.setColor(Color.green) 
        joe.setPenColor(Color.green)
        joe.left(90)

joe.forward(45)