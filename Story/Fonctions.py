# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 15:43:41 2021

@author: basti
"""

def collisions (liste_objet,x,y,rect_gugus,x_change,y_change):

    for objet in liste_objet:
        
        index = rect_gugus.collidelist(liste_objet)
        
        if index >= 0 : 
            
            objet = liste_objet[index]
    
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
