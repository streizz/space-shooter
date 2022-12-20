import pygame


class Ino(pygame.sprite.Sprite):
    def __init__(self, screen):
        '''инициализации пришельца'''
        super().__init__()
        self.image = pygame.image.load('media/ino.png')
        self.mask = pygame.mask.from_surface(self.image)
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.right = False

    def update(self):
        '''отрисовка пришельца'''
        self.move()
        self.screen.blit(self.image, self.rect)

    def move(self):
        '''изменение позиции пушки'''
        if self.rect.right < self.screen_rect.right:
            self.y += 0.5
        self.rect.y = self.y