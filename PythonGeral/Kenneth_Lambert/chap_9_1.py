# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 13:28:41 2020

@author: israe
"""

class student(object):
    
    #construtor da classe
    def __init__(self, nome, numero):
        self.nome = nome
        self.scores = []
        for cont in range(numero):
            self.scores.append(0)
    
    def get_Nome(self):
        return self.nome
    
    def set_Score(self, i, score):
        self.scores[i-1] = score
    
    def get_Score(self, i):
        return self.scores[i-1]
    
    def get_Average(self):
        return sum(self.scores)/len(self.scores)
    
    def get_High_Score(self):
        return max(self.scores)
    
    def get_Min_Score(self):
        return min(self.scores)
    
    def __str__(self):
        return "Name: " + self.nome + "\nScores: " + " ".join(map(str, self.scores))