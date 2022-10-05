# Import the pygame module
import pygame
from pygame import mixer

pygame.mixer.init()

BulletExist = 0

import random
import sys
import math

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
window = pygame.display.set_mode((winw, winh))
bg_img = pygame.image.load('background.png')
bg_img = pygame.transform.scale(bg_img,(winw, winh))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

i = 0

clock = pygame.time.Clock()

rect1 = pygame.rect.Rect(550, 550, 16, 16)

# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player():
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 150))
        self.image = pygame.image.load('triangleV3.png').convert_alpha()
        self.rect = self.image.get_rect()
    
    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -10)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 10)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-10, 0)
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

#class for basic bullet
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

class Button:
    def __init__(self, x, y, width, height, fg, bg, content, size):
        self.font = pygame.font.Font('arial.ttf',  32)
        self.content = content

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.fg = fg
        self.bg = bg

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

        self.text = self.font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect(center=(self.width/2, self.height/2))
        self.image.blit(self.text, self.text_rect)

    # get pos of mouse, check if mouse is on it, check if mouse pressed it
    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False


#Example enemy for collision
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


player = Player()
clock = pygame.time.Clock()
triangle  = Triangle()
bullet = Bullet()
enemies = [triangle]

#title = pygame.font.get_default_font('AT Robots Inspired Game', True, WHITE)
#title_rect = title.get_rect(x=220, y=200)

play_button = Button(350, 250, 100, 50, BLACK, WHITE, 'Play', 32)

intro = True
while intro:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            intro = False
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    if play_button.is_pressed(mouse_pos, mouse_pressed):
        intro = False

    #screen.blit(pygame.intro_background, (0,0))
    #pygame.screen.blit(title, title_rect)
    screen.blit(play_button.image, play_button.rect)
    clock.tick(FPS)
    pygame.display.update()

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
    #Create Screen
    
    window.fill((0,0,0))
    window.blit(bg_img,(i,0))
    window.blit(bg_img,(winw+i,0))
    if(i==-winw):
            window.blit(bg_img,(winw+i,0))
            i=0
            i-=0.05
    #Collision to remove enemy
    for enemy in enemies:
        enemy.move()
        bullet.collide(enemy, enemies)
        enemy.draw(screen)
        

    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    screen.blit(player.image, player.rect)
    #if bullet exist create bullet
    if BulletExist==1:
        bullet.update()

    # Draw the player on the screen
    if BulletExist==1:
       screen.blit(bullet.surf, bullet.rect)

    # Update the display
    pygame.display.update()

    clock.tick(40)
pygame.quit()