import csv

f = open("starwars.csv", "r")
l = csv.reader(f, delimiter=",")
c=[]
for ligne in l:
    c.append(ligne)
f.close

f = open("starwars.csv", "w")
e = csv.writer(f, delimiter=",")
e.writerow(["C3PO"])
e.writerows(["1.67", "droïde", "false", "Tatooine"])
f.close

