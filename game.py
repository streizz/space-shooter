from gun import Gun


class Game:
    def __init__(self, screen):
        self.gun = Gun(screen)

    def render(self):
        self.gun.render()
        for bullet in self.gun.bullets.sprites().copy():
            bullet.render()
            if bullet.rect.bottom <= 0:
                self.gun.bullets.remove(bullet)
