import pygame, sys
from pygame.locals import *

class Wall(object):
    def __init__(self,pos):
        self.rect=pygame.Rect(pos[0],pos[1],50,50)

class Key():
    ## Images
    blackout = pygame.image.load('images/blackout4.png') 
    blackout = pygame.transform.scale(blackout, (1050,800))
    key = pygame.image.load('images/key1.png')
    key = pygame.transform.scale(key, (50, 50))

    blackoutcoors = [0, -10]
    
    ## Key Variables
    keyscollected = 0
    keys = [False, False, False, False]
    keycoors0 = [350, 295]
    keycoors1 = [900, 400]
    keycoors2 = [300, 350]
    keycoors3 = [480, 600]
    keycoors = [keycoors0, keycoors1, keycoors2, keycoors3]
    key0rect = Rect(keycoors[0][0], keycoors[0][1], 50, 50)
    key1rect = Rect(keycoors[1][0], keycoors[1][1], 50, 50)
    key2rect = Rect(keycoors[2][0], keycoors[2][1], 50, 50)
    key3rect = Rect(keycoors[3][0], keycoors[3][1], 50, 50)
    keysrect = [key0rect, key1rect, key2rect, key3rect]
                                
    def toggleBox0(self):
        if not self.keys[0]:
            screen.blit(self.key, self.keycoors[0])
        
    def toggleBox1(self):
        if not self.keys[1]:
            screen.blit(self.key, self.keycoors[1])
        if not self.keys[0]:
            screen.blit(self.blackout, self.blackoutcoors)

    def toggleBox2(self):
        if not self.keys[2]:
            screen.blit(self.key, self.keycoors[2])
        if not self.keys[1]:
            screen.blit(self.blackout, self.blackoutcoors)

    def toggleBox3(self):
        if not self.keys[3]:
            screen.blit(self.key, self.keycoors[3])
        if not self.keys[0]:
            screen.blit(self.blackout, self.blackoutcoors)

    def obtainKey(self, playerx, playery, currentbox):
        temp = Rect(playerx, playery, 20, 20)
        if temp.colliderect(self.keysrect[0]) == 1 and currentbox == 0:
            self.keys[0] = True
        if temp.colliderect(self.keysrect[1]) == 1 and currentbox == 1:
            self.keys[1] = True
        if temp.colliderect(self.keysrect[2]) == 1 and currentbox == 2:
            self.keys[2] = True
        if temp.colliderect(self.keysrect[3]) == 1 and currentbox == 3:
            self.keys[3] = True


class Traps():
    def __init__(self,pos):
        self.images=[]
        image1=pygame.image.load('images/trapdoor1.1.png')
        image2=pygame.image.load('images/trapdoor1.2.png')
        image3=pygame.image.load('images/trapdoor1.3.png')
        image4=pygame.image.load('images/trapdoor2.1.png')
        image5=pygame.image.load('images/trapdoor3.png')
        image6=pygame.image.load('images/trapdoor4.1.png')
        image7=pygame.image.load('images/trapdoor5.1.png')
        image8=pygame.image.load('images/trapdoor5.2.png')
        image9=pygame.image.load('images/trapdoor5.3.png')
        image10=pygame.image.load('images/trapdoor4.2.png')
        image11=pygame.image.load('images/trapdoor3.png')
        image12=pygame.image.load('images/trapdoor2.2.png')
 
        self.images.append(image1)
        self.images.append(image2)
        self.images.append(image3)
        self.images.append(image4)
        self.images.append(image5)
        self.images.append(image6)
        self.images.append(image7)
        self.images.append(image8)
        self.images.append(image9)
        self.images.append(image10)
        self.images.append(image11)
        self.images.append(image12)
        self.index=0
        self.image=self.images[self.index]
        self.x=pos[0]
        self.y=pos[1]
        self.counter=0

    def update(self):
        self.index += 1
        if self.index >= 13:
            self.counter += 1
            self.index = 0
        if self.counter >= len(self.images):
            self.index = 0
            self.counter = 0
        self.image = self.images[self.counter]
        self.image = pygame.transform.scale(self.image, (50, 50))
        
    
    def draw(self):
        screen.blit(self.image, (self.x, self.y))
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
        self.startPos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.counter = 0
        self.deaths = 0

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
            return True
        return False

    def movey(self, n):
        if not self.wallCollide(0, n):
            self.y += n
            return True
        return False

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def wallCollide(self, xsteps, ysteps):
        r = Rect(self.x+xsteps, self.y+ysteps, 40, 40)
        return r.collidelist(walls) != -1

    def obstacleCollide(self,rectlist):
        r = Rect(self.x, self.y,25, 25)
        return r.collidelist(rectlist) != -1
    
    def kill(self):
        self.deaths += 1
        self.x, self.y = self.startPos

             
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
    "W   WWW  T  WWW    W",
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
    "W  T             WWW",
    "WWWWWWWWWWWWWWWWPWWW",
    ],
    [
    "WWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWW         WWW",
    "WWWWWWWW         WWW",
    "WWWWWWWW         WWW",
    "WWW T            WWW",
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
    "WWW       T WWW WWWW",
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
    ],
    [
    "WWWWWWWWWWWWWWWWWW W",
    "WWW        T     W W",
    "WWW W            W W",
    "WWW W            W W",
    "WWW W            W W",
    "W   WWWWWWWWWWWWWW W",
    "W WWWWWWWWWWWWWWW   ",
    "W WWWWWWWWWWWWWWW   ",
    "W WWWWWWWWWWWWWWW   ",
    "W WWWWWWWWWWWWWWW   ",
    "W W                 ",
    "W W WWWWWWWWWWWW WWW",
    "W W WWWWWWWWWWWW WWW",
    "W           WWWW WWW",
    "WWWWWWWWWWWWWWWWPWWW",
    ],
    [
    "WWWWWWWWWWWWWWWW WWW",
    "W WWWWWWWWWWWWWW WWW",
    "W WWWWWWWWWWWWWW WWW",
    "W T   WWWWWWWW     W",
    "WWW WWWWWWWWWWWW WWW",
    "WW   WW      WW   WW",
    "WWW WWW  WW  WWW WWW",
    "WW   WW  WW  WW   WW",
    "WWW WWW  WW  WWW WWW",
    "WW   WW  WW  WW   WW",
    "WWW WW  WWWW  WW WWW",
    "WWW W  WWWWWW  W WWW",
    "WWW   WWWWWWWW   WWW",
    "P    WWWWWWWWWW  WWW",
    "WWWWWWWWWWWWWWWWWWWW",
    ],
    [
    "WWWWWWWWWWWWWWWWWWWW",
    "P  WWWWWWWWWWWWWWWWW",
    "WW W W W W W W WWWWW",
    "WW    T            W",
    "WWWW W W W W W WWW W",
    "WWWWWWWWWWWWWWWWWW W",
    "W                  W",
    "W WWWWWWWWWWWWWWWWWW",
    "W                  W",
    "W WWWWWWWWWWWWWWWW W",
    "W WWWWWWWWWWWWWWWW W",
    "W WWWWWWWWWWWWWWWW W",
    "W WWWWWWWWWWWWWWWW W",
    "W                W W",
    "WWWWWWWWWWWWWWWWWW W",
    ],
    [
    "WWWWWWWWWWWWWWWWWWPW",
    "WWWWWWWWWWWWWWWWWW W",
    "WWWWWWWWWWWWWWWWWW W",
    "W  T               W",
    "W    WWWWWWWWWWW   W",
    "W    WWWWWWWWWWW   W",
    "W    WWWWWWWWWWW   W",
    "WWW W              W",
    "WWW WW             W",
    "WWW WWW            W",
    "WWW WWWW           W",
    "WWW WWWWW          W",
    "WWW WWWWWW         W",
    "WWW WWWWWW   WWWWWWW",
    "WWW WWWWWWWWWWWWWWWW",
    ],
    [
    "WWWPWWWWWWWWWWWWWWWW",
    "WWW WWWWWWWWWWWWWWWW",
    "WWW WWWWWWWWWWWWWWWW",
    "WWW              WWW",
    "WWW              WWW",
    "WWW       T      WWW",
    "WWW              WWW",
    "WWW                 ",
    "WWW              WWW",
    "WWW              WWW",
    "WWW              WWW",
    "WWW              WWW",
    "WWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWW",
    ]]
 
def load_box(box):                                                  #looping through the string above to get it set up for drawing. Creating rectangle objects
    walls=[]
    x = y = 0
    for row in boxes[box]:
        for col in row:
            if col == "W":
                walls.append(Wall((x, y)))
            if col=="T":
                trap=Traps((x,y))
            if col=="P":
                player=Player((x,y))
            x +=50
        y += 50
        x = 0
    return walls,player,trap

walls,player,trap=load_box(currentbox)
keys = Key()

died = False

loop = True                                                         #running the game
while loop:
    
    if died:
        player.kill()
        died = False
        currentbox = 0
        walls,player,trap=load_box(currentbox)
    
    screen.fill(Color("white"))                                     #making the background white

    if currentbox==0 and player.x>=800 and player.x<=850 and player.y==0:#for the y coordinate when it hits the top of the opening, it transports to the box #1
        currentbox=1
        walls,player,trap=load_box(currentbox)
    #considering the event when player decides go back to box #0 when in the first box   
    if currentbox==1 and player.x>=800 and player.x<=850 and player.y==750:
        currentbox=0
        walls,player,trap=load_box(currentbox)
        player.x=800
        player.y=30
    
    if currentbox==1 and player.x>=150 and player.x<=200 and player.y==0:
        currentbox=2
        walls,player,trap=load_box(currentbox)
    
    if currentbox==2 and player.x>=150 and player.x<=200 and player.y==750:
        currentbox=1
        walls,player,trap=load_box(currentbox)
        player.x=150
        player.y=30
    

    if currentbox==0 and player.y>=650 and player.y<=700 and player.x==1000:
        currentbox=3
        walls,player,trap=load_box(currentbox)

    if currentbox==3 and player.y>=650 and player.y<=700 and player.x<0:
        currentbox=0
        walls,player,trap=load_box(currentbox)
        player.x=950
        player.y=650
    

    for wall in walls:                                              #looping through the walls created to actually creat the rectangles
        pygame.draw.rect(screen, Color("blue"), wall.rect)

    trap.draw()
    trap.update()

    player.draw()
    player.update()

    if currentbox == 0:         ## generating enemies and keys for box 0
        keys.toggleBox0()

    if currentbox == 1:         ## generating enemies and keys for box 1
        keys.toggleBox1()

    if currentbox == 2:         ## generating enemies and keys for box 2
        keys.toggleBox2()

    if currentbox == 3:         ## generating enemies and keys for box 3
        keys.toggleBox3()

    keys.obtainKey(player.x, player.y, currentbox)

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
