# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 14:31:40 2021

@author: basti
"""
import pygame
pygame.mixer.pre_init(44100, -16, 1, 4096)
pygame.mixer.init()

import os

step_path = os.path.join("bank", "son", "step.ogg")
click_path = os.path.join("bank", "son", "click.ogg")
enter_path = os.path.join("bank", "son", "enter.ogg")
other_path = os.path.join("bank", "son", "other.ogg")
find_path = os.path.join("bank", "son", "find.ogg")
step_s = pygame.mixer.Sound(step_path)
step_s.set_volume(0.5)
click_ = pygame.mixer.Sound(click_path)
click_.set_volume(0.5)
enter_s = pygame.mixer.Sound(enter_path)
enter_s.set_volume(0.75)
other_s = pygame.mixer.Sound(other_path)
other_s.set_volume(0.1)
find_s = pygame.mixer.Sound(find_path)
find_s.set_volume(0.15)

display_width = 500
display_height = 500

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

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

#PNJ
rat_left = pygame.image.load('bank/pnj/rat_g.png')
rat_right = pygame.image.load('bank/pnj/rat_d.png')
