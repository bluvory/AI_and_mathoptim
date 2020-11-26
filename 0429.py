import matplotlib.pyplot as plt

# function
def f(x, y):
    return 5*x**2 - 6*x*y + y**2
    
def fx(x, y):
    return 10*x - 6*y
    
def fy(x, y):
    return -6*x + 10*y
    
# initial point
x0 = -0.5
y0 = -0.1

# descent method
eta = 0.1
method = "CD"
xn = x0
yn = y0
xlist = []
ylist = []
xlist.append(xn)
ylist.append(yn)

max_iter = 20

if method == "CD":
    for k in range(0, max_iter):
        xnp1 = xn - eta*fx(xn ,yn)
        ynp1 = yn - eta*fy(xnp1, yn)
        xlist.append(xnp1)
        ylist.append(ynp1)
        xn = xnp1
        yn = ynp1
        
elif method == "GD":
    for k in range(0, max_iter):
        xnp1 = xn - eta*fx(xn ,yn)
        ynp1 = yn - eta*fy(xn, yn)
        xlist.append(xnp1)
        ylist.append(ynp1)
        xn = xnp1
        yn = ynp1
        
plt.plot(xlist, ylist, '-o')
plt.show()
