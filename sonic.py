import os
import pygame
from pygame.locals import *
pygame.init()
def chemin(fichier):
    return os.path.join('Image', fichier)

fenetre = pygame.display.set_mode((1248,702), RESIZABLE)

BACKGROUD = pygame.image.load("background.png").convert()
fenetre.blit(BACKGROUD, (0,0))

pygame.display.flip()


continuer = 1
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("e")
            continuer = 0
            pygame.quit()
    pygame.display.flip()
