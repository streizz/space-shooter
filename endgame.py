from pygame import *
from btncreator import Creator
from importlib import reload
import json
from sys import exit

class End:
    def __init__(self):
        size = (1400, 788)
        self.screen = display.set_mode(size)
        init()
        self.font1 = font.SysFont('Copperplate Gothic', 50)
        self.font2 = font.SysFont('Copperplate Gothic', 80)
        self.menu = Creator()
        self.menu.clearing()
        self.menu.add_option('Menu ->', lambda: self.open_menu(), self.font1)
        self.menu.add_option('exit', lambda: exit(), self.font1)
        self.temp = json.load(open('temp.json', 'r'))
        self.win1 = self.temp['win']
        self.endgame_window()

    def open_menu(self):
        import start_menu
        reload(start_menu)
        exit()

    def endgame_window(self):
        score = self.temp['stats']
        while True:
            for event_ in event.get():
                if event_.type == QUIT:
                    exit()
                if event_.type == KEYDOWN:
                    if event_.key == K_UP:
                        self.menu.switch_point(-1)
                    elif event_.key == K_DOWN:
                        self.menu.switch_point(1)
                    elif event_.key == K_RIGHT:
                        self.menu.select()
            if self.win1 == 1:
                win = self.font2.render('You won!', True, (255, 255, 255))
                win_rect = win.get_rect()
                win_rect.topleft = (10, 20)
                scores = self.font1.render(f'Your new best is: {score}', True, (255, 255, 255))
            else:
                win = self.font2.render('You lost.', True, (255, 255, 255))
                win_rect = win.get_rect()
                win_rect.topleft = (10, 20)
                scores = self.font1.render(f'Your best is: {self.temp["highscore"]}', True, (255, 255, 255))
            self.screen.blit(image.load(self.temp["curbg"]).convert_alpha(), (0, 0))
            option_rect = scores.get_rect()
            option_rect.topleft = (10, 300)
            self.screen.blit(win, win_rect)
            self.screen.blit(scores, option_rect)
            self.menu.draw(self.screen, 10, 400, 50)
            display.flip()

