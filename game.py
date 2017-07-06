#-*- coding:utf-8 -*-
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run():
    pygame.init()#初始化
    ai_settings = Settings()#实例化
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(screen, ai_settings)

    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(screen, ai_settings, ship)

run()
