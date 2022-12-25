import pygame
from game import Game
from controls import process_events, update_display

class start_game:
    def main(curlvl):
        pygame.init()
        screen = pygame.display.set_mode((1400, 700))
        pygame.display.set_caption('Космический шутер')
        BLACK = (0, 0, 0)
        clock = pygame.time.Clock()
        fps = 100
        game = Game(screen, curlvl)
        while True:
            process_events(game)
            update_display(screen, game, BLACK, curlvl)
            clock.tick(fps)


if __name__ == '__main__':
    start_game.main()