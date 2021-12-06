# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 16:02:54 2021

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

Gus = Gus()
sac = sac_a_dos()
action=action_key()


def game_loop(sac,action,Gus):
    
    speed_move = Gus.speed
    
    frame_count = Gus.frame
    a=0
    
    x =  (display_width-gugus_width)/2
    y = (display_height-gugus_height)/2
    screen_x = -475 + x
    screen_y = -224 + y
    rel_x = 0 
    rel_y = 0
    x_change = 0
    y_change = 0
    
    phrases_papa_avant_soupe = [["Laisse moi tranquille"], ["Va voir ta mère","dans sa chambre"]]
    phrases_papa_entre_soupe = [["Tu as apporté à","manger à ta mère ?"]]
    phrases_papa_post_soupe = [["J'ai soif !!"],
                ["Trouves-moi une bière","et tais-toi!"]]
    sleep = [["ZZZzzzZZZzzz"]]
    phrases_maman = [["Apporte moi un truc","à manger s'il te plait"], ["Merci beaucoup Gus"],["ZZZzzzZZZzzz",
                     ""]]    
    
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
    pressed_sdb2 = -1
    
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
    
    gugus = gugus_face
        
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
            
        sac.Alcool = biere + bouteille_alc
        sac.Torchon = torchon_salon+torchonsdb1+torchoncoul+torchonch+torchon_entre+torchon_mom
        
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
                    Gus.pause += 1    
            ############################
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  
                    x_change = -speed_move
                    rel_x = speed_move
                    y_change = 0
                    rel_y = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = speed_move
                    rel_x = -speed_move
                    y_change = 0
                    rel_y = 0
                elif event.key == pygame.K_UP:
                    y_change = -speed_move
                    rel_y = speed_move
                    x_change = 0
                    rel_x = 0
                elif event.key == pygame.K_DOWN:
                    y_change = speed_move
                    rel_y = -speed_move
                    x_change = 0
                    rel_x = 0

                if event.key == pygame.K_a and not action.click:
                    action.click = True
                    #PERSONNES
                    if 0+screen_x < x < 75+screen_x and 0+screen_y < y < 100+screen_y and sac.soupe_chaude == 0 and service == False:
                        pressed_mom = 0
                        pressed_dad = -1
                    if 0+screen_x < x < 75+screen_x and 0+screen_y < y < 100+screen_y and sac.soupe_chaude == 1 and service == False:
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

                elif event.key != pygame.K_a:
                
                    action.click = False
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_change = 0
                    rel_x = 0
                    gugus = gugus_gauche                    
                if event.key == pygame.K_RIGHT:
                    x_change = 0
                    rel_x = 0
                    gugus = gugus_droite

                if event.key == pygame.K_UP:
                    y_change = 0
                    rel_y = 0
                    gugus = gugus_dos
                    
                if event.key == pygame.K_DOWN:
                    y_change = 0
                    rel_y = 0
                    gugus = gugus_face
                    
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
        elif 612+screen_x < x < 670+screen_x and 457+screen_y < y < 540+screen_y :

            pressed_sdb2 = zone_interaction(screen,"Fouiller le placard (A)",action,pressed_sdb2,"une bouteille d'alcool")

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
            
            if sac.Torchon <  5:
                textsurface = myfont.render("Ca fait un peu haut", False, (110, 110, 110))
                textsurface2 = myfont.render("pour sauter!", False, (110, 110, 110))
                screen.blit(fond_text,(260,380))
                screen.blit(textsurface,(280,400))
                screen.blit(textsurface2,(280,420)) 
            if sac.Torchon == 5:
                textsurface = myfont.render("C'est toujours haut mais ", False, (110, 110, 110))
                textsurface2 = myfont.render("avec 5 serviettes ça se tente!", False, (110, 110, 110))              
                screen.blit(fond_text,(260,380))
                screen.blit(textsurface,(280,400)) 
                screen.blit(textsurface2,(280,420)) 
            if sac.Torchon > 5:
                textsurface = myfont.render("J'ai assez de linge pour me faire ", False, (110, 110, 110)) 
                textsurface2 = myfont.render("une descente en rappel!", False, (110, 110, 110))              
                screen.blit(fond_text,(260,380))
                screen.blit(textsurface,(280,400)) 
                screen.blit(textsurface2,(280,420))                
            
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
                textsurface = myfont.render("Les clés ne sont pas sur la porte." , False, (110, 110, 110)) 
                textsurface2 = myfont.render("Où papa les a-t-il posé?" , False, (110, 110, 110)) 
                screen.blit(fond_text,(260,380))
                screen.blit(textsurface,(280,400))
                screen.blit(textsurface2,(280,420))  
                papa_fouillab = True
            if sac.Cle_maison == False and dad_sleep == True and mom_sleep == False:
                textsurface = myfont.render("Est-ce que maman dort ?", False, (110, 110, 110)) 
                textsurface2 = myfont.render("Où sont les clés de papa?", False, (110, 110, 110)) 
                screen.blit(fond_text,(260,380))
                screen.blit(textsurface,(270,400))
                screen.blit(textsurface2,(270,420)) 
                papa_fouillab = True                                     
            if sac.Cle_maison == False and dad_sleep == False and mom_sleep == True:               
                textsurface = myfont.render("Papa ne dort pas, c'est tendu!! ", False, (110, 110, 110)) 
                textsurface2 = myfont.render("Et j'ai pas les clés!", False, (110, 110, 110)) 
                screen.blit(fond_text,(260,380))
                screen.blit(textsurface,(280,400))
                screen.blit(textsurface2,(280,420)) 
            if sac.Cle_maison == True and dad_sleep == True and mom_sleep == False:               
                textsurface = myfont.render("Maman ne dort pas,", False, (110, 110, 110)) 
                textsurface2 = myfont.render("c'est tendu!!", False, (110, 110, 110)) 
                screen.blit(fond_text,(260,380))
                screen.blit(textsurface,(280,400))
                screen.blit(textsurface2,(280,420))
            if sac.Cle_maison == True and dad_sleep == True and mom_sleep == True:               
                textsurface = myfont.render("Tu as ouvert ", False, (110, 110, 110)) 
                textsurface2 = myfont.render("la porte d'entrée!", False, (110, 110, 110)) 
                screen.blit(fond_text,(260,380))
                screen.blit(textsurface,(280,400))
                screen.blit(textsurface2,(280,420))
                porte_entre = True
                Gus.porte_entre = True

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
            pause(screen)
            
        pygame.display.update()
        clock.tick(100)

game_loop(sac,action,Gus)
pygame.quit()
quit()