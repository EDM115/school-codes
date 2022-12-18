from gturtle import *

# fonction onKeyPressed associe à chaque touche une action 
# paramètre: key code ASCII de la touche enfoncée
# KeyEvent.VK_UP donne le code ASCII de la touche UP

def onKeyPressed(key):# touche enfoncée
    global n
# action à exécuter
    if key == KeyEvent.VK_UP:
        n=1
    else:
        n=2

def onKeyReleased(key): # touche relâchée
# action à exécuter
    global n
    if key == KeyEvent.VK_LEFT:
        n=3

# ligne suivante nécessaire pour que l'écoute clavier soit mise en place
joe=makeTurtle(keyPressed = onKeyPressed, keyReleased = onKeyReleased)
# keyPressed = onKeyPressed:  
# au mot clé keyPressed on associe la méthode onKeyPressed ci-dessus
n=0
while True:
    if n==1:
        joe.setColor('red')
        n=0
    elif n==2:
        joe.setColor('blue')
        n=0
    elif n==3:
        joe.setColor('orange')
        n=0
