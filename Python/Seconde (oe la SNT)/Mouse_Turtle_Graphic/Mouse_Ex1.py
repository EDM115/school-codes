from gturtle import *

def onMousePressed(x,y):
    if (x>0):
       joe.setColor('red') 
    else:
        joe.setColor('blue')
    
def onMouseReleased(x,y):
    if (y>0):
       joe.setColor('orange') 

joe=makeTurtle(mousePressed = onMousePressed, mouseReleased=onMouseReleased)
