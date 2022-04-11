
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 09:56:55 2022

@author: bchicot
"""

import pygame
import random
import numpy as np
from settings import * 

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
myfont = pygame.font.SysFont('Corbel Bold', 24)

def boucle():
    gameExit=False
      
    a = 0
    gugus = gus_fight_right[0]
    rect_gugus = gugus.get_rect()
    frame_count = 0
    side = True

    left2 = gus_fight_l1
    
    left_tr2 = left2.get_rect()
    
    triangle2 = left_tr2
    image2 = left2
    
    x = 150
    y = 230
    
    x2 = 300
    y2 = 230
    
    move_y = 0
    move_x = 0
    air_time = 1
    
    jump = False
    fall = False
    
    attack = False
    super_attack = False
    hit = False
    collision = False
    
    opp_clean = 0
    clean_hit = 0
    
    triangle_life = 100
    triangle2_life = 100
    
    clock = pygame.time.Clock()
    while not gameExit:
        
        if frame_count <= 60:
            frame_count += 1
        else:
            frame_count = 0
        
        if frame_count <= 15:
            a=0
        elif 15 < frame_count <= 30:
            a=1
        elif 30 < frame_count <= 45:
            a=1
        elif 45 < frame_count <= 60:
            a=1
           
        rect_gugus = gugus.get_rect() 
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
               
              # Condition becomes true when keyboard is pressed   
            if event.type == pygame.KEYDOWN:
   
                if event.key == pygame.K_UP :
                    # triangle = up_tr
                    # image = up
                    jump = True
                    
                if event.key == pygame.K_DOWN :
                    # triangle = dw_tr
                    # image = down
                    fall = True
                    
                if event.key == pygame.K_LEFT :
                    # triangle = left_tr
                    # image = left 
                    move_x = -2
                    side = False
                    
                if event.key == pygame.K_RIGHT :
                    # triangle = right_tr
                    # image = right
                    move_x = 2
                    side = True
                    
                if event.key == pygame.K_a :
                    attack = True
                if event.key == pygame.K_z :
                    super_attack = True         
                    
            if event.type == pygame.KEYUP:
   
                if event.key == pygame.K_UP :
                    jump = False
                    
                if event.key == pygame.K_DOWN :
                    fall = False
                    
                if event.key == pygame.K_LEFT :
                    move_x = 0

                if event.key == pygame.K_RIGHT :
                    move_x = 0

                if event.key == pygame.K_a :
                    attack = False
                if event.key == pygame.K_z :
                    super_attack = False
        
        if side:
            gugus=gus_fight_right[a]
        else:
            gugus=gus_fight_left[a]
        
        rect_gugus = gugus.get_rect() 
        
        if (y < 230 and not rect_gugus.colliderect(triangle2)) or jump :
            air_time += 1
 
        if jump : 
            move_y = -(25/air_time)
            
        if y < 230 and air_time > 30:
            move_y = 3
        elif y < 230 and fall :
            move_y = 5
        elif y >= 230 and not jump:
            move_y = 0
            y = 230
            jump = False
            air_time = 1
            
        if rect_gugus.colliderect(triangle2):
            if abs(rect_gugus.bottom - triangle2.top) <= 10 and move_y > 0:
                move_y = 0
                air_time = 1
                jump = False
            if abs(rect_gugus.top - triangle2.bottom) <= 10 and move_y < 0:
                move_y = 0
            if abs(rect_gugus.left - triangle2.right) <= 10 and move_x < 0:
                move_x = 0             
            if abs(rect_gugus.right - triangle2.left) <= 10 and move_x > 0:
                move_x = 0

        if abs(rect_gugus.right - triangle2.left) <= 80 and move_x > 0 and y2-20 < y < y2+20:
            if 50 < x2 < 400:
                x2 += move_x/4
            elif x2 >= 400 :
                x2 -= move_x
        if abs(rect_gugus.left - triangle2.right) <= 80 and move_x < 0 and y2-20 < y < y2+20:
            if 50 < x2 < 400:
                x2 += move_x/4
            elif x2 <= 50 :
                x2 -= move_x
            
        ##COUP SIMPLE AVEC A
        if abs(rect_gugus.left - triangle2.right) <= 5 and attack and move_x != 0:
            triangle2_life -=5
            clean_hit += 1
            x2 -= 80
            opp_clean = 0
        if abs(rect_gugus.right - triangle2.left) <= 5 and attack and move_x != 0:
            triangle2_life -=5
            x2 += 80
            clean_hit += 1
            opp_clean = 0
        
        ##COUP COMBO A ET Z
        if 80 < abs(rect_gugus.left - triangle2.right) < 120 and attack and move_x < 0 and super_attack:
            triangle2_life -= 10
            clean_hit += 1
            x -= abs(rect_gugus.left - triangle2.right)
            opp_clean = 0
        if abs(rect_gugus.right - triangle2.left) <= 5 and attack and move_x > 0 and super_attack:
            triangle2_life -= 10
            x += abs(triangle.right - triangle2.left)
            clean_hit += 1
            opp_clean = 0

        ##SUPER COUP AVEC Z
        if abs(rect_gugus.left - triangle2.right) <= 5 and super_attack and move_x != 0 and clean_hit >= 5:
            triangle2_life -=15
            clean_hit = 0
            x2 -= 120
            opp_clean = 0
        if abs(rect_gugus.right - triangle2.left) <= 5 and super_attack and move_x != 0 and clean_hit >= 5:
            triangle2_life -=15
            x2 += 120
            clean_hit = 0
            opp_clean = 0
        
        ##COUP SAUTE
        if abs(rect_gugus.left - triangle2.right) <= 5 and attack and air_time > 45:
            triangle2_life -= 10
            clean_hit += 1
            opp_clean = 0
            x2 -= 50
        if abs(rect_gugus.right - triangle2.left) <= 5 and attack and air_time > 45:
            triangle2_life -=10
            x2 += 50
            clean_hit += 1
            opp_clean = 0
            
        ##COUP ADVERSAIRE
        if rect_gugus.colliderect(triangle2):
            collision = True
        elif not rect_gugus.colliderect(triangle2):
            collision = False
            
        if collision and move_x == 0 and not attack and not jump:
            hit = True
        else:
            hit = False

        ##CORP A CORP           
        if abs(rect_gugus.left - triangle2.right) <= 5 and hit:
            triangle_life -=5
            x += 80
            clean_hit = 0
            opp_clean += 1
            
        if abs(rect_gugus.right - triangle2.left) <= 5 and hit:
            triangle_life -=5
            x -= 80
            clean_hit = 0
            opp_clean += 1
            
        ##SUPER COUP ADVERSAIRE
        if abs(rect_gugus.left - triangle2.right) <= 5 and hit and opp_clean == 3:
            triangle_life -= 10
            x += 100
            clean_hit = 0
            opp_clean = 0
            
        if abs(rect_gugus.right - triangle2.left) <= 5 and hit and opp_clean == 3:
            triangle_life -=10
            x -= 100
            clean_hit = 0
            opp_clean = 0
            
        ##COMBO ADVERSAIRE
        ##PROJECTILE??           
                
        if move_x == 0 and not jump:
            if x2 > x and not collision and x2 > 50:
                x2 -= 0.5
            elif x2 < x and not collision and x2 < 400:
                x2 += 0.5
            else:
                x2 = x2
            
        x += move_x
        y += move_y  

        if x > 450 :
            x=450
        if x < 0:
            x = 0
        if x2 > 480:
            x2 = 480
        if x2 < 20:
            x2 = 20
        
        screen.fill((0,0,0))
        
        rect_gugus.topleft = (x,y)        
        triangle2.topleft = (x2,y2)        

        screen.blit(gugus,rect_gugus)
        screen.blit(image2,triangle2)
        
        life = myfont.render(str(triangle_life), False, (210, 210, 210))
        screen.blit(life,(20,35))
        super_power = myfont.render(str(clean_hit), False, (210, 210, 210))
        screen.blit(super_power,(20,65))

        textsurface = myfont.render(str(triangle2_life), False, (210, 210, 210))
        screen.blit(textsurface,(460,35))
        

        pygame.display.update()
        clock.tick(100)        
        
boucle()
pygame.quit()