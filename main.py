import pygame,time
from sys import exit

pygame.init()
pygame.font.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800,600))

pygame.display.set_caption('SPACE-MANIA')
fonts = pygame.font.Font('assets/UI/Pixeltype.ttf',50)
#screens
Starter_menu = True
beginCut = False
gameLVL1 = False
gameLVL2 = False
game_ending = False
game_over = False

reply = pygame.image.load('assets/UI/REPLY.png')
reply_rect = reply.get_rect(center = (400,300))
loc = pygame.image.load('assets/UI/LOCATOR.png')

def chatUI():
    screen.blit(reply,reply_rect)
    screen.blit(loc, (400,44))
    pygame.mixer.music.load('music/JustAChat.ogg')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
def chat():
    list = 0
    for i in range (0,5):
        fonts.render(CutTexts[int(list)], 1, 'green')
        time.sleep(3)
        list += 1

def gameinfo():
    lives_label = fonts.render(f'Lives: {lives}', 1, (255,225,255))
    level_label = fonts.render(f'Level: {level}',1,(255,255,255))
    screen.blit(level_label,(10,10))
    screen.blit(lives_label,(100,100))


#variables
FPS = 60
level = 1
lives = 5

player = pygame.image.load('assets/player/0.png')
player_rect = player.get_rect(center = (20,20))
clock = pygame.time.Clock()

CutTexts = [
    "Evening" #0
    "Haha. I guess so." #1
    "..." #2
    "..." #3
    "Earth has been taken over." #4
    "All COMMS will be disconnected." #5

]


while True:
    if Starter_menu: #OPENING SCREEN (ADD ANIMS + HOVER MECHS)
        
    
    
    
    
    
    
    
    #KEYBINDSSSS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if reply_rect.collidepoint == (event.pos):
                if beginCut:   
    pygame.display.update()
    clock.tick(FPS)
            

