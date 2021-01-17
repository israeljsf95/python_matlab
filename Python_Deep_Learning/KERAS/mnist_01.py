# -*- coding: utf-8 -*-
"""
Created on Sun May 17 17:14:47 2020

@author: israe
"""

from tensorflow.keras.datasets import mnist


(train_images, train_labels), (test_images, test_labels) = mnist.load_data()


from tensorflow.keras import models
from tensorflow.keras import layers

#Adicionando camadas sequencialmente
rede = models.Sequential()
rede.add(layers.Dense(512, activation = 'relu', input_shape = (28*28, )))
rede.add(layers.Dense(1024, activation = 'relu'))
rede.add(layers.Dense(10, activation = 'softmax'))

rede.compile(optimizer = 'rmsprop',
             loss = 'categorical_crossentropy',
             metrics = ['accuracy'])

train_images = train_images.reshape((train_images.shape[0], train_images.shape[1]*train_images.shape[2]))
train_images = train_images.astype('float32') / 255


test_images = test_images.reshape((test_images.shape[0], test_images.shape[1]*test_images.shape[2]))
test_images = test_images.astype('float32') / 255


from tensorflow.keras.utils import to_categorical

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

rede.fit(train_images, train_labels, epochs = 2, batch_size = 32)


#avaliando o modelo
test_loss, test_acc = rede.evaluate(test_images, test_labels)
print('Precisao no conjunto de Teste: {}'.format(test_acc))








