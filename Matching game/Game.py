import pygame
pygame.init()
screen= pygame.display.set_mode((864, 500))
screen.fill("white")
pygame.display.update()

#Loading Images
ACL = pygame.image.load("Assassins-Creed-Logo.png")
BS = pygame.image.load("Brawl Stars.jpg")
ER = pygame.image.load("Elden Ring.jpg")
IW = pygame.image.load ("COD IW.jpg")


screen.blit(ACL, (108, 200))
screen.blit(BS, (108, 300 ))
screen.blit(ER, (108, 400))
screen.blit(IW, (108,100))
pygame.display.update()


run =True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()



--------------------------------------------------------------------------------------------------------------------------------------------------------------------

import pygame
pygame.init()
screen= pygame.display.set_mode((864, 500))
screen.fill("white")
pygame.display.update()

#Loading Images
ACL = pygame.image.load("Assassins-Creed-Logo.png")
BS = pygame.image.load("Brawl Stars.jpg")
ER = pygame.image.load("Elden Ring.jpg")
IW = pygame.image.load ("COD IW.jpg")


screen.blit(ACL, (108, 150))
screen.blit(BS, (108, 250 ))
screen.blit(ER, (108, 400))
screen.blit(IW, (108,50))

#Function to Display Text
font1 = pygame.font.SysFont("Helvetica", 40)
col1= (255,0,255)
def text(txt, font, textcol, x,y):
    tex= font.render(txt, True, textcol)
    screen.blit(tex, (x,y))

text("Elden Ring",font1, col1, 600,200)
text("COD IW",font1, col1, 600,300)
text("Assasins Creed",font1, col1, 600,400)
text("Brawl Stars",font1, col1, 600,100)
pygame.display.update()

run =True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    event = pygame.event.poll() 
    if event.type == pygame.MOUSEBUTTONDOWN:
        position = pygame.mouse.get_pos()
        pygame.draw.circle(screen,(0,0,0),(position),20,5)
        pygame.display.update()
    elif event.type == pygame.MOUSEBUTTONUP: 
        pos = pygame.mouse.get_pos()
        pygame.draw.line(screen, (0,0,0),(position),(pos),5)
        pygame.draw.circle(screen,(0,0,0),(pos),20,5)
        pygame.display.update()










pygame.quit()
