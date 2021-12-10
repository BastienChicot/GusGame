# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 16:40:54 2021

@author: basti
"""
import pygame

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

class zone_inter(pygame.Rect):
    def __init__(self,x,y,largeur,hauteur):
        # super().__init__()
        pygame.Rect.__init__(self,x,y,largeur,hauteur)
        self.passage = False
        self.interaction = -1
        
def zone_level_1():
    zone1 = zone_inter(235,480,60,50)  
    
    liste_zone=[zone1]
    return(liste_zone)

class wall(pygame.Rect):
    def __init__(self,x,y,largeur,hauteur,rel_x,rel_y):
        pygame.Rect.__init__(self,x+rel_x,y+rel_y,largeur,hauteur)
    
def level_1(gameDisplay,screen_x,screen_y):
    
    fond=pygame.image.load('Level/level_1.jpg').convert()
    fond_width,fond_height = fond.get_rect().size
    
    ##CHAMBRE PARENTS
    mur = wall(0,0,1000,10,screen_x,screen_y)
    mur2 = wall(0,0,42,430,screen_x,screen_y)
    mur3 = wall(0,430,12,140,screen_x,screen_y)
    mur4 = wall(0,571,167,137,screen_x,screen_y)  
    mur5 = wall(308,10,160,55,screen_x,screen_y)
    mur6 = wall(78,72,129,90,screen_x,screen_y)
    mur7 = wall(362,134,56,66,screen_x,screen_y)
    mur8 = wall(0,160,233,40,screen_x,screen_y)
    mur9 = wall(230,188,20,12,screen_x,screen_y)  
    ##CHAMBRE GUS
    mur10 = wall(410,65,37,112,screen_x,screen_y)
    mur11 = wall(517,0,13,170,screen_x,screen_y)
    mur12 = wall(618,0,118,63,screen_x,screen_y)
    mur13 = wall(657,68,75,215,screen_x,screen_y)
    mur14 = wall(518,254,150,21,screen_x,screen_y)  
    mur15 = wall(690,280,44,129,screen_x,screen_y)
    ##SDB
    mur16 = wall(519,333,170,27,screen_x,screen_y)
    mur17 = wall(660,355,34,54,screen_x,screen_y)
    mur18 = wall(520,357,43,105,screen_x,screen_y)
    mur19 = wall(724,407,10,70,screen_x,screen_y)  
    mur20 = wall(680,470,53,82,screen_x,screen_y)
    mur21 = wall(567,517,104,70,screen_x,screen_y)
    mur22 = wall(660,355,34,54,screen_x,screen_y)
    mur23 = wall(520,550,213,11,screen_x,screen_y)
    ##COULOIRS
    mur24 = wall(471,345,52,99,screen_x,screen_y)  
    mur25 = wall(265,289,91,40,screen_x,screen_y)
    mur26 = wall(410,663,326,38,screen_x,screen_y)
    ##PORTE ENTREE
    mur27 = wall(720,560,15,110,screen_x,screen_y)
    ##CUISINE
    mur28 = wall(210,650,200,50,screen_x,screen_y)
    mur29 = wall(290,500,124,55,screen_x,screen_y)  
    mur30 = wall(235,620,35,50,screen_x,screen_y)
    mur31 = wall(290,467,67,43,screen_x,screen_y)
    mur32 = wall(152,593,34,117,screen_x,screen_y)
    mur33 = wall(63,548,20,50,screen_x,screen_y)
    mur34 = wall(141,555,20,50,screen_x,screen_y)
    ##SALON
    mur35 = wall(35,450,170,31,screen_x,screen_y)
    mur36 = wall(35,380,150,70,screen_x,screen_y)  
    mur37 = wall(35,320,215,57,screen_x,screen_y)
    mur38 = wall(347,326,10,25,screen_x,screen_y)
    ##BUREAU
    mur43 = wall(35,300,80,20,screen_x,screen_y)
    mur39 = wall(35,240,6,55,screen_x,screen_y)
    mur40 = wall(35,194,50,48,screen_x,screen_y)
    mur41 = wall(90,190,100,30,screen_x,screen_y)
    ##PORTE BUREAU
    mur42 = wall(180,210,10,120,screen_x,screen_y)
    ##EXTERIEUR
    mur44 = wall(988,0,12,707,screen_x,screen_y)
    mur45 = wall(850,70,150,370,screen_x,screen_y)
    mur46 = wall(850,440,15,87,screen_x,screen_y)
        
    liste_mur = [mur,mur2,mur3,mur4,mur5,mur6,mur7,mur8,mur9,mur10,mur11,mur12,mur13,
                  mur14,mur15,mur16,mur17,mur18,mur19,mur20,mur21,mur22,mur23,mur24,
                  mur25,mur26,mur28,mur29,mur30,mur31,mur32,mur33,mur34,mur35,
                  mur36,mur37,mur38,mur39,mur40,mur41,mur43,mur44,mur45,mur46,
                  mur42,mur27
                  ]

    for mur in liste_mur:
        pygame.draw.rect(gameDisplay,black,mur)
        
    gameDisplay.fill(white)
    gameDisplay.blit(fond, (screen_x,screen_y)) 
    
    return(liste_mur)

def level_1_2(gameDisplay,screen_x,screen_y):
    
    fond=pygame.image.load('Level/level_1.2.jpg').convert()
    fond_width,fond_height = fond.get_rect().size
    
    ##CHAMBRE PARENTS
    mur = wall(0,0,1000,10,screen_x,screen_y)
    mur2 = wall(0,0,42,430,screen_x,screen_y)
    mur3 = wall(0,430,12,140,screen_x,screen_y)
    mur4 = wall(0,571,167,137,screen_x,screen_y)  
    mur5 = wall(308,10,160,55,screen_x,screen_y)
    mur6 = wall(78,72,129,90,screen_x,screen_y)
    mur7 = wall(362,134,56,66,screen_x,screen_y)
    mur8 = wall(0,160,233,40,screen_x,screen_y)
    mur9 = wall(230,188,20,12,screen_x,screen_y)  
    ##CHAMBRE GUS
    mur10 = wall(410,65,37,112,screen_x,screen_y)
    mur11 = wall(517,0,13,170,screen_x,screen_y)
    mur12 = wall(618,0,118,63,screen_x,screen_y)
    mur13 = wall(657,68,75,215,screen_x,screen_y)
    mur14 = wall(518,254,150,21,screen_x,screen_y)  
    mur15 = wall(690,280,44,129,screen_x,screen_y)
    ##SDB
    mur16 = wall(519,333,170,27,screen_x,screen_y)
    mur17 = wall(660,355,34,54,screen_x,screen_y)
    mur18 = wall(520,357,43,105,screen_x,screen_y)
    mur19 = wall(724,407,10,70,screen_x,screen_y)  
    mur20 = wall(680,470,53,82,screen_x,screen_y)
    mur21 = wall(567,517,104,70,screen_x,screen_y)
    mur22 = wall(660,355,34,54,screen_x,screen_y)
    mur23 = wall(520,550,213,11,screen_x,screen_y)
    ##COULOIRS
    mur24 = wall(471,345,52,99,screen_x,screen_y)  
    mur25 = wall(265,289,91,40,screen_x,screen_y)
    mur26 = wall(410,663,326,38,screen_x,screen_y)
    ##PORTE ENTREE
    mur27 = wall(720,560,15,110,screen_x,screen_y)
    ##CUISINE
    mur28 = wall(210,650,200,50,screen_x,screen_y)
    mur29 = wall(290,500,124,55,screen_x,screen_y)  
    mur30 = wall(235,620,35,50,screen_x,screen_y)
    mur31 = wall(290,467,67,43,screen_x,screen_y)
    mur32 = wall(152,593,34,117,screen_x,screen_y)
    mur33 = wall(63,548,20,50,screen_x,screen_y)
    mur34 = wall(141,555,20,50,screen_x,screen_y)
    ##SALON
    mur35 = wall(35,450,170,31,screen_x,screen_y)
    mur36 = wall(35,380,150,70,screen_x,screen_y)  
    mur37 = wall(35,320,215,57,screen_x,screen_y)
    mur38 = wall(347,326,10,25,screen_x,screen_y)
    ##BUREAU
    mur43 = wall(35,300,80,20,screen_x,screen_y)
    mur39 = wall(35,240,6,55,screen_x,screen_y)
    mur40 = wall(35,194,50,48,screen_x,screen_y)
    mur41 = wall(90,190,100,30,screen_x,screen_y)
    ##PORTE BUREAU
    #mur42 = wall(180,210,10,120,screen_x,screen_y)
    ##EXTERIEUR
    mur44 = wall(988,0,12,707,screen_x,screen_y)
    mur45 = wall(850,70,150,370,screen_x,screen_y)
    mur46 = wall(850,440,15,87,screen_x,screen_y)
        
    liste_mur = [mur,mur2,mur3,mur4,mur5,mur6,mur7,mur8,mur9,mur10,mur11,mur12,mur13,
                  mur14,mur15,mur16,mur17,mur18,mur19,mur20,mur21,mur22,mur23,mur24,
                  mur25,mur26,mur28,mur29,mur30,mur31,mur32,mur33,mur34,mur35,
                  mur36,mur37,mur38,mur39,mur40,mur41,mur43,mur44,mur45,mur46,
                  #mur42,
                  mur27
                  ]

    for mur in liste_mur:
        pygame.draw.rect(gameDisplay,black,mur)
    gameDisplay.blit(fond, (screen_x,screen_y)) 
    
    return(liste_mur)

def level_1_3(gameDisplay,screen_x,screen_y):
    
    fond=pygame.image.load('Level/level_1.3.jpg').convert()
    fond_width,fond_height = fond.get_rect().size
    
    ##CHAMBRE PARENTS
    mur = wall(0,0,1000,10,screen_x,screen_y)
    mur2 = wall(0,0,42,430,screen_x,screen_y)
    mur3 = wall(0,430,12,140,screen_x,screen_y)
    mur4 = wall(0,571,167,137,screen_x,screen_y)  
    mur5 = wall(308,10,160,55,screen_x,screen_y)
    mur6 = wall(78,72,129,90,screen_x,screen_y)
    mur7 = wall(362,134,56,66,screen_x,screen_y)
    mur8 = wall(0,160,233,40,screen_x,screen_y)
    mur9 = wall(230,188,20,12,screen_x,screen_y)  
    ##CHAMBRE GUS
    mur10 = wall(410,65,37,112,screen_x,screen_y)
    mur11 = wall(517,0,13,170,screen_x,screen_y)
    mur12 = wall(618,0,118,63,screen_x,screen_y)
    mur13 = wall(657,68,75,215,screen_x,screen_y)
    mur14 = wall(518,254,150,21,screen_x,screen_y)  
    mur15 = wall(690,280,44,129,screen_x,screen_y)
    ##SDB
    mur16 = wall(519,333,170,27,screen_x,screen_y)
    mur17 = wall(660,355,34,54,screen_x,screen_y)
    mur18 = wall(520,357,43,105,screen_x,screen_y)
    mur19 = wall(724,407,10,70,screen_x,screen_y)  
    mur20 = wall(680,470,53,82,screen_x,screen_y)
    mur21 = wall(567,517,104,70,screen_x,screen_y)
    mur22 = wall(660,355,34,54,screen_x,screen_y)
    mur23 = wall(520,550,213,11,screen_x,screen_y)
    ##COULOIRS
    mur24 = wall(471,345,52,99,screen_x,screen_y)  
    mur25 = wall(265,289,91,40,screen_x,screen_y)
    mur26 = wall(410,663,326,38,screen_x,screen_y)
    ##PORTE ENTREE
    #mur27 = wall(720,560,15,110,screen_x,screen_y)
    ##CUISINE
    mur28 = wall(210,650,200,50,screen_x,screen_y)
    mur29 = wall(290,500,124,55,screen_x,screen_y)  
    mur30 = wall(235,620,35,50,screen_x,screen_y)
    mur31 = wall(290,467,67,43,screen_x,screen_y)
    mur32 = wall(152,593,34,117,screen_x,screen_y)
    mur33 = wall(63,548,20,50,screen_x,screen_y)
    mur34 = wall(141,555,20,50,screen_x,screen_y)
    ##SALON
    mur35 = wall(35,450,170,31,screen_x,screen_y)
    mur36 = wall(35,380,150,70,screen_x,screen_y)  
    mur37 = wall(35,320,215,57,screen_x,screen_y)
    mur38 = wall(347,326,10,25,screen_x,screen_y)
    ##BUREAU
    mur43 = wall(35,300,80,20,screen_x,screen_y)
    mur39 = wall(35,240,6,55,screen_x,screen_y)
    mur40 = wall(35,194,50,48,screen_x,screen_y)
    mur41 = wall(90,190,100,30,screen_x,screen_y)
    ##PORTE BUREAU
    #mur42 = wall(180,210,10,120,screen_x,screen_y)
    ##EXTERIEUR
    mur44 = wall(988,0,12,707,screen_x,screen_y)
    mur45 = wall(850,70,150,370,screen_x,screen_y)
    mur46 = wall(850,440,15,87,screen_x,screen_y)
        
    liste_mur = [mur,mur2,mur3,mur4,mur5,mur6,mur7,mur8,mur9,mur10,mur11,mur12,mur13,
                  mur14,mur15,mur16,mur17,mur18,mur19,mur20,mur21,mur22,mur23,mur24,
                  mur25,mur26,mur28,mur29,mur30,mur31,mur32,mur33,mur34,mur35,
                  mur36,mur37,mur38,mur39,mur40,mur41,mur43,mur44,mur45,mur46,
                  #mur42,
                  #mur27
                  ]

    for mur in liste_mur:
        pygame.draw.rect(gameDisplay,black,mur)
    gameDisplay.blit(fond, (screen_x,screen_y)) 
    
    return(liste_mur)

def level_1_4(gameDisplay,screen_x,screen_y):
    
    fond=pygame.image.load('Level/level_1.4.jpg').convert()
    fond_width,fond_height = fond.get_rect().size
    
    ##CHAMBRE PARENTS
    mur = wall(0,0,1000,10,screen_x,screen_y)
    mur2 = wall(0,0,42,430,screen_x,screen_y)
    mur3 = wall(0,430,12,140,screen_x,screen_y)
    mur4 = wall(0,571,167,137,screen_x,screen_y)  
    mur5 = wall(308,10,160,55,screen_x,screen_y)
    mur6 = wall(78,72,129,90,screen_x,screen_y)
    mur7 = wall(362,134,56,66,screen_x,screen_y)
    mur8 = wall(0,160,233,40,screen_x,screen_y)
    mur9 = wall(230,188,20,12,screen_x,screen_y)  
    ##CHAMBRE GUS
    mur10 = wall(410,65,37,112,screen_x,screen_y)
    mur11 = wall(517,0,13,170,screen_x,screen_y)
    mur12 = wall(618,0,118,63,screen_x,screen_y)
    mur13 = wall(657,68,75,215,screen_x,screen_y)
    mur14 = wall(518,254,150,21,screen_x,screen_y)  
    mur15 = wall(690,280,44,129,screen_x,screen_y)
    ##SDB
    mur16 = wall(519,333,170,27,screen_x,screen_y)
    mur17 = wall(660,355,34,54,screen_x,screen_y)
    mur18 = wall(520,357,43,105,screen_x,screen_y)
    mur19 = wall(724,407,10,70,screen_x,screen_y)  
    mur20 = wall(680,470,53,82,screen_x,screen_y)
    mur21 = wall(567,517,104,70,screen_x,screen_y)
    mur22 = wall(660,355,34,54,screen_x,screen_y)
    mur23 = wall(520,550,213,11,screen_x,screen_y)
    ##COULOIRS
    mur24 = wall(471,345,52,99,screen_x,screen_y)  
    mur25 = wall(265,289,91,40,screen_x,screen_y)
    mur26 = wall(410,663,326,38,screen_x,screen_y)
    ##PORTE ENTREE
    #mur27 = wall(720,560,15,110,screen_x,screen_y)
    ##CUISINE
    mur28 = wall(210,650,200,50,screen_x,screen_y)
    mur29 = wall(290,500,124,55,screen_x,screen_y)  
    mur30 = wall(235,620,35,50,screen_x,screen_y)
    mur31 = wall(290,467,67,43,screen_x,screen_y)
    mur32 = wall(152,593,34,117,screen_x,screen_y)
    mur33 = wall(63,548,20,50,screen_x,screen_y)
    mur34 = wall(141,555,20,50,screen_x,screen_y)
    ##SALON
    mur35 = wall(35,450,170,31,screen_x,screen_y)
    mur36 = wall(35,380,150,70,screen_x,screen_y)  
    mur37 = wall(35,320,215,57,screen_x,screen_y)
    mur38 = wall(347,326,10,25,screen_x,screen_y)
    ##BUREAU
    mur43 = wall(35,300,80,20,screen_x,screen_y)
    mur39 = wall(35,240,6,55,screen_x,screen_y)
    mur40 = wall(35,194,50,48,screen_x,screen_y)
    mur41 = wall(90,190,100,30,screen_x,screen_y)
    ##PORTE BUREAU
    mur42 = wall(180,210,10,120,screen_x,screen_y)
    ##EXTERIEUR
    mur44 = wall(988,0,12,707,screen_x,screen_y)
    mur45 = wall(850,70,150,370,screen_x,screen_y)
    mur46 = wall(850,440,15,87,screen_x,screen_y)
        
    liste_mur = [mur,mur2,mur3,mur4,mur5,mur6,mur7,mur8,mur9,mur10,mur11,mur12,mur13,
                  mur14,mur15,mur16,mur17,mur18,mur19,mur20,mur21,mur22,mur23,mur24,
                  mur25,mur26,mur28,mur29,mur30,mur31,mur32,mur33,mur34,mur35,
                  mur36,mur37,mur38,mur39,mur40,mur41,mur43,mur44,mur45,mur46,
                  mur42
                  #mur27
                  ]

    for mur in liste_mur:
        pygame.draw.rect(gameDisplay,black,mur)
    gameDisplay.blit(fond, (screen_x,screen_y)) 
    
    return(liste_mur)