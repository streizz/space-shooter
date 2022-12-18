import pygame


def process_events(game):
    '''обрабатываем события'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                game.gun.mright = True
            elif event.key == pygame.K_LEFT:
                game.gun.mleft = True
            elif event.key == pygame.K_SPACE:
                game.gun.shoot()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                game.gun.mright = False
            elif event.key == pygame.K_LEFT:
                game.gun.mleft = False


def update_display(screen, game, background):
    screen.fill(background)
    game.update()
    pygame.display.flip()
