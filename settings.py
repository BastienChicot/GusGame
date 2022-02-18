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

gugus_width = 42
gugus_height = 44

lassl_face = pygame.image.load('Gus/LassL/lassl.png')
lassl_walkd1 = pygame.image.load('Gus/LassL/lassl_1.png')
lassl_walkd2 = pygame.image.load('Gus/LassL/lassl_2.png')
lassl_walkd = [lassl_walkd1,lassl_walkd2]

lassl_dos = pygame.image.load('Gus/LassL/lassl_dos.png')
lassl_walku1 = pygame.image.load('Gus/LassL/lassl_dos1.png')
lassl_walku2 = pygame.image.load('Gus/LassL/lassl_dos2.png')
lassl_walku = [lassl_walku1,lassl_walku2]

lassl_droite = pygame.image.load('Gus/LassL/lassl_r.png')
lassl_droite1 = pygame.image.load('Gus/LassL/lassl_r1.png')
lassl_droite2 = pygame.image.load('Gus/LassL/lassl_r2.png')
lassl_walkr = [lassl_droite1,lassl_droite2]

lassl_gauche = pygame.image.load('Gus/LassL/lassl_l.png')
lassl_gauche1 = pygame.image.load('Gus/LassL/lassl_l1.png')
lassl_gauche2 = pygame.image.load('Gus/LassL/lassl_l2.png')
lassl_walkl = [lassl_gauche1,lassl_gauche2]

lassl_width = 36
lassl_height = 62

gugus_move1 = pygame.image.load('Gus/Gus_move1.png')
gugus_move2 = pygame.image.load('Gus/Gus_move2.png')
gugus_move = [gugus_move1, gugus_move2]

fond_text = pygame.image.load("bank/image/zone_texte.png")
sac_image = pygame.image.load("bank/image/sac.png")
sac_tab = pygame.image.load("bank/image/sac_tab.png")
poze = pygame.image.load("bank/image/pause.png")

#PNJ
rat_left = pygame.image.load('bank/pnj/rat_g.png')
rat_right = pygame.image.load('bank/pnj/rat_d.png')

concierge_1=pygame.image.load('bank/pnj/concierge1.png')
concierge_2=pygame.image.load('bank/pnj/concierge2.png')
concierge = [concierge_1,concierge_2]

dame_left1 = pygame.image.load("bank/pnj/dameg1.png")
dame_left2 = pygame.image.load("bank/pnj/dameg2.png")
dame_left0 = pygame.image.load("bank/pnj/Dame_gauche.png")
dame_right1 = pygame.image.load("bank/pnj/damed1.png")
dame_right2 = pygame.image.load("bank/pnj/damed2.png")
dame_right0 = pygame.image.load("bank/pnj/Dame_droite.png")

dame_l = [dame_left1,dame_left2,dame_left0]
dame_d = [dame_right1,dame_right2,dame_right0]

vieille_bus = pygame.image.load("bank/pnj/vieille.png")
fond_bus = pygame.image.load("bank/pnj/fond_bus.png")
bouteille = pygame.image.load("bank/pnj/bouteille.png")
valise = pygame.image.load("bank/pnj/valise.png")
poussette = pygame.image.load("bank/pnj/poussette.png")

batteur0 = pygame.image.load("bank/pnj/batteur_0.png")
batteur1 = pygame.image.load("bank/pnj/batteur_1.png")
batteur2 = pygame.image.load("bank/pnj/batteur_2.png")
batteur = [batteur1,batteur2,batteur0]

bass0 = pygame.image.load("bank/pnj/bassiste0.png")
bass1 = pygame.image.load("bank/pnj/bassiste1.png")
bass2 = pygame.image.load("bank/pnj/bassiste2.png")
bassist = [bass1,bass2,bass0]

guit0 = pygame.image.load("bank/pnj/guitar0.png")
guit1 = pygame.image.load("bank/pnj/guitar1.png")
guit2 = pygame.image.load("bank/pnj/guitar2.png")
guitar = [guit1,guit2,guit0]


hook_left1 = pygame.image.load("bank/pnj/hooker/hooker_l1.png")
hook_left2 = pygame.image.load("bank/pnj/hooker/hooker_l2.png")
hook_left0 = pygame.image.load("bank/pnj/hooker/hooker_l0.png")
hook_right1 = pygame.image.load("bank/pnj/hooker/hooker_r1.png")
hook_right2 = pygame.image.load("bank/pnj/hooker/hooker_r2.png")
hook_right0 = pygame.image.load("bank/pnj/hooker/hooker_r0.png")

hook_l = [hook_left1,hook_left2,hook_left0]
hook_d = [hook_right1,hook_right2,hook_right0]
