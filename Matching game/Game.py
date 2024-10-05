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