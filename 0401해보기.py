# 0401 do it yourself
import matplotlib.pyplot as plt
a = 0
b = 2
c = 4
d = 6
n = 401
dx1 = (b-a)/(n-1)
dx2 = (c-b)/(n-1)
dx3 = (d-c)/(n-1)
x_list = []
y_list = []

for i in range(0,n):
    x = a + i*dx1
    y = x**2-2*x+2
    x_list.append(x)
    y_list.append(y)

for i in range(0,n):
    x = b + i*dx2
    y = -x**2+6*x-8
    x_list.append(x)
    y_list.append(y)
    
for i in range(0,n):
    x = c + i*dx3
    y = x**2-10*x+26
    x_list.append(x)
    y_list.append(y)
    
plt.plot(x_list, y_list)
plt.show()
