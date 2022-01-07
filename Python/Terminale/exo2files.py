def creerFileVide():
    return []

def enfiler(f, x):
    f.append(x)

def defiler(f):
    return f.pop(0)

def estVide(f):
    return len(f)==0

def remplir(f, tab):
    for i in range(len(tab)):
        enfiler(f, tab[i])

def tri(f):
    f1 = creerFileVide()
    f2 = creerFileVide()
    while not estVide(f):
        max = defiler(f)
        while not estVide(f):
            x = defiler(f)
            if x < max:
                enfiler(f1, max)
				max = x
			else:
				enfiler(f1, x)
		enfiler(f2, max)
	while not estVide(f1):
		enfiler(f, defiler(f1))
	while not estVide(f2):
		enfiler(f, defiler(f2))

def copie(f):
	f1 = creerFileVide()
    f2 = creerFileVide()
	while not estVide(f):
		x = defiler(f)
		enfiler(f1, x)
		enfiler(f2, x)
	while not estVide(f2):
		enfiler(f, defiler(f2))
	return f1

def maxi(f):
	f1 = copie(f)
	if not estVide(f1):
		maxi = defiler(f1)
		while not estVide(f1):
			x = defiler(f1)
			if x > maxi:
				maxi = x
		return maxi
	else:
		return null

def taille(f):
	n = 0
	f1 = creerFileVide()
	while not estVide(f):
		a = defiler(f)
		n = n + 1
		enfiler(f1, a)
	while not estVide(f1):
		a = defiler(f1)
		enfiler(f, a)
	return n

def inser_dec(f, x):
	f1 = creerFileVide()
	if not estVide(f):
		while x != None:
			a = defiler(f)
			if x <= a:
				enfiler(f1, x)
				x = None
			else:
				enfiler(f1, a)
		while not estVide(f):
			enfiler(f1, defiler(f))
		while not estVide(f):
			enfiler(f, defiler(f1))