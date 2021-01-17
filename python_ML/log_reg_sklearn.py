# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 19:44:08 2020

@author: israe
"""

#Agora fazendo a regressao logistica via sklearn


import numpy as np
import matplotlib.pyplot as plt

#Funcao para visualizar a superficie 
from matplotlib.colors import ListedColormap

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



    
from sklearn import datasets

iris = datasets.load_iris()

X = iris.data[:, [2,3]]
y = iris.target

from sklearn.model_selection import train_test_split

#Dividindo o conjunto de pontos para treinamento e depois validacao
X_train, X_test, y_train,  y_test = train_test_split(X, y, test_size = 0.3, 
                                                     random_state = 1, stratify = y)
print('Contagem dos labels em y:', np.bincount(y))#conta a qntd de ocurrencias dentro do conjunto de dados total

#importando o normalizador do sckit-learn
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std  = sc.transform(X_test)     



from sklearn.linear_model import LogisticRegression

lr = LogisticRegression(C = 100.0, random_state = 1, solver = 'lbfgs', multi_class = 'ovr')
lr.fit(X_train, y_train)

X_combined_std = np.vstack((X_train_std, X_test_std))
y_combined = np.hstack((y_train, y_test))

plot_reg_dec(X_combined_std, y_combined, classificador = lr, test_idx = range(105,150))

plt.xlabel('tamanho da petala [normalizado]')
plt.ylabel('largura da petala [normalizado]')
plt.legend(loc = 'upper left')
plt.tight_layout()
plt.show()




from sklearn.svm import SVC
svm = SVC(kernel = 'linear', C = 1.0, random_state = 1)
svm.fit(X_train_std, y_train)

plot_reg_dec(X_combined_std, y_combined, classificador = svm, test_idx = range(105,150))

plt.xlabel('tamanho da petala [normalizado]')
plt.ylabel('largura da petala [normalizado]')
plt.legend(loc = 'upper left')
plt.tight_layout()
plt.show()


