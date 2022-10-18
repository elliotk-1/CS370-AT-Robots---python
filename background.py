import pygame


from pygame.locals import *


pygame.init()

time = 60
width = 600
height = 600
bg_width = 1560
bg_height = 1000
screen = pygame.display.set_mode((width,height))
bg_img = pygame.image.load('background.png')
x = 0
y = 0

clock = pygame.time.Clock()

while True:
        clock.tick(time)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
                x -= 5
        if keys[pygame.K_RIGHT]:
                x += 5
        if keys[pygame.K_UP]:
                y -= 5
        if keys[pygame.K_DOWN]:
                y += 5
        screen.blit(bg_img, (-x, -y))
        if(x<0):
                screen.blit(bg_img, (bg_width,y))
                x=bg_width
        if(x>bg_width):
                screen.blit(bg_img, (0,y))
                x=0
        if(y<0):
                screen.blit(bg_img,(x,bg_height))
                y=bg_height
        if(y>bg_height):
                screen.blit(bg_img, (x, 0))
                y=0

        pygame.display.update()