import pygame

from gun import Gun
from ino import Ino


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.gun = Gun(screen)
        self.inos = pygame.sprite.Group()
        self.create_army()

    def render(self):
        self.gun.render()
        for ino in self.inos.sprites():
            ino.render()
        for bullet in self.gun.bullets.sprites().copy():
            bullet.render()
            if bullet.rect.bottom <= 0:
                self.gun.bullets.remove(bullet)
        pygame.sprite.groupcollide(self.gun.bullets, self.inos, True, True)

    def create_army(self):
        ino = Ino(self.screen)
        ino_width = ino.rect.width
        count_ino_on_row = (self.screen.get_width() - 2 * ino_width) // ino_width
        for ino_number in range(count_ino_on_row):
            ino = Ino(self.screen)
            ino.x = ino_width + ino_number * ino_width
            ino.rect.x = ino.x
            self.inos.add(ino)

