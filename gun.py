import pygame
from bullet import Bullet


class Gun:
    def __init__(self, screen):
        '''инициализация пушки'''
        self.screen = screen
        self.image = pygame.image.load('images/playable_ship2.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.bullets = pygame.sprite.Group()
        self.mright = False
        self.mleft = False

    def update(self):
        '''отрисовка пушки'''
        self.move()
        self.screen.blit(self.image, self.rect)

    def move(self):
        '''изменение позиции пушки'''
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 2.5
        if self.mleft and 0 < self.rect.left:
            self.center -= 2.5
        self.rect.centerx = self.center

    def shoot(self):
        '''функция реализует стрельбу пулями bullets'''
        bullet = Bullet(self.screen, self)
        self.bullets.add(bullet)