# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 18:45:34 2020

@author: israe
"""

class Settings():
    
    def __init__(self):
        #Configuracao de Tela
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (230,230,230)
        #Configuracao de Navio
        self.ship_speed_factor = 4
        #Configuracao da Bala
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 3
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 6