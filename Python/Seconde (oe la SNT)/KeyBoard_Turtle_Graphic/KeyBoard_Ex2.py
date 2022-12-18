from gturtle import *

# fonction onKeyPressed associe à chaque touche une action 
# paramètre: key code ASCII de la touche enfoncée
# 38: code ASCII de la touche UP
# 37: code ASCII de la touche LEFT

def onKeyPressed(key): # touche enfoncée
# action à exécuter
    if key == 38: #UP
       joe.setColor('red') 
    else:
        joe.setColor('blue')

def onKeyReleased(key): # touche relâchée
# action à exécuter
    if key == 37: #LEFT
       joe.setColor('orange') 

# ligne suivante nécessaire pour que l'écoute clavier soit mise en place
joe=makeTurtle(keyPressed = onKeyPressed , keyReleased = onKeyReleased)
# keyPressed = onKeyPressed: 
# au mot clé keyPressed on associe la méthode onKeyPressed ci-dessus
