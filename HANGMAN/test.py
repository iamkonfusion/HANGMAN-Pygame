import pygame
from sys import exit

pygame.init()

size = width, height = 940,540
screen = pygame.display.set_mode(size)

pygame.display.set_caption('HANGMAN')
pygame.display.set_icon(pygame.image.load('design/caticon.ico'))
background = pygame.image.load('design/background.png')
screen.blit(pygame.transform.smoothscale(background, size),(0,0))
pygame.display.flip()


################ CLASS BUTTON ####################


class Button():
    def __init__(self, x, y, image, scale):
        width, height = image.get_width(), image.get_height()
        self.image = pygame.transform.scale(image,(int(width*scale),int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0 :
            self.clicked = False
        # draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action

#LOAD BUTTON IMAGES
classique_img = pygame.image.load('design/buttons/classique.png').convert_alpha()
classique_button = Button(100,200, classique_img, 0.15)

##################################################

Running = True
while Running :

    if classique_button.draw():
        print ('Mode Partie Classique')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # pygame.display.quit()
            exit()
            running = False

        if event.type == pygame.KEYDOWN:            # registers 'pressed key' events
            if event.key == pygame.K_SPACE:
                print('Spacebar was pressed')

    pygame.display.flip()
