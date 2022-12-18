def creerFileVide(n):
    f = [None]*(n+1)
    f[0] = 0
 
    return f

def estPleine(f):
    taille = len(f)-1
    if f[0] == taille:
        return True
    else:
        return False

def estVide(f):
    if f[0] == 0:
        return True
    else:
        return False

def enfiler(f, x):
    if estPleine(f) is False:
        q = f[0]
        f[q+1] = x
        f[0] = q+1
    else:
        print("file pleine")

def defiler(f):
    if estVide(f) is False:
        x = f[1]
        q = f[0]
        f[0] = q-1
        for i in range(1, q):
            f[i] = f[i+1]

f=creerFileVide(5)
enfiler(f, 2); enfiler(f, 3); enfiler(f, 4); enfiler(f, 5)
print(f)
defiler(f)
print(f)