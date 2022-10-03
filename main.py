# Import the pygame module
import pygame
from pygame import mixer

pygame.mixer.init()

BulletExist = 0

import random

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
    K_SPACE,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

BlasterNoise = pygame.mixer.Sound('blaster.wav')

# Define constants for the screen width and height
winw = 600
winh = 600
screen = pygame.display.set_mode((winw, winh))

clock = pygame.time.Clock()

player1 = pygame.rect.Rect(32, 32, 24, 24)
rect1 = pygame.rect.Rect(550, 550, 16, 16)
# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("triangleV3.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
    
    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -10)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 10)
        if pressed_keys[K_LEFT]:
            self.rect = pygame.transform.rotate(self.rect, -10)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(10, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > winw:
            self.rect.right = winw
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= winh:
            self.rect.bottom = winh
   # def collide(self, enemy, enemy_list):
    #    if self.rect.colliderect(enemy.rect):
     #       enemy_list.remove(enemy)
    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 128), self.rect)

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super(Bullet, self).__init__()
        self.surf = pygame.image.load('BulletV1.png').convert()
        self.surf.set_colorkey((255, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()

    # Move the sprite based on user keypresses
    def update(self):
        if self.rect.right < (winw + 26):
            self.rect.move_ip(10,0)
    def collide(self, enemy, enemy_list):
        if self.rect.colliderect(enemy.rect):
            enemy_list.remove(enemy)

     

class Triangle(pygame.sprite.Sprite):
    def __init__(self):
        self.rect = rect1
        self.x = 0
        self.y = 0
    def move(self):
        self.rect.move_ip(0, 0)
    def draw(self, surface):
        pygame.draw.rect(surface, (100, 100, 100), self.rect)
       




# Initialize pygame
pygame.init()

# Instantiate player. Right now, this is just a rectangle.
player = Player()
clock = pygame.time.Clock()
triangle  = Triangle()
bullet = Bullet()
enemies = [triangle]

# Variable to keep the main loop running
running = True

# Main loop
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                if bullet.rect.right >= winw +26 or BulletExist==0:
                    BulletExist=1
                    BlasterNoise.play()
                    bullet.rect.left=player.rect.left+70
                    bullet.rect.top=player.rect.top+12
            # If the Esc key is pressed, then exit the main loop
            elif event.key == K_ESCAPE:
                running = False

    screen.fill((255, 255, 255))
    
    for enemy in enemies:
        enemy.move()
        bullet.collide(enemy, enemies)
        enemy.draw(screen)
        

    player.draw(screen) 
    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    
    if BulletExist==1:
        bullet.update()

    # Draw the player on the screen
    if BulletExist==1:
       screen.blit(bullet.surf, bullet.rect)

   # if pygame.sprite.spritecollideany(enemies, bullet):
    #   enemies.kill()
     #  running = True

    # Update the display
    pygame.display.update()

    clock.tick(40)