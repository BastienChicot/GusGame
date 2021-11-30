# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 15:43:41 2021

@author: basti
"""
import pygame

def collisions (liste_objet,x,y,rect_gugus,x_change,y_change):

    for objet in liste_objet :
            
        if objet.colliderect(rect_gugus):
    
    # index = rect_gugus.collidelist(liste_objet)
    
    # if index >= 0 : 
        
    #     objet = liste_objet[index]

            if abs (objet.top - rect_gugus.bottom) <= 10 and y_change >= 2.5:
                y_change = 0
            if abs (objet.bottom - rect_gugus.top) <= 10 and y_change <= -2.5:
                y_change = 0
            if abs (objet.left - rect_gugus.right) <= 10 and x_change >= 2.5:
                x_change = 0
            if abs (objet.right - rect_gugus.left) <= 10 and x_change <= -2.5:
                x_change = 0
        else:
            x_change = x_change
            y_change = y_change
        
    x += x_change
    y += y_change
    
    return(x,y)

def move_gugus(gugus,x_change,y_change):

    gugus_face = pygame.image.load('Gus/Gus.png')
    gugus_dos = pygame.image.load('Gus/Gus_dos.png')
    gugus_droite = pygame.image.load('Gus/Gus_droit.png')
    gugus_gauche = pygame.image.load('Gus/Gus_gauche.png')

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        x_change = 2
        gugus=gugus_droite
    elif keys[pygame.K_LEFT]:
        x_change = -2 
        gugus=gugus_gauche
    elif keys[pygame.K_UP]:
        y_change = -2
        gugus=gugus_dos
    elif keys[pygame.K_DOWN]:
        y_change = 2
        gugus=gugus_face
    else:
        y_change = 0
        x_change = 0
    
    return(gugus,x_change,y_change)


class sac_a_dos():
    def __init__(self):
        super().__init__()
        self.torchon_salon = False

class action_key():
    def __init__(self):
        super().__init__()
        self.click = False
        self.conversation_papa = 0
        self.fouille = 0
        