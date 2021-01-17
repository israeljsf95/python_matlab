# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 18:34:40 2020

@author: israe
"""

import game_functions as gf
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens  = Group()
    gf.create_fleet(ai_settings, screen, aliens) #criando a frota dos aliens
    #definindo a cor do fundo
    while True:
      gf.check_events(ai_settings, screen, ship, bullets)
      ship.update()
      gf.update_bullets(bullets)
      gf.update_screen(ai_settings, screen, ship, aliens, bullets)



run_game()