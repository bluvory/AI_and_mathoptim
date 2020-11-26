import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Data reading
df_train = pd.read_csv('train.csv')
df_test = pd.read_csv('test.csv')
print(df_train)

x_train = df_train['x']
y_train = df_train['y']
x_test = df_test['x']
y_test = df_test['y']

x_train = np.array(x_train)
y_train = np.array(y_train)
x_test = np.array(x_test)
y_test = np.array(y_test)

x_train = x_train.reshape(-1, 1)
y_train = y_train.reshape(-1, 1)
x_test = x_test.reshape(-1, 1)
y_test = y_test.reshape(-1, 1)


# Train : Find a0, a1
n = np.size(x_train)  #700
t = 0.0001  # step size for GD

# Initial
a0 = 0
a1 = 0

# Main Loop - Gradient Descent (GD)
max_iter = 1000
iter = 0

while (iter < max_iter):
    y = a0 + a1*x_train
    Err = y - y_train
    a0 = a0 - t*2.0*np.sum(Err) / n
    a1 = a1 - t*2.0*np.sum(Err*x_train) / n
    # Check MSE
    #MSE = np.sum(Err**2)/n
    #print(MSE)  # For check
    iter = iter + 1
    
    
# Check on training set
y = a0 + a1*x_train
plt.plot(x_train, y_train, 'r.')
plt.plot(x_train, y)
plt.show()


# Prediction
y_pred = a0 + a1*x_test
plt.plot(x_test, y_test, 'y.')
plt.plot(x_test, y_pred, 'k')
plt.show()










