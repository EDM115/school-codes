Pieces = [100,50,20,10,5,2,1]
def rendu_glouton(arendre, solution=[], i=0):
       if arendre == 0:
       return ...
    p = pieces[i]
    if p <= ... :
        return rendu_glouton(arendre - p, solution.append(...),i)
    else :
        return rendu_glouton(arendre, solution, ...)
