from random import * # pour utiliser shuffle

class Carte():
    valeurs={1:14,'R':13,'D':12,'V':11,10:10,9:9,8:8,7:7,6:6,5:5,4:4,3:3,2:2}
    couleurs=['C','K','P','T']

    def __init__(self, valeur, couleur):
        self.__valeur = valeur
        self.__couleur = couleur

    def print(self):
        print(self.__valeur,self.__couleur)

    def get_valeur(self):
        return self.__valeur

    def __repr__(self):
        if 2 <= self.__valeur <= 10:
            valeur = str(self.__valeur)
        elif self.__valeur == 11:
            valeur = 'Valet'
        elif self.__valeur == 12:
            valeur = 'Dame'
        elif self.__valeur == 13:
            valeur = 'Roi'
        elif self.__valeur == 14:
            valeur = 'As'
        if self.__couleur == 'T':
            couleur = 'Trefle'
        elif self.__couleur == 'K':
            couleur = 'Carreau'
        elif self.__couleur == 'C':
            couleur = 'Coeur'
        elif self.__couleur == 'P':
            couleur = 'Pique'
        return valeur+' de '+couleur

    def get_image(self):
        return "sprites/" + str(self.__valeur) + self.__couleur + ".GIF"

    def afficher_carte(self,tapis,x,y):
        file = Image.open(self.get_image()) # Chargement d'une image à partir de l'API PIL
        self.__image_carte=ImageTk.PhotoImage(file) # Convertit l'image en tableau
        return tapis.create_image(x,y, image=self.__image_carte) # affiche l'image dans le canvas tapis

class Paquet():
    def __init__(self,paquet): # paquet liste des objets de la classe Carte
        self.paquet = paquet

    def get_paquet(self):
        return self.paquet

    def ajouter_carte(self,carte):
        self.paquet.append(carte)

    def est_vide(self):
        if len(self.paquet)==0:
            return True
        return False

    def tirer_carte(self):
        if not self.est_vide():
            return self.paquet.pop(0)
        return None

    def melanger(self):
        shuffle(self.paquet)

    def afficher_paquet(self,tapis,x,y,d=50):
        self.__images = [] # stocke en memoire les images des cartes
        for carte in self.paquet:
            file = Image.open(carte.get_image()) # Chargement de l'image de la carte PIL
            self.__images.append(ImageTk.PhotoImage(file))

        for img in self.__images:
            tapis.create_image(x,y, image=img)
            y=d+y

    def distribuer(self, joueur, n):
        joueur.append

    def vider(self):
        self.paquet=[]

class Joueur:
    def __init__(self,tapis,paquet,x,y):
        self.__tapis = tapis
        self.paquet = paquet
        self.__x = x
        self.__y = y

    def melanger(self):
        self.paquet.melanger()

    def jouer_carte(self):
        if not self.paquet.est_vide():
            carte = self.paquet.tirer_carte()
            self.paquet.afficher_paquet(self, tapis_vert, self.__x, self.__y)

    def vider(self):
        pass

"""
    programme principal
"""

from PIL import Image, ImageTk ## Importation des modules utiles dans PIL
import tkinter as Tk
from tkinter import Canvas,Frame,Button

root = Tk.Tk() # la fenetre de jeu
tapis_vert = Canvas(root, width=800, height=600, bg='green', bd=0, highlightthickness=0) # le tapis de jeu
tapis_vert.grid(row=0,column=0, padx=10,pady=10) # insertion du tapis dans la fenetre
control_panel = Frame(root, bg='#777777')
control_panel.grid(row=0,column=1,ipadx=5)

joueur1=Joueur(tapis_vert,Paquet([]),100,100) # on cree le 1er joueur avec une main vide
joueur2=Joueur(tapis_vert,Paquet([]),700,100)

def init():
    cartes=[] # liste des cartes du jeu
    for e in ['K','C','P','T']:
        cartes=cartes+[Carte(i,e) for i in range(1,10)]+[Carte('R',e),Carte('D',e),Carte('V',e)]

    jeu=Paquet(cartes) # creation du jeu de cartes
    jeu.distribuer(joueur1,8) # distribution de huit cartes au joueur1
    jeu.distribuer(joueur2,8)
    joueur1.paquet.afficher_paquet(tapis_vert,joueur1.x,joueur1.y) # affichage de la main du joueur 1
    joueur2.paquet.afficher_paquet(tapis_vert,joueur2.x,joueur2.y)

def distribuer():
    if not joueur1.paquet.est_vide():
        joueur1.vider()

    if not joueur2.paquet.est_vide():
        joueur2.vider()

    init()

on=False # on= True partie en cours

def start():
    global on
    if  not on:
        distribuer()
    on = True

tapis_carte1_ = None; tapis_carte2_ = None # cartes abattues sur le tapis

def jouer():
    global on,tapis_carte1_,tapis_carte2_

    if tapis_carte1_ is not None: # on efface les cartes abattues precedentes
        tapis_vert.delete(tapis_carte1_)
        tapis_vert.delete(tapis_carte2_)

    if on :
        carte1 = joueur1.jouer_carte() # carte jouee par le joueur 1
        carte2 = joueur2.jouer_carte()

        if carte1 is not None and carte2 is not None:
            tapis_carte1_ = carte1.afficher_carte(tapis_vert,300,300)
            tapis_carte2_ = carte2.afficher_carte(tapis_vert,500,300)
            ramasser(carte1,carte2)
        else:# cas ou la main d'un joueur est vide
            on=False

            if carte1 is None:
                print("joueur2 gagnant")
            else:
                print("joueur1 gagnant")

def ramasser(carte1,carte2): # on distribue les cartes jouees au joueur gagnant
    if  carte1.get_valeur()>carte2.get_valeur():
        joueur1.paquet.ajouter_carte(carte1)
        joueur1.paquet.ajouter_carte(carte2)
    else:
        joueur2.paquet.ajouter_carte(carte1)
        joueur2.paquet.ajouter_carte(carte2)

def stop(): # arret de la partie
    global on,tapis_carte1_,tapis_carte2_
    on=False
    joueur1.paquet.afficher_paquet(tapis_vert,joueur1.x,joueur1.y)
    joueur2.paquet.afficher_paquet(tapis_vert,joueur2.x,joueur2.y)
    tapis_vert.delete(tapis_carte1_)
    tapis_vert.delete(tapis_carte2_)

Button(control_panel, text="start", fg="yellow", bg="black", command=start).pack()
Button(control_panel, text="mélanger paquet1", fg="yellow", bg="black", command=joueur1.melanger).pack()
Button(control_panel, text="mélanger paquet2", fg="yellow", bg="black", command=joueur2.melanger).pack()
Button(control_panel, text="jouer", fg="yellow", bg="black", command=jouer).pack()
Button(control_panel, text="stop", fg="yellow", bg="black", command=stop).pack()

root.mainloop()
