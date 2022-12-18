import csv
fichier = open("Prenoms2003_sans_accent.csv", "r")
lecture = csv.DictReader(fichier, delimiter=",")
contenu=[]
for ligne in lecture:
    contenu.append(dict(ligne))
    fichier.close()
print(contenu())
