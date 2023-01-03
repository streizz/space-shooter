import pygame
from game import Game
from controls import process_events, update_display


def start_game(curlvl):
    pygame.init()
    pygame.display.set_caption('Космический шутер')
    screen = pygame.display.set_mode((1400, 788))
    BLACK = (0, 0, 0)
    clock = pygame.time.Clock()
    fps = 100
    game = Game(screen, curlvl)
    while game.guns_count_life:
        process_events(game)
        update_display(screen, game, BLACK, curlvl)
        clock.tick(fps)

if __name__ == '__main__':
    start_game(1)