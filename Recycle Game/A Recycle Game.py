import pygame
import random
import time
from pygame.locals import *

#Defining the screen
def scrn(img):
    BG= pygame.image.load(img)
    bg1= pygame.transform.scale(BG, (width,height))
    screen.blit(bg1, (0,0))

#Initialising pygame and caption
pygame.init()
pygame.display.set_caption("Recycle Gamee")
width=1500
height=800
screen=pygame.display.set_mode([width,height])




#While loop
run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    scrn("BG.jpg")
    pygame.display.update()
pygame.quit()


--------------------------------------------------------------------------------------------------------------------------------------------------------------------






import pygame
import random
import time
from pygame.locals import *

#Defining the screen
def scrn(img):
    BG= pygame.image.load(img)
    bg1= pygame.transform.scale(BG, (width,height))
    screen.blit(bg1, (0,0))


#Initialising pygame and caption
pygame.init()
pygame.display.set_caption("Recycle Game")
width=1500
height=800
screen=pygame.display.set_mode([width,height])

#Create a classsssssssssssss
class Bin(pygame.sprite.Sprite):
    def __init__():
        self.image = pygame.image.load("AYB.png").convert_alpha()#Alpha makes image pixelated fr
        self.image= pygame.transform.scale(self.image, (40,50))
        self.rect = self.image.get_rect()   #Creating a rectangle
    
class Recycle(pygame.sprite.Sprite):
    def __init__(self,img):
        self.image = pygame.image.load(img).convert_alpha()#Alpha makes image pixelated fr
        self.image= pygame.transform.scale(self.image, (40,50))
        self.rect = self.image.get_rect()   #Creating a rectangle
    
 
class NonRecycle (pygame.sprite.Sprite):
    def __init__(self,img):
        self.image = pygame.image.load("PBAG.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40,50))
        self.rect = self.image.get_rect()

Recyclable= ["PBALL.png", "PENCIL.png", "PSTRAW.png"] 

#Creating groups
items= pygame.sprite.Group()
grecycle = pygame.sprite.Group()
nonrecycle = pygame.sprite.Group()

#Placing recyclable items
for i in range (30):
    m = Recycle(random.choice(Recyclable))
    m.rect.x = random.randint(0,1500)
    m.rect.y = random.randint(0,800)
    grecycle.add(m)
    items.add(m)

#Placing Non Recyclable items
for i in range(30):
    nr = NonRecycle()
    nr.rect.x = random.randint(0,1500)
    nr.rect.y = random.randint(0,800)
    nonrecycle.add(nr)
    items.add(nr)

#Creating/Placing Bin
B = Bin()
items.add(B)    

#Defining Common Variables
col1 = (25,122,34)
col2= (76,94,12)
clock = pygame.time.Clock()
start_time = time.time()
font1= pygame.font.SysFont("Helvetica", 40)
font2 = pygame.font.SysFont("Times New Roman", 20)

text= font1.render("Score= "+ str(0), True, col1)


#While loop
run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    scrn("BG.jpg")
    items.draw(screen)
    pygame.display.update()
pygame.quit()



-----------------------------------------------------------------------------------------------------------------------------------------------------------------

import pygame
import random
import time
from pygame.locals import *

#Defining the screen
def scrn(img):
    BG= pygame.image.load(img)
    bg1= pygame.transform.scale(BG, (width,height))
    screen.blit(bg1, (0,0))


#Initialising pygame and caption
pygame.init()
pygame.display.set_caption("Recycle Game")
width=1500
height=800
screen=pygame.display.set_mode([width,height])

#Create a classsssssssssssss
class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("AYB.png").convert_alpha()#Alpha makes image pixelated fr
        self.image= pygame.transform.scale(self.image, (70,60))
        self.rect = self.image.get_rect()   #Creating a rectangle
    
class Recycle(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()#Alpha makes image pixelated fr
        self.image= pygame.transform.scale(self.image, (40,50))
        self.rect = self.image.get_rect()   #Creating a rectangle
    
 
class NonRecycle (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("PBAG.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40,50))
        self.rect = self.image.get_rect()


Recyclable= ["PBALL.png", "PENCIL.png", "PSTRAW.png"] 

#Creating groups
items= pygame.sprite.Group()
grecycle = pygame.sprite.Group()
nonrecycle = pygame.sprite.Group()

#Placing recyclable items
for i in range (30):
    m = Recycle(random.choice(Recyclable))
    m.rect.x = random.randint(0,1500)
    m.rect.y = random.randint(0,800)
    grecycle.add(m)
    items.add(m)

#Placing Non Recyclable items
for i in range(30):
    nr = NonRecycle()
    nr.rect.x = random.randint(0,1500)
    nr.rect.y = random.randint(0,800)
    nonrecycle.add(nr)
    items.add(nr)

#Creating/Placing Bin
B = Bin()
items.add(B)    

#Defining Common Variables
col1 = (225,2,15)
col2= (76,4,12)
clock = pygame.time.Clock()
start_time = time.time()
font1= pygame.font.SysFont("Helvetica", 40)
font2 = pygame.font.SysFont("Times New Roman", 20)

text= font1.render("Score= "+ str(0), True, col1)


#While loop
run=True
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    scrn("BG.jpg")
    screen.blit(text, (750,10))
    items.draw(screen)
    pygame.display.update()
pygame.quit()

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

import pygame
import random
import time
from pygame.locals import *

#Defining the screen
def scrn(img):
    BG= pygame.image.load(img)
    bg1= pygame.transform.scale(BG, (width,height))
    screen.blit(bg1, (0,0))


#Initialising pygame and caption
pygame.init()
pygame.display.set_caption("Recycle Game")
width=1500
height=800
screen=pygame.display.set_mode([width,height])

#Create a classsssssssssssss
class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("AYB.png").convert_alpha()#Alpha makes image pixelated fr
        self.image= pygame.transform.scale(self.image, (70,60))
        self.rect = self.image.get_rect()   #Creating a rectangle
    
class Recycle(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()#Alpha makes image pixelated fr
        self.image= pygame.transform.scale(self.image, (40,50))
        self.rect = self.image.get_rect()   #Creating a rectangle
    
 
class NonRecycle (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("PBAG.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40,50))
        self.rect = self.image.get_rect()


Recyclable= ["PBALL.png", "PENCIL.png", "PSTRAW.png"] 

#Creating groups
items= pygame.sprite.Group()
grecycle = pygame.sprite.Group()
nonrecycle = pygame.sprite.Group()

#Placing recyclable items
for i in range (30):
    m = Recycle(random.choice(Recyclable))
    m.rect.x = random.randint(0,1500)
    m.rect.y = random.randint(0,800)
    grecycle.add(m)
    items.add(m)

#Placing Non Recyclable items
for i in range(30):
    nr = NonRecycle()
    nr.rect.x = random.randint(0,1500)
    nr.rect.y = random.randint(0,800)
    nonrecycle.add(nr)
    items.add(nr)

#Creating/Placing Bin
B = Bin()
items.add(B)    

#Defining Common Variables
col1 = (225,2,15)
col2= (76,4,12)
clock = pygame.time.Clock()
start_time = time.time()
font1= pygame.font.SysFont("Helvetica", 40)
font2 = pygame.font.SysFont("Times New Roman", 20)
score=0

text= font1.render("Score= "+ str(0), True, col1)



e1 = []
e2 = [] #Empty lists for idk wht

#While loop
run=True
while run:
    scrn("BG.jpg")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys= pygame.key.get_pressed() #Using Keys for Movement
    if keys[pygame.K_UP]:
        if B.rect.y>0:
            B.rect.y-= 80
    if keys[pygame.K_DOWN]:
        if B.rect.y<800:
            B.rect.y+= 50
    if keys[pygame.K_LEFT]:
        if B.rect.x>0:
            B.rect.x-= 50
    if keys[pygame.K_RIGHT]:
        if B.rect.x<1500:
            B.rect.x+= 50
    nHit= pygame.sprite.spritecollide(B,grecycle,True)
    bHit = pygame.sprite.spritecollide(B,nonrecycle,True)
    for i in nHit:
        score+=1
        text=font1.render("Score= "+str(score),True,col1)
    for i in bHit:
        score-=1
        text=font1.render("Score= "+str(score), True, col1)


    

    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.blit(text, (750,10))
    items.draw(screen)
    pygame.display.update()
pygame.quit()


-------------------------------------------------------------------------------------------------------------------------------------------------------------------

import pygame
import random
import time
from pygame.locals import *

#Defining the screen
def scrn(img):
    BG= pygame.image.load(img)
    bg1= pygame.transform.scale(BG, (width,height))
    screen.blit(bg1, (0,0))


#Initialising pygame and caption
pygame.init()
pygame.display.set_caption("Recycle Game")
width=1500
height=800
screen=pygame.display.set_mode([width,height])

#Create a classsssssssssssss
class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("AYB.png").convert_alpha()#Alpha makes image pixelated fr
        self.image= pygame.transform.scale(self.image, (70,60))
        self.rect = self.image.get_rect()   #Creating a rectangle
    
class Recycle(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()#Alpha makes image pixelated fr
        self.image= pygame.transform.scale(self.image, (40,50))
        self.rect = self.image.get_rect()   #Creating a rectangle
    
 
class NonRecycle (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("PBAG.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40,50))
        self.rect = self.image.get_rect()


Recyclable= ["PBALL.png", "PENCIL.png", "PSTRAW.png"] 

#Creating groups
items= pygame.sprite.Group()
grecycle = pygame.sprite.Group()
nonrecycle = pygame.sprite.Group()

#Placing recyclable items
for i in range (30):
    m = Recycle(random.choice(Recyclable))
    m.rect.x = random.randint(0,1500)
    m.rect.y = random.randint(0,800)
    grecycle.add(m)
    items.add(m)

#Placing Non Recyclable items
for i in range(30):
    nr = NonRecycle()
    nr.rect.x = random.randint(0,1500)
    nr.rect.y = random.randint(0,800)
    nonrecycle.add(nr)
    items.add(nr)

#Creating/Placing Bin
B = Bin()
items.add(B)    

#Defining Common Variables
col1 = (255,2,15)
col2= (255, 0, 255)
clock = pygame.time.Clock()
start_time = time.time()
font1= pygame.font.SysFont("Helvetica", 50)
font2 = pygame.font.SysFont("Times New Roman", 50)
score=0

text= font1.render("Score= "+ str(0), True, col1)



e1 = []
e2 = [] #Empty lists for idk wht

#While loop
run=True
while run:
    scrn("BG.jpg")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    timeT= time.time()-start_time
    if timeT >= 30:
        if score >= 7:
            text = font1.render("You Win !!!", True, col1)
            text2 = font1.render("Score: "+ str(score), True, col1)
    
        else:
            text = font1.render("You Loose !!!", True, col1)
            text2 = font1.render("Score: "+ str(score), True, col1)
            

        screen.blit(text, (750,400))
        screen.blit(text2, (750, 300))
    else:       
        counter= font2.render("Time Left: "+str(30-int(timeT)), True, col2)
        screen.blit(counter, (1000,750))



        keys= pygame.key.get_pressed() #Using Keys for Movement
        if keys[pygame.K_UP]:
            if B.rect.y>0:
                B.rect.y-= 80
        if keys[pygame.K_DOWN]:
            if B.rect.y<800:
                B.rect.y+= 50
        if keys[pygame.K_LEFT]:
            if B.rect.x>0:
                B.rect.x-= 50
        if keys[pygame.K_RIGHT]:
            if B.rect.x<1500:
                B.rect.x+= 50
        nHit= pygame.sprite.spritecollide(B,grecycle,True)
        bHit = pygame.sprite.spritecollide(B,nonrecycle,True)
        for i in nHit:
            score+=1
            text=font1.render("Score= "+str(score),True,col1)
        for i in bHit:
            score-=1
            text=font1.render("Score= "+str(score), True, col1)


        

        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.blit(text, (750,10))
        items.draw(screen)
    pygame.display.update()
pygame.quit()














