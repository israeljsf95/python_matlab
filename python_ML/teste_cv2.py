# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 12:47:22 2020

@author: israe
"""


import cv2

# Carregando uma imagem com opencp
img = cv2.imread('mandrill.png',1)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()