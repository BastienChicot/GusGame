# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 16:40:54 2021

@author: basti
"""
import pygame

white = (255,255,255)

def level_1(gameDisplay,display_width,display_height):
    
    fond=pygame.image.load('Level/level_1.jpg')
    fond_width = 1000
    fond_height = 707
    
    mur = pygame.Rect(0,0,1,0)
    mur2 = pygame.Rect(799,0,1,1)
    # mur3 = pygame.Rect(500,350,30,180)
    
    pygame.draw.rect(gameDisplay,white,mur)
    pygame.draw.rect(gameDisplay,white,mur2)
    # pygame.draw.rect(gameDisplay,white,mur3)
    liste_mur = [mur2,mur]
    
    gameDisplay.blit(fond, ((display_width-fond_width)/2,(display_height-fond_height)/2))        
 
    return(liste_mur)