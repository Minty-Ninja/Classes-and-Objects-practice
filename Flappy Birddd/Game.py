import pygame
from pygame.locals import *
import random


pygame.init()
clock= pygame.time.Clock()
width= 1500
height = 800
screen = pygame.display.set_mode((width,height)) #Construction of the screen
pygame.display.set_caption("Blappy Fird")
font1 = pygame.font.SysFont("Pacifico", 40)
col1 = (255,0,255) 

#Defining Game variables
imgright= 0
scspeed= 5
bfly = False
gameOver= False
gap= 100
Pipes= 1000
Timer= pygame.time.get_ticks()- Pipes
score= 0
passPipe= False


#Loading Images
Bg= pygame.image.load("bg.png")
Ground= pygame.image.load("ground.png")
Button = pygame.image.load("restart.png")


#Function to Display Text
def text(txt, font, textcol, x,y):
    tex= font.render(txt, True, textcol)
    screen.blit(tex, (x,y))


#Creating and Defining the Class
class Bird(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images= []
        self.index = 0
        self.conter = 0

        for i in range(1,4):
            img = pygame.image.load(f"bird{i}.png") #Format for using Variable in String
            self.images.append(img)
        
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y] #Rectangle goes to center of image
        self.velocity = 0
        self.clicked = False
    
    #Define Update
    def update(self): 
        if bfly:
            self.velocity+=1
            if self.velocity>20:
                self.velocity=20
            
            if self.rect.bottom<800:
                self.rect.y+=int(self.velocity)

        if not gameOver:
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked: #not self.clicked is to check if we're already not in clicked position
                self.clicked= True
                self.velocity -= 4

    
        #Making sure that click is reset back to false

            if pygame.mouse.get_pressed()[0] == 0 : 
                self.clicked= False

        #Bird Animation fr
        wingFlap= 9 # Cooldown for flapping of wings
        self.counter +=1
        
   ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import pygame
from pygame.locals import *
import random


pygame.init()
clock= pygame.time.Clock()
width= 864
height = 700
screen = pygame.display.set_mode((width,height)) #Construction of the screen
pygame.display.set_caption("Blappy Fird")
font1 = pygame.font.SysFont("Pacifico", 40)
col1 = (255,0,255) 

#Defining Game variables
imgright= 0
scspeed= 5
bfly = False
gameOver= False
gap= 100
Pipes= 1000
Timer= pygame.time.get_ticks()- Pipes
score= 0
passPipe= False
fps = 60

#Loading Images
Bg= pygame.image.load("bg.png")
Ground= pygame.image.load("ground.png")
button = pygame.image.load("restart.png")


#Function to Display Text
def text(txt, font, textcol, x,y):
    tex= font.render(txt, True, textcol)
    screen.blit(tex, (x,y))


#Creating and Defining the Class
class Bird(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images= []
        self.index = 0
        self.conter = 0

        for i in range(1,4):
            img = pygame.image.load(f"bird{i}.png") #Format for using Variable in String
            self.images.append(img)
        
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y] #Rectangle goes to center of image
        self.velocity = 0
        self.clicked = False
    
    #Define Update
    def update(self): 
        if bfly:
            self.velocity+=1
            if self.velocity>20:
                self.velocity=20
            
            if self.rect.bottom<800:
                self.rect.y+=int(self.velocity)

        if not gameOver:
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked: #not self.clicked is to check if we're already not in clicked position
                self.clicked= True
                self.velocity -= 4

    
        #Making sure that click is reset back to false

            if pygame.mouse.get_pressed()[0] == 0 : 
                self.clicked= False

            #Bird Animation fr
            wingFlap= 9 # Cooldown for flapping of wings
            self.counter +=1

            if self.counter>wingFlap: 
                self.counter=0
                self.index+=1

                if self.index>=len(self.images):
                    self.index=0

                self.image = self.images[self.index]

            #Rotating Bird when it flies
            self.image = pygame.transform.rotate(self.images[self.index], self.velocity*-2)
        else:
            self.image=pygame.transform.rotate(self.images[self.index], -90)


#Creating a class for Pipe
class Pipe (pygame.sprite.Sprite):
    def __init__(self, x, y, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("pipe.png")
        self.rect = self.image.get_rect()

        #Determine position for the pipe(1 for top, -1 for bottom)
        if pos ==1:
            self.image = pygame.transform.flip(self.image, False, True) #Flips image 180 degrees
            self.rect.bottomleft = [x,y -int(gap/2)]
        elif pos == -1:
            self.rect.topleft = [x , y+int(gap/2)]
        
    def update(self): #Moving pipes towards the left
        self.rect.x-= scspeed
        if self.rect.right<0:
            self.kill()


class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect= self.image.get_rect()
        self.rect.topleft = (x,y)

    def draw(self):
        action = False

        #Getting Mouse position
        Pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(Pos): 
            if pygame.mouse.get_pressed()[0] == 1:
                action = True
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action
    
# Creating Sprite Groups

# Group 1: Pipes
PipeGroup = pygame.sprite.Group()

#Group 2: Birds
BirdGroup = pygame.sprite.Group()

blappy = Bird(200, int(height/2))
BirdGroup.add(blappy)

Restart = Button(int(width/2), int(height/2), button)

run = True
while run:
    clock.tick(fps)
    screen.blit(Bg, (0,0))
    PipeGroup.draw(screen)
    BirdGroup.draw(screen)
    BirdGroup.update

    #Ground Scrolling
    screen.blit(Ground, (imgright, 768))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False

pygame.quit()

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

import pygame
from pygame.locals import *
import random


pygame.init()
clock= pygame.time.Clock()
width= 864
height = 700
screen = pygame.display.set_mode((width,height)) #Construction of the screen
pygame.display.set_caption("Blappy Fird")
font1 = pygame.font.SysFont("Pacifico", 70)
col1 = (255,0,255) 

#Defining Game variables
gscroll= 0
scspeed= 5
bfly = False
gameOver= False
gap= 100
Pipes= 1000
Timer= pygame.time.get_ticks()- Pipes
score= 0
passPipe= False
fps = 60

#Loading Images
Bg= pygame.image.load("bg.png")
Ground= pygame.image.load("ground.png")
button = pygame.image.load("restart.png")


#Function to Display Text
def text(txt, font, textcol, x,y):
    tex= font.render(txt, True, textcol)
    screen.blit(tex, (x,y))

#Function for Restarting Game
def Restartt():
    PipeGroup.empty()
    blappy.rect.x = 100
    blappy.rect.y = 350
    score = 0
    return score




#Creating and Defining the Class
class Bird(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images= []
        self.index = 0
        self.counter = 0

        for i in range(1,4):
            img = pygame.image.load(f"bird{i}.png") #Format for using Variable in String
            self.images.append(img)
        
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y] #Rectangle goes to center of image
        self.velocity = 0
        self.clicked = False
    
    #Define Update
    def update(self): 
        if bfly:
            self.velocity+=0.1
            if self.velocity>2:
                self.velocity=2
            
            if self.rect.bottom<800:
                self.rect.y+=int(self.velocity)

        if not gameOver:
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked: #not self.clicked is to check if we're already not in clicked position
                self.clicked= True
                self.velocity -= 4

    
        #Making sure that click is reset back to false

            if pygame.mouse.get_pressed()[0] == 0 : 
                self.clicked= False

            #Bird Animation fr
            wingFlap= 9 # Cooldown for flapping of wings
            self.counter +=1

            if self.counter>wingFlap: 
                self.counter=0
                self.index+=1

                if self.index>=len(self.images):
                    self.index=0

                self.image = self.images[self.index]

            #Rotating Bird when it flies
            self.image = pygame.transform.rotate(self.images[self.index], self.velocity*-2)
        else:
            self.image=pygame.transform.rotate(self.images[self.index], -90)


#Creating a class for Pipe
class Pipe (pygame.sprite.Sprite):
    def __init__(self, x, y, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("pipe.png")
        self.rect = self.image.get_rect()

        #Determine position for the pipe(1 for top, -1 for bottom)
        if pos ==1:
            self.image = pygame.transform.flip(self.image, False, True) #Flips image 180 degrees
            self.rect.bottomleft = [x,y -int(gap/2)]
        elif pos == -1:
            self.rect.topleft = [x , y+int(gap/2)]
        
    def update(self): #Moving pipes towards the left
        self.rect.x-= scspeed
        if self.rect.right<0:
            self.kill()


class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect= self.image.get_rect()
        self.rect.topleft = (x,y)

    def draw(self):
        action = False

        #Getting Mouse position
        Pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(Pos): 
            if pygame.mouse.get_pressed()[0] == 1:
                action = True
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action
    
# Creating Sprite Groups

# Group 1: Pipes
PipeGroup = pygame.sprite.Group()

#Group 2: Birds
BirdGroup = pygame.sprite.Group()

blappy = Bird(200, int(height/2))
BirdGroup.add(blappy)

Restart = Button(int(width/2), int(height/2), button)

run = True
while run:
    clock.tick(fps)
    screen.blit(Bg, (0,0))
    PipeGroup.draw(screen)
    BirdGroup.draw(screen)
    BirdGroup.update()

    #Ground Scrolling
    screen.blit(Ground, (gscroll, 568))
    #Updating the Score
    if len(PipeGroup)>0:
        #If Bird Passes Pipe
        if BirdGroup.sprites()[0].rect.left>PipeGroup.sprites()[0].rect.left\
        and BirdGroup.sprites()[0].rect.right<PipeGroup.sprites()[0].rect.left\
        and not passPipe: 
            passPipe = True
       
        if passPipe and BirdGroup.sprite()[0].rect.left>PipeGroup.sprites()[0].rect.right: 
            passPipe = False
            score+=1
        
    text(str(score), font1, col1, 432, 20 )
    
    #Checking Collision of Bird with Pipe
    if pygame.sprite.groupcollide(PipeGroup, BirdGroup, False, False)\
    or blappy.rect.top<0:
        gameOver = True
        bfly = False
    if blappy.rect.bottom>700:
        gameOver = True
        bfly = False
    if bfly and not gameOver: 
        timee = pygame.time.get_ticks()
        if timee - Timer > Pipes : 
            pipeHeight = random.randint(-100,100)
            bPipe = Pipe(width, int(height/2)+pipeHeight, -1)
            tPipe = Pipe(width, int(height/2)+pipeHeight, 1)
            PipeGroup.add (bPipe)
            PipeGroup.add(tPipe)
            Timer= timee
        PipeGroup.update()
        #Scrolling the Ground
        gscroll -= scspeed
        if abs (gscroll)>35:
            gscroll = 0

    if gameOver: 
        if Restart.draw():
            gameOver = False
            score= Restartt()
        





    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and not bfly and not gameOver: 
            bfly = True

    pygame.display.update()

pygame.quit()







        
        





            





        
        





            







            

