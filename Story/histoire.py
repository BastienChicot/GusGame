# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 13:28:37 2021

@author: basti
"""
import pygame
from Story.Fonctions import *
from Level.Levels import *
from settings import *

pygame.init()
pygame.font.init()


myfont = pygame.font.SysFont('corbel', 20, bold=True)
Gus_font = pygame.font.SysFont('corbel', 16, bold=True)

screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Gus veut boire un coup')

clock = pygame.time.Clock()


def nivo1(sac,action,Gus):
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
    pressed_salon = -1
    pressed_mom = -1
    pressed_dad = -1
    pressed_cuisine1 = -1
    pressed_cuisine2 = -1
    pressed_cuisine3 = -1
    pressed_four = -1
    pressed_sdb1 = -1
    pressed_frigo = -1 
    fouille = -1
    pressed_ch = -1
    pressed_couloir = -1
    pressed_arm_mom = -1
    pressed_entre = -1
    pressed_sdb2 = -1
    pressed_cleb = -1
    pressed_papier = -1 
    pressed_tune_buro = -1
    pressed_tune_entre = -1 
    pressed_couloir2 = -1
    pressed_buro = -1
    pressed_tune_ch = -1
    pressed_sortie = -1
    
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
    bouteille_alc = 0
    tune_buro = 0
    tune_entre = 0
    tune_ch = 0
    
    capote_buro = 0
    capote_entree = 0
        
    gameExit = False
    
    while not gameExit and Gus.level == 1:
        
        if frame_count <= 30:
            frame_count += 1
        else:
            frame_count = 0
        
        if frame_count <= 15:
            a=0
        elif frame_count > 15:
            a=1
            
        sac.Capote = capote_buro + capote_entree
        sac.Alcool = biere + bouteille_alc
        sac.Torchon = torchon_salon+torchonsdb1+torchoncoul+torchonch+torchon_entre+torchon_mom
        Gus.money = round(tune_buro + tune_entre + tune_ch,2)
        
        if open_buro == False and porte_entre == False :
            liste_mur = level_1(screen,screen_x,screen_y)
        if open_buro == True and porte_entre == False :
            liste_mur = level_1_2(screen,screen_x,screen_y)
        if open_buro == True and porte_entre == True :
            liste_mur = level_1_3(screen,screen_x,screen_y)
        if open_buro == False and porte_entre == True :
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
                    if 0+screen_x < x < 75+screen_x and 0+screen_y < y < 100+screen_y and sac.soupe_chaude == 0 and service == False and mom_sleep == False:
                        pressed_mom = 0
                        pressed_dad = -1
                    if 0+screen_x < x < 75+screen_x and 0+screen_y < y < 100+screen_y and sac.soupe_chaude == 1 and service == False and mom_sleep == False:
                        pressed_mom = 1
                        pressed_dad = -1
                    if 0+screen_x < x < 75+screen_x and 0+screen_y < y < 100+screen_y and service == True:
                        pressed_mom = 2
                        pressed_dad = -1
                        mom_sleep = True
                    if 170+screen_x < x < 210+screen_x and 378+screen_y < y < 440+screen_y and biere == 0:
                        pressed_dad += 1
                        service = False
                    if 170+screen_x < x < 210+screen_x and 378+screen_y < y < 440+screen_y and biere == 1 and pressed_mom>=1 and dad_sleep == False:
                        pressed_dad += 1
                        service = True
                    if 170+screen_x < x < 210+screen_x and 378+screen_y < y < 440+screen_y and papa_fouillab == True :
                        fouille += 1
                        
                    #OBJETS
                    if 612+screen_x < x < 670+screen_x and 457+screen_y < y < 540+screen_y:
                        pressed_sdb2 += 1
                    if 235+screen_x < x < 295+screen_x and 480+screen_y < y < 530+screen_y :
                        pressed_salon += 1
                    if 610+screen_x < x < 660+screen_x and 155+screen_y < y < 230+screen_y :
                        pressed_ch += 1
                    if 440+screen_x < x < 488+screen_x and 65+screen_y < y < 140+screen_y :
                        pressed_couloir += 1
                    if 550+screen_x < x < 590+screen_x and 370+screen_y < y < 550+screen_y :
                        pressed_sdb1 += 1
                    if 530+screen_x < x < 615+screen_x and 610+screen_y < y < 700+screen_y :
                        pressed_entre += 1
                    if 300+screen_x < x < 400+screen_x and 20+screen_y < y < 110+screen_y and mom_sleep == True :
                        pressed_arm_mom += 1
                    if 270+screen_x < x < 340+screen_x and 510+screen_y < y < 560+screen_y :
                        pressed_cuisine1 += 1  
                    if 240+screen_x < x < 300+screen_x and 580+screen_y < y < 680+screen_y :
                        pressed_cuisine2 += 1
                    if 341+screen_x < x < 410+screen_x and 510+screen_y < y < 560+screen_y and sac.soupe_froide == 0 and sac.soupe_chaude == 0:
                        pressed_four = -1
                    if 341+screen_x < x < 410+screen_x and 510+screen_y < y < 560+screen_y and sac.soupe_froide == 1 and sac.soupe_chaude == 0:
                        pressed_four = 0
                    if 270+screen_x < x < 335+screen_x and 600+screen_y < y < 680+screen_y and sac.soupe_chaude == 1:
                        pressed_four = 1
                    if 230+screen_x < x < 270+screen_x and 560+screen_y < y < 630+screen_y :
                        pressed_frigo +=1     
                    if 416+screen_x < x < 490+screen_x and 610+screen_y < y < 690+screen_y :
                        pressed_cleb = 0
                        Gus.pv -= 1
                    if 84+screen_x < x < 144+screen_x and 516+screen_y < y < 580+screen_y or 626+screen_x < x < 700+screen_x and 269+screen_y < y < 340+screen_y or 260+screen_x < x < 350+screen_x and 230+screen_y < y < 300+screen_y:
                        pressed_papier = 0
                    if 90+screen_x < x < 180+screen_x and 200+screen_y < y < 260+screen_y :   
                        pressed_tune_buro += 1
                    if 595+screen_x < x < 670+screen_x and 570+screen_y < y < 656+screen_y :
                        pressed_tune_entre += 1
                    if 350+screen_x < x < 400+screen_x and 600+screen_y < y < 670+screen_y :
                        pressed_cuisine3 = 0
                    if 430+screen_x < x < 500+screen_x and 330+screen_y < y < 430+screen_y :
                        pressed_couloir2 += 1
                    if 10+screen_x < x < 118+screen_x and 260+screen_y < y < 320+screen_y :
                        pressed_buro += 1
                    if 200+screen_x < x < 234+screen_x and 95+screen_y < y < 170+screen_y :
                        pressed_tune_ch += 1
                    if 920+screen_x < x < 1000+screen_x and 0+screen_y < y < 100+screen_y :
                        pressed_sortie += 1
                        
                elif event.key != pygame.K_a:
                
                    action.click = False

                if event.key == pygame.K_RETURN and not action.change_level:
                    action.change_level = True
                    enter_s.play()
                    if 560+screen_x < x < 650+screen_x and 0+screen_y < y < 30+screen_y and sac.Torchon >= 5:
                        Gus.level = 2  
                        Gus.spawn = 1
                        time = 0
                    elif 560+screen_x < x < 650+screen_x and 0+screen_y < y < 30+screen_y and sac.Torchon == 4:
                        Gus.level = 2.2
                        Gus.spawn = 4
                        Gus.pv -= 20
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
        if pressed_tune_buro >= 0:
            tune_buro = 0.1  
        if pressed_tune_entre >= 0:
            tune_entre = 0.05
        if pressed_tune_ch >= 0:
            tune_ch = 0.2
        if pressed_buro >= 0:
            capote_buro = 1        
        if pressed_sortie >= 0:
            capote_entree = 1
            
        if pressed_frigo == 0 :
            biere = 1
        
        if pressed_sdb2 == 0:
            bouteille_alc = 1
            
        ##DIALOGUESs
        if 0+screen_x < x < 75+screen_x and 0+screen_y < y < 100+screen_y :
    
            zone_dialogue(screen,"Parler à maman (A)",action,phrases_maman[pressed_mom],pressed_mom,3)
            
        elif 170+screen_x < x < 210+screen_x and 378+screen_y < y < 440+screen_y and sac.soupe_froide == 0 and sac.soupe_chaude == 0 and service == False and pressed_mom == -1 and papa_fouillab == False:
            
            zone_dialogue(screen,"Parler à papa (A)",action,phrases_papa_avant_soupe[pressed_dad],pressed_dad,2)
        
        elif 170+screen_x < x < 210+screen_x and 378+screen_y < y < 440+screen_y and sac.soupe_froide == 1 and sac.soupe_chaude == 0 and service == False and pressed_mom == 0 and papa_fouillab == False:
            
            zone_dialogue(screen,"Parler à papa (A)",action,phrases_papa_entre_soupe[pressed_dad],pressed_dad,2)

        elif 170+screen_x < x < 210+screen_x and 378+screen_y < y < 440+screen_y and  sac.soupe_chaude == 1 and service == False and pressed_mom >= 1 and papa_fouillab == False:
            
            zone_dialogue(screen,"Parler à papa (A)",action,phrases_papa_post_soupe[pressed_dad],pressed_dad,2)

        elif 170+screen_x < x < 210+screen_x and 378+screen_y < y < 440+screen_y and service == True and papa_fouillab == False:
            
            zone_dialogue(screen,"Parler à papa (A)",action,sleep[0],pressed_dad,2)
            dad_sleep = True
            sac.soupe_froide = 0 
            sac.soupe_chaude = 0
        
        elif 170+screen_x < x < 210+screen_x and 378+screen_y < y < 440+screen_y and papa_fouillab == True:

            fouille = zone_interaction(screen,"Fouiller papa (A)",action,fouille,"la clé de la maison!")
            sac.Cle_maison = 1  
            mom_sleep == True  
            biere = 0                                                                                     
            
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
            
            pressed_couloir2 = zone_interaction(screen,"Fouiller le placard (A)",action,pressed_couloir2,"un briquet!")
            sac.Briquet = 1

        elif 10+screen_x < x < 118+screen_x and 260+screen_y < y < 320+screen_y :

            pressed_buro = zone_interaction(screen,"Fouiller le placard (A)",action,pressed_buro,"un drôle de truc.")

        elif 920+screen_x < x < 1000+screen_x and 0+screen_y < y < 100+screen_y :
            
            pressed_sortie = zone_interaction(screen,"Regarder par terre (A)",action,pressed_sortie,"un drôle de truc.")

        elif 200+screen_x < x < 234+screen_x and 95+screen_y < y < 170+screen_y :
            
            pressed_tune_ch = zone_interaction(screen,"Fouiller le meuble (A)",action,pressed_tune_ch,"20 centimes")
            
        elif 350+screen_x < x < 400+screen_x and 600+screen_y < y < 670+screen_y :

            zone_dialogue(screen,"Fouiller le meuble (A)",action,phrases_cuisine[pressed_cuisine3],pressed_cuisine3,1)

        elif 612+screen_x < x < 670+screen_x and 457+screen_y < y < 540+screen_y :

            pressed_sdb2 = zone_interaction(screen,"Fouiller le placard (A)",action,pressed_sdb2,"une bouteille d'alcool")
        
        elif 90+screen_x < x < 180+screen_x and 200+screen_y < y < 260+screen_y :

            pressed_tune_buro = zone_interaction(screen,"Fouiller le bureau (A)",action,pressed_tune_buro,"10 centimes.")

        elif 595+screen_x < x < 670+screen_x and 570+screen_y < y < 656+screen_y :

            pressed_tune_entre = zone_interaction(screen,"Fouiller le meuble (A)",action,pressed_tune_entre,"5 centimes.")

        elif 416+screen_x < x < 490+screen_x and 610+screen_y < y < 690+screen_y :

            zone_dialogue(screen,"Caresser le chien (A)",action,phrases_cleb[pressed_cleb],pressed_cleb,1)

        elif 84+screen_x < x < 144+screen_x and 516+screen_y < y < 580+screen_y or 626+screen_x < x < 700+screen_x and 269+screen_y < y < 340+screen_y or 260+screen_x < x < 350+screen_x and 230+screen_y < y < 300+screen_y:

            zone_dialogue(screen,"Fouiller ici (A)",action,phrases_papier[pressed_papier],pressed_papier,1)

        elif 235+screen_x < x < 295+screen_x and 480+screen_y < y < 530+screen_y :

            pressed_salon = zone_interaction(screen,"Fouiller l'armoire (A)",action,pressed_salon,"un torchon")

        elif 610+screen_x < x < 660+screen_x and 155+screen_y < y < 230+screen_y :

            pressed_ch = zone_interaction(screen,"Fouiller l'armoire (A)",action,pressed_ch,"un t-shirt sale")

        elif 440+screen_x < x < 488+screen_x and 65+screen_y < y < 140+screen_y :

            pressed_couloir = zone_interaction(screen,"Fouiller l'armoire (A)",action,pressed_couloir,"une couverture")

        elif 530+screen_x < x < 615+screen_x and 610+screen_y < y < 700+screen_y :

            pressed_entre = zone_interaction(screen,"Fouiller l'armoire (A)",action,pressed_entre,"un vieux plaid")

        elif 300+screen_x < x < 400+screen_x and 20+screen_y < y < 110+screen_y and mom_sleep == True :

            pressed_arm_mom = zone_interaction(screen,"Fouiller l'armoire (A)",action,pressed_arm_mom,"une serviette")

        elif 290+screen_x < x < 340+screen_x and 510+screen_y < y < 560+screen_y :
            
            pressed_cuisine1 = zone_interaction(screen,"Fouiller les tirroirs (A)",action,pressed_cuisine1,"un tire-bouchon")

        elif 341+screen_x < x < 410+screen_x and 510+screen_y < y < 560+screen_y and sac.soupe_froide == 1:
            
            if pressed_four <= 0 and pressed_mom <= 0: 
                pressed_four = zone_interaction(screen,"Fouiller le four (A)",action,pressed_four,"une soupe chaude")
                sac.soupe_chaude=1 
                pressed_four = 0
            if pressed_four == 0 and pressed_mom >= 1: 
                pressed_four = zone_interaction(screen,"Fouiller le four (A)",action,pressed_four,"... un four vide")
                sac.soupe_chaude=1
                pressed_dad = -1
                
        elif 341+screen_x < x < 410+screen_x and 510+screen_y < y < 560+screen_y and sac.soupe_froide == 0:
          
            if pressed_mom < 0:
                pressed_four = zone_interaction(screen,"Fouiller le four (A)",action,pressed_four,"... un four vide")
                sac.soupe_chaude = 0
                pressed_four = 0

            if pressed_mom == 0:
                pressed_four = zone_interaction(screen,"Fouiller le four (A)",action,pressed_four," ... rien ... Trouve d'abord quelque chose à chauffer!")
                sac.soupe_chaude = 0
                pressed_four = 0
    
        elif 270+screen_x < x < 335+screen_x and 600+screen_y < y < 680+screen_y :
            
            if pressed_cuisine2 == -1:
                pressed_cuisine2 = zone_interaction(screen,"Fouiller le placard (A)",action,pressed_cuisine2,"une soupe froide")            

            if pressed_cuisine2 >= 0:
                pressed_cuisine2 = zone_interaction(screen,"Fouiller le placard (A)",action,pressed_cuisine2,"une soupe froide")            
                sac.soupe_froide=1
                pressed_dad = -1
                
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
            
            if pressed_sdb1 <= 0 and open_buro == False:                
                pressed_sdb1 = zone_interaction(screen,"Fouiller le linge (A)",action,pressed_sdb1,"une clé")
                cles_buro = 1
            if pressed_sdb1 <= 0 and open_buro == True:
                pressed_sdb1 = zone_interaction(screen,"Fouiller le linge (A)",action,pressed_sdb1,"une serviette")
                torchonsdb1 = 1    
                
        elif 185+screen_x < x < 225+screen_x and 200+screen_y < y < 300+screen_y :
            
            if cles_buro == 0 and service == False and mom_sleep == False:
                textsurface = myfont.render("La porte est fermée", False, (110, 110, 110)) 
                screen.blit(fond_text,(260,380))
                screen.blit(textsurface,(280,400))               
            if cles_buro == 1 and service == False and mom_sleep == False:
                textsurface = myfont.render("Papa va m'entendre,", False, (110, 110, 110)) 
                textsurface2 = myfont.render("c'est chaud !", False, (110, 110, 110)) 
                screen.blit(fond_text,(260,380))
                screen.blit(textsurface,(280,400))               
                screen.blit(textsurface2,(280,420)) 
            if cles_buro == 1 and service == True and mom_sleep == False:
                textsurface = myfont.render("Est-ce que maman dort ? ", False, (110, 110, 110)) 
                screen.blit(fond_text,(260,380))
                screen.blit(textsurface,(270,400))                                    
            if cles_buro == 1 and service == True and mom_sleep == True:                
                textsurface = myfont.render("Tu as ouvert", False, (110, 110, 110)) 
                textsurface2 = myfont.render("la porte du bureau", False, (110, 110, 110)) 
                screen.blit(fond_text,(260,380))
                screen.blit(textsurface,(280,400))               
                screen.blit(textsurface2,(280,420)) 
                pressed_sdb1 = -1
                open_buro = True
                
        elif 230+screen_x < x < 270+screen_x and 560+screen_y < y < 630+screen_y :

            pressed_frigo = zone_interaction(screen,"Ouvrir le frigo (A)",action,pressed_frigo,"une bière")
            
        elif 670+screen_x < x < 725+screen_x and 560+screen_y < y < 670+screen_y :
            
            if sac.Cle_maison == False and dad_sleep == False and mom_sleep == False:
                textsurface = myfont.render("La porte est fermée, ", False, (110, 110, 110)) 
                textsurface2 = myfont.render("les clés ne sont pas là.", False, (110, 110, 110)) 
                screen.blit(fond_text,(260,380))
                screen.blit(textsurface,(280,400))               
                screen.blit(textsurface2,(280,420))  
            if sac.Cle_maison == False and dad_sleep == True and mom_sleep == True:
                textsurface = myfont.render("Les clés ne sont pas " , False, (110, 110, 110)) 
                textsurface1 = myfont.render("sur la porte." , False, (110, 110, 110)) 
                textsurface2 = myfont.render("Où papa les a-t-il posé?" , False, (110, 110, 110)) 
                screen.blit(fond_text,(260,380))
                screen.blit(textsurface,(280,400))
                screen.blit(textsurface1,(280,420))
                screen.blit(textsurface2,(280,440))  
                papa_fouillab = True
            if sac.Cle_maison == False and dad_sleep == True and mom_sleep == False:
                textsurface = myfont.render("Est-ce que maman dort ?", False, (110, 110, 110)) 
                textsurface2 = myfont.render("Où sont les clés de papa?", False, (110, 110, 110)) 
                screen.blit(fond_text,(260,380))
                screen.blit(textsurface,(270,400))
                screen.blit(textsurface2,(270,420)) 
                papa_fouillab = True                                     

            if sac.Cle_maison == True and dad_sleep == True and mom_sleep == False:               
                textsurface = myfont.render("Tu as ouvert ", False, (110, 110, 110)) 
                textsurface2 = myfont.render("la porte d'entrée!", False, (110, 110, 110)) 
                screen.blit(fond_text,(260,380))
                screen.blit(textsurface,(280,400))
                screen.blit(textsurface2,(280,420))
                porte_entre = True
                Gus.porte_entre = True
            if sac.Cle_maison == True and dad_sleep == True and mom_sleep == True:               
                textsurface = myfont.render("Tu as ouvert ", False, (110, 110, 110)) 
                textsurface2 = myfont.render("la porte d'entrée!", False, (110, 110, 110)) 
                screen.blit(fond_text,(260,380))
                screen.blit(textsurface,(280,400))
                screen.blit(textsurface2,(280,420))
                porte_entre = True
                Gus.porte_entre = True
        
        elif 862+screen_x < x < 1000+screen_x and 440+screen_y < y < 480+screen_y :
            Gus.level = 2
            Gus.spawn = 1

        else:
            action.click = False
        
        screen.blit(gugus, rect_gugus)
        
        pv = Gus_font.render("Santé : " + str(Gus.pv), False, (78, 22, 9))
        argent = Gus_font.render("Argent : " + str(Gus.money), False, (31, 160, 85))
        lvl = Gus_font.render("Niveau : " + str(Gus.level), False, (78, 22, 9))

    
        screen.blit(pv , (10,20))
        screen.blit(lvl , (10,45))
        screen.blit(argent , (10,70))
        screen.blit(sac_tab , (10,450))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_TAB]:
            affich_sac(screen,sac)
        if (Gus.pause%2) == 1:
            pause(screen,gameExit,Gus,sac)
        if Gus.pv == 0:
            game_over(screen)

        pygame.display.update()

        clock.tick(100)
        
def nivo2(sac,action,Gus):
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
    #CREATION ET CARACTERISTIQUES PNJ
    speed_y = 0
    speed_x = -1
    rat_left = pygame.image.load('bank/pnj/rat_g.png')
    
    spawn_x = 820
    spawn_y = 400
       
    rat2 = pnj(spawn_x,spawn_y,screen_x,screen_y,rat_left,'left') 

    spawn_damex = 120
    spawn_damey = 250
    dame_left = dame_l[0]
    dame = pnj(spawn_damex,spawn_damey,screen_x,screen_y,dame_left,"left")
    
    ####LVL 2 EST

    #INTERACTIONS
    pressed_vieille = -1
    pressed_interphone = -1
    
    phrases_vieille =[["J'ai perdu mes","clopes gamin!!"],
                      ["Il me faut bien plus de","clopes que ça gamin!"]]
    phrases_interphone =[["Qui c'est ??"]]
    phrases_papier=[["Ah! Juste quelques", "feuilles de papiers et","des stylos.","Rien d'utile!"]]

    #OBJETS NIVEAU
    pressed_arbre = -1
    pressed_papier = -1
    
    ##LVL 2 NE
    
    #INTERACTIONS
    pressed_stuff = -1
    phrases_stuff = [["Touches pas à ça !! ","C'est mon sac!"]]
    pressed_tox = -1
    phrases_toxo = [["","Qu'est-ce tu veux toi?","","Dégages de là"]]
    #ITEMS
    pressed_seringue = -1
    pressed_ball = -1
    
    ##LVL 2 NORD
    #INTERACTIONS
    pressed_con = -1
    phrases_con = [["J'en ai mmarre de ce","quartier. Entre les ","dealers et les camés...",
                    "J'espère qu'ils finiront","tous au trou!"]]
    #ITEMS
    clopesEst = 0
    clopesNord = 0
    press_poub = -1
    argent_poub = 0
    press_coin = -1
        
    gameExit = False
    
    while not gameExit:
        
        if frame_count <= 30:
            frame_count += 1
        else:
            frame_count = 0
        
        if frame_count <= 15:
            a=0
        elif frame_count > 15:
            a=1
            
        rect_gugus = gugus.get_rect() 
        
        Gus.money = round(tune + argent_poub,2)
        sac.Clopes = round(clopesEst + clopesNord, 0)
        
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
                        pressed_vieille = 0
                    if 325+screen_x < x < 360+screen_x and 315+screen_y < y < 355+screen_y and Gus.level == 2 and sac.Clopes == 1:
                        pressed_vieille = 1
                    if 550+screen_x < x < 600+screen_x and 510+screen_y < y < 555+screen_y and Gus.level == 2:
                        pressed_interphone = 0
                    #OBJETS
                    ###EST
                    if 638+screen_x < x < 700+screen_x and 500+screen_y < y < 520+screen_y and Gus.level == 2:
                        pressed_arbre += 1  
                    if 635+screen_x < x < 792+screen_x and 320+screen_y < y < 368+screen_y and Gus.level == 2:
                        pressed_papier = 0
                    ###NORD EST
                    ##INTERACTIONS
                    if 777+screen_x < x < 870+screen_x and 20+screen_y < y < 70+screen_y and Gus.level == 2.1:
                        pressed_stuff = 0
                    if 894+screen_x < x < 940+screen_x and 20+screen_y < y < 70+screen_y and Gus.level == 2.1:
                        pressed_tox = 0
                    ##ITEMS
                    if 780+screen_x < x < 830+screen_x and 530+screen_y < y < 560+screen_y and Gus.level == 2.1:
                        pressed_seringue += 1
                    if 70+screen_x < x < 110+screen_x and 0+screen_y < y < 32+screen_y and Gus.level == 2.1:
                        pressed_ball += 1
                        
                    ###NORD
                    ##INTERACTIONS
                    if interact and Gus.level == 2.2:
                        pressed_con = 0
                    ##ITEMS
                    if 79+screen_x < x < 160+screen_x and 438+screen_y < y < 467+screen_y and Gus.level == 2.2:
                        press_poub += 1
                    if 0+screen_x < x < 45+screen_x and 0+screen_y < y < 45+screen_y and Gus.level == 2.2:
                        press_coin += 1
                        
                elif event.key != pygame.K_a:
                
                    action.click = False
                    
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
                
        if Gus.level == 2:
    
            if Gus.spawn == 1 and time < 2:
                screen_x,screen_y,x,y = spawn_level(x,y,226,225)
            elif Gus.spawn == 2 and time < 2:
                screen_x,screen_y,x,y = spawn_level(x,y,1000-gugus_width,80)
        
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
                
                screen_x,screen_y,x,y = spawn_level(x,y,1000-gugus_width,481)

            if Gus.spawn == 2 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,0+gugus_width,481)
                        
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
                
                screen_x,screen_y,x,y = spawn_level(x,y,1000-gugus_width,481)

            elif Gus.spawn == 2 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,0+gugus_width,481)

            if Gus.spawn == 3 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,190,11) 

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
                
                screen_x,screen_y,x,y = spawn_level(x,y,1000-gugus_width,481)
                
            if Gus.spawn == 2 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,112,651) 
                
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

            if dame.rect.colliderect(rect_gugus) and dame.side == "right":
                if abs (dame.rect.right - rect_gugus.left) <= 10:
                    speed_x = 0
                    speed_y *= -1  
                    dame.movement = False
                    
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
                
                screen_x,screen_y,x,y = spawn_level(x,y,112,50)
                        
            time += 1
            
            liste_mur = level_2O(screen,screen_x,screen_y)
        
            x_change,y_change,rel_x,rel_y = collisions(liste_mur,rect_gugus,x_change,y_change,speed_move,rel_x,rel_y)
            
            screen_x += rel_x
            screen_y += rel_y
            
            if y < 0:
                Gus.level = 2.3
                Gus.spawn = 2
                time = 0
            
        elif Gus.level == 2.5:
            
            if Gus.spawn == 1 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,190,655)
                        
            time += 1
            
            liste_mur = level_2NN(screen,screen_x,screen_y)
        
            x_change,y_change,rel_x,rel_y = collisions(liste_mur,rect_gugus,x_change,y_change,speed_move,rel_x,rel_y)
            
            screen_x += rel_x
            screen_y += rel_y
            
            if y > 465:
                Gus.level = 2.2
                Gus.spawn = 3
                time = 0             
         
        if press_poub >= 0:
            argent_poub = 0.1 
        
        ##INTERACTION LVL 2
        if 325+screen_x < x < 360+screen_x and 315+screen_y < y < 355+screen_y and Gus.level == 2:

            zone_dialogue(screen,"Parler à la vieille (A)",action,phrases_vieille[pressed_vieille],pressed_vieille,2)
            
        elif 550+screen_x < x < 600+screen_x and 510+screen_y < y < 555+screen_y and Gus.level == 2:

            zone_dialogue(screen,"Sonner à l'interphone (A)",action,phrases_interphone[pressed_interphone],pressed_interphone,1)
       
        ##OBJET LVL 2
        elif 638+screen_x < x < 700+screen_x and 500+screen_y < y < 520+screen_y and Gus.level == 2:
            
            pressed_arbre = zone_interaction(screen,"Qu'est-ce que c'est? (A)",action,pressed_arbre,"un paquet de clopes!")
            clopesEst = 1
            
        elif 680+screen_x < x < 712+screen_x and 88+screen_y < y < 140+screen_y and Gus.level == 2 and sac.Clef == 0 :

                textsurface = myfont.render("Il y a un truc", False, (110, 110, 110))
                textsurface2 = myfont.render("fermé à clé dans ce", False, (110, 110, 110))
                textsurface3 = myfont.render("carton", False, (110, 110, 110))
                screen.blit(fond_text,(260,380))
                screen.blit(textsurface,(280,400))
                screen.blit(textsurface2,(280,420)) 
                screen.blit(textsurface3,(280,440))  
                
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

            zone_dialogue(screen,"Fouiller ici (A)",action,phrases_papier[pressed_papier],pressed_papier,1)
        
        #### LVL 2.1
        ##INTERACTIONS
        elif 777+screen_x < x < 870+screen_x and 20+screen_y < y < 70+screen_y and Gus.level == 2.1:
            zone_dialogue(screen,"Fouiller les affaires (A)",action,phrases_stuff[pressed_stuff],pressed_stuff,2)
        elif 894+screen_x < x < 940+screen_x and 20+screen_y < y < 70+screen_y and Gus.level == 2.1:
            zone_dialogue(screen,"Parler avec le toxico (A)",action,phrases_toxo[pressed_tox],pressed_tox,2)
                        
        ##ITEMS
        elif 780+screen_x < x < 830+screen_x and 530+screen_y < y < 560+screen_y and Gus.level == 2.1:
            pressed_seringue = zone_interaction(screen,"Qu'est-ce que c'est? (A)",action,pressed_seringue,"un seringue!")
            sac.Seringue = 1
            
        elif 70+screen_x < x < 110+screen_x and 0+screen_y < y < 32+screen_y and Gus.level == 2.1:        
            pressed_ball = zone_interaction(screen,"Qu'est-ce que c'est? (A)",action,pressed_ball,"un ballon!")
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
            zone_dialogue(screen,"Parler au concierge (A)",action,phrases_con[pressed_con],pressed_con,2)
              
        
        ##ITEMS
        elif 79+screen_x < x < 160+screen_x and 438+screen_y < y < 467+screen_y and Gus.level == 2.2:
            press_poub = zone_interaction(screen,"Fouiller les poubelles (A)",action,press_poub,"10 centimes!")
        elif 0+screen_x < x < 45+screen_x and 0+screen_y < y < 45+screen_y and Gus.level == 2.2 and clopesNord == 1:
            press_coin = zone_interaction(screen,"Qu'est-ce que c'est? (A)",action,press_coin,"des capotes!")
            clopesNord = 1
            
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
        argent = Gus_font.render("Argent : " + str(Gus.money), False, (31, 160, 85))
        lvl = Gus_font.render("Niveau : " + str(int(Gus.level)), False, (78, 22, 9))
    
        screen.blit(pv , (10,20))
        screen.blit(lvl , (10,45))
        screen.blit(argent , (10,70))
        screen.blit(sac_tab , (10,450))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_TAB]:
            affich_sac(screen,sac)
        if (Gus.pause%2) == 1:
            pause(screen,gameExit,Gus,sac)
        if Gus.pv == 0:
            game_over(screen)

        pygame.display.update()

        clock.tick(100)

