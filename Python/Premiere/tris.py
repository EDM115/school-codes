t=[666, 882, 0, 2]
t2=[666, 882, 0, 2]
t3=[666, 882, 0, 2]

def tri_selection(t):
    n=len(t)
    for j in range(n-1):
        num=j
        mini=t[j]
        for i in range(j+1, n):
            if t[j]<mini:
                mini=t[i]
                num=i
        t[num]=t[j]
        t[j]=mini
    return t

def tri_insertion(t2):
    for i in range(len(t2)-1):
        k=i+1
        e=t2[k]
        while k>0 and e<t2[k-1]:
            t2[k]=t2[k-1]
            k=k-1
        t2[k]=e
    return t2

def insere(t3, e):
    i=0
    t4=[0]*(len(t3)+1)
    while i<len(t3) and e>t3[i]:
        t4[i]=t3[i]
        i=i+1
    t4[i]=e
    while i<len(t3):
        t4[i+1]=t3[i]
        i=i+1
    return t4
