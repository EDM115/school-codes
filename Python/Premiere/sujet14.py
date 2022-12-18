def recherche(elt, tab):
    search=[]
    for i, item in enumerate(tab):
        if elt==item:
            search.append(i)
    return search
