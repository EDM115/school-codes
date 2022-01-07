from gturtle import *

def onMousePressed(x,y):
    if (isLeftMouseButton()):
       joe.setColor('red') 
    else:
        joe.setColor('blue')
    
def onMouseReleased(x,y):
    if (isRightMouseButton()):
       joe.setColor('orange') 

joe=makeTurtle(mousePressed = onMousePressed, mouseReleased=onMouseReleased)
