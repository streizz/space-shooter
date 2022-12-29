import pygame
from game import Game
from stats import Stats
from controls import process_events, update_display


class start_game:
    def __init__(self):
        self.screen = pygame.display.set_mode((600, 900))
    def main(self, curlvl):
        pygame.init()
        pygame.display.set_caption('Космический шутер')
        BLACK = (0, 0, 0)
        clock = pygame.time.Clock()
        fps = 100
        self.game = Game(self.screen, curlvl)
        while self.game.guns_count_life:
            process_events(self.game)
            update_display(self.screen, self.game, BLACK, curlvl)
            clock.tick(fps)
#заебал, закомиться уже

if __name__ == '__main__':
    start_game.main()