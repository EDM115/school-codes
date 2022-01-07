from gturtle import *
import random # module ramdom
joe=Turtle()

pg = joe.getPlayground()# pour utiliser poser une image dans l'aire de jeu
pg.drawImage("carre_rouge.png", 0, 0)# (0,0) coordonnées du centre de l'image dans l'aire de jeu  
joe.penUp()# on lève le crayon pour que joe lise la couleur de l'image et non celle de son crayon
x=int(random.random()*200-100)# position aléatoire en x de la tortue
y=int(random.random()*200)-100 # position aléatoire en y de la tortue
joe.setPos(x,y)

while(joe.getPixelColorStr()=="white"):# tant que joe trouve du blanc, il avance de 1 pixel.
  joe.forward(1)
#remarque: 
#le test joe.getPixelColorStr()=="white" équivaut au test joe.getPixelColor()==Color.white