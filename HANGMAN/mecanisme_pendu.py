import pygame
from sys import exit
from Fonctions import *
from unidecode import unidecode

pygame.init()
pygame.font.init()

size = width, height = 940,540
screen = pygame.display.set_mode(size, pygame.RESIZABLE)

pygame.display.set_caption('HANGMAN')
pygame.display.set_icon(pygame.image.load('design/caticon.ico'))
background = pygame.image.load('design/background.png')

bgm = pygame.mixer.Sound('audio/happy.mp3')
bgm.set_volume(0.5)
bgm.play()

well_done = pygame.image.load('design/ingame/well_done.png')
try_again = pygame.image.load('design/ingame/try_again.png')

screen.blit(pygame.transform.smoothscale(background, size),(0,0))

clock = pygame.time.Clock()

"""
font = pygame.font.Font("bryndan-write-font/BryndanWrite.ttf", 97)
hangman = font.render("HANGMAN.", 1, (0,0,0))
screen.blit(hangman, (106,133))
"""

pygame.display.flip()


debutant = {"blue":"bleu",
            "difficult":"difficile",
            "other":"autre",
            "weird":"bizarre",
            "funny":"drôle",
            "strange":"étrange",
            "easy":"facile",
            "impossible": "impossible",
            "young":"jeune",
            "free":"libre",
            "sick":"malade",
            "same":"même",
            "poor":"pauvre",
            "clean":"propre",
            "dirty":"sale",
            "calm":"tranquille",
            "sad":"triste"}

font = pygame.font.Font("bryndan-write-font/BryndanWrite.ttf", 97)
color_values = r, g, b = (94,102,151) # ORIGINAL 'HANGMAN.' COLOR VALUES
color_values = r, g, b = (248,251,255) # couleur background
clock = pygame.time.Clock()

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
    clock.tick(65)

font = pygame.font.Font("bryndan-write-font/BryndanWrite.ttf", 20)
jeu_du_pendu_educatif = font.render("Jeu du pendu éducatif", True, (94,102,151))
tap_here_to_start = font.render("Appuyez sur une touche", True, (210,214,229))

screen.blit(hangman, (106,133))
screen.blit(jeu_du_pendu_educatif, (339,229))
screen.blit(tap_here_to_start, (190, 400))
pygame.display.flip()

HANGMAN = True
while HANGMAN:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            Running = True

            while Running :

                screen.blit(background,(0,0))
                pygame.display.flip()
                
                debutant, keys_debutant, mots_appris, word_et_trad = random_word(debutant)

                word, traduction = creation_liste_caractere((word_et_trad))
                display_word, display_trad = conversion_tirets(word, traduction)
                lettres_deja_rentrees = []

                font_ingame = pygame.font.Font("bryndan-write-font/BryndanWrite.ttf", 45)
                affichage_word_trad = " ".join(display_word) + " = " + " ".join(display_trad)
                screen.blit(font_ingame.render(affichage_word_trad, True, (r,g,b)), (350,260))
                pygame.display.flip()

                font_not_ingame = pygame.font.Font("bryndan-write-font/BryndanWrite.ttf", 30)

                mot_complet = False
                points = 0
                
                while points != 10 and not mot_complet:

                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            lettre = str(event)[32]

                            if lettre in word or lettre in traduction:
                                
                                for i in range(len(word)):
                                    if word[i] == lettre:
                                        display_word[i] = lettre

                                for j in range(len(traduction)):
                                    if traduction[j] == lettre:
                                        display_trad[j] = lettre

                                screen.blit(pygame.transform.smoothscale(background, size),(0,0))
                                affichage_word_trad = " ".join(display_word) + " = " + " ".join(display_trad)
                                screen.blit(font_ingame.render(affichage_word_trad, True, (r,g,b)), (350,260))
                                pygame.display.flip()


                            else:
                                screen.blit(pygame.transform.smoothscale(background, size),(0,0))
                                screen.blit(font_ingame.render("Mauvaise lettre !", True, (r,g,b)), (350,260))
                                points += 1
                                
                                if points == 10:
                                    screen.blit(pygame.transform.smoothscale(try_again, size),(0,0))
                                    screen.blit(font_not_ingame.render("Perdu ! Retentez :) ", True, (r,g,b)), (350,50))
                                    pygame.display.flip()

                            print (display_word, "=", display_trad, "\n Fautes :", points)

                            if word == display_word and traduction == display_trad :
                                mot_complet = True
                                screen.blit(pygame.transform.smoothscale(well_done, size),(0,0))
                                screen.blit(font_not_ingame.render("Well done!", True, (r,g,b)), ((385,60)))
                                pygame.display.flip()
                                
                Running = False                 

pygame.quit()
exit()
