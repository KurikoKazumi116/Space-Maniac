import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,600))

pygame.display.set_caption('SPACE-MANIA')

#screens
Starter_menu = True
beginCut = False
gameLVL1 = False
gameLVL2 = False
game_ending = False
game_over = False


player = pygame.image.load('assets/player/0.png')
player_rect = player.get_rect(center = (20,20))
clock = pygame.time.Clock()

class ship(): # make a class so multiple images can have the attributes
    def __init__(self,x,y,color,health = 100): # = sets a base parameter value
        self.x = x
        self.y = y
        self.health = health
        self.color = color
        self.shipimg = None
        self.laserimg = None
        self.lasers = []
        self.cooldown = 0
    def draw(self):
        pygame.draw.rect(screen, (90,90,0), (self.x, self.y,50,50),0)

def main():
    run = True
    FPS = 60
    level = 1
    lives = 5

    def game():
        lives_label = fonts.render(f'Lives: {lives}', 1, (255,225,255))
        level_label = fonts.render(f'Level: {level}',1,(255,255,255))
        screen.blit(level_label,(10,10))
        screen.blit(lives_label,(100,100))
    while True:
        ship.draw(screen)
        game()


        
        fonts = pygame.font.Font('assets/Pixeltype.ttf',50)
        screen.blit(player, (400,400))
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_LEFT:
                    ship.x +=2
                    
                if event.key ==pygame.K_RIGHT:
                    ship.x += 3
            if event.type == pygame.KEYUP:
                if event.key ==pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.left += 20
        if Starter_menu:
            screen.fill(0)


            
        pygame.display.update()
        clock.tick(FPS)
                

