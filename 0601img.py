# Image Compression by PCA
# 2020.06.01

# Libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

# Read image data
img_data = imread("sample_img.jpg")
#print(img_data)
#print(img_data.shape)

# Display the image
#plt.imshow(img_data)
#plt.show()

# Covert RGB image to gray scale
img_sum = img_data.sum(axis = 2)
img_gray = img_sum / img_sum.max()

# Display the image
#plt.imshow(img_gray, cmap=plt.cm.gray)
#plt.show()

# Image compression by PCA
x = np.array(img_gray)

# Compute the mean of x
mu = np.mean(x, axis=0)
x_tilde = x - mu

# Compute the covariance matrix C
N = np.size(x, 1)
C = np.dot(x_tilde, x_tilde.T) / N

# PCA : Store U, Sigma, V
U, sigma, V = np.linalg.svd(C)
#print(sigma[0:20])

# ----------------End of PCA----------------

# Image compression
num_Uk = 20    #num_Uk가 클수록 사진 선명하게 잘보임
Uk = U[:,0]
for k in range(1, num_Uk):
    Uk = np.column_stack((Uk, U[:,k].T))
#print(Uk.shape)

# Projected Image data
y = np.dot(Uk.T, x_tilde)
#print(y.shape)

# Reconstruction from the projected data
xk = np.dot(Uk, y) + mu

# Display the compressed image
plt.imshow(xk, cmap = plt.cm.gray)
plt.show()
