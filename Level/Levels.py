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
        self.movement = True
        
        
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
    mur0 = wall(424,0,676,400,screen_x,screen_y)
    
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

def level_2O_ohne(gameDisplay,screen_x,screen_y):
    
    fond=pygame.image.load('Level/level_2O_ohne.jpg').convert()
    fond_width,fond_height = fond.get_rect().size
    
    #BATIMENT
    mur0 = wall(424,0,676,400,screen_x,screen_y)
    
    #LIMTES
    mur1 = wall(0,705,1000,10,screen_x,screen_y)
    mur2 = wall(998,0,10,707,screen_x,screen_y)
    mur3 = wall(0,0,10,707,screen_x,screen_y)
    mur4 = wall(0,0,101,10,screen_x,screen_y)
    mur5 = wall(176,0,825,10,screen_x,screen_y)
    
    #VOITURES
    mur10 = wall(390,441,103,50,screen_x,screen_y)
    mur6 = wall(472,483,530,214,screen_x,screen_y)

    liste_mur = [mur0, mur1
                  ,mur2,mur3,mur4,mur5,mur6,
                    mur10
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


def level_bonus(gameDisplay,screen_x,screen_y):
    
    fond=pygame.image.load('Level/nivo_bonus.jpg').convert()
    fond_width,fond_height = fond.get_rect().size
    
    #INTERIEUR BUS
    mur0 = wall(150,0,80,175,screen_x,screen_y)
    mur6 = wall(306,0,77,133,screen_x,screen_y)
    mur7 = wall(295,250,100,250,screen_x,screen_y)
    mur8 = wall(151,268,84,82,screen_x,screen_y)
    
    # #LIMTES
    mur1 = wall(0,-10,500,10,screen_x,screen_y)
    mur2 = wall(383,0,200,500,screen_x,screen_y)
    mur3 = wall(-10,0,10,500,screen_x,screen_y)
    mur4 = wall(0,442,500,60,screen_x,screen_y)
    
    ## POUBELLE
    mur5 = wall(0,284,91,216,screen_x,screen_y)
    
    liste_mur = [mur0, mur1
                    ,mur2,mur3,mur4,mur5,mur6
                    ,mur7,mur8
                    ]    

    for mur in liste_mur:
        pygame.draw.rect(gameDisplay,black,mur)
    
    #PNJ
    gameDisplay.blit(fond, (0,0)) 
    
    return(liste_mur)

def level_3N(gameDisplay,screen_x,screen_y):
    
    fond=pygame.image.load('Level/level_3N.jpg').convert()
    fond_width,fond_height = fond.get_rect().size
    
    #Boites aux lettres
    mur0 = wall(0,0,1000,707,screen_x,screen_y)
    
    #limites
    mur1 = wall(0,0,1000,5,screen_x,screen_y)
    mur2 = wall(-5,0,5,710,screen_x,screen_y)
    mur3 = wall(995,0,5,710,screen_x,screen_y)
    mur4 = wall(0,705,295,5,screen_x,screen_y)
    mur5 = wall(610,634,400,100,screen_x,screen_y)
    
    # bus
    mur7 = wall(490,0,510,300,screen_x,screen_y)
    mur8 = wall(0,118,243,182,screen_x,screen_y)
    mur9 = wall(332,86,200,44,screen_x,screen_y)
    mur10 = wall(293,0,710,72,screen_x,screen_y)
    mur11 = wall(299,130,35,2,screen_x,screen_y)
    
    # Voiture
    mur12 = wall(737,600,270,110,screen_x,screen_y)
    mur13 = wall(765,567,210,33,screen_x,screen_y)
    
    ## Entrée métro
    mur14 = wall(610,541,83,170,screen_x,screen_y)
    mur15 = wall(206,543,84,200,screen_x,screen_y)
    
    liste_mur = [mur0,mur1,mur2,mur3,mur4,mur5,mur7,
                   mur8,mur9,mur10,mur11,mur12,
                   mur13,mur14,mur15
                  ]    

    for mur in liste_mur:
        pygame.draw.rect(gameDisplay,black,mur)
    
    #PNJ
    gameDisplay.blit(fond, (screen_x,screen_y)) 

    
    return(liste_mur) 

def level_3C(gameDisplay,screen_x,screen_y):
    
    fond=pygame.image.load('Level/level_3C.jpg').convert()
    fond_width,fond_height = fond.get_rect().size
    
    #limites
    mur0 = wall(0,0,295,50,screen_x,screen_y)
    mur1 = wall(606,0,400,50,screen_x,screen_y)
    mur2 = wall(205,0,87,102,screen_x,screen_y)
    mur3 = wall(606,0,87,102,screen_x,screen_y)
    mur4 = wall(-5,0,5,707,screen_x,screen_y)
    mur5 = wall(0,705,1000,5,screen_x,screen_y)
    mur6 = wall(965,0,50,710,screen_x,screen_y)

    # PNJ
    mur7 = wall(0,147,217,35,screen_x,screen_y)
    mur8 = wall(119,123,36,30,screen_x,screen_y)
    mur9 = wall(165,482,55,55,screen_x,screen_y)
    mur10 = wall(845,469,45,68,screen_x,screen_y)
    mur11 = wall(810,150,55,58,screen_x,screen_y)
    
    # Ticket
    mur12 = wall(216,621,471,100,screen_x,screen_y)
    
    # #POUBELLE
    mur13 = wall(690,75,43,10,screen_x,screen_y)

    #portiques
    mur14 = wall(916,162,90,20,screen_x,screen_y)
    mur15 = wall(916,240,90,20,screen_x,screen_y)
    mur16 = wall(916,315,90,20,screen_x,screen_y)
    mur17 = wall(916,391,90,20,screen_x,screen_y)
    mur18 = wall(916,467,90,20,screen_x,screen_y)
    mur19 = wall(916,544,90,30,screen_x,screen_y)
    mur20 = wall(948,592,70,47,screen_x,screen_y)
    
    liste_mur = [mur0,mur1,mur2,mur3,mur4,mur5,
                 mur6,
                 mur7,
                   mur8,mur9,mur10,mur11,mur12,
                   mur13,mur14,mur15,mur16,mur17,mur18,mur19,
                   mur20
                  ]    

    for mur in liste_mur:
        pygame.draw.rect(gameDisplay,black,mur)
    
    #PNJ
    gameDisplay.blit(fond, (screen_x,screen_y)) 

    
    return(liste_mur) 

def level_3Copen(gameDisplay,screen_x,screen_y):
    
    fond=pygame.image.load('Level/level_3C.jpg').convert()
    fond_width,fond_height = fond.get_rect().size
    
    #limites
    mur0 = wall(0,0,295,50,screen_x,screen_y)
    mur1 = wall(606,0,400,50,screen_x,screen_y)
    mur2 = wall(205,0,87,102,screen_x,screen_y)
    mur3 = wall(606,0,87,102,screen_x,screen_y)
    mur4 = wall(-5,0,5,707,screen_x,screen_y)
    mur5 = wall(0,705,1000,5,screen_x,screen_y)
    mur6 = wall(965,0,50,320,screen_x,screen_y)
    mur6bis = wall(965,395,50,350,screen_x,screen_y)

    # PNJ
    mur7 = wall(0,147,217,35,screen_x,screen_y)
    mur8 = wall(119,123,36,30,screen_x,screen_y)
    mur9 = wall(165,482,55,55,screen_x,screen_y)
    mur10 = wall(845,469,45,68,screen_x,screen_y)
    mur11 = wall(810,150,55,58,screen_x,screen_y)
    
    # Ticket
    mur12 = wall(216,621,471,100,screen_x,screen_y)
    
    # #POUBELLE
    mur13 = wall(690,75,43,10,screen_x,screen_y)

    #portiques
    mur14 = wall(916,162,90,20,screen_x,screen_y)
    mur15 = wall(916,240,90,20,screen_x,screen_y)
    mur16 = wall(916,315,90,20,screen_x,screen_y)
    mur17 = wall(916,391,90,20,screen_x,screen_y)
    mur18 = wall(916,467,90,20,screen_x,screen_y)
    mur19 = wall(916,544,90,30,screen_x,screen_y)
    mur20 = wall(948,592,70,47,screen_x,screen_y)
    
    liste_mur = [mur0,mur1,mur2,mur3,mur4,mur5,
                 mur6,mur6bis,
                 mur7,
                   mur8,mur9,mur10,mur11,mur12,
                   mur13,mur14,mur15,mur16,mur17,mur18,mur19,
                   mur20
                  ]    

    for mur in liste_mur:
        pygame.draw.rect(gameDisplay,black,mur)
    
    #PNJ
    gameDisplay.blit(fond, (screen_x,screen_y)) 

    
    return(liste_mur)

def level_3E(gameDisplay,screen_x,screen_y):
    
    fond=pygame.image.load('Level/level_3E.jpg').convert()
    fond_width,fond_height = fond.get_rect().size
    
    # Limites
    mur0 = wall(0,0,1000,50,screen_x,screen_y)
    mur1 = wall(0,0,10,320,screen_x,screen_y)
    mur1bis = wall(0,395,10,350,screen_x,screen_y)
    mur2 = wall(0,705,1000,5,screen_x,screen_y)
    mur3 = wall(995,0,10,707,screen_x,screen_y)
    mur4 = wall(810,158,34,580,screen_x,screen_y)
    
    #POUBELLE
    mur5 = wall(702,77,30,7,screen_x,screen_y)
    
    #Banc
    mur6 = wall(210,582,212,150,screen_x,screen_y)
    mur7 = wall(485,607,212,100,screen_x,screen_y)
    mur8 = wall(190,683,586,50,screen_x,screen_y)
    
    #portiques
    mur14 = wall(0,162,84,20,screen_x,screen_y)
    mur15 = wall(0,240,84,20,screen_x,screen_y)
    mur16 = wall(0,315,84,20,screen_x,screen_y)
    mur17 = wall(0,391,84,20,screen_x,screen_y)
    mur18 = wall(0,467,84,20,screen_x,screen_y)
    mur19 = wall(0,544,84,30,screen_x,screen_y)

    liste_mur = [mur0,mur1,mur1bis,
                 mur2,mur3,mur4,mur5,mur6,mur7,mur8,
                   mur14,mur15,mur16,mur17,mur18,mur19
                  ]    

    for mur in liste_mur:
        pygame.draw.rect(gameDisplay,black,mur)
    
    #PNJ
    gameDisplay.blit(fond, (screen_x,screen_y)) 

    
    return(liste_mur) 

def level_3SE(gameDisplay,screen_x,screen_y):
    
    fond=pygame.image.load('Level/level_3SE.jpg').convert()
    fond_width,fond_height = fond.get_rect().size
    
    #Boites aux lettres
    mur0 = wall(0,0,849,50,screen_x,screen_y)
    mur1 = wall(995,0,10,707,screen_x,screen_y)
    mur2 = wall(-5,0,10,707,screen_x,screen_y)
    mur3 = wall(0,588,1000,130,screen_x,screen_y)
    mur4 = wall(805,0,56,368,screen_x,screen_y)
    
    #machines et clodo
    mur5 = wall(590,0,220,90,screen_x,screen_y)
    mur6 = wall(0,0,134,95,screen_x,screen_y)

    # Bancs
    mur7 = wall(60,347,215,50,screen_x,screen_y)
    mur8 = wall(407,360,215,36,screen_x,screen_y)
    
    liste_mur = [mur0,mur1,mur2,mur3,mur4,mur5,mur6,mur7,
                   mur8
                  ]    

    for mur in liste_mur:
        pygame.draw.rect(gameDisplay,black,mur)
    
    #PNJ
    gameDisplay.blit(fond, (screen_x,screen_y)) 

    
    return(liste_mur) 

def level_3SEmetro(gameDisplay,screen_x,screen_y):
    
    fond=pygame.image.load('Level/level_3SEmetro.jpg').convert()
    fond_width,fond_height = fond.get_rect().size
    
    #Boites aux lettres
    mur0 = wall(0,0,849,50,screen_x,screen_y)
    mur1 = wall(995,0,10,707,screen_x,screen_y)
    mur2 = wall(-5,0,10,707,screen_x,screen_y)
    mur3 = wall(0,536,1000,130,screen_x,screen_y)
    mur4 = wall(805,0,56,368,screen_x,screen_y)
    
    #machines et clodo
    mur5 = wall(590,0,220,90,screen_x,screen_y)
    mur6 = wall(0,0,134,95,screen_x,screen_y)

    # Bancs
    mur7 = wall(60,347,215,50,screen_x,screen_y)
    mur8 = wall(407,360,215,36,screen_x,screen_y)
    
    liste_mur = [mur0,mur1,mur2,mur3,mur4,mur5,mur6,mur7,
                   mur8
                  ]    

    for mur in liste_mur:
        pygame.draw.rect(gameDisplay,black,mur)
    
    #PNJ
    gameDisplay.blit(fond, (screen_x,screen_y)) 

    
    return(liste_mur) 

def level_4(gameDisplay,screen_x,screen_y):
    fond=pygame.image.load('Level/level_4.jpg').convert()
    fond_width,fond_height = fond.get_rect().size
    
    #Limites
    mur0 = wall(0,0,1000,280,screen_x,screen_y)
    mur1 = wall(0,468,1000,200,screen_x,screen_y)
    mur9 = wall(-1,0,4,707,screen_x,screen_y)
    mur10 = wall(998,0,4,707,screen_x,screen_y)

    #Sièges
    mur2 = wall(0,279,142,50,screen_x,screen_y)
    mur3 = wall(245,279,800,50,screen_x,screen_y)
    mur4 = wall(0,388,86,60,screen_x,screen_y)
    mur5 = wall(86,412,69,65,screen_x,screen_y)
    mur6 = wall(247,413,73,65,screen_x,screen_y)
    mur7 = wall(380,412,294,65,screen_x,screen_y)
    mur8 = wall(706,412,70,65,screen_x,screen_y)
    
    #gens
    mur11 = wall(531,392,40,20,screen_x,screen_y)    
    mur12 = wall(827,300,52,55,screen_x,screen_y)
    mur13 = wall(917,380,62,88,screen_x,screen_y)
    
    liste_mur = [mur0,mur1,mur2,mur3,mur4,mur5,mur6,mur7,
                   mur8,mur9,mur10,
                   mur11,mur12,mur13
                  ]    

    for mur in liste_mur:
        pygame.draw.rect(gameDisplay,black,mur)
    
    #PNJ
    gameDisplay.blit(fond, (screen_x,screen_y)) 

    
    return(liste_mur)     

def level_5M(gameDisplay,screen_x,screen_y):
    fond=pygame.image.load('Level/level_5_metro.jpg').convert()
    fond_width,fond_height = fond.get_rect().size
    
    #Limites
    mur0 = wall(0,0,1000,45,screen_x,screen_y)
    mur1 = wall(998,0,2,707,screen_x,screen_y)
    mur9 = wall(0,532,1000,150,screen_x,screen_y)
    mur10 = wall(0,0,1,707,screen_x,screen_y)

    #Escaliers
    mur2 = wall(0,140,355,90,screen_x,screen_y)
    mur3 = wall(0,155,196,97,screen_x,screen_y)

    #poubelle
    mur4 = wall(950,86,50,53,screen_x,screen_y)
    
    #Bancs
    mur5 = wall(420,349,215,51,screen_x,screen_y)
    mur6 = wall(770,350,215,51,screen_x,screen_y)
    
    #PNJ
    mur7 = wall(720,285,47,55,screen_x,screen_y)
    mur8 = wall(0,340,55,65,screen_x,screen_y)
    mur11 = wall(692,38,43,50,screen_x,screen_y)
    mur12 = wall(273,212,64,64,screen_x,screen_y)
        
    liste_mur = [mur0,
                  mur1,mur2,mur3,mur4,mur5,mur6,mur7,
                     mur8,mur9,mur10,
                     mur11,mur12
                  ]    

    for mur in liste_mur:
        pygame.draw.rect(gameDisplay,black,mur)
    
    #PNJ
    gameDisplay.blit(fond, (screen_x,screen_y)) 

    
    return(liste_mur)

def level_5_esc1(gameDisplay,screen_x,screen_y):
    fond=pygame.image.load('Level/level_5_esc1.jpg').convert()
    fond_width,fond_height = fond.get_rect().size
    
    #Limites
    mur0 = wall(0,0,500,130,0,0)
    mur1 = wall(0,0,1,500,0,0)
    mur9 = wall(300,130,200,340,0,0)
    mur10 = wall(0,500,500,1,0,0)

    #Escaliers
    mur2 = wall(204,406,300,140,screen_x,screen_y)
    mur3 = wall(204,615,300,200,screen_x,screen_y)
    mur5 = wall(244,600,300,200,screen_x,screen_y)
    
    #Poubelle
    mur4 = wall(18,350,40,30,screen_x,screen_y)
    
    liste_mur = [mur0
                 ,mur1,
                 mur2,mur3,mur4,mur5,
                 mur9,mur10,
                  ]    

    for mur in liste_mur:
        pygame.draw.rect(gameDisplay,black,mur)
    
    #PNJ
    gameDisplay.blit(fond, (0,0)) 
    
    return(liste_mur)   

def level_5_esc2(gameDisplay,screen_x,screen_y):
    fond=pygame.image.load('Level/level_5_esc2.jpg').convert()
    fond_width,fond_height = fond.get_rect().size
    
    #Limites
    mur0 = wall(0,0,500,130,0,0)
    mur1 = wall(0,0,240,707,0,0)
    mur9 = wall(500,0,1,707,0,0)
    mur10 = wall(0,500,500,1,0,0)

    #Escaliers
    mur2 = wall(0,200,300,140,0,0)
    mur3 = wall(253,408,45,100,0,0)
    
    #Tox
    mur4 = wall(430,111,86,60,screen_x,screen_y)
    
    liste_mur = [mur0
                  ,mur1,mur2,mur3,mur4,mur9,mur10
                  ]    

    for mur in liste_mur:
        pygame.draw.rect(gameDisplay,black,mur)
    
    #PNJ
    gameDisplay.blit(fond, (0,0)) 

    
    return(liste_mur)            

def level_5NO(gameDisplay,screen_x,screen_y):
    fond=pygame.image.load('Level/level_5NO.jpg').convert()
    fond_width,fond_height = fond.get_rect().size
    
    #Limites
    mur0 = wall(0,0,1000,55,screen_x,screen_y)
    mur1 = wall(1000,0,1,395,screen_x,screen_y)
    mur9 = wall(1000,454,1,300,screen_x,screen_y)
    mur10 = wall(0,0,1,707,screen_x,screen_y)
    mur11 = wall(0,707,293,1,screen_x,screen_y)
    mur12 = wall(642,707,400,1,screen_x,screen_y)

    #Distributeurs
    mur2 = wall(0,200,95,364,screen_x,screen_y)
    mur3 = wall(95,290,42,267,screen_x,screen_y)

    #PNJ
    mur4 = wall(235,513,79,77,screen_x,screen_y)
    
    #Portiques
    mur5 = wall(905,200,100,195,screen_x,screen_y)
    mur6 = wall(905,454,100,300,screen_x,screen_y)
    
    #Trucs escaliers
    mur7 = wall(191,633,98,75,screen_x,screen_y)
    mur8 = wall(642,633,98,75,screen_x,screen_y)
    
    #Bancs
    mur13 = wall(133,97,241,53,screen_x,screen_y)
    mur14 = wall(512,97,241,53,screen_x,screen_y)
        
    liste_mur = [mur0
                 ,mur1,
                 mur2,mur3,mur4,mur5,mur6,mur7,
                    mur8,
                 mur9,mur10,mur11,mur12,
                 mur13,mur14
                  ]    

    for mur in liste_mur:
        pygame.draw.rect(gameDisplay,black,mur)
    
    #PNJ
    gameDisplay.blit(fond, (screen_x,screen_y)) 
    
    return(liste_mur)               

def level_5N(gameDisplay,screen_x,screen_y):
    fond=pygame.image.load('Level/level_5N.jpg').convert()
    fond_width,fond_height = fond.get_rect().size
    
    #Limites
    mur0 = wall(0,0,1000,55,screen_x,screen_y)
    mur1 = wall(1000,200,1,507,screen_x,screen_y)
    mur9 = wall(0,707,1000,1,screen_x,screen_y)
    mur10 = wall(0,0,12,395,screen_x,screen_y)
    mur11 = wall(0,454,12,300,screen_x,screen_y)

    #Bancs
    mur2 = wall(132,100,241,53,screen_x,screen_y)
    mur3 = wall(511,100,241,53,screen_x,screen_y)
    mur4 = wall(515,366,241,53,screen_x,screen_y)
    
    #Portiques
    mur5 = wall(0,197,94,178,screen_x,screen_y)
    mur6 = wall(0,455,94,300,screen_x,screen_y)
    
    #PNJ
    mur7 = wall(256,388,62,82,screen_x,screen_y)
    mur8 = wall(520,589,60,120,screen_x,screen_y)
    
    #Poubelles
    mur12 = wall(705,612,58,100,screen_x,screen_y)
    mur13 = wall(763,647,114,59,screen_x,screen_y)
    
    liste_mur = [mur0
                 ,mur1,
                 mur2,mur3,mur4,mur5,mur6,mur7,
                    mur8,
                 mur9,mur10,mur11
                 ,mur12,mur13
                  ]    

    for mur in liste_mur:
        pygame.draw.rect(gameDisplay,black,mur)
    
    #PNJ
    gameDisplay.blit(fond, (screen_x,screen_y)) 

    
    return(liste_mur)

def level_5O(gameDisplay,screen_x,screen_y):
    fond=pygame.image.load('Level/level_5O.jpg').convert()
    fond_width,fond_height = fond.get_rect().size
    
    #Limites
    mur0 = wall(0,0,297,60,screen_x,screen_y)
    mur1 = wall(605,0,400,60,screen_x,screen_y)
    mur9 = wall(895,0,101,298,screen_x,screen_y)
    mur10 = wall(998,536,2,200,screen_x,screen_y)
    mur11 = wall(0,0,30,707,screen_x,screen_y)    
    mur12 = wall(0,705,552,2,screen_x,screen_y)
    mur13 = wall(847,705,153,2,screen_x,screen_y)
    mur14 = wall(28,431,64,275,screen_x,screen_y)    
    mur15 = wall(98,488,60,218,screen_x,screen_y)
    mur16 = wall(155,553,75,160,screen_x,screen_y)
    mur17 = wall(229,626,82,82,screen_x,screen_y)

    #Ecran
    mur2 = wall(333,317,252,92,screen_x,screen_y)
    mur3 = wall(353,414,200,12,screen_x,screen_y)
    mur4 = wall(280,335,46,60,screen_x,screen_y)
    mur5 = wall(570,335,46,60,screen_x,screen_y)
    
    #Trucs escaliers
    mur6 = wall(205,0,92,111,screen_x,screen_y)
    mur7 = wall(605,0,128,111,screen_x,screen_y)    
    
    liste_mur = [mur0
                  ,mur1,mur2,mur3,mur4,mur5,mur6,mur7,
                    mur9,mur10,
                    mur11,mur12,mur13,
                    mur14,mur15,mur16,mur17
                  ]    

    for mur in liste_mur:
        pygame.draw.rect(gameDisplay,black,mur)
    
    #PNJ
    gameDisplay.blit(fond, (screen_x,screen_y)) 

    
    return(liste_mur)   

def level_5SO(gameDisplay,screen_x,screen_y):
    fond=pygame.image.load('Level/level_5SO.jpg').convert()
    fond_width,fond_height = fond.get_rect().size
    
    #Limites
    mur0 = wall(0,0,552,2,screen_x,screen_y)
    mur1 = wall(847,0,153,25,screen_x,screen_y)
    mur9 = wall(0,0,163,707,screen_x,screen_y)
    mur10 = wall(0,660,1000,45,screen_x,screen_y)
    mur2 = wall(953,154,49,552,screen_x,screen_y)
    
    #Toilettes
    mur3 = wall(150,0,305,145,screen_x,screen_y)
    mur4 = wall(150,205,161,145,screen_x,screen_y)
    mur5 = wall(150,412,161,145,screen_x,screen_y)
    mur6 = wall(280,630,32,73,screen_x,screen_y)
    
    #Lavabos
    mur7 = wall(593,345,90,50,screen_x,screen_y)
    mur8 = wall(593,446,90,50,screen_x,screen_y)
    mur11 = wall(593,570,90,50,screen_x,screen_y)    
    mur12 = wall(625,659,54,36,screen_x,screen_y)
    mur13 = wall(397,642,131,40,screen_x,screen_y)
    
    #mur milieu
    mur14 = wall(668,118,40,590,screen_x,screen_y)
    #poubelle
    mur15 = wall(644,252,33,24,screen_x,screen_y)

    #Stand
    mur16 = wall(764,437,208,154,screen_x,screen_y)    
    
    liste_mur = [mur0
                  ,mur1,mur2,mur3,mur4,mur5,mur6,mur7,
                    mur8,mur9,mur10,
                    mur11,mur12,mur13,
                    mur14,mur15,mur16
                  ]    

    for mur in liste_mur:
        pygame.draw.rect(gameDisplay,black,mur)
    
    #PNJ
    gameDisplay.blit(fond, (screen_x,screen_y)) 

    
    return(liste_mur)   

def level_5C(gameDisplay,screen_x,screen_y):
    fond=pygame.image.load('Level/level_5C.jpg').convert()
    fond_width,fond_height = fond.get_rect().size
    
    #Limites
    mur0 = wall(0,0,1000,2,screen_x,screen_y)
    mur1 = wall(995,0,5,707,screen_x,screen_y)
    mur9 = wall(0,0,2,298,screen_x,screen_y)
    mur10 = wall(0,536,2,200,screen_x,screen_y)
    mur11 = wall(0,574,437,137,screen_x,screen_y)    
    mur12 = wall(700,705,400,5,screen_x,screen_y)

    
    #Vitrines
    mur2 = wall(0,0,250,225,screen_x,screen_y)
    mur3 = wall(412,380,590,10,screen_x,screen_y)
    
    #Rayons
    mur4 = wall(348,0,371,60,screen_x,screen_y)
    mur5 = wall(926,0,75,395,screen_x,screen_y)
    mur6 = wall(905,66,27,273,screen_x,screen_y)
    mur7 = wall(479,78,101,90,screen_x,screen_y)
    mur8 = wall(661,200,109,90,screen_x,screen_y)
    
    #PNJ
    mur13 = wall(777,40,62,60,screen_x,screen_y)    
    mur14 = wall(862,447,55,60,screen_x,screen_y)    

    liste_mur = [mur0
                  ,mur1,mur2,mur3,mur4,mur5,mur6,mur7,
                    mur8,mur9,mur10,
                    mur11,mur12,mur13,mur14
                  ]    

    for mur in liste_mur:
        pygame.draw.rect(gameDisplay,black,mur)
    
    #PNJ
    gameDisplay.blit(fond, (screen_x,screen_y)) 

    
    return(liste_mur)          
             
def level_5S(gameDisplay,screen_x,screen_y):
    fond=pygame.image.load('Level/level_5S.jpg').convert()
    fond_width,fond_height = fond.get_rect().size
    
    #Limites
    mur0 = wall(0,0,437,100,screen_x,screen_y)
    mur1 = wall(700,0,300,2,screen_x,screen_y)
    mur9 = wall(0,285,35,425,screen_x,screen_y)
    mur10 = wall(967,0,33,707,screen_x,screen_y)
    mur11 = wall(0,669,1000,40,screen_x,screen_y)    

    #Meubles
    mur2 = wall(0,512,261,102,screen_x,screen_y)
    mur3 = wall(376,650,425,25,screen_x,screen_y)
    mur4 = wall(466,470,205,105,screen_x,screen_y)
    mur5 = wall(216,174,787,120,screen_x,screen_y)
    mur6 = wall(280,280,695,57,screen_x,screen_y)
    mur7 = wall(736,288,194,68,screen_x,screen_y)
    
    #PNJ
    mur8 = wall(884,384,50,55,screen_x,screen_y)
    mur12 = wall(693,590,51,60,screen_x,screen_y)
    mur13 = wall(920,33,58,72,screen_x,screen_y)
    
    liste_mur = [mur0
                  ,mur1,mur2,mur3,mur4,mur5,mur6,mur7,
                    mur8,mur9,mur10,
                    mur11,mur12,mur13
                  ]    

    for mur in liste_mur:
        pygame.draw.rect(gameDisplay,black,mur)
    
    #PNJ
    gameDisplay.blit(fond, (screen_x,screen_y)) 

    
    return(liste_mur)   

def level_6O(gameDisplay,screen_x,screen_y):
    fond=pygame.image.load('Level/level_6O.png').convert()
    fond_width,fond_height = fond.get_rect().size
    
    #Limites
    mur0 = wall(0,0,500,1,0,0)
    mur1 = wall(0,0,2,500,0,0)
    mur9 = wall(500,0,1,500,0,0)
    mur10 = wall(0,500,500,1,0,0)

    #Escaliers
    # mur2 = wall(0,200,300,140,0,0)
    # mur3 = wall(253,408,45,100,0,0)
    
    # #Tox
    # mur4 = wall(430,111,86,60,screen_x,screen_y)
    
    liste_mur = [mur0
                  ,mur1,
                  #mur2,mur3,mur4,
                  mur9,mur10
                  ]    

    for mur in liste_mur:
        pygame.draw.rect(gameDisplay,black,mur)
    
    #PNJ
    gameDisplay.blit(fond, (0,0)) 

    
    return(liste_mur)            


        