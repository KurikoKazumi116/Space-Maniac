import pygame,time
from sys import exit

pygame.init()
pygame.font.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800,600))

pygame.display.set_caption('SPACE-MANIA')
fonts = pygame.font.Font('assets/Pixeltype.ttf',50)
#screens
Starter_menu = True
beginCut = False
gameLVL1 = False
gameLVL2 = False
game_ending = False
game_over = False

reply = pygame.image.load('assets/')
reply_rect = reply.get_rect(center = (400,300))

FPS = 60
level = 1
lives = 5

player = pygame.image.load('assets/player/0.png')
player_rect = player.get_rect(center = (20,20))
clock = pygame.time.Clock()

CutText = [
    "Evening"
    "Haha. I guess so."
    "..."
    "..."
    "Earth has been taken over."
    "All COMMS will be disconnected."

]

def gameinfo():
    lives_label = fonts.render(f'Lives: {lives}', 1, (255,225,255))
    level_label = fonts.render(f'Level: {level}',1,(255,255,255))
    screen.blit(level_label,(10,10))
    screen.blit(lives_label,(100,100))
while True:
    
    gameinfo()

    
    screen.blit(player, (400,400))
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if reply_rect.collidepoint == (event.pos)
            
    pygame.display.update()
    clock.tick(FPS)
            

