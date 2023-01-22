from pygame import *
from btncreator import Creator
import json
from main import start_game
from sys import exit

init()

size = (1400, 788)

screen = display.set_mode(size)

skin_changing = False

ship_upgrade1 = False

levellisting = False

scoreissue = False

charinfo = {}

skins = ['ship1.png', 'ship2.png', 'ship3.png']

levelmaps = ['media/lvl1bg.png', 'media/lvl2bg.png', 'media/lvl3bg.png']

fontcreds = font.Font('copperplategothic_bold.ttf', 30)
font = font.Font('copperplategothic_bold.ttf', 50)

bg = image.load("media/frames_start_menu/f1 (1).gif").convert_alpha()

menu = Creator()


def ship_upgrade():
    menu.clearing()

    global ship_upgrade1

    ship_upgrade1 = True

    with open('spaceship.json', 'r', encoding='utf-8') as j:
        global charinfo

        charinfo = json.load(j)
        global counter
        counter = charinfo['counterskin']

    menu.add_option(
        f'Upgrade ship > Current level : {charinfo["curlevel"]}', lambda: charupgrade(), font)
    menu.add_option('Change Ship', lambda: skin_change(), font)
    menu.add_option(
        f'Level 1 record : {charinfo["currecordlvl1"]}', False, font)
    menu.add_option(
        f'Level 2 record : {charinfo["currecordlvl2"]}', False, font)
    menu.add_option(
        f'Level 3 record : {charinfo["currecordlvl3"]}', False, font)
    menu.add_option(f'Back >', lambda: main_menu(), font)


def charupgrade():
    if charinfo['currecordlvl1'] >= 13000 and charinfo['curlevel'] == 1:
        with open('spaceship.json', 'w', encoding='utf-8') as j:
            charinfo['curlevel'] += 1
            json.dump(charinfo, j)
    elif charinfo['currecordlvl2'] >= 13000 and charinfo['curlevel'] == 2:
        with open('spaceship.json', 'w', encoding='utf-8') as j:
            charinfo['curlevel'] += 1
            json.dump(charinfo, j)
    elif charinfo['currecordlvl3'] >= 13000 and charinfo['curlevel'] == 3:
        with open('spaceship.json', 'w', encoding='utf-8') as j:
            charinfo['curlevel'] += 1
            json.dump(charinfo, j)
    else:
        global error1, error_rect, scoreissue
        error1 = font.render(f'Error! Try better on level {charinfo["curlevel"]}.', True, (255, 255, 255))
        error_rect = error1.get_rect()
        scoreissue = True

    ship_upgrade()


def start_lvl(lvl):
    start_game(lvl)


def skin_change():
    global skin_changing

    skin_changing = True

    ship_upgrade()


def lvllist():

    menu.clearing()

    screen.blit(image.load(
        levelmaps[0]).convert_alpha(), (0, 0))

    global levellisting

    levellisting = True

    menu.add_option('Level 1 >', lambda: start_lvl(lvl=1), font)
    menu.add_option('Level 2 >', lambda: start_lvl(lvl=2), font)
    menu.add_option('Level 3 >', lambda: start_lvl(lvl=3), font)
    menu.add_option('Back >', lambda: main_menu(), font)

def main_menu():
    menu.clearing()
    global ship_upgrade1, levellisting, counter

    ship_upgrade1 = False

    levellisting = False

    counter = 0

    menu.add_option('Level list >', lambda: lvllist(), font)
    menu.add_option('Upgrade spaceship >', lambda: ship_upgrade(), font)
    menu.add_option('Quit >', lambda: exit(), font)


main_menu()


creds = [fontcreds.render('Credits:', True, (255, 255, 255)), fontcreds.render(
    'Nikita Kananadze', True, (255, 255, 255)), fontcreds.render('Anna Lobanova', True, (255, 255, 255))]

background_index = 1
background_time = 0
background_delay = 85

clock = time.Clock()
while True:
    for event_ in event.get():
        if event_.type == QUIT:
            exit()
        if event_.type == KEYDOWN:
            if not skin_changing and not levellisting:
                if event_.key == K_UP:
                    menu.switch_point(-1)
                elif event_.key == K_DOWN:
                    menu.switch_point(1)
                elif event_.key == K_RIGHT:
                    menu.select()
            elif skin_changing:
                if event_.key == K_RIGHT:
                    counter += 1
                if event_.key == K_LEFT:
                    counter -= 1
                if event_.key == K_UP:
                    with open('spaceship.json', 'w', encoding='utf-8') as j:
                        charinfo['curskin'] = f'media/playable_{skins[counter % 3]}'
                        charinfo['counterskin'] = counter % 3
                        json.dump(charinfo, j)
                    skin_changing = False
            elif levellisting:
                if event_.key == K_UP:
                    menu.switch_point(-1)
                    counter -= 1
                elif event_.key == K_DOWN:
                    menu.switch_point(1)
                    counter += 1
                elif event_.key == K_RIGHT:
                    menu.select()

    time_now = time.get_ticks()

    if not ship_upgrade1 and not levellisting:
        if time_now > background_time + background_delay:
            background_time = time_now
            background_index += 1
            if background_index > 45:
                background_index = 1

            screen.blit(image.load(
                f"media/frames_start_menu/f1 ({int(background_index)}).gif").convert_alpha(), (0, 0))

        for i, option in enumerate(creds):
            option_rect = option.get_rect()
            option_rect.topleft = (1100, 660 + i * 40)
            screen.blit(option, option_rect)

    elif ship_upgrade1:
        screen.blit(image.load(
            f"media/background_upgrading.png").convert_alpha(), (0, 0))
        screen.blit(image.load(
            f'media/{skins[counter % 3]}').convert_alpha(), (900, 450))
        if scoreissue:
            error_rect.topleft = (20, 700)
            screen.blit(error1, error_rect)

    elif levellisting:
        if counter > 2:
            screen.blit(image.load(
                levelmaps[2]).convert_alpha(), (0, 0))
            counter = 3
        elif counter <= 0:
            screen.blit(image.load(
                levelmaps[0]).convert_alpha(), (0, 0))
            counter = 0
        elif counter == 1 or counter == 2:
            screen.blit(image.load(
                levelmaps[counter]).convert_alpha(), (0, 0))

    if not skin_changing:
        menu.draw(screen, 100, 100, 75)

    else:
        menu.draw(screen, 100, 100, 75)
        screen.blit(image.load('media/left_icon.png'), (840, 600))
        screen.blit(image.load('media/right_icon.png'), (1200, 600))

    display.flip()

quit()
