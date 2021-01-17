# -*- coding: utf-8 -*-
"""
Created on Sun May 17 20:06:18 2020

@author: israe
"""

from tensorflow.keras import layers, models


seq_model = models.Sequential()
seq_model.add(layers.Dense(32, input_shape = (784, )))
#Nocao de implementacao, as camadas de baixo herdam o shape da camada imediata
#mente anterior
seq_modelo.add(layers.Dense(32))


#func_models

input_tensor = layers.Input(shape = (784, ) )
x = layers.Dense(32, activation = 'relu')(input_tensor)
output_tensor = layers.Dense(10, activation = 'softmax')(x)

func_model = models.Model(inputs = input_tensor, outputs = output_tensor)

