t_moy=[14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees=[2013, 2014, 2015, 2016, 2017, 2018, 2019]

def tri_insertion(t2):
    for i in range(len(t2)-1):
        k=i+1
        e=t2[k]
        while k>0 and e<t2[k-1]:
            t2[k]=t2[k-1]
            k=k-1
        t2[k]=e
    return t2

def mini(releve, date):
    a=tri_insertion(releve)
    print(a[0])

mini(t_moy, annees)