# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 16:40:54 2021

@author: basti
"""
import pygame

pygame.init()

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
        
class pnj(pygame.sprite.Sprite):
    def __init__(self,x_start,y_start,rel_x,rel_y,img_start,side_start):
        
        self.side = side_start
        self.image = img_start
        largeur,hauteur = self.image.get_rect().size
        
        self.rect = self.image.get_rect()
        self.rect.x = x_start + rel_x 
        self.rect.y = y_start + rel_y
        
        
    def move(self, spawnx, spawny, speedx, speedy):
        spawnx += speedx
        spawny += speedy
        return(spawnx,spawny)
        
    def collisions_pnj (self,liste_objet,speedx, speedy,img_d,img_g,scheme_move):
        if scheme_move == 0:
            for objet in liste_objet :
                    
                if self.rect.colliderect(objet):
                        
                    if abs (objet.left - self.rect.right) <= 10:
                        speedx = -1
                        self.side = "left"
                        self.image = img_g
        
                    if abs (objet.right - self.rect.left) <= 10:
                        speedx = 1
                        self.side = "right"
                        self.image = img_d
        
                else:
                    speedx = speedx
                    speedy = speedy            
            
        elif scheme_move == 1 :
            for objet in liste_objet :
                    
                if self.rect.colliderect(objet):
        
                    if abs (objet.top - self.rect.bottom) <= 10:
                        speedx = -1
                        speedy = 0
                        self.side = "left"
                        self.image = img_g
                    if abs (objet.bottom - self.rect.top) <= 10:
                        speedx = 1
                        speedy = 0
                        self.side = "right"
                        self.image=img_d

                    if abs (objet.left - self.rect.right) <= 10:
                        speedx = 0
                        speedy = 1
                        self.side = "down"
        
                    if abs (objet.right - self.rect.left) <= 10:
                        speedx = 0
                        speedy = -1
                        self.side = "up"
        
                else:
                    speedx = speedx
                    speedy = speedy
        
        return(speedx,speedy)
            



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
    
def level_2(gameDisplay,screen_x,screen_y):
    
    fond=pygame.image.load('Level/level_2E.jpg').convert()
    fond_width,fond_height = fond.get_rect().size
    
    #HALL
    mur0 = wall(0,507,240,200,screen_x,screen_y)
    mur1 = wall(0,0,25,707,screen_x,screen_y)
    mur2 = wall(0,0,945,30,screen_x,screen_y)
    mur3 = wall(231,293,52,415,screen_x,screen_y)
    mur4 = wall(606,0,54,158,screen_x,screen_y)
    mur5 = wall(606,280,30,270,screen_x,screen_y)
    mur6 = wall(282,275,57,75,screen_x,screen_y)
    mur7 = wall(275,466,151,10,screen_x,screen_y)
    
    #CAVE
    mur8 = wall(635,135,170,52,screen_x,screen_y)
    mur9 = wall(635,278,178,63,screen_x,screen_y)
    mur10 = wall(635,10,305,61,screen_x,screen_y)
    mur11 = wall(635,70,53,70,screen_x,screen_y)
    mur12 = wall(888,0,55,390,screen_x,screen_y)
    mur13 = wall(872,390,68,164,screen_x,screen_y)
    mur14 = wall(635,415,320,63,screen_x,screen_y)
    
    #EXT
    mur15 = wall(644,478,300,37,screen_x,screen_y)
    mur16 = wall(688,516,264,52,screen_x,screen_y)
    mur19 = wall(775,560,120,22,screen_x,screen_y)
    
    #limites
    mur17 = wall(0,700,1000,7,screen_x,screen_y)
    mur18 = wall(999,0,10,708,screen_x,screen_y)
    
    liste_mur = [mur0,mur1,mur2,mur3,mur4,mur5,mur6,mur7,
                 mur8,mur9,mur10,mur11,mur12,mur13,mur14,
                 mur15,mur16,mur17,mur18,mur19
                  ]    

    for mur in liste_mur:
        pygame.draw.rect(gameDisplay,black,mur)
    
    #PNJ

    gameDisplay.blit(fond, (screen_x,screen_y)) 
    
    return(liste_mur)

def level_2NE(gameDisplay,screen_x,screen_y):
    
    fond=pygame.image.load('Level/level_2NE.jpg').convert()
    fond_width,fond_height = fond.get_rect().size
    
    #HAIE
    mur0 = wall(823,364,107,350,screen_x,screen_y)
    mur1 = wall(771,433,55,75,screen_x,screen_y)
    
    #MUR BATIMENT
    mur2 = wall(116,0,885,20,screen_x,screen_y)
    mur3 = wall(768,20,240,20,screen_x,screen_y)
    mur4 = wall(884,40,110,20,screen_x,screen_y)
    mur5 = wall(120,0,50,35,screen_x,screen_y)
    
    #FONTAINE
    mur6 = wall(183,250,350,61,screen_x,screen_y)
    mur13 = wall(195,220,316,130,screen_x,screen_y)
    mur14 = wall(209,199,290,164,screen_x,screen_y)
    mur15 = wall(218,185,273,200,screen_x,screen_y)
    mur16 = wall(235,170,231,232,screen_x,screen_y)
    mur17 = wall(256,156,195,270,screen_x,screen_y)
    mur18 = wall(281,146,144,303,screen_x,screen_y)
    mur19 = wall(306,134,87,326,screen_x,screen_y)
    
    #POUBELLE
    mur7 = wall(627,180,40,20,screen_x,screen_y)
    
    #limites
    mur8 = wall(0,0,1000,2,screen_x,screen_y)
    mur9 = wall(998,0,10,707,screen_x,screen_y)
    mur10 = wall(0,705,920,10,screen_x,screen_y)
    mur11 = wall(-10,0,11,430,screen_x,screen_y)
    mur12 = wall(-10,552,11,155,screen_x,screen_y)
    
    liste_mur = [mur0,mur1,mur2,mur3,mur4,mur5,mur6,mur7,
                 mur8,mur9,mur10,mur11,mur12,
                 mur13,mur14,mur15,mur16,mur17,mur18,mur19
                  ]    

    for mur in liste_mur:
        pygame.draw.rect(gameDisplay,black,mur)
    
    #PNJ

    gameDisplay.blit(fond, (screen_x,screen_y)) 
    
    return(liste_mur)

def level_2NO(gameDisplay,screen_x,screen_y):
    
    fond=pygame.image.load('Level/level_2NO.jpg').convert()
    fond_width,fond_height = fond.get_rect().size
    
    #BATIMENT
    mur0 = wall(578,0,425,435,screen_x,screen_y)
    
    #LIMTES
    mur1 = wall(0,0,578,75,screen_x,screen_y)
    mur2 = wall(998,552,10,160,screen_x,screen_y)
    mur3 = wall(0,0,10,707,screen_x,screen_y)
    mur4 = wall(0,705,101,10,screen_x,screen_y)
    mur5 = wall(176,705,825,10,screen_x,screen_y)
    
    #VOITURES
    mur8 = wall(0,75,200,50,screen_x,screen_y)
    mur9 = wall(12,119,237,65,screen_x,screen_y)
    mur10 = wall(0,333,227,90,screen_x,screen_y)
    
    # #POUBELLE
    mur6 = wall(530,431,50,5,screen_x,screen_y)
    mur7 = wall(551,422,40,9,screen_x,screen_y)
    
    liste_mur = [mur0, mur1,mur2,mur3,mur4,mur5,mur6,mur7,
                   mur8,mur9,mur10
                   ]    
 
    for mur in liste_mur:
        pygame.draw.rect(gameDisplay,black,mur)
    
    #PNJ
    gameDisplay.blit(fond, (screen_x,screen_y))

    
    return(liste_mur)

def level_2O(gameDisplay,screen_x,screen_y):
    
    fond=pygame.image.load('Level/level_2O.jpg').convert()
    fond_width,fond_height = fond.get_rect().size
    
    #BATIMENT
    mur0 = wall(424,0,676,410,screen_x,screen_y)
    
    #LIMTES
    mur1 = wall(0,705,1000,10,screen_x,screen_y)
    mur2 = wall(998,0,10,707,screen_x,screen_y)
    mur3 = wall(0,0,10,707,screen_x,screen_y)
    mur4 = wall(0,0,101,10,screen_x,screen_y)
    mur5 = wall(176,0,825,10,screen_x,screen_y)
    
    #VOITURES
    mur8 = wall(0,566,310,141,screen_x,screen_y)
    mur9 = wall(144,530,46,150,screen_x,screen_y)
    mur10 = wall(390,450,103,50,screen_x,screen_y)
    mur6 = wall(472,493,530,214,screen_x,screen_y)

    liste_mur = [mur0, mur1
                  ,mur2,mur3,mur4,mur5,mur6,
                    mur8,mur9,mur10
                   ]    

    for mur in liste_mur:
        pygame.draw.rect(gameDisplay,black,mur)
    
    #PNJ
    gameDisplay.blit(fond, (screen_x,screen_y)) 

    
    return(liste_mur)

def level_2NN(gameDisplay,screen_x,screen_y):
    
    fond=pygame.image.load('Level/level_2NN.jpg').convert()
    fond_width,fond_height = fond.get_rect().size
    
    #POUBELLE
    mur0 = wall(345,0,660,438,screen_x,screen_y)
    mur6 = wall(591,420,65,135,screen_x,screen_y)
    
    #LIMTES
    mur1 = wall(0,705,178,10,screen_x,screen_y)
    mur2 = wall(253,605,800,110,screen_x,screen_y)
    mur3 = wall(0,0,178,707,screen_x,screen_y)
    mur4 = wall(0,0,1000,400,screen_x,screen_y)
    mur5 = wall(654,0,350,707,screen_x,screen_y)
    
    liste_mur = [mur0, mur1
                   ,mur2,mur3,mur4,mur5,mur6
                   ]    

    for mur in liste_mur:
        pygame.draw.rect(gameDisplay,black,mur)
    
    #PNJ
    gameDisplay.blit(fond, (screen_x,screen_y)) 

    
    return(liste_mur)

def level_2N(gameDisplay,screen_x,screen_y):
    
    fond=pygame.image.load('Level/level_2N.jpg').convert()
    fond_width,fond_height = fond.get_rect().size
    
    #Boites aux lettres
    mur0 = wall(40,0,102,8,screen_x,screen_y)
    
    #escalier
    mur1 = wall(0,133,31,11,screen_x,screen_y)
    mur2 = wall(35,148,31,11,screen_x,screen_y)
    mur23 = wall(0,47,31,1,screen_x,screen_y)
    mur24 = wall(31,63,31,1,screen_x,screen_y)
    
    #but
    mur3 = wall(535,66,82,100,screen_x,screen_y)
    mur4 = wall(555,48,62,120,screen_x,screen_y)
    mur5 = wall(575,28,42,140,screen_x,screen_y)
    mur6 = wall(599,0,18,168,screen_x,screen_y)

    #ARBRE
    mur15 = wall(430,243,355,47,screen_x,screen_y)
    mur16 = wall(455,222,339,100,screen_x,screen_y)
    mur17 = wall(466,177,323,150,screen_x,screen_y)
    mur18 = wall(500,155,270,200,screen_x,screen_y)
    mur19 = wall(524,136,200,233,screen_x,screen_y)
    mur21 = wall(616,110,60,255,screen_x,screen_y)
    mur22 = wall(600,345,62,90,screen_x,screen_y)
    
    #POUBELLE
    mur7 = wall(115,422,40,20,screen_x,screen_y)
    mur20 = wall(80,432,40,15,screen_x,screen_y)
    
    #limites
    mur8 = wall(0,0,172,2,screen_x,screen_y)
    mur9 = wall(252,0,751,2,screen_x,screen_y)
    mur10 = wall(998,0,10,430,screen_x,screen_y)
    mur11 = wall(998,552,10,160,screen_x,screen_y)
    mur12 = wall(0,705,1000,5,screen_x,screen_y)
    mur13 = wall(0,0,10,430,screen_x,screen_y)
    mur14 = wall(0,552,10,160,screen_x,screen_y)
    
    liste_mur = [mur0,mur1,mur2,mur3,mur4,mur5,mur6,mur7,
                  mur8,mur9,mur10,mur11,mur12,
                  mur13,mur14,mur15,mur16,mur17,mur18,mur19,
                  mur20,mur21,mur22,mur23,mur24
                  ]    

    for mur in liste_mur:
        pygame.draw.rect(gameDisplay,black,mur)
    
    #PNJ
    gameDisplay.blit(fond, (screen_x,screen_y)) 

    
    return(liste_mur)