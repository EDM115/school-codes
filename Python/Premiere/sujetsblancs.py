tab=input("Insérez vos valeurs ici : ")

def strtoint(tab):
    indice=tab[0]
    nbr=tab[indice]
    for i in range(len(tab)):
        int_nbr=int(nbr)
        indice=indice+1
    tab=int_nbr
    tab2=tab

def tri_insertion(tab2):
    for i in range(len(tab2)-1):
        k=i+1
        e=tab2[k]
        while k>0 and e<tab2[k-1]:
            tab2[k]=tab2[k-1]
            k=k-1
        tab2[k]=e

def est_trie(tab):
    strtoint(tab)
    tri_insertion(tab2)
    if tab==tab2:
        print(True)
    else:
        print(False)
