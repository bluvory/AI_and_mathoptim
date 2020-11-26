#numpy array

import numpy as np

x = np.array([1.0, 2.0, 3.0, 4.0])
print(x)
print(type(x))

y = np.array([2.0, 3.0, 5.0, 9.0])

print("x+y=", x+y)
print("x-y=", x-y)
print("x*y=", x*y)
print("x/y=", x/y)

a = np.array([[1,2], [3,4]])
print(a)
print(a.dtype)
print(a.shape)

a = np.array([[1,2], [3,4]])
b = np.array([[1,0], [0,4]])
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print(a[0])
print(a[0][1])

a = a.flatten()
print(a)
print(a>3)  # false false false true
print(a[a>3])
# for i in range(0,4): if [i]>3: print(a[i])


#broadcast
a = np.array([[1,2], [3,4]])
b = a*5
print(b)
c = np.array([20,30])
print(a*c)

