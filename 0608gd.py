# Library
import numpy as np
import matplotlib.pyplot as plt

# Define function and its derivatives
def f(x,y):
    return np.exp(x+3*y-0.1) + np.exp(x-3*y-0.1) + np.exp(-x-0.1)
  
def fx(x,y):
    return np.exp(x+3*y-0.1) + np.exp(x-3*y-0.1) - np.exp(-x-0.1)
    
def fy(x,y):
    return 3*np.exp(x+3*y-0.1) - 3*np.exp(x-3*y-0.1)
    
# Initialize
x0 = -1.0
y0 = 5.0
a = 0.1
b = 0.7
xk = x0
yk = y0
xlist = []   # List for saving updated values
ylist = []   # List for saving updated values
xlist.append(xk)
ylist.append(yk)
iter = 0

# Gradient Descent method with Backtracking line search
#t = 0.001
while True:
    dx = -fx(xk,yk)
    dy = -fy(xk,yk)
    
    # Backtracking Line Search
    t = 1
    while True:
        fkp1 = f(xk+t*dx, yk+t*dy)   # f(xkp1, ykp1)
        fk = f(xk, yk)
        if fkp1 < fk - a*t*(dx**2 + dy**2):
            break
        t = b*t
        
    xkp1 = xk + t*dx
    ykp1 = yk + t*dy
    xlist.append(xkp1)
    ylist.append(ykp1)
    
    if np.sqrt((xkp1-xk)**2 + (ykp1-yk)**2) < 10**(-5):
        print("GD converges at iter=", iter)
        break
    
    xk = xkp1
    yk = ykp1
    
    iter += 1
    
print("x=", xk)
print("y=", yk)

plt.plot(xlist, ylist, '-o')
plt.show()

