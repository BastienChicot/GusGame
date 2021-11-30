# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 13:28:37 2021

@author: basti
"""
import pygame

phrases_papa = ["Laisse moi tranquille", "Va voir ta mère, elle est dans la chambre",
                "Tu as apporté à manger à ta mère ?","Bon laisse moi tranquille maintenant",
                "Tu me fatigues! Va-t-en!","ZZZzzzZZZzzz"]

def histoire(screen,x,y,level,action,sac,pressed,liste_zone):
    pygame.font.init()
    
    myfont = pygame.font.SysFont('arial', 20)
    
    if level == "level_1":
    
        if 170 < x < 210 and 378 < y < 440 :
            
            textsurface = myfont.render('Parler à papa (A)', False, (255, 255, 255))
            screen.blit(textsurface,(290,440))
                
            i = pressed
            
            if i >= 0 and i < 6 :
                textsurface2 = myfont.render(phrases_papa[i], False, (255, 255, 255))
                screen.blit(textsurface2,(290,460))                     
            else:
                i = 0         
               
        elif 235 < x < 295 and 480 < y < 530 :
            
            textsurface = myfont.render("Fouiller l'armoire (A)", False, (255, 255, 255))
            screen.blit(textsurface,(290,440))

            if action.click == True: 
            
                if liste_zone[0].interaction == 0:
                                       
                    textsurface2 = myfont.render("Tu as trouvé un torchon et une cuillière", False, (255, 255, 255))
                    screen.blit(textsurface2,(290,460))
                           
                    sac.torchon_salon = True
                    action.fouille = 1
            
                if sac.torchon_salon == True and liste_zone[0].interaction > 0:
                                            
                    textsurface2 = myfont.render("Il n'y a plus rien ici !", False, (255, 255, 255))
                    screen.blit(textsurface2,(290,460))
                                        

        else:
            action.click = False
    
    return(action,sac)