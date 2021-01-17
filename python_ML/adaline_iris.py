# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 02:33:10 2020

@author: israe
"""

import numpy as np
import matplotlib.pyplot as plt


class AdalineSGD(object):
    
    def __init__(self, eta = 0.01, n_iter = 50, shuffle = True, random_state = 1):
        self.eta = eta
        self.n_iter = n_iter
        self.w_initialized = True
        self.shuffle = shuffle
        self.random_state = 1
        
        
    def fit(self, X, y):
        
        self._initialize_weights(X.shape[1])
        self.cost_ = []
        
        for i in range(self.n_iter):
            if self.shuffle:
                X, y = self._shuffle(X, y)
            cost = []
            for xi, target in zip(X, y):
                cost.append(self._update_weights(xi,target))
            avg_cost = sum(cost)/len(y)
            self.cost_.append(avg_cost)
        return self
    
    def partial_fit(self, X, y):
        if not self.w_initialized:
            self._initialize_weights(X.shape[1])
        if y.ravel().shape[0] > 1:
            for xi, target in zip(X,y):
                self._update_weights(xi, target)
        else:
            self._update_weights(X, y)
        return self
    
    def _shuffle(self, X, y):
        r = self.rgen.permutation(len(y))
        return X[r], y[r]
    
    def _initialize_weights(self, m):
        self.rgen = np.random.RandomState(self.random_state)
        self.w_ = self.rgen.normal(loc = 0.0, scale = 0.01,
                                   size = 1 + m)
        self.w_initalized = True            
    
    def _update_weights(self, xi, target):
        output = self.activation(self.net_input(xi))
        error = target - output
        self.w_[1:] += self.eta*xi.dot(error)
        self.w_[0] += self.eta*error
        cost = 0.5*(error**2)
        return cost
    
    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]
    
    def activation(self, X): #Ativacao linear
            return X
   
    def predict(self, X):
        return np.where(self.activation(self.net_input(X)) >= 0.0, 1, -1)


#Criando funcao para visualizar a fronteira de decisao

from matplotlib.colors import ListedColormap

def plot_reg_dec(X, y, classificador, resolucao = 0.02):
    markers = ('s', 'x', 'o', '^','v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])
    x1_min, x1_max = X[:,0].min() - 1, X[:,0].max() + 1
    x2_min, x2_max = X[:,1].min() - 1, X[:,1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolucao),
                           np.arange(x2_min, x2_max, resolucao))
    Z = classificador.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha = 0.3, cmap = cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    
    #plotando os exmplos
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x = X[y == cl, 0],
                    y = X[y == cl, 1],
                    alpha = 0.8,
                    c = colors[idx],
                    marker = markers[idx],
                    label = cl,
                    edgecolor = 'black'
                    )



fig, ax = plt.subplots(nrows = 2, ncols = 2, figsize = (10,10))


import os 
import pandas as pd

s = os.path.join('https://archive.ics.uci.edu', 'ml', 
                 'machine-learning-databases', 'iris', 'iris.data')
print('URL: ', s)

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header = None, encoding = 'utf-8')
df.tail()            

y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)
X = df.iloc[0:100, [0,2]].values


#Normalizando X
X_std = np.copy(X)
X_std[:, 0] = (X[:, 0] - X[:, 0].mean()) / X[:,0].std()
X_std[:, 1] = (X[:, 1] - X[:, 1].mean()) / X[:,1].std()                
                



ada1 = AdalineSGD(n_iter = 50, eta = 0.01).fit(X,y)
ax[0][0].plot(range(1, len(ada1.cost_) + 1),
          np.log10(ada1.cost_), marker = 'o')
ax[0][0].set_xlabel('Epochs')
ax[0][0].set_ylabel('log(Sum-squared-error)')
ax[0][0].set_title('Adaline - Learning rate 0.01')


ada2 = AdalineSGD(n_iter = 50, eta = 0.0001).fit(X,y)
ax[0][1].plot(range(1, len(ada2.cost_) + 1),
          np.log10(ada2.cost_), marker = 'o')
ax[0][1].set_xlabel('Epochs')
ax[0][1].set_ylabel('log(Sum-squared-error)')
ax[0][1].set_title('Adaline - Learning rate 0.0001')



ada_gd1 = AdalineSGD(n_iter = 50, eta = 0.01).fit(X_std,y)
ax[1][0].plot(range(1, len(ada_gd1.cost_) + 1),
          np.log10(ada_gd1.cost_), marker = 'o')
ax[1][0].set_xlabel('Epochs')
ax[1][0].set_ylabel('log(Sum-squared-error)')
ax[1][0].set_title('Adaline_STD - Learning rate 0.01')


ada_gd2 = AdalineSGD(n_iter = 50, eta = 0.0001).fit(X_std,y)
ax[1][1].plot(range(1, len(ada_gd2.cost_) + 1),
          np.log10(ada_gd2.cost_), marker = 'o')
ax[1][1].set_xlabel('Epochs')
ax[1][1].set_ylabel('log(Sum-squared-error)')
ax[1][1].set_title('Adaline_STD - Learning rate 0.0001')

plt.show()    
    
        
plot_reg_dec(X_std, y, classificador = ada_gd2)
plt.title('Adaline - Stochastic Gradient Descent eta = 0.0001')
plt.xlabel('sepal length [normalizado] ')
plt.ylabel('petal length [normalizado] ')
plt.legend(loc = 'upper left')
plt.tight_layout()
plt.show()

plot_reg_dec(X_std, y, classificador = ada_gd1)
plt.title('Adaline - Stochastic Gradient Descent eta = 0.01')
plt.xlabel('sepal length [normalizado] ')
plt.ylabel('petal length [normalizado] ')
plt.legend(loc = 'upper left')
plt.tight_layout()
plt.show()


    