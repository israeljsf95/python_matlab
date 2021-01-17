# -*- coding: utf-8 -*-
"""
Created on Sun May 17 22:50:30 2020

@author: israe
"""

from tensorflow.keras.datasets import imdb


(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words = 10000)

import numpy as np

def vectorize_sequences(sequences, dimension = 10000):
    results = np.zeros((len(sequences), dimension))
    for i,sequence in enumerate(sequences):
        results[i, sequence] = 1
    return results

x_train = vectorize_sequences(train_data)
x_test = vectorize_sequences(test_data)


y_train = np.asarray(train_labels).astype('float32')
y_test = np.asarray(test_labels).astype('float32')


from tensorflow.keras import models, layers, optimizers, losses, metrics


model = models.Sequential()
model.add(layers.Dense(16, activation = 'relu', input_shape = (x_train.shape[1], )))
model.add(layers.Dense(32, activation = 'relu'))
model.add(layers.Dense(64, activation = 'relu'))
model.add(layers.Dense(1, activation = 'sigmoid'))

eta = 0.001
#modo normal
#model.compile(optimizer = optimizers.RMSprop(lr = eta),
#              loss = 'binary_crossentropy',
#              metrics = ['accuracy'])

#modo customizado

model.compile(optimizer = optimizers.RMSprop(lr = 0.001),
              loss = losses.binary_crossentropy,
              metrics = [metrics.binary_accuracy])

x_val = x_train[:10000]
partial_x_train = x_train[10000:]
y_val = y_train[:10000]
partial_y_train = y_train[10000:]

#treinamento com validation
history = model.fit(partial_x_train, 
                    partial_y_train,
                    epochs = 4,
                    batch_size = 512,
                    validation_data = (x_val, y_val))
history_dict = history.history
history_dict.keys()

results = model.evaluate(x_test, y_test)
print(results)



#parte boa -> plotar os graficuzinho
import matplotlib.pyplot as plt

loss_values = history_dict['loss']
val_loss_values = history_dict['val_loss']
epochs = range(1, len(loss_values) + 1)

plt.subplot(2,1,1)
plt.plot(epochs, loss_values, 'bo', label = 'Training_loss')
plt.plot(epochs, val_loss_values, 'b', label = 'Validation_loss')
plt.title('Training and Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()


acc_values = history_dict['binary_accuracy']
val_acc_values = history_dict['val_binary_accuracy']

plt.subplot(2,1,2)
plt.plot(epochs, acc_values, 'bo', label = 'Training_Accuracy')
plt.plot(epochs, val_acc_values, 'b', label = 'Validation_Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

np.round(model.predict(x_test[:10]))





