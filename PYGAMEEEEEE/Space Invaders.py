import pygame
import os
from pygame.locals import *
pygame.font.init()
width,height=1500,800
screen=pygame.display.set_mode((width, height))
pygame.display.set_caption("Space Invaders 2")
green=(0,255,0)
red=(255,0,0)
blue=(0,0,255)
C4= (166,209,178)
#x= pygame.Rect((500,0), 20, 500)
fnt1= pygame.font.SysFont("Helvetica", 50)
fnt2= pygame.font.SysFont("Arial", 250)
health1=15
health2=10
spc1= pygame.image.load("P1.png")
spc2=pygame.image.load("P2.png")
bg= pygame.transform.scale(pygame.image.load("Space.jpg"),(1500,1000))
fps=60
velocity=50
velocityB=20
border=pygame.Rect(750,0,5,1000)
#class definition
class Movement(pygame.sprite.Sprite):
    def __init__(self, image, angle, x, y):
        super().__init__()
        self.image = pygame.transform.rotate(pygame.transform.scale(image, (200,150)), angle)
        self.rect= self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def vertical(self, vel):
        self.rect.move_ip(0, vel)
        if self.rect.top<=0 or self.rect.bottom>=height:
            self.rect.move_ip(0,-vel)
    def horizontal(self, vel, pl):
        self.rect.move_ip(vel, 0)
        if pl==1:
            if self.rect.left<=0 or self.rect.right>=border.left:
                self.rect.move_ip(-vel,0)
        if pl==2:
            if self.rect.left<=border.right or self.rect.right>=1500:
                self.rect.move_ip(-vel,0)
P1= Movement(spc1,270, 375,500)
P2 = Movement(spc2, 90, 1125, 500) 
Sprites= pygame.sprite.Group()
Sprites.add(P1)
Sprites.add(P2)
def OCA():
    screen.blit(bg, (0,0))
    pygame.draw.rect(screen,C4,border)
    GTxt = fnt1.render("Health: "+str(health1),1,green)
    Btxt= fnt1.render("Health: "+str(health2), 1, blue)
    screen.blit(GTxt,(375,50))
    screen.blit(Btxt, (1125,50))
runl=True
clock=pygame.time.Clock()
gblt=[]
bblt=[]
def bet():
    for i in gblt:
        pygame.draw.rect(screen, green, i)
        i.x+=velocityB
    for i in bblt:
        pygame.draw.rect(screen, blue, i)
        i.x-=velocityB
ghit=pygame.USEREVENT+1
bhit=pygame.USEREVENT+2
def handle():
    global health1, health2
    for i in gblt:
        if P1.rect.colliderect(i):
            health1=health1-1
            gblt.remove(i)
        elif i.x>1500:
            gblt.remove(i)
    for i in bblt:
        if P2.rect.colliderect(i):
            pygame.event.post(pygame.event.Event(bhit))
            bblt.remove(i)
        elif i.x>0:
            bblt.remove(i)
    for colblt in gblt:
        for colbllt in bblt:
            if colblt.colliderect(colbllt):
                gblt.remove(colblt)
                bblt.remove(colbllt)

def win(text):
    winner= fnt2.render(text, 1, C4)
    screen.blit(winner, (150, 300))
    pygame.display.update()
    pygame.time.delay(1000)
while runl:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == QUIT:
            runl=False
        if event.type == KEYDOWN:
            if event.key == K_LCTRL:
                bullet = pygame.Rect(P1.rect.x+P1.rect.width, P1.rect.y+P1.rect.height//2, 7,4)
                gblt.append(bullet)
            if event.key == K_RCTRL:
                bullet = pygame.Rect(P2.rect.x, P2.rect.y+P2.rect.height//2, 7,4)
                bblt.append(bullet)
        if event.type == ghit:
            health1-=1
        if event.type == bhit:
            health2-=1
    keys_pressed=pygame.key.get_pressed()
    if keys_pressed[K_a]:
        P1.horizontal(-velocity,1)
    if keys_pressed[K_d]:
        P1.horizontal(velocity,1)
    if keys_pressed[K_w]:
        P1.vertical(-velocity)
    if keys_pressed[K_s]:
        P1.vertical(velocity)
    #Second Player movement
    if keys_pressed[K_LEFT]:
        P2.horizontal(-velocity,2)
    if keys_pressed[K_RIGHT]:
        P2.horizontal(velocity,2)
    if keys_pressed[K_UP]:
        P2.vertical(-velocity)
    if keys_pressed[K_DOWN]:
        P2.vertical(velocity)
    handle()
    OCA()
    Sprites.draw(screen)
    bet()
    if health1<=0:
        winner="Player 2 Wins!"
        win(winner)
        runl= False

    if health2<=0:
        winner="Player 1 Wins!"
        win(winner)
        runl= False

    pygame.display.update()



pygame.quit()


