def concat(t1,t2):
    #t:tableau d'entiers de taille n
    #t1:tableau d'entiers de taille n
    #t2:tableau d'entiers de taille n
    t=[]
    t[0]*len(t1)
    n=len(t)
    for i in range(1,n):
        t[i]=t1[i]
    for i in range(1,n):
        t[n+i]=t2[i]
    return t

def sansdoublons(t):
    j=0
    while j<len(t)-1:
        i=j+1
        while i<len(t):
            if t[j]==t[i]:
                del t[i]
            else:
                i=i+1
        j=j+1

t1=[2, 5, 8, 13]
t2=[11, 14, 5, 7]