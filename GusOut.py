# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 16:02:54 2021

@author: basti
"""
import pygame
from Story.Fonctions import collisions
from Level.Levels import level_1

pygame.init()

display_width = 1200
display_height = 800

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
running = 1.02 



def gugus_affich(gugus,x,y):
    screen.blit(gugus, (x,y))

def game_loop():
    x =  (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    y_change = 0

    gugus = gugus_face
    
    gameExit = False
    run = False
    
    while not gameExit:
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
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    gugus = gugus_dos
                    y_change = -2.5
                elif event.key == pygame.K_DOWN:
                    gugus = gugus_face
                    y_change = 2.5
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = True
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    run = False
            ######################
        
        rect_gugus = gugus.get_rect()
        
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
        
        liste_mur = level_1(screen,display_width,display_height)
        
        x,y = collisions(liste_mur,x,y,rect_gugus,x_change,y_change)
        
        rect_gugus.topleft = (x,y)
        
        screen.blit(gugus, rect_gugus)
        
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()