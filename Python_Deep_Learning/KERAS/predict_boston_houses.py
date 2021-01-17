# -*- coding: utf-8 -*-
"""
Created on Thu May 21 00:48:37 2020

@author: israe
"""

from tensorflow.keras.datasets import boston_housing

(train_data, train_label), (test_data, test_label) = boston_housing.load_data()

#pre_processing the data

mean = train_data.mean(axis = 0)
train_data -= mean
std = train_data.std(axis = 0)
train_data /= std

test_data -= mean
test_data /= std

from tensorflow.keras import models
from tensorflow.keras import layers


def build_model():
    model = models.Sequential()
    model.add(layers.Dense(64, activation = 'relu', input_shape = (train_data[1], )))
    model.add(layers.Dense(64, activation = 'relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer = 'rmsprop',
                  loss = 'mse',
                  metrics = ['mae'])
    return model





