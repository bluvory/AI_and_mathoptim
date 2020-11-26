# GD

dictx1 = {0 : 9}
dictx2 = {0 : 1}
t = 0.0001

def x1(i):
    if i in dictx1:
        return dictx1[i]
    dictx1[i] = x1(i-1) + t*-x1(i-1)
    return dictx1[i]
    
def x2(i):
    if i in dictx2:
        return dictx2[i]
    dictx2[i] = x2(i-1) + t*-9*x2(i-1)
    return dictx2[i]

def func(x1, x2):
    return 1/2*(x1**2 + 9*x2**2)

iter = 0
max_iter = 100
e = 10**(-5)
k = 0

while ( ((x1(k+1) - x1(k))**2 + (x2(k+1) - x2(k))**2 )**1/2 < e ):
    a1 = x1(k)
    a2 = x2(k)
    k = k+1
    iter = iter + 1
    if iter > max_iter:
        print(func(a1, a2))
        break
