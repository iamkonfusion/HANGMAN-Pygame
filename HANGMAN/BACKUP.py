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
clock = pygame.time.Clock()

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

        if event.type == pygame.KEYDOWN:            # registers 'pressed key' events
            if event.key == pygame.K_SPACE:
                print('Spacebar was pressed')

    pygame.display.flip()




#############################################################





def partie():
    Playing = True # variable pour arrêter/continuer la partie

    while Playing:
        word, traduction = creation_liste_caractere(word_et_trad)
        display_word, display_trad = conversion_tirets(word, traduction)
        lettres_deja_rentrees = []

        mot_complet = False
        points = 0
            
        print (str(display_word), "=", str(display_trad))

        while points != 10 and not mot_complet:

            lettre = entrez_une_lettre(lettres_deja_rentrees)
            lettres_deja_rentrees.append(lettre)

            if lettre in word or lettre in traduction:                   # liste contenant chaque caractère du word
                for i in range(len(word)):
                    if word[i] == lettre:
                        display_word[i] = lettre

                for j in range(len(traduction)):
                    if traduction[j] == lettre:
                        display_trad[j] = lettre

            else:
                print ("Mauvaise lettre !")
                points += 1
                if points == 10:
                    print ("Perdu ! Retentez :)")

            print (display_word, "=", display_trad, "\n Fautes :", points)

            if word == display_word and traduction == display_trad :
                mot_complet = True
                print ("Well done!")

        Playing = False