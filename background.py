import pygame


from pygame.locals import *


pygame.init()

width = 800
height = 600
window = pygame.display.set_mode((width,height))
bg_img = pygame.image.load('background.png')
bg_img = pygame.transform.scale(bg_img,(width,height))

i = 0

running = True

while running:
        window.fill((0,0,0))
        window.blit(bg_img,(i,0))
        window.blit(bg_img,(width+i,0))
        if(i==-width):
                window.blit(bg_img,(width+i,0))
                i=0
        i-=0.05
        for event in pygame.event.get():
                if event.type == QUIT:
                        running = False
        pygame.display.update()
pygame.quit()
