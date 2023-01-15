import pygame
import sys


def process_events(game):
    '''обрабатываем события'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                game.gun.mright = True
            elif event.key == pygame.K_LEFT:
                game.gun.mleft = True
            elif event.key == pygame.K_SPACE:
                game.gun.shooting = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                game.gun.mright = False
            elif event.key == pygame.K_LEFT:
                game.gun.mleft = False
            elif event.key == pygame.K_SPACE:
                game.gun.shooting = False


def update_display(screen, game, background, curlvl):
    screen.fill(background)
    filename = 'media/lvl' + str(curlvl) + 'bg.png'
    screen.blit(pygame.image.load(filename).convert_alpha(), (0, 0))
    game.update()
    pygame.display.flip()
