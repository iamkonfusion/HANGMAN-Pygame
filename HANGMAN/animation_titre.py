import pygame
from sys import exit

pygame.init()
pygame.font.init()

size = width, height = 940,540
screen = pygame.display.set_mode(size, pygame.RESIZABLE)

pygame.display.set_caption('HANGMAN')
pygame.display.set_icon(pygame.image.load('design/caticon.ico'))
background = pygame.image.load('design/homescreen.png')
screen.blit(pygame.transform.smoothscale(background, size),(0,0))

font = pygame.font.Font("bryndan-write-font/BryndanWrite.ttf", 97)
# color_values = r, g, b = (94,102,151) # ORIGINAL 'HANGMAN.' COLOR VALUES
color_values = r, g, b = (248,251,255) # couleur background

while not (r < 94 and g < 102 and b < 151):
    if not r < 94 :
        r -= 1
    if not g < 102:
        g -= 1
    if not b < 151:
        b -= 1
    hangman = font.render("HANGMAN.", True, (r,g,b))
    screen.blit(hangman, (106,133))
    pygame.display.flip()
    pygame.time.wait(5)

font = pygame.font.Font("bryndan-write-font/BryndanWrite.ttf", 20)
jeu_du_pendu_educatif = font.render("Jeu du pendu éducatif", True, (94,102,151))
tap_here_to_start = font.render("Appuyez sur une touche", True, (210,214,229))

screen.blit(hangman, (106,133))
screen.blit(jeu_du_pendu_educatif, (339,229))
screen.blit(tap_here_to_start, (190, 400))
pygame.display.flip()

Running = True
while Running :

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # pygame.display.quit()
            exit()
            running = False

        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode(event.dict['size'], pygame.RESIZABLE)
            screen.blit(pygame.transform.scale(background, event.dict['size']), (0, 0))
            screen.blit(hangman, (106,133))
            screen.blit(jeu_du_pendu_educatif, (339,229))
            screen.blit(tap_here_to_start, (190, 400))
            pygame.display.flip()

        if event.type == pygame.KEYDOWN:            # registers 'pressed key' events
            if event.key == pygame.K_SPACE:
                print('Spacebar was pressed')

    pygame.display.flip()
