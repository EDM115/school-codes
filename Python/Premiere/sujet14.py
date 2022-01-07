def recherche(elt, tab):
    search=[]
    for i in range(len(tab)):
        if elt==tab[i]:
            search.append(i)
    return search