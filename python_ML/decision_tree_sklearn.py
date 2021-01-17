# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 18:08:05 2020

@author: israe
"""

#Brincando com arvores de decisao no sklearn

from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np
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
X_comb = np.vstack((X_train_std, X_test_std))
y_comb = np.hstack((y_train, y_test))


tree_model = DecisionTreeClassifier(criterion = 'gini', max_depth = 4, 
                                    random_state = 1)
tree_model.fit(X_train_std, y_train)
plot_reg_dec(X_comb, y_comb, classificador = tree_model, test_idx = range(105,150))
plt.xlabel('tamanho da petala')
plt.ylabel('largura da petala')
plt.legend(loc = 'upper left')
plt.show()

#from pydotplus import graph_from_dot_data
#from sklearn.tree import export_graphviz
#
#dot_data = export_graphviz(tree_model, 
#                           filled = True, 
#                           rounded = True, 
#                           class_names = ['Setosa', 'Versicolor', 'Virignica'],
#                           feature_names = ['petal length', 
#                                           'petal width'],
#                            out_file = None)
#graph = graph_from_dot_data(dot_data)
#graph.write_png('tree.png')                           
#




