# Import the pygame modules
import sys
import pygame_menu
from pygame import *
from pickle import NONE
from random import randint
import pygame
import time
import math
import os

def start_the_game():
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

    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception: base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    # Set sounds and music
    BlasterNoise=pygame.mixer.Sound(resource_path('blaster.wav'))
    KillNoise=pygame.mixer.Sound(resource_path('Kill.wav'))
    HitNoise=pygame.mixer.Sound(resource_path('Hit.wav'))
    winSound=pygame.mixer.Sound(resource_path('Victory.wav'))

    # Define constants for the screen width and height
    screen = pygame.display.set_mode((800,600))
    SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
    UI_HEIGHT = 70
    baseSpeed = ((SCREEN_HEIGHT + SCREEN_WIDTH)/700)*4

    clock = pygame.time.Clock()

    # Define player1
    class Player():
        def __init__(self):
            super(Player, self).__init__()
            self.size = SCREEN_HEIGHT/6
            self.surf = pygame.Surface((self.size, self.size))
            self.surf.fill((255, 255, 150))
            self.image = pygame.image.load(resource_path('spaceship1.png')).convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.size, self.size))
            self.rect = self.image.get_rect()
            self.health = 5
            self.dead = 0
            self.rect.bottom = SCREEN_HEIGHT
            self.rect.right = SCREEN_WIDTH
            self.boost = 50
            self.speed = baseSpeed
            self.mask = pygame.mask.from_surface(self.image)
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
                if self.rect.bottom >= SCREEN_HEIGHT-10:
                    self.rect.bottom = SCREEN_HEIGHT-10

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

                # Asteroid collision
                offset_x = asteroid.rect.x - self.rect.x
                offset_y = asteroid.rect.y - self.rect.y
                overlap = asteroid.mask.overlap(self.mask, (offset_x, offset_y))
                if overlap:
                    print("hit")
                    self.health-=1
                    asteroid.rect.left = -100
                    if self.health == 0:
                        KillNoise.play()
                        self.dead = 1
                        self.surf = pygame.Surface((0,0))
                        self.rect.top = -1
                        self.rect.right = -1
                        print("Kill!")
                    else:
                        HitNoise.play()

    # Create Player1's bullet
    class Bullet():
        def __init__(self):
            super(Bullet, self).__init__()
            self.surf = pygame.Surface((player.size/2, player.size/10))
            self.surf.fill((0, 0, 250))
            self.image = pygame.image.load(resource_path('bullet1R.png')).convert_alpha()
            self.rect = self.image.get_rect()
            self.exist = 0
            self.speed = 4*player.speed
            self.xVelocity = 0
            self.yVelocity = 0
        
        # Move the bullet based on direction of fire
        def update(self):
            self.speed = 4*player.speed
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
                self.image = pygame.transform.scale(self.image, (player.size/2, player.size/10))
                self.bulletrotation = pygame.transform.rotate(bullet.image,player.angle)
            self.rect.move_ip(self.xVelocity,self.yVelocity)

    # Copy of Bullet1
    class Bullet2():
        def __init__(self):
            super(Bullet2, self).__init__()
            self.surf = pygame.Surface((player2.size/2, player2.size/10))
            self.surf.fill((250, 0, 0))
            self.image = pygame.image.load(resource_path('bullet2R.png')).convert_alpha()
            self.rect = self.image.get_rect()
            self.exist = 0
            self.speed = 4*player2.speed
            self.xVelocity = 0
            self.yVelocity = 0
        
        def update(self):
            self.speed = 4*player.speed
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
                self.image = pygame.transform.scale(self.image, (player.size/2, player.size/10))
                self.bulletrotation = pygame.transform.rotate(bullet2.image,player2.angle)
            self.rect.move_ip(self.xVelocity,self.yVelocity)

    # Copy of Player1
    class Player2():
        def __init__(self):
            super(Player2, self).__init__()
            self.size = SCREEN_HEIGHT/6
            self.surf = pygame.Surface((self.size, self.size))
            self.surf.fill((255, 255, 150))
            self.image = pygame.image.load(resource_path('spaceship2.png')).convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.size, self.size))
            self.rect = self.image.get_rect()
            self.health = 5
            self.dead = 0
        
            self.boost = 50
            self.speed = 1*baseSpeed
            self.mask = pygame.mask.from_surface(self.image)
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
                if self.rect.bottom >= SCREEN_HEIGHT-10:
                    self.rect.bottom = SCREEN_HEIGHT-10

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

                # Asteroid collision
                offset_x = asteroid.rect.x - self.rect.x
                offset_y = asteroid.rect.y - self.rect.y
                overlap = asteroid.mask.overlap(self.mask, (offset_x, offset_y))
                if overlap:
                    print("hit")
                    self.health-=1
                    asteroid.rect.left = -100
                    if self.health == 0:
                        KillNoise.play()
                        self.dead = 1
                        self.surf = pygame.Surface((0,0))
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
            self.image = pygame.image.load(resource_path('DeadShip.png')).convert_alpha()
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
            self.image = pygame.image.load(resource_path('DeadShip.png')).convert_alpha()
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
            self.image = pygame.image.load(resource_path('Health5.png')).convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.top = SCREEN_HEIGHT+10
            self.rect.left = 175
        
        def update(self):
            if player.health == 4:
                self.image = pygame.image.load(resource_path('Health4.png')).convert_alpha()
            elif player.health == 3:
                self.image = pygame.image.load(resource_path('Health3.png')).convert_alpha()
            elif player.health == 2:
                self.image = pygame.image.load(resource_path('Health2.png')).convert_alpha()
            elif player.health == 1:
                self.image = pygame.image.load(resource_path('Health1.png')).convert_alpha()
            elif player.health == 0:
                self.image = pygame.image.load(resource_path('Health0.png')).convert_alpha()
            self.image = pygame.transform.scale(self.image, (150, 20))

    class Player2Health():
        def __init__(self):
            super(Player2Health, self).__init__()
            self.surf = pygame.Surface((150,100))
            self.surf.fill((255,255,255))
            self.image = pygame.image.load(resource_path('Health5.png')).convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.top = SCREEN_HEIGHT+10
            self.rect.left = (SCREEN_WIDTH/2)+125

        def update(self):
            if player2.health == 4:
                self.image = pygame.image.load(resource_path('Health4.png')).convert_alpha()
            if player2.health == 3:
                self.image = pygame.image.load(resource_path('Health3.png')).convert_alpha()
            if player2.health == 2:
                self.image = pygame.image.load(resource_path('Health2.png')).convert_alpha()
            if player2.health == 1:
                self.image = pygame.image.load(resource_path('Health1.png')).convert_alpha()
            if player2.health == 0:
                self.image = pygame.image.load(resource_path('Health0.png')).convert_alpha()
            self.image = pygame.transform.scale(self.image, (150, 20))

    class Asteroid():
        def __init__(self):
            super(Asteroid, self).__init__()
            self.size = SCREEN_HEIGHT/4
            self.surf = pygame.Surface((self.size, self.size))
            self.surf.fill((255, 255, 150))
            self.image = pygame.image.load(resource_path('asteroid2.png')).convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.size,self.size))
            self.rect = self.image.get_rect()
            self.rect.bottom = SCREEN_HEIGHT
            self.rect.left = -75
            self.mask = pygame.mask.from_surface(self.image)

            # Boundaries for asteroid
            if self.rect.left < -200:
                self.rect.left = -200
            if self.rect.right > SCREEN_WIDTH+200:
                self.rect.right = SCREEN_WIDTH+200
            if self.rect.top <= -200:
                self.rect.top = -200
            if self.rect.bottom >= SCREEN_HEIGHT+40:
                self.rect.bottom = SCREEN_HEIGHT+40

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
    asteroid = Asteroid()

    # Background
    direction = 1
    speed_x = randint(0,5)
    speed_y = randint(0,5)
    bg = pygame.image.load(resource_path('background.png')).convert()
    bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    bgRect = bg.get_rect()
    bgX = 0
    bgX2 = bg.get_width()
    def redrawWindow():
        screen.blit(bg, (bgX,0))
        screen.blit(bg, (bgX2,0))

    font = pygame.font.SysFont('agencyfb', 30)

    # Variable to keep the main loop running
    running = True

    # Main loop
    while running:
        #background movement
        redrawWindow()
        clock.tick(30)
        bgX -= 1.5
        bgX2 -= 1.5
        if bgX < bg.get_width() * -1:
            bgX = bg.get_width()    
        if bgX2 < bg.get_width() * -1:
            bgX2 = bg.get_width()
        # randomly moving asteroids
        if asteroid.rect.left <= -200 or asteroid.rect.right >= SCREEN_WIDTH+200:
            direction *= -1
            speed_x = randint(0, 5) * direction
            speed_y = randint(0, 5) * direction
            if speed_x == 0 and speed_y == 0:
                speed_x = randint(2, 5) * direction
                speed_y = randint(2, 5) * direction
        if asteroid.rect.top <= -200 or asteroid.rect.bottom >= SCREEN_HEIGHT+50:
            direction *= -1
            speed_x = randint(0, 5) * direction
            speed_y = randint(0, 5) * direction
            if speed_x == 0 and speed_y == 0:
                speed_x = randint(2, 5) * direction
                speed_y = randint(2, 5) * direction
        asteroid.rect.left += speed_x
        asteroid.rect.top += speed_y

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
            bg=pygame.image.load(resource_path('background.png')).convert()
            bg=pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
            bgX = 0
            bgX2 = bg.get_width()
            def redrawWindow():
                screen.blit(bg, (bgX,0))
                screen.blit(bg, (bgX2,0))
            bgRect=bg.get_rect()
            player.rect.bottom = tmpbottom
            player.rect.right = tmpright
            player2.rect.bottom = tmp2bottom
            player2.rect.right = tmp2right
            player.size = SCREEN_HEIGHT/6
            player2.size = SCREEN_HEIGHT/6
            asteroid.size = SCREEN_HEIGHT/4
            player.rect.update((player.rect.left,player.rect.top),(player.size,player.size))
            player2.rect.update((player2.rect.left,player2.rect.top),(player2.size,player2.size))
            bullet.rect.update((bullet.rect.left,bullet.rect.top),(player.size/2, player.size/10))
            bullet2.rect.update((bullet2.rect.left,bullet2.rect.top),(player2.size/2, player2.size/10))
            asteroid.rect.update((asteroid.rect.left,asteroid.rect.top),(asteroid.size,asteroid.size))
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
                    menu.mainloop(surface)
            # Check for QUIT event. If QUIT, then set running to false.
            elif event.type == QUIT:
                exit()
        # Get the set of keys pressed and check for user input
        pressed_keys = pygame.key.get_pressed()

        # Update the player sprite based on user keypresses
        player.update(pressed_keys)
        player2.update(pressed_keys)
        deadship.update()
        deadship2.update()

        screen.fill((0, 0, 0))
        redrawWindow()
        bgX -= 1.5
        bgX2 -= 1.5
        if bgX < bg.get_width() * -1:
            bgX = bg.get_width()    
        if bgX2 < bg.get_width() * -1:
            bgX2 = bg.get_width()

        if bullet.exist==1:
            bullet.update()
            screen.blit(bullet.bulletrotation, bullet.rect)
        if bullet2.exist==1:
            bullet2.update()
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
        screen.blit(Info2S, (SCREEN_WIDTH/2,SCREEN_HEIGHT+30))
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(SCREEN_WIDTH/2+100, SCREEN_HEIGHT+40, 150, 20),0)
        pygame.draw.rect(screen, (238, 255, 0), pygame.Rect(SCREEN_WIDTH/2+100, SCREEN_HEIGHT+40, player2.boost*1.5, 20))

        # Draw the objects on the screen
        playerrotation = pygame.transform.rotate(player.image,player.angle)
        screen.blit(playerrotation, player.rect)
        player2rotation = pygame.transform.rotate(player2.image,player2.angle)
        screen.blit(player2rotation,player2.rect)
        if player.dead == 1:
            font = pygame.font.SysFont('agencyfb', 60)
            screen.blit(deadship.image, deadship.rect)
            playerLostText = font.render("Player 2 Wins!", True, (255,255,255),(0,0,0))
            screen.blit(playerLostText,(SCREEN_WIDTH/2-100,SCREEN_HEIGHT/2-25))
        if player2.dead == 1:
            font = pygame.font.SysFont('agencyfb', 60)
            screen.blit(deadship2.image, deadship2.rect)
            player2LostText = font.render("Player 1 Wins!", True, (255,255,255),(0,0,0))
            screen.blit(player2LostText,(SCREEN_WIDTH/2-100,SCREEN_HEIGHT/2-25))
        screen.blit(asteroid.image, asteroid.rect)
            
        # Update the display
        pygame.display.flip()
        clock = pygame.time.Clock()
        clock.tick(360)

def how_to_play():
    font = pygame.font.SysFont('agencyfb', 30)
    from pygame.locals import (
        K_ESCAPE,
        KEYDOWN,
        QUIT
    )
    pygame.init()
    running = True
    while running:
        screen = pygame.display.set_mode((800, 600))
        screen.fill((0,0,0))
        line = font.render('How to Play', True, (255,255,255), (0,0,0))
        line1 = font.render('Each spaceship has 5 lives.', True, (255,255,255),(0,0,0))
        line2 = font.render('Use the arrow keys and ASDW keys to move the ships.', True, (255,255,255),(0,0,0))
        line3 = font.render('To shoot the other ship, press the respective alt keys.', True, (255,255,255),(0,0,0))
        line4 = font.render('Watch out for asteroids! The last one standing wins!', True, (255,255,255),(0,0,0))
        line5 = font.render('Press the escape key to return to the main menu.', True, (255,255,255),(0,0,0))
        screen.blit(line, (345, 0))
        screen.blit(line1, (275, 100))
        screen.blit(line2, (150, 200))
        screen.blit(line3, (145, 300))
        screen.blit(line4, (150, 400))
        screen.blit(line5, (175, 500))
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    menu.mainloop(surface)
            elif event.type == QUIT:
                exit()
        pygame.display.flip()

def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception: base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

pygame.mixer.init()
mixer.music.load(resource_path('BackgroundMusic.wav'))
mixer.music.play(-1)
pygame.init()
surface = pygame.display.set_mode((800,600))
menu = pygame_menu.Menu('AT-Spaceships', 800, 600, theme=pygame_menu.themes.THEME_BLUE)
menu.add.button('Play', start_the_game)
menu.add.button('How to Play', how_to_play)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)
