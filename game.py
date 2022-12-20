import pygame
from gun import Gun
import time
from ino import Ino
from score import Score
from stats import Stats


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.gun = Gun(screen)
        self.inos = pygame.sprite.Group()
        self.stats = Stats()
        self.score = Score(screen, self.stats)
        self.create_army()
        self.guns_count_life = 3
        self.life_image = pygame.image.load('images/life.png')

    def check_inos(self):
        for ino in self.inos.sprites():
            if ino.rect.bottom > self.screen.get_rect().bottom:
                return False
        return True

    def check_on_restart(self):
        if pygame.sprite.spritecollideany(self.gun, self.inos) or not self.check_inos():
            self.guns_count_life -= 1
            return True
        elif not self.inos:
            return True

    def show_life(self):
        life_rect = self.life_image.get_rect()
        for life_number in range(1, self.guns_count_life + 1):
            x = 15 + life_number * life_rect.width
            self.screen.blit(self.life_image, (x, 20))

    def update(self):
        self.show_life()
        self.stats.update_high_score()
        self.score.render()
        if self.check_on_restart():
            self.restart_game()
            time.sleep(1)
            return
        self.gun.update()
        self.inos.update()
        for bullet in self.gun.bullets.sprites().copy():
            bullet.update()
            if bullet.rect.bottom <= 0:
                self.gun.bullets.remove(bullet)
        collisions = pygame.sprite.groupcollide(self.gun.bullets, self.inos, True, True)
        self.stats.score += len(collisions) * 100

    def restart_game(self):
        if self.guns_count_life == 0:
            exit()
        self.inos.empty()
        self.gun = Gun(self.screen)
        self.create_army()

    def create_army(self):
        ino = Ino(self.screen)
        ino_width = ino.rect.width
        count_ino_on_row = int((self.screen.get_width() - ino_width) // ino_width)
        for ino_number in range(count_ino_on_row):
            ino = Ino(self.screen)
            ino.x = ino_width // 2 + ino_number * ino_width
            ino.rect.x = ino.x
            self.inos.add(ino)