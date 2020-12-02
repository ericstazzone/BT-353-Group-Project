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
        image4 = pygame.transform.flip(image1, True, False)
        image5 = pygame.transform.flip(image2, True, False)
        image6 = pygame.transform.flip(image3, True, False)
        image7 = pygame.image.load('images/squarehappy1.png')
        image8 = pygame.image.load('images/squarehappy2.png')
        image9 = pygame.image.load('images/squarehappy3.png')
        image10 = pygame.image.load('images/squarehappy3.png')
        image11 = pygame.image.load('images/squarehappy3.png')
        image12 =  pygame.image.load('images/squarehappy3.png')
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
        self.index = 0
        self.image = self.images[self.index]
        self.x = pos[0]
        self.y = pos[1]
        self.counter = 0
        self.counterL = 3
        self.counterR = 0
        self.counterK = 6
        self.counterD = 9
        self.truth = True

    def updateR(self):
        self.index+=1
        if self.index >= 4:
            self.counterR += 1
            self.index = 0
        if self.counterR > 2:
            self.index = 0
            self.counterR = 0
        self.image = self.images[self.counterR]
        self.image = pygame.transform.scale(self.image, (40, 40))

    def updateL(self):
        self.index+=1 
        if self.index >= 4:
            self.counterL += 1
            self.index = 0
        if self.counterL >= 5:
            self.index = 0
            self.counterL = 3
        self.image = self.images[self.counterL]
        self.image = pygame.transform.scale(self.image, (40, 40))\

    def updateK(self):
        self.index+=1 
        if self.index >= 4:
            self.counterK += 1
            self.index = 0
        if self.counterK >= 9:
            self.index = 0
            self.counterK = 6
        self.image = self.images[self.counterK]
        self.image = pygame.transform.scale(self.image, (40, 40))

    def updateD(self):
        self.index+=1 
        if self.index >= 4:
            self.counterD += 1
            self.index = 0
        if self.counterD >= 9:
            self.index = 0
            self.counterD = 6
        self.image = self.images[self.counterD]
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
    keyTruth = False
    blackoutcoors = [0, -10]
    
    ## Key Variables
    keys = [False, True, True, True, True, True, True, True]
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
            self.keyTruth = True
        if temp.colliderect(self.keysrect[1]) == 1 and currentbox == 1:
            self.keys[1] = True
            self.keyTruth = True
        if temp.colliderect(self.keysrect[2]) == 1 and currentbox == 2:
            self.keys[2] = True
            self.keyTruth = True
        if temp.colliderect(self.keysrect[3]) == 1 and currentbox == 3:
            self.keys[3] = True
            self.keyTruth = True
        if temp.colliderect(self.keysrect[4]) == 1 and currentbox == 4:
            self.keys[4] = True  
            self.keyTruth = True      
        if temp.colliderect(self.keysrect[5]) == 1 and currentbox == 5:
            self.keys[5] = True
            self.keyTruth = True
        if temp.colliderect(self.keysrect[6]) == 1 and currentbox == 6:
            self.keys[6] = True
            self.keyTruth = True
        if temp.colliderect(self.keysrect[7]) == 1 and currentbox == 7:
            self.keys[7] = True
            self.keyTruth = True

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
        screen.blit(image, (200, 0))
        font = pygame.font.SysFont('Garamond', 35)
        text = font.render(str(count), True, (255, 204, 1))
        screen.blit(text, (240, -2))

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

    coors17 = [100,600]
    coors18 = [250,200]
    coors19 = [400,450]
    coors20 = [400,400]
    coors21 = [400,350]
    coors22 = [400,300]
    coors23 = [400,250]

    coors24 = [200,150]
    coors25 = [200,250]
    coors26 = [500,250]
    coors27 = [200,350]
    coors28 = [200,500]
    coors29 = [100,650]
    coors30 = [200,750]
    coors31 = [750,200]
    coors32 = [850,500]

    coors33 = [700,500]
    coors34 = [50, 650]
    coors35 = [300,150]
    coors36 = [350,150]
    coors37 = [400,150]
    coors38 = [450,150]
    coors39 = [500,150]
    coors40 = [550,150]

    coors41 = [50,150]
    coors42 = [100,250]
    coors43 = [100,350]
    coors44 = [100,450]
    coors45 = [350,250]
    coors46 = [700,150]
    coors47 = [750,250]
    coors48 = [750,350]
    coors49 = [750,450]

    coors50 = [200, 100]
    coors51 = [300, 150]
    coors52 = [400, 200]
    coors53 = [500, 200]
    coors54 = [600, 150]
    coors55 = [700, 100]
    coors56 = [50, 300]

    coors57 = [50, 250]
    coors58 = [650,350]
    coors59 = [700,450]
    coors60 = [750,550]
    coors61 = [300,400]
    coors62 = [350,450]
    coors63 = [450,500]
    coors64 = [500,550]
    
    coors66 = [250, 350] ## vertical
    coors67 = [350, 450]
    coors68 = [450, 550]
    coors73 = [550, 350]
    coors74 = [650, 450]
    coors75 = [750, 550]
    coors65 = [200, 150] ## horizontal
    coors69 = [300, 250]
    coors70 = [400, 350]
    coors71 = [500, 450]
    coors72 = [600, 550]

    movespeed = 2
    check = [0, 0, 0, 0, 0, 
             0, 0, 0, 0, 0, 
             0, 0, 0, 0, 0, 
             0, 0, 0, 0, 0, 
             0, 0, 0, 0, 0, 
             0, 0, 0, 0, 0, 
             0, 0, 0, 0, 0, 
             0, 0, 0, 0, 0, 
             0, 0, 0, 0, 0,
             0, 0, 0, 0, 0,
             0, 0, 0, 0, 0,
             0, 0, 0, 0, 0,
             0, 0, 0, 0, 0,
             0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0] #increase to # of objects

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
    
    circle17rect = Rect(coors17[0], coors17[1], 10, 10)
    circle18rect = Rect(coors18[0], coors18[1], 10, 10)
    circle19rect = Rect(coors19[0], coors19[1], 10, 10)
    circle20rect = Rect(coors20[0], coors20[1], 10, 10)
    circle21rect = Rect(coors21[0], coors21[1], 10, 10)
    circle22rect = Rect(coors22[0], coors22[1], 10, 10)
    circle23rect = Rect(coors23[0], coors23[1], 10, 10)

    circle24rect = Rect(coors24[0], coors24[1], 10, 10)
    circle25rect = Rect(coors25[0], coors25[1], 10, 10)
    circle26rect = Rect(coors26[0], coors26[1], 10, 10)
    circle27rect = Rect(coors27[0], coors27[1], 10, 10)
    circle28rect = Rect(coors28[0], coors28[1], 10, 10)
    circle29rect = Rect(coors29[0], coors29[1], 10, 10)
    circle30rect = Rect(coors30[0], coors30[1], 10, 10)
    circle31rect = Rect(coors31[0], coors31[1], 10, 10)
    circle32rect = Rect(coors32[0], coors32[1], 10, 10)

    circle33rect = Rect(coors33[0], coors33[1], 10, 10)
    circle34rect = Rect(coors34[0], coors34[1], 10, 10)
    circle35rect = Rect(coors35[0], coors35[1], 10, 10)
    circle36rect = Rect(coors36[0], coors36[1], 10, 10)
    circle37rect = Rect(coors37[0], coors37[1], 10, 10)
    circle38rect = Rect(coors38[0], coors38[1], 10, 10)
    circle39rect = Rect(coors39[0], coors39[1], 10, 10)
    circle40rect = Rect(coors40[0], coors40[1], 10, 10)

    circle41rect = Rect(coors41[0], coors41[1], 10, 10)
    circle42rect = Rect(coors42[0], coors42[1], 10, 10)
    circle43rect = Rect(coors43[0], coors43[1], 10, 10)
    circle44rect = Rect(coors44[0], coors44[1], 10, 10)
    circle45rect = Rect(coors45[0], coors45[1], 10, 10)
    circle46rect = Rect(coors46[0], coors46[1], 10, 10)
    circle47rect = Rect(coors47[0], coors47[1], 10, 10)
    circle48rect = Rect(coors48[0], coors48[1], 10, 10)
    circle49rect = Rect(coors49[0], coors49[1], 10, 10)

    circle50rect = Rect(coors50[0], coors50[1], 10, 10)
    circle51rect = Rect(coors51[0], coors51[1], 10, 10)
    circle52rect = Rect(coors52[0], coors52[1], 10, 10)
    circle53rect = Rect(coors53[0], coors53[1], 10, 10)
    circle54rect = Rect(coors54[0], coors54[1], 10, 10)
    circle55rect = Rect(coors55[0], coors55[1], 10, 10)
    circle56rect = Rect(coors56[0], coors56[1], 10, 10)

    circle57rect = Rect(coors57[0], coors57[1], 10, 10)
    circle58rect = Rect(coors58[0], coors58[1], 10, 10)
    circle59rect = Rect(coors59[0], coors59[1], 10, 10)
    circle60rect = Rect(coors60[0], coors60[1], 10, 10)
    circle61rect = Rect(coors61[0], coors61[1], 10, 10)
    circle62rect = Rect(coors62[0], coors62[1], 10, 10)
    circle63rect = Rect(coors63[0], coors63[1], 10, 10)
    circle64rect = Rect(coors64[0], coors64[1], 10, 10)

    circle65rect = Rect(coors65[0], coors65[1], 10, 10)
    circle66rect = Rect(coors66[0], coors66[1], 10, 10)
    circle67rect = Rect(coors67[0], coors67[1], 10, 10)
    circle68rect = Rect(coors68[0], coors68[1], 10, 10)
    circle69rect = Rect(coors69[0], coors69[1], 10, 10)
    circle70rect = Rect(coors70[0], coors70[1], 10, 10)
    circle71rect = Rect(coors71[0], coors71[1], 10, 10)
    circle72rect = Rect(coors72[0], coors72[1], 10, 10)
    circle73rect = Rect(coors73[0], coors73[1], 10, 10)
    circle74rect = Rect(coors74[0], coors74[1], 10, 10)
    circle75rect = Rect(coors75[0], coors75[1], 10, 10)

    
    circlesrect= [
    circle0rect, circle1rect, circle2rect, circle3rect, circle4rect, circle5rect, circle6rect, circle7rect, circle8rect, 
    circle9rect, circle10rect, circle11rect, circle12rect, circle13rect, circle14rect, circle15rect, circle16rect, circle17rect,
    circle18rect, circle19rect, circle20rect, circle21rect, circle22rect, circle23rect, circle24rect, circle25rect, circle26rect, 
    circle27rect, circle28rect, circle29rect, circle30rect, circle31rect, circle32rect,
    circle33rect, circle34rect, circle35rect, circle36rect, circle37rect, circle38rect, circle39rect, circle40rect,
    circle41rect, circle42rect, circle43rect, circle44rect, circle45rect, circle46rect, circle47rect, circle48rect, circle49rect,
    circle50rect, circle51rect, circle52rect, circle53rect, circle54rect, circle55rect, circle56rect,
    circle57rect, circle58rect, circle59rect, circle60rect, circle61rect, circle62rect, circle63rect, circle64rect, circle65rect,
    circle66rect, circle67rect, circle68rect, circle69rect, circle70rect, circle71rect, circle72rect, circle73rect, circle74rect, 
    circle75rect]

    def collide(self, player, box):
        r = Rect(player.x, player.y, 30, 30)
        enemyList = []
        if box == 0:
            enemyList = self.circlesrect[:9]
        elif box == 1:
            enemyList = self.circlesrect[9:17]
        elif box == 2:
            enemyList = self.circlesrect[17:24]
        elif box == 3:
            enemyList = self.circlesrect[24:33]
        elif box == 4:
            enemyList = self.circlesrect[33: 41]
        elif box == 5:
            enemyList = self.circlesrect[41:50]
        elif box == 6:
            enemyList = self.circlesrect[50:57]
        elif box == 7:
            enemyList = self.circlesrect[57:65]
        elif box == 8:
            enemyList = self.circlesrect[65:75]
        return r.collidelist(enemyList) != -1

    def movement(self, enemy, enemycoors, direction, min, max):
        r = self.circlesrect[enemy]
        if self.check[enemy] == 1: ## moving right
            enemycoors[direction] += self.movespeed
            if direction == 0:
                self.circlesrect[enemy] = Rect(r.left + self.movespeed, r.top, 10, 10)
            else:
                self.circlesrect[enemy] = Rect(r.left, r.top + self.movespeed, 10, 10)

        else: ## moving left
            enemycoors[direction] -= self.movespeed
            if direction == 0:
                self.circlesrect[enemy] = Rect(r.left - self.movespeed, r.top, 10, 10)
            else:
                self.circlesrect[enemy] = Rect(r.left, r.top - self.movespeed, 10, 10)
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

    def draw3(self):
        screen.blit(self.enemy, self.coors17)
        screen.blit(self.enemy, self.coors18)
        screen.blit(self.enemy, self.coors19)
        screen.blit(self.enemy, self.coors20)
        screen.blit(self.enemy, self.coors21)
        screen.blit(self.enemy, self.coors22)
        screen.blit(self.enemy, self.coors23)

    def draw4(self):
        screen.blit(self.enemy, self.coors24)
        screen.blit(self.enemy, self.coors25)
        screen.blit(self.enemy, self.coors26)
        screen.blit(self.enemy, self.coors27)
        screen.blit(self.enemy, self.coors28)
        screen.blit(self.enemy, self.coors29)
        screen.blit(self.enemy, self.coors30)
        screen.blit(self.enemy, self.coors31)
        screen.blit(self.enemy, self.coors32)

    def draw5(self):
        screen.blit(self.enemy, self.coors33)
        screen.blit(self.enemy, self.coors34)
        screen.blit(self.enemy, self.coors35)
        screen.blit(self.enemy, self.coors36)
        screen.blit(self.enemy, self.coors37)
        screen.blit(self.enemy, self.coors38)
        screen.blit(self.enemy, self.coors39)
        screen.blit(self.enemy, self.coors40)

    def draw6(self):
        screen.blit(self.enemy, self.coors41)
        screen.blit(self.enemy, self.coors42)
        screen.blit(self.enemy, self.coors43)
        screen.blit(self.enemy, self.coors44)
        screen.blit(self.enemy, self.coors45)
        screen.blit(self.enemy, self.coors46)
        screen.blit(self.enemy, self.coors47)
        screen.blit(self.enemy, self.coors48)
        screen.blit(self.enemy, self.coors49)

    def draw7(self):
        screen.blit(self.enemy, self.coors50)
        screen.blit(self.enemy, self.coors51)
        screen.blit(self.enemy, self.coors52)
        screen.blit(self.enemy, self.coors53)
        screen.blit(self.enemy, self.coors54)
        screen.blit(self.enemy, self.coors55)
        screen.blit(self.enemy, self.coors56)

    def draw8(self):
        screen.blit(self.enemy, self.coors57)
        screen.blit(self.enemy, self.coors58)
        screen.blit(self.enemy, self.coors59)
        screen.blit(self.enemy, self.coors60)
        screen.blit(self.enemy, self.coors61)
        screen.blit(self.enemy, self.coors62)
        screen.blit(self.enemy, self.coors63)
        screen.blit(self.enemy, self.coors64)

    def draw9(self):
        screen.blit(self.enemy, self.coors65)
        screen.blit(self.enemy, self.coors66)
        screen.blit(self.enemy, self.coors67)
        screen.blit(self.enemy, self.coors68)
        screen.blit(self.enemy, self.coors69)
        screen.blit(self.enemy, self.coors70)
        screen.blit(self.enemy, self.coors71)
        screen.blit(self.enemy, self.coors72)
        screen.blit(self.enemy, self.coors73)
        screen.blit(self.enemy, self.coors74)
        screen.blit(self.enemy, self.coors75)

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
        if self.index >= 9:
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
            if col in ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","Q", "W"]:
                walls.append(Wall((x, y)))
            if col=="W":
                image,corx,cory=tile(x,y,'images/walldownA.png')
                tiles.append(image)
                tiles.append(int(corx))
                tiles.append(int(cory))
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
            if col=="Z":
                image,corx,cory=tile(x,y,'images/wallemptyZ.png')
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
        font = pygame.font.SysFont('Garamond', 35)
        text = font.render('Deaths: ' + str(deaths), True, (149, 33, 33))
        screen.blit(text, (50, -2))
    
pygame.init()
#backgroundsound = mixer.music.load('song1_aLtZHmr9.wav')
#mixer.music.play(-1)

clock = pygame.time.Clock()

size = 997,748
screen = pygame.display.set_mode(size,0,32)
pygame.display.set_caption('The Impossible Game')

currentbox=0                                                #setting the level to 0
boxes = [[                                                          #making the boundaries
    "DFFFCFCFFCCCCCCB DCB",
    "I   O O  QNNKKKJ LKJ",
    "I           LKNM QNJ",
    "I   A A DCB LJ  T  I",
    "LFE LCKFNNM LKCE HFJ",
    "I   LKJ   T LKJ    I",
    "I HFKKJ DCCCKKNFE HJ",
    "I   QNNFNNNNKJ     I",
    "I A         LNE HFCJ",
    "I I  A DB G I     LJ",
    "I O  O QJ   LCCB DKJ",
    "I   A   LB DKKKM QKJ",
    "I   LE HNM QNNM   QM",
    "I P I             T ",
    "QFFFNFFFFFFFFFFFFFFF", 
    ],
    [
    "DCB HFFFFFFFFFFFCCCB",
    "LKJ             LKKJ",
    "LNNFFFFFETTG  DCKKKJ",
    "I        T   DNNNNNJ",
    "I DFCCCFFFCCCJ     I",
    "I O QNM   QKNM HFETI",
    "I       A  I     T I",
    "LCB HFFCKB I  G  A I",
    "LNNE   QNM I     I I",
    "I    A TT  I HCE LCJ",
    "I G DJ G DCJ  O  LKJ",
    "I   LJ   LKJ     LKJ",
    "I HCNNFFFNNM  G  LKJ",
    "I  T             LKJ",
    "QFFFFFFFFFFFFFFEPQNM",
    ],
    [
    "DCCCCCCCCCCCCCCCCCCB",
    "LKKKKKKKKKKKKKKKKKKJ",
    "LKKKKKKKKKKKKKKKKKKJ",
    "LKKNNNNNNNNNNNNNNKKJ",
    "LKJ T            LKJ",
    "LKJ DCCBT        LKJ",
    "LKJ QNNJTT       LKJ",
    "LKJ    ITTT      LKJ",
    "LKKFFFFMT        LKJ",
    "LKJ              LKJ",
    "LKM HCCCB       DKKJ",
    "LM   QKKKB     DKKKJ",
    "I T T LKKKB   HNNNNM",
    "LB   DKKKKKB      T ",
    "QNEPHNNNNNNNFFFFFFFE",
    ],
    [
    "DCCCCCCCCCCCCCCFFFFE",
    "LKKKKKKKKKKKKKJ     ",
    "LKKNNNNNNNNNKKJ DCCB",
    "LKJ    T    LKM QKKJ",
    "LKJ    A    LJ   LKJ",
    "LKJ    I    LKB HKKJ",
    "LKJ    I    LKJ  LKJ",
    "LKJ   DKB   LKKB LKJ",
    "LKJ T LKJ   LKKJ QNJ",
    "LKJ T LKJ   LKKJ   I",
    "LKJ   QKM   LKKJ   I",
    "LKJ    I    LKKJ   I",
    "QNM    I    LKKKCB I",
    "PT     I    LKKKKJ I",
    "HFFFFFFNFFFFNNNNNM O",
    ],
    [
    "DCCFFFFFFFFFFFFFFB A",
    "LKJ T            I I",
    "LKJ ATTTTTTTTTTTTI I",
    "LKJ I            I I",
    "LNM I            I I",
    "I   LCCCCCCCCCCCCM I",
    "I DCKKKKKKKKKKKKJ  I",
    "I LKKKKKKKKKKKKKJ  I",
    "I LKKKKKKKKKKKKKJ  I",
    "I LNNNNNNNNNNNNNM  I",
    "I I             T  I",
    "I ITDCCCCCCCCCCB DCK",
    "I O QNNNNNNNKKKJ LKJ",
    "I           LKKJ LKJ",
    "QFFFFFFFFFFFNNNMPQNM",
    ],
    [
    "DFBZZZZZZZZZZZZI IZZ",
    "I IZZZZZZZZZZZZI IZZ",
    "I QFFFBZZZZZZDFM QFB",
    "I T   IZZZZZZI     I",
    "QCE HCKFFFFFFKCE HCM",
    "ZI   II      II   IZ",
    "ZLE HJI  DB  ILE HJZ",
    "ZI   II  II  II   IZ",
    "ZLE HJI  II  ILE HJZ",
    "ZI   LM  II  QJ   IZ",
    "ZQB DM  DMQB  QB DMZ",
    "ZZI O  DMZZQB  O IZZ",
    "FFM   DMZZZZQB   IZZ",
    "P    DMZZZZZZQB  IZZ",
    "FFFFFMZZZZZZZZQFFMZZ",
    ],
    [
    "FFFBZZZZZZZZZZZZZZZZ",
    "P  LFCFCFCFCFCFBZZZZ",
    "FB O O O O O O QFFFB",
    "ZI T   T   T   T   I",
    "ZQFB A A A A A DFB I",
    "DFFNFNFNFNFNFNFNFM I",
    "I                  I",
    "ITHFFFFFFFFFFFFFFFFJ",
    "I                  I",
    "I DFFFFFFFFFFFFFFB I",
    "I IZZZZZZZZZZZZZZI I",
    "I IZZZZZZZZZZZZZZI I",
    "I QFFFFFFFFFFFFFFJ I",
    "IT               ITI",
    "QFFFFFFFFFFFFFFFFJ I",
    ],
    [
    "ZZZZZZZZZZZZZZZZZIPI",
    "ZZZZZZZZZZZZZZZZZI I",
    "DFFFFFFFFFFFFFFFFM I",
    "I   T              I",
    "I   DFFFFFFFFFFB   I",
    "I   IZZZZZZZZZZI   I",
    "I   LFFFFFFCFFFM   I",
    "QFBTI T    I       I",
    "ZZI LBT    I       I",
    "ZZI IQBT   I       I",
    "ZZI IZQBT  I T     I",
    "ZZI IZZQBT I T     I",
    "ZZI IZZZQBTO T     I",
    "ZZI IZZZZI   DFFFFFM",
    "ZZI IZZZZQFFFMZZZZZZ",
    ],
    [
    "ZZIPIZZZZZZZZZZZZZZZ",
    "ZZI IZZZZZZZZZZZZZZZ",
    "ZZI QFFFFFFFFFFFFBZZ",
    "ZZI   T     T    IZZ",
    "ZZIT     T     T IZZ",
    "ZZI   T     T    IZZ",
    "ZZIT     T     T QFF",
    "ZZI   T     T    T  ",
    "ZZIT     T     T DFF",
    "ZZI   T     T    IZZ",
    "ZZIT     T     T IZZ",
    "ZZI   T     T    IZZ",
    "ZZQFFFFFFFFFFFFFFMZZ",
    "ZZZZZZZZZZZZZZZZZZZZ",
    "ZZZZZZZZZZZZZZZZZZZZ",
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
    key = pygame.key.get_pressed()
    
    if key[pygame.K_w] or key[pygame.K_UP]:
        player.movey(-10)
    elif key[pygame.K_a] or key[pygame.K_LEFT]: 
        player.movex(-10)
    if key[pygame.K_s] or key[pygame.K_DOWN]: 
        player.movey(10)
    elif key[pygame.K_d] or key[pygame.K_RIGHT]: 
        player.movex(10)

    if key[pygame.K_a] or key[pygame.K_LEFT]:
        player.truth = False

    if key[pygame.K_d] or key[pygame.K_RIGHT]:
        player.truth = True
    
    if player.truth == False:
        player.updateL()
    elif player.truth == True:
        player.updateR()

    i=0
    while i<=(len(tiles)-3):
        screen.blit(tiles[i],(tiles[i+1],tiles[i+2]))
        i+=3
    
    if currentbox == 0:         ## generating enemies and keys for box 0
        keys.toggleBox0()
        obstacles.movespeed = 3
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
        obstacles.movespeed = 5
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
        obstacles.movespeed = 4
        obstacles.movement(17, obstacles.coors17, 0, 50, 250)
        obstacles.movement(18, obstacles.coors18, 0, 250, 800)
        obstacles.movement(19, obstacles.coors19, 0, 400, 800)
        obstacles.movespeed = 6
        obstacles.movement(20, obstacles.coors20, 0, 400, 800)
        obstacles.movespeed = 8
        obstacles.movement(21, obstacles.coors21, 0, 400, 800)
        obstacles.movespeed = 10
        obstacles.movement(22, obstacles.coors22, 0, 400, 800)
        obstacles.movespeed = 12
        obstacles.movement(23, obstacles.coors23, 0, 400, 800)
        obstacles.draw3()
        keys.toggleBox2()

    if currentbox == 3:         ## generating enemies and keys for box 3
        obstacles.movespeed = 4
        obstacles.movement(24, obstacles.coors24, 0, 150, 450)
        obstacles.movement(25, obstacles.coors25, 0, 150, 300)
        obstacles.movement(26, obstacles.coors26, 0, 400, 550)
        obstacles.movement(27, obstacles.coors27, 0, 150, 250)
        obstacles.movement(28, obstacles.coors28, 0, 150, 250)
        obstacles.movement(29, obstacles.coors29, 0, 50, 300)
        obstacles.movement(30, obstacles.coors30, 0, 400, 800)
        obstacles.movement(31, obstacles.coors31, 0, 700, 800)
        obstacles.movement(32, obstacles.coors32, 0, 850, 800)
        obstacles.draw4()
        keys.toggleBox3()

    if currentbox == 4:         ## generating enemies and keys for box 4
        obstacles.movespeed = 4
        obstacles.movement(33, obstacles.coors33, 0, 700, 900)
        obstacles.movement(34, obstacles.coors34, 0, 50, 250)
        obstacles.movespeed = 8
        obstacles.movement(35, obstacles.coors35, 0, 250, 800)
        obstacles.movement(36, obstacles.coors36, 0, 250, 800)
        obstacles.movespeed = 16
        obstacles.movement(37, obstacles.coors37, 0, 250, 800)
        obstacles.movement(38, obstacles.coors38, 0, 250, 800)
        obstacles.movespeed = 32
        obstacles.movement(39, obstacles.coors39, 0, 250, 800)
        obstacles.movement(40, obstacles.coors40, 0, 250, 800)
        obstacles.draw5()
        keys.toggleBox4()

    if currentbox == 5:         ## generating enemies and keys for box 5
        obstacles.movespeed = 4
        obstacles.movement(41, obstacles.coors41, 0, 50, 250)
        obstacles.movement(42, obstacles.coors42, 0, 100, 200)
        obstacles.movement(43, obstacles.coors43, 0, 100, 200)
        obstacles.movement(44, obstacles.coors44, 0, 100, 200)
        obstacles.movement(45, obstacles.coors45, 0, 350, 600)
        obstacles.movement(46, obstacles.coors46, 0, 700, 900)
        obstacles.movement(47, obstacles.coors47, 0, 750, 850)
        obstacles.movement(48, obstacles.coors48, 0, 750, 850)
        obstacles.movement(49, obstacles.coors49, 0, 750, 850)
        obstacles.draw6()
        keys.toggleBox5()
    
    if currentbox == 6:         ## generating enemies and keys for box 6
        obstacles.movespeed = 4
        obstacles.movement(50, obstacles.coors50, 1, 100, 200)
        obstacles.movement(51, obstacles.coors51, 1, 100, 200)
        obstacles.movement(52, obstacles.coors52, 1, 100, 200)
        obstacles.movement(53, obstacles.coors53, 1, 100, 200)
        obstacles.movement(54, obstacles.coors54, 1, 100, 200)
        obstacles.movement(55, obstacles.coors55, 1, 100, 200)
        obstacles.movement(56, obstacles.coors56, 1, 300, 650)
        obstacles.draw7()
        keys.toggleBox6()
    
    if currentbox == 7:         ## generating enemies and keys for box 7
        obstacles.movespeed = 4
        obstacles.movement(57, obstacles.coors57, 0, 50, 150)
        obstacles.movement(58, obstacles.coors58, 1, 350, 600)
        obstacles.movement(59, obstacles.coors59, 1, 350, 600)
        obstacles.movement(60, obstacles.coors60, 1, 350, 600)
        obstacles.movespeed = 8
        obstacles.movement(61, obstacles.coors61, 0, 300, 500)
        obstacles.movespeed = 6
        obstacles.movement(62, obstacles.coors62, 0, 350, 500)
        obstacles.movespeed = 7
        obstacles.movement(63, obstacles.coors63, 0, 400, 500)
        obstacles.movespeed = 5
        obstacles.movement(64, obstacles.coors64, 0, 450, 500)
        obstacles.draw8()
        keys.toggleBox7()

    if currentbox == 8:         ## generating enemies and keys for box 8
        obstacles.movespeed = 12
        obstacles.movement(66, obstacles.coors66, 1, 150, 550)
        obstacles.movement(67, obstacles.coors67, 1, 150, 550)
        obstacles.movement(68, obstacles.coors68, 1, 150, 550)
        obstacles.movement(73, obstacles.coors73, 1, 150, 550)
        obstacles.movement(74, obstacles.coors74, 1, 150, 550)
        obstacles.movement(75, obstacles.coors75, 1, 150, 550)
        obstacles.movement(65, obstacles.coors65, 0, 165, 780)
        obstacles.movement(69, obstacles.coors69, 0, 165, 780)
        obstacles.movement(70, obstacles.coors70, 0, 165, 780)
        obstacles.movement(71, obstacles.coors71, 0, 165, 780)
        obstacles.movement(72, obstacles.coors72, 0, 165, 780)
        obstacles.draw9()
        keys.toggleBox8()
    
    displayDeaths(deaths)
    keys.keyCountDisplay()

    keys.obtainKey(player.x, player.y, currentbox)
    if keys.keyTruth == True:
        player.updateK()
        keys.keyTruth = False

    died = player.trapped(trap) or obstacles.collide(player, currentbox)

    if died == True:
        player.updateD()

    for event in pygame.event.get():
        if event.type==QUIT:
            loop = False
        if event.type == KEYUP and event.key == K_p:
            pause = True
    
    pygame.display.flip()                                           #refresh display
    clock.tick(30)                                                 #fps

pygame.quit()                                                       
