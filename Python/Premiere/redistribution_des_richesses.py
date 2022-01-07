pieces = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
qte = [3, 5, 2, 20, 80, 67, 49, 75, 63, 45, 35, 75, 37, 67, 59, 46
rendu = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
s = float(input("somme a rendre : "))
i=0
c=0
def affiche(pieces, rendu):
    a = []
    for i in range (len(pieces)):
        if rendu[i]!=0:
            a.append(pieces[i], rendu[i])
    print a
while s>0:
    if pieces[i]<=s and qte[i]!=0:
        s=s-pieces[i]
        qte[i]=qte[i]-1
        rendu[i]=rendu[i]+1
    else:
        i=i+1
affiche(pieces, rendu)