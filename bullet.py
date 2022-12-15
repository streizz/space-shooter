import pygame.sprite


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, gun):
        '''инициализации пули'''
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 3, 10)
        self.color = 255, 200, 255
        self.speed = 4.5
        self.rect.centerx = gun.rect.centerx
        self.rect.centery = gun.rect.centery - 50
        self.y = float(self.rect.y)

    def move(self):
        '''изменение позиции пули по ординате'''
        self.y -= self.speed
        self.rect.y = self.y

    def render(self):
        '''отрисовка одной пули'''
        self.move()
        pygame.draw.rect(self.screen, self.color, self.rect)