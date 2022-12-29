import pygame
from bullet import Bullet


class Gun:
    def __init__(self, screen):
        '''инициализация пушки'''
        self.screen = screen
        self.image = pygame.image.load('media/playable_ship2.png')
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.bullets = pygame.sprite.Group()
        self.mright = False
        self.speed = 6.5
        self.shooting = False
        self.mleft = False

    def update(self):
        '''отрисовка пушки'''
        self.move()
        self.screen.blit(self.image, self.rect)

    def move(self):
        '''изменение позиции пушки'''
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += self.speed
        if self.mleft and 0 < self.rect.left:
            self.center -= self.speed
        if self.shooting and len(self.bullets) < 25:
            self.shoot()
        self.rect.centerx = self.center

    def shoot(self):
        '''функция реализует стрельбу пулями bullets'''
        bullet = Bullet(self.screen, self)
        if not pygame.sprite.spritecollideany(bullet, self.bullets):
            self.bullets.add(bullet)