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

# track music state
music_playing = False  

# music function
def play_music(filename, loop=-1, volume=0.5):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(loop)   # -1 = infinite loop

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
        fadein()
        first = pygame.image.load('assets/opening/first.png')
        screen.blit(first, (100, 100))
        pygame.display.update()
        pygame.time.delay(3000)
        fadeout()
        second = pygame.image.load('assets/opening/sec.png')
        screen.blit(second, (120, 90))
        pygame.time.delay(3000)
        
        pygame.display.update()
        
        credits = True
    
    return credits



def Opening():  # blit this on the screen only after creds are loaded
    title = pygame.image.load('assets/opening/LOGO.png')
    screen.blit(title, (20, 10))
    pygame.display.update()
    pygame.time.delay(2000)
    start = pygame.image.load('assets/opening/start_nor.png')
    start_rect = start.get_rect(center=(200, 400))
    screen.blit(start, start_rect)
    pygame.display.update()
    return start_rect


def fadein():
    fade_surface = pygame.Surface((800, 600))
    fade_surface.fill((0, 0, 0))
    for alpha in range(255, -1, -5):
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.update()
        clock.tick(60)
   

def fadeout():
    fade_surface = pygame.Surface((800, 600))
    fade_surface.fill((0, 0, 0))
    for alpha in range(0, 255, 5):
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if Starter_menu:
                    print("WAZZZAP")

    if Starter_menu:
        creds()  # OPENING SCREEN (ADD ANIMS)
        if credits:
            screen.fill((0,0,0))
            if not music_playing:   #ONLY ONCE
                play_music('music/SafeZone.mp3')
                music_playing = True
            Opening()

    elif Game:
        screen.fill((0, 0, 0))
        gameinfo()
        screen.blit(player(), (350, 400))
        text()

    pygame.display.update()
    clock.tick(60)
