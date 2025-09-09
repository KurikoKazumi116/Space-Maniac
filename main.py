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
space = False
# track music state
music_playing = False  

# music function
def play_music(filename,vol = 0.5,loop = -1):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.set_volume(vol)
    pygame.mixer.music.play(loop)   # -1 !!!

#lazer

#red_laz = pygame.image.load('assets/UI/red_laz.png')


def gameinfo():
    lives_label = fonts.render(f'Location: {location}', 1, (255, 225, 255))
    level_label = fonts.render(f'T- {tme} seconds', 1, (255, 255, 255))
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
        
        
        pygame.display.update()
        
        credits = True
    
    return credits

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
    global space
    global Starter_menu
    for i, line in enumerate(CutTexts):
        word = fonts.render(line, 1, (255, 255, 255))
        screen.blit(word, (20, 100 + i * 60))
        pygame.display.update()
        pygame.time.delay(2000)
        if i == 7:
            print("hello")
            space = True
            Starter_menu = False
            
            


bg = pygame.image.load('assets/opening/openingbg.png')
bg_rect = bg.get_rect(center=(200, 200))


moving_down = True   # directions 
music_playing = False

#variables
FPS = 60
tme = 120  # IN SECONDS

location = 'Neptune'


#IK this is crude XD
a = 'The year is 3020. '
b = 'You are doing research.. '
c = 'in the outer solar system, when...'
d = 'An asteroid hits your spaceship!'
e = 'You are loosing oxygen at a rapid rate'
f = 'Avoid and shoot asteroids to get back to Earth!'
g = 'You have T-2 minutes.'
h = '     Press SPACE to begin.'

CutTexts = [a, b, c, d, e, f, g, h]

#hover mechs
mouse_pos = pygame.mouse.get_pos()

# actual game
start_rect = None

#KEYBINDSSSS
while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if Starter_menu:
                    clck = pygame.mixer.Sound('music/24.wav')
                    clck.play()
                    music_playing = False
                    print("working")
                    
                    pygame.time.delay(300)
                    fadeout()
                    screen.fill('black')
                    pygame.time.delay(600)
                    Starter_menu = False
                    
                    if not music_playing:
                        play_music('music/JustAChat.ogg')
                        music_playing = True  
                    text()
                    Starter_menu = False

            if event.key == pygame.K_SPACE:

                if space:
                    print("THIS THING WORKDS")
                    Starter_menu = False
                    pygame.time.delay(20)
                    fadeout()
                    
                    
                    Game = True
    
    if Starter_menu:
        creds()
          # OPENING SCREEN (ADD ANIMS)

        if credits:
            screen.fill((0, 0, 0))

            # Play music only once
            if not music_playing:
                play_music('music/SafeZone.mp3')
                music_playing = True
            screen.blit(bg, bg_rect)
            # Draw start + logo
            start = pygame.image.load('assets/opening/start_nor.png')
            screen.blit(start, (300, 300))
            title = pygame.image.load('assets/opening/LOGO.png')
            screen.blit(title, (140, 80))


    elif Game:
        pygame.time.delay(20)
        screen.fill((0, 0, 0))
        gameinfo()
        if tme <= 120:
            pygame.time.delay(1000)
            tme -= 1
        elif tme <=0:
            tme = 0
            game = False
            game_over = True
        screen.blit(player(), (350, 400))
        
    elif game_over:
        game_over()


    pygame.display.update()
    clock.tick(60)
