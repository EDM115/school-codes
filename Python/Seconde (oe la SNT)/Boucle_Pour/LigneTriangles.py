from gturtle import *

joe=Turtle()

for i in range(4):
    joe.setPos(-190+i*100,0);
    for j in range(3):
        joe.forward(50)
        joe.right(120)
    
joe.hideTurtle()