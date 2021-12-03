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
        self.torchon = 0
        self.soupe_froide = 0
        self.soupe_chaude = 0
        self.cle_maison = False

class action_key():
    def __init__(self):
        super().__init__()
        self.click = False
        self.conversation_papa = 0
        self.fouille = 0

def find_something(find,action,screen,objet_find):
    
    pygame.font.init()
 
    myfont = pygame.font.SysFont('arial', 20)

    find = find
    textsurface2 = myfont.render("",False,(255, 255, 255))
    
    if action.click == True and find == 0:
                       
        textsurface2 = myfont.render("Tu as trouvé " + str(objet_find), False, (255, 255, 255))
        screen.blit(textsurface2,(290,460))
        
    if action.click == True and find == 1:
                                
        textsurface2 = myfont.render("Il n'y a plus rien ici !", False, (255, 255, 255))
        screen.blit(textsurface2,(290,460))
        
    return(textsurface2)

def zone_interaction(screen,texte_zone,action,var_iter,objet_find):
    
    pygame.font.init()
 
    myfont = pygame.font.SysFont('arial', 20)
    
    textsurface = myfont.render(texte_zone, False, (255, 255, 255))
    screen.blit(textsurface,(290,440))
    
    if var_iter == 0:
        textsurface2 = find_something(0,action,screen,objet_find)
        
    if var_iter > 0:
        textsurface2 = find_something(1,action,screen,objet_find)
        
    return(var_iter)

def zone_dialogue(screen,texte_zone,action,liste_phrases,var_iter,max_iter):
    
    pygame.font.init()
 
    myfont = pygame.font.SysFont('arial', 20)
    
    textsurface = myfont.render(texte_zone, False, (255, 255, 255))
    screen.blit(textsurface,(290,440))
    
    i = var_iter
    
    if i < max_iter:
        textsurface2 = myfont.render(liste_phrases[i], False, (255, 255, 255))
        screen.blit(textsurface2,(290,460))
        i += 1

    if var_iter >= max_iter:
        i -= max_iter
    return(i)
