<<<<<<< HEAD
=======
## In order to use pygame, it will need to be installed on your computers
>>>>>>> c0ba76b77b2b9a9c7930960ea1e2019514643f7a

## In order to use pygame, it will need to be installed on your computers
## We could do it with classes or we could do it with just all functions
## Example of a class we could use
##class Player:

import pygame, sys
from pygame.locals import *

def main():
    pygame.init()

    
    DISPLAY=pygame.display.set_mode((800,600)) #creates the display. width of 800 and length of 600

 
    #making the background white
    DISPLAY.fill(Color("white"))

    #making the boundaries
    pygame.draw.rect(DISPLAY,Color("red"),(0,0,75,75))   #start place
    pygame.draw.rect(DISPLAY,Color("green"),(725,525,75,75))   #finish 
    pygame.draw.rect(DISPLAY,Color("blue"),(75,0,30,300))
    pygame.draw.rect(DISPLAY,Color("blue"),(0,400,250,30))
    

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

main()
class Player:
## Would utilize this class for player movement and all things related to the player
    ##pass

##sprite movement test below
import pygame
from pygame.locals import *
 
pygame.init()
clock = pygame.time.Clock()
size = 960, 540 
screen = pygame.display.set_mode(size,0,32)
pygame.display.set_caption('The Impossible Game')
x, y = 0,0
 
sprite = pygame.image.load(r'C:\Users\essta\Documents\GitHub\BT-353-Group-Project\BT-353-Group-Project\square1.png')
sprite = pygame.transform.scale(sprite, (100,100))
loop = True
while loop:
    screen.blit(sprite,(x,y))
 
    for event in pygame.event.get():
        if event.type==QUIT:
            loop = False
    key = pygame.key.get_pressed()
    if key[pygame.K_w] or key[pygame.K_UP]:
        y += 5
    elif key[pygame.K_a] or key[pygame.K_LEFT]: 
        x -= 5
    if key[pygame.K_s] or key[pygame.K_DOWN]: 
        y -= 5
    elif key[pygame.K_d] or key[pygame.K_RIGHT]: 
        x += 5

    
    pygame.display.flip()
    clock.tick(120)
    screen.fill((0,0,0))
pygame.quit()