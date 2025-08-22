import pygame,time
from pygame.locals import *
from sys import exit

pygame.init()
pygame.font.init()
pygame.mixer.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Space-Mania')

fonts = pygame.font.Font('assets/UI/Pixeltype.ttf',50)

#screens
Starter_menu = True
Game = False
Win = False
Loseanim = False
game_over = False

#lazer
red_laz = pygame.image.load('assets/UI/')



def gameinfo():
    lives_label = fonts.render(f'Lives: {lives}', 1, (255,225,255))
    level_label = fonts.render(f'Time: {tme}',1,(255,255,255))
    screen.blit(level_label,(10,10))
    screen.blit(lives_label,(100,100))

def player():
    player = pygame.image.load('assets/player/Playa.png')

def creds():
    pygame.image.load()

def Opening(): #blit this on the screen only after creds are loaded
    pygame.mixer.music.load('music/SafeZone.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    title = screen.blit('assets/UI/title.png',(400,200))
    pygame.time.delay(2)
    start = screen.blit('assets/UI/start.png')
    start_rect = start.get_rect(center = ())

def fade():
    screen.fill((0, 0, 0)) 
    screen.set_alpha(int(alpha))
    alpha = 0
    fading_out = True
    fade_speed = 5

    if fading_out:
        alpha += fade_speed 
        if alpha >= 255:
            alpha = 255
            fading_out = False  
        screen.set_alpha(alpha) 

def text():
    value = 0
    for i in CutTexts:
        word = fonts.render([value])
        screen.blit(word,(100,100))
        pygame.time.delay(30)
        value +=1
        if value == 6:
            break
               

    

#variables
FPS = 60
tme = 120 #IN SECONDSSS
lives = 5



#IK this is crude XD
a = 'The year is 3020. '
b = 'You are an astronaut on Mars.'
c = 'But, you are loosing oxygen fast!'
d = 'Defeat enemy spaceships that get in your way!'
e = 'Grab Yellow orbs to speed up!'
f = 'You have 2 minutes.'
g = 'Press SPACE to begin.'

CutTexts = [a,b,c,d,e,f,g]

#hover mechs 
mouse_pos = pygame.mouse.get_pos()

#actual game
while True:
    

    for event in pygame.event.get():#KEYBINDSSSS
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_rect.collidepoint == (event.pos):
                fade()
                Starter_menu = False
                Game  = True

                
                pygame.mixer.Sound()

    if Starter_menu:
        fade() #OPENING SCREEN (ADD ANIMS)
        

    if Game:



    pygame.display.update() 
    clock.tick(FPS)
