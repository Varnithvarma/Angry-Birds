import pygame
pygame.init()
import time
import random
import os
import numpy as np

# Creating Variables for the length and width of our screen
HEIGHT = 800
WIDTH = 1200

# Red's starting positions and its size
Red_draw_height = (HEIGHT/2) 
Red_draw_width = (WIDTH/2) 

# Minimum height for map 1
minimum_height = 697

# Set up the drawing window
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# Importing the background
Back_ground1 = pygame.image.load(os.path.join("Backgrounds", "Background1.jpg"))
Back_ground2 = pygame.image.load(os.path.join("Backgrounds", "Background2.jpg"))

# Importing our Birds
Red = pygame.image.load(os.path.join("Characters", "Red.png"))
Baby_bird = pygame.image.load(os.path.join("Characters", "Baby Bird.png"))
Bomb = pygame.image.load(os.path.join("Characters", "Bomb.png"))
Big_bird = pygame.image.load(os.path.join("Characters", "Big Guy.png"))
Boomerang = pygame.image.load(os.path.join("Characters", "Boomerang.png"))
Egg_man = pygame.image.load(os.path.join("Characters", "Egg man.png"))
Chuck = pygame.image.load(os.path.join("Characters", "Chuck.png"))

# Arrays for all the information 
birds = np.array([Red,Baby_bird,Bomb,Big_bird,Boomerang,Egg_man,Chuck])
birds_height = np.array([36,24,65,74,57,70,44])
birds_width = np.array([36,24,47,77,76,62,45])
birds_flight_time = np.array([4])

# This will give you a random bird
bird_select = random.randint(0,(len(birds)-1))

# Here are some variables that use the module time. They will be used later to constantly update the game
FPS = 120
run = True
clock = pygame.time.Clock()

# Sets the screen color to black
screen.fill((0, 0, 0))

# Tells python the size of our objects
bird = pygame.transform.scale(birds[bird_select], (birds_width[bird_select], birds_height[bird_select]))
Back_ground1 = pygame.transform.scale(Back_ground1, (WIDTH,HEIGHT))

# Prints our Space Ship on the screen
screen.blit(Back_ground1, (0,0))
screen.blit(birds[bird_select], (Red_draw_width, Red_draw_height))


while run:
    # Will update the game certain times a second, in this case 120 times
    clock.tick(FPS)

    # Saves the pressed key
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and Red_draw_width > 0:
        screen.blit(Back_ground1, (0,0))
        Red_draw_width -= 2 
        screen.blit(birds[bird_select], (Red_draw_width, Red_draw_height))

    if keys[pygame.K_RIGHT] and Red_draw_width < WIDTH - birds_width[bird_select]: 
        screen.blit(Back_ground1, (0,0))
        Red_draw_width += 2
        screen.blit(birds[bird_select], (Red_draw_width, Red_draw_height))
         
    if keys[pygame.K_UP] and Red_draw_height > 0:  
        screen.blit(Back_ground1, (0,0))
        Red_draw_height -= 2
        screen.blit(birds[bird_select], (Red_draw_width, Red_draw_height))
          
    if keys[pygame.K_DOWN] and Red_draw_height < minimum_height - birds_height[bird_select]: 
        screen.blit(Back_ground1, (0,0)) 
        Red_draw_height += 2
        screen.blit(birds[bird_select], (Red_draw_width, Red_draw_height))

    # Did the user click the window close button?
    for event in pygame.event.get():

        # If the quit button is pressed, the code will turn off
        if event.type == pygame.QUIT:
            # Turns run to false
            run = False

            # Breaks out of the loop
            break
    
    # Redraws the window, updating the window
    def redraw_window():
        pygame.display.update()

    # Flip the display
    pygame.display.flip()
