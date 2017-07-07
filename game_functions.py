#-*- coding:utf-8 -*-
import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #创造一颗子弹 并将其加入编组bullets
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():  # 监听事件
        if event.type == pygame.QUIT:
            # 退出
            sys.exit()
        elif event.type == pygame.KEYDOWN:#按键为KEYDOWN事件
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets):
    screen.fill(ai_settings.bg_color)  # 填充屏幕
    for bullet in bullets.sprites():#返回所有bullet的列表
        bullet.draw_bullet()
    ship.blitme()  # 将图像绘制到特定位置

    pygame.display.flip()  # 更新屏幕