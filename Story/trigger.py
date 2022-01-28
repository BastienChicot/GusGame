# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 11:32:39 2022

@author: basti
"""

class trigger():
    def __init__(self):
        super().__init__()
        self.game_over = False
        self.drug_money = 0
        
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
        
        self.cles_buro=0
        
        ##NIVO 2
        self.pressed_vieille = -1
        self.apporte_clope = False
        self.pressed_interphone = -1
        self.pressed_arbre = -1
        self.pressed_papier = -1
        self.pressed_stuff = -1
        self.press_cave = -1
        
        self.pressed_tox = -1
        self.pressed_seringue = -1
        self.pressed_ball = -1
        
        self.pressed_con = -1
        self.missions_con = False
        self.ask_con = False
        self.press_poub = -1
        self.press_coin = -1
        self.tree_22 = -1
        
        self.press_vois = -1
        self.press_poub2 = -1
        self.press_car = -1 
        
        self.press_dealer = -1
        self.ask_deal = False
        self.press_pnj_bus = -1
        self.horaire_bus = -1
        self.press_conduct = -1
        self.ticket_bus = 0
        self.back_bus = -1
        
        self.pnj_bus = 0
    
        
        self.nord1 = -1
        self.nord2 = -1
        self.nord3 = -1
        
        
        self.give_money = 0
        self.vire_dealer = False
        
        self.argent_vieille = 0
        self.argent_tox = 0
        self.argent_vois = 0
        self.argent_con = 0
        self.argent_cond = 0
        self.argent_teu = 0
        self.ask_phone = False
        
        self.tout_vendu = False
        self.accept_deal =False
        self.vente_teu = False
        self.miss_money = 0
        self.fouille_sac = False
        self.show_photo = False
        self.repair_inter = False
        ###Items collectables
        self.torchon_salon = 0
        self.torchonsdb1 = 0
        self.torchoncoul = 0
        self.torchonch = 0
        self.torchon_entre = 0
        self.torchon_mom = 0
        
        self.biere=0
        self.bouteille_alc = 0
        self.tune_buro = 0
        self.tune_entre = 0
        self.tune_ch = 0
        
        self.capote_buro = 0
        self.capote_entree = 0

        self.clopesEst = 0
        self.capoteNord = 0
        self.argent_poub = 0
        self.seringue_NE = 0
        self.seringue_NO = 0
        self.seringueN = 0
        self.seringueO = 0
        
        self.bouteille_NO = 0
        self.capote_nn = 0
        self.clopes_nn = 0
        
        self.collect_bonbon = False
        
    def update_items(self):
         self.give_money = self.pnj_bus
         self.drug_money = (0 + self.argent_vieille + self.argent_tox + 
                            self.argent_vois + self.argent_cond )
        
    def iter_objects(self):
        return (self.__dict__) 