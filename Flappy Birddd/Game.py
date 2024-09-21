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
        
        





            

