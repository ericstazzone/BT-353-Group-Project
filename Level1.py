import pygame, sys
from pygame.locals import *

class Wall(object):
    def __init__(self,pos):
        self.rect=pygame.Rect(pos[0],pos[1],50,50)

class Key():
    ## Images
    blackout = pygame.image.load('images/blackout.png') 
    blackout = pygame.transform.scale(blackout, (500,390))
    key = pygame.image.load('images/key1.png')
    key = pygame.transform.scale(key, (50, 50))
        
    ## Key Variables
    keyscollected = 0
    keys = [False, False]
    keycoors0 = [350, 295]
    keycoors1 = [900, 400]
    keycoors = [keycoors0, keycoors1]
    key0rect = Rect(keycoors[0][0], keycoors[0][1], 50, 50)
    key1rect = Rect(keycoors[1][0], keycoors[1][1], 50, 50)
    keysrect = [key0rect, key1rect]
                                
    def toggleBox0(self):
        if not self.keys[0]:
            screen.blit(self.key, self.keycoors[0])
        
    def toggleBox1(self):
        if not self.keys[1]:
            screen.blit(self.key, self.keycoors[1])

    def obtainKey(self, playerx, playery):
        temp = Rect(playerx, playery, 20, 20)
        if temp.colliderect(self.keysrect[0]) == 1:
            self.keys[0] = True
        if temp.colliderect(self.keysrect[1]) == 1:
            self.keys[1] = True


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
             
pygame.init()
clock = pygame.time.Clock()
size = 1000,750
screen = pygame.display.set_mode(size,0,32)
pygame.display.set_caption('The Impossible Game')
currentbox=0                                                        #setting the level to 1
boxes = [[                                                          #making the boundaries
    "WWWWWWWWWWWWWWWW WWW",
    "W   W W WWWWWWWW WWW",
    "W           WWWW WWW",
    "W   W W WWW WW     W",
    "WWW WWWWWWW WWWW WWW",
    "W   WWW     WWW    W",
    "W WWWWW WWWWWWWWW WW",
    "W   WWWWWWWWWW     W",
    "W W         WWW WWWW",
    "W W  W WW W W     WW",
    "W W  W WW   WWWW WWW",
    "W   W   WW WWWWW WWW",
    "W   WW WWW WWWW   WW",
    "W P W               ",
    "WWWWWWWWWWWWWWWWWWWW", 
    ],
    [
    "WWW WWWWWWWWWWWWWWWW",
    "WWW             WWWW",
    "WWWWWWWWW WW  WWWWWW",
    "W            WWWWWWW",
    "W WWWWWWWWWWWW     W",
    "W W WWW   WWWW WWW W",
    "W       W  W       W",
    "WWW WWWWWW W  W  W W",
    "WWWW   WWW W     W W",
    "W    W     W WWW WWW",
    "W W WW W WWW  W  WWW",
    "W   WW   WWW     WWW",
    "W WWWWWWWWWW  W  WWW",
    "W                WWW",
    "WWWWWWWWWWWWWWWWPWWW",
    ],
    [
    "WWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWW         WWW",
    "WWWWWWWW         WWW",
    "WWWWWWWW         WWW",
    "WWW              WWW",
    "WWW WWWW         WWW",
    "WWW WWWW         WWW",
    "WWW    W         WWW",
    "WWWWWWWW         WWW",
    "WWW              WWW",
    "WWW WWWWW       WWWW",
    "WW   WWWWW     WWWWW",
    "W     WWWWW   WWWWWW",
    "WW   WWWWWWW        ",
    "WWWPWWWWWWWWWWWWWWWW",
    ],
    [
    "WWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWW     ",
    "WWWWWWWWWWWWWWW WWWW",
    "WWW         WWW WWWW",
    "WWW    W    WW   WWW",
    "WWW    W    WWW WWWW",
    "WWW    W    WWW  WWW",
    "WWW   WWW   WWWW WWW",
    "WWW   WWW   WWWW WWW",
    "WWW   WWW   WWWW   W",
    "WWW   WWW   WWWW   W",
    "WWW    W    WWWW   W",
    "WWW    W    WWWWWW W",
    "P      W    WWWWWW W",
    "WWWWWWWWWWWWWWWWWW W",
    ]]
 
def load_box(box):                                                  #looping through the string above to get it set up for drawing. Creating rectangle objects
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
keys = Key()

loop = True                                                         #running the game
while loop:
    screen.fill(Color("white"))                                     #making the background white

    if currentbox==0 and player.x>=800 and player.x<=850 and player.y==0:#for the y coordinate when it hits the top of the opening, it transports to the box #1
        currentbox=1
        walls,player=load_box(currentbox)
        
    if currentbox==1 and player.x>=800 and player.x<=850 and player.y==750:#considering the event when player decides go back to box #0
        currentbox=0
        walls,player=load_box(currentbox)
        player.x=800
        player.y=30

    for wall in walls:                                              #looping through the walls created to actually creat the rectangles
        pygame.draw.rect(screen, Color("blue"), wall.rect)

    if currentbox == 0:         ## generating enemies and keys for box 0
        keys.toggleBox0()

    if currentbox == 1:         ## generating enemies and keys for box 1
        keys.toggleBox1()

    player.draw()
    player.update()

    keys.obtainKey(player.x, player.y)

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
    pygame.display.flip()                                           #refresh display
    clock.tick(30)                                                  #fps
pygame.quit()                                                       
