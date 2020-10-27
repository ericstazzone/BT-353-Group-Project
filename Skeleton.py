
## In order to use pygame, it will need to be installed on your computers
## We could do it with classes or we could do it with just all functions
## Example of a class we could use
##class Player:

import pygame, sys
from pygame.locals import *

class Wall(object):
    def __init__(self,pos):
        walls.append(self)
        self.rect=pygame.Rect(pos[0],pos[1],50,50)

class Player():
## Would utilize this class for player movement and all things related to the player
    def __init__(self):
        self.images = []
        image1 = pygame.image.load('square1.png')
        image2 = pygame.image.load('square2.png')
        image3 = pygame.image.load('square3.png')
        self.images.append(image1)
        self.images.append(image2)
        self.images.append(image3)
        self.index = 0
        self.image = self.images[self.index]
        #self.image = pygame.transform.scale(image, (50, 50))
        #image = pygame.image.load('square1.png')
        #self.image = image
        self.x = 50
        self.y = 50
    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        self.image = pygame.transform.scale(self.image, (40, 40))
        
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
size = 1000,750
screen = pygame.display.set_mode(size,0,32) #DISPLAY=pygame.display.set_mode((800,600)) #creates the display. width of 800 and length of 600
pygame.display.set_caption('The Impossible Game')
player = Player()


#making the boundaries
walls=[]
level = [
"WWWWWWWWWWWWWWWWWWWW",
"W                  W",
"W         WWWWWW   W",
"W   WWWW       W   W",
"W   W        WWWW  W",
"W WWW  WWWW        W",
"W   W     W W      W",
"W   W     W   WWW WW",
"W   WWW WWW   W W  W",
"W     W   W   W W  W",
"WWW   W   WWWWW W  W",
"W W      WW        W",
"W W   WWWW   WWW   W",
"W     W    E   W   W",
"WWWWWWWWWWWWWWWWWWWW",
]


#looping through the string above to get it set up for drawing. Creating rectangle objects
x = y = 0
for row in level:
    for col in row:
        if col == "W":
            Wall((x, y))
        if col == "E":
            end_rect = pygame.Rect(x, y, 50, 50)
        x +=50
    y += 50
    x = 0






loop = True
#running the game
while loop:
    #making the background white
    screen.fill(Color("white"))
  
    #looping through the walls created to actually creat the rectangles
    for wall in walls:
        pygame.draw.rect(screen, Color("blue"), wall.rect)
    pygame.draw.rect(screen, (255, 0, 0), end_rect)
    player.draw(screen)
    ##event control, move to player class
    player.update()
    for event in pygame.event.get():
        if event.type==QUIT:
            loop = False
    key = pygame.key.get_pressed()
    if key[pygame.K_w] or key[pygame.K_UP]:
        player.movey(-10)
    elif key[pygame.K_a] or key[pygame.K_LEFT]: 
        player.movex(-10)
    if key[pygame.K_s] or key[pygame.K_DOWN]: 
        player.movey(10)
    elif key[pygame.K_d] or key[pygame.K_RIGHT]: 
        player.movex(10)
    #refresh display
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
