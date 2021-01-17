# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 14:21:53 2020

@author: israe

Script contendo um modelo  de Regressao logistica adaptado ao dataset
"""

import numpy as np

def sigmoid(z):
    """
    Funcao que recebe uma entrada vetorial e retorna a aplicacao da funcao 
    sigmoid em cada uma dessas entradas
    """
    return 1/(1 + np.exp(-z))


def propagate(w, b, X, Y):
    """
    Funcao que propaga, no sentido de fluxo de informacao das redes neurais, os
    dados armazenados na matriz X e gera a saida Y
    """    
    m = X.shape[1]
    A = sigmoid(np.dot(w.T, X) + b)
    cost = (-1/m)*np.sum(Y*np.log(A)) + (np.sum((1-Y)*np.log(1-A)))
    
    dw = (1/m)*np.dot(X, (A-Y).T)
    db = (1/m)*np.sum(A-Y)
    
    grads ={"dw": dw,
            "db": db}
    return grads, cost

def optimize(w, b, X, Y, num_iterations = 1500, learning_rate = 0.01, print_cost = False):
    """
    Processo de otimizacao através do algoritmo: Descida do Gradiente, para ajustar
    os pesos e limiar (w e b)
    """
    
    costs = []
    
    for i in range(num_iterations):
        grads, cost = propagate(w, b, X, Y)
        dw = grads["dw"]
        db = grads["db"]
        w = w - learning_rate*dw
        b = b - learning_rate*db
        
        if i%100 == 0:
            costs.append(cost)
            
        if print_cost and i%100 == 0:
            print("Cost after iteration {}: {%.6f}".format(i, cost))
    
    params = {"w": w,
              "b": b}
    grads = {"dw": dw,
             "db": db}
    return params, grads, costs
    
def predict(w, b, X):
    
    A = sigmoid(np.dot(w.t, X) + b)
    Y_prediction = 1.*(A > 0.5)
    return Y_prediction

def model(X_train, Y_train, X_test, Y_test, num_iter = 1500, lr = 0.5, print_cost = False):
    
    w,b = (np.zeros((X_train.shape[0], 1)), 0)
    parameters, grads, costs = optimize(w, b, X_train, Y_train, num_iter, lr, print_cost)
    w = parameters["w"]
    b = parameters["b"]
    
    Y_prediction_test = predict(w, b, X_test)
    Y_prediction_train = predict(w, b, X_train)
    
    print("Accuracy Training Set: {%.4f}".format(100 - np.mean(np.abs(Y_prediction_train - Y_train))*100))
    print("Accuracy Test Set: {%.4f}".format(100 - np.mean(np.abs(Y_prediction_test - Y_test))*100))
    
    d = {"costs": costs,
         "Y_prediction_test": Y_prediction_test,
         "Y_prediction_train": Y_prediction_train,
         "w": w,
         "b": b,
         "learning_rate": lr,
         "num_iterations": num_iter}
    
    return d
    
    
    