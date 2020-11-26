import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x_data = [2.5, 0.5, 2.2, 1.9, 3.1, 2.3,   2,   1, 1.5, 1.1]
y_data = [2.4, 0.7, 2.9, 2.2, 3.0, 2.7, 1.6, 1.1, 1.6, 0.9]

x_data = np.array(x_data)
y_data = np.array(y_data)

mu_x = np.mean(x_data)
mu_y = np.mean(y_data)

x_data_tilde = x_data - mu_x
y_data_tilde = y_data - mu_y

X_tilde = np.row_stack((x_data_tilde.T,y_data_tilde.T))

N = np.size(x_data,0)
C = np.dot(X_tilde,X_tilde.T)/N

eigenvalues, eigenvectors = np.linalg.eig(C)

v1 = eigenvectors[0]
v2 = eigenvectors[1]

plt.arrow(mu_x,mu_y,v1[0],v1[1])
plt.arrow(mu_x,mu_y,v2[0],v2[1])
plt.scatter(y_data,x_data,marker=".")
plt.axis('equal')
plt.show()

