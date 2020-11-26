import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

t = 0.0001

def x1(i):
    if i == 0:
        return 9
    else:
        return x1(i-1) + t*-1*x1(i-1)

def x2(i):
    if i == 0:
        return 1
    else:
        return x2(i-1) + t*-9*x2(i-1)

def f(x1, x2):
    return 1/2*(x1**2 + 9*x2**2)

x1_train = []
x2_train = []
y_train = []

for i in (0, 100):
    x1_train.append(x1(i))
    x2_train.append(x2(i))
    y(i)=f(x1(i), x2(i))
    y_train.append(y(i))

x1_data = np.array(x1_train)
x2_data = np.array(x2_train)
y_data = np.array(y_train)

a1 = 0
a2 = 0
b = 0
k = 0
n = 3

iter = 0
max_iter = 100
e = 10**-5


while (f(x1(k+1)-x1(k), x2(k+1)-x2(k))<e):
    y = a1*x1_data + a2*x2_data + b
    Err = y - y_data
    a1 = a1 - t*2*np.sum(Err*x1_data) / n
    a2 = a2 - t*2*np.sum(Err*x2_data) / n
    b = b - t*2*np.sum(Err) / n
    iter = iter + 1
    k = k+1
    if iter > max_iter:
        print(y)
        break
    
