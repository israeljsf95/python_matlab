# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 11:18:36 2020

@author: israe
"""
#Brincando com scikit-learn


from sklearn import datasets
import numpy as np


iris = datasets.load_iris()

X = iris.data[:, [2,3]]
y = iris.target
print('Lables das Classes: ', np.unique(y))

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

#importando o classificador
from sklearn.linear_model import Perceptron
pepe = Perceptron(eta0 = 0.1, random_state = 1)
pepe.fit(X_train_std, y_train)
y_pred = pepe.predict(X_test_std)

print(f'Exemplos Classificados errados: {(y_test != y_pred).sum()}')

from sklearn.metrics import accuracy_score

print('Acuracia: %.3f' %accuracy_score(y_test, y_pred))
print('Acuracia: %.3f' %pepe.score(X_test_std, y_test))


#Criando funcao para visualizar a fronteira de decisao
import matplotlib.pyplot as plt
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

X_combined_std = np.vstack((X_train_std, X_test_std))
y_combined = np.hstack((y_train, y_test))
plot_reg_dec(X = X_combined_std, y = y_combined, classificador = pepe, test_idx = range(105,150))
plt.xlabel('sepal length [normalizado] ')
plt.ylabel('petal length [normalizado] ')
plt.legend(loc = 'upper left')
plt.tight_layout()
plt.show()




#brincando agora com a regressoa logistica


