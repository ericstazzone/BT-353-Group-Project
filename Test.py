
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
    

class Player(pygame.sprite.Sprite):
## Would utilize this class for player movement and all things related to the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("square1.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect=self.image.get_rect()
        self.mask=pygame.mask.from_surface(self.image)
        self.x = 50
        self.y = 50
  
        
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


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self,obstacles)
        self.x=200
        self.y=200
        self.ball=pygame.image.load("square3.png") 
        self.ball = pygame.transform.scale(self.ball, (40, 40))
        self.rect=self.ball.get_rect()
        self.mask=pygame.mask.from_surface(self.ball)  

    def draw(self):
        screen.blit(self.ball,(self.x,self.y))    

    
    
##sprite movement test below
pygame.init()
clock = pygame.time.Clock()
size = 1000,750
screen = pygame.display.set_mode(size,0,32) #DISPLAY=pygame.display.set_mode((800,600)) #creates the display. width of 800 and length of 600
pygame.display.set_caption('The Impossible Game')
player = Player()
obstacles=pygame.sprite.Group()
ball=Ball()
obstacles.add(ball)

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
    player.draw()
    ball.draw()
        

    ##event control, move to player class
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
    
    if(pygame.sprite.spritecollide(player,obstacles,False,pygame.sprite.collide_mask)):
        print("hello")
    #refresh display
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
