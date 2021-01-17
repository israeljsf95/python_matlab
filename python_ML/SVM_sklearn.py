# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 17:30:54 2020

@author: israe
"""

#Brincando com o sklearn e SMVM

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

from sklearn.svm import SVC
from sklearn import datasets

def plot_reg_dec(X, y, classificador, test_idx = None, resolucao = 0.02):
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
    if test_idx:
        X_test, y_test = X[test_idx, :], y[test_idx]
        plt.scatter(X_test[:, 0], X_test[:,1], c = '', edgecolor = 'black',
                    alpha = 1.0, linewidth = 1, marker = 'o', s= 100, 
                    label = 'dados teste')



iris = datasets.load_iris()

X = iris.data[:, [2,3]]
y = iris.target


from sklearn.model_selection import train_test_split
#importando o normalizador do sckit-learn
from sklearn.preprocessing import StandardScaler

#Dividindo o conjunto de pontos para treinamento e depois validacao
X_train, X_test, y_train,  y_test = train_test_split(X, y, test_size = 0.3, 
                                                     random_state = 1, stratify = y)

sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std  = sc.transform(X_test)    

svm = SVC(kernel = 'linear', C = 1.0, random_state = 1)
svm.fit(X_train_std, y_train)

X_comb = np.vstack((X_train_std, X_test_std))
y_comb = np.concatenate((y_train, y_test))
plot_reg_dec(X_comb, y_comb, classificador = svm, 
                      test_idx = range(105,150))

plt.xlabel('tamanho da petala [norm]')
plt.ylabel('largura da petala [norm]')
plt.legend(loc = 'upper left')
plt.show()


#Brincando como fronteiras linearmente nao separaveis

X_xor = np.random.randn(200,2)
y_xor = np.logical_xor(X_xor[:, 0] > 0, X_xor[:, 1] > 0)
y_xor = np.where(y_xor, 1, -1)

plt.scatter(X_xor[y_xor == 1, 0], X_xor[y_xor == 1, 1], 
            c = 'b', marker = 'x', label = '1')

plt.scatter(X_xor[y_xor == -1, 0], X_xor[y_xor == -1, 1], 
            c = 'r', marker = 's', label = '-1')

plt.xlim([-3, 3])
plt.ylim([-3, 3])
plt.legend(loc = 'best')
plt.tight_layout()
plt.grid()
plt.show()

#Usando funcoes de base radial

svm = SVC(kernel = 'rbf', random_state = 1, gamma = .1, C = 10.0)
svm.fit(X_xor, y_xor)
plot_reg_dec(X_xor, y_xor, classificador = svm)
plt.legend(loc = 'upper left')
plt.tight_layout()
plt.show()

#Usando agora o SVM kernel nos dados Iris

svm = SVC(kernel = 'rbf', random_state = 1, gamma = .2, C = 1.0)
svm.fit(X_train_std, y_train)
plot_reg_dec(X_comb, y_comb, classificador = svm, test_idx = range(105,150))
plt.legend(loc = 'upper left')
plt.tight_layout()
plt.show()



