# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 15:43:41 2021

@author: basti
"""
import pygame
from settings import *

def collisions (liste_objet,rect_gugus,x_change,y_change,speed,rel_x,rel_y):

    for objet in liste_objet :
            
        if rect_gugus.colliderect(objet):
    
    # index = rect_gugus.collidelist(liste_objet)
    
    # if index >= 0 : 
        
    #     objet = liste_objet[index]

            if abs (objet.top - rect_gugus.bottom) <= 10 and y_change >= speed:
                y_change = 0
                rel_y = 0
            if abs (objet.bottom - rect_gugus.top) <= 10 and y_change <= -speed:
                y_change = 0
                rel_y = 0
            if abs (objet.left - rect_gugus.right) <= 10 and x_change >= speed:
                x_change = 0
                rel_x = 0 
            if abs (objet.right - rect_gugus.left) <= 10 and x_change <= -speed:
                x_change = 0
                rel_x = 0 
        else:
            x_change = x_change
            y_change = y_change
            
            rel_x = rel_x
            rel_y = rel_y
    
    return(x_change,y_change,rel_x,rel_y)


class sac_a_dos():
    def __init__(self):
        super().__init__()
        self.Torchon = 0
        self.soupe_froide = 0
        self.soupe_chaude = 0
        self.Cle_maison = 0
        self.Alcool = 0

    def iter_objects(self):
        return (self.__dict__)                    

class action_key():
    def __init__(self):
        super().__init__()
        self.click = False
        self.conversation_papa = 0
        self.fouille = 0
        
class Gus():
    def __init__(self):
        super().__init__()
        self.pv = 100 
        self.porte_entre = False
        self.level = 1
        self.money = 0
        self.speed = 2

def find_something(find,action,screen,objet_find):
    
    pygame.font.init()
 
    myfont = pygame.font.SysFont('corbel', 20, bold=True)

    find = find
    textsurface2 = myfont.render("",False, (110, 110, 110))
    
    if action.click == True and find == 0:
                       
        textsurface2 = myfont.render("Tu as trouvé :" , False, (110, 110, 110))
        textsurface3 = myfont.render(str(objet_find), False, (110, 110, 110))
        
        screen.blit(textsurface2,(290,425))
        screen.blit(textsurface3,(290,445))
        
    if action.click == True and find == 1:
                                
        textsurface2 = myfont.render("Il n'y a plus rien ici !", False, (110, 110, 110))
        screen.blit(textsurface2,(290,425))
        
    return(textsurface2)

def zone_interaction(screen,texte_zone,action,var_iter,objet_find):
    
    pygame.font.init()
 
    myfont = pygame.font.SysFont('corbel', 20, bold=True)
    
    textsurface = myfont.render(texte_zone, False, (110, 110, 110))
    screen.blit(fond_text,(260,380))
    screen.blit(textsurface,(280,400))
    
    if var_iter == 0:
        textsurface2 = find_something(0,action,screen,objet_find)
        
    if var_iter > 0:
        textsurface2 = find_something(1,action,screen,objet_find)
        
    return(var_iter)

def zone_dialogue(screen,texte_zone,action,liste_phrases,var_iter,max_iter):
    
    pygame.font.init()
 
    myfont = pygame.font.SysFont('corbel', 20, bold=True)
    
    textsurface = myfont.render(texte_zone, False, (110, 110, 110))
    screen.blit(fond_text,(260,380))
    screen.blit(textsurface,(280,400))
    
    i = var_iter
    
    if i < max_iter and action.click == True:
        textsurface2 = myfont.render(liste_phrases[i], False, (110, 110, 110))
        screen.blit(textsurface2,(290,425))
        i += 1

    if var_iter >= max_iter and action.click == True:
        i -= max_iter
    return(i)

def affich_sac(screen,sac):
    
    pygame.font.init()
    
    myfont = pygame.font.SysFont('corbel', 18, bold=True)
    texts = []
    sac_dict = sac.iter_objects()

    for i in sac_dict:
        if sac_dict[i] == True or sac_dict[i] != 0:

            text = str(i) + " -> " + str(sac_dict[i])
            texts.append(text)
   
    screen.blit(sac_image,(25,130))
    i = 220
    for text in texts :

        textsurface = myfont.render(text, False, (220, 220, 220))
        screen.blit(textsurface,(75,i))
        i += 20
    