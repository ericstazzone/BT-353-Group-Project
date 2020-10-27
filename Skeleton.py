
## In order to use pygame, it will need to be installed on your computers
## We could do it with classes or we could do it with just all functions
## Example of a class we could use
##class Player:
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
    if key[pygame.K_w]:
        y -= 5
    elif key[pygame.K_a]: 
        x -= 5
    if key[pygame.K_s]: 
        y += 5
    elif key[pygame.K_d]: 
        x += 5

    
    pygame.display.flip()
    clock.tick(120)
    screen.fill((0,0,0))
pygame.quit()