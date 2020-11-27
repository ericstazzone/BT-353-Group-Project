import pygame, sys
from pygame.locals import *
from pygame import mixer

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
    
    def trapped(self, traps):
        r = Rect(self.x, self.y, 30, 30)
        for t in traps:
            tr = Rect(t.x, t.y, 30, 30)
            if (r.colliderect(tr) and t.counter > 5 and t.counter < 9):
                return True
        return False

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
    coors9 = [450, 50]
    coors10 = [600, 550]
    coors11 = [625, 400]
    coors12 = [700, 300]
    coors13 = [500, 50]
    coors14 = [150, 300]
    coors15 = [300, 500]    
    coors16 = [400, 500]
    movespeed = 2
    check = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    circle0rect = Rect(coors0[0], coors0[1], 10, 10)
    circle1rect = Rect(coors1[0], coors1[1], 10, 10)
    circle2rect = Rect(coors2[0], coors2[1], 10, 10)
    circle3rect = Rect(coors3[0], coors3[1], 10, 10)
    circle4rect = Rect(coors4[0], coors4[1], 10, 10)
    circle5rect = Rect(coors5[0], coors5[1], 10, 10)
    circle6rect = Rect(coors6[0], coors6[1], 10, 10)
    circle7rect = Rect(coors7[0], coors7[1], 10, 10)
    circle8rect = Rect(coors8[0], coors8[1], 10, 10)
    circle9rect = Rect(coors9[0], coors9[1], 10, 10)
    circle10rect = Rect(coors10[0], coors10[1], 10, 10)
    circle11rect = Rect(coors11[0], coors11[1], 10, 10)
    circle12rect = Rect(coors12[0], coors12[1], 10, 10)
    circle13rect = Rect(coors13[0], coors13[1], 10, 10)
    circle14rect = Rect(coors14[0], coors14[1], 10, 10)
    circle15rect = Rect(coors15[0], coors15[1], 10, 10)
    circle16rect = Rect(coors16[0], coors16[1], 10, 10)
    circlesrect=[circle0rect, circle1rect, circle2rect, circle3rect, circle4rect, circle5rect, circle6rect, circle7rect, circle8rect, 
    circle9rect, circle10rect, circle11rect, circle12rect, circle13rect, circle14rect, circle15rect, circle16rect]

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
    
    def draw2(self):
        screen.blit(self.enemy, self.coors9)
        screen.blit(self.enemy, self.coors10)
        screen.blit(self.enemy, self.coors11)
        screen.blit(self.enemy, self.coors12)
        screen.blit(self.enemy, self.coors13)
        screen.blit(self.enemy, self.coors14)
        screen.blit(self.enemy, self.coors15)    
        screen.blit(self.enemy, self.coors16)



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
       


def tile(x,y,image):
    image = pygame.image.load(image)
    image=pygame.transform.scale(image, (50, 50))
    return image,x,y

 
def load_box(box):                                                  #looping through the string above to get it set up for drawing. Creating rectangle objects
    walls=[]
    tiles=[]
    traps=[]
    i=0
    x = y = 0
    for row in boxes[box]:
        for col in row:
            if col in ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","Q"]:
                walls.append(Wall((x, y)))
            if col=="A":
                image,corx,cory=tile(x,y,'images/walldownA.png')
                tiles.append(image)
                tiles.append(int(corx))
                tiles.append(int(cory))
            if col=="B":
                image,corx,cory=tile(x,y,'images/walldownleftB.png')
                tiles.append(image)
                tiles.append(int(corx))
                tiles.append(int(cory))
            if col=="C":
                image,corx,cory=tile(x,y,'images/walldownleftrightC.png')
                tiles.append(image)
                tiles.append(int(corx))
                tiles.append(int(cory))
            if col=="D":
                image,corx,cory=tile(x,y,'images/walldownrightD.png')
                tiles.append(image)
                tiles.append(int(corx))
                tiles.append(int(cory))
            
            if col=="E":
                image,corx,cory=tile(x,y,'images/wallleftE.png')
                tiles.append(image)
                tiles.append(int(corx))
                tiles.append(int(cory))
            if col=="F":
                image,corx,cory=tile(x,y,'images/wallleftrightF.png')
                tiles.append(image)
                tiles.append(int(corx))
                tiles.append(int(cory))
            if col=="G":
                image,corx,cory=tile(x,y,'images/wallnoneG.png')
                tiles.append(image)
                tiles.append(int(corx))
                tiles.append(int(cory))

            if col=="H":
                image,corx,cory=tile(x,y,'images/wallrightH.png')
                tiles.append(image)
                tiles.append(int(corx))
                tiles.append(int(cory))
            if col=="I":
                image,corx,cory=tile(x,y,'images/wallupdownI.png')
                tiles.append(image)
                tiles.append(int(corx))
                tiles.append(int(cory))
        
            if col=="J":
                image,corx,cory=tile(x,y,'images/wallupdownleftJ.png')
                tiles.append(image)
                tiles.append(int(corx))
                tiles.append(int(cory))
            if col=="K":
                image,corx,cory=tile(x,y,'images/wallupdownleftrightK.png')
                tiles.append(image)
                tiles.append(int(corx))
                tiles.append(int(cory))
            if col=="L":
                image,corx,cory=tile(x,y,'images/wallupdownrightL.png')
                tiles.append(image)
                tiles.append(int(corx))
                tiles.append(int(cory))
            if col=="M":
                image,corx,cory=tile(x,y,'images/wallupleftM.png')
                tiles.append(image)
                tiles.append(int(corx))
                tiles.append(int(cory))
            if col=="N":
                image,corx,cory=tile(x,y,'images/wallupleftrightN.png')
                tiles.append(image)
                tiles.append(int(corx))
                tiles.append(int(cory))
            if col=="O":
                image,corx,cory=tile(x,y,'images/wallupO.png')
                tiles.append(image)
                tiles.append(int(corx))
                tiles.append(int(cory))
            if col=="Q":
                image,corx,cory=tile(x,y,'images/walluprightQ.png')
                tiles.append(image)
                tiles.append(int(corx))
                tiles.append(int(cory))
            
            


            if col=="T":
                traps.append(Traps((x,y)))
            if col=="P":
                player=Player((x,y))
            x +=50
        y += 50
        x = 0
    return walls,player,traps,tiles
             

def displayDeaths(deaths):
        font = pygame.font.SysFont('Comic Sans MS', 35)
        text = font.render('Deaths: ' + str(deaths), True, (255, 0, 0))
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
    "DFFFCFCFCCCCCCCB DCB",
    "I   O O PNNNKKKJ LKJ",
    "I           LKNM QNJ",
    "I   A A DCB LJ  T  I",
    "LFE LCKFNNM LKCE HFJ",
    "I   LKJ   T LKJ    I",
    "I HFKKJ DKCCKKNFE HJ",
    "I   QNNFNNNNKJ     I",
    "I B         LNE HFCJ",
    "I J  A DB G I     LJ",
    "I M  O QJ   LCCB DKJ",
    "I   A   LB DKKKM QKJ",
    "I   LE HNM QNNM   QM",
    "I P I               ",
    "QFFFNFFFFFFFFFFFFFFF", 
    ],
    [
    "DCB HFFFFFFFFFFFCCCB",
    "LKJ             LKKJ",
    "LNNFFFFFE HE  DCKKKJ",
    "I            DNNNNNJ",
    "I DFCCCFFFCCCJ     I",
    "I O QNM   QKNM HFE I",
    "I       A  I       I",
    "LCB HFFCKB I  G  A I",
    "LNNE   QNM I     I I",
    "I    A     I HCE LCJ",
    "I G DJ G DCJ  O  LKJ",
    "I   LJ   LKJ     LKJ",
    "I HCNNFFFNNM  G  LKJ",
    "I  T             LKJ",
    "QFFFFFFFFFFFFFFEPQNM",
    ],
    [
    "DCCCCCCCFFFFFFFFFCCB",
    "LKKKKKKJ         LKJ",
    "LKKKKKKJ         LKJ",
    "LKKNNNNM         LKJ",
    "LKJ T            LKJ",
    "LKJ DCCB         LKJ",
    "LKJ QNNJ         LKJ",
    "LKJ    I         LKJ",
    "LKKFFFFM         LKJ",
    "LKJ              LKJ",
    "LKM HCCCB       DKKJ",
    "LM   QKKKB     DKKKJ",
    "I     LKKKB   HNNNNM",
    "LB   DKKKKKB        ",
    "QNEPHNNNNNNNFFFFFFFE",
    ],
    [
    "DCCCCCCCCCCCCCCFFFFE",
    "LKKKKKKKKKKKKKJ     ",
    "LKKNNNNNNNNNKKJ DCCB",
    "LKJ       T LKM QKKJ",
    "LKJ    A    LJ   LKJ",
    "LKJ    I    LKB HKKJ",
    "LKJ    I    LKJ  LKJ",
    "LKJ   DKB   LKKB LKJ",
    "LKJ   LKJ   LKKJ QNJ",
    "LKJ   LKJ   LKKJ   I",
    "LKJ   QKM   LKKJ   I",
    "LKJ    I    LKKJ   I",
    "QNM    I    LKKKCB I",
    "P      I    LKKKKJ I",
    "HFFFFFFNFFFFNNNNNM O",
    ],
    [
    "DCCFFFFFFFFFFFFFFB A",
    "LKJ        T     I I",
    "LKJ A            I I",
    "LKJ I            I I",
    "LNM I            I I",
    "I   LCCCCCCCCCCCCM O",
    "I DCKKKKKKKKKKKKJ   ",
    "I LKKKKKKKKKKKKKJ   ",
    "I LKKKKKKKKKKKKKJ   ",
    "I LNNNNNNNNNNNNNM   ",
    "I I                 ",
    "I I DCCCCCCCCCCB DCB",
    "I O QNNNNNNNKKKJ LKJ",
    "I           LKKJ LKJ",
    "QFFFFFFFFFFFNNNMPQNM",
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

deaths = 0
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
        died = False
        deaths += 1
        currentbox = 0
        walls,player,trap,tiles=load_box(currentbox)
    
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
        pygame.draw.rect(screen, Color("white"), wall.rect)

    for t in trap:
        t.draw()
        t.update()

    player.draw()
    player.update()

    i=0
    while i<=(len(tiles)-3):
        screen.blit(tiles[i],(tiles[i+1],tiles[i+2]))
        i+=3
    
    if currentbox == 0:         ## generating enemies and keys for box 0
        keys.toggleBox0()
        obstacles.movespeed = 2
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
        obstacles.movespeed = 4
        obstacles.movement(9, obstacles.coors9, 1, 50, 150)
        obstacles.movement(10, obstacles.coors10, 0, 600, 800)
        obstacles.movement(11, obstacles.coors11, 0, 600, 800)
        obstacles.movement(12, obstacles.coors12, 0, 600, 900)
        obstacles.movement(13, obstacles.coors13, 0, 500, 750)
        obstacles.movement(14, obstacles.coors14, 1, 250, 350)
        obstacles.movement(15, obstacles.coors15, 1, 400, 550)
        obstacles.movement(16, obstacles.coors16, 1, 450, 550)
        obstacles.draw2()
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

    
    
    displayDeaths(deaths)
    keys.keyCountDisplay()

    keys.obtainKey(player.x, player.y, currentbox)

    died = player.trapped(trap)

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
    clock.tick(30)                                                 #fps

pygame.quit()                                                       
