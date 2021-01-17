# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 15:58:07 2020

@author: israe
"""

#Implementando o Array ADT no python usando os ctypes

import ctypes

class Array:
    
    def _init__(self, size):
         assert size > 0, "Tamanho do Array deve ser maior que zero > 0"
         self._size = size
         PyArrayType = ctypes.py_object * size
         self._elements = PyArrayType()
         self.clear( None )
    
    def __len__( self ):
        return self._size
    
    def __getitem__( self, index):
        assert index >= 0 and index < len(self), "Array fora do limite"
        
    def __setitem__ (self, index, value):
        assert index >= 0 and index < len(self), "Array fora do limite"
        self._elements[index] = value
        
    def clear(self, value):
        for i in range(len(self)):
            self._elements[i] = value
    
    def __iter__ (self):
        return _ArrayIterator( self._elements )
    
class _ArraIterator:
    
    def __init__(self, theArray):
        self._arrayRef = theArray
        self._curNdx = 0
   
    def __iter__(self):
        return self
    
    def __next__(self):
       if self._curNdx < len(self._arrayRef):
           entry = self._arrayRef[self._curNdx]
           self._curNdx += 1
           return entry
       else:
           raise StopIteration