#-*- coding:utf-8 -*-
import pygame
from settings import Settings
from ship import Ship
from aliens import Alien
import game_functions as gf
from pygame.sprite import Group

def run():
    pygame.init()#初始化
    ai_settings = Settings()#实例化
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(screen, ai_settings)

    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, aliens, ship)

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, bullets, aliens)

run()
