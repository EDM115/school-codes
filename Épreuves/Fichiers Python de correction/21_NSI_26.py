def nbLig(image):
    '''renvoie le nombre de lignes de l'image'''
    return ...

def nbCol(image):
    '''renvoie la largeur de l'image'''
    return ...

def negatif(image):
    '''renvoie le négatif de l'image sous la forme 
       d'une liste de listes'''
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))] # on créé une image de 0 aux mêmes dimensions que le paramètre image 
    for i in range(len(image)):
        for j in range(...):
            L[i][j] = ...
    return L

def binaire(image, seuil):
    '''renvoie une image binarisée de l'image sous la forme 
       d'une liste de listes contenant des 0 si la valeur 
       du pixel est strictement inférieure au seuil 
       et 1 sinon'''
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))] # on crée une image de 0 aux mêmes dimensions que le paramètre image 
    for i in range(len(image)):
        for j in range(...):
            if L[i][j] < ... :
                L[i][j] = ...
            else:
                L[i][j] = ...
    return L
