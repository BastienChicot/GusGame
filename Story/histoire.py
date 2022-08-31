# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 13:28:37 2021

@author: basti
"""
import pygame
import random

from Story.Fonctions import *
from Level.Levels import *
from settings import *
import numpy as np

pygame.init()
pygame.font.init()
pygame.mixer.init()

myfont = pygame.font.SysFont('corbel', 20, bold=True)
Gus_font = pygame.font.SysFont('corbel', 16, bold=True)
big_font = pygame.font.SysFont('corbel', 40, bold=True)

screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Gus veut boire un coup')

clock = pygame.time.Clock()


def nivo1(sac,action,Gus,tr):
    pygame.init()
    speed_move = Gus.speed
    frame_count = Gus.frame
    a=0
    time = 0
    x =  (display_width-gugus_width)/2
    y = (display_height-gugus_height)/2    
    screen_x = -475 + x
    screen_y = -224 + y    
    rel_x = 0 
    rel_y = 0
    x_change = 0
    y_change = 0
    gugus = gugus_face
    
    phrases_papa_avant_soupe = [["Laisse moi tranquille"], ["Va voir ta mère","dans sa chambre"]]
    phrases_papa_entre_soupe = [["Tu as apporté à","manger à ta mère ?"]]
    phrases_papa_post_soupe = [["J'ai soif !!"],
                ["Trouves-moi une bière","et tais-toi!"]]
    sleep = [["ZZZzzzZZZzzz"]]
    phrases_maman = [["Apporte moi un truc","à manger s'il te plait"], ["Merci beaucoup Gus"],["ZZZzzzZZZzzz",
                     ""]]    
    phrases_cleb=[["Aîe !","Ca fait mal!"]]
    phrases_papier=[["Ah! Juste quelques", "feuilles de papiers et","des stylos.","Rien d'utile!"]]
    phrases_cuisine=[["Juste des assiettes","et des couverts..."]]
    
    #INTERACTIONS
    
    #OBJETS NIVEAU
        
    gameExit = False
    
    while not gameExit and Gus.level == 1:
        
        if not pygame.mixer.music.get_busy() and Gus.current <= len(playlist):
            Gus.current+=1
            pygame.mixer.music.load ( playlist[Gus.current])
            pygame.mixer.music.play()
        elif not pygame.mixer.music.get_busy() and Gus.current > len(playlist):
            Gus.current=0
            pygame.mixer.music.load ( playlist[Gus.current])
            pygame.mixer.music.play()
            
        if frame_count <= 30:
            frame_count += 1
        else:
            frame_count = 0
        
        if frame_count <= 15:
            a=0
        elif frame_count > 15:
            a=1
            
        Gus.update_items(tr)
        sac.update_items(tr)        

        if tr.open_buro == False and tr.porte_entre == False :
            liste_mur = level_1(screen,screen_x,screen_y)
        if tr.open_buro == True and tr.porte_entre == False :
            liste_mur = level_1_2(screen,screen_x,screen_y)
        if tr.open_buro == True and tr.porte_entre == True :
            liste_mur = level_1_3(screen,screen_x,screen_y)
        if tr.open_buro == False and tr.porte_entre == True :
            liste_mur = level_1_4(screen,screen_x,screen_y)

        rect_gugus = gugus.get_rect() 
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    other_s.play()
                    Gus.pause += 1    
                if event.key == pygame.K_TAB:
                    other_s.play() 
            ############################
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  
                    x_change = -speed_move
                    rel_x = speed_move
                    y_change = 0
                    rel_y = 0
                    step_s.play(-1)
                elif event.key == pygame.K_RIGHT:
                    x_change = speed_move
                    rel_x = -speed_move
                    y_change = 0
                    rel_y = 0
                    step_s.play(-1)
                elif event.key == pygame.K_UP:
                    y_change = -speed_move
                    rel_y = speed_move
                    x_change = 0
                    rel_x = 0
                    step_s.play(-1)
                elif event.key == pygame.K_DOWN:
                    y_change = speed_move
                    rel_y = -speed_move
                    x_change = 0
                    rel_x = 0
                    step_s.play(-1)
                if event.key == pygame.K_a and not action.click:
                    action.click = True
                    click_.play()
                    #PERSONNES
                    if 0+screen_x < x < 75+screen_x and 0+screen_y < y < 100+screen_y and sac.soupe_chaude == 0 and tr.service == False and tr.mom_sleep == False:
                        tr.pressed_mom = 0
                        tr.pressed_dad = -1
                    if 0+screen_x < x < 75+screen_x and 0+screen_y < y < 100+screen_y and sac.soupe_chaude == 1 and tr.service == False and tr.mom_sleep == False:
                        tr.pressed_mom = 1
                        tr.pressed_dad = -1
                    if 0+screen_x < x < 75+screen_x and 0+screen_y < y < 100+screen_y and tr.service == True:
                        tr.pressed_mom = 2
                        tr.pressed_dad = -1
                        tr.mom_sleep = True
                    if 170+screen_x < x < 210+screen_x and 378+screen_y < y < 440+screen_y and tr.biere == 0:
                        tr.pressed_dad += 1
                        tr.service = False
                    if 170+screen_x < x < 210+screen_x and 378+screen_y < y < 440+screen_y and tr.biere == 1 and tr.pressed_mom>=1 and tr.dad_sleep == False:
                        tr.pressed_dad += 1
                        tr.service = True
                    if 170+screen_x < x < 210+screen_x and 378+screen_y < y < 440+screen_y and tr.papa_fouillab == True :
                        tr.fouille += 1
                        
                    #OBJETS
                    if 612+screen_x < x < 670+screen_x and 457+screen_y < y < 540+screen_y:
                        tr.pressed_sdb2 += 1
                    if 235+screen_x < x < 295+screen_x and 480+screen_y < y < 530+screen_y :
                        tr.pressed_salon += 1
                    if 610+screen_x < x < 660+screen_x and 155+screen_y < y < 230+screen_y :
                        tr.pressed_ch += 1
                    if 440+screen_x < x < 488+screen_x and 65+screen_y < y < 140+screen_y :
                        tr.pressed_couloir += 1
                    if 550+screen_x < x < 590+screen_x and 370+screen_y < y < 550+screen_y :
                        tr.pressed_sdb1 += 1
                    if 530+screen_x < x < 615+screen_x and 610+screen_y < y < 700+screen_y :
                        tr.pressed_entre += 1
                    if 300+screen_x < x < 400+screen_x and 20+screen_y < y < 110+screen_y and tr.mom_sleep == True :
                        tr.pressed_arm_mom += 1
                    if 270+screen_x < x < 340+screen_x and 510+screen_y < y < 560+screen_y :
                        tr.pressed_cuisine1 += 1  
                    if 240+screen_x < x < 300+screen_x and 580+screen_y < y < 680+screen_y :
                        tr.pressed_cuisine2 += 1
                    if 341+screen_x < x < 410+screen_x and 510+screen_y < y < 560+screen_y and sac.soupe_froide == 0 and sac.soupe_chaude == 0:
                        tr.pressed_four = -1
                    if 341+screen_x < x < 410+screen_x and 510+screen_y < y < 560+screen_y and sac.soupe_froide == 1 and sac.soupe_chaude == 0:
                        tr.pressed_four = 0
                    if 270+screen_x < x < 335+screen_x and 600+screen_y < y < 680+screen_y and sac.soupe_chaude == 1:
                        tr.pressed_four = 1
                    if 230+screen_x < x < 270+screen_x and 560+screen_y < y < 630+screen_y :
                        tr.pressed_frigo +=1     
                    if 416+screen_x < x < 490+screen_x and 610+screen_y < y < 690+screen_y :
                        tr.pressed_cleb = 0
                        Gus.pv -= 1
                    if 84+screen_x < x < 144+screen_x and 516+screen_y < y < 580+screen_y or 626+screen_x < x < 700+screen_x and 269+screen_y < y < 340+screen_y or 260+screen_x < x < 350+screen_x and 230+screen_y < y < 300+screen_y:
                        tr.pressed_papier = 0
                    if 90+screen_x < x < 180+screen_x and 200+screen_y < y < 260+screen_y :   
                        tr.pressed_tune_buro += 1
                    if 595+screen_x < x < 670+screen_x and 570+screen_y < y < 656+screen_y :
                        tr.pressed_tune_entre += 1
                    if 350+screen_x < x < 400+screen_x and 600+screen_y < y < 670+screen_y :
                        tr.pressed_cuisine3 = 0
                    if 430+screen_x < x < 500+screen_x and 330+screen_y < y < 430+screen_y :
                        tr.pressed_couloir2 += 1
                    if 10+screen_x < x < 118+screen_x and 260+screen_y < y < 320+screen_y :
                        tr.pressed_buro += 1
                    if 200+screen_x < x < 234+screen_x and 95+screen_y < y < 170+screen_y :
                        tr.pressed_tune_ch += 1
                    if 920+screen_x < x < 1000+screen_x and 0+screen_y < y < 100+screen_y :
                        tr.pressed_sortie += 1
                        
                elif event.key != pygame.K_a:
                
                    action.click = False

                if event.key == pygame.K_RETURN and not action.change_level:
                    action.change_level = True
                    enter_s.play()
                    if 560+screen_x < x < 650+screen_x and 0+screen_y < y < 30+screen_y and sac.Torchon >= 5:
                        Gus.level = 2  
                        Gus.spawn = 1
                        sac.Torchon = 0
                        time = 0
                        sac.soupe_froide = 0
                    elif 560+screen_x < x < 650+screen_x and 0+screen_y < y < 30+screen_y and sac.Torchon == 4:
                        Gus.level = 2.2
                        Gus.spawn = 4
                        Gus.pv -= 20
                        sac.Torchon -= 4
                        time = 0
                        sac.soupe_froide = 0
                elif event.key != pygame.K_RETURN:
                
                    action.change_level = False
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_change = 0
                    rel_x = 0
                    gugus = gugus_gauche 
                    step_s.stop()
                if event.key == pygame.K_RIGHT:
                    x_change = 0
                    rel_x = 0
                    gugus = gugus_droite 
                    step_s.stop()

                if event.key == pygame.K_UP:
                    y_change = 0
                    rel_y = 0
                    gugus = gugus_dos 
                    step_s.stop()
                    
                if event.key == pygame.K_DOWN:
                    y_change = 0
                    rel_y = 0
                    gugus = gugus_face 
                    step_s.stop()
                    
            ######################            
        keys=pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            gugus=gugus_walkdown[a]
        if keys[pygame.K_UP]:
            gugus=gugus_walkup[a]
        if keys[pygame.K_RIGHT]:
            gugus=gugus_walkright[a]
        if keys[pygame.K_LEFT]:
            gugus=gugus_walkleft[a]
            
        rect_gugus.topleft = (x,y)
        
        x_change,y_change,rel_x,rel_y = collisions(liste_mur,rect_gugus,x_change,y_change,speed_move,rel_x,rel_y)
        
        screen_x += rel_x
        screen_y += rel_y
        
        if screen_x >= 0 and rel_x > 0:
            screen_x = 0
            x -= rel_x
        elif screen_x <= display_width - 1000 and rel_x < 0 :
            screen_x = display_width - 1000
            x -= rel_x
        if screen_y >= 0 and rel_y > 0 :
            screen_y = 0
            y  -= rel_y
        elif screen_y <= display_height - 707 and rel_y < 0:
            screen_y = display_height - 707 
            y -= rel_y
            
        if x < (display_width-gugus_width)/2 and rel_x < 0:
            screen_x = 0
            x -= rel_x
        elif x > (display_width-gugus_width)/2 and rel_x > 0:
            screen_x = display_width - 1000
            x -= rel_x
            
        if y < (display_height-gugus_height)/2 and rel_y < 0:
            screen_y = 0
            y -= rel_y
        elif y > (display_height-gugus_height)/2 and rel_y > 0:
            screen_y = display_height - 707 
            y -= rel_y
             
        if tr.pressed_salon >= 0:
            tr.torchon_salon = 1
        if tr.pressed_ch >= 0:
            tr.torchonch = 1
        if tr.pressed_couloir >= 0:
            tr.torchoncoul = 1
        if tr.pressed_sdb1 >= 0:
            tr.torchonsdb1 = 1
        if tr.pressed_entre >= 0:
            tr.torchon_entre = 1
        if tr.pressed_arm_mom >= 0:
            tr.torchon_mom = 1
        if tr.pressed_tune_buro >= 0:
            tr.tune_buro = 0.1  
        if tr.pressed_tune_entre >= 0:
            tr.tune_entre = 0.05
        if tr.pressed_tune_ch >= 0:
            tr.tune_ch = 0.2
        if tr.pressed_buro >= 0:
            tr.capote_buro = 1        
        if tr.pressed_sortie >= 0:
            tr.capote_entree = 1
            
        if tr.pressed_frigo == 0 :
            tr.biere = 1
        
        if tr.pressed_sdb2 == 0:
            tr.bouteille_alc = 1
            
        ##DIALOGUESs
        if 0+screen_x < x < 75+screen_x and 0+screen_y < y < 100+screen_y :
    
            zone_dialogue(screen,"Parler à maman (A)",action,phrases_maman[tr.pressed_mom],tr.pressed_mom,3)
            
        elif 170+screen_x < x < 210+screen_x and 378+screen_y < y < 440+screen_y and sac.soupe_froide == 0 and sac.soupe_chaude == 0 and tr.service == False and tr.pressed_mom == -1 and tr.papa_fouillab == False:
            
            zone_dialogue(screen,"Parler à papa (A)",action,phrases_papa_avant_soupe[tr.pressed_dad],tr.pressed_dad,2)
        
        elif 170+screen_x < x < 210+screen_x and 378+screen_y < y < 440+screen_y and sac.soupe_froide == 1 and sac.soupe_chaude == 0 and tr.service == False and tr.pressed_mom == 0 and tr.papa_fouillab == False:
            
            zone_dialogue(screen,"Parler à papa (A)",action,phrases_papa_entre_soupe[tr.pressed_dad],tr.pressed_dad,2)

        elif 170+screen_x < x < 210+screen_x and 378+screen_y < y < 440+screen_y and  sac.soupe_chaude == 1 and tr.service == False and tr.pressed_mom >= 1 and tr.papa_fouillab == False:
            
            zone_dialogue(screen,"Parler à papa (A)",action,phrases_papa_post_soupe[tr.pressed_dad],tr.pressed_dad,2)

        elif 170+screen_x < x < 210+screen_x and 378+screen_y < y < 440+screen_y and tr.service == True and tr.papa_fouillab == False:
            
            zone_dialogue(screen,"Parler à papa (A)",action,sleep[0],tr.pressed_dad,2)
            tr.dad_sleep = True
            sac.soupe_froide = 0 
            sac.soupe_chaude = 0
        
        elif 170+screen_x < x < 210+screen_x and 378+screen_y < y < 440+screen_y and tr.papa_fouillab == True:

            tr.fouille = zone_interaction(screen,"Fouiller papa (A)",action,tr.fouille,"la clé de la maison!")
            sac.Cle_maison = 1  
            tr.mom_sleep == True  
            tr.biere = 0                                                                                     
            
        ##OBJETS
        elif 0+screen_x < x < 50+screen_x and 460+screen_y < y < 586+screen_y :

                textsurface = myfont.render("Ca fait un peu haut", False, (110, 110, 110))
                textsurface2 = myfont.render("pour sauter!", False, (110, 110, 110))
                textsurface3 = myfont.render("Je suis pas fou!", False, (110, 110, 110))
                screen.blit(fond_text,(260,380))
                screen.blit(textsurface,(280,400))
                screen.blit(textsurface2,(280,420)) 
                screen.blit(textsurface3,(280,440)) 

        elif 10+screen_x < x < 93+screen_x and 195+screen_y < y < 258+screen_y :

                textsurface = myfont.render("Pourquoi elle est", False, (110, 110, 110))
                textsurface2 = myfont.render("toute nue la dame ?", False, (110, 110, 110))
                screen.blit(fond_text,(260,380))
                screen.blit(textsurface,(280,400))
                screen.blit(textsurface2,(280,420)) 
                
        elif 430+screen_x < x < 500+screen_x and 330+screen_y < y < 430+screen_y :
            
            tr.pressed_couloir2 = zone_interaction(screen,"Fouiller le placard (A)",action,tr.pressed_couloir2,"un briquet!")
            sac.Briquet = 1

        elif 10+screen_x < x < 118+screen_x and 260+screen_y < y < 320+screen_y :

            tr.pressed_buro = zone_interaction(screen,"Fouiller le placard (A)",action,tr.pressed_buro,"un drôle de truc.")

        elif 920+screen_x < x < 1000+screen_x and 0+screen_y < y < 100+screen_y :
            
            tr.pressed_sortie = zone_interaction(screen,"Regarder par terre (A)",action,tr.pressed_sortie,"un drôle de truc.")

        elif 200+screen_x < x < 234+screen_x and 95+screen_y < y < 170+screen_y :
            
            tr.pressed_tune_ch = zone_interaction(screen,"Fouiller le meuble (A)",action,tr.pressed_tune_ch,"20 centimes")
            
        elif 350+screen_x < x < 400+screen_x and 600+screen_y < y < 670+screen_y :

            zone_dialogue(screen,"Fouiller le meuble (A)",action,phrases_cuisine[tr.pressed_cuisine3],tr.pressed_cuisine3,1)

        elif 612+screen_x < x < 670+screen_x and 457+screen_y < y < 540+screen_y :

            tr.pressed_sdb2 = zone_interaction(screen,"Fouiller le placard (A)",action,tr.pressed_sdb2,"une bouteille d'alcool")
        
        elif 90+screen_x < x < 180+screen_x and 200+screen_y < y < 260+screen_y :

            tr.pressed_tune_buro = zone_interaction(screen,"Fouiller le bureau (A)",action,tr.pressed_tune_buro,"10 centimes.")

        elif 595+screen_x < x < 670+screen_x and 570+screen_y < y < 656+screen_y :

            tr.pressed_tune_entre = zone_interaction(screen,"Fouiller le meuble (A)",action,tr.pressed_tune_entre,"5 centimes.")

        elif 416+screen_x < x < 490+screen_x and 610+screen_y < y < 690+screen_y :

            zone_dialogue(screen,"Caresser le chien (A)",action,phrases_cleb[tr.pressed_cleb],tr.pressed_cleb,1)

        elif 84+screen_x < x < 144+screen_x and 516+screen_y < y < 580+screen_y or 626+screen_x < x < 700+screen_x and 269+screen_y < y < 340+screen_y or 260+screen_x < x < 350+screen_x and 230+screen_y < y < 300+screen_y:

            zone_dialogue(screen,"Fouiller ici (A)",action,phrases_papier[tr.pressed_papier],tr.pressed_papier,1)

        elif 235+screen_x < x < 295+screen_x and 480+screen_y < y < 530+screen_y :

            tr.pressed_salon = zone_interaction(screen,"Fouiller l'armoire (A)",action,tr.pressed_salon,"un torchon")

        elif 610+screen_x < x < 660+screen_x and 155+screen_y < y < 230+screen_y :

            tr.pressed_ch = zone_interaction(screen,"Fouiller l'armoire (A)",action,tr.pressed_ch,"un t-shirt sale")

        elif 440+screen_x < x < 488+screen_x and 65+screen_y < y < 140+screen_y :

            tr.pressed_couloir = zone_interaction(screen,"Fouiller l'armoire (A)",action,tr.pressed_couloir,"une couverture")

        elif 530+screen_x < x < 615+screen_x and 610+screen_y < y < 700+screen_y :

            tr.pressed_entre = zone_interaction(screen,"Fouiller l'armoire (A)",action,tr.pressed_entre,"un vieux plaid")

        elif 300+screen_x < x < 400+screen_x and 20+screen_y < y < 110+screen_y and tr.mom_sleep == True :

            tr.pressed_arm_mom = zone_interaction(screen,"Fouiller l'armoire (A)",action,tr.pressed_arm_mom,"une serviette")

        elif 290+screen_x < x < 340+screen_x and 510+screen_y < y < 560+screen_y :
            
            tr.pressed_cuisine1 = zone_interaction(screen,"Fouiller les tiroirs (A)",action,tr.pressed_cuisine1,"un tire-bouchon")

        elif 341+screen_x < x < 410+screen_x and 510+screen_y < y < 560+screen_y and sac.soupe_froide == 1:
            
            if tr.pressed_four <= 0 and tr.pressed_mom <= 0: 
                tr.pressed_four = zone_interaction(screen,"Fouiller le four (A)",action,tr.pressed_four,"une soupe chaude")
                sac.soupe_chaude=1 
                tr.pressed_four = 0
            if tr.pressed_four == 0 and tr.pressed_mom >= 1: 
                tr.pressed_four = zone_interaction(screen,"Fouiller le four (A)",action,tr.pressed_four,"... un four vide")
                sac.soupe_chaude=1
                tr.pressed_dad = -1
                
        elif 341+screen_x < x < 410+screen_x and 510+screen_y < y < 560+screen_y and sac.soupe_froide == 0:
          
            if tr.pressed_mom < 0:
                tr.pressed_four = zone_interaction(screen,"Fouiller le four (A)",action,tr.pressed_four,"... un four vide")
                sac.soupe_chaude = 0
                tr.pressed_four = 0

            if tr.pressed_mom == 0:
                tr.pressed_four = zone_interaction(screen,"Fouiller le four (A)",action,tr.pressed_four," ... rien ")
                sac.soupe_chaude = 0
                tr.pressed_four = 0
    
        elif 270+screen_x < x < 335+screen_x and 600+screen_y < y < 680+screen_y :
            
            if tr.pressed_cuisine2 == -1:
                tr.pressed_cuisine2 = zone_interaction(screen,"Fouiller le placard (A)",action,tr.pressed_cuisine2,"une soupe froide")            

            if tr.pressed_cuisine2 >= 0:
                tr.pressed_cuisine2 = zone_interaction(screen,"Fouiller le placard (A)",action,tr.pressed_cuisine2,"une soupe froide")            
                sac.soupe_froide=1
                tr.pressed_dad = -1
                
        elif 560+screen_x < x < 650+screen_x and 0+screen_y < y < 30+screen_y :
            
            if sac.Torchon <  4:
                textsurface = myfont.render("Ca fait un peu haut", False, (110, 110, 110))
                textsurface2 = myfont.render("pour sauter!", False, (110, 110, 110))
                screen.blit(fond_text,(260,380))
                screen.blit(textsurface,(280,400))
                screen.blit(textsurface2,(280,420)) 
            if sac.Torchon == 4:
                textsurface = myfont.render("C'est toujours haut ", False, (110, 110, 110))
                textsurface2 = myfont.render("mais avec 4 serviettes", False, (110, 110, 110))
                textsurface3 = myfont.render("ça se tente!", False, (110, 110, 110)) 
                textsurface4 = myfont.render("Descendre : (ENTER)", False, (110, 110, 110)) 
                screen.blit(fond_text,(260,380))
                screen.blit(textsurface,(280,400)) 
                screen.blit(textsurface2,(280,415)) 
                screen.blit(textsurface3,(280,430))
                screen.blit(textsurface4,(280,445))
            if sac.Torchon >= 5:
                textsurface = myfont.render("J'ai assez de linge ", False, (110, 110, 110)) 
                textsurface2 = myfont.render(" pour me faire une", False, (110, 110, 110)) 
                textsurface3 = myfont.render("descente en rappel!", False, (110, 110, 110))              
                screen.blit(fond_text,(260,380))
                screen.blit(textsurface,(280,400)) 
                screen.blit(textsurface2,(280,415))                
                screen.blit(textsurface3,(280,430))
                
        elif 550+screen_x < x < 590+screen_x and 370+screen_y < y < 550+screen_y :
            
            if tr.pressed_sdb1 <= 0 and tr.open_buro == False:                
                tr.pressed_sdb1 = zone_interaction(screen,"Fouiller le linge (A)",action,tr.pressed_sdb1,"une clé")
                tr.cles_buro = 1
            if tr.pressed_sdb1 <= 0 and tr.open_buro == True:
                tr.pressed_sdb1 = zone_interaction(screen,"Fouiller le linge (A)",action,tr.pressed_sdb1,"une serviette")
                tr.torchonsdb1 = 1    
                
        elif 185+screen_x < x < 225+screen_x and 200+screen_y < y < 300+screen_y :
            
            if tr.cles_buro == 0 and tr.service == False and tr.mom_sleep == False:
                textsurface = myfont.render("La porte est fermée", False, (110, 110, 110)) 
                screen.blit(fond_text,(260,380))
                screen.blit(textsurface,(280,400))               
            if tr.cles_buro == 1 and tr.service == False and tr.mom_sleep == False:
                textsurface = myfont.render("Papa va m'entendre,", False, (110, 110, 110)) 
                textsurface2 = myfont.render("c'est chaud !", False, (110, 110, 110)) 
                screen.blit(fond_text,(260,380))
                screen.blit(textsurface,(280,400))               
                screen.blit(textsurface2,(280,420)) 
            if tr.cles_buro == 1 and tr.service == True and tr.mom_sleep == False:
                textsurface = myfont.render("Est-ce que maman dort ? ", False, (110, 110, 110)) 
                screen.blit(fond_text,(260,380))
                screen.blit(textsurface,(270,400))                                    
            if tr.cles_buro == 1 and tr.service == True and tr.mom_sleep == True:                
                textsurface = myfont.render("Tu as ouvert", False, (110, 110, 110)) 
                textsurface2 = myfont.render("la porte du bureau", False, (110, 110, 110)) 
                screen.blit(fond_text,(260,380))
                screen.blit(textsurface,(280,400))               
                screen.blit(textsurface2,(280,420)) 
                tr.pressed_sdb1 = -1
                tr.open_buro = True
                
        elif 230+screen_x < x < 270+screen_x and 560+screen_y < y < 630+screen_y :

            tr.pressed_frigo = zone_interaction(screen,"Ouvrir le frigo (A)",action,tr.pressed_frigo,"une bière")
            
        elif 670+screen_x < x < 725+screen_x and 560+screen_y < y < 670+screen_y :
            
            if sac.Cle_maison == False and tr.dad_sleep == False and tr.mom_sleep == False:
                textsurface = myfont.render("La porte est fermée, ", False, (110, 110, 110)) 
                textsurface2 = myfont.render("les clés ne sont pas là.", False, (110, 110, 110)) 
                screen.blit(fond_text,(260,380))
                screen.blit(textsurface,(280,400))               
                screen.blit(textsurface2,(280,420))  
            if sac.Cle_maison == False and tr.dad_sleep == True and tr.mom_sleep == True:
                textsurface = myfont.render("Les clés ne sont pas " , False, (110, 110, 110)) 
                textsurface1 = myfont.render("sur la porte." , False, (110, 110, 110)) 
                textsurface2 = myfont.render("Où papa les a-t-il posé?" , False, (110, 110, 110)) 
                screen.blit(fond_text,(260,380))
                screen.blit(textsurface,(280,400))
                screen.blit(textsurface1,(280,420))
                screen.blit(textsurface2,(280,440))  
                tr.papa_fouillab = True
            if sac.Cle_maison == False and tr.dad_sleep == True and tr.mom_sleep == False:
                textsurface = myfont.render("Est-ce que maman dort ?", False, (110, 110, 110)) 
                textsurface2 = myfont.render("Où sont les clés de papa?", False, (110, 110, 110)) 
                screen.blit(fond_text,(260,380))
                screen.blit(textsurface,(270,400))
                screen.blit(textsurface2,(270,420)) 
                tr.papa_fouillab = True                                     

            if sac.Cle_maison == True and tr.dad_sleep == True and tr.mom_sleep == False:               
                textsurface = myfont.render("Tu as ouvert ", False, (110, 110, 110)) 
                textsurface2 = myfont.render("la porte d'entrée!", False, (110, 110, 110)) 
                screen.blit(fond_text,(260,380))
                screen.blit(textsurface,(280,400))
                screen.blit(textsurface2,(280,420))
                tr.porte_entre = True
                Gus.porte_entre = True
            if sac.Cle_maison == True and tr.dad_sleep == True and tr.mom_sleep == True:               
                textsurface = myfont.render("Tu as ouvert ", False, (110, 110, 110)) 
                textsurface2 = myfont.render("la porte d'entrée!", False, (110, 110, 110)) 
                screen.blit(fond_text,(260,380))
                screen.blit(textsurface,(280,400))
                screen.blit(textsurface2,(280,420))
                tr.porte_entre = True
                Gus.porte_entre = True
        
        elif 862+screen_x < x < 1000+screen_x and 440+screen_y < y < 480+screen_y :
            Gus.level = 2
            Gus.spawn = 1
            sac.soupe_froide = 0
        else:
            action.click = False
        
        screen.blit(gugus, rect_gugus)
        
        pv = Gus_font.render("Santé : " + str(Gus.pv), False, (78, 22, 9))
        argent = Gus_font.render("Argent : " + str(round(Gus.money,2)), False, (31, 160, 85))
        lvl = Gus_font.render("Niveau : " + str(Gus.level), False, (78, 22, 9))

    
        screen.blit(pv , (10,20))
        screen.blit(lvl , (10,45))
        screen.blit(argent , (10,70))
        screen.blit(sac_tab , (10,450))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_TAB]:
            affich_sac(screen,sac)
        if (Gus.pause%2) == 1:
            pause(screen,gameExit,Gus,sac,tr)
        if Gus.pv == 0:
            game_over(screen)

        pygame.display.update()

        clock.tick(100)
        
def nivo2(sac,action,Gus,tr):
    pygame.init()
    speed_move = Gus.speed
    frame_count = Gus.frame
    a=0
    time = 0
    x =  (display_width-gugus_width)/2
    y = (display_height-gugus_height)/2  
    rel_x = 0 
    rel_y = 0
    x_change = 0
    y_change = 0
    gugus = gugus_face
    
    screen_x = -225 + x
    screen_y = -225 + y 
    
    gus_run = False
    interact = False
    tune = Gus.money
    alcool = sac.Alcool
    preservatif = sac.Capote
    #CREATION ET CARACTERISTIQUES PNJ
    speed_y = 0
    speed_x = -1
    rat_left = pygame.image.load('bank/pnj/rat_g.png')
    
    spawn_x = 820
    spawn_y = 400
    spawnx_nord = 650
    spawny_nord = 580
       
    rat2 = pnj(spawn_x,spawn_y,screen_x,screen_y,rat_left,'left') 
    rat_nord = pnj(spawnx_nord,spawny_nord,screen_x,screen_y,rat_left,'left')
    
    spawn_damex = 120
    spawn_damey = 250
    dame_left = dame_l[0]
    dame = pnj(spawn_damex,spawn_damey,screen_x,screen_y,dame_left,"left")
    
    ####LVL 2 EST

    #INTERACTIONS
    phrases_vieille =[["J'ai perdu mes","clopes gamin!!"],
                      ["Il me faut bien plus de","clopes que ça gamin!"],
                      ["","Est-ce que tu aurais","les horaires du bus?"],
                      ["Merci Gus mais je","ne peux pas te payer.","Mon mari a mon","portefeuille"],
                      ["Nickel Gus ...","eurk! Eurk! EURK","Y a mon fils qui a","besoin d'un coup de","main aussi... Kof"]]
    phrases_interphone =[["SCHkoNNRk schroonnnk"],
                         ["Qui c'est?"],
                         ["Je l'ai pas ton argent!","J'ai passé le portefeuille","au concierge pour qu'il","l'apporte à ma femme."]]
    phrases_papier=[["Ah! Juste quelques", "feuilles de papiers et","des stylos.","Rien d'utile!"]]

    #OBJETS NIVEAU
    
    ##LVL 2 NE
    
    #INTERACTIONS
    phrases_stuff = [["Touches pas à ça !! ","C'est mon sac!"],
                     ["","Jsuii défoncéé Gus","Qu-ess tu fai?","Vas-y sers-toiii!"],
                     ]
    phrases_toxo = [["","Qu'est-ce tu veux toi?","","Dégages de là"],
                    ["","Va voir ma mère","si tu veux le reste","de l'argent."]]
    #ITEMS
    
    ##LVL 2 NORD
    #INTERACTIONS
    phrases_con = [["J'en ai marre de ce","quartier. Entre les ","dealers et les camés...",
                    "J'espère qu'ils finiront","tous au trou!"],
                   ["Qu'est-ce que tu","fais avec ça Gus?"],
                   ["finito"],
                   ["Il me faut un filtre","à postillon pour réparer","l'interphone."],
                   ["Tu as le filtre que","je cherchais.","Vas le changer sur","l'interphone!"],
                   ["Tu veux ton argent?","Va falloir me rendre","quelques services avant.","Va ramasser","les seringues."],
                   ["Bon boulot, merci Gus.","Est-ce que tu peux","me trouver de l'huile","pour mon râteau?"],
                   ["Encore merci Gus.","Il va moins grincer","maintenant. Tiens, tu","as bien mérité ton","argent."],
                   ["Quoi? Il bloque le bus","ce trou du c**!!","Je vais lui coller un","coup de râteau!"]
                                                                 ]
    
    ##LVL 2 NORD OUEST
    phrases_vois=[["J'ai pas le temps","de discuter avec toi","Gus."],
                  ["Oh! Tu as trouvé","le ballon de mon fils.","Merci beaucoup. Viens",
                   "me voir si jamais","tu as besoin d'aide."],
                  ["Tu veux me rendre mon","téléphone?","","          ENTER"]]
    #ITEMS
    
    ##LVL 2 OUEST
    phrases_deal=[["Ah Gus!! Tu diras","à ton père qu'il","me doit encore de","l'argent."],
                  ["J'ai pas besoin de","ça Gus! ","Reviens me voir quand","tu auras tout vendu."],
                  ["Tu as déjà tout vendu?","Est-ce que tu voudrais","me rendre un service?","ENTER"],
                  ["Prends ça et reviens","me voir quand tu auras","mon argent."],
                  ["Il manque 10 balles!!"],
                  ["Le compte est bon Gus."],
                  ["Le compte est bon Gus.","Tu veux aller à la","station de métro ?","    -oui- ENTER"]]
    phrases_pnj_bus=[["Il me manque juste","20 centimes pour","prendre le bus.","",
                      "Donner 20 cts : ENTER"],
                     ["Tiens, j'ai trouvé ces","clés. Je ne sais pas à","qui elles sont."],
                     ["Quand-est-ce qu'il va","partir ce bus?"]]
    phrases_conducteur=[["Est-ce que quelqu'un","peut lui dire de","bouger sa caisse???!!!"],
                        ["C'est 1ç le ticket."]]
    
    gameExit = False
    
    while not gameExit and Gus.level >= 2 and Gus.level < 3:

        if not pygame.mixer.music.get_busy() and Gus.current <= len(playlist):
            Gus.current+=1
            pygame.mixer.music.load ( playlist[Gus.current])
            pygame.mixer.music.play()
        elif not pygame.mixer.music.get_busy() and Gus.current > len(playlist):
            Gus.current=0
            pygame.mixer.music.load ( playlist[Gus.current])
            pygame.mixer.music.play()
            
        if gus_run:
            speed_move = 3
        else:
            speed_move = Gus.speed
            
        if frame_count <= 30:
            frame_count += 1
        else:
            frame_count = 0
        
        if frame_count <= 15:
            a=0
        elif frame_count > 15:
            a=1
            
        rect_gugus = gugus.get_rect() 
        tr.update_items()
        Gus.update_items(tr)
        sac.update_items(tr)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    other_s.play()
                    Gus.pause += 1    
                if event.key == pygame.K_TAB:
                    other_s.play() 
            ############################
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  
                    x_change = -speed_move
                    rel_x = speed_move
                    y_change = 0
                    rel_y = 0
                    step_s.play(-1)
                elif event.key == pygame.K_RIGHT:
                    x_change = speed_move
                    rel_x = -speed_move
                    y_change = 0
                    rel_y = 0
                    step_s.play(-1)
                elif event.key == pygame.K_UP:
                    y_change = -speed_move
                    rel_y = speed_move
                    x_change = 0
                    rel_x = 0
                    step_s.play(-1)
                elif event.key == pygame.K_DOWN:
                    y_change = speed_move
                    rel_y = -speed_move
                    x_change = 0
                    rel_x = 0
                    step_s.play(-1)
                if event.key == pygame.K_a and not action.click:
                    action.click = True
                    click_.play()
                    #PERSONNES
                    ###EST
                    if 325+screen_x < x < 360+screen_x and 315+screen_y < y < 355+screen_y and Gus.level == 2 and sac.Clopes == 0:
                        tr.pressed_vieille = 0
                    if 325+screen_x < x < 360+screen_x and 315+screen_y < y < 355+screen_y and Gus.level == 2 and sac.Clopes == 1 and tr.show_photo == False and tr.apporte_clope == False:
                        tr.pressed_vieille = 1
                    if 325+screen_x < x < 360+screen_x and 315+screen_y < y < 355+screen_y and Gus.level == 2 and sac.Clopes == 2 and tr.show_photo == False and tr.apporte_clope == False:
                        tr.pressed_vieille = 4
                        tr.apporte_clope = True
                    if 325+screen_x < x < 360+screen_x and 315+screen_y < y < 355+screen_y and Gus.level == 2 and sac.Photos == 0 and tr.show_photo == False and tr.apporte_clope == True:
                        tr.pressed_vieille = 2
                    if 325+screen_x < x < 360+screen_x and 315+screen_y < y < 355+screen_y and Gus.level == 2 and sac.Photos == 1 and tr.apporte_clope == True:
                        tr.pressed_vieille = 4
                        tr.show_photo = True
                    if 325+screen_x < x < 360+screen_x and 315+screen_y < y < 355+screen_y and Gus.level == 2 and tr.vente_teu == True and tr.miss_money == 1 and tr.show_photo == True:
                        tr.pressed_vieille = 3
                        
                    if 550+screen_x < x < 600+screen_x and 510+screen_y < y < 555+screen_y and Gus.level == 2 and tr.repair_inter == False:
                        tr.pressed_interphone = 0
                    if 550+screen_x < x < 600+screen_x and 510+screen_y < y < 555+screen_y and Gus.level == 2 and tr.repair_inter == True and tr.miss_money == 0:
                        tr.pressed_interphone = 1
                    if 550+screen_x < x < 600+screen_x and 510+screen_y < y < 555+screen_y and Gus.level == 2 and tr.repair_inter == True and tr.miss_money == 1:
                        tr.pressed_interphone = 2
                    #OBJETS
                    ###EST
                    if 638+screen_x < x < 700+screen_x and 500+screen_y < y < 520+screen_y and Gus.level == 2:
                        tr.pressed_arbre += 1  
                    if 635+screen_x < x < 792+screen_x and 320+screen_y < y < 368+screen_y and Gus.level == 2:
                        tr.pressed_papier = 0
                    if 680+screen_x < x < 712+screen_x and 88+screen_y < y < 140+screen_y and Gus.level == 2 and sac.Clef == 1 :
                        tr.press_cave += 1
                        tr.collect_bonbon = True

                    ###NORD EST
                    ##INTERACTIONS
                    if 777+screen_x < x < 870+screen_x and 20+screen_y < y < 70+screen_y and Gus.level == 2.1 and tr.miss_money == 0:
                        tr.pressed_stuff = 0
                    if 777+screen_x < x < 870+screen_x and 20+screen_y < y < 70+screen_y and Gus.level == 2.1 and tr.miss_money == 1:
                        tr.pressed_stuff = 1
                        tr.fouille_sac = True
                    if 894+screen_x < x < 940+screen_x and 20+screen_y < y < 70+screen_y and Gus.level == 2.1:
                        tr.pressed_tox = 0
                    if 894+screen_x < x < 940+screen_x and 20+screen_y < y < 70+screen_y and Gus.level == 2.1 and sac.Teuteu == 0 and tr.miss_money == 1:
                        tr.pressed_tox = 1
                    ##ITEMS
                    if 780+screen_x < x < 830+screen_x and 530+screen_y < y < 560+screen_y and Gus.level == 2.1:
                        tr.pressed_seringue += 1
                    if 70+screen_x < x < 110+screen_x and 0+screen_y < y < 32+screen_y and Gus.level == 2.1:
                        tr.pressed_ball += 1
                        
                    ###NORD
                    ##INTERACTIONS
                    if interact and Gus.level == 2.2 and sac.Bonbons_bizarres == 0 and tr.pressed_vieille < 3:
                        tr.pressed_con = 0
                    if interact and Gus.level == 2.2 and sac.Bonbons_bizarres > 0:
                        tr.pressed_con = 1
                    if interact and Gus.level == 2.2 and sac.Bonbons_bizarres == 0 and tr.miss_money == 1 and tr.pressed_vieille == 3 and sac.Filtre_postillon == 0 and tr.missions_con == False:
                        tr.pressed_con = 3                   
                    if interact and Gus.level == 2.2 and sac.Bonbons_bizarres == 0 and tr.repair_inter == False and tr.pressed_vieille == 3 and sac.Filtre_postillon == 1:
                        tr.pressed_con = 4                   
                    if interact and Gus.level == 2.2 and sac.Bonbons_bizarres == 0 and tr.repair_inter == True and sac.Filtre_postillon == 0 and sac.Seringue < 4 and tr.missions_con == False and tr.miss_money == 0:
                        tr.pressed_con = 0
                    if interact and Gus.level == 2.2 and sac.Bonbons_bizarres == 0 and tr.repair_inter == True and sac.Filtre_postillon == 0 and sac.Seringue < 4 and tr.missions_con == False and tr.miss_money == 1:
                        tr.pressed_con = 5  
                    if interact and Gus.level == 2.2 and sac.Bonbons_bizarres == 0 and tr.repair_inter == True and sac.Filtre_postillon == 0 and sac.Seringue == 4 and tr.missions_con == False:
                        tr.pressed_con = 6    
                    if interact and Gus.level == 2.2 and sac.Bonbons_bizarres == 0 and tr.repair_inter == True and sac.Huile_rateau == 1 and sac.Seringue == 4 :
                        tr.pressed_con = 7
                        tr.missions_con = True
                        ##ITEMS
                    if 79+screen_x < x < 160+screen_x and 438+screen_y < y < 467+screen_y and Gus.level == 2.2:
                        tr.press_poub += 1
                    if 0+screen_x < x < 45+screen_x and 0+screen_y < y < 45+screen_y and Gus.level == 2.2:
                        tr.press_coin += 1
                    if 480+screen_x < x < 550+screen_x and 85+screen_y < y < 170+screen_y and Gus.level == 2.2:
                        tr.tree_22 += 1
                        
                    ###NORD OUEST
                    if interact and Gus.level == 2.3 and sac.Ballon == 0 and tr.ask_phone == False:
                        tr.press_vois = 0
                    if interact and Gus.level == 2.3 and sac.Ballon == 1:
                        tr.press_vois = 1
                        tr.ask_phone = True
                        sac.Ballon = 0
                    if interact and Gus.level == 2.3 and sac.Ballon == 0 and sac.Telephone == 1 and tr.ask_phone == True:
                        tr.press_vois = 2
                    if interact and Gus.level == 2.3 and sac.Ballon == 0 and sac.Telephone == 0 and tr.ask_phone == True:
                        tr.press_vois = 1
                        
                    if 525+screen_x < x < 575+screen_x and 400+screen_y < y < 445+screen_y and Gus.level == 2.3:
                        tr.press_poub2 += 1                        
                    if 0+screen_x < x < 58+screen_x and 140+screen_y < y < 190+screen_y and Gus.level == 2.3:
                        tr.press_car+= 1   
                        
                    ###OUEST
                    if 125+screen_x < x < 188+screen_x and 465+screen_y < y < 550+screen_y and Gus.level == 2.4 and tr.ask_deal == False and tr.tout_vendu == False:
                        tr.press_dealer = 0
                    if 125+screen_x < x < 188+screen_x and 465+screen_y < y < 550+screen_y and Gus.level == 2.4 and tr.ask_deal == True and tr.tout_vendu == False:
                        tr.press_dealer = 1
                    if 125+screen_x < x < 188+screen_x and 465+screen_y < y < 550+screen_y and Gus.level == 2.4 and tr.tout_vendu == True and tr.accept_deal == False:
                        tr.press_dealer = 2
                    if 125+screen_x < x < 188+screen_x and 465+screen_y < y < 550+screen_y and Gus.level == 2.4 and tr.tout_vendu == True and tr.accept_deal == True and tr.vente_teu == False:
                        tr.press_dealer = 3
                    if 125+screen_x < x < 188+screen_x and 465+screen_y < y < 550+screen_y and Gus.level == 2.4 and tr.vente_teu == True and tr.accept_deal == True and tr.miss_money == 1:
                        tr.press_dealer = 4
                    if 125+screen_x < x < 188+screen_x and 465+screen_y < y < 550+screen_y and Gus.level == 2.4 and tr.argent_teu == 10 and tr.argent_con == 10 and tr.missions_con == True and sac.Telephone == 0:
                        tr.press_dealer = 5
                        sac.Huile_rateau = 0
                    if 125+screen_x < x < 188+screen_x and 465+screen_y < y < 550+screen_y and Gus.level == 2.4 and tr.argent_teu == 10 and tr.argent_con == 10 and tr.missions_con == True and sac.Telephone == 1:
                        tr.press_dealer = 5
                    if 125+screen_x < x < 188+screen_x and 465+screen_y < y < 550+screen_y and Gus.level == 2.4 and tr.argent_teu == 10 and tr.argent_con == 10 and tr.missions_con == True and sac.Telephone == 0:
                        tr.press_dealer = 6
                        
                    if 420+screen_x < x < 490+screen_x and 480+screen_y < y < 510+screen_y and Gus.level == 2.4 and sac.Clef == 0:
                        tr.press_pnj_bus = 0
                    if 420+screen_x < x < 490+screen_x and 480+screen_y < y < 510+screen_y and Gus.level == 2.4 and sac.Clef == 1 and sac.Bonbons_bizarres == 0 and tr.tout_vendu == False:
                        tr.press_pnj_bus = 1
                    if 420+screen_x < x < 490+screen_x and 480+screen_y < y < 510+screen_y and Gus.level == 2.4 and sac.Clef == 1 and (sac.Bonbons_bizarres > 0 or tr.tout_vendu == True):
                        tr.press_pnj_bus = 2
                    if 370+screen_x < x < 390+screen_x and 475+screen_y < y < 510+screen_y and Gus.level == 2.4 and sac.Telephone == 1:
                        tr.horaire_bus += 1
                    if 526+screen_x < x < 594+screen_x and 430+screen_y < y < 500+screen_y and Gus.level == 2.4 and tr.vire_dealer == False:
                        tr.press_conduct = 0 
                    if 526+screen_x < x < 594+screen_x and 430+screen_y < y < 500+screen_y and Gus.level == 2.4 and tr.vire_dealer == True:
                        tr.press_conduct = 1 
                    if 920+screen_x < x < 975+screen_x and 444+screen_y < y < 504+screen_y and Gus.level == 2.4:
                        tr.back_bus += 1
                        
                    ###NORD-NORD
                    if 340+screen_x < x < 400+screen_x and 410+screen_y < y < 445+screen_y and Gus.level == 2.5:
                        tr.nord1 += 1   
                    if 400+screen_x < x < 536+screen_x and 430+screen_y < y < 450+screen_y and Gus.level == 2.5 and tr.repair_inter == False:
                        tr.nord2 += 1 
                    if 540+screen_x < x < 620+screen_x and 510+screen_y < y < 540+screen_y and Gus.level == 2.5:
                        tr.nord3 += 1
                         
                elif event.key != pygame.K_a:
                
                    action.click = False
                
                if event.key == pygame.K_LCTRL:
                    if interact and Gus.level == 2.2 and sac.Bonbons_bizarres == 0 and tr.repair_inter == True and tr.missions_con == True and sac.Seringue == 4:
                        tr.pressed_con = 8
                        sac.Huile_rateau = 0
                        tr.vire_dealer = True
                elif event.key != pygame.K_LCTRL:
                    gus_run = False
                
                if event.key == pygame.K_RETURN:
                    enter_s.play()
                    if 550+screen_x < x < 600+screen_x and 510+screen_y < y < 555+screen_y and Gus.level == 2 and tr.repair_inter == False and sac.Filtre_postillon == 1:
                        tr.repair_inter = True
                        sac.Filtre_postillon = 0
                    if 777+screen_x < x < 870+screen_x and 20+screen_y < y < 70+screen_y and Gus.level == 2.1 and tr.fouille_sac == True:
                        sac.Huile_rateau = 1
                    if 420+screen_x < x < 490+screen_x and 480+screen_y < y < 510+screen_y and Gus.level == 2.4 and tr.press_pnj_bus == 0:
                        tr.pnj_bus = -0.2  
                        sac.Clef = 1
                    if 325+screen_x < x < 360+screen_x and 315+screen_y < y < 355+screen_y and Gus.level == 2 and sac.Bonbons_bizarres > 0 and tr.argent_vieille == 0:
                        tr.argent_vieille = 0.2
                        sac.Bonbons_bizarres -= 5
                    if 894+screen_x < x < 940+screen_x and 20+screen_y < y < 70+screen_y and Gus.level == 2.1 and sac.Bonbons_bizarres > 0 and tr.argent_tox == 0:
                        tr.argent_tox = 0.2
                        sac.Bonbons_bizarres -= 5
                    if 894+screen_x < x < 940+screen_x and 20+screen_y < y < 70+screen_y and Gus.level == 2.1 and sac.Teuteu > 0 and tr.argent_teu == 0:
                        tr.argent_teu = 10
                        sac.Teuteu =  0
                        tr.vente_teu = True
                        tr.miss_money = 1
                    if interact == True and Gus.level == 2.2 and sac.Bonbons_bizarres != 0:
                        zone_dialogue(screen,"Parler au concierge (A)",action,phrases_con[0],0,2)
                    if interact == True and Gus.level == 2.2 and tr.pressed_con == 1:
                        tr.ask_con = True
                        tr.pressed_con = 2
                    if interact and Gus.level == 2.2 and sac.Bonbons_bizarres == 0 and tr.repair_inter == True and sac.Huile_rateau == 1 and sac.Seringue == 4:
                        tr.argent_con = 10 
                    if 125+screen_x < x < 188+screen_x and 465+screen_y < y < 550+screen_y and Gus.level == 2.4 and sac.Bonbons_bizarres > 0:
                        tr.ask_deal = True
                    if 125+screen_x < x < 188+screen_x and 465+screen_y < y < 550+screen_y and Gus.level == 2.4 and tr.tout_vendu == True and tr.miss_money == 0:
                        sac.Teuteu = 1
                        tr.accept_deal = True

                    if interact and Gus.level == 2.3 and sac.Ballon == 0 and tr.ask_phone == True:
                        sac.Telephone = 1
                    if interact and Gus.level == 2.3 and sac.Ballon == 0 and tr.ask_phone == True and tr.press_vois == 2:
                        sac.Telephone = 0
                        sac.Photos = 0
                    if 420+screen_x < x < 490+screen_x and 480+screen_y < y < 510+screen_y and Gus.level == 2.4 and sac.Bonbons_bizarres > 0 and tr.argent_vois == 0:
                        tr.argent_vois = 0.2
                        sac.Bonbons_bizarres -= 5                         
                    if 526+screen_x < x < 594+screen_x and 450+screen_y < y < 500+screen_y and Gus.level == 2.4 and sac.Bonbons_bizarres > 0 and tr.argent_cond == 0:
                        tr.argent_cond = 0.2 
                        sac.Bonbons_bizarres -= 5
                    if 526+screen_x < x < 594+screen_x and 430+screen_y < y < 500+screen_y and Gus.level == 2.4 and tr.vire_dealer == True and sac.Telephone == 0:
                        tr.ticket_bus = -1
                        Gus.level = 0
                        Gus.spawn = 1
                        time = 0
                        
                    if 125+screen_x < x < 188+screen_x and 465+screen_y < y < 550+screen_y and Gus.level == 2.4 and tr.argent_teu == 10 and tr.argent_con == 10 and tr.missions_con == True and sac.Telephone == 0:
                        Gus.level = 3
                        Gus.spawn = 1
                        time = 0
                            
                elif event.key != pygame.K_RETURN:
                
                    action.change_level = False
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_change = 0
                    rel_x = 0
                    gugus = gugus_gauche 
                    step_s.stop()
                if event.key == pygame.K_RIGHT:
                    x_change = 0
                    rel_x = 0
                    gugus = gugus_droite 
                    step_s.stop()

                if event.key == pygame.K_UP:
                    y_change = 0
                    rel_y = 0
                    gugus = gugus_dos 
                    step_s.stop()
                    
                if event.key == pygame.K_DOWN:
                    y_change = 0
                    rel_y = 0
                    gugus = gugus_face 
                    step_s.stop()
                    
            ######################            
        keys=pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            gugus=gugus_walkdown[a]
        if keys[pygame.K_UP]:
            gugus=gugus_walkup[a]
        if keys[pygame.K_RIGHT]:
            gugus=gugus_walkright[a]
        if keys[pygame.K_LEFT]:
            gugus=gugus_walkleft[a]
            
        rect_gugus.topleft = (x,y)
        
        if tr.pressed_con == 2:
            tr.game_over = True
                
        if Gus.level == 2:
    
            if Gus.spawn == 1 and time < 2:
                screen_x,screen_y,x,y = spawn_level(x,y,229,224)
            elif Gus.spawn == 2 and time < 2:
                screen_x,screen_y,x,y = spawn_level(x,y,1001-gugus_width,80)
        
            time += 1
            liste_mur = level_2(screen,screen_x,screen_y)
               
            if rat2.side == "left":
                rat2 = pnj(spawn_x,spawn_y,screen_x,screen_y,rat_left,'left')
            elif rat2.side == "right":
                rat2 = pnj(spawn_x,spawn_y,screen_x,screen_y,rat_right,'right')
                
            speed_x,speed_y = rat2.collisions_pnj(liste_mur,speed_x,speed_y,rat_right,rat_left,0)
            spawn_x,spawn_y = rat2.move(spawn_x,spawn_y,speed_x,speed_y)
            
            x_change,y_change,rel_x,rel_y = collisions(liste_mur,rect_gugus,x_change,y_change,speed_move,rel_x,rel_y)
    
            if rat2.rect.colliderect(rect_gugus) and rat2.side == "left":
                if abs (rat2.rect.left - rect_gugus.right) <= 10:
                    speed_x *= -1
                    speed_y *= -1
                    rat2.side = "right"
                    
            if rat2.rect.colliderect(rect_gugus) and rat2.side == "right":
                if abs (rat2.rect.right - rect_gugus.left) <= 10:
                    speed_x *= -1
                    speed_y *= -1
                    rat2.side = "left"
                    
            if rect_gugus.colliderect(rat2.rect):
                if abs (rat2.rect.left - rect_gugus.right) <= 10:
                    x_change = 0
                    rel_x = 0
            if rat2.rect.colliderect(rect_gugus):
                if abs (rat2.rect.right - rect_gugus.left) <= 10:
                    x_change = 0
                    rel_x = 0           
            screen_x += rel_x
            screen_y += rel_y
            
            screen.blit(rat2.image, rat2.rect)
        
            if y < -2:
                Gus.level = 2.1
                Gus.spawn = 1
                time = 0

            
        elif Gus.level == 2.1:
            
            if Gus.spawn == 1 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,1001-gugus_width,481)

            if Gus.spawn == 2 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,1+gugus_width,481)
                        
            time += 1
            
            liste_mur = level_2NE(screen,screen_x,screen_y)
        
            x_change,y_change,rel_x,rel_y = collisions(liste_mur,rect_gugus,x_change,y_change,speed_move,rel_x,rel_y)
            
            screen_x += rel_x
            screen_y += rel_y
            
            if y > 460 :
                Gus.level = 2
                Gus.spawn = 2
                time = 0
            if x < 0:
                Gus.level = 2.2
                Gus.spawn = 1
                time = 0

            
        elif Gus.level == 2.2:
            
            if Gus.spawn == 1 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,1001-gugus_width,481)

            elif Gus.spawn == 2 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,1+gugus_width,481)

            if Gus.spawn == 3 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,191,12) 

            if Gus.spawn == 4 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,510,631)
                                           
            time += 1
            
            liste_mur = level_2N(screen,screen_x,screen_y)
        
            x_change,y_change,rel_x,rel_y = collisions(liste_mur,rect_gugus,x_change,y_change,speed_move,rel_x,rel_y)
            
            pnj_concierge = concierge[a]
            rect_concierge = pnj_concierge.get_rect()
            rect_concierge.topleft=(783+screen_x,383+screen_y)
                  
            if rect_gugus.colliderect(rect_concierge) and x_change > 0:
                if abs (rect_concierge.left - rect_gugus.right) <= 10:
                    x_change = 0
                    rel_x = 0
            if rect_gugus.colliderect(rect_concierge) and x_change < 0:
                if abs (rect_concierge.right - rect_gugus.left) <= 10:
                    x_change = 0
                    rel_x = 0   
            if rect_gugus.colliderect(rect_concierge) and y_change < 0:
                if abs (rect_concierge.bottom - rect_gugus.top) <= 10:
                    y_change = 0
                    rel_y = 0
                    interact = True                    
            if rect_gugus.colliderect(rect_concierge) and y_change > 0:
                if abs (rect_concierge.top - rect_gugus.bottom) <= 10:
                    y_change = 0
                    rel_y = 0  
            if not rect_gugus.colliderect(rect_concierge):
                interact = False       
                
            screen_x += rel_x
            screen_y += rel_y
        
            screen.blit(pnj_concierge, rect_concierge)
            
            if Gus.spawn == 4 and time < 150: 
                textsurface = myfont.render("Aïe ma cheville!", False, (110, 110, 110))
                screen.blit(fond_text,(260,380))
                screen.blit(textsurface,(280,400))

            if x < 0 :
                Gus.level = 2.3
                Gus.spawn = 1
                time = 0
            if y < 0:
                Gus.level = 2.5
                Gus.spawn = 1
                time = 0
            if x > 480 :
                Gus.level = 2.1
                Gus.spawn = 2
                time = 0   
                
        elif Gus.level == 2.3:
            
            if Gus.spawn == 1 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,1001-gugus_width,481)
                
            if Gus.spawn == 2 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,111,651) 
                
            time += 1
            
            liste_mur = level_2NO(screen,screen_x,screen_y)
            
            if dame.movement == True:
                dame_left = dame_l[a]            
                dame_right = dame_d[a]
            elif dame.movement == False:
                dame_left = dame_l[2]            
                dame_right = dame_d[2]
                
            if dame.side == "left":
                dame = pnj(spawn_damex,spawn_damey,screen_x,screen_y,dame_left,'left')
            elif dame.side == "right":
                dame = pnj(spawn_damex,spawn_damey,screen_x,screen_y,dame_right,'right')
            
            speed_x,speed_y = dame.collisions_pnj(liste_mur,speed_x,speed_y,dame_right,dame_left,0)
            spawn_damex,spawn_damey = dame.move(spawn_damex,spawn_damey,speed_x,speed_y)
            
            x_change,y_change,rel_x,rel_y = collisions(liste_mur,rect_gugus,x_change,y_change,speed_move,rel_x,rel_y)
    
            if dame.rect.colliderect(rect_gugus) and dame.side == "left":
                if abs (dame.rect.left - rect_gugus.right) <= 10:
                    speed_x *= 0
                    speed_y *= -1
                    dame.movement = False
                    interact = True

            if dame.rect.colliderect(rect_gugus) and dame.side == "right":
                if abs (dame.rect.right - rect_gugus.left) <= 10:
                    speed_x = 0
                    speed_y *= -1  
                    dame.movement = False
                    interact = True
                    
            if not dame.rect.colliderect(rect_gugus) and dame.side == "left":
                if abs (dame.rect.left - rect_gugus.right) <= 10:
                    speed_x = -1
                    speed_y *= -1
                    dame.side = "left"
                    dame.movement = True

            if not dame.rect.colliderect(rect_gugus) and dame.side == "right":
                if abs (dame.rect.right - rect_gugus.left) <= 10:
                    speed_x = 1
                    speed_y *= -1
                    dame.side = "right" 
                    dame.movement = True
                                        

            if rect_gugus.colliderect(dame.rect):
                if abs (dame.rect.left - rect_gugus.right) <= 10 and x_change > 0:
                    x_change = 0
                    rel_x = 0
            if rect_gugus.colliderect(dame.rect):
                if abs (dame.rect.right - rect_gugus.left) <= 10 and x_change < 0:
                    x_change = 0
                    rel_x = 0     
            if rect_gugus.colliderect(dame.rect):
                if abs (dame.rect.bottom - rect_gugus.top) <= 10 and y_change < 0:
                    y_change = 0
                    rel_y = 0    
            if rect_gugus.colliderect(dame.rect):
                if abs (dame.rect.top - rect_gugus.bottom) <= 10 and y_change > 0:
                    y_change = 0
                    rel_y = 0   
            if not rect_gugus.colliderect(dame.rect):
                interact = False 
                
            screen_x += rel_x
            screen_y += rel_y
            
            screen.blit(dame.image, dame.rect)
            
            if x > 480 :
                Gus.level = 2.2
                Gus.spawn = 2
                time = 0
            if y > 465:
                Gus.level = 2.4
                Gus.spawn = 1
                time = 0
                
        elif Gus.level == 2.4:
            
            if Gus.spawn == 1 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,111,50)
                        
            time += 1
            
            if tr.vire_dealer == False:
                liste_mur = level_2O(screen,screen_x,screen_y)
            if tr.vire_dealer == True:
                liste_mur = level_2O_ohne(screen,screen_x,screen_y)
        
            x_change,y_change,rel_x,rel_y = collisions(liste_mur,rect_gugus,x_change,y_change,speed_move,rel_x,rel_y)
            
            screen_x += rel_x
            screen_y += rel_y
            
            if y < 0:
                Gus.level = 2.3
                Gus.spawn = 2
                time = 0
            
        elif Gus.level == 2.5:
            
            if Gus.spawn == 1 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,191,655)
                        
            time += 1
            
            liste_mur = level_2NN(screen,screen_x,screen_y)
            
            if rat_nord.side == "left":
                rat_nord = pnj(spawnx_nord,spawny_nord,screen_x,screen_y,rat_left,'left')
            elif rat_nord.side == "right":
                rat_nord = pnj(spawnx_nord,spawny_nord,screen_x,screen_y,rat_right,'right')
                
            speed_x,speed_y = rat_nord.collisions_pnj(liste_mur,speed_x,speed_y,rat_right,rat_left,0)
            spawnx_nord,spawny_nord = rat_nord.move(spawnx_nord,spawny_nord,speed_x,speed_y)
        
            x_change,y_change,rel_x,rel_y = collisions(liste_mur,rect_gugus,x_change,y_change,speed_move,rel_x,rel_y)
            
            if rat_nord.rect.colliderect(rect_gugus) and rat_nord.side == "left":
                if abs (rat_nord.rect.left - rect_gugus.right) <= 10:
                    speed_x *= -1
                    speed_y *= -1
                    rat_nord.side = "right"
                    
            if rat_nord.rect.colliderect(rect_gugus) and rat_nord.side == "right":
                if abs (rat_nord.rect.right - rect_gugus.left) <= 10:
                    speed_x *= -1
                    speed_y *= -1
                    rat_nord.side = "left"
                    
            if rect_gugus.colliderect(rat_nord.rect):
                if abs (rat_nord.rect.left - rect_gugus.right) <= 10:
                    x_change = 0
                    rel_x = 0
            if rat_nord.rect.colliderect(rect_gugus):
                if abs (rat_nord.rect.right - rect_gugus.left) <= 10:
                    x_change = 0
                    rel_x = 0           

            screen_x += rel_x
            screen_y += rel_y
            
            screen.blit(rat_nord.image, rat_nord.rect)

            
            if y > 465:
                Gus.level = 2.2
                Gus.spawn = 3
                time = 0             
         
        if tr.press_poub >= 0:
            tr.argent_poub = 0.1 
        
        if tr.collect_bonbon and sac.Bonbons_bizarres == 0:
            tr.tout_vendu = True
        
        ##INTERACTION LVL 2
        if 325+screen_x < x < 360+screen_x and 315+screen_y < y < 355+screen_y and Gus.level == 2:

            zone_dialogue(screen,"Parler à la vieille (A)",action,phrases_vieille[tr.pressed_vieille],tr.pressed_vieille,5)
            
            if sac.Bonbons_bizarres > 0 and tr.argent_vieille == 0:
                textsurface = myfont.render("Proposer des bonbons", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40))  
            
        elif 550+screen_x < x < 600+screen_x and 510+screen_y < y < 555+screen_y and Gus.level == 2:

            zone_dialogue(screen,"Sonner à l'interphone (A)",action,phrases_interphone[tr.pressed_interphone],tr.pressed_interphone,4)
            
            if sac.Filtre_postillon == 1 and tr.repair_inter == False:
                textsurface = myfont.render("Réparer l'interphone.", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40))       
        ##OBJET LVL 2
        elif 638+screen_x < x < 700+screen_x and 500+screen_y < y < 520+screen_y and Gus.level == 2:
            
            tr.pressed_arbre = zone_interaction(screen,"Qu'est-ce que c'est? (A)",action,tr.pressed_arbre,"un paquet de clopes!")
            tr.clopesEst = 1
            
        elif 680+screen_x < x < 712+screen_x and 88+screen_y < y < 140+screen_y and Gus.level == 2 and sac.Clef == 0 :

                textsurface = myfont.render("Il y a un truc", False, (110, 110, 110))
                textsurface2 = myfont.render("fermé à clé dans ce", False, (110, 110, 110))
                textsurface3 = myfont.render("carton", False, (110, 110, 110))
                screen.blit(fond_text,(260,380))
                screen.blit(textsurface,(280,400))
                screen.blit(textsurface2,(280,420)) 
                screen.blit(textsurface3,(280,440))  
        
        elif 680+screen_x < x < 712+screen_x and 88+screen_y < y < 140+screen_y and Gus.level == 2 and sac.Clef == 1 and tr.collect_bonbon == False:
            tr.press_cave = zone_interaction(screen,"Ouvrir le coffre (A)",action,tr.press_cave,"plein de bonbons...")
            sac.Bonbons_bizarres = 20
        elif 680+screen_x < x < 712+screen_x and 88+screen_y < y < 140+screen_y and Gus.level == 2 and sac.Clef == 1 and tr.collect_bonbon == True:
            tr.press_cave = zone_interaction(screen,"Ouvrir le coffre (A)",action,tr.press_cave,"plein de bonbons...")
                
        elif 545+screen_x < x < 610+screen_x and 20+screen_y < y < 110+screen_y and Gus.level == 2 :

                textsurface = myfont.render("Beurk...", False, (110, 110, 110))
                screen.blit(fond_text,(260,380))
                screen.blit(textsurface,(280,400))
                
        elif 368+screen_x < x < 513+screen_x and 0+screen_y < y < 35+screen_y and Gus.level == 2 :

                textsurface = myfont.render("Il n'y a rien ", False, (110, 110, 110))
                textsurface2 = myfont.render("d'intéressant sur", False, (110, 110, 110))
                textsurface3 = myfont.render(" ce tableau.", False, (110, 110, 110))
                screen.blit(fond_text,(260,380))
                screen.blit(textsurface,(280,400))
                screen.blit(textsurface2,(280,420)) 
                screen.blit(textsurface3,(280,440))
        
        elif 33+screen_x < x < 231+screen_x and 0+screen_y < y < 50+screen_y and Gus.level == 2 :

                textsurface = myfont.render("Elles sont toutes ", False, (110, 110, 110))
                textsurface2 = myfont.render("fermées à clé.", False, (110, 110, 110))
                screen.blit(fond_text,(260,380))
                screen.blit(textsurface,(280,400))
                
                screen.blit(textsurface2,(280,420))
                
        elif 635+screen_x < x < 792+screen_x and 320+screen_y < y < 368+screen_y and Gus.level == 2:

            zone_dialogue(screen,"Fouiller ici (A)",action,phrases_papier[tr.pressed_papier],tr.pressed_papier,1)
        
        #### LVL 2.1
        ##INTERACTIONS
        elif 777+screen_x < x < 870+screen_x and 20+screen_y < y < 70+screen_y and Gus.level == 2.1:
            zone_dialogue(screen,"Fouiller les affaires (A)",action,phrases_stuff[tr.pressed_stuff],tr.pressed_stuff,2)
            if tr.vente_teu == True and tr.fouille_sac == True:
                textsurface = myfont.render("Fouiller le sac", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x-120,y-60))
                screen.blit(textsurface2,(x-25,y-40)) 
        elif 894+screen_x < x < 940+screen_x and 20+screen_y < y < 70+screen_y and Gus.level == 2.1:
            zone_dialogue(screen,"Parler avec le toxico (A)",action,phrases_toxo[tr.pressed_tox],tr.pressed_tox,2)
            
            if sac.Bonbons_bizarres > 0 and tr.argent_tox == 0:
                textsurface = myfont.render("Proposer des bonbons", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x-120,y-60))
                screen.blit(textsurface2,(x-25,y-40)) 
            if sac.Teuteu > 0 and tr.argent_teu == 0 and tr.vente_teu == False:
                textsurface = myfont.render("Proposer le teuteu", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x-120,y-60))
                screen.blit(textsurface2,(x-25,y-40))                         
        ##ITEMS
        elif 780+screen_x < x < 830+screen_x and 530+screen_y < y < 560+screen_y and Gus.level == 2.1:
            tr.pressed_seringue = zone_interaction(screen,"Qu'est-ce que c'est? (A)",action,tr.pressed_seringue,"un seringue!")
            tr.seringue_NE = 1
            
        elif 70+screen_x < x < 110+screen_x and 0+screen_y < y < 32+screen_y and Gus.level == 2.1:        
            tr.pressed_ball = zone_interaction(screen,"Qu'est-ce que c'est? (A)",action,tr.pressed_ball,"un ballon!")
            sac.Ballon = 1
            
        elif 395+screen_x < x < 450+screen_x and 540+screen_y < y < 590+screen_y and Gus.level == 2.1 :

            textsurface = myfont.render("Beurk...", False, (110, 110, 110))
            screen.blit(fond_text,(x,y-80))
            screen.blit(textsurface,(x+20,y-60))
            
        elif 750+screen_x < x < 840+screen_x and 630+screen_y < y < 707+screen_y and Gus.level == 2.1 :

            textsurface = myfont.render("Beurk...", False, (110, 110, 110))
            screen.blit(fond_text,(x,y-80))
            screen.blit(textsurface,(x+20,y-60))
            
        ###LVL 2.2
        ##INTERACTIONS
        elif interact == True and Gus.level == 2.2:
            zone_dialogue(screen,"Parler au concierge (A)",action,phrases_con[tr.pressed_con],tr.pressed_con,9)
            
            if sac.Bonbons_bizarres > 0 and tr.pressed_con != 1:
                textsurface = myfont.render("Proposer des bonbons", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40)) 
            elif sac.Bonbons_bizarres > 0 and tr.pressed_con == 1:
                textsurface = myfont.render("Vendre quand même", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40))  
            if sac.Bonbons_bizarres == 0 and tr.repair_inter == True and sac.Huile_rateau == 1 and sac.Seringue == 4:
                textsurface = myfont.render("Prendre l'argent", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40))  
                
                textsurface3 = myfont.render("Demander un service", False, (0, 0, 0))
                textsurface4 = myfont.render("CTRL", False, (0, 0, 0))
                screen.blit(textsurface3,(x-150,y-60))
                screen.blit(textsurface4,(x-65,y-40))   
        ##ITEMS
        elif 79+screen_x < x < 160+screen_x and 438+screen_y < y < 467+screen_y and Gus.level == 2.2:
            tr.press_poub = zone_interaction(screen,"Fouiller les poubelles (A)",action,tr.press_poub,"10 centimes!")
        elif 0+screen_x < x < 45+screen_x and 0+screen_y < y < 45+screen_y and Gus.level == 2.2 :
            tr.press_coin = zone_interaction(screen,"Qu'est-ce que c'est? (A)",action,tr.press_coin,"un drôle de truc!")
            tr.capoteNord = 1
        elif 480+screen_x < x < 550+screen_x and 85+screen_y < y < 170+screen_y and Gus.level == 2.2:
            tr.tree_22 = zone_interaction(screen,"Qu'est-ce que c'est? (A)",action,tr.tree_22,"une seringue!")
            tr.seringueN = 1
            
        ###LVL 2.3
        ##INTERACTIONS
        elif interact == True and Gus.level == 2.3:
            zone_dialogue(screen,"Parler à la voisine (A)",action,phrases_vois[tr.press_vois],tr.press_vois,3)
            
            if sac.Ballon == 0 and tr.ask_phone == True and tr.press_vois == 1:
                textsurface = myfont.render("Demander le téléphone", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40)) 
            if sac.Ballon == 0 and tr.ask_phone == True and tr.press_vois == 2:
                textsurface = myfont.render("Rendre le téléphone", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40)) 
                
        elif 162+screen_x < x < 262+screen_x and 50+screen_y < y < 161+screen_y and Gus.level == 2.3 :
                textsurface = myfont.render("C'est la voiture de", False, (110, 110, 110))
                textsurface2 = myfont.render("papa.", False, (110, 110, 110))
                screen.blit(fond_text,(260,380))
                screen.blit(textsurface,(280,400))
                screen.blit(textsurface2,(280,420)) 
        ##ITEMS
        elif 525+screen_x < x < 575+screen_x and 400+screen_y < y < 445+screen_y and Gus.level == 2.3:
            tr.press_poub2 = zone_interaction(screen,"Fouiller la poubelle (A)",action,tr.press_poub2,"une seringue!")
            tr.seringue_NO = 1
        elif 0+screen_x < x < 58+screen_x and 140+screen_y < y < 190+screen_y and Gus.level == 2.3:            
            tr.press_car = zone_interaction(screen,"Qu'est-ce que c'est? (A)",action,tr.press_car,"un fond d'alcool!")
            tr.bouteille_NO = 1
            
        ###LVL 2.4
        ##INTERACTIONS
        elif 125+screen_x < x < 188+screen_x and 465+screen_y < y < 550+screen_y and Gus.level == 2.4:
            zone_dialogue(screen,"Parler au dealer (A)",action,phrases_deal[tr.press_dealer],tr.press_dealer,7)
            
            if sac.Bonbons_bizarres > 0 and tr.ask_deal == False:
                textsurface = myfont.render("Proposer des bonbons", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40)) 
                
        elif 420+screen_x < x < 490+screen_x and 480+screen_y < y < 510+screen_y and Gus.level == 2.4:
            zone_dialogue(screen,"Parler au voisin (A)",action,phrases_pnj_bus[tr.press_pnj_bus],tr.press_pnj_bus,3)
            
            if sac.Bonbons_bizarres > 0 and tr.argent_vois == 0:
                textsurface = myfont.render("Proposer des bonbons", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40)) 
                
        elif 370+screen_x < x < 390+screen_x and 475+screen_y < y < 510+screen_y and Gus.level == 2.4 and sac.Telephone == 0:
                textsurface = myfont.render("Ce sont les  ", False, (110, 110, 110))
                textsurface2 = myfont.render("horaires du bus..", False, (110, 110, 110))
                screen.blit(fond_text,(260,380))
                screen.blit(textsurface,(280,400))
                screen.blit(textsurface2,(280,420))
                
        elif 370+screen_x < x < 390+screen_x and 475+screen_y < y < 510+screen_y and Gus.level == 2.4 and sac.Telephone == 1:
            tr.horaire_bus = zone_interaction(screen,"Prendre en photo (A)",action,tr.horaire_bus,"les horaires du bus!")
            sac.Photos = 1 
        
        elif 920+screen_x < x < 975+screen_x and 444+screen_y < y < 504+screen_y and Gus.level == 2.4:
            tr.back_bus = zone_interaction(screen,"Regarder sour le bus (A)",action,tr.back_bus,"une seringue!")
            tr.seringueO = 1 
            
        elif 526+screen_x < x < 594+screen_x and 430+screen_y < y < 500+screen_y and Gus.level == 2.4:
            zone_dialogue(screen,"Parler au conducteur (A)",action,phrases_conducteur[tr.press_conduct],tr.press_conduct,2) 
            
            if sac.Bonbons_bizarres > 0 and tr.argent_cond == 0:
                textsurface = myfont.render("Proposer des bonbons", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40)) 
            if tr.vire_dealer == True and tr.ticket_bus == 0 and sac.Telephone == 1:
                textsurface = myfont.render("Tu as un téléphone", False, (0, 0, 0))
                textsurface2 = myfont.render("qui ne t'appartient pas", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x,y-40)) 
            if tr.vire_dealer == True and tr.ticket_bus == 0 and sac.Telephone == 0:
                textsurface = myfont.render("Partir en bus", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40)) 
                                                
        ###LVL 2.5
        ##ITEMS
        elif 340+screen_x < x < 400+screen_x and 410+screen_y < y < 445+screen_y and Gus.level == 2.5:
            tr.nord1 = zone_interaction(screen,"Fouiller la poubelle (A)",action,tr.nord1,"un drôle de truc!")
            capote_nn = 1  
        elif 400+screen_x < x < 536+screen_x and 430+screen_y < y < 450+screen_y and Gus.level == 2.5 and tr.repair_inter == False:
            tr.nord2 = zone_interaction(screen,"Fouiller la poubelle (A)",action,tr.nord2,"un truc electrique!")
            sac.Filtre_postillon = 1
        elif 540+screen_x < x < 620+screen_x and 510+screen_y < y < 540+screen_y and Gus.level == 2.5:
            tr.nord3 = zone_interaction(screen,"Fouiller la poubelle (A)",action,tr.nord3,"quelques clopes!")
            tr.clopes_nn = 1  
###############################################################################################
            
        if screen_x >= 0 and rel_x > 0:
            screen_x = 0
            x -= rel_x
        elif screen_x <= display_width - 1000 and rel_x < 0 :
            screen_x = display_width - 1000
            x -= rel_x
        if screen_y >= 0 and rel_y > 0 :
            screen_y = 0
            y  -= rel_y
        elif screen_y <= display_height - 707 and rel_y < 0:
            screen_y = display_height - 707 
            y -= rel_y
            
        if x < (display_width-gugus_width)/2 and rel_x < 0:
            screen_x = 0
            x -= rel_x
        elif x > (display_width-gugus_width)/2 and rel_x > 0:
            screen_x = display_width - 1000
            x -= rel_x
            
        if y < (display_height-gugus_height)/2 and rel_y < 0:
            screen_y = 0
            y -= rel_y
        elif y > (display_height-gugus_height)/2 and rel_y > 0:
            screen_y = display_height - 707 
            y -= rel_y
        
        ##OBJETS

        screen.blit(gugus, rect_gugus)
        
        pv = Gus_font.render("Santé : " + str(Gus.pv), False, (78, 22, 9))
        argent = Gus_font.render("Argent : " + str(round(Gus.money,2)), False, (31, 160, 85))
        lvl = Gus_font.render("Niveau : " + str(int(Gus.level)), False, (78, 22, 9))
    
        screen.blit(pv , (10,20))
        screen.blit(lvl , (10,45))
        screen.blit(argent , (10,70))
        screen.blit(sac_tab , (10,450))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_TAB]:
            affich_sac(screen,sac)
        if (Gus.pause%2) == 1:
            pause(screen,gameExit,Gus,sac,tr)
        if Gus.pv == 0 or tr.game_over == True:
            game_over(screen)

        pygame.display.update()
        
        clock.tick(100)

def bonus_level(sac,action,Gus,tr):
    pygame.init()
    speed_move = Gus.speed
    frame_count = Gus.frame
    a=0
    time = 0
    x =  20
    y = 20
    rel_x = 0 
    rel_y = 0
    x_change = 0
    y_change = 0
    gugus = gugus_face
    
    screen_x = -225 + x
    screen_y = -225 + y 
    
    interact = False
    tune = Gus.money
    alcool = sac.Alcool
    preservatif = sac.Capote
    
     #CREATION ET CARACTERISTIQUES PNJ  
    start_ticks=pygame.time.get_ticks()
    
    start_x = 195
    start_y = 389
    start_2 = 243
    start_3 = 253
    start_4 = 317
    start_5 = 155
    start_2y = 20
    start_3y = 159
    start_4y = 182
    start_5y = 192
   
    player = pygame.Rect(x, y, 48, 52)
    pnj = bonhomme(start_x, start_y,vieille_bus)
    pnj2 = bonhomme(start_2, start_2y,fond_bus)
    pnj3 = bonhomme(start_3, start_3y,bouteille)
    pnj4 = bonhomme(start_4, start_4y,valise)
    pnj5 = bonhomme(start_5, start_5y,poussette)
    
    liste_pnj = [pnj,pnj2,pnj3,pnj4,pnj5]
    
    gameExit = False
    
    while not gameExit and Gus.level == 0:
        
        if not pygame.mixer.music.get_busy() and Gus.current <= len(playlist):
            Gus.current+=1
            pygame.mixer.music.load ( playlist[Gus.current])
            pygame.mixer.music.play()
        elif not pygame.mixer.music.get_busy() and Gus.current > len(playlist):
            Gus.current=0
            pygame.mixer.music.load ( playlist[Gus.current])
            pygame.mixer.music.play()
            
        seconds=(pygame.time.get_ticks()-start_ticks)/1000
            
        countdown = int(130 - seconds)
        
        if seconds <= 10:
            start = int(10 - seconds)
            liste_mur = level_bonus(screen,0,0)
            
            start_down = big_font.render(str(start), False, (255, 20, 20))
            
            pygame.draw.rect(screen,(20,20,20),(105,115,400,230))            
            pygame.draw.rect(screen,(200,200,200),(110,120,390,220))
            
            ligne_0 = myfont.render("AIDE", False, (255, 100, 50))
            ligne_1 = myfont.render("Aide le chauffeur de bus :", False, (255, 100, 50))
            ligne_2 = myfont.render("  - Débarasse le de la vieille,", False, (255, 100, 50))
            ligne_3 = myfont.render("  - Place les gens correctement,", False, (255, 100, 50))
            ligne_4 = myfont.render("  - Ramasse les déchets si tu en trouves,", False, (255, 100, 50))
            ligne_5 = myfont.render("  - Installes toi au fond,", False, (255, 100, 50))
            ligne_6 = myfont.render("Tu auras peut-être une surprise", False, (255, 100, 50))
            ligne_7 = myfont.render("Tu peux déplacer certains objets en ", False, (255, 100, 50))
            ligne_8 = myfont.render("maintenant A appuyer lorsque tu es à", False, (255, 100, 50))
            ligne_9 = myfont.render("côté d'eux.", False, (255, 100, 50))
            ligne_10 = Gus_font.render("Pour revoir cette aide, approche-toi du chauffeur", False, (10, 10, 10))
            
            screen.blit(ligne_0,(130,140))             
            screen.blit(ligne_1,(155,160))            
            screen.blit(ligne_2,(155,175))            
            screen.blit(ligne_3,(155,190))            
            screen.blit(ligne_4,(155,205))            
            screen.blit(ligne_5,(155,220)) 
            screen.blit(ligne_6,(155,245)) 
            screen.blit(ligne_7,(155,265)) 
            screen.blit(ligne_8,(155,280)) 
            screen.blit(ligne_9,(155,295)) 
            screen.blit(ligne_10,(130,315)) 

            screen.blit(start_down,(420,160)) 
            
        elif 10 < seconds < 130:
            if frame_count <= 30:
                frame_count += 1
            else:
                frame_count = 0
            
            if frame_count <= 15:
                a=0
            elif frame_count > 15:
                a=1
                
            rect_gugus = gugus.get_rect() 
            tr.update_items()
            Gus.update_items(tr)
            sac.update_items(tr)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        other_s.play()
                        Gus.pause += 1    
                    if event.key == pygame.K_TAB:
                        other_s.play() 
                ############################
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:  
                        x_change = -speed_move
                        rel_x = speed_move
                        y_change = 0
                        rel_y = 0
                        step_s.play(-1)
                    elif event.key == pygame.K_RIGHT:
                        x_change = speed_move
                        rel_x = -speed_move
                        y_change = 0
                        rel_y = 0
                        step_s.play(-1)
                    elif event.key == pygame.K_UP:
                        y_change = -speed_move
                        rel_y = speed_move
                        x_change = 0
                        rel_x = 0
                        step_s.play(-1)
                    elif event.key == pygame.K_DOWN:
                        y_change = speed_move
                        rel_y = -speed_move
                        x_change = 0
                        rel_x = 0
                        step_s.play(-1)
                    if event.key == pygame.K_a and not action.click:
                        action.click = True
                        click_.play()

                        if 220 < x < 265 and -10 < y < 50 and Gus.level == 0:
                            tr.pos_bonus += 1
                    elif event.key != pygame.K_a:
                
                        action.click = False

                    for elt in liste_pnj:
                        if event.key == pygame.K_a and player.colliderect(elt):
                            elt.in_touch = True 
                        #PERSONNES
                        ###EST
                    
                    if event.key == pygame.K_RETURN:
                        enter_s.play()
                                
                    elif event.key != pygame.K_RETURN:
                    
                        action.change_level = False
                
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        x_change = 0
                        rel_x = 0
                        gugus = gugus_gauche 
                        step_s.stop()
                    if event.key == pygame.K_RIGHT:
                        x_change = 0
                        rel_x = 0
                        gugus = gugus_droite 
                        step_s.stop()
    
                    if event.key == pygame.K_UP:
                        y_change = 0
                        rel_y = 0
                        gugus = gugus_dos 
                        step_s.stop()
                        
                    if event.key == pygame.K_DOWN:
                        y_change = 0
                        rel_y = 0
                        gugus = gugus_face 
                        step_s.stop()
                        
                    for elt in liste_pnj:
                        if event.key == pygame.K_a:
                            elt.in_touch = False

                                
                ######################            
            keys=pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                gugus=gugus_walkdown[a]
            if keys[pygame.K_UP]:
                gugus=gugus_walkup[a]
            if keys[pygame.K_RIGHT]:
                gugus=gugus_walkright[a]
            if keys[pygame.K_LEFT]:
                gugus=gugus_walkleft[a]
                
            rect_gugus.topleft = (x,y)
            
            liste_mur = level_bonus(screen,0,0)
            
            x_change,y_change,rel_x,rel_y = collisions(liste_mur,rect_gugus,x_change,y_change,speed_move,rel_x,rel_y)
        
            time += 1
            
            for truc in liste_pnj:
                if rect_gugus.colliderect(truc) and truc.in_touch == False:
                    if abs(rect_gugus.bottom - truc.top) <= 10 and rel_y < 0:
                        rel_y = 0
                    if abs(rect_gugus.top - truc.bottom) <= 10 and rel_y > 0:
                        rel_y = 0
                    if abs(rect_gugus.left - truc.right) <= 10 and rel_x > 0:
                        rel_x = 0
                    if abs(rect_gugus.right - truc.left) <= 10 and rel_x < 0:
                        rel_x = 0
                        
            for elt in liste_pnj:
                if elt.in_touch:
                    liste_temp = [x for x in liste_pnj if x != elt]
                    for truc in liste_temp:
                        if elt.colliderect(truc) and truc.in_touch == False:
                            if abs(elt.bottom - truc.top) <= 10 and rel_y < 0:
                                rel_y = 0
                            if abs(elt.top - truc.bottom) <= 10 and rel_y > 0:
                                rel_y = 0
                            if abs(elt.left - truc.right) <= 10 and rel_x > 0:
                                rel_x = 0
                            if abs(elt.right - truc.left) <= 10 and rel_x < 0:
                                rel_x = 0
                                
                    for mur in liste_mur:
                        if elt.colliderect(mur):
                            if abs(elt.bottom - mur.top) <= 10 and rel_y < 0:
                                rel_y = 0
                            if abs(elt.top - mur.bottom) <= 10 and rel_y > 0:
                                rel_y = 0
                            if abs(elt.left - mur.right) <= 10 and rel_x > 0:
                                rel_x = 0
                            if abs(elt.right - mur.left) <= 10 and rel_x < 0:
                                rel_x = 0
                                
            screen_x += rel_x
            screen_y += rel_y
                        
            ##INTERACTION LVL 
            ##OBJET LVL 
            
            x -= rel_x
            y -= rel_y  
            
            if pnj.x < 106 and pnj2.x >= 152 and pnj3.x < 152 and pnj4.x >= 152 and pnj5.x >= 152:
                tr.fin_nivo_bonus = True
            
            if 220 < x < 265 and -10 < y < 50 and Gus.level == 0:
                tr.pos_bonus = zone_interaction(screen,"Qu'est-ce que c'est (A)",action,tr.pos_bonus,"5 ç!")
                tr.argent_bonus = 5
    
            if tr.fin_nivo_bonus == True and tr.argent_bonus == 5:
                Gus.level = 3
                Gus.spawn = 2
                time = 0
            ##OBJETS
            
            player.topleft = (x,y)
            for pp in liste_pnj:
                if pp.in_touch == True:
                    pp.x -= rel_x
                    pp.y -= rel_y
            
            for elt in liste_pnj:
                elt.rect.topleft = (elt.x,elt.y)
                screen.blit(elt.image,elt.rect)
            
            screen.blit(gugus, rect_gugus)

        elif seconds >= 130:
            Gus.level = 3
            Gus.spawn = 2
            time = 0
            
        titre = myfont.render("Time", False, (20, 20, 20))
        textsurface = myfont.render(str(countdown), False, (20, 20, 20))
        screen.blit(titre,(450,20))
        screen.blit(textsurface,(455,35))
        
        pv = Gus_font.render("Santé : " + str(Gus.pv), False, (78, 22, 9))
        argent = Gus_font.render("Argent : " + str(round(Gus.money,2)), False, (31, 160, 85))
        lvl = Gus_font.render("Niveau : Bonus", False, (78, 22, 9))
    
        screen.blit(pv , (10,20))
        screen.blit(lvl , (10,45))
        screen.blit(argent , (10,70))
        screen.blit(sac_tab , (10,450))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_TAB]:
            affich_sac(screen,sac)
        if (Gus.pause%2) == 1 and seconds > 10:
            pause(screen,gameExit,Gus,sac,tr)
        if Gus.pv == 0 or tr.game_over == True:
            game_over(screen)
            
        if 240 < x < 320 and 390 < y < 480:
            
            pygame.draw.rect(screen,(20,20,20),(105,115,390,230))            
            pygame.draw.rect(screen,(200,200,200),(110,120,380,220))
            
            ligne_0 = myfont.render("AIDE", False, (255, 100, 50))
            ligne_1 = myfont.render("Aide le chauffeur de bus :", False, (255, 100, 50))
            ligne_2 = myfont.render("  - Débarasse le de la vieille,", False, (255, 100, 50))
            ligne_3 = myfont.render("  - Place les gens correctement,", False, (255, 100, 50))
            ligne_4 = myfont.render("  - Ramasse les déchets si tu en trouves,", False, (255, 100, 50))
            ligne_5 = myfont.render("  - Installes toi au fond,", False, (255, 100, 50))
            ligne_6 = myfont.render("Tu auras peut-être une surprise", False, (255, 100, 50))
            ligne_7 = myfont.render("Tu peux déplacer certains objets en ", False, (255, 100, 50))
            ligne_8 = myfont.render("maintenant A appuyer lorsque tu es à", False, (255, 100, 50))
            ligne_9 = myfont.render("côté d'eux.", False, (255, 100, 50))
        
            screen.blit(ligne_0,(130,140))             
            screen.blit(ligne_1,(155,160))            
            screen.blit(ligne_2,(155,175))            
            screen.blit(ligne_3,(155,190))            
            screen.blit(ligne_4,(155,205))            
            screen.blit(ligne_5,(155,220)) 
            screen.blit(ligne_6,(155,245)) 
            screen.blit(ligne_7,(155,265)) 
            screen.blit(ligne_8,(155,280)) 
            screen.blit(ligne_9,(155,295)) 

        pygame.display.update()
        
        clock.tick(100)
        
        
def nivo3(sac,action,Gus,tr):
    pygame.init()
    speed_move = Gus.speed
    frame_count = Gus.frame
    a=0
    time = 0
    x =  (display_width-gugus_width)/2
    y = (display_height-gugus_height)/2  
    rel_x = 0 
    rel_y = 0
    x_change = 0
    y_change = 0
    gugus = gugus_face
    lassl = lassl_face
    
    screen_x = -225 + x
    screen_y = -225 + y 
    
    interact = False
    interact_bass = False
    interact_guit = False
    
    tune = Gus.money
    alcool = sac.Alcool
    preservatif = sac.Capote
    #CREATION ET CARACTERISTIQUES PNJ
    
    speed_y = 0
    speed_x = 1
    
    spawn_hookx = 7
    spawn_hooky = 608
    hook_right = hook_d[0]
    hooker = pnj(spawn_hookx,spawn_hooky,screen_x,screen_y,hook_right,"right")
    
    #INTERACTIONS
    #LVL 3 N
    
    phrases_hooker = [["Eh gamin ! ","Tu saurais pas où je","pourrais me trouver ","des capotes?"],
                      ["Tu pourrais me rendre",'un autre service ?', "Il faudrait apporter cet"," argent à mon chef.",
                       "Il est dans sa voiture"],
                      ["Oh la! J'ai personne","à voir aujourd'hui.","Aides moi à trouver","quelqu'un."],
                      ["Ah bah ça tombe pas","trop mal, j'ai un ","trou dans mon agenda","mais je dois avoir","l'accord de mon mac"],
                      ["C'est parti ! "]]
    phrases_mac = [["Yo Gus, Tu as", "vu mon employée ?"],
                   ["Merci petit. Tu","travaille bien. Je","peux te confier son","planing?"],
                   ["Oh tu lui as trouvé un","client. C'est cool,","prends ça et dis!","lui que c'est ok ","pour moi"]]
    phrases_bus = [["J'ai pas le temps","de parler!"]]
    
    #LVL 3 C
    phrases_lassl = [["Yo Gus comment","tu vas?","T'as pas vu ma","pince à cheveux?"],
                     ["T'as pas un petit","gâteau pour moi ?"],
                     ["J'adore le groupe qui","joue dans cette station","Pourquoi ils ne","jouent pas ?"],
                     ["T'as assuré avec le","groupe. Tu vas en","ville? On se reverra","peut-être là-bas." ],
                     ["Le métro va partir ! "]]
    
    phrases_contr1 = [["Eh gamin, y'a mon","collègue qu'est pas","bien. C'est pas le","jour de m'embêter!"],
                      ["T'as pas vu passer","un fraudeur ?"],
                      ["On est mal, il n'y a","plus de papier dans le","distributeur."],
                      ["Tu as besoin d'un","ticket pour passer."],
                      ["Quoi?? Il est juste là?","On va intervenir.","J'ai trouvé ça par terre","Je ne sais pas quoi",
                       "en faire."]]
    
    phrases_contr2 = [["Euh......bah... euheu","... mon... mon","....................","AAah ça va pas ouf....",
                       "me manque un truc"],
                      ["Oh merci. Ca va aller","beaucoup mieux avec","ça. Je vais pouvoir me","concentrer sur cette",
                       "histoire de fraudeur"],
                      ["Oh la la !! ","On va intervenir au ","plus vite."]]
    phrases_random1 =[["J'ai pas réussi à","prendre mon ticket."],
                      ["Merci petit, je m'en","souviendrai."]]
    phrases_billeterie = [["","C'est cassé !"],["","Tu as acheté un","ticket de métro"],["","Tu en as déjà un"]]
    
    #LVL 3 E
    phrases_bassist = [["Notre batteur a perdu","son rythme. Tu peux","nous aider?"],
                       ["Tu veux chanter avec ","nous ?"]]
    
    phrases_batteur = [["Et 1, et 2","et ... 3 je crois","et 1, 2, 3","...","C'est quoi la suite ? "],
                       ["Allez, t'es chaud ?"]]
    
    phrases_guitar = [["Wow! C'est dur de jouer","sans rythme."],
                      ["On veut bien un chanteur","si t'as rien d'autre","à faire..."]]
    
    phrases_fraudeur = [["J'aime beaucoup cette","station de métro."],
                        ["Les contrôleurs sont","vraiment stupides ici.","Ils ne m'ont même","pas contrôlé"]]
    
    #LVL 3 SE
    phrases_clodo = [["J'ai faim..."],
                     ["Tiens, j'ai trouvé", "cette pince par terre"],
                     ["Mon carton"," commence à se faire","vieux..."],
                     ["Ca c'est un beau carton","Merci petit!","T'as pas un truc à","manger ?" ],
                     ["C'est encore pas ça","dont j'ai besoin...","Tu sais pas où trouver","quelque chose qui me","fasse planer ?"],
                     ["Tu as des seringues !!??","Génial! Si tu me les","donnes, je te donnerai","des infos sur le gars là","bas"],
                     ["Merci encore.","Bah le gars sur le banc","il est juste triste gamin.","T'es pas bien malin","toi"]]
    
    phrases_depressif = [["Ohlala ça va pas","mais alors pas du ","tout..."],
                         ["J'ai besoin d'oublier","sinon je vais me jeter","sous le train..."],
                         ["Eeheh merci...","ça vôa d'ja peu mieux","ùais sque jai bzoin","c'est d'lamouuuur"]]
    
    machine_1 = [["Elle est cassée!"]]
    #OBJETS NIVEA
    #INTERACTIONS
    #ITEMS    
    
    gameExit = False
    
    while not gameExit and Gus.level >= 3 and Gus.level < 4:
        
        if not pygame.mixer.music.get_busy() and Gus.current <= len(playlist):
            Gus.current+=1
            pygame.mixer.music.load ( playlist[Gus.current])
            pygame.mixer.music.play()
        elif not pygame.mixer.music.get_busy() and Gus.current > len(playlist):
            Gus.current=0
            pygame.mixer.music.load ( playlist[Gus.current])
            pygame.mixer.music.play()        
                    
        if frame_count <= 30:
            frame_count += 1
        else:
            frame_count = 0
        
        if frame_count <= 15:
            a=0
        elif frame_count > 15:
            a=1
            
        rect_gugus = gugus.get_rect() 
        # rect_lassl = lassl.get_rect()
        tr.update_items()
        Gus.update_items(tr)
        sac.update_items(tr)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    other_s.play()
                    Gus.pause += 1    
                if event.key == pygame.K_TAB:
                    other_s.play() 
                if event.key == pygame.K_LCTRL:
                    other_s.play()

            ############################
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  
                    x_change = -speed_move
                    rel_x = speed_move
                    y_change = 0
                    rel_y = 0
                    step_s.play(-1)
                elif event.key == pygame.K_RIGHT:
                    x_change = speed_move
                    rel_x = -speed_move
                    y_change = 0
                    rel_y = 0
                    step_s.play(-1)
                elif event.key == pygame.K_UP:
                    y_change = -speed_move
                    rel_y = speed_move
                    x_change = 0
                    rel_x = 0
                    step_s.play(-1)
                elif event.key == pygame.K_DOWN:
                    y_change = speed_move
                    rel_y = -speed_move
                    x_change = 0
                    rel_x = 0
                    step_s.play(-1)
                if event.key == pygame.K_a and not action.click:
                    action.click = True
                    click_.play()
                    #PERSONNES
                    ###NORD
                    if interact and Gus.level == 3 and tr.give_condom == False and sac.Planing == 0:
                        tr.press_hook = 0
                    if interact and Gus.level == 3 and tr.give_condom == True and sac.Planing == 0:
                        tr.press_hook = 1
                        sac.Argent_mac = 50
                    if interact and Gus.level == 3 and sac.Planing == 1 and tr.ask_love == False:
                        tr.press_hook = 2
                    if interact and Gus.level == 3 and sac.Planing == 1 and tr.ask_love == True and tr.accord_mac == False:
                        tr.press_hook = 3
                    if interact and Gus.level == 3 and sac.Planing == 1 and tr.ask_love == True and tr.accord_mac == True:
                        tr.press_hook = 4
                        
                    if 826+screen_x < x < 907+screen_x and 522+screen_y < y < 576+screen_y and Gus.level == 3 and tr.give_mac == False and sac.Capote != 0:
                        tr.press_mac = 0
                    if 826+screen_x < x < 907+screen_x and 522+screen_y < y < 576+screen_y and Gus.level == 3 and tr.give_mac == True and tr.ask_love == False:
                        tr.press_mac = 1
                    if 826+screen_x < x < 907+screen_x and 522+screen_y < y < 576+screen_y and Gus.level == 3 and tr.give_mac == True and tr.ask_love == True:
                        tr.press_mac = 2
                        tr.accord_mac = True
                        
                    if 521+screen_x < x < 593+screen_x and 258+screen_y < y < 329+screen_y and Gus.level == 3:
                        tr.press_conduct = 0                        
                    
                    if 689+screen_x < x < 736+screen_x and 565+screen_y < y < 650+screen_y and Gus.level == 3:
                        tr.press_trash += 1
                    if 300+screen_x < x < 335+screen_x and 120+screen_y < y < 150+screen_y and Gus.level == 3:
                        tr.press_trash2 += 1
                        
                ##CENTRE
                    if 112+screen_x < x < 155+screen_x and 166+screen_y < y < 200+screen_y and Gus.level == 3.1 and tr.give_pince == False:
                        tr.press_lassl = 0
                    if 112+screen_x < x < 155+screen_x and 166+screen_y < y < 200+screen_y and Gus.level == 3.1 and tr.give_pince == True:
                        tr.press_lassl = 1
                    if 112+screen_x < x < 155+screen_x and 166+screen_y < y < 200+screen_y and Gus.level == 3.1 and tr.give_lassl_gateau == True and tr.unlock_minigame1 == False:
                        tr.press_lassl = 2
                    if 112+screen_x < x < 155+screen_x and 166+screen_y < y < 200+screen_y and Gus.level == 3.1 and tr.give_lassl_gateau == True and Gus.pb_music >= 3000:
                        tr.press_lassl = 3
                    if 112+screen_x < x < 155+screen_x and 166+screen_y < y < 200+screen_y and Gus.level == 3.1 and tr.ask_love == True and tr.accord_mac == True and tr.press_hook == 4:
                        tr.press_lassl = 4
                        
                    if 804+screen_x < x < 857+screen_x and 200+screen_y < y < 220+screen_y and Gus.level == 3.1 and tr.give_charism == False:
                        tr.press_contr1 = 0
                    if 804+screen_x < x < 857+screen_x and 200+screen_y < y < 220+screen_y and Gus.level == 3.1 and tr.give_charism == True and tr.repair_distri == True and sac.Ticket == 1:
                        tr.press_contr1 = 1
                    if 804+screen_x < x < 857+screen_x and 200+screen_y < y < 220+screen_y and Gus.level == 3.1 and tr.give_charism == True and tr.repair_distri == False:
                        tr.press_contr1 = 2                        
                    if 804+screen_x < x < 857+screen_x and 200+screen_y < y < 220+screen_y and Gus.level == 3.1 and tr.give_charism == True and tr.repair_distri == True and sac.Ticket == 0:
                        tr.press_contr1 = 3
                    if 804+screen_x < x < 857+screen_x and 200+screen_y < y < 220+screen_y and Gus.level == 3.1 and tr.denonce_fraude == True :
                        tr.press_contr1 = 4
                        sac.Rythme = 1
                    
                    if 828+screen_x < x < 882+screen_x and 519+screen_y < y < 558+screen_y and Gus.level == 3.1 and tr.give_charism == False:
                        tr.press_contr2 = 0
                    if 828+screen_x < x < 882+screen_x and 519+screen_y < y < 558+screen_y and Gus.level == 3.1 and tr.give_charism == True:
                        tr.press_contr2 = 1
                    if 828+screen_x < x < 882+screen_x and 519+screen_y < y < 558+screen_y and Gus.level == 3.1 and tr.denonce_fraude == True:
                        tr.press_contr2 = 2
                        
                    if 176+screen_x < x < 241+screen_x and 520+screen_y < y < 557+screen_y and Gus.level == 3.1 and tr.give_ticket == False:
                        tr.press_random_ticket = 0
                    if 176+screen_x < x < 241+screen_x and 520+screen_y < y < 557+screen_y and Gus.level == 3.1 and tr.give_ticket == True:
                        tr.press_random_ticket = 1

                    if 700+screen_x < x < 745+screen_x and 75+screen_y < y < 100+screen_y and Gus.level == 3.1:
                        tr.press_trash_metro1 += 1                        
                    if 900+screen_x < x < 964+screen_x and 589+screen_y < y < 633+screen_y and Gus.level == 3.1:
                        tr.press_trash_metro2 += 1
                        
                    if 235+screen_x < x < 668+screen_x and 570+screen_y < y < 633+screen_y and Gus.level == 3.1:
                        tr.press_billeterie = 0
                        
                ##EST
                    if interact and Gus.level == 3.2 and tr.unlock_minigame1 == False:
                        tr.press_batteur = 0
                    if interact and Gus.level == 3.2 and tr.unlock_minigame1 == True:
                        tr.press_batteur = 1

                    if interact_bass and Gus.level == 3.2 and tr.unlock_minigame1 == False:
                        tr.press_bassist = 0
                    if interact_bass and Gus.level == 3.2 and tr.unlock_minigame1 == True:
                        tr.press_bassist = 1

                    if interact_guit and Gus.level == 3.2 and tr.unlock_minigame1 ==False:
                        tr.press_guitar = 0
                    if interact_guit and Gus.level == 3.2 and tr.unlock_minigame1 ==True:
                        tr.press_guitar = 1

                    if 312+screen_x < x < 365+screen_x and 530+screen_y < y < 590+screen_y and Gus.level == 3.2:
                        tr.press_fraudeur = 0
                    if 312+screen_x < x < 365+screen_x and 530+screen_y < y < 590+screen_y and Gus.level == 3.2 and tr.give_lassl_gateau == True :
                        tr.press_fraudeur = 1                    
                        
                    if 695+screen_x < x < 725+screen_x and 80+screen_y < y < 100+screen_y and Gus.level == 3.2:
                        tr.press_trash3 += 1
                        
                ##SUD EST
                    if 33+screen_x < x < 210+screen_x and 13+screen_y < y < 100+screen_y and Gus.level == 3.3 and tr.give_dwich == False:
                        tr.press_clodo = 0
                    if 33+screen_x < x < 210+screen_x and 13+screen_y < y < 100+screen_y and Gus.level == 3.3 and tr.give_dwich == True and tr.give_pince ==False:
                        tr.press_clodo = 1
                        sac.Pince = 1
                    if 33+screen_x < x < 210+screen_x and 13+screen_y < y < 100+screen_y and Gus.level == 3.3 and tr.give_dwich == True and tr.give_pince == True:
                        tr.press_clodo = 2
                    if 33+screen_x < x < 210+screen_x and 13+screen_y < y < 100+screen_y and Gus.level == 3.3 and tr.give_carton == True and tr.gateau_clodo == False:
                        tr.press_clodo = 3
                    if 33+screen_x < x < 210+screen_x and 13+screen_y < y < 100+screen_y and Gus.level == 3.3 and tr.gateau_clodo == True and tr.propose_seringue == False:
                        tr.press_clodo = 4
                    if 33+screen_x < x < 210+screen_x and 13+screen_y < y < 100+screen_y and Gus.level == 3.3 and tr.propose_seringue == True and tr.give_seringue == False:
                        tr.press_clodo = 5
                    if 33+screen_x < x < 210+screen_x and 13+screen_y < y < 100+screen_y and Gus.level == 3.3 and tr.propose_seringue == True and tr.give_seringue == True:
                        tr.press_clodo = 6
                        
                    if 134+screen_x < x < 195+screen_x and 380+screen_y < y < 412+screen_y and Gus.level == 3.3 and tr.give_seringue == False:
                        tr.depressif = 0
                    if 134+screen_x < x < 195+screen_x and 380+screen_y < y < 412+screen_y and Gus.level == 3.3 and tr.give_seringue ==True and tr.give_alcool == False:
                        tr.depressif = 1
                    if 134+screen_x < x < 195+screen_x and 380+screen_y < y < 412+screen_y and Gus.level == 3.3 and tr.give_seringue ==True and tr.give_alcool == True:
                        tr.depressif = 2
                        tr.ask_love = True
                    
                    if 590+screen_x < x < 690+screen_x and 75+screen_y < y < 109+screen_y and Gus.level == 3.3:
                        tr.press_machine1 = 0

                        
                elif event.key != pygame.K_a:
                
                    action.click = False
                
                if event.key == pygame.K_RETURN:
                    enter_s.play()
                    if interact and Gus.level == 3 and tr.press_hook == 0 and sac.Capote != 0:
                        tr.capote_nn = 0 
                        tr.capote_buro = 0 
                        tr.capote_entree = 0 
                        tr.capoteNord = 0
                        tr.capote_3 = 0
                        tr.give_condom = True
                    if 826+screen_x < x < 907+screen_x and 522+screen_y < y < 576+screen_y and Gus.level == 3 and sac.Argent_mac == 50:
                        tr.give_mac = True
                    if 826+screen_x < x < 907+screen_x and 522+screen_y < y < 576+screen_y and Gus.level == 3 and sac.Argent_mac == 0 and tr.press_mac == 1 and sac.Planing == 0:
                        tr.take_plan = True

                    if 112+screen_x < x < 155+screen_x and 166+screen_y < y < 200+screen_y and Gus.level == 3.1 and tr.give_pince == False and sac.Pince == 1:
                        tr.give_pince = True
                        sac.Pince = 0
                    if 112+screen_x < x < 155+screen_x and 166+screen_y < y < 200+screen_y and Gus.level == 3.1 and tr.give_pince == True and sac.Gateau != 0:
                        tr.give_lassl_gateau = True
                        tr.gateau_offert = -1
                        
                    if 235+screen_x < x < 668+screen_x and 570+screen_y < y < 633+screen_y and Gus.level == 3.1 and sac.Papier > 0:
                        tr.repair_distri = True
                        
                    if 804+screen_x < x < 857+screen_x and 200+screen_y < y < 220+screen_y and Gus.level == 3.1 and tr.find_fraudeur == True:
                        tr.denonce_fraude = True
                    if 828+screen_x < x < 882+screen_x and 519+screen_y < y < 558+screen_y and Gus.level == 3.1 and tr.give_charism == False and sac.Charisme == 1:
                        tr.give_charism = True
                        sac.Charisme = 0
                        
                    if 176+screen_x < x < 241+screen_x and 520+screen_y < y < 557+screen_y and Gus.level == 3.1 and sac.Ticket == 1 and tr.give_ticket == False:
                        sac.Ticket = 0
                        tr.achat_ticket = False
                        tr.give_ticket = True
                        
                    if 235+screen_x < x < 668+screen_x and 570+screen_y < y < 633+screen_y and Gus.level == 3.1 and tr.repair_distri == True and sac.Papier == 0 and tr.give_ticket == False:
                        sac.Ticket = 1
                        tr.achat_ticket = True
                        tr.argent_ticket_metro = -2
                    if 235+screen_x < x < 668+screen_x and 570+screen_y < y < 633+screen_y and Gus.level == 3.1 and tr.repair_distri == True and sac.Papier == 0 and tr.give_ticket == True:
                        sac.Ticket = 1
                        tr.achat_ticket = True
                        tr.argent_ticket_metro = -4

                    if 312+screen_x < x < 365+screen_x and 530+screen_y < y < 590+screen_y and Gus.level == 3.2 and tr.give_lassl_gateau == True and tr.find_fraudeur == False:
                        tr.find_fraudeur = True
                        
                    if interact and Gus.level == 3.2 and sac.Rythme == 1:
                        sac.Rythme = 0
                        tr.rythm = 1
                        tr.unlock_minigame1 = True
                        
                    if (interact or interact_bass or interact_guit) and Gus.level == 3.2 and tr.unlock_minigame1 == True:
                        Gus.level = 99
                        
                    if 700+screen_x < x < 800+screen_x and 80+screen_y < y < 125+screen_y and Gus.level == 3.3 :
                        tr.press_machine2 += 1
                        
                    if 33+screen_x < x < 210+screen_x and 13+screen_y < y < 100+screen_y and Gus.level == 3.3 and tr.give_dwich == False and sac.Sandwich != 0:
                        tr.give_dwich = True
                    if 33+screen_x < x < 210+screen_x and 13+screen_y < y < 100+screen_y and Gus.level == 3.3 and tr.give_carton == False and sac.Carton != 0:
                        tr.give_carton = True
                    if 33+screen_x < x < 210+screen_x and 13+screen_y < y < 100+screen_y and Gus.level == 3.3 and tr.give_carton == True and sac.Carton == 0 and sac.Gateau != 0:
                        tr.gateau_clodo = True 
                        tr.gateau_offert = -2
                    if 33+screen_x < x < 210+screen_x and 13+screen_y < y < 100+screen_y and Gus.level == 3.3 and tr.press_clodo == 4 and sac.Seringue != 0 :
                        tr.propose_seringue = True        
                    if 33+screen_x < x < 210+screen_x and 13+screen_y < y < 100+screen_y and Gus.level == 3.3 and tr.propose_seringue == True and sac.Seringue != 0  and tr.press_clodo == 5:
                        tr.give_seringue = True  

                    if 134+screen_x < x < 195+screen_x and 380+screen_y < y < 412+screen_y and Gus.level == 3.3 and tr.depressif == 1:
                        tr.give_alcool = True
                        
                    if 488+screen_y < y < 536+screen_y and tr.press_hook >= 4:
                        Gus.level = 4
                        Gus.spawn = 1
                        
                elif event.key != pygame.K_RETURN:
                
                    action.change_level = False
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_change = 0
                    rel_x = 0
                    gugus = gugus_gauche 
                    # lassl = lassl_gauche
                    step_s.stop()
                if event.key == pygame.K_RIGHT:
                    x_change = 0
                    rel_x = 0
                    gugus = gugus_droite
                    # lassl = lassl_droite
                    step_s.stop()

                if event.key == pygame.K_UP:
                    y_change = 0
                    rel_y = 0
                    gugus = gugus_dos 
                    # lassl = lassl_dos
                    step_s.stop()
                    
                if event.key == pygame.K_DOWN:
                    y_change = 0
                    rel_y = 0
                    gugus = gugus_face 
                    # lassl = lassl_face
                    step_s.stop()
                    
            ######################            
        keys=pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            gugus=gugus_walkdown[a]
            # lassl=lassl_walkd[a]
        if keys[pygame.K_UP]:
            gugus=gugus_walkup[a]
            # lassl=lassl_walku[a]
        if keys[pygame.K_RIGHT]:
            gugus=gugus_walkright[a]
            # lassl=lassl_walkr[a]            
        if keys[pygame.K_LEFT]:
            gugus=gugus_walkleft[a]
            # lassl=lassl_walkl[a]
            
        rect_gugus.topleft = (x,y)
        # rect_lassl.topleft = (x,y)
                        
        if Gus.level == 3:
    
            if Gus.spawn == 1 and time < 2:
                screen_x,screen_y,x,y = spawn_level(x,y,823,514)
            elif Gus.spawn == 2 and time < 2:
                screen_x,screen_y,x,y = spawn_level(x,y,401,122)
            elif Gus.spawn == 3 and time < 2:
                screen_x,screen_y,x,y = spawn_level(x,y,401,707-gugus_height)
                
            time += 1
            liste_mur = level_3N(screen,screen_x,screen_y)
               
            if hooker.movement == True:
                hook_left = hook_l[a]            
                hook_right = hook_d[a]
            elif hooker.movement == False:
                hook_left = hook_l[2]            
                hook_right = hook_d[2]
                
            if hooker.side == "left":
                hooker = pnj(spawn_hookx,spawn_hooky,screen_x,screen_y,hook_left,'left')
            elif hooker.side == "right":
                hooker = pnj(spawn_hookx,spawn_hooky,screen_x,screen_y,hook_right,'right')
            
            speed_x,speed_y = hooker.collisions_pnj(liste_mur,speed_x,speed_y,hook_right,hook_left,0)
            spawn_hookx,spawn_hooky = hooker.move(spawn_hookx,spawn_hooky,speed_x,speed_y)
            
            # if Gus.perso == "gus":
            x_change,y_change,rel_x,rel_y = collisions(liste_mur,rect_gugus,x_change,y_change,speed_move,rel_x,rel_y)
            # if Gus.perso == "lassl":
            #     x_change,y_change,rel_x,rel_y = collisions(liste_mur,rect_lassl,x_change,y_change,speed_move,rel_x,rel_y)

            if hooker.rect.colliderect(rect_gugus) and hooker.side == "left":
                if abs (hooker.rect.left - rect_gugus.right) <= 10:
                    speed_x *= 0
                    speed_y *= -1
                    hooker.movement = False
                    interact = True

            if hooker.rect.colliderect(rect_gugus) and hooker.side == "right":
                if abs (hooker.rect.right - rect_gugus.left) <= 10:
                    speed_x = 0
                    speed_y *= -1  
                    hooker.movement = False
                    interact = True
                    
            if not hooker.rect.colliderect(rect_gugus) and hooker.side == "left":
                if abs (hooker.rect.left - rect_gugus.right) <= 10:
                    speed_x = -1
                    speed_y *= -1
                    hooker.side = "left"
                    hooker.movement = True

            if not hooker.rect.colliderect(rect_gugus) and hooker.side == "right":
                if abs (hooker.rect.right - rect_gugus.left) <= 10:
                    speed_x = 1
                    speed_y *= -1
                    hooker.side = "right" 
                    hooker.movement = True
                                        

            if rect_gugus.colliderect(hooker.rect):
                if abs (hooker.rect.left - rect_gugus.right) <= 10 and x_change > 0:
                    x_change = 0
                    rel_x = 0
            if rect_gugus.colliderect(hooker.rect):
                if abs (hooker.rect.right - rect_gugus.left) <= 10 and x_change < 0:
                    x_change = 0
                    rel_x = 0     
            if rect_gugus.colliderect(hooker.rect):
                if abs (hooker.rect.bottom - rect_gugus.top) <= 10 and y_change < 0:
                    y_change = 0
                    rel_y = 0    
            if rect_gugus.colliderect(hooker.rect):
                if abs (hooker.rect.top - rect_gugus.bottom) <= 10 and y_change > 0:
                    y_change = 0
                    rel_y = 0   
            if not rect_gugus.colliderect(hooker.rect):
                interact = False 
                
            screen_x += rel_x
            screen_y += rel_y
            
            screen.blit(hooker.image, hooker.rect)
        
            if y > 460:
                Gus.level = 3.1
                Gus.spawn = 1
                time = 0

            
        elif Gus.level == 3.1:
            
            if Gus.spawn == 1 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,401,50)

            if Gus.spawn == 2 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,1001-gugus_width,339)
                        
            time += 1
            
            if sac.Ticket == 0:
                liste_mur = level_3C(screen,screen_x,screen_y)
            elif sac.Ticket != 0:
                liste_mur = level_3Copen(screen,screen_x,screen_y)
        
            # if Gus.perso == "gus":
            x_change,y_change,rel_x,rel_y = collisions(liste_mur,rect_gugus,x_change,y_change,speed_move,rel_x,rel_y)
            # if Gus.perso == "lassl":
            #     x_change,y_change,rel_x,rel_y = collisions(liste_mur,rect_lassl,x_change,y_change,speed_move,rel_x,rel_y)

            screen_x += rel_x
            screen_y += rel_y
            
            if x > 470 and 320+screen_y < y < 395+screen_y:
                Gus.level = 3.2
                Gus.spawn = 1
                time = 0
            if y < 0:
                Gus.level = 3
                Gus.spawn = 3
                time = 0  
                
                
    
        elif Gus.level == 3.2:
            
            if Gus.spawn == 1 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,31,338)

            if Gus.spawn == 2 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,901,339)

            time += 1
            
            liste_mur = level_3E(screen,screen_x,screen_y)
        
            # if Gus.perso == "gus":
            x_change,y_change,rel_x,rel_y = collisions(liste_mur,rect_gugus,x_change,y_change,speed_move,rel_x,rel_y)
            # if Gus.perso == "lassl":
            #     x_change,y_change,rel_x,rel_y = collisions(liste_mur,rect_lassl,x_change,y_change,speed_move,rel_x,rel_y)
            if Gus.spawn == 3 :
                if time < 200 and Gus.try_music == 2:
                    screen_x,screen_y,x,y = spawn_level(x,y,229,228)
                    textsurface = myfont.render("Tu récupères un carton", False, (0, 0, 0))
                    screen.blit(textsurface,(x,y-60))
                if time < 2 and Gus.try_music > 2:
                    screen_x,screen_y,x,y = spawn_level(x,y,229,228)
                    
            if tr.rythm == 0:
                pnj_batteur = batteur[2]
                pnj_bass = bassist[2]
                pnj_guit = guitar[2]

            elif tr.rythm == 1:                
                pnj_batteur = batteur[a]
                pnj_bass = bassist[a]
                pnj_guit = guitar[a]
            
            rect_batteur = pnj_batteur.get_rect()
            rect_batteur.topleft=(320+screen_x,20+screen_y)
            
            rect_bass = pnj_bass.get_rect()
            rect_bass.topleft=(250+screen_x,50+screen_y)
            
            rect_guit = pnj_guit.get_rect()
            rect_guit.topleft=(400+screen_x,80+screen_y)
            
            if rect_gugus.colliderect(rect_batteur) and x_change > 0:
                if abs (rect_batteur.left - rect_gugus.right) <= 10:
                    x_change = 0
                    rel_x = 0
            if rect_gugus.colliderect(rect_batteur) and x_change < 0:
                if abs (rect_batteur.right - rect_gugus.left) <= 10:
                    x_change = 0
                    rel_x = 0   
            if rect_gugus.colliderect(rect_batteur) and y_change < 0:
                if abs (rect_batteur.bottom - rect_gugus.top) <= 10:
                    y_change = 0
                    rel_y = 0
                    interact = True                    
            if rect_gugus.colliderect(rect_batteur) and y_change > 0:
                if abs (rect_batteur.top - rect_gugus.bottom) <= 10:
                    y_change = 0
                    rel_y = 0  
            if not rect_gugus.colliderect(rect_batteur):
                interact = False 
                
            if rect_gugus.colliderect(rect_bass) and x_change > 0:
                if abs (rect_bass.left - rect_gugus.right) <= 10:
                    x_change = 0
                    rel_x = 0
            if rect_gugus.colliderect(rect_bass) and x_change < 0:
                if abs (rect_bass.right - rect_gugus.left) <= 10:
                    x_change = 0
                    rel_x = 0   
            if rect_gugus.colliderect(rect_bass) and y_change < 0:
                if abs (rect_bass.bottom - rect_gugus.top) <= 10:
                    y_change = 0
                    rel_y = 0
                    interact_bass = True                    
            if rect_gugus.colliderect(rect_bass) and y_change > 0:
                if abs (rect_bass.top - rect_gugus.bottom) <= 10:
                    y_change = 0
                    rel_y = 0  
            if not rect_gugus.colliderect(rect_bass):
                interact_bass = False 
     
            
            if rect_gugus.colliderect(rect_guit) and x_change > 0:
                if abs (rect_guit.left - rect_gugus.right) <= 10:
                    x_change = 0
                    rel_x = 0
            if rect_gugus.colliderect(rect_guit) and x_change < 0:
                if abs (rect_guit.right - rect_gugus.left) <= 10:
                    x_change = 0
                    rel_x = 0   
            if rect_gugus.colliderect(rect_guit) and y_change < 0:
                if abs (rect_guit.bottom - rect_gugus.top) <= 10:
                    y_change = 0
                    rel_y = 0
                    interact_guit = True                    
            if rect_gugus.colliderect(rect_guit) and y_change > 0:
                if abs (rect_guit.top - rect_gugus.bottom) <= 10:
                    y_change = 0
                    rel_y = 0  
            if not rect_gugus.colliderect(rect_guit):
                interact_guit = False 
                
            screen_x += rel_x
            screen_y += rel_y
        
            screen.blit(pnj_batteur, rect_batteur)
            screen.blit(pnj_bass, rect_bass)
            screen.blit(pnj_guit, rect_guit)
            
            if x > 350 and y > 230:
                Gus.level = 3.3
                Gus.spawn = 1
                time = 0
            if x < 0 and 320+screen_y < y < 395+screen_y:
                Gus.level = 3.1
                Gus.spawn = 2
                time = 0   

        elif Gus.level == 3.3:
            
            if Gus.spawn == 1 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,901,142)
                        
            time += 1
            
            if tr.press_hook < 4:
                liste_mur = level_3SE(screen,screen_x,screen_y)
            elif tr.press_hook >= 4:
                liste_mur = level_3SEmetro(screen,screen_x,screen_y)
        
            # if Gus.perso == "gus":
            x_change,y_change,rel_x,rel_y = collisions(liste_mur,rect_gugus,x_change,y_change,speed_move,rel_x,rel_y)
            # if Gus.perso == "lassl":
            #     x_change,y_change,rel_x,rel_y = collisions(liste_mur,rect_lassl,x_change,y_change,speed_move,rel_x,rel_y)

            screen_x += rel_x
            screen_y += rel_y
            
            if x > 350 and y < 40:
                Gus.level = 3.2
                Gus.spawn = 2
                time = 0
          
        ##INTERACTION LVL 3
        if tr.give_mac == True:
            sac.Argent_mac = 0
        if tr.take_plan == True:
            sac.Planing = 1
        if tr.press_contr2 != -1:
            tr.talk_contr2 = True
        if tr.repair_distri == True:
            sac.Papier = 0
        if tr.give_dwich == True:
            sac.Sandwich = 0
        if tr.give_carton == True:
            sac.Carton = 0
        if tr.give_seringue == True:
            sac.Seringue = 0
        if tr.give_alcool == True:
            sac.Alcool = 0
        if tr.accord_mac == True:
            tr.argent_rdv_pute = 5
            
        if tr.press_machine2 != 0:
            sac.Gateau = tr.press_machine2 + tr.gateau_offert
            tr.achat_gateau = (tr.press_machine2)* - 2
    
        ##NORD
        if interact and Gus.level == 3:
            zone_dialogue(screen,"Parler à la dame (A)",action,phrases_hooker[tr.press_hook],tr.press_hook,5)
            
            if sac.Capote > 0 and tr.press_hook == 0:
                textsurface = myfont.render("Donner des capotes", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40)) 
                
        elif 826+screen_x < x < 907+screen_x and 522+screen_y < y < 576+screen_y and Gus.level == 3 and sac.Argent_mac == 0:
            zone_dialogue(screen,"Parler au dealer (A)",action,phrases_mac[tr.press_mac],tr.press_mac,5)
            if tr.press_mac == 1 and sac.Planing == 0:
                textsurface = myfont.render("Prendre le planing", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40))
                
        elif 826+screen_x < x < 907+screen_x and 522+screen_y < y < 576+screen_y and Gus.level == 3 and sac.Argent_mac > 0 and tr.give_mac == False:
            zone_dialogue(screen,"Parler au dealer (A)",action,phrases_mac[tr.press_mac],tr.press_mac,5)   
            if sac.Argent_mac > 0 and tr.press_mac ==0:
                textsurface = myfont.render("Donner l'argent", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40)) 
                
        elif 521+screen_x < x < 593+screen_x and 258+screen_y < y < 329+screen_y and Gus.level == 3:
            zone_dialogue(screen,"Parler au chauffeur (A)",action,phrases_bus[tr.press_conduct],tr.press_conduct,2)
            
        elif 689+screen_x < x < 736+screen_x and 565+screen_y < y < 650+screen_y and Gus.level == 3 and tr.talk_contr2 == True and tr.give_charism == False:
            tr.press_trash = zone_interaction(screen,"Fouiller la poubelle (A)",action,tr.press_trash,"du charisme!")
            sac.Charisme = 1
        elif 300+screen_x < x < 335+screen_x and 120+screen_y < y < 150+screen_y and Gus.level == 3:
            tr.press_trash2 = zone_interaction(screen,"Fouiller la poubelle (A)",action,tr.press_trash2,"un drôle de truc!")
            tr.capote_3 = 1
            
        ##CENTRE
        elif 112+screen_x < x < 155+screen_x and 166+screen_y < y < 200+screen_y and Gus.level == 3.1:
            zone_dialogue(screen,"Parler à celle-là (A)",action,phrases_lassl[tr.press_lassl],tr.press_lassl,5) 
            if sac.Pince == 1 and tr.give_pince == False:
                textsurface = myfont.render("Donner la pince", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40))
            if sac.Gateau != 0 and tr.give_pince == True and tr.give_lassl_gateau == False:
                textsurface = myfont.render("Donner un gâteau", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40))
                
        elif 804+screen_x < x < 857+screen_x and 200+screen_y < y < 220+screen_y and Gus.level == 3.1:
            zone_dialogue(screen,"Parler au contrôleur (A)",action,phrases_contr1[tr.press_contr1],tr.press_contr1,5)  
            if tr.find_fraudeur == True and sac.Rythme == 0:
                textsurface = myfont.render("Dénoncer le fraudeur", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40))
                
        elif 828+screen_x < x < 882+screen_x and 519+screen_y < y < 558+screen_y and Gus.level == 3.1:
            zone_dialogue(screen,"Parler au contrôleur (A)",action,phrases_contr2[tr.press_contr2],tr.press_contr2,5)
            if tr.give_charism == False and sac.Charisme == 1:
                textsurface = myfont.render("Rendre son charisme", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40))
            if tr.find_fraudeur == True and tr.press_contr2 != 2:
                textsurface = myfont.render("Dénoncer le fraudeur", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40))
                
        elif 176+screen_x < x < 241+screen_x and 520+screen_y < y < 557+screen_y and Gus.level == 3.1:
            zone_dialogue(screen,"Parler à ce type (A)",action,phrases_random1[tr.press_random_ticket],tr.press_random_ticket,5)
            if tr.achat_ticket == True and sac.Ticket == 1 and tr.give_ticket == False:
                textsurface = myfont.render("Donner un ticket", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40))

        elif 700+screen_x < x < 745+screen_x and 75+screen_y < y < 100+screen_y and Gus.level == 3.1:
            tr.press_trash_metro1 = zone_interaction(screen,"Fouiller la poubelle (A)",action,tr.press_trash_metro1,"des clopes!")
            tr.clope_metro = 3           
        elif 900+screen_x < x < 964+screen_x and 589+screen_y < y < 633+screen_y and Gus.level == 3.1:
            tr.press_trash_metro2 = zone_interaction(screen,"Fouiller la poubelle (A)",action,tr.press_trash_metro2,"du papier à ticket!")
            sac.Papier = 10
            
        elif 235+screen_x < x < 668+screen_x and 570+screen_y < y < 633+screen_y and Gus.level == 3.1 and tr.repair_distri == False:
            zone_dialogue(screen,"Acheter un ticket (A)",action,phrases_billeterie[tr.press_billeterie],tr.press_billeterie,5)
            
            if sac.Papier > 0 :
                textsurface = myfont.render("Réparer la machine", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40)) 
                
        elif 235+screen_x < x < 668+screen_x and 570+screen_y < y < 633+screen_y and Gus.level == 3.1 and tr.repair_distri == True:
            if tr.achat_ticket == False:
                textsurface = myfont.render("Acheter un ticket", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40))
            if tr.achat_ticket == True:
                textsurface = myfont.render("Tu as ton ticket", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
        ##EST
        elif interact and Gus.level == 3.2:
            zone_dialogue(screen,"Parler au batteur (A)",action,phrases_batteur[tr.press_batteur],tr.press_batteur,5)
            if sac.Rythme == 1 and tr.score_music == 0:
                textsurface = myfont.render("Donner le rythme", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40))                
            if tr.unlock_minigame1 == True :
                textsurface = myfont.render("Chanter", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40))                  
            
        elif interact_bass and Gus.level == 3.2:
            zone_dialogue(screen,"Parler au bassiste (A)",action,phrases_bassist[tr.press_bassist],tr.press_bassist,5) 
            if tr.unlock_minigame1 == True :
                textsurface = myfont.render("Chanter", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40))  
                
        elif interact_guit and Gus.level == 3.2:
            zone_dialogue(screen,"Parler au guitariste (A)",action,phrases_guitar[tr.press_guitar],tr.press_guitar,5) 
            if tr.unlock_minigame1 == True :
                textsurface = myfont.render("Chanter", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40))  
                
        elif 312+screen_x < x < 365+screen_x and 530+screen_y < y < 590+screen_y and Gus.level == 3.2:
            zone_dialogue(screen,"Parler au monsieur (A)",action,phrases_fraudeur[tr.press_fraudeur],tr.press_fraudeur,5)
            if tr.give_lassl_gateau == True and tr.find_fraudeur == False:
                textsurface = myfont.render("Demander s'il a son ticket", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40))
            if tr.give_lassl_gateau == True and tr.find_fraudeur == True:
                textsurface = myfont.render("Tu as trouvé le", False, (0, 0, 0))
                textsurface2 = myfont.render("fraudeur.", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40))
                
        elif 695+screen_x < x < 725+screen_x and 80+screen_y < y < 100+screen_y and Gus.level == 3.2:
            tr.press_trash3 = zone_interaction(screen,"Fouiller la poubelle (A)",action,tr.press_trash3,"vieux sandwich!")       
            sac.Sandwich = 1
            
        ##SUD EST
        elif 33+screen_x < x < 210+screen_x and 13+screen_y < y < 100+screen_y and Gus.level == 3.3:
            zone_dialogue(screen,"Parler au clodo (A)",action,phrases_clodo[tr.press_clodo],tr.press_clodo,6)
            if sac.Sandwich == 1 and tr.give_dwich == False:
                textsurface = myfont.render("Donner le sandwich", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40)) 
            if sac.Carton == 1 and tr.give_carton == False:
                textsurface = myfont.render("Donner le carton", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40)) 
            if sac.Gateau != 0 and tr.gateau_clodo == False and tr.give_carton == True:
                textsurface = myfont.render("Donner un gateau", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40)) 
            if tr.press_clodo == 4 and sac.Seringue != 0 and tr.propose_seringue == False:
                textsurface = myfont.render("Proposer les seringues", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40)) 
            if tr.press_clodo == 5 and sac.Seringue != 0 and tr.propose_seringue == True:
                textsurface = myfont.render("Donner les seringues", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40)) 
                
        elif 134+screen_x < x < 195+screen_x and 380+screen_y < y < 412+screen_y and Gus.level == 3.3:
            zone_dialogue(screen,"Parler au monsieur (A)",action,phrases_depressif[tr.depressif],tr.depressif,5)
            if tr.depressif == 1 and sac.Alcool != 0 :
                textsurface = myfont.render("Proposer de l'alcool", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40))
                
        elif 590+screen_x < x < 690+screen_x and 75+screen_y < y < 109+screen_y and Gus.level == 3.3:
            zone_dialogue(screen,"Acheter un truc (A)",action,machine_1[tr.press_machine1],tr.press_machine1,5)
            
        elif 700+screen_x < x < 800+screen_x and 80+screen_y < y < 125+screen_y and Gus.level == 3.3 :
            textsurface = myfont.render("Acheter un truc", False, (110, 110, 110))
            textsurface2 = myfont.render("       ENTER.", False, (110, 110, 110))
            screen.blit(fond_text,(260,380))
            screen.blit(textsurface,(280,400))
            screen.blit(textsurface2,(280,420))   
        
        elif 488+screen_y < y < 536+screen_y and Gus.level == 3.3 and tr.press_hook >= 4:
            textsurface = myfont.render("Prendre le métro", False, (110, 110, 110))
            textsurface2 = myfont.render("       ENTER.", False, (110, 110, 110))
            screen.blit(fond_text,(260,380))
            screen.blit(textsurface,(280,400))
            screen.blit(textsurface2,(280,420))   
            
        elif 216+screen_x < x < 400+screen_x and 0+screen_y < y < 50+screen_y and Gus.level == 3.3 :
            textsurface = myfont.render("C'est le plan de", False, (110, 110, 110))
            textsurface2 = myfont.render("la ville.", False, (110, 110, 110))
            screen.blit(fond_text,(260,380))
            screen.blit(textsurface,(280,400))
            screen.blit(textsurface2,(280,420))    
            
        if screen_x >= 0 and rel_x > 0:
            screen_x = 0
            x -= rel_x
        elif screen_x <= display_width - 1000 and rel_x < 0 :
            screen_x = display_width - 1000
            x -= rel_x
        if screen_y >= 0 and rel_y > 0 :
            screen_y = 0
            y  -= rel_y
        elif screen_y <= display_height - 707 and rel_y < 0:
            screen_y = display_height - 707 
            y -= rel_y
            
        if x < (display_width-gugus_width)/2 and rel_x < 0:
            screen_x = 0
            x -= rel_x
        elif x > (display_width-gugus_width)/2 and rel_x > 0:
            screen_x = display_width - 1000
            x -= rel_x
            
        if y < (display_height-gugus_height)/2 and rel_y < 0:
            screen_y = 0
            y -= rel_y
        elif y > (display_height-gugus_height)/2 and rel_y > 0:
            screen_y = display_height - 707 
            y -= rel_y
        
        ##OBJETS
        
        # if Gus.perso == "gus":
        screen.blit(gugus, rect_gugus)
        # elif Gus.perso == "lassl":
        #     screen.blit(lassl, rect_lassl)
        
        pv = Gus_font.render("Santé : " + str(Gus.pv), False, (78, 22, 9))
        argent = Gus_font.render("Argent : " + str(round(Gus.money,2)), False, (31, 160, 85))
        lvl = Gus_font.render("Niveau : " + str(int(Gus.level)), False, (78, 22, 9))
    
        screen.blit(pv , (10,20))
        screen.blit(lvl , (10,45))
        screen.blit(argent , (10,70))
        screen.blit(sac_tab , (10,450))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_TAB]:
            affich_sac(screen,sac)
            
        # if keys[pygame.K_LCTRL]:
        #     if Gus.perso == "gus":
        #         Gus.perso = "lassl"
        #     elif Gus.perso != "gus":
        #         Gus.perso = "gus"
        
        if (Gus.pause%2) == 1:
            pause(screen,gameExit,Gus,sac,tr)
        if Gus.pv == 0 or tr.game_over == True:
            game_over(screen)

        pygame.display.update()
        
        clock.tick(100)
        
def end_game(score,replay = False):
    final_font = pygame.font.SysFont('Corbel Bold', 50)
    screen.fill((250,250,250))
    
    titer = final_font.render("Score :", False, (21, 21, 21))
        
    final_score = final_font.render(score, False, (21, 21, 21))
    
    screen.blit(titer,(100,200))
    screen.blit(final_score,(250,200))
    titr = final_font.render("Retour au jeu : ENTER", False, (21, 21, 21))
    
    screen.blit(titr,(100,300))
    
    if replay == True :
        rejoue = final_font.render("Rejouer au jeu : SPACE", False, (21, 21, 21))
        
        screen.blit(rejoue,(100,400))
    
    
def music_level(sac,action,Gus,tr):
    gameExit=False
    
    fond=pygame.image.load('Level/fond_minimusic.jpg').convert()
    fond_width,fond_height = fond.get_rect().size
    
    frame_count = Gus.frame
    a=0
    time = 0
    
    start_ticks=pygame.time.get_ticks()
    score = 0
    
    total_score = 0
    countdown = 63
    
    x = 140
    y=400
    
    pressed = False
    wrong = False
    time = 0
    done = 0

    start_y = 0
    
    left = pygame.image.load("bank/image/left_arrow.png")
    right = pygame.image.load("bank/image/right_arrow.png")
    up = pygame.image.load("bank/image/up_arrow.png")
    down = pygame.image.load("bank/image/down_arrow.png")
    
    left_tr = left.get_rect()
    right_tr = right.get_rect()
    up_tr = up.get_rect()
    dw_tr = down.get_rect()
    
    liste_img = [left,right,up,down]
    liste_tr = [left_tr,right_tr,up_tr,dw_tr]
    
    pick = random.randint(0, 3)
    triangle = up_tr
    
    line = pygame.Rect(0,300,500,2)
    zone = pygame.Rect(x-5, y, 50, 50)
    
    clock = pygame.time.Clock()
    while not gameExit and Gus.level == 99:
        
        if countdown >= 0:
        
            if frame_count <= 30:
                frame_count += 1
            else:
                frame_count = 0
            
            if frame_count <= 15:
                a=0
            elif frame_count > 15:
                a=1
        
               
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                   
                  # Condition becomes true when keyboard is pressed   
                if event.type == pygame.KEYDOWN:
       
                    if event.key == pygame.K_UP and start_y >= 300 and triangle == up_tr:
                        pressed = True
                    elif event.key != pygame.K_UP and start_y >= 500 and triangle == up_tr:
                        time = 0
                        pressed = False
                    elif event.key == pygame.K_UP and start_y >= 300 and triangle != up_tr:
                        wrong = True
                        
                    if event.key == pygame.K_DOWN and start_y >= 300 and triangle == dw_tr:
                        pressed = True
                    elif event.key != pygame.K_DOWN and start_y >= 500 and triangle == dw_tr:
                        time = 0
                        pressed = False
                    elif event.key == pygame.K_DOWN and start_y >= 300 and triangle != dw_tr:
                        wrong = True
                        
                    if event.key == pygame.K_LEFT and start_y >= 300 and triangle == left_tr:
                        pressed = True
                    elif event.key != pygame.K_LEFT and start_y >= 500 and triangle == left_tr:
                        time = 0
                        pressed = False
                    elif event.key == pygame.K_LEFT and start_y >= 300 and triangle != left_tr:
                        wrong = True
                        
                    if event.key == pygame.K_RIGHT and start_y >= 300 and triangle == right_tr:
                        pressed = True
                    elif event.key != pygame.K_RIGHT and start_y >= 500 and triangle == right_tr:
                        time = 0
                        pressed = False                                        
                    elif event.key == pygame.K_RIGHT and start_y >= 300 and triangle != right_tr:
                        wrong = True
                        
            if pressed == True:
                time += 1
                
                if time == 1:
                    score = 100-abs((start_y - y)/5)
                elif time != 1:
                    score = 0
        
            if wrong == True:
                time += 1
                done = 0
                
                if time == 1:
                    score = -80
                elif time != 1:
                    score = 0
                    
            start_y += 2 + (done/8)
            if start_y >= 500:
                pressed = False
                wrong = False
                start_y = -50
                time = 0
                pick = random.randint(0, 3)
                triangle = liste_tr[pick]
                done += 1
                
            seconds=(pygame.time.get_ticks()-start_ticks)/1000
            countdown = int(60 - seconds)
            
            screen.fill((0,0,0))
            triangle.topleft = (140,start_y)        
    
            total_score += score
            points = str(int(total_score))
            
            pnj_batteur = batteur[a]
            pnj_bass = bassist[a]
            pnj_guit = guitar[a]
            
            rect_batteur = pnj_batteur.get_rect()
            rect_batteur.topleft=(270,20)
            
            rect_bass = pnj_bass.get_rect()
            rect_bass.topleft=(200,50)
            
            rect_guit = pnj_guit.get_rect()
            rect_guit.topleft=(350,80)
            
            gugus = gugus_move[a]
            rect_gugus = gugus.get_rect()
            rect_gugus.topleft = (250,150)
            
            screen.blit(fond, (0,0)) 
            screen.blit(pnj_batteur, rect_batteur)
            screen.blit(pnj_bass, rect_bass)
            screen.blit(pnj_guit, rect_guit)        
            screen.blit(gugus, rect_gugus)        
            
            pygame.draw.rect(screen, (250,250,0), zone)
            pygame.draw.rect(screen, (250,0,0), line)        
            pygame.draw.rect(screen, (250,250,250), triangle)
            screen.blit(liste_img[pick],liste_tr[pick])
            
            titre = myfont.render("Time", False, (20, 20, 20))
            textsurface = myfont.render(str(countdown), False, (20, 20, 20))
            pts = myfont.render(points, False, (20, 20, 20))
            
            textsurface1 = myfont.render("Appuies sur la flèche ", False, (0, 0, 0))
            textsurface2 = myfont.render("lorsque celle-ci est ", False, (0, 0, 0))
            textsurface25 = myfont.render("dans le carré jaune.", False, (0, 0, 0))            
            if Gus.try_music == 1:
                textsurface3 = myfont.render("Score à battre :", False, (0, 0, 0))
                textsurface4 = myfont.render(" 3000", False, (0, 0, 0))
            elif Gus.try_music != 1:
                textsurface3 = myfont.render("Meilleur score :", False, (0, 0, 0))
                textsurface4 = myfont.render(str(Gus.pb_music), False, (0, 0, 0))

            screen.blit(textsurface1,(250, 350))
            screen.blit(textsurface2,(250,370)) 
            screen.blit(textsurface25,(250,390)) 
            screen.blit(textsurface3,(250, 415))
            screen.blit(textsurface4,(325,435)) 
    
            screen.blit(titre,(20,20))
            screen.blit(textsurface,(20,35))
            screen.blit(pts,(20,50))
        
        elif countdown < 0:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if int(total_score) >= 3000 and Gus.try_music == 1:
                            Gus.try_music = 2
                            sac.Carton = 1
                            Gus.pb_music = int(total_score)
                        elif int(total_score) >= int(Gus.pb_music) and Gus.try_music >= 2:
                            Gus.try_music +=1
                            Gus.pb_music = int(total_score)
                        if Gus.try_music > 2 :
                            tr.money_win_music += int(total_score/1000)
                        Gus.level = 3.2
                        Gus.spawn = 3
                        time = 0

                              
            end_game(points)

            
        pygame.display.update()
        
        clock.tick(100)        

def nivo4(sac,action,Gus,tr):
    pygame.init()
    speed_move = Gus.speed
    frame_count = Gus.frame
    a=0
    time = 0
    x =  (display_width-gugus_width)/2
    y = (display_height-gugus_height)/2  
    rel_x = 0 
    rel_y = 0
    x_change = 0
    y_change = 0
    gugus = gugus_face
    
    screen_x = -225 + x
    screen_y = -225 + y 
    
    interact = False
    tune = Gus.money
    alcool = sac.Alcool
    preservatif = sac.Capote   
    
    gameExit = False
    
    while not gameExit and Gus.level >= 4 and Gus.level < 5:
        
        if not pygame.mixer.music.get_busy() and Gus.current <= len(playlist):
            Gus.current+=1
            pygame.mixer.music.load ( playlist[Gus.current])
            pygame.mixer.music.play()
        elif not pygame.mixer.music.get_busy() and Gus.current > len(playlist):
            Gus.current=0
            pygame.mixer.music.load ( playlist[Gus.current])
            pygame.mixer.music.play()        
                    
        if frame_count <= 30:
            frame_count += 1
        else:
            frame_count = 0
        
        if frame_count <= 15:
            a=0
        elif frame_count > 15:
            a=1
            
        rect_gugus = gugus.get_rect() 
        tr.update_items()
        Gus.update_items(tr)
        sac.update_items(tr)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    other_s.play()
                    Gus.pause += 1    
                if event.key == pygame.K_TAB:
                    other_s.play() 
            ############################
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  
                    x_change = -speed_move
                    rel_x = speed_move
                    y_change = 0
                    rel_y = 0
                    step_s.play(-1)
                elif event.key == pygame.K_RIGHT:
                    x_change = speed_move
                    rel_x = -speed_move
                    y_change = 0
                    rel_y = 0
                    step_s.play(-1)
                elif event.key == pygame.K_UP:
                    y_change = -speed_move
                    rel_y = speed_move
                    x_change = 0
                    rel_x = 0
                    step_s.play(-1)
                elif event.key == pygame.K_DOWN:
                    y_change = speed_move
                    rel_y = -speed_move
                    x_change = 0
                    rel_x = 0
                    step_s.play(-1)
                if event.key == pygame.K_a and not action.click:
                    action.click = True
                    click_.play()
                    
                    if 655+screen_x < x < 711+screen_x and 326+screen_y < y < 398+screen_y and Gus.level == 4:
                        tr.barre_cereal += 1
                        
                    if 40+screen_x < x < 96+screen_x and 300+screen_y < y < 383+screen_y and Gus.level == 4:
                        tr.press_clope_trom += 1
                    #PERSONNES
                    ###EST
                         
                elif event.key != pygame.K_a:
                
                    action.click = False
                
                if event.key == pygame.K_RETURN:
                    enter_s.play()
                    if 710+screen_x < x < 800+screen_x and 326+screen_y < y < 398+screen_y and Gus.level == 4 and sac.Barre_Cereales == 1:
                        tr.eat_barre = True
                        Gus.spawn = 2
                        time = 0
                    
                    if 856+screen_x < x < 952+screen_x and 410+screen_y < y < 469+screen_y and Gus.level == 4:
                        Gus.level = 1000
                                            

                elif event.key != pygame.K_RETURN:
                
                    action.change_level = False
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_change = 0
                    rel_x = 0
                    gugus = gugus_gauche 
                    step_s.stop()
                if event.key == pygame.K_RIGHT:
                    x_change = 0
                    rel_x = 0
                    gugus = gugus_droite 
                    step_s.stop()

                if event.key == pygame.K_UP:
                    y_change = 0
                    rel_y = 0
                    gugus = gugus_dos 
                    step_s.stop()
                    
                if event.key == pygame.K_DOWN:
                    y_change = 0
                    rel_y = 0
                    gugus = gugus_face 
                    step_s.stop()
                    
            ######################            
        keys=pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            gugus=gugus_walkdown[a]
        if keys[pygame.K_UP]:
            gugus=gugus_walkup[a]
        if keys[pygame.K_RIGHT]:
            gugus=gugus_walkright[a]
        if keys[pygame.K_LEFT]:
            gugus=gugus_walkleft[a]
            
        rect_gugus.topleft = (x,y)
                        
        if Gus.level == 4:
    
            if Gus.spawn == 1 and time < 2:
                screen_x,screen_y,x,y = spawn_level(x,y,159,340)
            elif Gus.spawn == 2 and time < 2:
                screen_x,screen_y,x,y = spawn_level(x,y,769,367)
        
            time += 1
            liste_mur = level_4(screen,screen_x,screen_y)
            
            x_change,y_change,rel_x,rel_y = collisions(liste_mur,rect_gugus,x_change,y_change,speed_move,rel_x,rel_y)
            
            screen_x += rel_x
            screen_y += rel_y
               
        
        ##INTERACTION LVL 2
        if tr.eat_barre == True and time == 1 and sac.Barre_Cereales == 1:
            if Gus.pv >= 80:
                Gus.pv = 100
                sac.Barre_Cereales == 0
            elif Gus.pv < 80:
                Gus.pv += 20
                sac.Barre_Cereales == 1
                
        ##OBJET LVL 2
        if 655+screen_x < x < 711+screen_x and 326+screen_y < y < 398+screen_y and Gus.level == 4:
            tr.barre_cereal = zone_interaction(screen,"Qu'est-ce que c'est? (A)",action,tr.barre_cereal,"une barre de céréales!")
            sac.Barre_Cereales = 1
            
        elif 710+screen_x < x < 800+screen_x and 326+screen_y < y < 398+screen_y and Gus.level == 4 and sac.Barre_Cereales == 1 and tr.eat_barre == False:
            textsurface = myfont.render("Manger la barre de céréales", False, (0, 0, 0))
            textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
            screen.blit(textsurface,(x,y-60))
            screen.blit(textsurface2,(x+35,y-40))            

        elif 856+screen_x < x < 952+screen_x and 410+screen_y < y < 469+screen_y and Gus.level == 4:
            textsurface = myfont.render("Donnes moi ton sac !! ", False, (0, 0, 0))
            textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
            screen.blit(textsurface,(x-100,y-60))
            screen.blit(textsurface2,(x,y-40))  
            
        elif 40+screen_x < x < 96+screen_x and 300+screen_y < y < 383+screen_y and Gus.level == 4:
            tr.press_clope_trom = zone_interaction(screen,"Fouiller sous le siège (A)",action,tr.press_clope_trom,"un paquet de clopes!")
            tr.clope_trome = 5
            
        if screen_x >= 0 and rel_x > 0:
            screen_x = 0
            x -= rel_x
        elif screen_x <= display_width - 1000 and rel_x < 0 :
            screen_x = display_width - 1000
            x -= rel_x
        if screen_y >= 0 and rel_y > 0 :
            screen_y = 0
            y  -= rel_y
        elif screen_y <= display_height - 707 and rel_y < 0:
            screen_y = display_height - 707 
            y -= rel_y
            
        if x < (display_width-gugus_width)/2 and rel_x < 0:
            screen_x = 0
            x -= rel_x
        elif x > (display_width-gugus_width)/2 and rel_x > 0:
            screen_x = display_width - 1000
            x -= rel_x
            
        if y < (display_height-gugus_height)/2 and rel_y < 0:
            screen_y = 0
            y -= rel_y
        elif y > (display_height-gugus_height)/2 and rel_y > 0:
            screen_y = display_height - 707 
            y -= rel_y
        
        ##OBJETS

        screen.blit(gugus, rect_gugus)
        
        pv = Gus_font.render("Santé : " + str(Gus.pv), False, (220, 220, 220))
        argent = Gus_font.render("Argent : " + str(round(Gus.money,2)), False, (31, 160, 85))
        lvl = Gus_font.render("Niveau : " + str(int(Gus.level)), False, (220, 220, 220))
    
        screen.blit(pv , (10,20))
        screen.blit(lvl , (10,45))
        screen.blit(argent , (10,70))
        screen.blit(sac_tab , (10,450))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_TAB]:
            affich_sac(screen,sac)
        if (Gus.pause%2) == 1:
            pause(screen,gameExit,Gus,sac,tr)
        if Gus.pv == 0 or tr.game_over == True:
            game_over(screen)

        pygame.display.update()
        
        clock.tick(100)    

def nivo_fight(sac,action,Gus,tr):
    gameExit=False
      
    a = 0
    gugus = gus_fight_right[0]
    rect_gugus = gugus.get_rect()
    frame_count = 0
    side = True
    animation = False
    type_anim ="none"

    fightr = fighter_1_r[0]
    
    fightrect = fightr.get_rect()
    
    lvl = lvl_fight[0]
    
    x = 150
    y = 230
    
    x2 = 300
    y2 = 214
    
    move_y = 0
    move_x = 0
    air_time = 1
    
    jump = False
    fall = False
    
    attack = False
    super_attack = False
    hit = False
    collision = False
    
    opp_clean = 0
    clean_hit = 0
    
    gus_life = 100
    fighter_life = 100
    
    clock = pygame.time.Clock()
    
    while not gameExit and Gus.level == 1000:
        
        sac.Planing = 0
        
        if Gus.pv > 0 and fighter_life > 0:
            if frame_count <= 60:
                frame_count += 1
            else:
                frame_count = 0
                animation = False
                type_anim = "none"
            
            if frame_count <= 15 and not animation:
                a=0
            elif 15 < frame_count <= 30 and not animation:
                a=1
            elif 30 < frame_count <= 45 and not animation:
                a=2
            elif 45 < frame_count <= 60 and not animation:
                a=3
    
            elif frame_count <= 15 and animation:
                a = 0
            elif 15 < frame_count <= 30 and animation:
                a = 1
            elif 30 < frame_count <= 45 and animation :
                a = 2
            elif 45 < frame_count <= 60 and animation:
                a = 3
                           
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                   
                  # Condition becomes true when keyboard is pressed   
                if event.type == pygame.KEYDOWN:
       
                    if event.key == pygame.K_UP :
    
                        jump = True
                        
                    if event.key == pygame.K_DOWN :
                        fall = True
                        
                    if event.key == pygame.K_LEFT :
                        move_x = -2
                        side = False
                        
                    if event.key == pygame.K_RIGHT :
                        move_x = 2
                        side = True
                        
                    if event.key == pygame.K_a :
                        attack = True
                    if event.key == pygame.K_z :
                        super_attack = True         
                        
                if event.type == pygame.KEYUP:
       
                    if event.key == pygame.K_UP :
                        jump = False
                        
                    if event.key == pygame.K_DOWN :
                        fall = False
                        
                    if event.key == pygame.K_LEFT :
                        move_x = 0
    
                    if event.key == pygame.K_RIGHT :
                        move_x = 0
    
                    if event.key == pygame.K_a :
                        attack = False
                    if event.key == pygame.K_z :
                        super_attack = False
            
            if side:
                if type_anim == "none":
                    gugus=gus_fight_right[a]
                elif type_anim == "punch":
                    gugus = gus_pch_r[a]
                elif type_anim == "kick":
                    gugus = gus_kick_r[a]
                elif type_anim == "super_punch":
                    gugus = gus_sp_r[a]
                elif type_anim =="jump_punch":
                    gugus = gus_jp_r[a]
                elif type_anim =="adv_c2c":
                    gugus = gus_ouille_r[a]
                elif type_anim =="adv_sp":
                    gugus = gus_ouille_r[a]
    
            else:
                if type_anim == "none":
                    gugus=gus_fight_left[a]
                elif type_anim == "punch":
                    gugus = gus_pch_l[a]
                elif type_anim == "kick":
                    gugus = gus_kick_l[a]
                elif type_anim == "super_punch":
                    gugus = gus_sp_l[a]
                elif type_anim =="jump_punch":
                    gugus = gus_jp_l[a]
                elif type_anim =="adv_c2c":
                    gugus = gus_ouille_l[a]
                elif type_anim =="adv_sp":
                    gugus = gus_ouille_l[a]
                    
            if (y < 230 and not rect_gugus.colliderect(fightrect)) or jump :
                air_time += 1
     
            if jump : 
                move_y = -(30/air_time)
                
            if y < 230 and air_time > 30:
                move_y = 3
            elif y < 230 and fall :
                move_y = 5
            elif y >= 230 and not jump:
                move_y = 0
                y = 230
                jump = False
                air_time = 1
                
            if rect_gugus.colliderect(fightrect):
                if abs(rect_gugus.bottom - fightrect.top) <= 10 and move_y > 0:
                    move_y = 0
                    air_time = 1
                    jump = False
                if abs(rect_gugus.top - fightrect.bottom) <= 10 and move_y < 0:
                    move_y = 0
                if abs(rect_gugus.left - fightrect.right) <= 10 and move_x < 0:
                    move_x = 0             
                if abs(rect_gugus.right - fightrect.left) <= 10 and move_x > 0:
                    move_x = 0
    
    
            if abs(rect_gugus.right - fightrect.left) <= 80 and move_x > 0 and y2-20 < y < y2+20:
                if 50 < x2 < 400:
                    x2 += move_x/4
                elif x2 >= 400 :
                    x2 -= move_x
            if abs(rect_gugus.left - fightrect.right) <= 80 and move_x < 0 and y2-20 < y < y2+20:
                if 50 < x2 < 400:
                    x2 += move_x/4
                elif x2 <= 50 :
                    x2 -= move_x
                
            ##COUP SIMPLE AVEC A
            if abs(rect_gugus.left - fightrect.right) <= 5 and attack and move_x != 0:
                fighter_life -=5
                if clean_hit < 5:
                    clean_hit += 1
                x2 -= 20
                opp_clean = 0
                animation = True
                type_anim = "punch"
                frame_count = 1
            if abs(rect_gugus.right - fightrect.left) <= 5 and attack and move_x != 0:
                fighter_life -=5
                x2 += 20
                if clean_hit < 5:
                    clean_hit += 1
                opp_clean = 0
                animation = True
                type_anim = "punch"
                frame_count = 1
                
            ##COUP COMBO A ET Z
            if abs(rect_gugus.left - fightrect.right) <= 5 and attack and move_x != 0 and super_attack:
                fighter_life -= 10
                if clean_hit < 5:
                    clean_hit += 1
                x += 20
                opp_clean = 0
                animation = True
                type_anim = "kick"
                frame_count = 1
            if abs(rect_gugus.right - fightrect.left) <= 5 and attack and move_x != 0 and super_attack:
                fighter_life -= 10
                x -= 20
                if clean_hit < 5:
                    clean_hit += 1
                opp_clean = 0
                animation = True
                type_anim = "kick"
                frame_count = 1
    
            ##SUPER COUP AVEC Z
            if abs(rect_gugus.left - fightrect.right) <= 5 and super_attack and move_x != 0 and clean_hit >= 5:
                fighter_life -=15
                clean_hit = 0
                x2 -= 120
                opp_clean = 0
                animation = True
                type_anim = "super_punch"
                frame_count = 1
            if abs(rect_gugus.right - fightrect.left) <= 5 and super_attack and move_x != 0 and clean_hit >= 5:
                fighter_life -=15
                x2 += 120
                clean_hit = 0
                opp_clean = 0
                animation = True
                type_anim = "super_punch"
                frame_count = 1
                
            ##COUP SAUTE
            if abs(rect_gugus.left - fightrect.right) <= 15 and attack and 10 < air_time < 35:
                fighter_life -= 10
                if clean_hit < 5:
                    clean_hit += 1
                opp_clean = 0
                x2 -= 50
                animation = True
                type_anim = "jump_punch"
                frame_count = 1
                
            if abs(rect_gugus.right - fightrect.left) <= 15 and attack and 10 < air_time < 35:
                fighter_life -=10
                x2 += 50
                if clean_hit < 5:
                    clean_hit += 1
                opp_clean = 0
                animation = True
                type_anim = "jump_punch"
                frame_count = 1
                
            ##COUP ADVERSAIRE
            if rect_gugus.colliderect(fightrect):
                collision = True
            elif not rect_gugus.colliderect(fightrect):
                collision = False
                
            if collision and move_x == 0 and not attack and not jump:
                hit = True
            else:
                hit = False
    
            ##CORP A CORP           
            if abs(rect_gugus.left - fightrect.right) <= 1 and hit:
                Gus.pv -=5
                x += 80
                clean_hit = 0
                opp_clean += 1
                animation = True
                type_anim = "adv_c2c"
                frame_count = 1            
                
            if abs(rect_gugus.right - fightrect.left) <= 1 and hit:
                Gus.pv -=5
                x -= 80
                clean_hit = 0
                opp_clean += 1
                animation = True
                type_anim = "adv_c2c"
                frame_count = 1            
                
            ##SUPER COUP ADVERSAIRE
            if abs(rect_gugus.left - fightrect.right) <= 5 and hit and opp_clean == 3:
                Gus.pv -= 10
                x += 100
                clean_hit = 0
                opp_clean = 0
                animation = True
                type_anim = "adv_sp"
                frame_count = 1            
                
            if abs(rect_gugus.right - fightrect.left) <= 5 and hit and opp_clean == 3:
                Gus.pv -=10
                x -= 100
                clean_hit = 0
                opp_clean = 0
                animation = True
                type_anim = "adv_sp"
                frame_count = 1            
                
            ##COMBO ADVERSAIRE
            ##PROJECTILE??           
                    
            if move_x == 0 and not jump:
                if x2 > x and not collision and x2 > 50:
                    x2 -= 0.5
                    if type_anim == "none":
                        fightr = fighter_1_r[a]
                    elif type_anim == "adv_c2c":
                        fightr = fighter_pch_r[a]
                    elif type_anim == "adv_sp":
                        fightr = fighter_sp_r[a]
                    elif type_anim == "punch" or type_anim == "kick" or type_anim == "super_punch" or type_anim == "jump_punch":
                        fightr = fighter_ouille_r[a]
    
                elif x2 < x and not collision and x2 < 400:
                    x2 += 0.5
                    if type_anim == "none":
                        fightr = fighter_1_l[a]
                    elif type_anim == "adv_c2c":
                        fightr = fighter_pch_l[a]
                    elif type_anim == "adv_sp":
                        fightr = fighter_sp_l[a]
                    elif type_anim == "punch" or type_anim == "kick" or type_anim == "super_punch" or type_anim == "jump_punch":
                        fightr = fighter_ouille_l[a]
    
                else:
                    x2 = x2
                    if type_anim == "none" and side:
                        fightr = fighter_1_r[a]
                    elif type_anim == "none" and not side:
                        fightr = fighter_1_l[a]
                    elif type_anim == "adv_c2c" and side:
                        fightr = fighter_pch_r[a]
                    elif type_anim == "adv_c2c" and not side:
                        fightr = fighter_pch_l[a]
                    elif type_anim == "adv_sp" and side:
                        fightr = fighter_sp_r[a]
                    elif type_anim == "adv_sp" and not side:
                        fightr = fighter_sp_l[a]
                    elif (type_anim == "punch" or type_anim == "kick" or type_anim == "super_punch" or type_anim == "jump_punch") and side:
                        fightr = fighter_ouille_r[a]
                    elif (type_anim == "punch" or type_anim == "kick" or type_anim == "super_punch" or type_anim == "jump_punch") and not side:
                        fightr = fighter_ouille_l[a]
                       
            x += move_x
            y += move_y  
    
            if x > 450 :
                x=450
            if x < 0:
                x = 0
            if x2 > 480:
                x2 = 480
            if x2 < 20:
                x2 = 20
            
            screen.fill((0,0,0))
            
            rect_gugus.topleft = (x,y)        
            fightrect.topleft = (x2,y2)        
            
            lvl = lvl_fight[a]
            screen.blit(lvl,(0,0))
            screen.blit(gugus,rect_gugus)
            screen.blit(fightr,fightrect)
            
            clean_bar = power_bar[clean_hit]

            screen.blit(clean_bar,(20,70))
            
            pv = Gus_font.render("Santé : " + str(Gus.pv), False, (220, 220, 220))
            super_punch = Gus_font.render("Super power : ", False, (220, 220, 220))
            lvl = Gus_font.render("Niveau : FIGHT!", False, (220, 220, 220))
            frapper = Gus_font.render("Frapper", False, (220, 220, 220))
            control = Gus_font.render("(A et/ou Z) + flèches", False, (220, 220, 220))
        
            screen.blit(pv , (20,35))
            screen.blit(super_punch,(20,50))
            screen.blit(lvl , (20,95))
            screen.blit(frapper, (400,65))
            screen.blit(control, (360,95))
            
            textsurface = myfont.render(str(fighter_life), False, (210, 210, 210))
            screen.blit(textsurface,(460,35))
        
        elif Gus.pv <= 0 and fighter_life > 0:
            tr.clopesEst = 0 
            tr.clopes_nn = 0 
            tr.clope_metro = 0
            tr.clope_trome = 0
            tr.capote_nn = 0
            tr.capote_buro = 0
            tr.capote_entree = 0 
            tr.capoteNord = 0
            tr.capote_3 = 0
            tr.seringue_NE = 0
            tr.seringue_NO = 0
            tr.seringueN = 0
            tr.seringueO = 0
            tr.bouteille_NO = 0
            tr.bouteille_alc = 0
            tr.biere = 0
            tr.torchon_salon = 0
            tr.torchonsdb1 = 0
            tr.torchoncoul = 0
            tr.torchonch = 0
            tr.torchon_entre = 0
            tr.torchon_mom = 0
            
            sac.soupe_froide = 0
            sac.soupe_chaude = 0
            sac.Cle_maison = 0
            sac.Briquet = 0
            sac.Bonbons_bizarres = 0 
            sac.Ballon = 0
            
            sac.Telephone = 0
            sac.Clef = 0
            sac.Horaires_bus = 0
            sac.Portefeuille = 0
            sac.Photos = 0
            sac.Filtre_postillon = 0
            sac.Teuteu = 0
            sac.Huile_rateau = 0
            sac.Rythme = 0
            sac.Argent_mac = 0
            sac.Planing = 0
            sac.Papier = 0
            sac.Ticket = 0
            sac.Charisme = 0
            sac.Sandwich =0
            sac.Gateau = 0
            sac.Pince = 0
            sac.Carton = 0
            sac.Barre_Cereales = 0
               
            Gus.money = 0
            Gus.level = 5
            Gus.spawn = 1
            Gus.pv = 100
            
        elif Gus.pv > 0 and fighter_life <= 0:
            Gus.level = 5
            Gus.spawn = 1
            
        pygame.display.update()
        
        clock.tick(100)    

def nivo5(sac,action,Gus,tr):
    pygame.init()
    speed_move = Gus.speed
    frame_count = Gus.frame
    lvl_move = True
    a=0
    time = 0
    x =  (display_width-gugus_width)/2
    y = (display_height-gugus_height)/2  
    rel_x = 0 
    rel_y = 0
    x_change = 0
    y_change = 0
    gugus = gugus_face
    
    screen_x = -225 + x
    screen_y = -225 + y 
    
    jeu_voit = False
    tune = Gus.money
    alcool = sac.Alcool
    preservatif = sac.Capote
    #CREATION ET CARACTERISTIQUES PNJ
    
    rat_left = pygame.image.load('bank/pnj/rat_g.png')
    
    speed_y = 0
    speed_x = -1
    
    spawn_x = 410
    spawn_y = 470
    spawnx_esc = 490
    spawny_esc = 530
    spawnx_N = 900
    spawny_N = 675
       
    rat_m = pnj(spawn_x,spawn_y,screen_x,screen_y,rat_left,'left') 
    rat_esc = pnj(spawnx_esc,spawny_esc,screen_x,screen_y,rat_left,'left') 
    rat_nord = pnj(spawnx_N,spawny_N,screen_x,screen_y,rat_left,'left') 
    
    #INTERACTIONS

    #OBJETS NIVEAU
    #INTERACTIONS
    phrases_dame_5m = [["Hey gamin, t'as pas","quelques vêtements de","rechange ?"],
                        ["Ah ! Tu m'as trouvé des","habits ?"],
                        ["Merci gamin.","Prends ce plan de la ville", "en échange ."],
                        ["T'as pas fini de venir","me parler ?!"]]
    phrases_assis_5m = [["Tu vois pas que","je suis en train","de lire ?"],
                        ["C'est quoi ça ?","Une clé USB ?","Tu veux que j'en fasse","quoi ?","Moi je veux des trucs","qui me font voyager..." ],
                        ["J'peux pas te payer","mais prends cette clé","Elle doit ouvrir quelque","chose de génial !"]]
    phrases_machine_5m = [["Il parait que mon","frère vit ici...","Mais je ne vois pas","d'appartement dans le","coin..."],
                          ["Tu ne saurais pas","où je pourrais trouver","un plan de la ville ?"],
                          ["Merci pour ce plan","Je vais repartir d'ici","J'ai du me tromper","de station."]]
    phrases_banc_5m = [["Quand partira le","prochain métro ?"],
                       ["Ah cool ! Merci bien .","Si t'as besoin de quoi","que ce soit, va voir","mon cousin. Il est vers","les machines à ticket."],
                       ["T'as vu mon cousin ?"]]
    phrases_chauve_5m = [["Euh ....","Que? Jô nô parlé","pass ton linguea..."],
                         ["'Je me suis fait voler mon ","portefeuille par une","personne avec un haut","bleu et un pantalon ","blanc...'"]]
    
    phrases_clodo_5m = [["Héééé toi !!","T'as pas une p'tite","pièce ou un ticket ?"],
                        ["Tu peux appeler mon","frère avec ton tél ? ","Il faut lui dire ","d'aller à l'autre bout de","la ville..."],
                        ["Ca m'a donné soif tout","ça. T'as pas un","truc à boire ?"],
                        ["Merci petit !! Tu sais, il", "y a des gars dangereux","dans le métro. Tu devrais","être plus prudent. J'en ai","vu un en chaussures grises."]]
    
    phrases_controleur_5n = [["T'as bien ton ticket","petit ?"]]
    phrases_lassl_5n = [["Hey salut Gus,","Tu vas en ville ?"],
                        ["Tiens ! J'ai trouvé","ce truc sur :","'Comment réparer un","ordinateur tout seul'."],
                        ["Tu fais quoi après ?","On m'a parlé d'un verre","en ville."]]
    phrases_pnj_5n = [["J'ai plus de café","dans ma tasse..."],
                      ["Il y a un truc dans ce carton","mais il faudrait se","débarasser des rats ..."],
                      ["J'ai peur de choper une","maladie près de ces","poubelles."],
                      ["C'est un reportage sur les","maladies créées en labo.","Le seul moyen de se","protéger c'est d'avoir un","masque."],
                      ["Merci pour le masque .","Ils ont du prévoir des","medicaments. C'est pour ça","qu'ils créés ces maladies.","Il faut prévenir les gens!"],
                      ["Merci mec, ça va","déjà mieux..."]]
    
    phrases_controleur_5no = [["On nous a signalé","la présence d'une ","personne dangereuse." , "Faites attention ! "],
                              ["J'ai super soif !"],
                              ["Heyyyyy ....Merçiii petchi ! ","wow !! ça tourne...","T'sais, mwa j'ème bien","collektioné lé catre de","jeu..."],
                              ["Oh tu as la carte d'un","Ostoplouc evolution 100 !","Je te l'échange contre","mon talkie walkie."],
                              ["J'adore ma nouvelle carte !"]]
    phrases_pnj_5no = [["Je flippe à fond!"],
                       ["Je peux te prêter mon","téléphone. Mais il","n'a plus de batterie."],
                       ["Si tu as ce que je","recherche, je peux","même te donner le","téléphone."],
                       ["Tiens, prends le tel !"],
                       ["..."]]
    
    phrases_stand_5o = [["On cherche des ","candidats pour l'armée.","Tu en connais ?"]]
    
    phrases_etagere = [["Hé ! Je te vois !", "T'essayes de voler ","quoi là ??"], 
                       ["Non, ils sont","vraiment trop moches !"]]
    phrases_caisse_5c = [["Je peux vous ","aider ?"],
                         ["Hey ! C'est toi qui","m'a coupé internet ?","Bouges pas.","J'appelle le vigile"],
                         ["Je comprend pas,","mon ordinateur ne","marche plus. J'ai","remis internet mais","plus rien ne marche..."],
                         ["Ah ! C'est un problème","de carte mère !","T'en as une sur toi ?"],
                         ["Super, une carte mère","J'ai aucune idée de","ce à quoi ça sert","ni où ça va ..."],
                         ["Tu peux me changer","la carte mère ?","Merci beaucoup, je","vais pouvoir travailler."],
                         ["Je peux t'aider ?"]]
    phrases_mag_5c = [["J'adore ce magasin."]]
    phrases_allee_5c = [["Le vigil ne veut","pas me laisser partir..."],
                        ["Tu as entendu parler de","cette nouvelle maladie ?"],
                        ["J'espère que c'est efficace"],
                        ["On va enfin pouvoir sortir !"]]
    
    phrases_caisse_5s = [["J'en ai marre de","ce travail !"],
                         ["Attends....","Je suis occupé, je rempli ","ce formulaire et je quitte","ce travail !!"]]
    phrases_jeu_5s = [["Hey Gus !","Le vendeur m'a repris","le jeu de voiture","Tu veux pas le","retrouver ?"],
                      ["Je suis sûr que tu", "pourras jamais faire","mieux que mon score !"],
                      ["Bravo tu m'as battu !","Prends cette carte rare","avec toi."],
                      ["Tu es super fort au jeu !","T'as déjà pensé à","donner des cours ?"]]
    phrases_vigil_5s = [["On est en vigilance","rouge écarlate !", "Personne ne sort ","d'ici !"],
                        ["Merci pour l'info, mais","je n'ai plus mon talkie","walkie pour prévenir mes","collègues."],
                        ["Cool un talkie walkie","Je n'en avais plus.","Mais ça ne me dit pas","où est le voleur"],
                        ["Avec ce talkie-walkie","je peux intervenir !","Tout le monde sort !!!"]]
    
    
    phrases_tel = [["Allo ! ... Comment ça ?","... mais c'est à l'autre"," bout de la","ville !! ...","                      flèche+a"],
                   ["Vous dites que mon","frère est là bas ? ..","Très bien ! j'y vais...","","                      flèche+a"],
                   ["Heureusement que j'ai","récupéré un plan de la","ville ! ","                      flèche+a"],
                   [""]]
    
    gameExit = False
    
    while not gameExit and Gus.level >= 5 and Gus.level < 6:

        if not pygame.mixer.music.get_busy() and Gus.current <= len(playlist):
            Gus.current+=1
            pygame.mixer.music.load ( playlist[Gus.current])
            pygame.mixer.music.play()
        elif not pygame.mixer.music.get_busy() and Gus.current > len(playlist):
            Gus.current=0
            pygame.mixer.music.load ( playlist[Gus.current])
            pygame.mixer.music.play()
                    
        if frame_count <= 30:
            frame_count += 1
        else:
            frame_count = 0
        
        if frame_count <= 15:
            a=0
        elif frame_count > 15:
            a=1
            
        rect_gugus = gugus.get_rect() 
        tr.update_items()
        Gus.update_items(tr)
        sac.update_items(tr)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    other_s.play()
                    Gus.pause += 1    
                if event.key == pygame.K_TAB:
                    other_s.play() 
            ############################
            if event.type == pygame.KEYDOWN and tr.game_over == False :

                if event.key == pygame.K_LEFT:  
                    x_change = -speed_move
                    rel_x = speed_move
                    y_change = 0
                    rel_y = 0
                    step_s.play(-1)
                elif event.key == pygame.K_RIGHT:
                    x_change = speed_move
                    rel_x = -speed_move
                    y_change = 0
                    rel_y = 0
                    step_s.play(-1)
                elif event.key == pygame.K_UP:
                    y_change = -speed_move
                    rel_y = speed_move
                    x_change = 0
                    rel_x = 0
                    step_s.play(-1)
                elif event.key == pygame.K_DOWN:
                    y_change = speed_move
                    rel_y = -speed_move
                    x_change = 0
                    rel_x = 0
                    step_s.play(-1)
                if event.key == pygame.K_a and not action.click:
                    action.click = True
                    click_.play()
                    
                    # 5 METRO
                    if 0+screen_x < x < 94+screen_x and 240+screen_y < y < 300+screen_y and Gus.level == 5 and sac.Soda < 2:
                         tr.press_mach1 += 1 
                    if 100+screen_x < x < 201+screen_x and 240+screen_y < y < 300+screen_y and Gus.level == 5 and sac.Soda < 2:
                         tr.press_mach2 += 1 
                    if 220+screen_x < x < 255+screen_x and 230+screen_y < y < 294+screen_y and Gus.level == 5:
                        tr.cig_5m += 1
                    if 908+screen_x < x < 961+screen_x and 86+screen_y < y < 158+screen_y and Gus.level == 5:
                        tr.poubelle_5m += 1
                        
                    if 39+screen_x < x < 91+screen_x and 363+screen_y < y < 435+screen_y and Gus.level == 5 :
                        if sac.Habits == 0 and tr.donne_habits == False :
                            tr.dame_5m = 0
                        if sac.Habits == 1 and tr.donne_habits == False :
                            tr.dame_5m = 1
                        if sac.Habits == 0 and tr.donne_habits == True :
                            tr.dame_5m = 2
                        if tr.give_plan == True :
                            tr.dame_5m = 3
                    
                    if 485+screen_x < x < 541+screen_x and 389+screen_y < y < 446+screen_y and Gus.level == 5:
                        if sac.Cle_USB == 0 and tr.vente_assis == False :
                            tr.pnj_assis_5m = 0
                        if sac.Cle_USB == 1 and tr.vente_assis == False and tr.cachets_pnj_metro == 0:
                            tr.pnj_assis_5m = 1
                        if tr.vente_assis == False and tr.cachets_pnj_metro != 0 and sac.Cle_meuble == 0:
                            tr.pnj_assis_5m = 2
                        if tr.vente_assis == True and sac.Cle_meuble == 1:
                            tr.pnj_assis_5m = 0
                        
                    if 276+screen_x < x < 333+screen_x and 250+screen_y < y < 328+screen_y and Gus.level == 5:
                        if sac.Plan == 0 and tr.give_plan == False :
                            tr.pnj_machine_5m = 0
                        elif sac.Plan == 1:
                            tr.pnj_machine_5m = 1
                        elif sac.Plan == 0 and tr.give_plan == True:
                            tr.pnj_machine_5m = 2

                    if 715+screen_x < x < 777+screen_x and 329+screen_y < y < 430+screen_y and Gus.level == 5:
                        if tr.give_horaire == False:
                            tr.pnj_banc_5m = 0
                        if tr.give_horaire == True:
                            tr.pnj_banc_5m = 1
                        if sac.Telephone == 1:
                            tr.pnj_banc_5m = 2

                    if 664+screen_x < x < 705+screen_x and 50+screen_y < y < 150+screen_y and Gus.level == 5:
                        if tr.info_vol == False:
                            tr.chauve = 0
                        if tr.info_vol == True:
                            tr.chauve = 1
                        
                    # 5 ESCALIER 1
                    if 6 < x < 69 and 148 < y < 238 and Gus.level == 5.1 :
                        tr.poub_esc1 += 1
                        
                    # 5 ESCALIER 2
                    if 360 < x < 503 and 120 < y < 236 and Gus.level == 5.2 :
                        if sac.Telephone == 0:
                            tr.clodo_5m = 0
                        if sac.Telephone == 1 and tr.appelle_frere_clodo == False:
                            tr.clodo_5m = 1
                        if tr.appelle_frere_clodo == True and tr.give_soda == False:
                            tr.clodo_5m = 2
                        if tr.appelle_frere_clodo == True and tr.give_soda == True:
                            tr.clodo_5m = 3
                        if tr.call == True:
                            tr.disc += 1
                        
                    # 5 NORD
                    if 404+screen_x < x < 478+screen_x and 140+screen_y < y < 207+screen_y and Gus.level == 5.3 :
                        tr.press_capote_5n += 1
                    if 670+screen_x < x < 739+screen_x and 600+screen_y < y < 700+screen_y and Gus.level == 5.3 :
                        tr.poub_5n += 1
                    if 761+screen_x < x < 822+screen_x and 573+screen_y < y < 667+screen_y and Gus.level == 5.3 :
                        tr.sac_5n += 1
                    if 824+screen_x < x < 930+screen_x and 618+screen_y < y < 700+screen_y and Gus.level == 5.3 :
                        if tr.tue_rats == True:
                            tr.carton_5n += 1
                        elif tr.tue_rats == False:
                            tr.carton_5n = -1
                    if 646+screen_x < x < 710+screen_x and 420+screen_y < y < 482+screen_y and Gus.level == 5.3 :
                        tr.teille_5n += 1
                    if 0+screen_x < x < 110+screen_x and 86+screen_y < y < 167+screen_y and Gus.level == 5.3 :
                        tr.cachet_5n += 1
                        
                    if 256+screen_x < x < 334+screen_x and 460+screen_y < y < 538+screen_y and Gus.level == 5.3 :
                        tr.controleur_5n = 0
                        
                    if 595+screen_x < x < 678+screen_x and 135+screen_y < y < 210+screen_y and Gus.level == 5.3 :
                        if sac.Capote >= 1 and tr.give_capote_lassl == False and Gus.savoir_info == False:
                            tr.lassl_5n = 0
                        if tr.give_capote_lassl == True and Gus.savoir_info == True:
                            tr.lassl_5n = 1
                        if tr.repare_ordi == True:
                            tr.lassl_5n = 2
                        
                    if 550+screen_x < x < 655+screen_x and 610+screen_y < y < 700+screen_y and Gus.level == 5.3 and tr.give_cig_5n == False:
                        tr.pnj_5n = 0
                    if 550+screen_x < x < 655+screen_x and 610+screen_y < y < 700+screen_y and Gus.level == 5.3 and tr.give_cig_5n == True and tr.tue_rats == False:
                        tr.pnj_5n = 1
                        
                    if 550+screen_x < x < 655+screen_x and 610+screen_y < y < 700+screen_y and Gus.level == 5.3 and tr.give_cig_5n == True and tr.tue_rats == True and tr.give_CD == False:
                        tr.pnj_5n = 2
                    if 550+screen_x < x < 655+screen_x and 610+screen_y < y < 700+screen_y and Gus.level == 5.3 and tr.give_cig_5n == True and tr.tue_rats == True and tr.give_CD == True and tr.give_mask == False:
                        tr.pnj_5n = 3
                    if 550+screen_x < x < 655+screen_x and 610+screen_y < y < 700+screen_y and Gus.level == 5.3 and tr.give_cig_5n == True and tr.tue_rats == True and tr.give_CD == True and tr.give_mask == True and tr.give_cachet_5n == False:
                        tr.pnj_5n = 4
                    if 550+screen_x < x < 655+screen_x and 610+screen_y < y < 700+screen_y and Gus.level == 5.3 and tr.give_CD == True and tr.give_mask == True and tr.give_cachet_5n == True:
                        tr.pnj_5n = 5
                        
                    # 5 NORD OUEST
                    if 125+screen_x < x < 215+screen_x and 326+screen_y < y < 427+screen_y and Gus.level == 5.4 and sac.Ticket == 0:
                        tr.mach_tick1 += 1
                    if 125+screen_x < x < 215+screen_x and 438+screen_y < y < 553+screen_y and Gus.level == 5.4 and sac.Ticket == 0:
                        tr.mach_tick2 += 1
                        
                    if 225+screen_x < x < 320+screen_x and 450+screen_y < y < 550+screen_y and Gus.level == 5.4 :
                        if tr.give_cachet_5c == False or tr.give_cachets_5no == False or tr.give_cachet_5n == False and tr.give_alcool_5 == False:
                            tr.controleur_5no = 0
                        if tr.give_cachet_5c == True and tr.give_cachets_5no == True and tr.give_cachet_5n == True and tr.give_alcool_5 == False:
                            tr.controleur_5no = 1
                        if tr.give_alcool_5 == True and sac.Carte_Rare == 0:
                            tr.controleur_5no = 2    
                        if tr.give_alcool_5 == True and sac.Carte_Rare == 1 and tr.echange_tw == False:
                            tr.controleur_5no = 3
                        if tr.echange_tw == True:
                            tr.controleur_5no = 4
                    
                    if 210+screen_x < x < 280+screen_x and 145+screen_y < y < 222+screen_y and Gus.level == 5.4 :
                        if tr.give_horaire == False :
                            tr.pnj_5no = 0
                        if tr.give_horaire == True and tr.batt_tel_5no == False :
                            tr.pnj_5no = 1
                        if tr.batt_tel_5no == True and tr.give_cachets_5no == False :
                            tr.pnj_5no = 2
                        if tr.batt_tel_5no == True and tr.give_cachets_5no == True :
                            tr.pnj_5no = 3
                        if sac.Telephone == 1:
                            tr.pnj_5no = 4
                        
                    # 5 OUEST
                    if 693+screen_x < x < 760+screen_x and 100+screen_y < y < 170+screen_y and Gus.level == 5.5 :
                        tr.poub_5o += 1
                    
                    # 5 SUD OUEST
                    if 195+screen_x < x < 260+screen_x and 585+screen_y < y < 675+screen_y and Gus.level == 5.6 :
                        tr.press_seringue_5so += 1
                    if 345+screen_x < x < 430+screen_x and 130+screen_y < y < 210+screen_y and Gus.level == 5.6 :
                        tr.distrib_5so += 1
                    if 586+screen_x < x < 677+screen_x and 250+screen_y < y < 305+screen_y and Gus.level == 5.6 :
                        tr.poub_5so += 1   
                    if 550+screen_x < x < 675+screen_x and 614+screen_y < y < 675+screen_y and Gus.level == 5.6 :
                        tr.sac_5so += 1
                    if 395+screen_x < x < 524+screen_x and 595+screen_y < y < 672+screen_y and Gus.level == 5.6 and sac.Cle_meuble == 1:
                        tr.meuble_5so += 1
                        
                    if 720+screen_x < x < 975+screen_x and 390+screen_y < y < 525+screen_y and Gus.level == 5.6 :
                        tr.pnj_stand_5so = 0
                        
                    # 5 CENTRE
                    
                    if 346+screen_x < x < 492+screen_x and 60+screen_y < y < 150+screen_y and Gus.level == 5.7 :
                        if tr.caisse_occupee_5c == True:
                            tr.etag_5c2 += 1
                        elif tr.caisse_occupee_5c == False:
                            tr.etag_5c2 = -1
                    if 40+screen_x < x < 435+screen_x and 525+screen_y < y < 616+screen_y and Gus.level == 5.7 :
                        tr.etag_5c1 += 1
                        
                    if 242+screen_x < x < 315+screen_x and 40+screen_y < y < 190+screen_y and Gus.level == 5.7:
                        if tr.ordi_vendeuse == False and tr.recherche == False and tr.coupe_cable == False:
                            tr.caisse_5c = 0
                        if tr.ordi_vendeuse == True and tr.recherche == True and tr.coupe_cable == True:
                            tr.caisse_5c = 1
                        if tr.ordi_vendeuse == True and tr.recherche == False and Gus.savoir_info == False and sac.Carte_Mere == 0:
                            tr.caisse_5c = 2
                        if tr.ordi_vendeuse == True and tr.recherche == False and Gus.savoir_info == True and sac.Carte_Mere == 0 and tr.caisse_occupee_5c == False:
                            tr.caisse_5c = 3
                        if tr.ordi_vendeuse == True and tr.recherche == False and Gus.savoir_info == False and sac.Carte_Mere == 1 and tr.caisse_occupee_5c == False:
                            tr.caisse_5c = 4
                        if tr.ordi_vendeuse == True and tr.recherche == False and Gus.savoir_info == True and sac.Carte_Mere == 1 and tr.caisse_occupee_5c == False:
                            tr.caisse_5c = 5
                        if tr.repare_ordi == True:
                            tr.caisse_5c = 6
                            
                    if 730+screen_x < x < 834+screen_x and 86+screen_y < y < 167+screen_y and Gus.level == 5.7 :
                        tr.pnj_mag_5c = 0
                        
                    if 790+screen_x < x < 900+screen_x and 455+screen_y < y < 535+screen_y and Gus.level == 5.7 :
                        if tr.give_mask == False:
                            tr.pnj_allee_5c = 0
                        if tr.give_mask == True and tr.give_cachet_5c == False:
                            tr.pnj_allee_5c = 1
                        if tr.give_mask == True and tr.give_cachet_5c == True:
                            tr.pnj_allee_5c = 2
                        if tr.give_tw_5 == True and tr.balance_5 == True:
                            tr.pnj_allee_5c = 3
                        
                    # 5 SUD
                    if 35+screen_x < x < 190+screen_x and 450+screen_y < y < 530+screen_y and Gus.level == 5.8 :
                        if tr.caisse_5s_occupe == False:
                            tr.caisse_5s = 0
                        if tr.caisse_5s_occupe == True:
                            tr.caisse_5s = 1
                    
                    if 813+screen_x < x < 900+screen_x and 379+screen_y < y < 460+screen_y and Gus.level == 5.8 :
                        if sac.Jeu == 1 and tr.score_voiture <= 40000:
                            tr.pnj_jeu_5s = 1
                        elif sac.Jeu == 1 and tr.score_voiture  >40000:
                            tr.pnj_jeu_5s = 2
                        elif sac.Jeu == 0 :
                            tr.pnj_jeu_5s = 0
                        if tr.echange_tw == True:
                            tr.pnj_jeu_5s = 3
                        
                    if 840+screen_x < x < 940+screen_x and 30+screen_y < y < 130+screen_y and Gus.level == 5.8 :
                        if tr.balance_5 == False and tr.give_tw_5 == False:
                            tr.vigil_5s = 0
                        if tr.balance_5 == True and tr.give_tw_5 == False:
                            tr.vigil_5s = 1
                        if tr.balance_5 == False and tr.give_tw_5 == True:
                            tr.vigil_5s = 2
                        if tr.balance_5 == True and sac.Talkie_Walkie == 1:
                            tr.vigil_5s = 3
                        
                    if 560+screen_x < x < 706+screen_x and 315+screen_y < y < 395+screen_y and Gus.level == 5.8 :
                        tr.etag_5s += 1
                    if 485+screen_x < x < 650+screen_x and 400+screen_y < y < 480+screen_y and Gus.level == 5.8 :
                        if tr.caisse_5s_occupe == True :
                            tr.bac_5s += 1
                        elif tr.caisse_5s_occupe == False :
                            tr.bac_5s = -1
                    
                elif event.key != pygame.K_a:
                
                    action.click = False
                
                if event.key == pygame.K_RETURN:
                    enter_s.play()
                    if 39+screen_x < x < 91+screen_x and 363+screen_y < y < 435+screen_y and Gus.level == 5 and sac.Habits == 1:
                        tr.donne_habits = True
                        
                    if 276+screen_x < x < 333+screen_x and 250+screen_y < y < 328+screen_y and Gus.level == 5 and sac.Plan == 1:
                        tr.give_plan = True
                        
                    if 715+screen_x < x < 777+screen_x and 329+screen_y < y < 470+screen_y and Gus.level == 5 and sac.Horaires_metro == 1:
                        tr.give_horaire = True
                        
                    if 485+screen_x < x < 541+screen_x and 389+screen_y < y < 446+screen_y and Gus.level == 5 and sac.Cle_USB == 1 and tr.cachets_pnj_metro == 0 and tr.vente_assis == False:
                        tr.donne_USB = True
                    if 485+screen_x < x < 541+screen_x and 389+screen_y < y < 446+screen_y and Gus.level == 5 and tr.cachets_pnj_metro == 1:
                        tr.vente_assis = True
                        
                    if 664+screen_x < x < 705+screen_x and 50+screen_y < y < 150+screen_y and Gus.level == 5 and sac.Telephone == 1:
                        tr.info_vol = True
                        
                    if 360 < x < 503 and 120 < y < 236 and Gus.level == 5.2 and tr.clodo_5m == 1 and sac.Telephone == 1:
                        tr.appelle_frere_clodo = True
                        tr.call = True
                        
                    if 360 < x < 503 and 120 < y < 236 and Gus.level == 5.2 and tr.clodo_5m == 2 and tr.appelle_frere_clodo and sac.Soda != 0:
                        tr.give_soda = True
                    
                    if 550+screen_x < x < 655+screen_x and 610+screen_y < y < 700+screen_y and Gus.level == 5.3 :
                        if sac.Clopes != 0:
                            tr.give_cig_5n = True
                        if tr.tue_rats == True and sac.CD != 0:
                            tr.give_CD = True
                        if tr.give_CD == True and sac.Masque != 0 and tr.pnj_5n == 3:
                            tr.give_mask = True
                        if tr.cachets_militaire != 0 and tr.give_mask == True and tr.pnj_5n == 4:
                            tr.give_cachet_5n = True
                            if sac.Cachets == 1 :
                                tr.recherche = True
                                countdown = (time+10)/60   

                    if 595+screen_x < x < 678+screen_x and 135+screen_y < y < 210+screen_y and Gus.level == 5.3 :
                        if sac.Capote >= 1 and tr.lassl_5n == 0 and Gus.savoir_info == False:
                            tr.give_capote_lassl = True
                    
                    if 824+screen_x < x < 930+screen_x and 618+screen_y < y < 700+screen_y and Gus.level == 5.3 :
                        if sac.Mort_aux_rats == 1 :
                            tr.tue_rats = True
                    
                    if 210+screen_x < x < 280+screen_x and 145+screen_y < y < 222+screen_y and Gus.level == 5.4 and sac.Chargeur == 1:
                        tr.batt_tel_5no = True
                    if 210+screen_x < x < 280+screen_x and 145+screen_y < y < 222+screen_y and Gus.level == 5.4 and tr.cachets_5no == 2 :
                        tr.give_cachets_5no = True
                        if sac.Cachets == 1 :
                            tr.recherche = True
                            countdown = (time+10)/60   
                    
                    if 225+screen_x < x < 320+screen_x and 450+screen_y < y < 550+screen_y and Gus.level == 5.4 :
                        if sac.Alcool != 0 and tr.controleur_5no == 1 :
                            tr.give_alcool_5 = True
                        if tr.give_alcool_5 == True and sac.Carte_Rare == 1 and tr.controleur_5no == 3:
                            tr.echange_tw = True
                        
                    if 313+screen_x < x < 587+screen_x and 231+screen_y < y < 325+screen_y and Gus.level == 5.5 :
                        tr.affich_plan += 1
                    if 886+screen_x < x < 984+screen_x and 260+screen_y < y < 380+screen_y and Gus.level == 5.6 :
                        tr.tab_5so = 0
                        
                    if 720+screen_x < x < 975+screen_x and 390+screen_y < y < 525+screen_y and Gus.level == 5.6 and tr.give_mask== True and sac.Cachets != 0 and tr.validate == False:

                        tr.OK = True
                    if 720+screen_x < x < 975+screen_x and 390+screen_y < y < 525+screen_y and Gus.level == 5.6 and tr.give_mask== True and sac.Cachets != 0 and tr.validate == True:

                        tr.game_over = True
                        
                    if 834+screen_x < x < 935+screen_x and 60+screen_y < y < 190+screen_y and Gus.level == 5.7 :
                        tr.disparu += 1
                        timing = time
                    if 242+screen_x < x < 315+screen_x and 40+screen_y < y < 190+screen_y and Gus.level == 5.7 and sac.Ciseaux == 1 and tr.ordi_vendeuse == False :
                        tr.coupe_cable = True
                        
                        tr.recherche = True
                        countdown = (time+10)/60

                    if 242+screen_x < x < 315+screen_x and 40+screen_y < y < 190+screen_y and Gus.level == 5.7 and sac.Carte_Mere == 1 and tr.ordi_vendeuse == True and tr.recherche == False and Gus.savoir_info == True:
                        tr.repare_ordi = True
                                                
                    if 790+screen_x < x < 900+screen_x and 455+screen_y < y < 535+screen_y and Gus.level == 5.7 and tr.cachets_allee != 0 and tr.give_mask == True:
                        tr.give_cachet_5c = True
                        if sac.Cachets == 1 :
                            tr.recherche = True
                            countdown = (time+10)/60   

                    if 813+screen_x < x < 900+screen_x and 379+screen_y < y < 460+screen_y and Gus.level == 5.8 and tr.pnj_jeu_5s > 0 and sac.Jeu == 1:
                        jeu_voit = True

                    if 840+screen_x < x < 940+screen_x and 30+screen_y < y < 130+screen_y and Gus.level == 5.8 :
                        if tr.info_vol == True and tr.clodo_5m == 3:
                            tr.balance_5 = True
                        if sac.Talkie_Walkie == 1:
                            tr.give_tw_5 = True                            
                            
                    if 35+screen_x < x < 190+screen_x and 450+screen_y < y < 530+screen_y and Gus.level == 5.8 :
                        if tr.pnj_stand_5so == 0 and sac.Contrat == 1 and sac.Stylo == 1 :
                            tr.caisse_5s_occupe = True
                    

                    #     tr.capote_nn = 0 
                    #     tr.capote_buro = 0 
                    #     tr.capote_entree = 0 
                    #     tr.capoteNord = 0
                    #     tr.capote_3 = 0
                    #     tr.give_condom = True
                    # if 826+screen_x < x < 907+screen_x and 522+screen_y < y < 576+screen_y and Gus.level == 3 and sac.Argent_mac == 50:
                    #     tr.give_mac = True
                            
                elif event.key != pygame.K_RETURN:
                
                    action.change_level = False
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_change = 0
                    rel_x = 0
                    gugus = gugus_gauche 
                    step_s.stop()
                if event.key == pygame.K_RIGHT:
                    x_change = 0
                    rel_x = 0
                    gugus = gugus_droite 
                    step_s.stop()

                if event.key == pygame.K_UP:
                    y_change = 0
                    rel_y = 0
                    gugus = gugus_dos 
                    step_s.stop()
                    
                if event.key == pygame.K_DOWN:
                    y_change = 0
                    rel_y = 0
                    gugus = gugus_face 
                    step_s.stop()
                    
            ######################            
        keys=pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            gugus=gugus_walkdown[a]
        if keys[pygame.K_UP]:
            gugus=gugus_walkup[a]
        if keys[pygame.K_RIGHT]:
            gugus=gugus_walkright[a]
        if keys[pygame.K_LEFT]:
            gugus=gugus_walkleft[a]
            
        rect_gugus.topleft = (x,y)
                        
        if Gus.level == 5:
            
            lvl_move = True
    
            if Gus.spawn == 1 and time < 2:
                screen_x,screen_y,x,y = spawn_level(x,y,705,461)
            elif Gus.spawn == 2 and time < 2:
                screen_x,screen_y,x,y = spawn_level(x,y,229,100)
        
            time += 1
            liste_mur = level_5M(screen,screen_x,screen_y)
               
            if rat_m.side == "left":
                rat_m = pnj(spawn_x,spawn_y,screen_x,screen_y,rat_left,'left')
            elif rat_m.side == "right":
                rat_m = pnj(spawn_x,spawn_y,screen_x,screen_y,rat_right,'right')
                
            speed_x,speed_y = rat_m.collisions_pnj(liste_mur,speed_x,speed_y,rat_right,rat_left,0)
            spawn_x,spawn_y = rat_m.move(spawn_x,spawn_y,speed_x,speed_y)
            
            x_change,y_change,rel_x,rel_y = collisions(liste_mur,rect_gugus,x_change,y_change,speed_move,rel_x,rel_y)
    
            if rat_m.rect.colliderect(rect_gugus) and rat_m.side == "left":
                if abs (rat_m.rect.left - rect_gugus.right) <= 10:
                    speed_x *= -1
                    speed_y *= -1
                    rat_m.side = "right"
                    
            if rat_m.rect.colliderect(rect_gugus) and rat_m.side == "right":
                if abs (rat_m.rect.right - rect_gugus.left) <= 10:
                    speed_x *= -1
                    speed_y *= -1
                    rat_m.side = "left"
                    
            if rect_gugus.colliderect(rat_m.rect):
                if abs (rat_m.rect.left - rect_gugus.right) <= 10:
                    x_change = 0
                    rel_x = 0
            if rat_m.rect.colliderect(rect_gugus):
                if abs (rat_m.rect.right - rect_gugus.left) <= 10:
                    x_change = 0
                    rel_x = 0  
                    
            screen_x += rel_x
            screen_y += rel_y
            
            screen.blit(rat_m.image, rat_m.rect)
        
            if x < 229 and y < 130:
                Gus.level = 5.1
                Gus.spawn = 1
                time = 0

            
        elif Gus.level == 5.1:
            
            lvl_move = False
            
            if Gus.spawn == 1 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,166,335)

            if Gus.spawn == 2 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,166,545)
                        
            time += 1
            
            liste_mur = level_5_esc1(screen,screen_x,screen_y)
        
            x_change,y_change,rel_x,rel_y = collisions(liste_mur,rect_gugus,x_change,y_change,speed_move,rel_x,rel_y) 
            
            x -= rel_x
            y -= rel_y
            
            if y < 270 and x > 265 :
                Gus.level = 5
                Gus.spawn = 2
                time = 0
            if y > 270 and x > 265:
                Gus.level = 5.2
                Gus.spawn = 1
                time = 0            

        elif Gus.level == 5.2:
            
            lvl_move = False

            if Gus.spawn == 1 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,291,145)

            if Gus.spawn == 2 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,285,545)
                        
            time += 1
            
            liste_mur = level_5_esc2(screen,screen_x,screen_y)
            
            if rat_esc.side == "left":
                rat_esc = pnj(spawnx_esc,spawny_esc,screen_x,screen_y,rat_left,'left')
            elif rat_esc.side == "right":
                rat_esc = pnj(spawnx_esc,spawny_esc,screen_x,screen_y,rat_right,'right')
                
            speed_x,speed_y = rat_esc.collisions_pnj(liste_mur,speed_x,speed_y,rat_right,rat_left,0)
            spawnx_esc,spawny_esc = rat_esc.move(spawnx_esc,spawny_esc,speed_x,speed_y)
            
            x_change,y_change,rel_x,rel_y = collisions(liste_mur,rect_gugus,x_change,y_change,speed_move,rel_x,rel_y)
            
                        
            if rat_esc.rect.colliderect(rect_gugus) and rat_esc.side == "left":
                if abs (rat_esc.rect.left - rect_gugus.right) <= 10:
                    speed_x *= -1
                    speed_y *= -1
                    rat_esc.side = "right"
                    
            if rat_esc.rect.colliderect(rect_gugus) and rat_esc.side == "right":
                if abs (rat_esc.rect.right - rect_gugus.left) <= 10:
                    speed_x *= -1
                    speed_y *= -1
                    rat_esc.side = "left"
                    
            if rect_gugus.colliderect(rat_esc.rect):
                if abs (rat_esc.rect.left - rect_gugus.right) <= 10:
                    x_change = 0
                    rel_x = 0
            if rat_esc.rect.colliderect(rect_gugus):
                if abs (rat_esc.rect.right - rect_gugus.left) <= 10:
                    x_change = 0
                    rel_x = 0 
                    
            x -= rel_x
            y -= rel_y
            
            screen.blit(rat_esc.image, rat_esc.rect)
            
            if y < 270 and x < 255 :
                Gus.level = 5.1
                Gus.spawn = 2
                time = 0
            if y > 270 and x < 255:
                Gus.level = 5.3
                Gus.spawn = 1
                time = 0  

        elif Gus.level == 5.3:
            
            lvl_move = True
            
            if Gus.spawn == 1 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,999 - gugus_width,200)

            if Gus.spawn == 2 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,109,407)
                        
            time += 1
            
            liste_mur = level_5N(screen,screen_x,screen_y)
            
            if rat_nord.side == "left":
                rat_nord = pnj(spawnx_N,spawny_N,screen_x,screen_y,rat_left,'left')
            elif rat_nord.side == "right":
                rat_nord = pnj(spawnx_N,spawny_N,screen_x,screen_y,rat_right,'right')
                
            speed_x,speed_y = rat_nord.collisions_pnj(liste_mur,speed_x,speed_y,rat_right,rat_left,0)
            spawnx_N,spawny_N = rat_nord.move(spawnx_N,spawny_N,speed_x,speed_y)
        
            x_change,y_change,rel_x,rel_y = collisions(liste_mur,rect_gugus,x_change,y_change,speed_move,rel_x,rel_y)

            if rat_nord.rect.colliderect(rect_gugus) and rat_nord.side == "left":
                if abs (rat_nord.rect.left - rect_gugus.right) <= 10:
                    speed_x *= -1
                    speed_y *= -1
                    rat_nord.side = "right"
                    
            if rat_nord.rect.colliderect(rect_gugus) and rat_nord.side == "right":
                if abs (rat_nord.rect.right - rect_gugus.left) <= 10:
                    speed_x *= -1
                    speed_y *= -1
                    rat_nord.side = "left"
                    
            if rect_gugus.colliderect(rat_nord.rect):
                if abs (rat_nord.rect.left - rect_gugus.right) <= 10:
                    x_change = 0
                    rel_x = 0
            if rat_nord.rect.colliderect(rect_gugus):
                if abs (rat_nord.rect.right - rect_gugus.left) <= 10:
                    x_change = 0
                    rel_x = 0 
                    
            screen_x += rel_x
            screen_y += rel_y
            
            if tr.tue_rats == False:
                screen.blit(rat_nord.image, rat_nord.rect)
            
            if x > 480 :
                Gus.level = 5.2
                Gus.spawn = 2
                time = 0
            if y > 220 and x < 10:
                Gus.level = 5.4
                Gus.spawn = 1
                time = 0 

        elif Gus.level == 5.4:

            lvl_move = True
            
            if Gus.spawn == 1 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,765,407)

            if Gus.spawn == 2 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,415,631)
                        
            time += 1
            
            liste_mur = level_5NO(screen,screen_x,screen_y)
        
            x_change,y_change,rel_x,rel_y = collisions(liste_mur,rect_gugus,x_change,y_change,speed_move,rel_x,rel_y)
            
            screen_x += rel_x
            screen_y += rel_y
            
            if x > 480 and y > 220:
                Gus.level = 5.3
                Gus.spawn = 2
                time = 0
            if y > 480 :
                Gus.level = 5.5
                Gus.spawn = 1
                time = 0       
                
        elif Gus.level == 5.5:

            lvl_move = True
            
            if Gus.spawn == 1 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,415,66)

            if Gus.spawn == 2 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,621,611)

            if Gus.spawn == 3 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,881,425)
                        
            time += 1
            
            liste_mur = level_5O(screen,screen_x,screen_y)
        
            x_change,y_change,rel_x,rel_y = collisions(liste_mur,rect_gugus,x_change,y_change,speed_move,rel_x,rel_y)
            
            screen_x += rel_x
            screen_y += rel_y
            
            if y < 20 :
                Gus.level = 5.4
                Gus.spawn = 2
                time = 0
            if y > 495 :
                Gus.level = 5.6
                Gus.spawn = 2
                time = 0
            if x > 495:
                Gus.level = 5.7
                Gus.spawn = 1
                time = 0 
                
        elif Gus.level == 5.6:

            lvl_move = True
            
            if Gus.spawn == 1 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,651,28)

            if Gus.spawn == 2 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,899,86)
                        
            time += 1
            
            liste_mur = level_5SO(screen,screen_x,screen_y)
        
            x_change,y_change,rel_x,rel_y = collisions(liste_mur,rect_gugus,x_change,y_change,speed_move,rel_x,rel_y)
            
            screen_x += rel_x
            screen_y += rel_y
            
            if y < 5 :
                Gus.level = 5.5
                Gus.spawn = 2
                time = 0
            if x > 480 :
                Gus.level = 5.8
                Gus.spawn = 1
                time = 0
                
        elif Gus.level == 5.7:

            lvl_move = True
            
            if Gus.spawn == 1 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,21,426)

            if Gus.spawn == 2 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,660,615)
                        
            time += 1
            
            liste_mur = level_5C(screen,screen_x,screen_y)
        
            x_change,y_change,rel_x,rel_y = collisions(liste_mur,rect_gugus,x_change,y_change,speed_move,rel_x,rel_y)
            
            screen_x += rel_x
            screen_y += rel_y
            
            if x < 5 :
                Gus.level = 5.5
                Gus.spawn = 3
                time = 0
            if y > 480 :
                Gus.level = 5.8
                Gus.spawn = 2
                time = 0

        elif Gus.level == 5.8:

            lvl_move = True
            
            if Gus.spawn == 1 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,11,140)

            if Gus.spawn == 2 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,660,16)

            if Gus.spawn == 3:
                if time < 200 and tr.score_voiture > 40000:
                    screen_x,screen_y,x,y = spawn_level(x,y,801,400)
                    textsurface = myfont.render("Tu récupères une carte de jeu", False, (0, 0, 0))
                    screen.blit(textsurface,(x,y-60))
                    sac.Carte_Rare = 1
                elif time < 2 and tr.score_voiture <= 40000 :
                    screen_x,screen_y,x,y = spawn_level(x,y,801,400)
                    
                        
            time += 1
            
            liste_mur = level_5S(screen,screen_x,screen_y)
        
            x_change,y_change,rel_x,rel_y = collisions(liste_mur,rect_gugus,x_change,y_change,speed_move,rel_x,rel_y)
            
            screen_x += rel_x
            screen_y += rel_y
            
            if x < 5 :
                Gus.level = 5.6
                Gus.spawn = 2
                time = 0
            if y < 5 :
                Gus.level = 5.7
                Gus.spawn = 2
                time = 0
                
        
        if tr.press_mach1 != -1 and tr.press_mach2 == -1:
            sac.Soda = 1
        elif tr.press_mach1 == -1 and tr.press_mach2 != -1:
            sac.Soda = 1
        elif tr.press_mach1 != -1 and tr.press_mach2 != -1:
            sac.Soda = 2
        else:
            sac.Soda = 0
            
        if tr.mach_tick1 != -1 and tr.mach_tick2 == -1:
            sac.Ticket = 1
            tr.argent_ticket2 = -1
        elif tr.mach_tick1 == -1 and tr.mach_tick2 != -1:
            sac.Ticket = 1
            tr.argent_ticket2 = -1
        elif tr.mach_tick1 != -1 and tr.mach_tick2 != -1:
            sac.Ticket = 1
            tr.argent_ticket2 = -2
            
        tr.argent_mach_5m = sac.Soda * -1.5
        
        if tr.press_capote_5n != -1:
            tr.capote_5n = 1
        if sac.Contrat == 1 and tr.carton_5n != -1:
            sac.Mort_aux_rats = 0
            
        if tr.coupe_cable == True:
            tr.ordi_vendeuse = True
            sac.Ciseaux = 0
            
        if tr.recherche == True :
            textsurface = myfont.render("Tu devrais ", False, (200, 0, 0))
            textsurface2 = myfont.render("te cacher.", False, (200, 0, 0))
            screen.blit(textsurface,(x,y+60))
            screen.blit(textsurface2,(x,y+80)) 
            
            if tr.caisse_5c == 0 and tr.disparu%2 != 1:
                research = 30 + (countdown-(time/60))
                temps = myfont.render(str(int(research)), False, (22, 22, 9))
                screen.blit(temps , (x,y+100))
            
                if int(research) <= 0:
                        tr.game_over = True
                        
            elif tr.caisse_5c == 1 and tr.disparu%2 != 1:
                research = 15 + (countdown-(time/60))
                temps = myfont.render(str(int(research)), False, (22, 22, 9))
                screen.blit(temps , (x,y+100))
                    
                if int(research) <= 0:
                        tr.game_over = True
                        
            elif sac.Cachets == 0 and tr.give_cachet_5c == True and tr.give_cachet_5n == True and tr.disparu%2 != 1:
                research = 30 + (countdown-(time/60))
                temps = myfont.render(str(int(research)), False, (22, 22, 9))
                screen.blit(temps , (x,y+100))
            
                if int(research) <= 0:
                        tr.game_over = True

        if tr.give_capote_lassl == True:
            Gus.savoir_info = True
            sac.Capote = 0
            
        if tr.repare_ordi == True:
            tr.caisse_occupee_5c = True
            sac.Carte_Mere = 0
            
        if tr.donne_habits == True :
            sac.Habits = 0
        
        if tr.dame_5m == 2 :
            sac.Plan = 1
         
        if tr.give_plan == True :
            sac.Plan = 0
            
        if tr.give_horaire == True :
            sac.Horaires_metro = 0
        
        if tr.batt_tel_5no == True:
            sac.Chargeur = 0
        if tr.give_cachets_5no == True:
            sac.Telephone = 1
            tr.cachets_5no = 0
            
        if tr.donne_USB == True :
            sac.Cle_USB = 0
        if tr.vente_assis == True :
            tr.cachets_pnj_metro = 0
            sac.Cle_meuble = 1
            
        if tr.give_soda == True :
            sac.Soda = 0
        
        if tr.disc >= 4 :
            tr.call = False
            
        if tr.give_cig_5n == True :
            sac.Clopes = 0
            
        if tr.tue_rats == True:
            sac.Mort_aux_rats = 0
            
        if tr.give_CD == True:
            sac.CD = 0
        if tr.give_mask == True:
            sac.Masque = 0
            
        if tr.give_cachet_5c == True :
            tr.cachets_allee = 0
            
        if tr.give_cachet_5n == True :
            tr.cachets_militaire = 0
            
        if tr.OK == True:
            tr.validate = True
            
        if sac.Cachets == 0 and tr.recherche == True:
            textsurface = myfont.render("Tu as tout vendu", False, (0, 0, 0))
            textsurface2 = myfont.render("Mais un contrôleur t'as vu", False, (0, 0, 0))
            screen.blit(textsurface,(x,y-60))
            screen.blit(textsurface2,(x,y-40))
            
        if tr.give_alcool_5 == True :
            sac.Alcool = 0
            
        if tr.caisse_5s_occupe == True:
            sac.Contrat = 0
            sac.Stylo = 0
        
        if jeu_voit == True:
            Gus.level = 333
        
        if tr.echange_tw == True :
            sac.Carte_Rare = 0
            sac.Talkie_Walkie = 1
            
        if tr.give_tw_5 == True:
            Gus.level = 6
            Gus.spawn = 1

        sac.Cachets = tr.cachets_5no + tr.cachets_pnj_metro + tr.cachets_allee + tr.cachets_militaire
        #LEVEL  METRO
        if 0+screen_x < x < 94+screen_x and 240+screen_y < y < 300+screen_y and Gus.level == 5 and sac.Soda < 2:
            tr.press_mach1 = zone_interaction(screen,"Acheter un truc (A)",action,tr.press_mach1,"une bouteille de soda")
        elif 100+screen_x < x < 201+screen_x and 240+screen_y < y < 300+screen_y and Gus.level == 5 and sac.Soda < 2:
            tr.press_mach2 = zone_interaction(screen,"Acheter un truc (A)",action,tr.press_mach2,"une bouteille de soda")
        elif 220+screen_x < x < 255+screen_x and 230+screen_y < y < 294+screen_y and Gus.level == 5:
            tr.cig_5m = zone_interaction(screen,"Qu'est-ce que c'est ? (A)",action,tr.cig_5m,"quelques clopes !")
            tr.clope_5m = 5
        elif 908+screen_x < x < 961+screen_x and 86+screen_y < y < 158+screen_y and Gus.level == 5:
            tr.poubelle_5m = zone_interaction(screen,"Fouiller la poubelle (A)",action,tr.poubelle_5m,"50 ç !")
            tr.money_5m = 0.5
            
        elif 39+screen_x < x < 91+screen_x and 363+screen_y < y < 435+screen_y and Gus.level == 5 :
            zone_dialogue(screen,"Parler à la dame (A)",action,phrases_dame_5m[tr.dame_5m],tr.dame_5m,5)
            if sac.Habits == 1 and tr.donne_habits == False:
                zone_dialogue(screen,"Parler à la dame (A)",action,phrases_dame_5m[tr.dame_5m],tr.dame_5m,5)
                textsurface = myfont.render("Donner les habits", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40))                
            
        elif 485+screen_x < x < 541+screen_x and 389+screen_y < y < 446+screen_y and Gus.level == 5:
            zone_dialogue(screen,"Parler à la dame (A)",action,phrases_assis_5m[tr.pnj_assis_5m],tr.pnj_assis_5m,5)
            if tr.cachets_pnj_metro == 0 and tr.vente_assis == False and sac.Cle_USB == 1:
                textsurface = myfont.render("Donner la clé USB", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40))
            if tr.cachets_pnj_metro == 1 and tr.vente_assis == False :
                textsurface = myfont.render("Proposer des cachets", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40))                 
            
        elif 276+screen_x < x < 333+screen_x and 250+screen_y < y < 328+screen_y and Gus.level == 5:
            zone_dialogue(screen,"Parler (A)",action,phrases_machine_5m[tr.pnj_machine_5m],tr.pnj_machine_5m,5)

            if sac.Plan == 1 and tr.give_plan == False :
                textsurface = myfont.render("Donner le plan de la ville", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40)) 
                
        elif 715+screen_x < x < 777+screen_x and 329+screen_y < y < 470+screen_y and Gus.level == 5:
            zone_dialogue(screen,"Parler (A)",action,phrases_banc_5m[tr.pnj_banc_5m],tr.pnj_banc_5m,5) 
            if sac.Horaires_metro == 1 :
                textsurface = myfont.render("Donner les horaires du métro", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40))                 
            
        elif 664+screen_x < x < 705+screen_x and 50+screen_y < y < 150+screen_y and Gus.level == 5:
            zone_dialogue(screen,"Parler (A)",action,phrases_chauve_5m[tr.chauve],tr.chauve,5)
            if sac.Telephone == 1 and tr.info_vol == False:
                textsurface = myfont.render("Utiliser le téléphone pour traduire", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x-30,y-60))
                screen.blit(textsurface2,(x+35,y-40))                  

        #LEVEL ESCALIER 1
        elif 6 < x < 69 and 148 < y < 238 and Gus.level == 5.1 :
            tr.poub_esc1 = zone_interaction(screen,"Fouiller la poubelle (A)",action,tr.poub_esc1,"une carte mère ??")
            sac.Carte_Mere = 1
            
        #LEVEL ESCALIER 2
        elif 360 < x < 503 and 120 < y < 236 and Gus.level == 5.2 :
            if tr.call == False:
                zone_dialogue(screen,"Parler au clodo (A)",action,phrases_clodo_5m[tr.clodo_5m],tr.clodo_5m,5)
            elif tr.call == True :
                zone_dialogue(screen,"",action,phrases_tel[tr.disc],tr.disc,5)
                
            if tr.clodo_5m == 1 and tr.appelle_frere_clodo == False :
                textsurface = myfont.render("Appeler le frère :", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x-60,y-60))
                screen.blit(textsurface2,(x-25,y-40))                 
            if tr.clodo_5m == 2 and tr.appelle_frere_clodo == True and sac.Soda != 0:
                textsurface = myfont.render("Donner un soda", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x-60,y-60))
                screen.blit(textsurface2,(x-25,y-40)) 
        #LEVEL NORD
        elif 404+screen_x < x < 478+screen_x and 140+screen_y < y < 207+screen_y and Gus.level == 5.3 :
            tr.press_capote_5n = zone_interaction(screen,"Qu'est-ce que c'est (A)",action,tr.press_capote_5n,"une capote.")
            
        elif 670+screen_x < x < 739+screen_x and 600+screen_y < y < 700+screen_y and Gus.level == 5.3 :
            tr.poub_5n = zone_interaction(screen,"Fouiller la poubelle (A)",action,tr.poub_5n,"une paire de ciseaux.")
            sac.Ciseaux = 1
            
        elif 761+screen_x < x < 822+screen_x and 573+screen_y < y < 667+screen_y and Gus.level == 5.3 :
            tr.sac_5n = zone_interaction(screen,"Fouiller le sac (A)",action,tr.sac_5n,"un CD.")
            sac.CD = 1
            
        elif 824+screen_x < x < 930+screen_x and 618+screen_y < y < 700+screen_y and Gus.level == 5.3 :
            if tr.tue_rats == True :
                tr.carton_5n = zone_interaction(screen,"Fouiller le carton (A)",action,tr.carton_5n,"un contrat bizarre.")  
                sac.Contrat = 1

            if sac.Mort_aux_rats == 1 and tr.tue_rats == False and tr.give_cig_5n == True:
                textsurface = myfont.render("Utiliser la mort aux rats :", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x-60,y-60))
                screen.blit(textsurface2,(x-25,y-40))                 
            elif sac.Mort_aux_rats == 0 and tr.tue_rats == False and tr.give_cig_5n == False:
                textsurface = myfont.render("Ah beurk ! C'est ", False, (0, 0, 0))
                textsurface2 = myfont.render("plein de rats", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x,y-40))
                
        elif 646+screen_x < x < 710+screen_x and 420+screen_y < y < 482+screen_y and Gus.level == 5.3 :
            tr.teille_5n = zone_interaction(screen,"Qu'est-ce que c'est ? (A)",action,tr.teille_5n,"une bouteille.")
            tr.bouteille_5n = 1
            
        elif 0+screen_x < x < 110+screen_x and 86+screen_y < y < 167+screen_y and Gus.level == 5.3 :
            tr.cachet_5n = zone_interaction(screen,"Qu'est-ce que c'est ? (A)",action,tr.cachet_5n,"des cachets.")
            tr.cachets_5no = 2 
            tr.cachets_pnj_metro = 1 
            tr.cachets_allee = 1 
            tr.cachets_militaire = 1
            
        elif 256+screen_x < x < 334+screen_x and 460+screen_y < y < 538+screen_y and Gus.level == 5.3:
            zone_dialogue(screen,"Parler (A)",action,phrases_controleur_5n[tr.controleur_5n],tr.controleur_5n,5)
            
        elif 595+screen_x < x < 678+screen_x and 135+screen_y < y < 210+screen_y and Gus.level == 5.3 :
            zone_dialogue(screen,"Parler (A)",action,phrases_lassl_5n[tr.lassl_5n],tr.lassl_5n,5)
            if sac.Capote >= 1 and tr.lassl_5n == 0 and Gus.savoir_info == False:
                textsurface = myfont.render("Donner des capotes", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40))
            
        elif 550+screen_x < x < 655+screen_x and 610+screen_y < y < 700+screen_y and Gus.level == 5.3 :
            zone_dialogue(screen,"Parler (A)",action,phrases_pnj_5n[tr.pnj_5n],tr.pnj_5n,7)
            if sac.Clopes != 0 and tr.give_cig_5n == False:
                textsurface = myfont.render("Donner des cigarettes", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40)) 
            if sac.CD == 1 and tr.tue_rats == True:
                textsurface = myfont.render("Donner le CD", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40))                
            if sac.Masque == 1 and tr.give_CD == True:
                textsurface = myfont.render("Donner le masque", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40))                
            if tr.cachets_militaire == 1 and tr.give_mask == True :
                textsurface = myfont.render("Donner le médicament", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40)) 
                
        #LEVEL NORD OUEST
        elif 125+screen_x < x < 215+screen_x and 326+screen_y < y < 427+screen_y and Gus.level == 5.4 :
            if sac.Ticket == 0:
                tr.mach_tick1 = zone_interaction(screen,"Acheter un ticket (A)",action,tr.mach_tick1,"un ticket")
            else :
                textsurface = myfont.render("J'ai déjà mon ticket", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                
        elif 125+screen_x < x < 215+screen_x and 438+screen_y < y < 553+screen_y and Gus.level == 5.4:
            if sac.Ticket == 0:
                tr.mach_tick2 = zone_interaction(screen,"Acheter un ticket (A)",action,tr.mach_tick2,"un ticket")
            else :
                textsurface = myfont.render("J'ai déjà mon ticket", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
            
        elif 225+screen_x < x < 320+screen_x and 450+screen_y < y < 550+screen_y and Gus.level == 5.4 :
            zone_dialogue(screen,"Parler (A)",action,phrases_controleur_5no[tr.controleur_5no],tr.controleur_5no,5)
            if tr.controleur_5no == 1 and tr.give_alcool_5 == False:
                textsurface = myfont.render("Donner de l'alcool", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40))
            if sac.Carte_Rare == 1 and tr.give_alcool_5 == True and tr.echange_tw == False :
                textsurface = myfont.render("Echanger la carte rare", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40))                
            
        elif 210+screen_x < x < 280+screen_x and 145+screen_y < y < 222+screen_y and Gus.level == 5.4 :
            zone_dialogue(screen,"Parler (A)",action,phrases_pnj_5no[tr.pnj_5no],tr.pnj_5no,5)
            if sac.Chargeur == 1 and tr.batt_tel_5no == False :
                textsurface = myfont.render("Recharger le téléphone", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40))                
            if sac.Chargeur == 0 and tr.batt_tel_5no == True and tr.cachets_5no == 2 and tr.give_cachets_5no == False:
                textsurface = myfont.render("Donner des cachets", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40))             
            
        #LEVEL OUEST
        elif 313+screen_x < x < 587+screen_x and 231+screen_y < y < 325+screen_y and Gus.level == 5.5 :
            textsurface = myfont.render("Voir le plan", False, (0, 0, 0))
            textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
            screen.blit(textsurface,(x,y-60))
            screen.blit(textsurface2,(x+35,y-40))
            
        elif 693+screen_x < x < 760+screen_x and 100+screen_y < y < 170+screen_y and Gus.level == 5.5 :
            tr.poub_5o = zone_interaction(screen,"Fouiller la poubelle (A)",action,tr.poub_5o,"une clé USB")
            sac.Cle_USB = 1
        
        #LEVEL SUD OUEST
        elif 195+screen_x < x < 260+screen_x and 585+screen_y < y < 675+screen_y and Gus.level == 5.6 :
            tr.press_seringue_5so = zone_interaction(screen,"Qu'est-ce que c'est ? (A)",action,tr.press_seringue_5so,"une seringue ! ")
            tr.seringue_5so = 1
        elif 345+screen_x < x < 430+screen_x and 130+screen_y < y < 210+screen_y and Gus.level == 5.6 :
            tr.distrib_5so = zone_interaction(screen,"Acheter un truc (A)",action,tr.distrib_5so,"un masque")
            sac.Masque = 1 
            tr.argent_mask = -0.5
        elif 586+screen_x < x < 677+screen_x and 250+screen_y < y < 305+screen_y and Gus.level == 5.6 :
            tr.poub_5so = zone_interaction(screen,"Fouiller la poubelle (A)",action,tr.poub_5so,"... Beurkkkk!!!")
        elif 550+screen_x < x < 675+screen_x and 614+screen_y < y < 675+screen_y and Gus.level == 5.6 :
            tr.sac_5so =  zone_interaction(screen,"Fouiller la poubelle (A)",action,tr.poub_5so,"de la mort aux rats")  
            sac.Mort_aux_rats = 1
        elif 395+screen_x < x < 524+screen_x and 595+screen_y < y < 672+screen_y and Gus.level == 5.6 :
            if sac.Cle_meuble == 1:
                tr.meuble_5so =  zone_interaction(screen,"Fouiller le meuble (A)",action,tr.meuble_5so,"un chargeur ! ") 
                sac.Chargeur = 1
            else :
                textsurface = myfont.render("C'est fermé", False, (220, 120, 0))
                textsurface2 = myfont.render("à clé !", False, (220, 120, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x,y-40))
        elif 170+screen_x < x < 255+screen_x and 350+screen_y < y < 430+screen_y and Gus.level == 5.6 :
            textsurface = myfont.render("C'est dégueu !", False, (0, 0, 0))
            screen.blit(textsurface,(x,y-60))
        elif 886+screen_x < x < 984+screen_x and 260+screen_y < y < 380+screen_y and Gus.level == 5.6 :
            if tr.tab_5so == -1:
                textsurface = myfont.render("Lire le tableau", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x-100,y-60))
                screen.blit(textsurface2,(x-65,y-40))  
            elif tr.tab_5so == 0:
                textsurface = myfont.render("Un concours de jongles", False, (0, 0, 0))
                textsurface2 = myfont.render("en ville ?", False, (0, 0, 0))
                screen.blit(textsurface,(x-120,y-60))
                screen.blit(textsurface2,(x-120,y-40))  
            
        elif 720+screen_x < x < 975+screen_x and 390+screen_y < y < 525+screen_y and Gus.level == 5.6 :
            zone_dialogue(screen,"Parler (A)",action,phrases_stand_5o[tr.pnj_stand_5so],tr.pnj_stand_5so,5) 
            if tr.give_mask == True and sac.Cachets != 0 and tr.validate == False:
                textsurface = myfont.render("Vendre un médicament", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x-100,y-60))
                screen.blit(textsurface2,(x-65,y-40))                 
            if tr.give_mask == True and sac.Cachets != 0 and tr.validate == True:
                textsurface = myfont.render("Tu es sûr ?", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x-100,y-60))
                screen.blit(textsurface2,(x-65,y-40))            
        #LEVEL CENTRE
        elif 346+screen_x < x < 492+screen_x and 60+screen_y < y < 150+screen_y and Gus.level == 5.7 :  
            if tr.caisse_occupee_5c == True :                
                tr.etag_5c2 =  zone_interaction(screen,"Voler un vêtement (A)",action,tr.etag_5c2,"des habits !")
                sac.Habits = 1
            elif tr.caisse_occupee_5c == False : 
                zone_dialogue(screen,"Voler un vêtement (A)",action,phrases_etagere[0],0,5) 
                
        elif 40+screen_x < x < 435+screen_x and 525+screen_y < y < 616+screen_y and Gus.level == 5.7 :
            tr.etag_5c1 =  zone_interaction(screen,"Fouiller le présentoire (A)",action,tr.etag_5c1,"les horaires du métro !")
            sac.Horaires_metro = 1
            
        elif 650+screen_x < x < 780+screen_x and 240+screen_y < y < 345+screen_y and Gus.level == 5.7 :
            zone_dialogue(screen,"Voler un vêtement (A)",action,phrases_etagere[1],0,5) 
            
        elif 834+screen_x < x < 935+screen_x and 60+screen_y < y < 190+screen_y and Gus.level == 5.7 :
            textsurface = myfont.render("Se cacher", False, (0, 0, 0))
            textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
            screen.blit(textsurface,(x-100,y-60))
            screen.blit(textsurface2,(x-65,y-40))
            
        elif 242+screen_x < x < 315+screen_x and 40+screen_y < y < 190+screen_y and Gus.level == 5.7:
            zone_dialogue(screen,"Parler (A)",action,phrases_caisse_5c[tr.caisse_5c],tr.caisse_5c,10)
            if sac.Ciseaux == 1 and tr.ordi_vendeuse == False :
                textsurface = myfont.render("Couper le câble internet", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40))  
                
            if tr.ordi_vendeuse == True and tr.recherche == False and Gus.savoir_info == True and sac.Carte_Mere == 1 and tr.caisse_occupee_5c == False:
                textsurface = myfont.render("Réparer le PC", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40))                 
            
        elif 730+screen_x < x < 834+screen_x and 86+screen_y < y < 167+screen_y and Gus.level == 5.7 :
            zone_dialogue(screen,"Parler (A)",action,phrases_mag_5c[tr.pnj_mag_5c],tr.pnj_mag_5c,5)

        elif 790+screen_x < x < 900+screen_x and 455+screen_y < y < 535+screen_y and Gus.level == 5.7 :
            zone_dialogue(screen,"Parler (A)",action,phrases_allee_5c[tr.pnj_allee_5c],tr.pnj_allee_5c,5)
            if tr.give_mask == True and tr.give_cachet_5c == False:    
                textsurface = myfont.render("Vendre un médicament", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x-100,y-60))
                screen.blit(textsurface2,(x-65,y-40)) 
            
        #LEVEL SUD
        elif 35+screen_x < x < 190+screen_x and 450+screen_y < y < 530+screen_y and Gus.level == 5.8 :
            zone_dialogue(screen,"Parler (A)",action,phrases_caisse_5s[tr.caisse_5s],tr.caisse_5s,5)
            
            if tr.pnj_stand_5so == 0 and sac.Contrat == 1 and sac.Stylo == 1 :
                textsurface = myfont.render("Donner un contrat ", False, (0, 0, 0))
                textsurface2 = myfont.render("et un stylo pour ", False, (0, 0, 0))
                textsurface3 = myfont.render("rejoindre l'armée ", False, (0, 0, 0))
                textsurface4 = myfont.render("ENTER ", False, (0, 0, 0))
                screen.blit(textsurface,(x-100,y-80))
                screen.blit(textsurface2,(x-100,y-60))
                screen.blit(textsurface3,(x-100,y-40)) 
                screen.blit(textsurface4,(x-65,y-20))  
            
        elif 813+screen_x < x < 900+screen_x and 379+screen_y < y < 460+screen_y and Gus.level == 5.8 :
            zone_dialogue(screen,"Parler (A)",action,phrases_jeu_5s[tr.pnj_jeu_5s],tr.pnj_jeu_5s,5)
            if tr.pnj_jeu_5s == 1 and sac.Jeu == 1:
                textsurface = myfont.render("Jouer au jeu", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x-100,y-60))
                screen.blit(textsurface2,(x-65,y-40)) 
                
        elif 840+screen_x < x < 940+screen_x and 30+screen_y < y < 130+screen_y and Gus.level == 5.8 :
            zone_dialogue(screen,"Parler (A)",action,phrases_vigil_5s[tr.vigil_5s],tr.vigil_5s,5)
            if tr.info_vol == True and tr.clodo_5m == 3 and tr.balance_5 == False:
                textsurface = myfont.render("Dénoncer le voleur", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x-100,y-60))
                screen.blit(textsurface2,(x-65,y-40))     
            if sac.Talkie_Walkie == 1 and tr.give_tw_5 == False:
                textsurface = myfont.render("Donner le talkie-walkie", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x-100,y-60))
                screen.blit(textsurface2,(x-65,y-40))                 
            
        elif 560+screen_x < x < 706+screen_x and 315+screen_y < y < 395+screen_y and Gus.level == 5.8 :
            tr.etag_5s =  zone_interaction(screen,"Fouiller l'étagère (A)",action,tr.etag_5s,"un stylo !")
            sac.Stylo = 1
            
        elif 485+screen_x < x < 650+screen_x and 400+screen_y < y < 480+screen_y and Gus.level == 5.8 :
            if tr.caisse_5s_occupe == True :
                tr.bac_5s = zone_interaction(screen,"Fouiller le bac (A)",action,tr.etag_5s,"un jeu-vidéo !")
                sac.Jeu = 1
            elif tr.caisse_5s_occupe == False :
                zone_dialogue(screen,"Fouiller le bac (A)",action,phrases_etagere[0],0,5)            

        #     if sac.Papier > 0 :
        #         textsurface = myfont.render("Réparer la machine", False, (0, 0, 0))
        #         textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
        #         screen.blit(textsurface,(x,y-60))
        #         screen.blit(textsurface2,(x+35,y-40)) 
                
        if screen_x >= 0 and rel_x > 0  and lvl_move:
            screen_x = 0
            x -= rel_x
        elif screen_x <= display_width - 1000 and rel_x < 0 and lvl_move :
            screen_x = display_width - 1000
            x -= rel_x
        if screen_y >= 0 and rel_y > 0 and lvl_move :
            screen_y = 0
            y  -= rel_y
        elif screen_y <= display_height - 707 and rel_y < 0 and lvl_move:
            screen_y = display_height - 707 
            y -= rel_y
            
        if x < (display_width-gugus_width)/2 and rel_x < 0 and lvl_move:
            screen_x = 0
            x -= rel_x
        elif x > (display_width-gugus_width)/2 and rel_x > 0 and lvl_move:
            screen_x = display_width - 1000
            x -= rel_x
            
        if y < (display_height-gugus_height)/2 and rel_y < 0 and lvl_move:
            screen_y = 0
            y -= rel_y
        elif y > (display_height-gugus_height)/2 and rel_y > 0 and lvl_move:
            screen_y = display_height - 707 
            y -= rel_y
        
        ##OBJETS
        
        if tr.disparu%2 != 1:
            screen.blit(gugus, rect_gugus)
        else :
            countdown = (timing+10)/60
            time_out = -(countdown-(time/60))
            temps = myfont.render("Attends 10 secondes : " + str(int(time_out)), False, (22, 22, 9))
            screen.blit(temps , (225,150))
            if tr.recherche == True and time_out >= 10:
                tr.recherche = False
        
        pv = Gus_font.render("Santé : " + str(Gus.pv), False, (78, 22, 9))
        argent = Gus_font.render("Argent : " + str(round(Gus.money,2)), False, (31, 160, 85))
        lvl = Gus_font.render("Niveau : " + str(int(Gus.level)), False, (78, 22, 9))
    
        screen.blit(pv , (10,20))
        screen.blit(lvl , (10,45))
        screen.blit(argent , (10,70))
        screen.blit(sac_tab , (10,450))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_TAB]:
            affich_sac(screen,sac)
        if (Gus.pause%2) == 1:
            pause(screen,gameExit,Gus,sac,tr)

        if tr.affich_plan%2 == 1:
            affichage_plan(screen,gameExit)
        if Gus.pv == 0 or tr.game_over == True:
            game_over(screen)

        pygame.display.update()
        
        clock.tick(100) 
        
def nivo_voiture (sac,action,Gus,tr) :
    
    gameExit=False
    
    x = 262.5
    x2 =237.5 
    
    y = 390
    y_back = 420
    
    move = 1
    nivo = 1
    score = 0
    nb_voiture = 0
    clean = 0
    life = 100
    
    accel = 0.009
    frein = 0
    turn =0
    time = 0
    angle = 0
    
    start_x = 0
    start_y = -500
    start_xr = 350
    
    pnj_car = voiture(0,liste_voit)
    pnj_car2 = voiture(-167,liste_voit)
    pnj_car3 = voiture(-333,liste_voit)
    pnj_car4 = voiture(-500,liste_voit)
    pnj_car5 = voiture(-500,liste_voit)
    pnj_car6 = voiture(-500,liste_voit)
    
    pnj_rect = pnj_car.image.get_rect()
    pnj_rect.topleft = (pnj_car.random_x,pnj_car.random_y)
    pnj_rect2 = pnj_car2.image.get_rect()
    pnj_rect2.topleft = (pnj_car2.random_x,pnj_car2.random_y)
    pnj_rect3 = pnj_car3.image.get_rect()
    pnj_rect3.topleft = (pnj_car3.random_x,pnj_car3.random_y)

    pnj_rect4 = pnj_car4.image.get_rect()
    pnj_rect4.topleft = (pnj_car4.random_x,pnj_car4.random_y)
    pnj_rect5 = pnj_car5.image.get_rect()
    pnj_rect5.topleft = (pnj_car5.random_x,pnj_car5.random_y)
    pnj_rect6 = pnj_car6.image.get_rect()
    pnj_rect6.topleft = (pnj_car6.random_x,pnj_car6.random_y)
    
    start_y_red = -1500
    
    clock = pygame.time.Clock()
    while not gameExit:
        
        if life > 0:
                
            if nivo == 1:
                v_max = 5
            elif nivo == 2:
                v_max = 6.5
            elif nivo == 3:
                v_max = 7
            elif nivo == 4:
                v_max = 7.5
            elif nivo == 5:
                v_max = 8
            elif nivo == 6:
                v_max = 8.5
            elif nivo == 7:
                v_max = 9
            elif nivo > 7:
                v_max = 9 + ((nivo-7)/2)
                
            if score > 1:
                nivo = int((clean+10)/10)
            else:
                nivo = 1
                
            if nivo == 1:
                liste_car=[pnj_car,pnj_car2,pnj_car3]
                liste_rect=[pnj_rect,pnj_rect2,pnj_rect3]
            elif 2 <= nivo < 5 :
                liste_car=[pnj_car,pnj_car2,pnj_car3,pnj_car4]
                liste_rect=[pnj_rect,pnj_rect2,pnj_rect3, pnj_rect4]
            elif 5 <= nivo < 10 :
                liste_car=[pnj_car,pnj_car2,pnj_car3,pnj_car4,pnj_car5]
                liste_rect=[pnj_rect,pnj_rect2,pnj_rect3, pnj_rect4, pnj_rect5]
            elif nivo >= 10:
                liste_car=[pnj_car,pnj_car2,pnj_car3,pnj_car4,pnj_car5,pnj_car6]
                liste_rect=[pnj_rect,pnj_rect2,pnj_rect3, pnj_rect4, pnj_rect5, pnj_rect6]
                
            time += 1
            ###VOITURE
            car = pygame.Surface((5, 10),pygame.SRCALPHA)
            car.fill((250,250,250))
            car2 = pygame.Surface((5, 10),pygame.SRCALPHA)
            car2.fill((250,250,250))
            
            car3 = pygame.Surface((5, 10),pygame.SRCALPHA)
            car3.fill((250,250,250))
            car4 = pygame.Surface((5, 10),pygame.SRCALPHA)
            car4.fill((250,250,250))
            
            body_rect = car_player.get_rect()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
            
            ###ACCEL ET DECEL
            keys=pygame.key.get_pressed()
            if keys[pygame.K_UP]and move == 0:
                move = 1
            elif keys[pygame.K_UP]and move != 0 and move <= v_max and 317.5 > x2 > 147.5:  
                accel = (np.sin((move*0.15)+7)+1)/20
                move += accel
            elif keys[pygame.K_UP]and (317.5 < x2 or x2 < 147.5):  
                if move > 0 :
                    move -= ((move**5)**(-1/4))
                    
                elif move <= 0:
                    move = 0
                
            elif keys[pygame.K_DOWN]:
                if move > 0:
                    frein += 0.002
                    move -= ((move**12)**(-1/4)) + frein
                elif move <= 0:
                    accel = (np.sin((move*0.15)+7)+1)/20
                    move = 0
                    
            elif not keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
                if move > 0 :
                    move -= ((move**12)**(-1/4))
                    
                elif move <= 0:
                    move = 0
                
            ###TURN MARCHE AVANT
            if keys[pygame.K_LEFT] and move > 0 and 60 < x and angle < 25:
                angle += 0.75
                move *= 0.9995
                if angle >= 0:
                    turn = -2
                else:
                    turn = 0
            elif keys[pygame.K_LEFT] and move > 0 and 60 < x and angle >=25:
                angle += 0
                move *= 0.9995
                if angle >= 0:
                    turn = -2
                else:
                    turn = 0
                    
            elif keys[pygame.K_RIGHT] and move > 0 and x < 490 and angle > -25:
                angle -= 0.75
                move *= 0.9995
                if angle <= 0:
                    turn = 2
                else:
                    turn = 0
            elif keys[pygame.K_RIGHT] and move > 0 and x < 490 and angle <= -25:
                angle -= 0
                move *= 0.9995
                if angle <= 0:
                    turn = 2
                else:
                    turn = 0
                    
            ###TURN MARCHE ARRIERE
            
            elif keys[pygame.K_LEFT] and move < 0 and 60 < x:
                angle -= 0.75
                move *= 0.9995
                if angle >= 0:
                    turn = -2
                else:
                    turn = 0
            elif keys[pygame.K_RIGHT] and move < 0 and x < 490:
                angle += 0.75
                move *= 0.9995
                if angle <= 0:
                    turn = 2
                else:
                    turn = 0
            
            else:
                turn = 0
                if angle > 0:
                        angle -= 1.25
                elif angle < 0:
                        angle += 1.25
                        
            ###UNTURN
    
            if keys[pygame.K_RIGHT] and angle > 0:
                angle -= 1.5    
    
            if keys[pygame.K_LEFT] and angle < 0:
                angle += 1.5
            
            ###MOVE CAR
                
            if y > 350 :
                y -= move
    
            else:
                start_y += move
                start_y_red += move
    
            if y_back > 380:
                y_back -= move  
            
            if start_y + move >= 500 :
                start_y = -1500  
            if start_y_red + move >= 500 :
                start_y_red = -1500   
    
            ###BORDER
            if x > 0 or x < 490 and x2 > 0 or x2 < 430:
                x += turn
                x2 += turn
            elif x <= 25 and x2 <= 0:
                x = 60
                x2 =0
            elif x >= 490 and x2 >= 430:
                x = 490          
                x2 = 430
                
            ###TALUS
            if x2 < 147.5 or x > 347.5 :
                score -= 10 * nivo
                
            screen.fill((0,0,0))
    
            screen.blit(route,(0,start_y))
            screen.blit(route,(0,start_y_red))
            
            car = pygame.transform.rotate(car,angle)
            car2 = pygame.transform.rotate(car2,angle)             
            
            screen.blit(car,(x,y))
            screen.blit(car2,(x2,y))
                
            screen.blit(car3,(x,y_back))
            screen.blit(car4,(x2,y_back))
            
            body_rect.topleft = (x2+2.5,y-3)
            screen.blit(car_player,body_rect)
            
            if move <= 0 :
                nivo = 1
                clean = 0
                
            ###COLLISIONS
            for elt in liste_car:
                if elt.random_x - 30 < (x2) < elt.random_x + 30  and abs((elt.random_y + 40) - (y-3)) <= 1 and move != 0 and time >= 100:
                        score -= 100
                        move = 0
                        clean = 0
                        life -= 20                       
                        time = 0
                if (abs(elt.random_x + 30 - x2) <= 1  and elt.random_y - 46 < y < elt.random_y + 40) or (abs(elt.random_x - x + 5) <= 1  and elt.random_y - 46 < y < elt.random_y + 40):
                        score -= 20
                        move = 0
                        turn *= -1
                        clean = 0
                        life -= 0.05                    
                if elt.random_x - 50 < (x2 + 2.5) < elt.random_x + 30  and abs((elt.random_y) - (y+27)) <= 1 and move != 0:
                        score += 20
                        life -= 5

            ###DOUBLER LES PNJ
            for elt in liste_car:
                
                if elt.random_y > 500:
                    elt.random_x = random.randint(150,320)
                    elt.random_y = random.randint(-100, -40)
                    elt.nb = random.randint(0,6)
                    elt.image = liste_voit[elt.nb]
                    nb_voiture += 1
                    clean += 1
                    score += 100 * (move/(v_max*0.9)) * nivo
                    
                if move >= 15:
                   elt.random_y += move - 7
                elif 12 < move < 15:
                   elt.random_y += move - 6
                elif 9 < move < 12:
                   elt.random_y += move - 5
                elif 6 < move < 9:
                   elt.random_y += move - 4
                elif 0 < move < 6:
                   elt.random_y += move - 3
                elif move == 0:
                   elt.random_y += move
                
                for rect in liste_rect:
                    rect.topleft = (elt.random_x,elt.random_y)
                    screen.blit(elt.image,rect)
                
            vitesse = str(round(move*20,1))
            
            points = str(int(score))
            multi = str(int(nivo))
            
            vie = str(int(life))
            
            titre = myfont.render("Speed", False, (21, 21, 21))
            titre4 = myfont.render("Life", False, (21, 21, 21))
            titre2 = myfont.render("Score", False, (21, 21, 21))
            titre3 = myfont.render("Multiplier", False, (21, 21, 21))
            score_battre = myfont.render("Score à battre : 40 000", False, (180, 180, 180))
            
            textsurface = myfont.render(vitesse, False, (21, 21, 21))
            textsurface2 = myfont.render(points, False, (21, 21, 21))
            textsurface4 = myfont.render(vie, False, (21, 21, 21))
            textsurface3 = myfont.render(multi, False, (21, 21, 21))
            
            screen.blit(titre,(20,20))
            screen.blit(titre2,(20,52))
            screen.blit(titre4,(420,20))
            screen.blit(titre3,(420,52))
            screen.blit(score_battre,(180,20))
            
            screen.blit(textsurface,(20,35))
            screen.blit(textsurface2,(20,65))
            screen.blit(textsurface4,(420,35))
            screen.blit(textsurface3,(420,65))

        ###FIN JEU        
        elif life <= 0:
            tr.score_voiture = int(score)
            
            if tr.score_voiture <= 40000 :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                    
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            nb_voiture = 0
                            score = 0
                            nivo = 1
                            move = 0
                            clean = 0
                            life = 100
                            for elt in liste_car:
                                elt.random_y -= 500
                            x = 262.5
                            x2 =237.5 
        
                            y = 390
                            y_back = 420

                        if event.key == pygame.K_RETURN:
                            gameExit = True
                            Gus.level = 5.8
                            Gus.spawn = 3
                            
                end_game(points,replay = True)
                
            elif tr.score_voiture > 40000:
                gameExit = True
                Gus.level = 5.8
                Gus.spawn = 3
                

        pygame.display.update()
        
        clock.tick(100)             


def nivo6(sac,action,Gus,tr):
    pygame.init()
    speed_move = Gus.speed
    frame_count = Gus.frame
    lvl_move = True
    interact = False
    a=0
    time = 0
    x =  (display_width-gugus_width)/2
    y = (display_height-gugus_height)/2  
    rel_x = 0 
    rel_y = 0
    x_change = 0
    y_change = 0
    gugus = gugus_face
    
    screen_x = -225 + x
    screen_y = -225 + y 
    
    jeu_voit = False
    tune = Gus.money
    alcool = sac.Alcool
    preservatif = sac.Capote
    #CREATION ET CARACTERISTIQUES PNJ  
    ca_touche = False
    
    move = 4
    front_car_x = 173 
    front_car = voiture(0,liste_car_front)    
    pnj_front_rect = front_car.image.get_rect()
    pnj_front_rect.topleft = (front_car_x,front_car.random_y)


    back_car_x = 300 
    back_car = voiture(0,liste_car_back)    
    pnj_back_rect = back_car.image.get_rect()
    pnj_back_rect.topleft = (back_car_x,300)
        
    #INTERACTIONS

    #OBJETS NIVEAU
    #INTERACTIONS
    
    gameExit = False
    
    while not gameExit and Gus.level >= 6 and Gus.level < 7:
        
        liste_car=[front_car]
        liste_rect=[pnj_front_rect]
        liste_back_car=[back_car]
        liste_back_rect=[pnj_back_rect]
        
        liste_voiture = [pnj_front_rect,pnj_back_rect]

        if not pygame.mixer.music.get_busy() and Gus.current <= len(playlist):
            Gus.current+=1
            pygame.mixer.music.load ( playlist[Gus.current])
            pygame.mixer.music.play()
        elif not pygame.mixer.music.get_busy() and Gus.current > len(playlist):
            Gus.current=0
            pygame.mixer.music.load ( playlist[Gus.current])
            pygame.mixer.music.play()
                    
        if frame_count <= 30:
            frame_count += 1
        else:
            frame_count = 0
        
        if frame_count <= 15:
            a=0
        elif frame_count > 15:
            a=1
            
        rect_gugus = gugus.get_rect() 
        tr.update_items()
        Gus.update_items(tr)
        sac.update_items(tr)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    other_s.play()
                    Gus.pause += 1    
                if event.key == pygame.K_TAB:
                    other_s.play() 
            ############################
            if event.type == pygame.KEYDOWN and tr.game_over == False :

                if event.key == pygame.K_LEFT:  
                    x_change = -speed_move
                    rel_x = speed_move
                    y_change = 0
                    rel_y = 0
                    step_s.play(-1)
                elif event.key == pygame.K_RIGHT:
                    x_change = speed_move
                    rel_x = -speed_move
                    y_change = 0
                    rel_y = 0
                    step_s.play(-1)
                elif event.key == pygame.K_UP:
                    y_change = -speed_move
                    rel_y = speed_move
                    x_change = 0
                    rel_x = 0
                    step_s.play(-1)
                elif event.key == pygame.K_DOWN:
                    y_change = speed_move
                    rel_y = -speed_move
                    x_change = 0
                    rel_x = 0
                    step_s.play(-1)
                if event.key == pygame.K_a and not action.click:
                    action.click = True
                    click_.play()
                    
                    # 5 METRO
                    # if 0+screen_x < x < 94+screen_x and 240+screen_y < y < 300+screen_y and Gus.level == 5 and sac.Soda < 2:
                    #      tr.press_mach1 += 1 
                    
                elif event.key != pygame.K_a:
                
                    action.click = False
                
                if event.key == pygame.K_RETURN:
                    enter_s.play()
                    if 706+screen_x < x < 767+screen_x and 286+screen_y < y < 343+screen_y and Gus.level == 6.4:
                        Gus.spawn = 3
                        time = 0
                        
                    if 700+screen_x < x < 790+screen_x and 575+screen_y < y < 660+screen_y and Gus.level == 6.4:
                        Gus.spawn = 2
                        time = 0

                            
                elif event.key != pygame.K_RETURN:
                
                    action.change_level = False
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_change = 0
                    rel_x = 0
                    gugus = gugus_gauche 
                    step_s.stop()
                if event.key == pygame.K_RIGHT:
                    x_change = 0
                    rel_x = 0
                    gugus = gugus_droite 
                    step_s.stop()

                if event.key == pygame.K_UP:
                    y_change = 0
                    rel_y = 0
                    gugus = gugus_dos 
                    step_s.stop()
                    
                if event.key == pygame.K_DOWN:
                    y_change = 0
                    rel_y = 0
                    gugus = gugus_face 
                    step_s.stop()
                    
            ######################            
        keys=pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            gugus=gugus_walkdown[a]
        if keys[pygame.K_UP]:
            gugus=gugus_walkup[a]
        if keys[pygame.K_RIGHT]:
            gugus=gugus_walkright[a]
        if keys[pygame.K_LEFT]:
            gugus=gugus_walkleft[a]
            
        rect_gugus.topleft = (x,y)
                        
        if Gus.level == 6:
            
            lvl_move = False
    
            if Gus.spawn == 1 and time < 2:
                screen_x,screen_y,x,y = spawn_level(x,y,50,50)
            elif Gus.spawn == 2 and time < 2:
                screen_x,screen_y,x,y = spawn_level(x,y,980,100)
        
            time += 1
            liste_mur = level_6O(screen,screen_x,screen_y)
            
            x_change,y_change,rel_x,rel_y = collisions(liste_mur,rect_gugus,x_change,y_change,speed_move,rel_x,rel_y)

            ###COLLISIONS
            ###DOUBLER LES PNJ
                    
            for elt in liste_voiture:
                if elt.colliderect(rect_gugus):
                    if abs (elt.left - rect_gugus.right) <= 5:
                        move = 0
                        ca_touche = True
                        
                if elt.colliderect(rect_gugus):
                    if abs (elt.right - rect_gugus.left) <= 5:
                        move = 0
                        ca_touche = True
                        
                if rect_gugus.colliderect(elt):
                    if abs (elt.left - rect_gugus.right) <= 5:
                        move = 0
                        ca_touche = True
                        
                if rect_gugus.colliderect(elt):
                    if abs (elt.right - rect_gugus.left) <= 5:
                        move = 0
                        ca_touche = True
                        
            for elt in liste_car:
                
                if elt.random_y > 500:
                    elt.random_y = random.randint(-100, -40)
                    elt.nb = random.randint(0,6)
                    elt.image = liste_car_front[elt.nb]
                    
                elt.random_y += move 
                
                for rect in liste_rect:
                    rect.topleft = (front_car_x,elt.random_y)
                    screen.blit(elt.image,rect)

            for elt in liste_back_car:
                
                if elt.random_y < -200:
                    elt.random_y = random.randint(500, 540)
                    elt.nb = random.randint(0,6)
                    elt.image = liste_car_back[elt.nb]
                    
                elt.random_y -= move 
                
                for rect in liste_back_rect:
                    rect.topleft = (back_car_x,elt.random_y)
                    screen.blit(elt.image,rect)
                    
            x -= rel_x
            y -= rel_y
            
            if x > 490 :
                Gus.level = 6.1
                Gus.spawn = 1
                time = 0
                
            
        elif Gus.level == 6.1:
            
            lvl_move = True
            
            if Gus.spawn == 1 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,41,621)

            if Gus.spawn == 2 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,950,621)
                        
            time += 1
            
            liste_mur = level_6_1(screen,screen_x,screen_y)
        
            x_change,y_change,rel_x,rel_y = collisions(liste_mur,rect_gugus,x_change,y_change,speed_move,rel_x,rel_y) 
            
            screen_x += rel_x
            screen_y += rel_y
            
            if x > 495 :
                Gus.level = 6.2
                Gus.spawn = 1
                time = 0
            if x < 0:
                Gus.level = 6
                Gus.spawn = 2
                time = 0            

        elif Gus.level == 6.2:
            
            lvl_move = True
            
            if Gus.spawn == 1 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,41,621)

            if Gus.spawn == 2 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,941,621)
                        
            time += 1
            
            liste_mur = level_6_2(screen,screen_x,screen_y)
        
            x_change,y_change,rel_x,rel_y = collisions(liste_mur,rect_gugus,x_change,y_change,speed_move,rel_x,rel_y) 
            
            pnj_tp = tp[a]
            rect_tp = pnj_tp.get_rect()
            rect_tp.topleft=(429+screen_x,541+screen_y)
                  
            if rect_gugus.colliderect(rect_tp) and x_change > 0:
                if abs (rect_tp.left - rect_gugus.right) <= 10:
                    x_change = 0
                    rel_x = 0
            if rect_gugus.colliderect(rect_tp) and x_change < 0:
                if abs (rect_tp.right - rect_gugus.left) <= 10:
                    x_change = 0
                    rel_x = 0   
            if rect_gugus.colliderect(rect_tp) and y_change < 0:
                if abs (rect_tp.bottom - rect_gugus.top) <= 10:
                    y_change = 0
                    rel_y = 0
                    interact = True                    
            if rect_gugus.colliderect(rect_tp) and y_change > 0:
                if abs (rect_tp.top - rect_gugus.bottom) <= 10:
                    y_change = 0
                    rel_y = 0  
            if not rect_gugus.colliderect(rect_tp):
                interact = False       
                
            screen_x += rel_x
            screen_y += rel_y

            screen.blit(pnj_tp, rect_tp)
            
            if x > 460 :
                Gus.level = 6.3
                Gus.spawn = 1
                time = 0
            if x < 0:
                Gus.level = 6.1
                Gus.spawn = 2
                time = 0  
                
        if Gus.level == 6.3:
            
            lvl_move = False
    
            if Gus.spawn == 1 and time < 2:
                screen_x,screen_y,x,y = spawn_level(x,y,50,635)
            elif Gus.spawn == 2 and time < 2:
                screen_x,screen_y,x,y = spawn_level(x,y,700,115)
        
            time += 1
            
            liste_mur = level_6_3_avec(screen,screen_x,screen_y)
            
            x_change,y_change,rel_x,rel_y = collisions(liste_mur,rect_gugus,x_change,y_change,speed_move,rel_x,rel_y)

            x -= rel_x
            y -= rel_y
            
            if y < 110 :
                Gus.level = 6.4
                Gus.spawn = 1
                time = 0
                gugus = gugus_droite
            if x < 0 :
                Gus.level = 6.2
                Gus.spawn = 2
                time = 0
                
        elif Gus.level == 6.4:
            
            lvl_move = True
            
            if Gus.spawn == 1 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,55,351)

            if Gus.spawn == 2 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,725,284)
                
            if Gus.spawn == 3 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,721,611)
                        
            time += 1
            
            liste_mur = level_6_4_avec(screen,screen_x,screen_y)
        
            x_change,y_change,rel_x,rel_y = collisions(liste_mur,rect_gugus,x_change,y_change,speed_move,rel_x,rel_y) 
                
            screen_x += rel_x
            screen_y += rel_y
            
            if x < 25:
                Gus.level = 6.3
                Gus.spawn = 2
                time = 0
            if y > 500:
                Gus.level = 6.5
                Gus.spawn = 1
                time = 0                 

        elif Gus.level == 6.5:
            
            lvl_move = True
            
            if Gus.spawn == 1 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,650,50)

            if Gus.spawn == 2 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,100,621)
                        
            time += 1
            
            liste_mur = level_6_5(screen,screen_x,screen_y)
        
            x_change,y_change,rel_x,rel_y = collisions(liste_mur,rect_gugus,x_change,y_change,speed_move,rel_x,rel_y) 
                
            screen_x += rel_x
            screen_y += rel_y
            
            if y < 0:
                Gus.level = 6.4
                Gus.spawn = 3
                time = 0
            # if y > 700:
            #     Gus.level = 6.5
            #     Gus.spawn = 1
            #     time = 0  

        #LEVEL  METRO
        # if 0+screen_x < x < 94+screen_x and 240+screen_y < y < 300+screen_y and Gus.level == 5 and sac.Soda < 2:
        #     tr.press_mach1 = zone_interaction(screen,"Acheter un truc (A)",action,tr.press_mach1,"une bouteille de soda")

            
        # elif 39+screen_x < x < 91+screen_x and 363+screen_y < y < 435+screen_y and Gus.level == 5 :
        #     zone_dialogue(screen,"Parler à la dame (A)",action,phrases_dame_5m[tr.dame_5m],tr.dame_5m,5)
        #     if sac.Habits == 1 and tr.donne_habits == False:
        #         zone_dialogue(screen,"Parler à la dame (A)",action,phrases_dame_5m[tr.dame_5m],tr.dame_5m,5)
        #         textsurface = myfont.render("Donner les habits", False, (0, 0, 0))
        #         textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
        #         screen.blit(textsurface,(x,y-60))
        #         screen.blit(textsurface2,(x+35,y-40))

        if 706+screen_x < x < 767+screen_x and 286+screen_y < y < 343+screen_y and Gus.level == 6.4:
            textsurface = myfont.render("Descendre les escaliers", False, (0, 0, 0))
            textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
            screen.blit(textsurface,(x,y-60))
            screen.blit(textsurface2,(x+35,y-40))
            
        elif 700+screen_x < x < 790+screen_x and 575+screen_y < y < 645+screen_y and Gus.level == 6.4:
            textsurface = myfont.render("Monter sur le toit", False, (0, 0, 0))
            textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
            screen.blit(textsurface,(x,y-60))
            screen.blit(textsurface2,(x+35,y-40))           

                
        if screen_x >= 0 and rel_x > 0  and lvl_move:
            screen_x = 0
            x -= rel_x
        elif screen_x <= display_width - 1000 and rel_x < 0 and lvl_move :
            screen_x = display_width - 1000
            x -= rel_x
        if screen_y >= 0 and rel_y > 0 and lvl_move :
            screen_y = 0
            y  -= rel_y
        elif screen_y <= display_height - 707 and rel_y < 0 and lvl_move:
            screen_y = display_height - 707 
            y -= rel_y
            
        if x < (display_width-gugus_width)/2 and rel_x < 0 and lvl_move:
            screen_x = 0
            x -= rel_x
        elif x > (display_width-gugus_width)/2 and rel_x > 0 and lvl_move:
            screen_x = display_width - 1000
            x -= rel_x
            
        if y < (display_height-gugus_height)/2 and rel_y < 0 and lvl_move:
            screen_y = 0
            y -= rel_y
        elif y > (display_height-gugus_height)/2 and rel_y > 0 and lvl_move:
            screen_y = display_height - 707 
            y -= rel_y
        
        ##OBJETS
        screen.blit(gugus, rect_gugus)
        
        pv = Gus_font.render("Santé : " + str(Gus.pv), False, (78, 22, 9))
        argent = Gus_font.render("Argent : " + str(round(Gus.money,2)), False, (31, 160, 85))
        lvl = Gus_font.render("Niveau : " + str(int(Gus.level)), False, (78, 22, 9))
    
        screen.blit(pv , (10,20))
        screen.blit(lvl , (10,45))
        screen.blit(argent , (10,70))
        screen.blit(sac_tab , (10,450))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_TAB]:
            affich_sac(screen,sac)
        if (Gus.pause%2) == 1:
            pause(screen,gameExit,Gus,sac,tr)

        if Gus.pv == 0 or tr.game_over == True:
            game_over(screen)
        if ca_touche == True :
            game_over(screen)
            
        pygame.display.update()
        print(y)
        clock.tick(100) 
        
        
        
