from pile import *
p0 = creerPileVide(5)
p1 = creerPileVide(len(p0))
a = depiler(p0)
while estVide(p0) is False:
	b = depiler(p0)
	empiler (p1, b)
empiler(p0, a)
while estVide(p1) is False:
	b = depiler(p1)
	empiler (p0, b)
