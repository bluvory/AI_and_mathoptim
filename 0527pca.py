# Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Data reading
df_data = pd.read_csv('PCA_Test_data.csv')
x_data = df_data['x']
y_data = df_data['y']
x_data = np.array(x_data)
y_data = np.array(y_data)
x_data = x_data.reshape(-1, 1)
y_data = y_data.reshape(-1, 1)

# Debug
#plt.scatter(x_data, y_data)
#plt.show()

# Principal Component Analysis (PCA)
# Compute Mean
mu_x = np.mean(x_data)
mu_y = np.mean(y_data)

# Define a (shifted) data matrix
x_data_tilde = x_data - mu_x   # (987, 1)
y_data_tilde = y_data - mu_y   # (987, 1)
x_tilde = np.row_stack((x_data_tilde.T, y_data_tilde.T))   # 행쌓기
#print(x_tilde.shape)  # (2행 987열)

# Compute the Covariance Matrix Component
N = np.size(x_data, 0)   # 987
C = np.dot(x_tilde, x_tilde.T)/N
#print(C)

# Do the PCA : Eigendecomposition of C
eigenvalues, eigenvectors = np.linalg.eig(C)
#print(eigenvalues, eigenvectors)

# Visualization
v1 = eigenvectors[0]
v2 = eigenvectors[1]

plt.arrow(mu_x, mu_y, v1[0], v1[1])   #시점2, 종점2
plt.arrow(mu_x, mu_y, v2[0], v2[1])
plt.scatter(x_data, y_data)
plt.scatter(y_data, x_data, marker='.')
plt.axis('equal')
plt.show()

