# Import the pygame modules
from pickle import NONE
from turtle import Screen, window_height
import pygame
from pygame import *
import time
import math

pygame.mixer.init()

# Import pygame.locals for easier access to key coordinates
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_RALT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_w,
    K_a,
    K_s,
    K_d,
    K_LALT
)

# Set sounds and music
BlasterNoise=pygame.mixer.Sound('blaster.wav')
KillNoise=pygame.mixer.Sound('Kill.wav')
HitNoise=pygame.mixer.Sound('Hit.wav')
winSound=pygame.mixer.Sound('Victory.wav')
mixer.music.load('BackgroundMusic.wav')
mixer.music.play(-1)

# Define constants for the screen width and height
screen = pygame.display.set_mode((800,600))
SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
UI_HEIGHT = 70
baseSpeed = ((SCREEN_HEIGHT + SCREEN_WIDTH)/700)*3

# Define player1
class Player():
    def __init__(self):
        super(Player, self).__init__()
        self.size = SCREEN_HEIGHT/6
        self.surf = pygame.Surface((self.size, self.size))
        self.surf.fill((255, 255, 150))
        self.image = pygame.image.load('spaceship1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.health = 5
        self.dead = 0
        self.rect.bottom = SCREEN_HEIGHT
        self.rect.right = SCREEN_WIDTH
        self.boost = 50
        self.speed = baseSpeed
        self.angle = 180
    
    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if self.dead == 0:
            if pressed_keys[K_UP]:
                if self.angle<=90:
                    tmpAngle = self.angle
                    xAngle=1
                    yAngle=-1
                elif self.angle<=180:
                    tmpAngle = self.angle - 90
                    xAngle=-1
                    yAngle=-1
                elif self.angle<=270:
                    tmpAngle = self.angle - 180
                    xAngle=-1
                    yAngle=1
                else:
                    tmpAngle = self.angle - 270
                    xAngle=1
                    yAngle=1
                TmpRad = tmpAngle * 0.0174533
                yVelocity = math.sin(TmpRad)
                xVelocity = math.cos(TmpRad)
                xVelocity = xVelocity * self.speed
                yVelocity = yVelocity * self.speed
                if self.angle <= 90 or 180 < self.angle <= 270:
                    self.rect.move_ip(xVelocity * xAngle,yVelocity * yAngle)
                else:
                    self.rect.move_ip(yVelocity * xAngle,xVelocity * yAngle)
            if pressed_keys[K_DOWN]:
                if self.angle<=90:
                    tmpAngle = self.angle
                    xAngle=-1
                    yAngle=1
                elif self.angle<=180:
                    tmpAngle = self.angle - 90
                    xAngle=1
                    yAngle=1
                elif self.angle<=270:
                    tmpAngle = self.angle - 180
                    xAngle=1
                    yAngle=-1
                else:
                    tmpAngle = self.angle - 270
                    xAngle=-1
                    yAngle=-1
                TmpRad = tmpAngle * 0.0174533
                yVelocity = math.sin(TmpRad)
                xVelocity = math.cos(TmpRad)
                xVelocity = xVelocity * self.speed
                yVelocity = yVelocity * self.speed
                if self.angle <= 90 or 180 < self.angle <= 270:
                    self.rect.move_ip(xVelocity * xAngle,yVelocity * yAngle)
                else:
                    self.rect.move_ip(yVelocity * xAngle,xVelocity * yAngle)
            if pressed_keys[K_LEFT]:
                    self.angle+=3
            if pressed_keys[K_RIGHT]:
                    self.angle-=3
            if self.angle < 0:
                self.angle+=360
            if self.angle >= 360:
                self.angle-=360
            if pressed_keys[K_RSHIFT]:
                if self.boost > 0:
                    self.speed = 2*baseSpeed
            if self.speed == 2*baseSpeed:
                self.boost-=2
                if self.boost<=0:
                    self.speed = 1*baseSpeed
            if self.speed == 1*baseSpeed:
                self.boost+=.25
                if self.boost>=100:
                    self.boost=100
            if event.type == pygame.KEYUP:
                if event.key == K_RSHIFT:
                    self.speed = 1*baseSpeed

            # Keep player on the screen
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH
            if self.rect.top <= 0:
                self.rect.top = 0
            if self.rect.bottom >= SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT 

            # Bullet collision
            if ((((bullet2.rect.right <= self.rect.right) and (bullet2.rect.right >= self.rect.left)) or ((bullet2.rect.left >= self.rect.left) and (bullet2.rect.left <= self.rect.right))) and (((bullet2.rect.top >= self.rect.top) and (bullet2.rect.top <= self.rect.bottom)) or ((bullet2.rect.bottom <= self.rect.bottom) and (bullet2.rect.bottom >= self.rect.top)))) and bullet2.exist == 1:
                print("hit")
                self.health-=1
                bullet2.rect.right = -999999999
                if self.health==0:
                    KillNoise.play()
                    self.dead=1
                    self.surf = pygame.Surface((0, 0))
                    self.rect.top = -999999999
                    self.rect.right = -999999999
                    print("Kill!")
                else:
                    HitNoise.play()

# Create Player1's bullet
class Bullet():
    def __init__(self):
        super(Bullet, self).__init__()
        self.surf = pygame.Surface((player.size/2, player.size/10))
        self.surf.fill((0, 0, 250))
        self.image = self.surf
        self.rect = self.surf.get_rect()
        self.exist = 0
        self.speed = 4*player.speed
        self.xVelocity = 0
        self.yVelocity = 0
    
    # Move the bullet based on direction of fire
    def update(self):
        if self.xVelocity == 0:
            if player.angle<=90:
                tmpAngle = player.angle
                xAngle=1
                yAngle=-1
            elif player.angle<=180:
                tmpAngle = player.angle - 90
                xAngle=-1
                yAngle=-1
            elif player.angle<=270:
                tmpAngle = player.angle - 180
                xAngle=-1
                yAngle=1
            else:
                tmpAngle = player.angle - 270
                xAngle=1
                yAngle=1
            TmpRad = tmpAngle * 0.0174533
            self.yVelocity = math.sin(TmpRad)
            self.xVelocity = math.cos(TmpRad)
            self.xVelocity = self.xVelocity * self.speed
            self.yVelocity = self.yVelocity * self.speed
            if player.angle <= 90 or 180 < player.angle <= 270:
                self.xVelocity = self.xVelocity * xAngle
                self.yVelocity = self.yVelocity * yAngle
            else:
                tmpVelo = self.xVelocity
                self.xVelocity = self.yVelocity * xAngle
                self.yVelocity = tmpVelo * yAngle
            self.bulletrotation = pygame.transform.rotate(bullet.image,player.angle)
        self.rect.move_ip(self.xVelocity,self.yVelocity)
# Copy of Bullet1
class Bullet2():
    def __init__(self):
        super(Bullet2, self).__init__()
        self.surf = pygame.Surface((player2.size/2, player2.size/10))
        self.surf.fill((250, 0, 0))
        self.image = self.surf
        self.rect = self.surf.get_rect()
        self.exist = 0
        self.speed = 4*player2.speed
        self.xVelocity = 0
        self.yVelocity = 0
    
    def update(self):
        if self.xVelocity == 0:
            if player2.angle<=90:
                tmpAngle = player2.angle
                xAngle=1
                yAngle=-1
            elif player2.angle<=180:
                tmpAngle = player2.angle - 90
                xAngle=-1
                yAngle=-1
            elif player2.angle<=270:
                tmpAngle = player2.angle - 180
                xAngle=-1
                yAngle=1
            else:
                tmpAngle = player2.angle - 270
                xAngle=1
                yAngle=1
            TmpRad = tmpAngle * 0.0174533
            self.yVelocity = math.sin(TmpRad)
            self.xVelocity = math.cos(TmpRad)
            self.xVelocity = self.xVelocity * self.speed
            self.yVelocity = self.yVelocity * self.speed
            if player2.angle <= 90 or 180 < player2.angle <= 270:
                self.xVelocity = self.xVelocity * xAngle
                self.yVelocity = self.yVelocity * yAngle
            else:
                tmpVelo = self.xVelocity
                self.xVelocity = self.yVelocity * xAngle
                self.yVelocity = tmpVelo * yAngle
            self.bulletrotation = pygame.transform.rotate(bullet2.image,player2.angle)
        self.rect.move_ip(self.xVelocity,self.yVelocity)

# Initialize pygame
pygame.init()

# Copy of Player1
class Player2():
    def __init__(self):
        super(Player2, self).__init__()
        self.size = SCREEN_HEIGHT/6
        self.surf = pygame.Surface((self.size, self.size))
        self.surf.fill((255, 255, 150))
        self.image = pygame.image.load('spaceship2.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.health = 5
        self.dead = 0
        self.boost = 50
        self.speed = 1*baseSpeed
        self.angle = 0
    
    def update(self, pressed_keys):
        if self.dead==0:
            if pressed_keys[K_w]:
                if self.angle<=90:
                    tmpAngle = self.angle
                    xAngle=1
                    yAngle=-1
                elif self.angle<=180:
                    tmpAngle = self.angle - 90
                    xAngle=-1
                    yAngle=-1
                elif self.angle<=270:
                    tmpAngle = self.angle - 180
                    xAngle=-1
                    yAngle=1
                else:
                    tmpAngle = self.angle - 270
                    xAngle=1
                    yAngle=1
                TmpRad = tmpAngle * 0.0174533
                yVelocity = math.sin(TmpRad)
                xVelocity = math.cos(TmpRad)
                xVelocity = xVelocity * self.speed
                yVelocity = yVelocity * self.speed
                if self.angle <= 90 or 180 < self.angle <= 270:
                    self.rect.move_ip(xVelocity * xAngle,yVelocity * yAngle)
                else:
                    self.rect.move_ip(yVelocity * xAngle,xVelocity * yAngle)
            if pressed_keys[K_s]:
                if self.angle<=90:
                    tmpAngle = self.angle
                    xAngle=-1
                    yAngle=1
                elif self.angle<=180:
                    tmpAngle = self.angle - 90
                    xAngle=1
                    yAngle=1
                elif self.angle<=270:
                    tmpAngle = self.angle - 180
                    xAngle=1
                    yAngle=-1
                else:
                    tmpAngle = self.angle - 270
                    xAngle=-1
                    yAngle=-1
                TmpRad = tmpAngle * 0.0174533
                yVelocity = math.sin(TmpRad)
                xVelocity = math.cos(TmpRad)
                xVelocity = xVelocity * self.speed
                yVelocity = yVelocity * self.speed
                if self.angle <= 90 or 180 < self.angle <= 270:
                    self.rect.move_ip(xVelocity * xAngle,yVelocity * yAngle)
                else:
                    self.rect.move_ip(yVelocity * xAngle,xVelocity * yAngle)
            if pressed_keys[K_a]:
                self.angle+=3
            if pressed_keys[K_d]:
                self.angle-=3
            if self.angle < 0:
                self.angle+=360
            if self.angle >= 360:
                self.angle-=360
            if pressed_keys[K_LSHIFT]:
                if self.boost > 0:
                    self.speed = 2*baseSpeed
            if self.speed == 2*baseSpeed:
                self.boost-=2
                if self.boost<=0:
                    self.speed = 1*baseSpeed
            if self.speed == 1*baseSpeed:
                self.boost+=.25
                if self.boost>=100:
                    self.boost=100
            if event.type == pygame.KEYUP:
                if event.key == K_LSHIFT:
                    self.speed = 1*baseSpeed
                
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH
            if self.rect.top <= 0:
                self.rect.top = 0
            if self.rect.bottom >= SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT

            if ((((bullet.rect.right <= self.rect.right) and (bullet.rect.right >= self.rect.left)) or ((bullet.rect.left >= self.rect.left) and (bullet.rect.left <= self.rect.right))) and (((bullet.rect.top >= self.rect.top) and (bullet.rect.top <= self.rect.bottom)) or ((bullet.rect.bottom <= self.rect.bottom) and (bullet.rect.bottom >= self.rect.top)))) and bullet.exist == 1:
                print("hit")
                self.health-=1
                bullet.rect.right = -999999999
                if self.health==0:
                    KillNoise.play()
                    self.dead=1
                    self.surf = pygame.Surface((0, 0))
                    self.rect.top = -999999999
                    self.rect.right = -999999999
                    print("Kill!")
                else:
                    HitNoise.play()

# Explosion that follows Player1 to show when it dies
class deadShip():
    def __init__(self):
        super(deadShip, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 150))
        self.image = pygame.image.load('DeadShip.png').convert_alpha()
        self.rect = self.image.get_rect()

    def update(self):
        if player.dead == 0:
            self.image = pygame.transform.scale(self.image, (player.size, player.size))
            self.rect.top = player.rect.top
            self.rect.left = player.rect.left

# Copy of the first deadship
class deadShip2():
    def __init__(self):
        super(deadShip2, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 150))
        self.image = pygame.image.load('DeadShip.png').convert_alpha()
        self.rect = self.image.get_rect()

    def update(self):
        if player2.dead == 0:
            self.image = pygame.transform.scale(self.image, (player2.size, player2.size))
            self.rect.top = player2.rect.top
            self.rect.left = player2.rect.left

class PlayerHealth():
    def __init__(self):
        super(PlayerHealth, self).__init__()
        self.surf = pygame.Surface((150,100))
        self.surf.fill((255,255,255))
        self.image = pygame.image.load('Health5.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.top = SCREEN_HEIGHT+10
        self.rect.left = 175
    
    def update(self):
        if player.health == 4:
            self.image = pygame.image.load('Health4.png').convert_alpha()
        elif player.health == 3:
            self.image = pygame.image.load('Health3.png').convert_alpha()
        elif player.health == 2:
            self.image = pygame.image.load('Health2.png').convert_alpha()
        elif player.health == 1:
            self.image = pygame.image.load('Health1.png').convert_alpha()
        elif player.health == 0:
            self.image = pygame.image.load('Health0.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (150, 20))

class Player2Health():
    def __init__(self):
        super(Player2Health, self).__init__()
        self.surf = pygame.Surface((150,100))
        self.surf.fill((255,255,255))
        self.image = pygame.image.load('Health5.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.top = SCREEN_HEIGHT+10
        self.rect.left = (SCREEN_WIDTH/2)+125

    def update(self):
        if player2.health == 4:
            self.image = pygame.image.load('Health4.png').convert_alpha()
        if player2.health == 3:
            self.image = pygame.image.load('Health3.png').convert_alpha()
        if player2.health == 2:
            self.image = pygame.image.load('Health2.png').convert_alpha()
        if player2.health == 1:
            self.image = pygame.image.load('Health1.png').convert_alpha()
        if player2.health == 0:
            self.image = pygame.image.load('Health0.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (150, 20))

# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT + UI_HEIGHT),RESIZABLE)

# Instantiate classes
player = Player()
bullet = Bullet()
player2 = Player2()
bullet2 = Bullet2()
deadship = deadShip()
deadship2 = deadShip2()
playerHealth = PlayerHealth()
player2Health = Player2Health()

font = pygame.font.SysFont('agencyfb', 30)
backgroundImage=pygame.image.load('background.png').convert()
backgroundImage=pygame.transform.scale(backgroundImage, (SCREEN_WIDTH, SCREEN_HEIGHT))
backgroundImageRect=backgroundImage.get_rect()
# Variable to keep the main loop running
running = True

# Main loop
while running:
    #Resize and keep proportional
    if (SCREEN_WIDTH, (SCREEN_HEIGHT + UI_HEIGHT)) != screen.get_size():
        (tmpSW, tmpSH) = screen.get_size()
        screenWdiff = tmpSW - SCREEN_WIDTH
        screenHdiff = (tmpSH - UI_HEIGHT) - SCREEN_HEIGHT
        tmpbottom = (player.rect.bottom / SCREEN_HEIGHT) * tmpSH
        tmpright = (player.rect.right / SCREEN_WIDTH) * tmpSW
        tmp2bottom = (player2.rect.bottom / SCREEN_HEIGHT) * tmpSH
        tmp2right = (player2.rect.right / SCREEN_WIDTH) * tmpSW
        (SCREEN_WIDTH, SCREEN_HEIGHT) = screen.get_size()
        SCREEN_HEIGHT -= UI_HEIGHT
        backgroundImage=pygame.image.load('background.png').convert()
        backgroundImage=pygame.transform.scale(backgroundImage, (SCREEN_WIDTH, SCREEN_HEIGHT))
        backgroundImageRect=backgroundImage.get_rect()
        player.rect.bottom = tmpbottom
        player.rect.right = tmpright
        player2.rect.bottom = tmp2bottom
        player2.rect.right = tmp2right
        player.size = SCREEN_HEIGHT/6
        player2.size = SCREEN_HEIGHT/6
        player.rect.update((player.rect.left,player.rect.top),(player.size,player.size))
        player2.rect.update((player2.rect.left,player2.rect.top),(player2.size,player2.size))
        bullet.rect.update((bullet.rect.left,bullet.rect.top),(player.size/2, player.size/10))
        bullet2.rect.update((bullet2.rect.left,bullet2.rect.top),(player2.size/2, player2.size/10))
        if player.rect.bottom>SCREEN_HEIGHT:
            player.rect.bottom = SCREEN_HEIGHT
        if player.rect.right>SCREEN_WIDTH:
            player.rect.right=SCREEN_WIDTH
        if player2.rect.bottom>SCREEN_HEIGHT:
            player2.rect.bottom = SCREEN_HEIGHT
        if player2.rect.right>SCREEN_WIDTH:
            player2.rect.right=SCREEN_WIDTH
        baseSpeed = ((SCREEN_HEIGHT + SCREEN_WIDTH)/700)*3
        if baseSpeed<1:
            baseSpeed=1
        player.speed = baseSpeed
        player2.speed = baseSpeed
    if player.dead == 1 or player2.dead == 1:
        mixer.music.stop()
        winSound.play()
        time.sleep(3)
        font = pygame.font.SysFont('agencyfb', 30)
        running = False
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            if player.dead == 0:
                if event.key == K_RALT:
                    if bullet.rect.right >= SCREEN_WIDTH+(player2.size/2) or bullet.rect.right <= 0 or bullet.rect.bottom < 0 or bullet.rect.top >SCREEN_HEIGHT or bullet.exist==0:
                        bullet.exist=1
                        BlasterNoise.play()
                        bullet.xVelocity = 0
                        bullet.rect.top = player.rect.top + (player.size/2)
                        bullet.rect.left = player.rect.left + (player.size/2)

            #Player2
            if player2.dead == 0:
                if event.key == K_LALT:
                    if bullet2.rect.right >= SCREEN_WIDTH+(player2.size/2) or bullet2.rect.right <= 0 or bullet2.rect.bottom < 0 or bullet2.rect.top >SCREEN_HEIGHT or bullet2.exist==0:
                        bullet2.exist=1
                        BlasterNoise.play()
                        bullet2.xVelocity = 0
                        bullet2.rect.top = player2.rect.top + (player2.size/2)
                        bullet2.rect.left = player2.rect.left + (player2.size/2)
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False
    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()

    # Update the player sprite based on user keypresses
    player.update(pressed_keys)
    player2.update(pressed_keys)
    deadship.update()
    deadship2.update()
    if bullet.exist==1:
        bullet.update()
    if bullet2.exist==1:
        bullet2.update()

    # Fill the screen with background image
    screen.fill((0, 0, 0))
    screen.blit(backgroundImage,backgroundImageRect)

    if bullet.exist==1:
        screen.blit(bullet.bulletrotation, bullet.rect)
    if bullet2.exist==1:
        screen.blit(bullet2.bulletrotation,bullet2.rect)
    #Update UI
    Info1H = font.render("Magenta Health:", True, (236, 240, 241))
    Info1S = font.render("Stamina:", True, (236, 240, 241))
    Info2H = font.render("Red Health:", True, (236, 240, 241))
    Info2S = font.render("Stamina:", True, (236, 240, 241))
    playerHealth.update()
    player2Health.update()
    screen.blit(Info1H, (10,SCREEN_HEIGHT))
    screen.blit(playerHealth.image,playerHealth.rect)
    playerHealth.rect.top = SCREEN_HEIGHT+10
    playerHealth.rect.left = 175
    screen.blit(Info1S, (10,SCREEN_HEIGHT+30))
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(110, SCREEN_HEIGHT+40, 150, 20))
    pygame.draw.rect(screen, (238, 255, 0), pygame.Rect(110, SCREEN_HEIGHT+40, player.boost*1.5, 20))
    screen.blit(Info2H, (SCREEN_WIDTH/2,SCREEN_HEIGHT))
    screen.blit(player2Health.image,player2Health.rect)
    player2Health.rect.top = SCREEN_HEIGHT+10
    player2Health.rect.left = SCREEN_WIDTH/2+125
    screen.blit(Info1S, (SCREEN_WIDTH/2,SCREEN_HEIGHT+30))
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(SCREEN_WIDTH/2+100, SCREEN_HEIGHT+40, 150, 20),0)
    pygame.draw.rect(screen, (238, 255, 0), pygame.Rect(SCREEN_WIDTH/2+100, SCREEN_HEIGHT+40, player2.boost*1.5, 20))

    # Draw the objects on the screen
    playerrotation = pygame.transform.rotate(player.image,player.angle)
    screen.blit(playerrotation, player.rect)
    player2rotation = pygame.transform.rotate(player2.image,player2.angle)
    screen.blit(player2rotation,player2.rect)
    if player.dead == 1:
        font = pygame.font.SysFont('agencyfb', 50)
        screen.blit(deadship.image, deadship.rect)
        playerLostText = font.render("Player 2 Wins!", True, (255,255,255),(0,0,0))
        screen.blit(playerLostText,(SCREEN_WIDTH/2-100,SCREEN_HEIGHT/2-25))
    if player2.dead == 1:
        font = pygame.font.SysFont('agencyfb', 50)
        screen.blit(deadship2.image, deadship2.rect)
        player2LostText = font.render("Player 1 Wins!", True, (255,255,255),(0,0,0))
        screen.blit(player2LostText,(SCREEN_WIDTH/2-100,SCREEN_HEIGHT/2-25))
        
    # Update the display
    pygame.display.flip()
    clock = pygame.time.Clock()
    clock.tick(60)