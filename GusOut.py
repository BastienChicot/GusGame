# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 16:02:54 2021

@author: basti
"""
import pygame
from Story.Fonctions import *
from Story.histoire import *
from Level.Levels import *
from settings import *

pygame.init()
pygame.font.init()

Gus = Gus()
sac = sac_a_dos()
action=action_key()

if Gus.level == 1:
    nivo1(sac,action,Gus)

if Gus.level == 2:
    nivo2(sac,action,Gus)


pygame.quit()
quit()