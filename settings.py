# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 14:31:40 2021

@author: basti
"""
import pygame

display_width = 500
display_height = 500

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

gugus_face = pygame.image.load('Gus/Gus.png')
gugus_walkdown_1 = pygame.image.load('Gus/Gus_1.png')
gugus_walkdown_2 = pygame.image.load('Gus/Gus_2.png')
gugus_walkdown = [gugus_walkdown_1,gugus_walkdown_2]

gugus_dos = pygame.image.load('Gus/Gus_dos.png')
gugus_walkup1 = pygame.image.load('Gus/Gus_dos_1.png')
gugus_walkup2 = pygame.image.load('Gus/Gus_dos_2.png')
gugus_walkup = [gugus_walkup1,gugus_walkup2]

gugus_droite = pygame.image.load('Gus/Gus_droit.png')
gugus_droite1 = pygame.image.load('Gus/Gus_droit_1.png')
gugus_droite2 = pygame.image.load('Gus/Gus_droit_2.png')
gugus_walkright = [gugus_droite1,gugus_droite2]

gugus_gauche = pygame.image.load('Gus/Gus_gauche.png')
gugus_gauche1 = pygame.image.load('Gus/Gus_gauche_1.png')
gugus_gauche2 = pygame.image.load('Gus/Gus_gauche_2.png')
gugus_walkleft = [gugus_gauche1,gugus_gauche2]

gugus_width = 48
gugus_height = 52

fond_text = pygame.image.load("bank/image/zone_texte.png")
sac_image = pygame.image.load("bank/image/sac.png")
sac_tab = pygame.image.load("bank/image/sac_tab.png")
poze = pygame.image.load("bank/image/pause.png")
