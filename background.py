import pygame


from pygame.locals import *


pygame.init()

time = 60
width = 800
height = 600
bg_width = 1760
bg_height = 1000
screen = pygame.display.set_mode((width,height))
bg_img = pygame.image.load('background.png')
#bg_img = pygame.transform.scale(bg_img,(width,height))

#screen_size = screen.get_size()
#bg_size = bg_img.get_size()
#bg_x = (bg_size[0]-screen_size[0]) // 2
#bg_y = (bg_size[1]-screen_size[1]) // 2
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
        #bg_x = max(0, min(bg_size[0]-screen_size[0], bg_x))
        #bg_y = max(0, min(bg_size[1]-screen_size[1], bg_y))
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

        pygame.display.flip()

#i = 0

#running = True

#while running:
        #window.fill((0,0,0))
        #window.blit(bg_img,(i,0))
        #window.blit(bg_img,(width+i,0))
        #if(i==-width):
                #window.blit(bg_img,(width+i,0))
                #i=0
        #i-=0.05
        #for event in pygame.event.get():
                #if event.type == QUIT:
                        #running = False
        #pygame.display.update()
pygame.quit()
