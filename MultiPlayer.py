# Import the pygame module
import pygame
from pygame import mixer
import random

pygame.mixer.init()

BulletExist=0
Bullet2Exist=0
FacingLeft=0
FacingLeft2=1

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
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

BlasterNoise=pygame.mixer.Sound('blaster.wav')
KillNoise=pygame.mixer.Sound('Kill.wav')
HitNoise=pygame.mixer.Sound('Hit.wav')

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player():
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 150))
        self.image = pygame.image.load('firstShip(2).png').convert_alpha()
        self.rect = self.image.get_rect()
        self.health = 5
        self.dead = 0
    
    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if self.dead == 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -1)
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 1)
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-1, 0)
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(1, 0)
                

            # Keep player on the screen
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH
            if self.rect.top <= 0:
                self.rect.top = 0
            if self.rect.bottom >= SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT 

            if (bullet2.rect.right <= self.rect.right) and (bullet2.rect.top >= self.rect.top) and (bullet2.rect.left >= self.rect.left) and (bullet2.rect.bottom <= self.rect.bottom) and Bullet2Exist == 1:
                print("hit")
                self.health-=1
                bullet2.rect.right = 0
                if self.health==0:
                    KillNoise.play()
                    self.dead=1
                    self.surf = pygame.Surface((0, 0))
                    self.rect.top = -1
                    self.rect.right = -1
                    print("Kill!")
                else:
                    HitNoise.play()
class Bullet():
    def __init__(self):
        super(Bullet, self).__init__()
        self.surf = pygame.Surface((25, 5))
        self.surf.fill((0, 0, 250))
        self.rect = self.surf.get_rect()
    
    # Move the sprite based on user keypresses
    def updateR(self):
        if self.rect.right < (SCREEN_WIDTH + 26) and self.rect.right != 0:
            self.rect.move_ip(1,0)
    def updateL(self):
        if self.rect.right > 0 and self.rect.right != (SCREEN_WIDTH + 26):
            self.rect.move_ip(-1,0)

class Bullet2():
    def __init__(self):
        super(Bullet2, self).__init__()
        self.surf = pygame.Surface((25, 5))
        self.surf.fill((250, 0, 0))
        self.rect = self.surf.get_rect()
    
    # Move the sprite based on user keypresses
    def updateR(self):
        if self.rect.right < (SCREEN_WIDTH + 26) and self.rect.right != 0:
            self.rect.move_ip(1,0)
    def updateL(self):
        if self.rect.right > 0 and self.rect.right != (SCREEN_WIDTH + 26):
            self.rect.move_ip(-1,0)
# Initialize pygame
pygame.init()

class Player2():
    def __init__(self):
        super(Player2, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 150))
        self.image = pygame.image.load('firstShip(2)L.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.health = 5
        self.dead = 0
        self.rect.bottom = SCREEN_HEIGHT
        self.rect.right = SCREEN_WIDTH
    
    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if self.dead==0:
            if pressed_keys[K_w]:
                self.rect.move_ip(0, -1)
            if pressed_keys[K_s]:
                self.rect.move_ip(0, 1)
            if pressed_keys[K_a]:
                self.rect.move_ip(-1, 0)
            if pressed_keys[K_d]:
                self.rect.move_ip(1, 0)
                

            # Keep player on the screen
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH
            if self.rect.top <= 0:
                self.rect.top = 0
            if self.rect.bottom >= SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT

            if (bullet.rect.right <= self.rect.right) and (bullet.rect.top >= self.rect.top) and (bullet.rect.left >= self.rect.left) and (bullet.rect.bottom <= self.rect.bottom) and BulletExist == 1:
                print("hit")
                self.health-=1
                bullet.rect.right = 0
                if self.health==0:
                    KillNoise.play()
                    self.dead=1
                    self.surf = pygame.Surface((0, 0))
                    self.rect.top = -1
                    self.rect.right = -1
                    print("Kill!")
                else:
                    HitNoise.play()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Instantiate player. Right now, this is just a rectangle.
player = Player()
bullet = Bullet()
player2 = Player2()
bullet2 = Bullet2()

# Variable to keep the main loop running
running = True

# Main loop
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                if bullet.rect.right >= SCREEN_WIDTH+26 or bullet.rect.right == 0 or BulletExist==0:
                    FacingLeft=0
                    player.image= pygame.image.load('firstShip(2).png').convert_alpha()
            elif event.key ==K_LEFT:
                if bullet.rect.right >= SCREEN_WIDTH+26 or bullet.rect.right == 0 or BulletExist==0:
                    FacingLeft=1
                    player.image= pygame.image.load('firstShipL.png').convert_alpha()
            elif event.key == K_RALT:
                if bullet.rect.right >= SCREEN_WIDTH+26 or bullet.rect.right == 0 or BulletExist==0:
                    BulletExist=1
                    BlasterNoise.play()
                    if FacingLeft==0:
                        bullet.rect.left=player.rect.left+70
                        bullet.rect.top=player.rect.top+12
                    if FacingLeft==1:
                        bullet.rect.left=player.rect.left+5
                        bullet.rect.top=player.rect.top+12

            #Player2
            if event.key == K_a:
                if bullet2.rect.right >= SCREEN_WIDTH+26 or bullet2.rect.right == 0 or Bullet2Exist==0:
                    FacingLeft2=1
                    player2.image= pygame.image.load('firstShip(2)L.png').convert_alpha()
            elif event.key ==K_d:
                if bullet2.rect.right >= SCREEN_WIDTH+26 or bullet2.rect.right == 0 or Bullet2Exist==0:
                    FacingLeft2=0
                    player2.image= pygame.image.load('firstShip.png').convert_alpha()
            elif event.key == K_LALT:
                if bullet2.rect.right >= SCREEN_WIDTH+26 or bullet2.rect.right == 0 or Bullet2Exist==0:
                    Bullet2Exist=1
                    BlasterNoise.play()
                    if FacingLeft2==0:
                        bullet2.rect.left=player2.rect.left+70
                        bullet2.rect.top=player2.rect.top+12
                    if FacingLeft2==1:
                        bullet2.rect.left=player2.rect.left+5
                        bullet2.rect.top=player2.rect.top+12
            # If the Esc key is pressed, then exit the main loop
            elif event.key == K_ESCAPE:
                running = False
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False
    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()

    # Update the player sprite based on user keypresses
    player.update(pressed_keys)
    player2.update(pressed_keys)
    if BulletExist==1:
        if FacingLeft==1:
            bullet.updateL()
        elif FacingLeft==0:
            bullet.updateR()
    if Bullet2Exist==1:
        if FacingLeft2==1:
            bullet2.updateL()
        elif FacingLeft2==0:
            bullet2.updateR()

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw the player on the screen
    screen.blit(player.image, player.rect)
    screen.blit(player2.image,player2.rect)
    if BulletExist==1:
        screen.blit(bullet.surf, bullet.rect)
    if Bullet2Exist==1:
        screen.blit(bullet2.surf,bullet2.rect)
    # Update the display
    pygame.display.flip()