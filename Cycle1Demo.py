# Import the pygame modules
import pygame
from pygame import *
import time

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
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# Constants for colors
WHITE = (255,255,255)
BLACK = (0,0,0)
MAGENTA = (255,165,240)
# Title image import
title_img = pygame.image.load('title_screen_image.png')
title_img.set_colorkey(WHITE)

# Define player1
class Player():
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 150))
        self.image = pygame.image.load('spaceship1R.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.health = 5
        self.dead = 0
        self.rect.bottom = SCREEN_HEIGHT
        self.rect.right = SCREEN_WIDTH
        self.facingLeft = 1
    
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

            # Change sprite direction
            if self.facingLeft==0:
                self.image = pygame.image.load('spaceship1R.png').convert_alpha()
            if player.facingLeft==1:
                self.image = pygame.image.load('spaceship1L.png').convert_alpha()

            # Keep size uniform
            self.image = pygame.transform.scale(self.image, (50, 50))

            # Bullet collision
            if (bullet2.rect.right <= self.rect.right) and (bullet2.rect.top >= self.rect.top) and (bullet2.rect.left >= self.rect.left) and (bullet2.rect.bottom <= self.rect.bottom) and bullet2.exist == 1:
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

# Button for title screen
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

# Create Player1's bullet
class Bullet():
    def __init__(self):
        super(Bullet, self).__init__()
        self.surf = pygame.Surface((25, 5))
        self.surf.fill((0, 0, 250))
        self.image = self.surf
        self.rect = self.surf.get_rect()
        self.exist = 0
        self.facingLeft = 1
    
    # Move the bullet based on direction of fire
    def updateR(self):
        if self.rect.right < (SCREEN_WIDTH + 26) and self.rect.right != 0:
            self.rect.move_ip(4,0)
            self.image = pygame.image.load('bullet1R.png').convert_alpha()
    def updateL(self):
        if self.rect.right > 0 and self.rect.right != (SCREEN_WIDTH + 26):
            self.rect.move_ip(-4,0)
            self.image = pygame.image.load('bullet1L.png').convert_alpha()

# Copy of Bullet1
class Bullet2():
    def __init__(self):
        super(Bullet2, self).__init__()
        self.surf = pygame.Surface((25, 5))
        self.surf.fill((250, 0, 0))
        self.image = self.surf
        self.rect = self.surf.get_rect()
        self.exist = 0
        self.facingLeft = 0
    
    def updateR(self):
        if self.rect.right < (SCREEN_WIDTH + 26) and self.rect.right != 0:
            self.rect.move_ip(4,0)
            self.image = pygame.image.load('bullet2R.png').convert_alpha()
    def updateL(self):
        if self.rect.right > 0 and self.rect.right != (SCREEN_WIDTH + 26):
            self.rect.move_ip(-4,0)
            self.image = pygame.image.load('bullet2L.png').convert_alpha()

# Initialize pygame
pygame.init()

# Copy of Player1
class Player2():
    def __init__(self):
        super(Player2, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 150))
        self.image = pygame.image.load('RShipL.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.health = 5
        self.dead = 0
        self.facingLeft = 0
    
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
                
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH
            if self.rect.top <= 0:
                self.rect.top = 0
            if self.rect.bottom >= SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT

            if self.facingLeft==0:
                self.image = pygame.image.load('spaceship2R.png').convert_alpha()

            if self.facingLeft==1:
                self.image = pygame.image.load('spaceship2L.png').convert_alpha()

            self.image = pygame.transform.scale(self.image, (50, 50))

            if (bullet.rect.right <= self.rect.right) and (bullet.rect.top >= self.rect.top) and (bullet.rect.left >= self.rect.left) and (bullet.rect.bottom <= self.rect.bottom) and bullet.exist == 1:
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

# Explosion that follows Player1 to show when it dies
class deadShip():
    def __init__(self):
        super(deadShip, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 150))
        self.image = pygame.image.load('DeadShip.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

    def update(self):
        if player.dead == 0:
            self.rect.top = player.rect.top
            self.rect.left = player.rect.left

# Copy of the first deadship
class deadShip2():
    def __init__(self):
        super(deadShip2, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 150))
        self.image = pygame.image.load('DeadShip.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

    def update(self):
        if player2.dead == 0:
            self.rect.top = player2.rect.top
            self.rect.left = player2.rect.left

# Text to display when Player1 loses
class PlayerLost():
    def __init__(self):
        super(PlayerLost, self).__init__()
        self.surf = pygame.Surface((150, 100))
        self.surf.fill((255, 255, 150))
        self.image = pygame.image.load('PlayerLost.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.top = 270
        self.rect.left = 278

#Text to display when Player2 loses
class Player2Lost():
    def __init__(self):
        super(Player2Lost, self).__init__()
        self.surf = pygame.Surface((150, 100))
        self.surf.fill((255, 255, 150))
        self.image = pygame.image.load('Player2Lost.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.top = 270
        self.rect.left = 278

# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),RESIZABLE)

# Instantiate classes
player = Player()
bullet = Bullet()
player2 = Player2()
bullet2 = Bullet2()
deadship = deadShip()
deadship2 = deadShip2()
playerLost = PlayerLost()
player2Lost = Player2Lost()

# Intro screen
play_button = Button( ((SCREEN_WIDTH/2) - 50), 300, 100, 50, BLACK, WHITE, 'Play', 32)
screen.fill(MAGENTA)
screen.blit(title_img, (50,100))    

intro = True
while intro:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            intro = False
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    if play_button.is_pressed(mouse_pos, mouse_pressed):
        intro = False

    screen.blit(play_button.image, play_button.rect)
    pygame.display.update()

# Variable to keep the main loop running
running = True

# Main loop
while running:
    if player.dead == 1 or player2.dead == 1:
        mixer.music.stop()
        winSound.play()
        time.sleep(3)
        running = False
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            if player.dead == 0:
                if event.key == K_RIGHT:
                    if bullet.rect.right >= SCREEN_WIDTH+26 or bullet.rect.right <= 0 or bullet.exist==0:
                        player.facingLeft=0
                elif event.key ==K_LEFT:
                    if bullet.rect.right >= SCREEN_WIDTH+26 or bullet.rect.right <= 0 or bullet.exist==0:
                        player.facingLeft=1
                elif event.key == K_RALT:
                    if bullet.rect.right >= SCREEN_WIDTH+26 or bullet.rect.right <= 0 or bullet.exist==0:
                        bullet.exist=1
                        BlasterNoise.play()
                        if player.facingLeft==0:
                            bullet.facingLeft=0
                            bullet.rect.left=player.rect.left+45
                            bullet.rect.top=player.rect.top+25
                        if player.facingLeft==1:
                            bullet.facingLeft=1
                            bullet.rect.left=player.rect.left+5
                            bullet.rect.top=player.rect.top+25

            #Player2
            if player2.dead == 0:
                if event.key == K_a:
                    if bullet2.rect.right >= SCREEN_WIDTH+26 or bullet2.rect.right <= 0 or bullet2.exist==0:
                        player2.facingLeft=1
                elif event.key ==K_d:
                    if bullet2.rect.right >= SCREEN_WIDTH+26 or bullet2.rect.right <= 0 or bullet2.exist==0:
                        player2.facingLeft=0
                elif event.key == K_LALT:
                    if bullet2.rect.right >= SCREEN_WIDTH+26 or bullet2.rect.right <= 0 or bullet2.exist==0:
                        bullet2.exist=1
                        BlasterNoise.play()
                        if player2.facingLeft==0:
                            bullet2.facingLeft=0
                            bullet2.rect.left=player2.rect.left+45
                            bullet2.rect.top=player2.rect.top+25
                        if player2.facingLeft==1:
                            bullet2.facingLeft=1
                            bullet2.rect.left=player2.rect.left+5
                            bullet2.rect.top=player2.rect.top+25
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
        if bullet.facingLeft==1:
            bullet.updateL()
        elif bullet.facingLeft==0:
            bullet.updateR()
    if bullet2.exist==1:
        if bullet2.facingLeft==1:
            bullet2.updateL()
        elif bullet2.facingLeft==0:
            bullet2.updateR()

    backgroundImage=pygame.image.load('background.png').convert()
    backgrounImage = pygame.transform.scale(backgroundImage, (800, 600))
    backgroundImageRect=backgroundImage.get_rect()

    # Fill the screen with background image
    screen.fill((0, 0, 0))
    screen.blit(backgroundImage,backgroundImageRect)

    # Draw the objects on the screen
    screen.blit(player.image, player.rect)
    screen.blit(player2.image,player2.rect)
    if bullet.exist==1:
        screen.blit(bullet.image, bullet.rect)
    if bullet2.exist==1:
        screen.blit(bullet2.image,bullet2.rect)
    if player.dead == 1:
        screen.blit(deadship.image, deadship.rect)
        screen.blit(playerLost.image, playerLost.rect)
    if player2.dead == 1:
        screen.blit(deadship2.image, deadship2.rect)
        screen.blit(player2Lost.image, player2Lost.rect)
        
    # Update the display
    pygame.display.flip()
