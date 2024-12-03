import pygame
from pygame.locals import*

import sys

pygame.init()
X = 1440
Y = 800

scrn = pygame.display.set_mode((X, Y))
pygame.display.set_caption('image')

imparr= [pygame.image.load("Red_Bird.png").convert(), 
         pygame.image.load("Yellow_Bird.png").convert()]

rects=[]
for img in imparr: 
    rect = img.get_rect() 
    rect.center = (X//2, Y//2) 
    rects.append(rect)

drag=[False,False]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if rects[0].collidepoint(event.pos):
                drag[0]= True
                mouse_x, mouse_y = event.pos
                offset_x = rects[0].x - mouse_x
                offset_y = rects[0].y - mouse_y
            elif rects[1].collidepoint(event.pos):
                drag[1]= True
                mouse_x, mouse_y = event.pos
                offset_x = rects[1].x - mouse_x
                offset_y = rects[1].y - mouse_y
        elif event.type == pygame.MOUSEBUTTONUP:
            drag[0] = False
            drag[1] = False
        elif event.type == pygame.MOUSEMOTION:
            if drag[0]:
                mouse_x, mouse_y = event.pos
                rects[0].x = mouse_x + offset_x
                rects[0].y = mouse_y + offset_y
            elif drag[1]:
                mouse_x, mouse_y = event.pos
                rects[1].x = mouse_x + offset_x
                rects[1].y = mouse_y + offset_y

    # Fill the screen with a color
    scrn.fill((255, 255, 255))

    # Draw the images
    scrn.blit(imparr[0], rects[0])
    scrn.blit(imparr[1], rects[1])

    # Update the display
    pygame.display.flip()
            
