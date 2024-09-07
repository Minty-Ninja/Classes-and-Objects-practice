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
