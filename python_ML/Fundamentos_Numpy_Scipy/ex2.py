# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 12:14:07 2020

@author: israe
Brincando com o numpy e o Pandas
"""


import pandas as pd

import numpy as np


print('Pandas Series sem indice definido: ')
s1 = pd.Series([12,-4,7,9])
print(s1)

print('Pandas Series com indice definido: ')
s2 = pd.Series([12,-4,7,9], index = ['a','b','c','d'])
print(s2)

#pegando os valores e os indices

print('Imprimindo os valores em s1: \n', s1.values)
print('Imprimindo os idxs em s1: \n', s1.index)


print('Imprimindo os valores em s2: \n', s2.values)
print('Imprimindo os idxs em s2: \n', s2.index)

#Podemos acessar os elementos pelo valor no indice ou pelo indice do array dos valores

#Aplicando operacoes matematicas nos Pandas Series

print(np.log(s2))

serd = pd.Series([1, 0, 2, 1, 2, 3], index = ['white','white','blue','green','green','yellow'])

print(serd)


print('Imprimindo os valores unicos em serd: ', serd.unique())
print('Imprimindo e contando os valores unicos em serd: ', serd.value_counts())


#Tratando dos avlaores numericos que nao podem ser tratados numericamente


s3 = pd.Series([5,-3, -2, np.NaN, 14, 15, np.NaN])
print('S3: \n', s3)

print('Imprimindo se S3 é null: \n',s3.isnull())
print('Imprimindo se S3 não é Null: \n', s3.notnull())

print('Imprimindo os valores que não são Nan em s3: \n', s3[s3.notnull()])

#Nao seria estranho criar uma serie partindo da estrutura dicionarios no python
#Que negocio massa 
dd = {'red': 2000, 'blue': 1000, 'yellow': 500, 'cian': 1200,'green': 120}

ssdd = pd.Series(dd)
print(ssdd)

colors = ['red','blue','yellow','cian','green','purple','orange']
ssdd = pd.Series(dd, index = colors)
print(ssdd)



#Aqui finalizamos os series
#Agora vamos perceber um pouco as coisinhas referentes a estrutura dataframe
#muito mais usada para validar as coisas do ponot de vista de multiplas dimensoes

data = {'cor':['azul', 'verde', 'amarelo', 'vermelho','branco'],
        'objeto':['bola', 'caneta',  'lapis', 'papel', 'caneca'],
        'preco':[1.2, 1.0, 0.6, 0.9, 1.7]}

# Ou seja, é como se o frame fosse um deicionario em que cada valor é uma lista 
frame= pd.DataFrame(data)
print(frame)

frame2 = pd.DataFrame(data, columns = ['objeto','preco'])
print(frame2)

frame3 = pd.DataFrame(data, index = ['one','two','three','four','five'])
print(frame3)

frame4 = pd.DataFrame(np.arange(16).reshape((4,4)), 
                      index = ['vermelho','azul','amarelo','branco'],
                      columns = ['bola','caneta','lapis','papel'])

print(frame4)

print(frame.columns)

#escolho qual coluna sera mostrada, ou visualizada
print(frame4.caneta)

#escolho qual linha sera mostrada, ou visualizada
print(frame4.loc[['vermelho','azul']])
frame4.index.name = 'id'
frame4.columns.name = 'produto'
print(frame4)

#adicionando uma nova coluna

frame4['nova'] = np.random.random_integers(1,10, size = (4,1))
print(frame4)




