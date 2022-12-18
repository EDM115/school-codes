def fusion(L1, L2):
	L = [None] * (len(L1) + len(L2))
	i = 0
	j = 0
	k = 0
	while i < len(L1) and j < len(L2):
		if L1[i] > L2[j]:
			L[k] = L2[j]
			j = j + 1
		else:
			L[k] = L[i]
			i = i + 1
		k = k + 1
	if i == len(L1):
		for p in range(k, len(L - 1)):
			L[p] = L2[j]
			j = j + 1
	else:
		for p in range(k, len(L - 1)):
			L[p] = L1[i]
			i = i + 1
	return L

def creer_liste(L, i, j):
	l = [None] * len(j - i + 1)
	for k in range(0, len(l - 1)):
		l[k] = L[i + k]
	return l

def tri_fusion(L):
	n = len(L)
	if n > 1:
		L1 = creer_liste(L, 0, n//2)
		L2 = creer_liste(L, (n//2) + 1, n - 1)
		t1 = tri_fusion(L1)
		t2 = tri_fusion(L2)
		t = fusion(t1, t2)
		return t
	return L
