# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 16:40:54 2021

@author: basti
"""
import pygame

white = (255,255,255)
black = (0,0,0)


class zone_inter(pygame.Rect):
    def __init__(self,x,y,largeur,hauteur):
        # super().__init__()
        pygame.Rect.__init__(self,x,y,largeur,hauteur)
        self.passage = False
        self.interaction = -1
        
    def draw (x,y,largeur,hauteur):
        pygame.Rect(x,y,largeur,hauteur)

        
def level_1(gameDisplay,display_width,display_height):
    
    fond=pygame.image.load('Level/level_1.jpg')
    fond_width = 1000
    fond_height = 707


    ##CHAMBRE PARENTS
    mur = pygame.Rect(0,0,1000,10)
    mur2 = pygame.Rect(0,0,42,430)
    mur3 = pygame.Rect(0,430,12,140)
    mur4 = pygame.Rect(0,571,167,137)  
    mur5 = pygame.Rect(308,10,160,55)
    mur6 = pygame.Rect(78,72,129,90)
    mur7 = pygame.Rect(362,134,56,66)
    mur8 = pygame.Rect(0,160,233,40)
    mur9 = pygame.Rect(230,188,20,12)  
    ##CHAMBRE GUS
    mur10 = pygame.Rect(410,65,37,112)
    mur11 = pygame.Rect(517,0,13,170)
    mur12 = pygame.Rect(618,0,118,63)
    mur13 = pygame.Rect(657,68,75,215)
    mur14 = pygame.Rect(518,254,150,21)  
    mur15 = pygame.Rect(690,280,44,129)
    ##SDB
    mur16 = pygame.Rect(519,333,170,27)
    mur17 = pygame.Rect(660,355,34,54)
    mur18 = pygame.Rect(520,357,43,105)
    mur19 = pygame.Rect(724,407,10,70)  
    mur20 = pygame.Rect(680,470,53,82)
    mur21 = pygame.Rect(567,517,104,70)
    mur22 = pygame.Rect(660,355,34,54)
    mur23 = pygame.Rect(520,550,213,11)
    ##COULOIRS
    mur24 = pygame.Rect(471,345,52,99)  
    mur25 = pygame.Rect(265,289,91,40)
    mur26 = pygame.Rect(410,663,326,38)
    ##PORTE ENTREE
    #mur27 = pygame.Rect(720,560,15,110)
    ##CUISINE
    mur28 = pygame.Rect(210,650,200,50)
    mur29 = pygame.Rect(290,500,124,55)  
    mur30 = pygame.Rect(235,620,35,50)
    mur31 = pygame.Rect(290,467,67,43)
    mur32 = pygame.Rect(152,593,34,117)
    mur33 = pygame.Rect(63,548,20,50)
    mur34 = pygame.Rect(141,555,20,50)
    ##SALON
    mur35 = pygame.Rect(35,450,170,31)
    mur36 = pygame.Rect(35,380,150,70)  
    mur37 = pygame.Rect(35,320,215,57)
    mur38 = pygame.Rect(347,326,10,25)
    ##BUREAU
    mur43 = pygame.Rect(35,300,80,20)
    mur39 = pygame.Rect(35,240,6,55)
    mur40 = pygame.Rect(35,194,50,48)
    mur41 = pygame.Rect(90,190,100,30)
    ##PORTE BUREAU
    #mur42 = pygame.Rect(180,210,10,120)
    ##EXTERIEUR
    mur44 = pygame.Rect(988,0,12,707)
    mur45 = pygame.Rect(850,70,150,370)
    mur46 = pygame.Rect(850,440,15,87)
        
    liste_mur = [mur,mur2,mur3,mur4,mur5,mur6,mur7,mur8,mur9,mur10,mur11,mur12,mur13,
                 mur14,mur15,mur16,mur17,mur18,mur19,mur20,mur21,mur22,mur23,mur24,
                 mur25,mur26,mur28,mur29,mur30,mur31,mur32,mur33,mur34,mur35,
                 mur36,mur37,mur38,mur39,mur40,mur41,mur43,mur44,mur45,mur46,
                 #mur42,mur27
                 ]
    
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
    pygame.draw.rect(gameDisplay,white,mur11)    
    pygame.draw.rect(gameDisplay,white,mur12)
    pygame.draw.rect(gameDisplay,white,mur13) 
    pygame.draw.rect(gameDisplay,white,mur14)
    pygame.draw.rect(gameDisplay,white,mur15)           
    pygame.draw.rect(gameDisplay,white,mur16)
    pygame.draw.rect(gameDisplay,white,mur17) 
    pygame.draw.rect(gameDisplay,white,mur18)
    pygame.draw.rect(gameDisplay,white,mur19)  
    pygame.draw.rect(gameDisplay,white,mur20)
    pygame.draw.rect(gameDisplay,white,mur21) 
    pygame.draw.rect(gameDisplay,white,mur22)
    pygame.draw.rect(gameDisplay,white,mur23)           
    pygame.draw.rect(gameDisplay,white,mur24)
    pygame.draw.rect(gameDisplay,white,mur25) 
    pygame.draw.rect(gameDisplay,white,mur26)
    #pygame.draw.rect(gameDisplay,white,mur27)  
    pygame.draw.rect(gameDisplay,white,mur28)
    pygame.draw.rect(gameDisplay,white,mur29) 
    pygame.draw.rect(gameDisplay,white,mur30)
    pygame.draw.rect(gameDisplay,white,mur31)  
    pygame.draw.rect(gameDisplay,white,mur32)
    pygame.draw.rect(gameDisplay,white,mur33)  
    pygame.draw.rect(gameDisplay,white,mur34)
    pygame.draw.rect(gameDisplay,white,mur35)  
    pygame.draw.rect(gameDisplay,white,mur36)
    pygame.draw.rect(gameDisplay,white,mur37) 
    pygame.draw.rect(gameDisplay,white,mur38)
    pygame.draw.rect(gameDisplay,white,mur39)  
    pygame.draw.rect(gameDisplay,white,mur40)
    pygame.draw.rect(gameDisplay,white,mur41)  
    #pygame.draw.rect(gameDisplay,white,mur42)
    pygame.draw.rect(gameDisplay,white,mur43)
    pygame.draw.rect(gameDisplay,white,mur44)  
    pygame.draw.rect(gameDisplay,white,mur45)
    pygame.draw.rect(gameDisplay,white,mur46)
    
    zone1 = zone_inter(235,480,60,50)  
    
    liste_zone=[zone1]
    
    gameDisplay.blit(fond, ((display_width-fond_width)/2,(display_height-fond_height)/2)) 
    
    return(liste_mur,liste_zone)