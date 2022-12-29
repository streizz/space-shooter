from pygame import *
from btncreator import creator
import json

size = (600, 900)
screen = display.set_mode(size)
init()
font1 = font.SysFont('Copperplate Gothic', 50)
font2 = font.SysFont('Copperplate Gothic', 80)
menu = creator()
menu.clearing()
menu.add_option('Menu ->', lambda: open_menu(), font1)
menu.add_option('exit', lambda: newexit(), font1)
temp = json.load(open('temp.json', 'r'))

def endgame_window(win1):
    score = temp['stats']
    while True:
        for event_ in event.get():
            if event_.type == QUIT:
                exit()
            if event_.type == KEYDOWN:
                if event_.key == K_UP:
                    menu.switch_point(-1)
                elif event_.key == K_DOWN:
                    menu.switch_point(1)
                elif event_.key == K_RIGHT:
                    menu.select()
        if win1 == 1:
            win = font2.render('You won!', True, (255, 255, 255))
            win_rect = win.get_rect()
            win_rect.topleft = (10, 20)
            scores = font1.render(f'Your new best is: {score}', True, (255, 255, 255))
        else:
            win = font2.render('You lost.', True, (255, 255, 255))
            win_rect = win.get_rect()
            win_rect.topleft = (10, 20)
            scores = font1.render(f'Your best is: {score}', True, (255, 255, 255))
        screen.blit(image.load('media/endgame.png').convert_alpha(), (0, 0))
        option_rect = scores.get_rect()
        option_rect.topleft = (10, 300)
        screen.blit(win, win_rect)
        screen.blit(scores, option_rect)
        menu.draw(screen, 10, 400, 50)
        display.flip()

def open_menu():
    import start_menu
    temp['win'] = 0
    temp['stats'] = 0

def newexit():
    temp['win'] = 0
    temp['stats'] = 0
    exit()

endgame_window(temp['win'])