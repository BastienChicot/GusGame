# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 16:40:54 2021

@author: basti
"""
import pygame

white = (255,255,255)

def level_1(gameDisplay):
    
    fond=pygame.image.load('Level/test_fond.jpg')
    
    mur = pygame.Rect(100,300,32,180)
    mur2 = pygame.Rect(200,30,320,80)
    mur3 = pygame.Rect(500,350,30,180)
    
    pygame.draw.rect(gameDisplay,white,mur)
    pygame.draw.rect(gameDisplay,white,mur2)
    pygame.draw.rect(gameDisplay,white,mur3)
    liste_mur = [mur2,mur,mur3]
    
    gameDisplay.blit(fond, (0,0))        
 
    return(liste_mur)