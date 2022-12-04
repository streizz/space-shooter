import pygame


class Gun:
    def __init__(self, screen):
        '''инициализация пушки'''
        self.screen = screen
        self.image = pygame.image.load('images/playable_ship2.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def render(self):
        '''отображение пушки'''
        self.move()
        self.screen.blit(self.image, self.rect)

    def move(self):
        '''изменение позиции пушки'''
        if self.mright and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1.0
        elif self.mleft and 0 < self.rect.left:
            self.rect.centerx -= 1.0