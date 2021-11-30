# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 16:02:54 2021

@author: basti
"""
import pygame
from Story.Fonctions import collisions, sac_a_dos, action_key
from Level.Levels import level_1
from Story.histoire import histoire

pygame.init()
pygame.font.init()
 
myfont = pygame.font.SysFont('arial', 20)

display_width = 1000
display_height = 707

screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Gus veut boire un coup')

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

clock = pygame.time.Clock()

gugus_face = pygame.image.load('Gus/Gus.png')
gugus_dos = pygame.image.load('Gus/Gus_dos.png')
gugus_droite = pygame.image.load('Gus/Gus_droit.png')
gugus_gauche = pygame.image.load('Gus/Gus_gauche.png')

gugus_width = 48
gugus_height = 52
running=1.02

sac = sac_a_dos()
action=action_key()

phrases_papa = ["Laisse moi tranquille", "Va voir ta mère, elle est dans la chambre",
                "Tu as apporté à manger à ta mère ?","Bon laisse moi tranquille maintenant",
                "Tu me fatigues! Va-t-en!","ZZZzzzZZZzzz"]

def gugus_affich(gugus,x,y):
    screen.blit(gugus, (x,y))

def game_loop(sac,action):
    x =  575
    y = 73
    x_change = 0
    y_change = 0
    
    pressed = -1
    pressed_dad = -1
    
    gugus = gugus_face
    gugus_dir = "face"
        
    gameExit = False
    run = False

    liste_mur,liste_zone = level_1(screen,display_width,display_height)
    
    while not gameExit:
        
        liste_mur,liste_zone = level_1(screen,display_width,display_height)
        rect_gugus = gugus.get_rect() 
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
    
            ############################
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    gugus_dir="left"
                    gugus = gugus_gauche
                    x_change = -2.5
                elif event.key == pygame.K_RIGHT:
                    gugus_dir="right"
                    gugus = gugus_droite
                    x_change = 2.5
                elif event.key == pygame.K_UP:
                    gugus_dir="up"
                    gugus = gugus_dos
                    y_change = -2.5
                elif event.key == pygame.K_DOWN:
                    gugus_dir="face"
                    gugus = gugus_face
                    y_change = 2.5

                if event.key == pygame.K_a and not action.click:
                    action.click = True
                    if 170 < x < 210 and 378 < y < 440 :
                        pressed_dad += 1
                    if 235 < x < 295 and 480 < y < 530 :
                        pressed += 1
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

        rect_gugus.topleft = (x,y)
        
        # action,sac=histoire(screen,x,y,"level_1",action,sac,pressed,liste_zone)
    
        if 170 < x < 210 and 378 < y < 440 :
            
            textsurface = myfont.render('Parler à papa (A)', False, (255, 255, 255))
            screen.blit(textsurface,(290,440))
                
            i = pressed_dad
            
            if i >= 0 and i < 6 :
                textsurface2 = myfont.render(phrases_papa[i], False, (255, 255, 255))
                screen.blit(textsurface2,(290,460))                     
            else:
                i = 0         
               
        elif 235 < x < 295 and 480 < y < 530 :
            
            textsurface = myfont.render("Fouiller l'armoire (A)", False, (255, 255, 255))
            screen.blit(textsurface,(290,440))

            def find_torchon(find):
                find = find
                sac.torchon_salon = False
                
                if action.click == True and find == 0:
                                   
                    textsurface2 = myfont.render("Tu as trouvé un torchon et une cuillière", False, (255, 255, 255))
                    screen.blit(textsurface2,(290,460))
                    
                    
                if action.click == True and find == 1:
                                            
                    textsurface2 = myfont.render("Il n'y a plus rien ici !", False, (255, 255, 255))
                    screen.blit(textsurface2,(290,460))
                    
                    sac.torchon_salon = True
                                        
            if sac.torchon_salon == False and pressed == 0:
                find_torchon(0)
            if pressed > 0:
                find_torchon(1)
            
            print(liste_zone[0].interaction,sac.torchon_salon)
            
        else:
            action.click = False
            
        # for zone in liste_zone :
        #     if zone.colliderect(rect_gugus) and action.click == True:
        #         zone.passage = True  
        #         return zone.passage

        screen.blit(gugus, rect_gugus)

        pygame.display.update()
        clock.tick(60)

game_loop(sac,action)
pygame.quit()
quit()