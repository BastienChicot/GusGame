# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 11:32:39 2022

@author: basti
"""

class trigger():
    def __init__(self):
        super().__init__()
        ###NIVO 1
        self.pressed_salon = -1
        self.pressed_mom = -1
        self.pressed_dad = -1
        self.pressed_cuisine1 = -1
        self.pressed_cuisine2 = -1
        self.pressed_cuisine3 = -1
        self.pressed_four = -1
        self.pressed_sdb1 = -1
        self.pressed_frigo = -1 
        self.fouille = -1
        self.pressed_ch = -1
        self.pressed_couloir = -1
        self.pressed_arm_mom = -1
        self.pressed_entre = -1
        self.pressed_sdb2 = -1
        self.pressed_cleb = -1
        self.pressed_papier = -1 
        self.pressed_tune_buro = -1
        self.pressed_tune_entre = -1 
        self.pressed_couloir2 = -1
        self.pressed_buro = -1
        self.pressed_tune_ch = -1
        self.pressed_sortie = -1
        
        self.open_buro = False
        self.service=False
        self.mom_sleep = False
        self.dad_sleep = False
        self.papa_fouillab = False
        self.porte_entre = False
        
        ##NIVO 2
        self.pressed_vieille = -1
        self.pressed_interphone = -1
        self.pressed_arbre = -1
        self.pressed_papier = -1
        self.pressed_stuff = -1
        
        self.pressed_tox = -1
        self.pressed_seringue = -1
        self.pressed_ball = -1
        
        self.pressed_con = -1
        self.press_poub = -1
        self.press_coin = -1
        
        self.press_vois = -1
        self.press_poub2 = -1
        self.press_car = -1 
        
        self.nord1 = -1
        self.nord2 = -1
        self.nord3 = -1
        
    def iter_objects(self):
        return (self.__dict__) 