import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
pygame.display.set_caption('SPACE-MANIA')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                

    
    

    clock.tick(60)
    pygame.display.update()
