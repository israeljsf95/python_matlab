# -*- coding: utf-8 -*-
"""
Created on Sun May 17 18:15:45 2020

@author: israe
"""


import numpy as np 


x = np.random.rand(100,1)
y = np.random.rand(100,1)

z = np.max(x+y, 0.) #RELU :) 

x = np.random.random((64, 3, 32, ))
y = np.random.random((32, 10))
z = np.maximum(x, y)
