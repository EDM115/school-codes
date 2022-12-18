def creerPileVide(n):
    tab = [None]*(n+1)
    tab[0] = 0
    return tab

def estVide(tab):
    vide = False
    if tab[0] == 0:
        vide = True
    return vide

def estPleine(tab):
    pleine =  False
    if tab[0] == len(tab):
        pleine = True
    return pleine

def empiler(tab, elt):
    if estPleine(tab) is not True:
        k = tab[0] + 1
        tab[k] = elt
        tab[0] = k
    else:
        print("pile pleine")

def depiler(tab):
    if estVide(tab) is not True:
        elt = tab[tab[0]]
        tab[0] = tab[0] - 1
        return elt
    else:
        print("pile vide")

def top(tab):
    if estVide(tab) is not True:
        elt = depiler(tab)
        empiler(tab, elt)
        return elt
    print("pile vide")

def taille(pile):
    n=0
    p=creerPileVide()
    while estVide(pile) is False:
        n=n+1
        empiler(p, depiler(pile))
    while estVide(p) is False:
        empiler(pile, depiler(p))

""" pile = creerPileVide(5)
empiler(pile, "a")
empiler(pile, "b")
print(estPleine(pile))
print(estVide(pile))
a = depiler(pile)
print(a)
print(pile[0]) """
