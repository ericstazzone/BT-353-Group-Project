
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

## Obstacles
class Obstacles:
## Would utilize this class for player movement and all things related to the player
    ## Obstacle Class

    ## Circle Obstacles
    circle1 = pygame.image.load('circle1.png') 
    circle1 = pygame.transform.scale(circle1, (50,50))
    circle2 = pygame.image.load('circle1.png')
    circle2 = pygame.transform.scale(circle2, (50,50))
    circle3 = pygame.image.load('circle1.png')
    circle3 = pygame.transform.scale(circle3, (50,50))
    circle4 = pygame.image.load('circle1.png')
    circle4 = pygame.transform.scale(circle4, (50,50))
    
    coors1 = [600, 50]
    coors2 = [400, 50]
    coors3 = [650, 300]
    coors4 = [50, 250]
    movespeed = 2
    check1 = 0
    check2 = 0
    check3 = 0
    check4 = 0
    circle1rect = Rect(coors1[0], coors1[1], 10, 10)
    circle2rect = Rect(coors2[0], coors2[1], 10, 10)
    circle3rect = Rect(coors3[0], coors3[1], 10, 10)
    circle4rect = Rect(coors4[0], coors4[1], 10, 10)
    circlesrect=[circle1rect,circle2rect,circle3rect,circle4rect]

    ## Inputs are (coors # of the enemey, 0 for horizontal and y for vertical, minimum coordinate value, maximum coordinate value, check value)

    def movement1(self):
        if self.check1 == 1: ## moving right
            self.coors1[0] += self.movespeed
        else: ## moving left
            self.coors1[0] -= self.movespeed
        if self.coors1[0] > 900: ## how far right the sprite goes
            self.check1 = 0
        if self.coors1[0] < 600: ## how far left the sprite goes
            self.check1 = 1

    def movement2(self):
        if self.check2 == 1: ## moving right
            self.coors2[1] += self.movespeed
        else: ## moving left
            self.coors2[1] -= self.movespeed
        if self.coors2[1] > 200: ## how far right the sprite goes
            self.check2 = 0
        if self.coors2[1] < 50: ## how far left the sprite goes
            self.check2 = 1

    def movement3(self):
        if self.check3 == 1: ## moving right
            self.coors3[0] += self.movespeed
        else: ## moving left
            self.coors3[0] -= self.movespeed
        if self.coors3[0] > 900: ## how far right the sprite goes
            self.check3 = 0
        if self.coors3[0] < 650: ## how far left the sprite goes
            self.check3 = 1

    def movement4(self):
        if self.check4 == 1: ## moving right
            self.coors4[1] += self.movespeed
        else: ## moving left
            self.coors4[1] -= self.movespeed
        if self.coors4[1] > 450: ## how far right the sprite goes
            self.check4 = 0
        if self.coors4[1] < 250: ## how far left the sprite goes
            self.check4 = 1    

    def draw(self):
        screen.blit(self.circle1, self.coors1)
        screen.blit(self.circle2, self.coors2)
        screen.blit(self.circle3, self.coors3)
        screen.blit(self.circle4, self.coors4)

    

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
        #self.image_b=self.image.get_rect()
        #self.image = pygame.transform.scale(image, (50, 50))
        #image = pygame.image.load('square1.png')
        #self.image = image
        self.resetPosition()
        self.deaths = 0
        self.counter = 0

    def resetPosition(self):
        self.x = 50
        self.y = 50

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
            self.kill()
    
    def kill(self):
        self.deaths += 1
        self.resetPosition()        
       

    
    

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




obstacles = Obstacles()

loop = True
#running the game
while loop:
    #making the background white
    screen.fill(Color("white"))

    #looping through the walls created to actually creat the rectangles
    for wall in walls:
        pygame.draw.rect(screen, Color("blue"), wall.rect)
    
    pygame.draw.rect(screen, (255, 0, 0), end_rect)
    player.draw()
    
    ##obstacles
    obstacles.movement1()
    obstacles.movement2()
    obstacles.movement3()
    obstacles.movement4()
    obstacles.draw()
    circle1rect = Rect(obstacles.coors1[0], obstacles.coors1[1], 15, 15)
    circle2rect = Rect(obstacles.coors2[0], obstacles.coors2[1], 15, 15)
    circle3rect = Rect(obstacles.coors3[0], obstacles.coors3[1], 15, 15)
    circle4rect = Rect(obstacles.coors4[0], obstacles.coors4[1], 15, 15)
    circlesrect=[circle1rect,circle2rect,circle3rect,circle4rect]
    player.obstacleCollide(circlesrect)



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
