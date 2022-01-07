import csv
import math
from tkinter import *

largeur=750
hauteur=750
x_centre=375
y_centre=375
dmax=200


#1. Fonction qui renvoie le dictionnaire des étoiles
def creationDico(filename):
    """
    :param filename: nom du fichier csv
    :type filename: string
    :return: dictionnaire d'étoiles
    """

    ###############################
    #A COMPLETER
    ###############################


#2. Fonction qui calcule la distance projetée d'une étoile par rapport au pôle nord céleste à partir de sa déclinaison
def distanceProjeteeEtoile(declinaison):
    """
    :param declinaison: valeur de DErad
    :type declinaison: float
    :return: la distance relative
    :rtype: float
    """

    ###############################
    #A COMPLETER
    ###############################

#3. Fonction qui transforme les coordonnées polaires en coordonnées cartésiennes
def coordonneeEtoile(distance,angle):
    """
    :param distance: distance de l'étoile au pôle nord céleste
    :type distance: float
    :param angle: angle en radians
    :type angle: float
    :return: abscisse et ordonnée de l'étoile
    :rtype : tuple de 2 floats
    """

    ###############################
    #A COMPLETER
    ###############################

#4. Fonction qui renvoie le diamètre apparent de l'étoile
def diametreEtoile(magnitude):
    """
    :param magnitude: valeur de Hpmag
    :type magnitude:float
    :return: diamètre apparent de l'étoile
    :rtype: float
    """

    ###############################
    #A COMPLETER
    ###############################

#5. Fonction qui affiche une étoile
def affichageUneEtoile(ciel,distance,angle,couleur,diametre):
    """
    :param ciel: le canvas (le panneau de dessin)
    :type ciel: Canvas
    :param distance: distance projetée de l'étoile par rapport au pôle nord céleste
    :type distance:float
    :param angle: angle en radians
    :type angle: float
    :param diametre: diamètre apparent de l'étoile
    :type diametre: float
    :return: l'affichage de l'étoile
    """

    global x_centre,y_centre #abscisse et ordonnée   du centre de la représentation graphique, le pôle nord céleste
    ###############################
    #A COMPLETER
    ###############################

#6. Fonction qui affiche toutes les étoiles
def affichageToutesEtoiles(ciel):
    """
    :param ciel: le canvas (le panneau de dessin)
    :type ciel: Canvas
    :param critere: liste des criteres (intervalle de magnitude) ou None pour afficher toutes les étoiles
    :type critere: tuple ou None
    :return: l'affichage des étoiles
    """

    global dicoEtoiles #dicoEtoiles contient la liste des dictionnaires des étoiles
    ###############################
    #A COMPLETER
    ###############################

#PROGRAMME PRINCIPAL

#Creation de la fenêtre graphique

###############################
#A COMPLETER
###############################


#A COMPLETER  #création de la liste de dictionnaires
#A COMPLETER #affichage de la carte des étoiles
