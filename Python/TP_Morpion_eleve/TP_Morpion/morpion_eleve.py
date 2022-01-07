from tkinter import *


btns=[[None,None,None],[None,None,None],[None,None,None]]# la grille de boutons
M=[[0,0,0],[0,0,0],[0,0,0]] # la grille de jeu (0= libre,-1=joueur 1,1= joueur2)
L=[[],[],[]] # représente les lignes
C=[[],[],[]] # représente les colonnes
D=[[],[]] # représente les diagonales
code_player=-1 # code associé au joueur (-1= joueur 1, 1= joueur 2)
code_winner=0 # code associé au gagnant (1= joueur 1, 2= joueur 2, 0= pas de gagnant)
n=0 # nombre de coups joués n max= 9
Symbol=['O','X'] # symbole de chaque joueur sur les boutons

def update(i,j,code_player):
    pass

def check(L):
    global code_winner
    # a completer
    pass

def game(evt,i,j):
    global btns,code_player,code_winner,n
    # a completer
    pass

def reset():
    global btns,M,L,C,D,n,code_player,code_winner
    pass

# partie graphique programme principal

#creation de la fenetre (Tk=fenetre)
morpion = Tk()
morpion.title("MORPION")

#Creation de la grille de boutons

for ... in range(...):
    for ...
        btns[...][...]=Button(morpion,height =9 ,width = 20) # creation du bouton de coordonnées (i;j),
        btns[...][...].grid(row=i, column=j, sticky=N+S+E+W) # insertion du bouton dans la grille
        btns[...][...].bind('<Button-1>',lambda evt,i_=i,j_=j:game(evt,i_,j_)) # association d'une action au bouton
btn_reset=Button(morpion,text='RESET',height =2 ,width = 20,command=reset)
btn_reset.grid(row=3, column=1)

morpion.mainloop()