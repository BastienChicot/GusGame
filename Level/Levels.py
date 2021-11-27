# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 16:40:54 2021

@author: basti
"""
import pygame

white = (255,255,255)
black = (0,0,0)

def level_1(gameDisplay,display_width,display_height):
    
    fond=pygame.image.load('Level/level_1.jpg')
    fond_width = 1000
    fond_height = 707

    mur = pygame.Rect(0,0,1000,10)
    mur2 = pygame.Rect(0,0,42,430)
    mur3 = pygame.Rect(0,430,12,140)
    mur4 = pygame.Rect(0,571,167,137)  
    mur5 = pygame.Rect(308,10,160,55)
    mur6 = pygame.Rect(78,72,129,90)
    mur7 = pygame.Rect(362,134,56,66)
    mur8 = pygame.Rect(0,160,233,40)
    mur9 = pygame.Rect(230,188,20,12)  
    mur10 = pygame.Rect(410,65,37,112)
    
    liste_mur = [mur,mur2,mur3,mur4,mur5,mur6,mur7,mur8,mur9,mur10]
    
    
    pygame.draw.rect(gameDisplay,white,mur)
    pygame.draw.rect(gameDisplay,white,mur2)
    pygame.draw.rect(gameDisplay,white,mur3)
    pygame.draw.rect(gameDisplay,white,mur4)
    pygame.draw.rect(gameDisplay,white,mur5)
    pygame.draw.rect(gameDisplay,white,mur6)
    pygame.draw.rect(gameDisplay,white,mur7)
    pygame.draw.rect(gameDisplay,white,mur8)
    pygame.draw.rect(gameDisplay,white,mur9)
    pygame.draw.rect(gameDisplay,white,mur10)
    
    gameDisplay.blit(fond, ((display_width-fond_width)/2,(display_height-fond_height)/2)) 
        
    return(liste_mur)