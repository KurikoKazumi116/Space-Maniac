import pygame, time
import random
from pygame.locals import *
from sys import exit

pygame.init()
pygame.font.init()
pygame.mixer.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Space-Mania')

fonts = pygame.font.Font('assets/UI/Pixeltype.ttf', 50)
wins = 0
losses = 0
#screens
Starter_menu = True
Game = False
Win = False
Lose = False
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

Value = 6


def gameinfo():
    loca = fonts.render(f'Location: {location}', 1, (255, 225, 255))
    level_label = fonts.render(f'T- {tme} seconds', 1, (255, 255, 255))
    screen.blit(level_label, (10, 10))
    screen.blit(loca, (500, 10))

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
        screen.blit(word, (10, 50 + i * 60))
        pygame.display.update()
        pygame.time.delay(2000)
        if i == 8:
            print("hello")
            space = True
            Starter_menu = False
            
def winscr():
    winbg = pygame.image.load('assets/UI/win.png')
    screen.blit(winbg,(100,0))  
    Wmes = fonts.render('You have reached Earth!',1, (255,255,255))
    screen.blit(Wmes,(90, 100))  
    Restart = fonts.render('Press [R] to reset',1, (255,255,255))
    
    
    screen.blit(Restart,(200, 300))
    
    pygame.time.delay(20)
def losescr():            
    losebg = pygame.image.load('assets/UI/lose.png')
    screen.blit(losebg,(0,0))  
    Lmes = fonts.render('You have sustained too much damage.',1, (255,255,255))
    Restart = fonts.render('Press [R] to reset',1, (255,255,255))
    
    screen.blit(Lmes,(200, 100))
    screen.blit(Restart,(200, 300))
    
    pygame.time.delay(20)
    



bg = pygame.image.load('assets/opening/openingbg.png')
bg_rect = bg.get_rect(center=(200, 200))

player = pygame.image.load('assets/player/Playa.png').convert_alpha()
player_rect = player.get_rect(center=(600, 300))
player_speed = 6

#i need more boolets
bullets = []
bullet_speed = 8
bullet_img = pygame.image.load('assets/player/bullet.png').convert_alpha()
#aster
asteroid_img = pygame.image.load('assets/UI/asteroid.png').convert_alpha()

asteroids = []
asteroid_speed = 5
spawn_timer = 0

music_playing = False

#variables
FPS = 60
tme = 120  # IN SECONDS

#sound effects
clck = pygame.mixer.Sound('music/24.wav')
shoot = pygame.mixer.Sound('music/Fire 4.mp3')
hit = pygame.mixer.Sound('music/Hit 1.mp3')

location = 'Neptune'


#IK this is crude XD
a = 'The year is 3020. '
b = 'You are in the outer-solarsystem when.. '
c = 'An asteroid hits your spaceship!'
d = 'You are loosing oxygen at a rapid rate'
e = 'Avoid and shoot asteroids to get back to Earth!'
f = 'You have T-2 minutes.'
g = 'USE W,S or UP & DOWN arrows to move.'
h = 'USE SPACE to shoot.'
i = 'Press [SPACE] to begin.'

CutTexts = [a, b, c, d, e, f, g, h,i]
last_tick = None
#hover mechs
mouse_pos = pygame.mouse.get_pos()

number = 50
x = 0
start_rect = None
shoot_cooldown = 200  
last_shot = 0          
gam = pygame.image.load('assets/UI/gamespace.png')
start = pygame.image.load('assets/opening/start_nor.png')
title = pygame.image.load('assets/opening/LOGO.png')
# actual game
while True:#KEYBINDSSSS
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            #starter menu functionality
            if event.key == pygame.K_a:
                if Starter_menu:
                    clck.play()
                    music_playing = False
                    print("working")
                    pygame.time.delay(300)
                    fadeout()
                    screen.blit(bg,(30,40))

                    pygame.time.delay(600)
                    Starter_menu = False           
                    if not music_playing:
                        play_music('music/JustAChat.ogg')
                        music_playing = True  
                    text()
                    Starter_menu = False

            elif event.key == pygame.K_SPACE:
                
                if space:
                    clck.play()
                    print("THIS THING WORKDS")
                    Starter_menu = False
                    fadeout()
                    Game = True
                    space = False
                    music_playing = False
                    if not music_playing:
                        play_music('music/OrbitalMania.mp3')
                        music_playing = True 
                 
            elif event.key == pygame.K_r:
                if game_over:
                    clck.play()
                    print("THIS THING WORKs too")
                    Starter_menu = False
                    fadeout()
                    Game = True
                    tme = 120
                   
                    music_playing = False
                    if not music_playing:
                        play_music('music/OrbitalMania.mp3')
                        music_playing = True 
            
    if Starter_menu:
        creds()
          # OPENING SCREEN (ADD ANIMS)

        if credits:
            screen.fill((0, 0, 0))
            if not music_playing:
                play_music('music/SafeZone.mp3')
                music_playing = True 
            screen.blit(bg, bg_rect)
            # Draw start + logo
            
            screen.blit(start, (300, 300))
            
            screen.blit(title, (140, 80))


    elif Game:
        lose = False
        win = False
        bg_width = gam.get_width()
        x -= Value
        if x <= -bg_width:
            x = 0
        pygame.time.delay(20)
        
        screen.blit(gam, (x,0))
        screen.blit(gam, (x + bg_width, 0))
        

        gameinfo()
       
   
        current_time = pygame.time.get_ticks()  # gets milliseconds since pygame.init()
        if last_tick is None:
            last_tick = current_time  # initialize the first time the game starts

       
        if current_time - last_tick >= 1000:  
            tme -= 1        
            last_tick = current_time

        if tme <= 95 and tme > 75:
            location = 'Uranus'
            Value = 8
        elif tme <=75 and tme > 50:
            Value = 8.5
            number = 40
            location = 'Saturn'

        elif tme <= 50 and tme > 35:
            Value = 9
            number = 30
            location = 'Jupiter' 

        elif tme <= 35 and tme > 20:
            Value = 10
            number = 20
            location = 'Mars'

        elif tme <= 20 and tme > 15:
            Value = 11
            number = 15
            location= 'Earth'

           
        elif tme == 0:
            tme = 0
            game = False
            game_over = True
            music_playing = False
            win = True
        #actual gameplay
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            if player_rect.top > 0:
                player_rect.y -= player_speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            if player_rect.bottom < 600:
                player_rect.y += player_speed
            
    
        if keys[pygame.K_SPACE] and current_time - last_shot >= shoot_cooldown:
            shoot.play()
            bullet_rect = bullet_img.get_rect(center=(player_rect.left, player_rect.centery))  
            bullets.append(bullet_rect)
            last_shot = current_time  

        
        for bullet in bullets[:]:
            bullet.x -= bullet_speed  
            if bullet.right < 0:  # off screen
                bullets.remove(bullet)


        spawn_timer += 1
        if spawn_timer > number:  
            asteroid_Y = random.randint(50, 550)  
            asteroid_rect = asteroid_img.get_rect(center=(-20, asteroid_Y)) 
            asteroids.append(asteroid_rect)
            spawn_timer = 0

        for asteroid in asteroids[:]:
            asteroid.x += asteroid_speed  
            if asteroid.left > 800: 
                asteroids.remove(asteroid)


        for bullet in bullets[:]:
            for asteroid in asteroids[:]:
                if bullet.colliderect(asteroid):  
                    hit.play()
                    bullets.remove(bullet)
                    asteroids.remove(asteroid)
                    break  


        for asteroid in asteroids[:]:
            if player_rect.colliderect(asteroid):  
                lose = True
                hit.play()
                print("asteroid hit")
                Game = False
                music_playing = False
                game_over = True
                break

        screen.blit(player, player_rect)  
        for bullet in bullets:
            screen.blit(bullet_img, bullet)  
        for asteroid in asteroids:
            screen.blit(asteroid_img, asteroid)
        

    elif game_over:
        location = 'Neptune'
        for asteroid in asteroids[:]:
            asteroids.remove(asteroid)
        if win:
            wins +=1
            winscr()
            if not music_playing:
                play_music('music/Winnin.mp3')
                music_playing = True 
        elif lose:
            losescr()
            losses +=1
            if not music_playing:
                play_music('music/Lose.mp3')
                music_playing = True 
                

    
        
        

        


    pygame.display.update()
    clock.tick(60)
