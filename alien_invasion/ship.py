# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 19:02:35 2020

@author: israe
"""
import pygame


class Ship():
    
    #metodo para iniciar a nave e definir sua posicao inicial
    def __init__(self, ai_settings, screen):
        self.ai_settings = ai_settings
        self.screen = screen 
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()#O pygame permite trabalhar elementos de jogos como retangulos
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False
        
    #Desenha a espaçonave em sua posicao atual
    def blitme(self): 
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        
        
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        
        self.rect.centerx = self.center
        
        
        