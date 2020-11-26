# Libraries
import numpy as np
import pandas as pd  # csv 읽어들이기
import matplotlib.pyplot as plt

# Data Reading
df_train = pd.read_csv('SVM_training_data.csv')
df_test  = pd.read_csv('SVM_test_data.csv')

x1_train = df_train['x']
x2_train = df_train['y']
y_train  = df_train['Label']
x1_test  = df_test['x']
x2_test  = df_test['y']
y_test   = df_test['Label']
# label : 직선의 방정식을 만들었을때 0보다 크면 1, 작으면 -1

x1_train = np.array(x1_train)
x2_train = np.array(x2_train)
y_train  = np.array(y_train)
x1_test  = np.array(x1_test)
x2_test  = np.array(x2_test)
y_test   = np.array(y_test)
x1_train = x1_train.reshape(-1, 1)
x2_train = x2_train.reshape(-1, 1)
x1_test = x1_test.reshape(-1, 1)
x2_test = x2_test.reshape(-1, 1)

plt.scatter(x1_train, x2_train)

# Sequential Minimal Optimization
# Parameter
c = 1.0
n = np.size(x1_train)
lamb = np.zeros(n)
omega = np.zeros(2)
b = 0
iter = 0
max_iter = 100

# Main algorithm (SMO)
while iter < max_iter:
    lamb_old = np.copy(lamb)
    for i in range(0, n):
        omega[0] = np.dot(x1_train.T, lamb*y_train)
        omega[1] = np.dot(x2_train.T, lamb*y_train)
        
        xi = np.array([x1_train[i], x2_train[i]])
        fi = np.dot(omega, xi) + b
        Ei = fi - y_train[i]
        
        j = 0
        if j != i:
            j = np.random.randint(0, n)
            
        xj = np.array([x1_train[j], x2_train[j]])
        fj = np.dot(omega, xj) + b
        Ej = fj - y_train[j]
        
        lambiold = lamb[i]
        lambjold = lamb[j]
        
        s = y_train[i]*y_train[j]
        
        # Compute L, H
        L = 0
        H = 0
        if s == 1:
            L = max(0, lamb[i] + lamb[j] - c)
            H = min(c, lamb[i] + lamb[j])
        elif s == -1:
            L = max(0, lamb[j] - lamb[i])
            H = min(c, c + lamb[j] - lamb[i])
            
        if L == H:
            continue
            
        # Compute k11, k12, k22, eta
        k11 = np.dot(xi.T, xi)
        k12 = np.dot(xi.T, xj)
        k22 = np.dot(xj.T, xj)
        eta = 2 * k12 - k11 - k22
        
        if eta >= 0:
            continue
            
        # lambda j new
        lamb[j] = lamb[j] + (y_train[j]*(Ej - Ei)) / eta
        lamb[j] = max(lamb[j], L)
        lamb[j] = min(lamb[j], H)
        
        if abs(lamb[j] - lambjold) < 1e-5:
            continue
            
        # lambda  i new
        lamb[i] = lambiold + s*(lambjold - lamb[j])
        
        # Update b
        b_temp = y_train - omega[0]*x1_train - omega[1]*x2_train
        b = np.mean(b_temp)
        
    print("iter: ", iter)
    
    error = np.linalg.norm(lamb - lamb_old)
    if error < 1e-3:
        print("Converge!")
        break
        
    iter = iter +1

print("Training is over!")

# Visualization
x = np.linspace(min(x1_train), max(x1_train), 101)
y = - omega[0]/omega[1]*x - b/omega[1]
plt.plot(x, y)
plt.scatter(x1_train, x2_train)
plt.show()

# Prediction
y_pred = np.sign(omega[0]*x1_test + omega[1]*x2_test + b).astype(int)
n_test = np.size(y_pred)
count = 0

for k in range(0, n_test):
    if y_pred[k] == y_test[k]:
        count = count+1
        
acc = count / n_test
print("Accuracy of SVM : ", acc)    # 정확도 알아보기
