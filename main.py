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
beginCut = False
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

def Opening():
    pygame.mixer.music.load('music/SafeZone.ogg')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    screen.blit()

#variables
FPS = 60
tme = 120 #IN SECONDSSS
lives = 5
Val = 0


#IK this is crude XD
a = 'The year is 3020. '
b = 'You are an astronaut on Mars.'
c = 'But, you are loosing oxygen fast!'
d = 'Defeat enemy spaceships that get in your way!'
e = 'Grab Yellow orbs to speed up!'
f = 'You have 2 minutes.'
g = 'Press SPACE to begin.'


CutTexts = [a,b,c,d,e,f,g]


while True:
    pygame.display.update() 
    clock.tick(FPS)

    if Starter_menu: #OPENING SCREEN (ADD ANIMS + HOVER MECHS)
        Opening()

        
    
    for event in pygame.event.get():#KEYBINDSSSS
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if reply_rect.collidepoint == (event.pos):
                Val += 1
                pygame.mixer.Sound()
