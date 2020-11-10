
## In order to use pygame, it will need to be installed on your computers
## We could do it with classes or we could do it with just all functions
## Example of a class we could use
##class Player:

import pygame, sys
from pygame.locals import *

class Wall(object):
    def __init__(self,pos):
        self.rect=pygame.Rect(pos[0],pos[1],50,50)
class Key():
    def __init__(self,pos):
        pass
        #import image here
        # set the x and y 
        #update function
class Traps():
    def __init__(self,pos):
        pass
        #do the same thing as Player and Key.
        #make sure to set the x and y 
        #update function
       

class Player():
## Would utilize this class for player movement and all things related to the player
    def __init__(self,pos):
        self.images = []
        image1 = pygame.image.load('images/square1.png')
        image2 = pygame.image.load('images/square2.png')
        image3 = pygame.image.load('images/square3.png')
        self.images.append(image1)
        self.images.append(image2)
        self.images.append(image3)
        self.index = 0
        self.image = self.images[self.index]
        #self.image_b=self.image.get_rect()
        #self.image = pygame.transform.scale(image, (50, 50))
        #image = pygame.image.load('square1.png')
        #self.image = image
        self.x = pos[0]
        self.y = pos[1]
        self.counter = 0


    def update(self):
        self.index += 1
        if self.index >= 4:
            self.counter += 1
            self.index = 0
        if self.counter >= len(self.images):
            self.index = 0
            self.counter = 0
        self.image = self.images[self.counter]
        self.image = pygame.transform.scale(self.image, (40, 40))
        
    ## Player Movement
    def movex(self, n):
        if not self.wallCollide(n, 0):
            self.x += n
    def movey(self, n):
        if not self.wallCollide(0, n):
            self.y += n
    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def wallCollide(self, xsteps, ysteps):
        r = Rect(self.x+xsteps, self.y+ysteps, 40, 40)
        return r.collidelist(walls) != -1

    def obstacleCollide(self,rectlist):
        r = Rect(self.x, self.y,25, 25)
        if r.collidelist(rectlist) !=-1:
            sys.exit()
             

    
    

##sprite movement test below
pygame.init()
clock = pygame.time.Clock()
size = 1000,750
screen = pygame.display.set_mode(size,0,32) #DISPLAY=pygame.display.set_mode((800,600)) #creates the display. width of 800 and length of 600
pygame.display.set_caption('The Impossible Game')

#setting the level to 1
currentbox=0


#making the boundaries
boxes = [[
    "WWWWWWWWWWWWWWWW WWW",
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
    "W P   W        W    ",
    "WWWWWWWWWWWWWWWWWWWW",
    ],
    [
    "WWWWWWWWWWWWWWWW WWW",
    "W                  W",
    "W  WWWWWWwwwwwwww  W",
    "W   WWWW      wW   W",
    "W   W  w      WWWW W",
    "W WWW  WWWW   www wW",
    "W         W W  w   W",
    "W   W     W   WWWwWW",
    "W   WWW WWW   W W  W",
    "W     W   W   W W  W",
    "WWW   W   WWWWW W  W",
    "W W      WW        W",
    "W W   WWWW   WWW   W",
    "W     W        W   ",
    "WWWWWWWWWWWWWWWWPWWW",

    ]]


    #looping through the string above to get it set up for drawing. Creating rectangle objects
def load_box(box):
    walls=[]
    x = y = 0
    for row in boxes[box]:
        for col in row:
            if col == "W":
                walls.append(Wall((x, y)))
            if col=="P":
                player=Player((x,y))
            x +=50
        y += 50
        x = 0
    return walls,player





walls,player=load_box(currentbox)

loop = True
#running the game
while loop:
    #making the background white
    screen.fill(Color("white"))

    #looping through the walls created to actually creat the rectangles

    #for the y coordinate when it hits the top of the opening, it transports to the box #1
    if currentbox==0 and player.x>=800 and player.x<=850 and player.y==0:
        currentbox=1
        walls,player=load_box(currentbox)
    
    #considering the event when player decides go back to box #0
    #doesn't work if I want to go back and forth
    if currentbox==1 and player.x>=800 and player.x<=850 and player.y==750:
        currentbox=0
        walls,player=load_box(currentbox)
        player.x=800
        player.y=30
    
    for wall in walls:
        pygame.draw.rect(screen, Color("blue"), wall.rect)


    player.draw()

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
