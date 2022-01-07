def creerFileVide(n):
    f = [None]*(n+3)
    f[0] = 3
    f[1] = 3
    f[2] = 0
    return f

def estPleine(f):
	n = len(f)-3
	if f[2] == n:
    	return True
    else:
        return False 

def estVide(f):
    if f[1] == 0:
        return True
    else:
        return False

def enfiler(f, x):
	if estPleine(f)==False:
		n = len(f)-3
		q = f[1]
		if q != n+3:
			f[q+1] = x
			f[1] = q+1
			f[2] = f[2]+1
		else:
			q = 4
			f[q] = x
			f[1] = q
			f[2] = f[2]+1

def defiler(f):
	if estVide(f)==False:
		n = len(f)-3
		t = f[1]
		if q != n+3:
			x = f[t]
			f[0] = f[1]+1
			f[2] = f[2]+1
		else:
			q = 4
			f[q] = x
			f[1] = q
			f[2] = f[2]+1