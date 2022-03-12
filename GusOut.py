# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 16:02:54 2021

@author: basti
"""
import pygame
#import pandas as pd

from Story.Fonctions import *
from Story.histoire import *
from Story.trigger import *
from Level.Levels import *
from settings import *

pygame.mixer.init()
pygame.init()
pygame.font.init()

Gus = Gus()
sac = sac_a_dos()
action=action_key()
tr = trigger()

def launch(Gus):
    if Gus.level == 1:
        nivo1(sac,action,Gus,tr)
    if Gus.level >= 2 and Gus.level < 3:
        nivo2(sac,action,Gus,tr)      
    if Gus.level == 0:
        bonus_level(sac,action,Gus,tr)
    if Gus.level >= 3 and Gus.level < 4:
        nivo3(sac,action,Gus,tr)
    if Gus.level == 99:
        music_level(sac,action,Gus,tr)
    if Gus.level >= 3 and Gus.level < 4:
        nivo3(sac,action,Gus,tr)
    if Gus.level >= 4 and Gus.level < 5:
        end_game("nivo 4")
        
gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    demarrer = pygame.Rect(25,25,450,130)
    charger = pygame.Rect(25,180,450,130)
    quitter = pygame.Rect(25,335,450,130)
    
    pygame.draw.rect(screen,green,demarrer)
    pygame.draw.rect(screen,blue,charger)
    pygame.draw.rect(screen,red,quitter)
    
    dem_font = pygame.font.SysFont('corbel', 40, bold=True)

    text_demarrer = dem_font.render("DEMARRER (ENTER)", False, (0, 0, 0))
    screen.blit(text_demarrer,(80,75))
    text_load = dem_font.render("CHARGER (L)", False, (0, 0, 0))
    screen.blit(text_load,(140,230))
    text_quitter = dem_font.render("QUITTER (Q)", False, (0, 0, 0))
    screen.blit(text_quitter,(150,395))
    
    keys=pygame.key.get_pressed()
    
    if keys[pygame.K_RETURN]:
        enter_s.play()
        launch(Gus)
    if keys[pygame.K_l]:
        enter_s.play()
        Gus,sac,tr=load(Gus,sac,tr)
        launch(Gus)
    if keys[pygame.K_q]:
        other_s.play()
        pygame.quit() 
        
    pygame.display.update()


pygame.quit()
quit()