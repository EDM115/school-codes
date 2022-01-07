from gturtle import *

def onMousePressed(x,y):
    global X,Y
    global n
    n=1
    X=x;Y=y
    if (x>0):
       joe.setColor('red') 
    else:
        joe.setColor('blue')
    
def onMouseReleased(x,y):
    if (y>0):
       joe.setColor('orange') 

joe=makeTurtle(mousePressed = onMousePressed, mouseReleased=onMouseReleased)
n=0
X=Y=0
while (True):
    if (n==1):
        print(X,Y)
        n=0