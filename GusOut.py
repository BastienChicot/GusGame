# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 16:02:54 2021

@author: basti
"""
import pygame
from Story.Fonctions import collisions, sac_a_dos, action_key, zone_interaction, zone_dialogue
from Level.Levels import level_1, zone_level_1
from settings import *

pygame.init()
pygame.font.init()
 
myfont = pygame.font.SysFont('arial', 20)

screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Gus veut boire un coup')

clock = pygame.time.Clock()

sac = sac_a_dos()
action=action_key()

liste_zone = zone_level_1()

def game_loop(sac,action):
    x =  575
    y = 73
    x_change = 0
    y_change = 0
    
    phrases_papa = ["Laisse moi tranquille", "Va voir ta mère, elle est dans la chambre",
                "Tu as apporté à manger à ta mère ?","Bon laisse moi tranquille maintenant",
                "Tu me fatigues! Va-t-en!","ZZZzzzZZZzzz",""]
    phrases_maman = ["Kof kof ! Apporte moi un truc chaud à manger s'il te plait", "Merci beaucoup Gus","ZZZzzzZZZzzz",
                     ""]    

    pressed_salon = -1
    pressed_mom = -1
    pressed_dad = -1
    pressed_cuisine1 = -1
    pressed_cuisine2 = -1
    pressed_four = -1
    
    gugus = gugus_face
        
    gameExit = False
    run = False

    liste_mur = level_1(screen,display_width,display_height)
    
    while not gameExit:
            
        liste_mur = level_1(screen,display_width,display_height)
        rect_gugus = gugus.get_rect() 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
    
            ############################
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    gugus = gugus_gauche
                    x_change = -2.5
                elif event.key == pygame.K_RIGHT:
                    gugus = gugus_droite
                    x_change = 2.5
                elif event.key == pygame.K_UP:
                    gugus = gugus_dos
                    y_change = -2.5
                elif event.key == pygame.K_DOWN:
                    gugus = gugus_face
                    y_change = 2.5

                if event.key == pygame.K_a and not action.click:
                    action.click = True
                    if 0 < x < 75 and 0 < y < 100 and sac.soupe_chaude == 0:
                        pressed_mom = 0
                    if 0 < x < 75 and 0 < y < 100 and sac.soupe_chaude == 1:
                        pressed_mom = 1
                    if 170 < x < 210 and 378 < y < 440 :
                        pressed_dad += 1
                    if 235 < x < 295 and 480 < y < 530 :
                        pressed_salon += 1
                    if 270 < x < 340 and 510 < y < 560 :
                        pressed_cuisine1 += 1  
                    if 240 < x < 300 and 580 < y < 680 :
                        pressed_cuisine2 += 1
                    if 341 < x < 410 and 510 < y < 560 and sac.soupe_froide == 0 and sac.soupe_chaude == 0:
                        pressed_four = 1
                    if 341 < x < 410 and 510 < y < 560 and sac.soupe_froide == 1 and sac.soupe_chaude == 0:
                        pressed_four = 0
                    if 270 < x < 335 and 600 < y < 680 and sac.soupe_froide == 1 and sac.soupe_chaude == 1:
                        pressed_four = 0
                        
                elif event.key != pygame.K_a:
                
                    action.click = False
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = True
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                if event.key == pygame.K_SPACE:
                    run = False
            ######################

        
        if run == True:
            if x_change != 0:
                x_change = x_change * running
            elif y_change !=0:
                y_change = y_change * running
            else:
                x_change = x_change
                y_change = y_change
            
        
        if x <= 0 :
            x=0
        elif x >= display_width - gugus_width:
            x = display_width - gugus_width
            
        if y <= 0 :
            y=0
        elif y >= display_height - gugus_height:
            y = display_height - gugus_height 
        
        rect_gugus.topleft = (x,y)
        
        x,y = collisions(liste_mur,x,y,rect_gugus,x_change,y_change)

#        rect_gugus.topleft = (x,y)
        
        if 0 < x < 75 and 0 < y < 100 :
    
            zone_dialogue(screen,"Parler à maman (A)",action,phrases_maman,pressed_mom,3)
            
        elif 170 < x < 210 and 378 < y < 440 :
            
            zone_dialogue(screen,"Parler à papa (A)",action,phrases_papa,pressed_dad,2)

        elif 170 < x < 210 and 378 < y < 440 and pressed_mom >= 1:
            
            zone_dialogue(screen,"Parler à papa (A)",action,phrases_papa,pressed_dad,3)
               
        elif 235 < x < 295 and 480 < y < 530 :
            
            sac.torchon_salon, pressed_salon = zone_interaction(screen,"Fouiller l'armoire (A)",action,sac.torchon_salon,pressed_salon,"un torchon")
       
        elif 290 < x < 340 and 510 < y < 560 :
            
            sac.tire_bouchon,pressed_cuisine1 = zone_interaction(screen,"Fouiller les tirroirs (A)",action,sac.tire_bouchon,pressed_cuisine1,"un tire-bouchon")

        elif 341 < x < 410 and 510 < y < 560 and sac.soupe_froide == 1:
            
            if pressed_four == -1: 
                sac.soupe_chaude,pressed_four = zone_interaction(screen,"Fouiller le four (A)",action,sac.soupe_chaude,pressed_four,"une soupe chaude")
            if pressed_four >= 0: 
                sac.soupe_chaude,pressed_four = zone_interaction(screen,"Fouiller le four (A)",action,sac.soupe_chaude,pressed_four,"une soupe chaude")
            
        elif 341 < x < 410 and 510 < y < 560 and sac.soupe_froide == 0:
            
            sac.soupe_chaude,pressed_four = zone_interaction(screen,"Fouiller le four (A)",action,sac.soupe_chaude,pressed_four,"... un four vide")
            sac.soupe_chaude = 0
        
        elif 270 < x < 335 and 600 < y < 680 :
            
            if pressed_cuisine2 == -1:
                sac.soupe_froide,pressed_cuisine2 = zone_interaction(screen,"Fouiller le placard (A)",action,sac.soupe_froide,pressed_cuisine2,"une soupe froide")            
            if pressed_cuisine2 >= 0:
                sac.soupe_froide,pressed_cuisine2 = zone_interaction(screen,"Fouiller le placard (A)",action,sac.soupe_froide,pressed_cuisine2,"une soupe froide")            
                sac.soupe_froide=1
        else:
            action.click = False
        
        screen.blit(gugus, rect_gugus)
      
        pygame.display.update()
        clock.tick(60)

game_loop(sac,action)
pygame.quit()
quit()