import pygame
from sys import exit

pygame.init() #starts & initiates pygame (IMPORTANT)
screen = pygame.display.set_mode((600,400)) #création de la fenêtre + ! ARGUMENT = TUPLE (hauteur,largeur)
pygame.display.set_caption('HANGMAN')
clock = pygame.time.Clock() # framerate control

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    clock.tick(60) # ceiling = 60 FPS
    
