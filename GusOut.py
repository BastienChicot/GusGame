# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 16:02:54 2021

@author: basti
"""
import pygame
from Story.Fonctions import collisions, sac_a_dos, action_key, zone_interaction, zone_dialogue
from Level.Levels import *
from settings import *

pygame.init()
pygame.font.init()
 
myfont = pygame.font.SysFont('arial', 20)

screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Gus veut boire un coup')

clock = pygame.time.Clock()

sac = sac_a_dos()
action=action_key()


def game_loop(sac,action):
    x =  575
    y = 73
    x_change = 0
    y_change = 0
    
    phrases_papa_avant_soupe = ["Laisse moi tranquille", "Va voir ta mère, elle est dans la chambre"]
    phrases_papa_entre_soupe = ["Tu as apporté à manger à ta mère ?","Tu as apporté à manger à ta mère ?"]
    phrases_papa_post_soupe = ["J'ai soif !!",
                "Apportes moi une bière et tais-toi par pitié!"]
    sleep = ["ZZZzzzZZZzzz","ZZZzzzZZZzzz"]
    phrases_maman = ["Kof kof ! Apporte moi un truc chaud à manger s'il te plait", "Merci beaucoup Gus","ZZZzzzZZZzzz",
                     ""]    
    
    #INTERACTIONS
    pressed_salon = -1
    pressed_mom = -1
    pressed_dad = -1
    pressed_cuisine1 = -1
    pressed_cuisine2 = -1
    pressed_four = -1
    pressed_sdb1 = -1
    pressed_frigo = -1 
    fouille = -1
    pressed_ch = -1
    pressed_couloir = -1
    pressed_arm_mom = -1
    pressed_entre = -1
    
    open_buro = False
    service=False
    mom_sleep = False
    dad_sleep = False
    papa_fouillab = False
    porte_entre = False
    
    #OBJETS NIVEAU
    torchon_salon = 0
    torchonsdb1 = 0
    torchoncoul = 0
    torchonch = 0
    torchon_entre = 0
    torchon_mom = 0
    
    cles_buro=0
    biere=0
    
    gugus = gugus_face
        
    gameExit = False
    run = False
    
    while not gameExit:
            
        sac.torchon = torchon_salon+torchonsdb1+torchoncoul+torchonch+torchon_entre+torchon_mom
        
        if open_buro == False and porte_entre == False :
            liste_mur = level_1(screen,display_width,display_height)
        if open_buro == True and porte_entre == False :
            liste_mur = level_1_2(screen,display_width,display_height)
        if open_buro == True and porte_entre == True :
            liste_mur = level_1_3(screen,display_width,display_height)
        if open_buro == False and porte_entre == True :
            liste_mur = level_1_4(screen,display_width,display_height)

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
                    #PERSONNES
                    if 0 < x < 75 and 0 < y < 100 and sac.soupe_chaude == 0 and service == False:
                        pressed_mom = 0
                        pressed_dad = -1
                    if 0 < x < 75 and 0 < y < 100 and sac.soupe_chaude == 1 and service == False:
                        pressed_mom = 1
                        pressed_dad = -1
                    if 0 < x < 75 and 0 < y < 100 and sac.soupe_chaude == 1 and service == True:
                        pressed_mom = 2
                        pressed_dad = -1
                        mom_sleep = True
                    if 170 < x < 210 and 378 < y < 440 and biere == 0:
                        pressed_dad += 1
                        service = False
                    if 170 < x < 210 and 378 < y < 440 and biere == 1 and pressed_mom>=1 and dad_sleep == False:
                        pressed_dad += 1
                        service = True
                    if 170 < x < 210 and 378 < y < 440 and papa_fouillab == True :
                        fouille += 1
                        
                    #OBJETS
                    if 235 < x < 295 and 480 < y < 530 :
                        pressed_salon += 1
                    if 610 < x < 660 and 155 < y < 230 :
                        pressed_ch += 1
                    if 440 < x < 488 and 65 < y < 140 :
                        pressed_couloir += 1
                    if 550 < x < 590 and 370 < y < 550 :
                        pressed_sdb1 += 1
                    if 530 < x < 615 and 610 < y < 700 :
                        pressed_entre += 1
                    if 300 < x < 400 and 20 < y < 110 and mom_sleep == True :
                        pressed_arm_mom += 1
                    if 270 < x < 340 and 510 < y < 560 :
                        pressed_cuisine1 += 1  
                    if 240 < x < 300 and 580 < y < 680 :
                        pressed_cuisine2 += 1
                    if 341 < x < 410 and 510 < y < 560 and sac.soupe_froide == 0 and sac.soupe_chaude == 0:
                        pressed_four = -1
                    if 341 < x < 410 and 510 < y < 560 and sac.soupe_froide == 1 and sac.soupe_chaude == 0:
                        pressed_four = 0
                    if 270 < x < 335 and 600 < y < 680 and sac.soupe_froide == 1 and sac.soupe_chaude == 1:
                        pressed_four = 1
                    if 230 < x < 270 and 560 < y < 630 :
                        pressed_frigo +=1                        

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
        
        if pressed_salon >= 0:
            torchon_salon = 1
        if pressed_ch >= 0:
            torchonch = 1
        if pressed_couloir >= 0:
            torchoncoul = 1
        if pressed_sdb1 >= 0:
            torchonsdb1 = 1
        if pressed_entre >= 0:
            torchon_entre = 1
        if pressed_arm_mom >= 0:
            torchon_mom = 1
            
        ##DIALOGUES
        if 0 < x < 75 and 0 < y < 100 :
    
            zone_dialogue(screen,"Parler à maman (A)",action,phrases_maman,pressed_mom,3)
            
        elif 170 < x < 210 and 378 < y < 440 and sac.soupe_froide == 0 and sac.soupe_chaude == 0 and service == False and pressed_mom == -1 and papa_fouillab == False:
            
            zone_dialogue(screen,"Parler à papa (A)",action,phrases_papa_avant_soupe,pressed_dad,2)
        
        elif 170 < x < 210 and 378 < y < 440 and sac.soupe_froide == 1 and sac.soupe_chaude == 0 and service == False and pressed_mom == 0 and papa_fouillab == False:
            
            zone_dialogue(screen,"Parler à papa (A)",action,phrases_papa_entre_soupe,pressed_dad,2)

        elif 170 < x < 210 and 378 < y < 440 and sac.soupe_froide == 1 and sac.soupe_chaude == 1 and service == False and pressed_mom >= 1 and papa_fouillab == False:
            
            zone_dialogue(screen,"Parler à papa (A)",action,phrases_papa_post_soupe,pressed_dad,2)

        elif 170 < x < 210 and 378 < y < 440 and sac.soupe_froide == 1 and sac.soupe_chaude == 1 and service == True and papa_fouillab == False:
            
            zone_dialogue(screen,"Parler à papa (A)",action,sleep,pressed_dad,2)
            dad_sleep = True
        
        elif 170 < x < 210 and 378 < y < 440 and papa_fouillab == True:

            fouille = zone_interaction(screen,"Fouiller papa (A)",action,fouille,"la clé de la maison!")
            sac.cle_maison = True                                                                                         
            
        ##OBJETS
        elif 235 < x < 295 and 480 < y < 530 :

            pressed_salon = zone_interaction(screen,"Fouiller l'armoire (A)",action,pressed_salon,"un torchon")

        elif 610 < x < 660 and 155 < y < 230 :

            pressed_ch = zone_interaction(screen,"Fouiller l'armoire (A)",action,pressed_ch,"un t-shirt sale")

        elif 440 < x < 488 and 65 < y < 140 :

            pressed_couloir = zone_interaction(screen,"Fouiller l'armoire (A)",action,pressed_couloir,"une couverture")

        elif 530 < x < 615 and 610 < y < 700 :

            pressed_entre = zone_interaction(screen,"Fouiller l'armoire (A)",action,pressed_entre,"une vieille couverture du chien")

        elif 300 < x < 400 and 20 < y < 110 and mom_sleep == True :

            pressed_arm_mom = zone_interaction(screen,"Fouiller l'armoire (A)",action,pressed_arm_mom,"une serviette")

        elif 290 < x < 340 and 510 < y < 560 :
            
            pressed_cuisine1 = zone_interaction(screen,"Fouiller les tirroirs (A)",action,pressed_cuisine1,"un tire-bouchon")

        elif 341 < x < 410 and 510 < y < 560 and sac.soupe_froide == 1:
            
            if pressed_four <= 0 and pressed_mom <= 0: 
                pressed_four = zone_interaction(screen,"Fouiller le four (A)",action,pressed_four,"une soupe chaude")
                sac.soupe_chaude=1 
                pressed_four = 0
            if pressed_four == 0 and pressed_mom >= 1: 
                pressed_four = zone_interaction(screen,"Fouiller le four (A)",action,pressed_four,"... un four vide")
                sac.soupe_chaude=1
                pressed_dad = -1
                
        elif 341 < x < 410 and 510 < y < 560 and sac.soupe_froide == 0:
          
            if pressed_mom < 0:
                pressed_four = zone_interaction(screen,"Fouiller le four (A)",action,pressed_four,"... un four vide")
                sac.soupe_chaude = 0
                pressed_four = 0

            if pressed_mom == 0:
                pressed_four = zone_interaction(screen,"Fouiller le four (A)",action,pressed_four," ... rien ... Trouve d'abord quelque chose à chauffer!")
                sac.soupe_chaude = 0
                pressed_four = 0
    
        elif 270 < x < 335 and 600 < y < 680 :
            
            if pressed_cuisine2 == -1:
                pressed_cuisine2 = zone_interaction(screen,"Fouiller le placard (A)",action,pressed_cuisine2,"une soupe froide")            

            if pressed_cuisine2 >= 0:
                pressed_cuisine2 = zone_interaction(screen,"Fouiller le placard (A)",action,pressed_cuisine2,"une soupe froide")            
                sac.soupe_froide=1
                pressed_dad = -1
                
        elif 560 < x < 650 and 0 < y < 30 :
            
            if sac.torchon <  5:
                textsurface = myfont.render("Ca fait un peu haut pour sauter!", False, (255, 255, 255))
                screen.blit(textsurface,(290,440))
                
        elif 550 < x < 590 and 370 < y < 550 :
            
            if pressed_sdb1 <= 0 and open_buro == False:                
                pressed_sdb1 = zone_interaction(screen,"Fouiller le linge (A)",action,pressed_sdb1,"une clé")
                cles_buro = 1
            if pressed_sdb1 <= 0 and open_buro == True:
                pressed_sdb1 = zone_interaction(screen,"Fouiller le linge (A)",action,pressed_sdb1,"une serviette")
                torchonsdb1 = 1    
                
        elif 185 < x < 225 and 200 < y < 300 :
            
            if cles_buro == 0 and service == False and mom_sleep == False:
                textsurface = myfont.render("La porte est fermée", False, (255, 255, 255))
                screen.blit(textsurface,(290,440))                
            if cles_buro == 1 and service == False and mom_sleep == False:
                textsurface = myfont.render("Papa va m'entendre, c'est chaud !", False, (255, 255, 255))
                screen.blit(textsurface,(290,440))
            if cles_buro == 1 and service == True and mom_sleep == False:
                textsurface = myfont.render("Est-ce que maman dort ? Il ne faudrait pas qu'elle me grille.", False, (255, 255, 255))
                screen.blit(textsurface,(290,440))                                     
            if cles_buro == 1 and service == True and mom_sleep == True:                
                textsurface = myfont.render("Tu as ouvert la porte du bureau", False, (255, 255, 255))
                screen.blit(textsurface,(290,440))
                pressed_sdb1 = -1
                open_buro = True
                
        elif 230 < x < 270 and 560 < y < 630 :

            pressed_frigo = zone_interaction(screen,"Ouvrir le frigo (A)",action,pressed_frigo,"une bière")
            biere = 1
            
        elif 670 < x < 725 and 560 < y < 670 :
            
            if sac.cle_maison == False and dad_sleep == False and mom_sleep == False:
                textsurface = myfont.render("La porte est fermée, les clés ne sont pas là.", False, (255, 255, 255))
                screen.blit(textsurface,(290,440))                
            if sac.cle_maison == False and dad_sleep == True and mom_sleep == True:
                textsurface = myfont.render("Les clés ne sont pas sur la porte. Papa a dû les garder sur lui!", False, (255, 255, 255))
                screen.blit(textsurface,(290,440))
                papa_fouillab = True
            if sac.cle_maison == False and dad_sleep == True and mom_sleep == False:
                textsurface = myfont.render("Est-ce que maman dort ? \n Papa a dû garder les clés sur lui", False, (255, 255, 255))
                screen.blit(textsurface,(290,440))
                papa_fouillab = True                                     
            if sac.cle_maison == False and dad_sleep == False and mom_sleep == True:               
                textsurface = myfont.render("Papa ne dort pas, c'est tendu!! Et j'ai pas les clés!", False, (255, 255, 255))
                screen.blit(textsurface,(290,440))
            if sac.cle_maison == True and dad_sleep == True and mom_sleep == False:               
                textsurface = myfont.render("Maman ne dort pas, c'est tendu!!", False, (255, 255, 255))
                screen.blit(textsurface,(290,440))
            if sac.cle_maison == True and dad_sleep == True and mom_sleep == True:               
                textsurface = myfont.render("Tu as ouvert la porte d'entrée Batard!", False, (255, 255, 255))
                screen.blit(textsurface,(290,440))
                porte_entre = True

        else:
            action.click = False
        
        screen.blit(gugus, rect_gugus)
        print(sac.torchon)
        pygame.display.update()
        clock.tick(60)

game_loop(sac,action)
pygame.quit()
quit()