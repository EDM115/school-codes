from gturtle2 import *

def onKeyPressed(code):
    global n
    if code == KeyEvent.VK_C:
           n=1
    elif code==KeyEvent.VK_E:
        n=2
    else:
        joe.left(10)

def onKeyReleased(code):
    if code == KeyEvent.VK_LEFT:
       joe.setColor('orange') 

def carre():
    for i in range(4):
        joe.forward(50)
        joe.right(90) 

def triangle():
    for i in range(3):
        joe.forward(100)
        joe.right(120)

joe=makeTurtle(keyPressed=onKeyPressed,keyReleased=onKeyReleased)
n=0
while True:
    if n==1:
        carre()
        n=0
    elif n==2:
        triangle()
        n=0


