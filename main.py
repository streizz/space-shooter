import pygame
from gun import Gun
from controls import process_events, update_display


def main():
    pygame.init()
    screen = pygame.display.set_mode((1400, 788))
    pygame.display.set_caption('Космический шутер')
    BLACK = (0, 0, 0)
    gun = Gun(screen)

    while True:
        process_events(gun)
        update_display(screen, gun, BLACK)


if __name__ == '__main__':
    main()