## In order to use pygame, it will need to be installed on your computers

## We could do it with classes or we could do it with just all functions

## Example of a class we could use

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
    pass

