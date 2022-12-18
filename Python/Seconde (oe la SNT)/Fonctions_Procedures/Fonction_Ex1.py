from gturtle import *
joe=Turtle()

def carre(tortue=joe,longueur=100):
    for i in range(4):
        tortue.forward(longueur)
        tortue.right(90)

jack=Turtle(joe)
joe.setPos(100,0)
jack.setPos(-100,0)
jack.setColor('red')
jack.setPenColor('red')
luka=Turtle(joe)
luka.setPos(-300,0)
luka.setColor('green')
luka.setPenColor('green')
carre()
carre(luka)
carre(longueur=50)
carre(jack,20)
