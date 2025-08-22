import pygame, time
from pygame.locals import *
from sys import exit

pygame.init()
pygame.font.init()
pygame.mixer.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Space-Mania')

fonts = pygame.font.Font('assets/UI/Pixeltype.ttf', 50)

#screens
Starter_menu = True
Game = False
Win = False
Loseanim = False
game_over = False
credits = False

#lazer

#red_laz = pygame.image.load('assets/UI/red_laz.png')


def gameinfo():
    lives_label = fonts.render(f'Lives: {lives}', 1, (255, 225, 255))
    level_label = fonts.render(f'Time: {tme}', 1, (255, 255, 255))
    screen.blit(level_label, (10, 10))
    screen.blit(lives_label, (100, 100))


def player():
    return pygame.image.load('assets/player/Playa.png')


def creds():
    global credits
    if not credits:
        fadeout()
        first = pygame.image.load('assets/opening/first.png')
        screen.blit(first, (100, 100))
        pygame.display.update()
        pygame.time.delay(5000)
        fadeout()
        second = pygame.image.load('assets/opening/sec.png')
        screen.blit(second, (120, 90))
        pygame.display.update()
        pygame.time.delay(5000)
        credits = True
    
    return credits



def Opening():  # blit this on the screen only after creds are loaded
    pygame.mixer.music.load('music/SafeZone.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()
    #title = pygame.image.load('assets/opening/title.png')
    #screen.blit(title, (400, 200))
    pygame.display.update()
    pygame.time.delay(2000)
    start = pygame.image.load('assets/opening/start_nor.png')
    start_rect = start.get_rect(center=(200, 400))
    screen.blit(start, start_rect)
    pygame.display.update()
    return start_rect


def fadein():
    alpha = 0
    fade_speed = 3
    fading_in = True
    while fading_in:
        screen.fill((0, 0, 0))
        alpha += fade_speed
        if alpha >= 255:
            alpha = 255
            fading_in = False
        surface = pygame.Surface((800, 600))
        surface.set_alpha(alpha)
        screen.blit(surface, (0, 0))
        pygame.display.update()
        clock.tick(60)

def fadeout():
    alpha = 255
    fade_speed = 100
    fading_out = True
    while fading_out:
        screen.fill((0, 0, 0))
        alpha -= fade_speed
        if alpha <= 0:
            alpha = 0
            fading_out = False
        surface = pygame.Surface((800, 600))
        surface.set_alpha(alpha)
        screen.blit(surface, (0, 0))
        pygame.display.update()
        clock.tick(60)



def text():
    for i, line in enumerate(CutTexts):
        word = fonts.render(line, 1, (255, 255, 255))
        screen.blit(word, (100, 100 + i * 60))
        pygame.display.update()
        pygame.time.delay(300)
        if i == 6:
            break


#variables
FPS = 60
tme = 120  # IN SECONDS
lives = 5

#IK this is crude XD
a = 'The year is 3020. '
b = 'You are an astronaut on Mars.'
c = 'But, you are losing oxygen fast!'
d = 'Defeat enemy spaceships that get in your way!'
e = 'Grab Yellow orbs to speed up!'
f = 'You have 2 minutes.'
g = 'Press SPACE to begin.'

CutTexts = [a, b, c, d, e, f, g]

#hover mechs
mouse_pos = pygame.mouse.get_pos()

# actual game
start_rect = None  

while True:
    for event in pygame.event.get():  # KEYBINDSSSS
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Starter_menu:
                if event.key == pygame.K_a:
                    print("You pressed A in the starter menu!")

    

    if Starter_menu:
        
        creds()  # OPENING SCREEN (ADD ANIMS)
        if credits:
            screen.fill((0,0,0))
            Opening()

    elif Game:
        
        screen.fill((0, 0, 0))
        gameinfo()
        screen.blit(player(), (350, 400))
        text()

    pygame.display.update()
    clock.tick(FPS)
