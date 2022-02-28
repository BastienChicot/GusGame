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
                      ["Oh la! J'ai personne","à voir aujourd'hui.","Aides moi à trouver","quelqu'un."]]
    phrases_mac = [["Yo Gus, Tu as", "vu mon employée ?"],
                   ["Merci petit. Tu","travaille bien. Je","peux te confier son","planing?"]]
    phrases_bus = [["J'ai pas le temps","de parler!"]]
    
    #LVL 3 C
    phrases_lassl = [["Yo Gus comment","tu vas?","T'as pas vu ma","pince à cheveux?"],
                     ["T'as pas un petit","gâteau pour moi ?"],
                     ["J'adore le groupe qui","joue dans cette station","Pourquoi ils ne","jouent pas ?"]]
    
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
                     ["Mon carton"," commence à se faire","vieux..."]]
    
    phrases_depressif = [["Ohlala ça va pas","mais alors pas du ","tout..."]]
    
    machine_1 = [["Elle est cassée!"]]
    #OBJETS NIVEA
    #INTERACTIONS
    #ITEMS    
    
    gameExit = False
    
    while not gameExit and Gus.level >= 3 and Gus.level < 4:
                    
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
                    if interact and Gus.level == 3 and tr.give_condom == False:
                        tr.press_hook = 0
                    if interact and Gus.level == 3 and tr.give_condom == True:
                        tr.press_hook = 1
                        sac.Argent_mac = 50
                    if interact and Gus.level == 3 and sac.Planing == 1:
                        tr.press_hook = 2
                        
                    if 826+screen_x < x < 907+screen_x and 522+screen_y < y < 576+screen_y and Gus.level == 3 and tr.give_mac == False and sac.Capote != 0:
                        tr.press_mac = 0
                    if 826+screen_x < x < 907+screen_x and 522+screen_y < y < 576+screen_y and Gus.level == 3 and tr.give_mac == True:
                        tr.press_mac = 1
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
                    if 112+screen_x < x < 155+screen_x and 166+screen_y < y < 200+screen_y and Gus.level == 3.1 and tr.give_lassl_gateau == True:
                        tr.press_lassl = 2
                        
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

                    if 134+screen_x < x < 195+screen_x and 380+screen_y < y < 412+screen_y and Gus.level == 3.3:
                        tr.depressif = 0
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

                        
                    if 700+screen_x < x < 800+screen_x and 80+screen_y < y < 125+screen_y and Gus.level == 3.3 :
                        tr.press_machine2 += 1
                        
                    if 33+screen_x < x < 210+screen_x and 13+screen_y < y < 100+screen_y and Gus.level == 3.3 and tr.give_dwich == False and sac.Sandwich != 0:
                        tr.give_dwich = True
                        
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
                
                screen_x,screen_y,x,y = spawn_level(x,y,1001-gugus_width,228)
                        
            time += 1
            
            liste_mur = level_3C(screen,screen_x,screen_y)
        
            # if Gus.perso == "gus":
            x_change,y_change,rel_x,rel_y = collisions(liste_mur,rect_gugus,x_change,y_change,speed_move,rel_x,rel_y)
            # if Gus.perso == "lassl":
            #     x_change,y_change,rel_x,rel_y = collisions(liste_mur,rect_lassl,x_change,y_change,speed_move,rel_x,rel_y)

            screen_x += rel_x
            screen_y += rel_y
            
            if x > 470 :
                Gus.level = 3.2
                Gus.spawn = 1
                time = 0
            if y < 0:
                Gus.level = 3
                Gus.spawn = 3
                time = 0  
                
                
    
        elif Gus.level == 3.2:
            
            if Gus.spawn == 1 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,31,228)

            if Gus.spawn == 2 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,901,302)
                        
            time += 1
            
            liste_mur = level_3E(screen,screen_x,screen_y)
        
            # if Gus.perso == "gus":
            x_change,y_change,rel_x,rel_y = collisions(liste_mur,rect_gugus,x_change,y_change,speed_move,rel_x,rel_y)
            # if Gus.perso == "lassl":
            #     x_change,y_change,rel_x,rel_y = collisions(liste_mur,rect_lassl,x_change,y_change,speed_move,rel_x,rel_y)

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
            if x < 0:
                Gus.level = 3.1
                Gus.spawn = 2
                time = 0   

        elif Gus.level == 3.3:
            
            if Gus.spawn == 1 and time < 2:
                
                screen_x,screen_y,x,y = spawn_level(x,y,901,142)
                        
            time += 1
            
            liste_mur = level_3SE(screen,screen_x,screen_y)
        
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
            if tr.achat_ticket == True and sac.Ticket == 1 and tr.give_tivket == False:
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
            zone_dialogue(screen,"Parler au clodo (A)",action,phrases_clodo[tr.press_clodo],tr.press_clodo,5)
            if sac.Sandwich == 1 and tr.give_dwich == False:
                textsurface = myfont.render("Donner le sandwich", False, (0, 0, 0))
                textsurface2 = myfont.render("ENTER", False, (0, 0, 0))
                screen.blit(textsurface,(x,y-60))
                screen.blit(textsurface2,(x+35,y-40)) 
            
        elif 134+screen_x < x < 195+screen_x and 380+screen_y < y < 412+screen_y and Gus.level == 3.3:
            zone_dialogue(screen,"Parler au monsieur (A)",action,phrases_depressif[tr.depressif],tr.depressif,5)

        elif 590+screen_x < x < 690+screen_x and 75+screen_y < y < 109+screen_y and Gus.level == 3.3:
            zone_dialogue(screen,"Acheter un truc (A)",action,machine_1[tr.press_machine1],tr.press_machine1,5)
            
        elif 700+screen_x < x < 800+screen_x and 80+screen_y < y < 125+screen_y and Gus.level == 3.3 :
            textsurface = myfont.render("Acheter un truc", False, (110, 110, 110))
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