
## In order to use pygame, it will need to be installed on your computers
## We could do it with classes or we could do it with just all functions
## Example of a class we could use
##class Player:

import pygame, sys
from pygame.locals import *

class Player():
## Would utilize this class for player movement and all things related to the player
    def __init__(self):
        image = pygame.image.load('square1.png')
        image = pygame.transform.scale(image, (50, 50))
        self.image = image
        self.x = 0
        self.y = 0
        
    ## Player Movement
    def movex(self, n):
        self.x += n
    def movey(self, n):
        self.y += n

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
    

##sprite movement test below
pygame.init()
clock = pygame.time.Clock()
size = 800,600 
screen = pygame.display.set_mode(size,0,32) #DISPLAY=pygame.display.set_mode((800,600)) #creates the display. width of 800 and length of 600
pygame.display.set_caption('The Impossible Game')
player = Player()
loop = True
#running the game
while loop:
    #making the background white
    screen.fill(Color("white"))
    #making the boundaries
    pygame.draw.rect(screen,Color("red"),(0,0,75,75))   #start place
    pygame.draw.rect(screen,Color("green"),(725,525,75,75))   #finish 
    pygame.draw.rect(screen,Color("blue"),(75,0,30,300))
    pygame.draw.rect(screen,Color("blue"),(0,400,250,30))
    player.draw(screen)
    ##event control, move to player class
    for event in pygame.event.get():
        if event.type==QUIT:
            loop = False
    key = pygame.key.get_pressed()
    if key[pygame.K_w] or key[pygame.K_UP]:
        player.movey(-5)
    elif key[pygame.K_a] or key[pygame.K_LEFT]: 
        player.movex(-5)
    if key[pygame.K_s] or key[pygame.K_DOWN]: 
        player.movey(5)
    elif key[pygame.K_d] or key[pygame.K_RIGHT]: 
        player.movex(5)
    #refresh display
    pygame.display.flip()
    clock.tick(120)
pygame.quit()
