import pygame, sys
from pygame.locals import *
from pygame import mixer

class Wall(object):
    def __init__(self,pos):
        self.rect=pygame.Rect(pos[0],pos[1],50,50)
# class Tile(object):
#     def __init__(self,pos,block):
#         if(block=="top"):
#             self.image = pyame.image.load('images/walltop.png')

#         self.image=pygame.transform.scale(self.image, (50, 50)
        
#         self.x = pos[0]
#         self.y = pos[1]

#     def draw(self):
#         screen.blit(self.image, (self.x, self.y))


class Key():
    ## Images
    blackout = pygame.image.load('images/blackout4.png') 
    blackout = pygame.transform.scale(blackout, (1050,800))
    key = pygame.image.load('images/key1.png')
    key = pygame.transform.scale(key, (50, 50))

    blackoutcoors = [0, -10]
    
    ## Key Variables
    keys = [False, False, False, False, False, False, False, False]
    keycoors0 = [350, 295]
    keycoors1 = [900, 400]
    keycoors2 = [300, 350]
    keycoors3 = [480, 600]
    keycoors4 = [800, 200]
    keycoors5 = [50, 50]
    keycoors6 = [800, 650]
    keycoors7 = [250, 350]
    keycoors = [keycoors0, keycoors1, keycoors2, keycoors3, keycoors4, keycoors5, keycoors6, keycoors7]
    key0rect = Rect(keycoors[0][0], keycoors[0][1], 50, 50)
    key1rect = Rect(keycoors[1][0], keycoors[1][1], 50, 50)
    key2rect = Rect(keycoors[2][0], keycoors[2][1], 50, 50)
    key3rect = Rect(keycoors[3][0], keycoors[3][1], 50, 50)
    key4rect = Rect(keycoors[4][0], keycoors[4][1], 50, 50)
    key5rect = Rect(keycoors[5][0], keycoors[5][1], 50, 50)
    key6rect = Rect(keycoors[6][0], keycoors[6][1], 50, 50)
    key7rect = Rect(keycoors[7][0], keycoors[7][1], 50, 50)
    keysrect = [key0rect, key1rect, key2rect, key3rect, key4rect, key5rect, key6rect, key7rect]
                                
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
        if not self.keys[2]:
            screen.blit(self.blackout, self.blackoutcoors)

    def toggleBox4(self):
        if not self.keys[4]:
            screen.blit(self.key, self.keycoors[4])
        if not self.keys[5]:
            screen.blit(self.blackout, self.blackoutcoors)

    def toggleBox5(self):
        if not self.keys[5]:
            screen.blit(self.key, self.keycoors[5])
        if not self.keys[0]:
            screen.blit(self.blackout, self.blackoutcoors)

    def toggleBox6(self):
        count = 0
        for k in self.keys:
            if k:
                count += 1

        if not self.keys[6]:
            screen.blit(self.key, self.keycoors[6])
        if count < 6:
            screen.blit(self.blackout, self.blackoutcoors)

    def toggleBox7(self):
        if not self.keys[7]:
            screen.blit(self.key, self.keycoors[7])
        if not self.keys[6]:
            screen.blit(self.blackout, self.blackoutcoors)

    def toggleBox8(self):
        if not self.keys[7]:
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
        if temp.colliderect(self.keysrect[4]) == 1 and currentbox == 4:
            self.keys[4] = True        
        if temp.colliderect(self.keysrect[5]) == 1 and currentbox == 5:
            self.keys[5] = True
        if temp.colliderect(self.keysrect[6]) == 1 and currentbox == 6:
            self.keys[6] = True
        if temp.colliderect(self.keysrect[7]) == 1 and currentbox == 7:
            self.keys[7] = True

    def keysCollected(self):
        count = 0
        for k in self.keys:
            if k:
                count += 1
        return count

    def keyCountDisplay(self):
        count = self.keysCollected()
        image = pygame.image.load('images/key1.png')
        image = pygame.transform.scale(image, (40, 40))
        screen.blit(image, (945, 50))
        font = pygame.font.SysFont('Comic Sans MS', 25)
        text = font.render(str(count), True, (255, 255, 255))
        screen.blit(text, (981, 50))

## Obstacles
class Obstacles():
    ## Obstacle Class

    ## Enemies
    enemy = pygame.image.load('images/circle1.png') 
    enemy = pygame.transform.scale(enemy, (50,50))
 
    coors0 = [250, 550]
    coors1 = [250, 50]
    coors2 = [350, 100]
    coors3 = [700, 150]
    coors4 = [750, 250]
    coors5 = [750, 350]
    coors6 = [675, 450]
    coors7 = [450, 400]
    coors8 = [500, 500]
    movespeed = 2
    check = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    circle0rect = Rect(coors0[0], coors0[1], 10, 10)
    circle1rect = Rect(coors1[0], coors1[1], 10, 10)
    circle2rect = Rect(coors2[0], coors2[1], 10, 10)
    circle3rect = Rect(coors3[0], coors3[1], 10, 10)
    circle4rect = Rect(coors4[0], coors4[1], 10, 10)
    circle5rect = Rect(coors5[0], coors5[1], 10, 10)
    circle6rect = Rect(coors6[0], coors6[1], 10, 10)
    circle7rect = Rect(coors7[0], coors7[1], 10, 10)
    circle8rect = Rect(coors8[0], coors8[1], 10, 10)
    circlesrect=[circle0rect, circle1rect, circle2rect, circle3rect, circle4rect, circle5rect, circle6rect, circle7rect, circle8rect]

    def reset(self):
        self.coors0 = [250, 550]
        self.check = [0]

    def movement(self, enemy, enemycoors, direction, min, max):
        if self.check[enemy] == 1: ## moving right
            enemycoors[direction] += self.movespeed
        else: ## moving left
            enemycoors[direction] -= self.movespeed
        if enemycoors[direction] > max: ## how far right the sprite goes
            self.check[enemy] = 0
        if enemycoors[direction] < min: ## how far left the sprite goes
            self.check[enemy] = 1

    def draw1(self):
        screen.blit(self.enemy, self.coors0)
        screen.blit(self.enemy, self.coors1)
        screen.blit(self.enemy, self.coors2)
        screen.blit(self.enemy, self.coors3)
        screen.blit(self.enemy, self.coors4)
        screen.blit(self.enemy, self.coors5)
        screen.blit(self.enemy, self.coors6)    
        screen.blit(self.enemy, self.coors7)
        screen.blit(self.enemy, self.coors8)


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

    def displayDeaths(self):
        font = pygame.font.SysFont('Comic Sans MS', 35)
        text = font.render('Deaths: ' + str(self.deaths), True, (255, 0, 0))
        screen.blit(text, (400, -2))

             
pygame.init()
backgroundsound = mixer.music.load('song1_aLtZHmr9.wav')
mixer.music.play(-1)
clock = pygame.time.Clock()
size = 1000,750
screen = pygame.display.set_mode(size,0,32)
pygame.display.set_caption('The Impossible Game')
currentbox=0                                                        #setting the level to 1
boxes = [[                                                          #making the boundaries
    "WUUUUUUUUUUUUWWW WWW",
    "W   W W WWWWWWWW WWW",
    "W           WWWW WWW",
    "W   W W WWW WW  T  W",
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
def topbox(x,y):
    image = pygame.image.load('images/walltop.png')
    image=pygame.transform.scale(image, (50, 50))
    return image,x,y

 
def load_box(box):                                                  #looping through the string above to get it set up for drawing. Creating rectangle objects
    walls=[]
    tiles=[]
    i=0
    x = y = 0
    for row in boxes[box]:
        for col in row:
            if col == "W" or col=="U":
                walls.append(Wall((x, y)))
            if col=="U":
                image,corx,cory=topbox(x,y)
                tiles.append(image)
                tiles.append(int(corx))
                tiles.append(int(cory))

            if col=="T":
                trap=Traps((x,y))
            if col=="P":
                player=Player((x,y))
            x +=50
        y += 50
        x = 0
    return walls,player,trap,tiles
    
walls,player,trap,tiles=load_box(currentbox) 
keys = Key()

obstacles = Obstacles()

died = False

loop = True                                                         #running the game
pause = False
while loop:
    while pause:
        for event in pygame.event.get():
            if event.type == KEYUP and event.key == K_p:
                pause = False
    if died:
        player.kill()
        died = False
        currentbox = 0
        walls,player,trap=load_box(currentbox)
    
    screen.fill(Color("white"))                                     #making the background white


    if currentbox==0 and player.x>=800 and player.x<=850 and player.y==0:#for the y coordinate when it hits the top of the opening, it transports to the box #1
        currentbox=1
        walls,player,trap,tiles=load_box(currentbox)
    #considering the event when player decides go back to box #0 when in the first box   
    if currentbox==1 and player.x>=800 and player.x<=850 and player.y==750:
        currentbox=0
        walls,player,trap,tiles=load_box(currentbox)
        player.x=800
        player.y=30
    
    if currentbox==1 and player.x>=150 and player.x<=200 and player.y==0:
        currentbox=2
        walls,player,trap,tiles=load_box(currentbox)
    
    if currentbox==2 and player.x>=150 and player.x<=200 and player.y==750:
        currentbox=1
        walls,player,trap,tiles=load_box(currentbox)
        player.x=150
        player.y=30
    
    if currentbox==2 and player.y>=650 and player.y<=750 and player.x==1000:
        currentbox=3
        walls,player,trap,tiles=load_box(currentbox)
    
    if currentbox==3 and player.y>=650 and player.y<=750 and player.x<0:
        currentbox=2
        walls,player,trap,tiles=load_box(currentbox)
        player.x=950
        player.y=650
    

    if currentbox==0 and player.y>=650 and player.y<=700 and player.x==1000:
        currentbox=5
        walls,player,trap,tiles=load_box(currentbox)

    if currentbox==5 and player.y>=650 and player.y<=700 and player.x<0:
        currentbox=0
        walls,player,trap,tiles=load_box(currentbox)
        player.x=950
        player.y=650
    
    if currentbox==5 and player.x>=800 and player.x<=850 and player.y==0:
        currentbox=4
        walls,player,trap,tiles=load_box(currentbox)
    
    if currentbox==4 and player.x>=800 and player.x<=850 and player.y==750:
        currentbox=5
        walls,player,trap,tiles=load_box(currentbox)
        player.x=800 
        player.y=30
    if currentbox==4 and player.x>=900 and player.x<=950 and player.y==0:
        currentbox=3
        walls,player,trap,tiles=load_box(currentbox)
        player.x=900
        player.y=720
    if currentbox==3 and player.x>=900 and player.x<=950 and player.y==750:
        currentbox=4
        walls,player,trap,tiles=load_box(currentbox)
        player.x=900
        player.y=30
    if currentbox==3 and player.y>=50 and player.y<=100 and player.x==1000:
        currentbox=6
        walls,player,trap,tiles=load_box(currentbox)

    if currentbox==6 and player.y>=50 and player.y<=100 and player.x<0:
        currentbox=3
        walls,player,trap,tiles=load_box(currentbox)
        player.x=950
        player.y=50
    
    if currentbox==6 and player.x>=900 and player.x<=950 and player.y==750:
        currentbox=7
        walls,player,trap,tiles=load_box(currentbox)
        player.y=30
    
    if currentbox==7 and player.x>=900 and player.x<=950 and player.y==0:
        currentbox=6
        walls,player,trap,tiles=load_box(currentbox)
        player.x=900
        player.y=720
    if currentbox==7 and player.x>=150 and player.x<=200 and player.y==750:
        currentbox=8
        walls,player,trap,tiles=load_box(currentbox)
        player.y=30
    if currentbox==8 and player.x>=150 and player.x<=200 and player.y==0:
        currentbox=7
        walls,player,trap,tiles=load_box(currentbox)
        player.x=150
        player.y=720



    
    

    for wall in walls:                                              #looping through the walls created to actually creat the rectangles
        pygame.draw.rect(screen, Color("blue"), wall.rect)

    trap.draw()
    trap.update()

    player.draw()
    player.update()
    
    if currentbox == 0:         ## generating enemies and keys for box 0
        keys.toggleBox0()
        obstacles.movement(0, obstacles.coors0, 0, 250, 350)
        obstacles.movement(1, obstacles.coors1, 1, 50, 150)
        obstacles.movement(2, obstacles.coors2, 1, 50, 150)
        obstacles.movement(3, obstacles.coors3, 0, 700, 900)
        obstacles.movement(4, obstacles.coors4, 0, 750, 900)
        obstacles.movement(5, obstacles.coors5, 0, 700, 900)
        obstacles.movement(6, obstacles.coors6, 0, 650, 850)
        obstacles.movement(7, obstacles.coors7, 0, 450, 550)
        obstacles.movement(8, obstacles.coors8, 0, 450, 550)
        obstacles.draw1()

    if currentbox == 1:         ## generating enemies and keys for box 1
        keys.toggleBox1()

    if currentbox == 2:         ## generating enemies and keys for box 2
        keys.toggleBox2()

    if currentbox == 3:         ## generating enemies and keys for box 3
        keys.toggleBox3()

    if currentbox == 4:         ## generating enemies and keys for box 4
        keys.toggleBox4()

    if currentbox == 5:         ## generating enemies and keys for box 5
        keys.toggleBox5()
    
    if currentbox == 6:         ## generating enemies and keys for box 6
        keys.toggleBox6()
    
    if currentbox == 7:         ## generating enemies and keys for box 7
        keys.toggleBox7()

    if currentbox == 8:         ## generating enemies and keys for box 8
        keys.toggleBox8()

    i=0
    while i<=(len(tiles)-3):
        screen.blit(tiles[i],(tiles[i+1],tiles[i+2]))
        i+=3
    
    player.displayDeaths()
    keys.keyCountDisplay()

    keys.obtainKey(player.x, player.y, currentbox)

    for event in pygame.event.get():
        if event.type==QUIT:
            loop = False
        if event.type == KEYUP and event.key == K_p:
            pause = True
    
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
