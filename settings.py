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
step_s.set_volume(0.1)
click_ = pygame.mixer.Sound(click_path)
click_.set_volume(0.5)
enter_s = pygame.mixer.Sound(enter_path)
enter_s.set_volume(0.75)
other_s = pygame.mixer.Sound(other_path)
other_s.set_volume(0.1)
find_s = pygame.mixer.Sound(find_path)
find_s.set_volume(0.15)

#####PLAYLIST#####
playlist = list()

playlist.append("bank/musiques/Gus_track_1.wav")
playlist.append("bank/musiques/Gus_track_2.wav")
playlist.append("bank/musiques/Gus_track_5.wav")
playlist.append("bank/musiques/Gus_track_6.wav")
playlist.append("bank/musiques/Gus_track_7.wav")
playlist.append("bank/musiques/Gus_track_8.wav")
playlist.append("bank/musiques/Gus_track_9.wav")
playlist.append("bank/musiques/Gus_track_11.wav")
playlist.append("bank/musiques/Gus_track_12.wav")

pygame.mixer.music.set_volume(0.0)

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

gus_fight_r1 = pygame.image.load("Gus/gus_fight/gus_fr1.png")
gus_fight_r2 = pygame.image.load("Gus/gus_fight/gus_fr2.png")
gus_fight_l1 = pygame.image.load("Gus/gus_fight/gus_lr1.png")
gus_fight_l2 = pygame.image.load("Gus/gus_fight/gus_lr2.png")

gus_fight_right = [gus_fight_r1,gus_fight_r2,gus_fight_r1,gus_fight_r2]
gus_fight_left = [gus_fight_l1,gus_fight_l2,gus_fight_l1,gus_fight_l2]

gus_pch_r1 = pygame.image.load("Gus/gus_fight/gus_punch_r1.png")
gus_pch_r2 = pygame.image.load("Gus/gus_fight/gus_punch_r2.png")
gus_pch_l1 = pygame.image.load("Gus/gus_fight/gus_punch_l1.png")
gus_pch_l2 = pygame.image.load("Gus/gus_fight/gus_punch_l2.png")

gus_pch_r = [gus_pch_r1,gus_pch_r1,gus_pch_r2,gus_pch_r2]
gus_pch_l = [gus_pch_l1,gus_pch_l1,gus_pch_l2,gus_pch_l2]


gus_kick1 = pygame.image.load("Gus/gus_fight/gus_kick_r1.png")
gus_kick2 = pygame.image.load("Gus/gus_fight/gus_kick_r2.png")
gus_kick3 = pygame.image.load("Gus/gus_fight/gus_kick_r3.png")
gus_kick4 = pygame.image.load("Gus/gus_fight/gus_kick_r4.png")

gus_kick1_l = pygame.transform.flip(gus_kick1, True, False)
gus_kick2_l = pygame.transform.flip(gus_kick2, True, False)
gus_kick3_l = pygame.transform.flip(gus_kick3, True, False)
gus_kick4_l = pygame.transform.flip(gus_kick4, True, False)

gus_kick_r = [gus_kick1,gus_kick2,gus_kick3,gus_kick4]
gus_kick_l = [gus_kick1_l,gus_kick2_l,gus_kick3_l,gus_kick4_l]

gus_sp1 = pygame.image.load("Gus/gus_fight/gus_super_punch2.png")
gus_sp2 = pygame.image.load("Gus/gus_fight/gus_super_punch1.png")

gus_sp1_l = pygame.transform.flip(gus_sp1, True, False)
gus_sp2_l = pygame.transform.flip(gus_sp2, True, False)

gus_sp_r = [gus_sp1,gus_sp1,gus_sp2,gus_sp2]
gus_sp_l = [gus_sp1_l,gus_sp1_l,gus_sp2_l,gus_sp2_l]

gus_jp1 = pygame.image.load("Gus/gus_fight/gus_jp1.png")
gus_jp2 = pygame.image.load("Gus/gus_fight/gus_jp2.png")
gus_jp3 = pygame.image.load("Gus/gus_fight/gus_jp3.png")
gus_jp4 = pygame.image.load("Gus/gus_fight/gus_jp4.png")

gus_jp1_l = pygame.transform.flip(gus_jp1, True, False)
gus_jp2_l = pygame.transform.flip(gus_jp2, True, False)
gus_jp3_l = pygame.transform.flip(gus_jp3, True, False)
gus_jp4_l = pygame.transform.flip(gus_jp4, True, False)

gus_jp_r = [gus_jp1,gus_jp2,gus_jp3,gus_jp4]
gus_jp_l = [gus_jp1_l,gus_jp2_l,gus_jp3_l,gus_jp4_l]

gus_ouille1 = pygame.image.load("Gus/gus_fight/gus_hitted1.png")
gus_ouille2 = pygame.image.load("Gus/gus_fight/gus_hitted2.png")

gus_ouille1_l = pygame.transform.flip(gus_ouille1, True, False)
gus_ouille2_l = pygame.transform.flip(gus_ouille2, True, False)

gus_ouille_r = [gus_ouille1,gus_ouille1,gus_ouille2,gus_ouille2]
gus_ouille_l = [gus_ouille1_l,gus_ouille1_l,gus_ouille2_l,gus_ouille2_l]


fighter_r1 = pygame.image.load("Gus/fighter_1/fighter_1.png")
fighter_r2 = pygame.image.load("Gus/fighter_1/fighter_1_2.png")
fighter_l1 = pygame.transform.flip(fighter_r1, True, False)
fighter_l2 = pygame.transform.flip(fighter_r2, True, False)

fighter_1_r = [fighter_r1,fighter_r2,fighter_r1,fighter_r2]
fighter_1_l = [fighter_l1,fighter_l2,fighter_l1,fighter_l2]

fighter_pch_r1 = pygame.image.load("Gus/fighter_1/fighter_1_punch1.png")
fighter_pch_r2 = pygame.image.load("Gus/fighter_1/fighter_1_punch2.png")
fighter_pch_l1 = pygame.transform.flip(fighter_pch_r1, True, False)
fighter_pch_l2 = pygame.transform.flip(fighter_pch_r2, True, False)

fighter_pch_r = [fighter_pch_r2,fighter_pch_r2,fighter_pch_r1,fighter_pch_r1]
fighter_pch_l = [fighter_pch_l2,fighter_pch_l2,fighter_pch_l1,fighter_pch_l1]

fighter_sp_r1 = pygame.image.load("Gus/fighter_1/fighter_1_sp1.png")
fighter_sp_r2 = pygame.image.load("Gus/fighter_1/fighter_1_sp2.png")
fighter_sp_l1 = pygame.transform.flip(fighter_sp_r1, True, False)
fighter_sp_l2 = pygame.transform.flip(fighter_sp_r2, True, False)

fighter_sp_r = [fighter_sp_r1,fighter_sp_r1,fighter_sp_r2,fighter_sp_r2]
fighter_sp_l = [fighter_sp_l1,fighter_sp_l1,fighter_sp_l2,fighter_sp_l2]

fighter_ouille_r1 = pygame.image.load("Gus/fighter_1/fighter_1_ouille1.png")
fighter_ouille_r2 = pygame.image.load("Gus/fighter_1/fighter_1_ouille2.png")
fighter_ouille_l1 = pygame.transform.flip(fighter_ouille_r1, True, False)
fighter_ouille_l2 = pygame.transform.flip(fighter_ouille_r2, True, False)

fighter_ouille_r = [fighter_ouille_r1,fighter_ouille_r1,fighter_ouille_r2,fighter_ouille_r2]
fighter_ouille_l = [fighter_ouille_l1,fighter_ouille_l1,fighter_ouille_l2,fighter_ouille_l2]

lvl_fight1=pygame.image.load('Level/fight_lvl1.jpg')
lvl_fight2=pygame.image.load('Level/fight_lvl2.jpg')
lvl_fight3=pygame.image.load('Level/fight_lvl3.jpg')
lvl_fight4=pygame.image.load('Level/fight_lvl4.jpg')

lvl_fight = [lvl_fight1,lvl_fight2,lvl_fight3,lvl_fight4]

power_bar0 = pygame.image.load("bank/image/super_power0.png")
power_bar1 = pygame.image.load("bank/image/super_power1.png")
power_bar2 = pygame.image.load("bank/image/super_power2.png")
power_bar3 = pygame.image.load("bank/image/super_power3.png")
power_bar4 = pygame.image.load("bank/image/super_power4.png")
power_bar5 = pygame.image.load("bank/image/super_power5.png")
power_bar = [power_bar0,power_bar1,power_bar2,power_bar3,power_bar4,power_bar5]

plan = pygame.image.load("bank/image/plan_metro.png")

