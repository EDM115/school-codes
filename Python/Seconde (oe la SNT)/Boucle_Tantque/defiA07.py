from gturtle import *
joe=Turtle()

pg = joe.getPlayground()# pour utiliser poser une image dans l'aire de jeu
pg.drawImage("chemin_rouge.png", 0, 0)# (0,0) coordonnées du centre de l'image dans l'aire de jeu  
joe.penUp()# on lève le crayon pour que joe lise la couleur de l'image et non celle de son crayon
joe.setPos(-175,50)
