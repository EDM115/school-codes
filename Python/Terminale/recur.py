def horner(t, n, x):
    h = 0
    if n == len(t-1):
        h = a[n]
    else:
        h = a [n] + x*horner(t, n+1, x)
    return h
def fibo(n):
    F = 0
    if n <= 2:
        F = 1
    else:
        F = fibo(n-1) + fibo(n-2)
    return F
F = [1, 1]
def fiboDyn(n, F):
	if n < len(F):
		f = F[n]
	else:
		F[n] = fiboDyn(n-1) + fiboDyn(n-2)
		f = F[n]
	return f
t=[8,4,2,1]
n=4
x=2