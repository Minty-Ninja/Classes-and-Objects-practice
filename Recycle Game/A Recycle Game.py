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


