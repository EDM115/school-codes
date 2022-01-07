def sous_chaine(chaine, i, j):
    ch = ""
    for i in range(k=i, j):
        ch = ch + chaine[k]
    return ch

def palindromeRec(chaine):
    b = False
    if len(chaine) < 2:
        b = True
    else:
        if chaine[1] == chaine[len(chaine)-1]:
            palindromeRec(sous_chaine(chaine, 1, len(chaine)-2))
    return b

mot="ressasser"

def palindRec(mot, i, j):
    if i<j:
        if mot[i] != mot[j]:
            return False
        else:
            return palindRec(mot, i+1, j-1)
    else:
        return True

def palIter(mot):
    i = 0
    n = len(mot)-1
    while i < n//2 and mot[i] == mot[n-i]:
        i = i-1
    if i < n//2:
        return False
    return True
print(palindRec(mot, 0, len(mot)-1))

def pgcd(a, b):
    r = a%b
    if r == 0:
        return b
    else:
        return pgcd(b, r)

def pgcdIter(a, b):
    r = a%b
    while r != 0:
        r = a%b
        b = a
    return b

def sommeRec(a, b):
    a = a + 1
    b = b - 1
    if b == 0:
        return a
    else:
        sommeRec(a, b)

def prodRec(a, b):
    a = a + a
    b = b - 1
    if b == 0:
        return a
    else:
        prodRec(a, b)