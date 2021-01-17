# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 21:57:07 2020

@author: israe
"""
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)