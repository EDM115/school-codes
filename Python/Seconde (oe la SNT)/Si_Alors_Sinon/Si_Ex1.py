from gturtle import *
import random

i =random.random()
joe=Turtle()
joe.forward(50)
if i<0.5 :
    joe.setColor('red')
    joe.setPenColor('red')
    joe.right(90)
else : 
    joe.setColor('green')
    joe.setPenColor('green')
    joe.left(90)    

joe.forward(45)
