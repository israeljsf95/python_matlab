# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 15:50:05 2020

@author: israe
"""


import os
import numpy as np
import matplotlib.pyplot as plt


os.chdir('D:\\Bibliotecas_Usuario\\Documentos\\Documentos\\UFS\\Estudo_de_Computação\\python_matlab\python_ML\data')
data = np.genfromtxt("web_traffic.tsv", delimiter = "\t")
print(data.shape)

x = data[:,0]
y = data[:,1]

#tratando os valores que sao Nan
x = x[~np.isnan(y)]
y = y[~np.isnan(y)]
print(f'X_shape: {x.shape} \nY_shape: {y.shape} ')


def plot_web_traffic(x, y, models = None):
    plt.figure(figsize = (12,6))
    plt.scatter(x, y, s =10)
    plt.title("Web traffic over the last month")
    
    plt.xlabel("Tempo")
    plt.ylabel("Hits/hora")
    plt.xticks ([w*7*24 for w in range(5)],['semana %i' %(w+1) for w in range(5)])
    
    if models:
        colors = ['g', 'k', 'r', 'm', 'b']
        linestyles = ['-', '-.', '--', ':', '-']
        
        mx = np.linspace(0, x[-1], 1000)
        for model, style, color in zip(models, linestyles, colors):
            plt.plot(mx, model(mx), ls = style, lw = 2, c = color)
        
        plt.legend(["d = %i" % m.order for m in models], loc = "upper left")

    plt.autoscale(tight = True)
    plt.grid()


def eqm(f, x, y):
    return np.mean((f(x)-y)**2)

#brincando com o modelo 
f1 = np.polyfit(x, y, 1)
f2 = np.polyfit(x, y, 2)
f3 = np.polyfit(x, y, 50)
print("Parametros Encontrados M1: %s" %(f1))    
print("Parametros Encontrados M2: %s" %(f2))    
print("Parametros Encontrados M3: %s" %(f3))    


#avaliando o modelo
f_m1 = np.poly1d(f1)
f_m2 = np.poly1d(f2)
f_m3 = np.poly1d(f3)
print(f"EQM M1: {eqm(f_m1, x, y): .2f}")
print(f"EQM M2: {eqm(f_m2, x, y): .2f}")
print(f"EQM M3: {eqm(f_m3, x, y): .2f}")


plot_web_traffic(x, y, [f_m1, f_m2, f_m3])    














