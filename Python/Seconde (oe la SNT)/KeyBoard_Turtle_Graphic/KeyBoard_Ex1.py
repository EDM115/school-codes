from gturtle import *

def onKeyPressed(code):
    if code == KeyEvent.VK_UP:
       joe.setColor('red') 
    else:
        joe.setColor('blue')

def onKeyReleased(code):
    if code == KeyEvent.VK_LEFT:
       joe.setColor('orange') 
    
joe=makeTurtle(keyPressed=onKeyPressed,keyReleased=onKeyReleased)
