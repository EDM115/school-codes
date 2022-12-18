from pile import *

p0 = creerPileVide
p1 = creerPileVide
p2 = creerPileVide
empiler(p0)
j = 3

if j <= taille(p0):
    for i in range(j):
        empiler(p1, depiler(p0))
    while estVide(p0) is False:
        empiler(p2, depiler(p0))
    while estVide(p1) is False:
        empiler(p0, depiler(p1))
    while estVide(p2) is False:
        empiler(p0, depiler(p2))
else:
    print("nombre de rotations > taille")
