import pygame
pygame.init()
import time
import random
import os
import numpy as np

# Creating Variables for the length and width of our screen
HEIGHT = 800
WIDTH = 1200

# Red's starting positions
position_x = 50
position_y = HEIGHT - 100

velocity_x = 15
velocity_y = -15

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

#notsure what is better but im making the pigs as arrays since they have mutli states for the armored pig- Hector 
Armored_pig= [pygame.image.load(os.path.join("Characters","Armored Pig.png")), pygame.image.load(os.path.join("Characters","Damaged Armored Pig.png"))]
King_pig=pygame.image.load(os.path.join("Characters","King Pig.png"))
Moustache_pig= [pygame.image.load(os.path.join("Characters","Moustache Pig.png")), pygame.image.load(os.path.join("Characters","Sleepy Pig.pmg"))]
Norm_pig==pygame.image.load(os.path.join("Characters","Normal Pig.png"))

# Arrays for all the information 
birds = np.array([Red,Baby_bird,Bomb,Big_bird,Boomerang,Egg_man,Chuck])
birds_height = np.array([36,24,65,74,57,70,44])
birds_width = np.array([36,24,47,77,76,62,45])
birds_flight_time = np.array([4])

# This will give you a random bird
bird_select = random.randint(0,(len(birds)-1))

# Here are some variables that use the module time. They will be used later to constantly update the game
FPS = 60
run = True
clock = pygame.time.Clock()

# Sets the screen color to black
screen.fill((0, 0, 0))

# Tells python the size of our objects
bird = pygame.transform.scale(birds[bird_select], (birds_width[bird_select], birds_height[bird_select]))
Back_ground1 = pygame.transform.scale(Back_ground1, (WIDTH,HEIGHT))

# Prints our Space Ship on the screen
screen.blit(Back_ground1, (0,0))
screen.blit(birds[bird_select], (position_x, position_y))


""""
hi, it's me, Devin.
I've commented out this code since we've added more variables to make the physics work
trying to do this in a function is nice to split the code into parts
but *in my opinion*, it's kind of a mess due to scope

in the future, look into creating a bird Object if you want to organize the code better
"""

"""
def move_bird(keys, bird_select, position_x, position_y, velocity_x, velocity_y):
    if keys[pygame.K_LEFT] and position_x > 0:
        position_x -= 2 
    if keys[pygame.K_RIGHT] and position_x < WIDTH - birds_width[bird_select]: 
        position_x += 2
    if keys[pygame.K_UP] and position_y > 0:  
        position_y -= 2
    if keys[pygame.K_DOWN] and position_y < minimum_height - birds_height[bird_select]: 
        position_y += 2
    velocity_y += 1

    position_x += velocity_x
    position_y += velocity_y
    return position_x, position_y
"""

def get_random_bird():
    bird_select = random.randint(0, (len(birds) - 1))
    bird = pygame.transform.scale(birds[bird_select], (birds_width[bird_select], birds_height[bird_select]))
    return bird_select, bird

bird_select, bird = get_random_bird()

while run:
    # Will update the game certain times a second, in this case 120 times
    clock.tick(FPS)

    # Saves the pressed key
    keys = pygame.key.get_pressed()

    # Check if the bird is used or dies (example condition, you can replace it with actual game logic)
    if keys[pygame.K_SPACE]:  # Example condition to change the bird
        bird_select, bird = get_random_bird()

    #position_x, position_y = move_bird(keys, bird_select, position_x, position_y, velocity_x, velocity_y)

    # UPDATING GAME STATE

    # change bird velocity
    velocity_y += 0.4

    # change bird position
    position_x += velocity_x
    position_y += velocity_y

    
    screen.blit(Back_ground1, (0,0))
    screen.blit(bird, (position_x, position_y))

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
