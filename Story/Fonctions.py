# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 15:43:41 2021

@author: basti
"""
import pygame
from settings import *
import pickle

pygame.init()

def collisions (liste_objet,rect_gugus,x_change,y_change,speed,rel_x,rel_y):

    for objet in liste_objet :
            
        if rect_gugus.colliderect(objet):

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

def collisions_pnj (liste_objet,rect_gugus,x_change,y_change,side):

    for objet in liste_objet :
            
        if rect_gugus.colliderect(objet):

            if abs (objet.top - rect_gugus.bottom) <= 10:
                y_change = 0

            if abs (objet.bottom - rect_gugus.top) <= 10:
                y_change = 0

            if abs (objet.left - rect_gugus.right) <= 10:
                x_change = 0

            if abs (objet.right - rect_gugus.left) <= 10:
                x_change = 0

        else:
            x_change = x_change
            y_change = y_change
            
    if side == "left" and x_change == 0:
        side = "right"

    elif side == "right" and x_change == 0:
        side = "left"
        
    return(x_change,y_change,side)

def coll_gus_pnj(liste_objet,rect_gugus,x_change,y_change,speed,rel_x,rel_y):

    for objet in liste_objet :
            
        if objet.rect.colliderect(rect_gugus):

            if abs (objet.rect.top - rect_gugus.bottom) <= 10 and y_change >= speed:
                y_change = 0
                rel_y = 0

            if abs (objet.rect.bottom - rect_gugus.top) <= 10 and y_change <= -speed:
                y_change = 0
                rel_y = 0
                print(1)
            if abs (objet.rect.left - rect_gugus.right) <= 10 and x_change >= speed:
                x_change = 0
                rel_x = 0 
                print(1)
            if abs (objet.rect.right - rect_gugus.left) <= 10 and x_change <= -speed:
                x_change = 0
                rel_x = 0 
                print(1)
        else:
            x_change = x_change
            y_change = y_change
            
            rel_x = rel_x
            rel_y = rel_y
    
    return(x_change,y_change,rel_x,rel_y)

class bonhomme(pygame.Rect):
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.width,self.height = image.get_rect().size
        pygame.Rect.__init__(self,x,y,self.width,self.height)
        self.in_touch = False
    def move_truc(self,move_x,move_y):
        self.x += move_x
        self.y += move_y
        pygame.Rect.__init__(self,self.x,self.y,self.width,self.height)

class sac_a_dos():
    def __init__(self):
        super().__init__()
        #Nivo1
        self.Torchon = 0
        self.soupe_froide = 0
        self.soupe_chaude = 0
        self.Cle_maison = 0
        self.Alcool = 0
        self.Briquet = 0
        self.Capote = 0 
        #Nivo2
        self.Bonbons_bizarres = 0 
        self.Clopes = 0
        self.Ballon = 0
        
        self.Telephone = 0
        self.Clef = 0
        self.Horaires_bus = 0
        self.Portefeuille = 0
        self.Photos = 0
        self.Seringue = 0
        self.Filtre_postillon = 0
        self.Teuteu = 0
        self.Huile_rateau = 0
        
        ##Nivo3
        self.Rythme = 0
        self.Argent_mac = 0
        self.Planing = 0
        self.Papier = 0
        self.Charisme = 0
        
    def update_items(self,tr):
        self.Clopes = tr.clopesEst + tr.clopes_nn + tr.clope_metro
        self.Capote = tr.capote_nn + tr.capote_buro + tr.capote_entree + tr.capoteNord + tr.capote_3
        self.Seringue = tr.seringue_NE + tr.seringue_NO + tr.seringueN + tr.seringueO
        self.Alcool = tr.bouteille_NO + tr.bouteille_alc + tr.biere
        self.Torchon = (tr.torchon_salon + tr.torchonsdb1 + tr.torchoncoul + tr.torchonch +
        tr.torchon_entre + tr.torchon_mom)
        
    def iter_objects(self):
        return (self.__dict__)                    

class action_key():
    def __init__(self):
        super().__init__()
        self.click = False
        self.conversation_papa = 0
        self.fouille = 0
        self.change_level = False

        
class Gus():
    def __init__(self):
        super().__init__()
        self.pv = 100 
        self.porte_entre = False
        self.level = 1
        self.money = 0
        self.speed = 2
        self.pause = 0
        self.frame = 0
        self.spawn = 1
        self.perso = "gus"
        
    def update_items(self,tr):
        self.money = (0.1 + tr.argent_poub + tr.tune_buro + tr.tune_entre + tr.tune_ch +
                      tr.give_money + tr.drug_money + tr.argent_teu + tr.argent_con + tr.ticket_bus +
                      tr.argent_bonus + tr.argent_ticket_metro)
        
    def iter_objects(self):
        return (self.__dict__)  
    
def spawn_level(x,y,start_x,start_y):
    
    screen_x = -start_x + x
    screen_y = -start_y + y    

    
    if screen_x >= 0 :
        screen_x = 0
        x = start_x
    elif screen_x <= display_width - 1000 :
        screen_x = display_width - 1000
        x = start_x + display_width - 1000
    if screen_y >= 0 :
        screen_y = 0
        y = start_y
    elif screen_y <= display_height - 707 :
        screen_y = display_height - 707 
        y = start_y + display_height - 707
        
    return(screen_x,screen_y,x,y)
        
def find_something(find,action,screen,objet_find):
    
    pygame.font.init()
 
    myfont = pygame.font.SysFont('corbel', 19, bold=True)

    find = find
    textsurface2 = myfont.render("",False, (110, 110, 110))
    
    if action.click == True and find == 0:
        find_s.play()
                       
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
 
    myfont = pygame.font.SysFont('corbel', 19, bold=True)
    
    textsurface = myfont.render(texte_zone, False, (110, 110, 110))
    screen.blit(fond_text,(260,380))
    screen.blit(textsurface,(280,385))
    i=var_iter
    j = 405
    for phrases in liste_phrases :
        
        if i < max_iter and action.click == True:
            textsurface2 = myfont.render(phrases, False, (110, 110, 110))
            screen.blit(textsurface2,(290,j))

            j += 15
    
        if var_iter >= max_iter and action.click == True:
            i -= max_iter

def zone_dialogue_noiter(screen,texte_zone,action,liste_phrases):
    
    pygame.font.init()
 
    myfont = pygame.font.SysFont('corbel', 19, bold=True)
    
    textsurface = myfont.render(texte_zone, False, (110, 110, 110))
    screen.blit(fond_text,(260,380))
    screen.blit(textsurface,(280,385))
    j = 405
    for phrases in liste_phrases :
        
        if action.click == True:
            textsurface2 = myfont.render(phrases, False, (110, 110, 110))
            screen.blit(textsurface2,(290,j))

            j += 15
            
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
    j = 75
    for text in texts :
        textsurface = myfont.render(text, False, (220, 220, 220))
        screen.blit(textsurface,(j,i))
        i += 20
        if i > 335:
            j += 150
            i = 220

def pause(screen,gameExit,Gus,sac,tr):
    keys=pygame.key.get_pressed()
    
    screen.blit(poze, (50 , 150))
    
    if keys[pygame.K_s]:
        other_s.play()
        gus_save = Gus.iter_objects()
        sac_save = sac.iter_objects()
        trigger_save = tr.iter_objects()
        with open('Story/saves/Gus.pkl', 'wb') as f:
            pickle.dump(gus_save, f, pickle.HIGHEST_PROTOCOL)
        with open('Story/saves/Sac.pkl', 'wb') as fi:
            pickle.dump(sac_save, fi, pickle.HIGHEST_PROTOCOL)       
        with open('Story/saves/Trigger.pkl', 'wb') as tr:
            pickle.dump(trigger_save, tr, pickle.HIGHEST_PROTOCOL)
            
        pygame.font.init()
 
        myfont = pygame.font.SysFont('corbel', 25, bold=True)
        
        textsurface = myfont.render("Partie sauvegardée", False, (0, 0, 0))
        screen.blit(textsurface,(135,350))

    if keys[pygame.K_q]: 
        other_s.play()
        pygame.quit()

def load(Gus,sac,tr):
    with open('Story/saves/Gus.pkl', 'rb') as f:
        gus_load = pickle.load(f)
    for key,value in gus_load.items():
        setattr(Gus,key,value)
    
    with open('Story/saves/Sac.pkl', 'rb') as fi:
        sac_load = pickle.load(fi)    
    for key,value in sac_load.items():
        setattr(sac,key,value)
        
    with open('Story/saves/Trigger.pkl', 'rb') as trig:
        trigger_load = pickle.load(trig)    
    for key,value in trigger_load.items():
        setattr(tr,key,value)
        
    return(Gus,sac,tr)

def game_over(screen):
    screen.fill(black)

    pygame.font.init()
 
    myfont = pygame.font.SysFont('corbel', 40, bold=True)
    
    textsurface = myfont.render("GAME OVER", False, (255, 0, 0))
    screen.blit(textsurface,(135,200))

def border_start(screen_x,screen_y,x,y,start_x,start_y,display_width,display_height):
    if screen_x >= 0:
        screen_x = 0
        x += start_x
    elif screen_x <= display_width - 1000 :
        screen_x = display_width - 1000
        x += start_x
    if screen_y >= 0  :
        screen_y = 0
        y  += start_y
    elif screen_y <= display_height - 707:
        screen_y = display_height - 707 
        y += start_y
    else:
        x=x
        y=y
        
    return(x,y,screen_x,screen_y)
