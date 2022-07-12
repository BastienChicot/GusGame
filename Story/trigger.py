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
        self.change_level = False
        
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
        
        ## LVL BONUS
        self.argent_bonus = 0
        self.fin_nivo_bonus = False
        self.pos_bonus = -1
        
        
        ## LVL 3
        self.press_hook = -1
        self.press_mac = -1
        
        self.press_lassl = -1
        self.press_contr1 = -1
        self.press_contr2 = -1
        self.press_random_ticket = -1 
        
        self.press_batteur = -1
        self.press_bassist = -1
        self.press_guitar = -1
        self.press_fraudeur = -1
        
        self.press_clodo = -1
        self.press_machine1 = -1
        self.press_machine2 = 0
        self.depressif = -1
        
        ## OBJETS
        self.press_trash = -1
        self.press_trash2 = -1
        
        self.press_trash_metro1 = -1
        self.press_trash_metro2 = -1
        self.press_billeterie = -1
        
        self.capote_3 = 0
        
        self.argent_ticket_metro = 0
        self.clope_metro = 0

        self.press_trash3 = -1   
        
        self.achat_gateau = 0
        self.gateau_offert = 0
        #INTERACT LVL 3
        self.give_condom = False
        self.give_mac = False
        self.take_plan = False
        
        self.repair_distri = False
        self.give_charism = False
        self.give_ticket = False
        self.find_fraudeur = False
        self.denonce_fraude = False
        self.achat_ticket = False
        self.talk_contr2 = False
        
        self.give_dwich = False
        self.give_pince = False
        self.give_lassl_gateau = False
        self.give_carton = False
        self.gateau_clodo = False
        self.propose_seringue = False
        self.give_seringue = False
        self.give_alcool = False
        ##########################
        
        self.score_music = 0
        
        self.rythm = 0
        self.unlock_minigame1 = False
        self.valid_music = False
        self.money_win_music = 0
        self.ask_love = False
        self.accord_mac = False
        
        self.argent_rdv_pute = 0
        
        ##Lvl 4
        self.barre_cereal = -1
        
        self.eat_barre = False
        
        self.press_clope_trom = -1
        self.clope_trome = 0
        
        self.fight = False
        
        
        ##NIVO 5
        #5 metro
        
        self.press_mach1 = -1
        self.press_mach2 = -1
        self.argent_mach_5m = 0
        self.cig_5m = -1
        self.clope_5m = 0
        self.poubelle_5m = -1
        self.money_5m = 0
        
        self.dame_5m = -1
        self.pnj_assis_5m = -1
        self.pnj_machine_5m = -1
        self.pnj_banc_5m = -1
        self.chauve = -1
        
        self.donne_habits = False
        self.give_plan = False
        self.give_horaire = False
        
        self.cachets_pnj_metro = 0
        self.vente_assis = False
        self.donne_USB = False
        
        # 5 esc 1
        
        self.poub_esc1 = -1
        
        # 5 esc 2
        
        self.clodo_5m = -1
        
        # 5 Nord
        self.press_capote_5n = -1
        self.capote_5n = 0
        self.poub_5n = -1
        self.sac_5n = -1
        self.carton_5n = -1
        self.teille_5n = -1
        self.bouteille_5n = 0
        self.cachet_5n = -1
        
        self.controleur_5n = -1
        self.lassl_5n = -1
        self.pnj_5n = -1
        
        self.give_capote_lassl = False
        
        # 5 Nord Ouest
        
        self.mach_tick1 = -1
        self.mach_tick2 = -1
        self.argent_ticket2 = 0
        self.controleur_5no = -1
        self.pnj_5no = -1
        
        self.batt_tel_5no = False
        self.give_cachets_5no = False
        self.cachets_5no = 0
        
        # 5 Ouest
        self.affich_plan = 0
        
        # 5 Ouest
        self.poub_5o = -1
        
        # 5 Sud Ouest
        self.press_seringue_5so = -1
        self.seringue_5so = 0
        self.distrib_5so = -1
        self.argent_mask = 0
        self.poub_5so = -1
        self.sac_5so = -1
        self.meuble_5so = -1
        
        self.tab_5so = -1
        self.pnj_stand_5so = -1
        
        self.cachets_militaire = 0
        
        # 5 Centre
        self.etag_5c1 = -1
        self.etag_5c2 = -1
        self.etag_5c3 = -1
        self.etag_5c4 = -1
        
        self.caisse_5c = -1
        self.pnj_mag_5c = -1
        self.pnj_allee_5c = -1
        
        self.ordi_vendeuse = False
        self.coupe_cable = False
        self.caisse_occupee_5c = False
        self.disparu = 0
        
        self.recherche = False
        self.repare_ordi = False
        
        self.cachets_allee = 0
        
        # 5 Sud
        
        self.caisse_5s = -1
        self.pnj_jeu_5s = -1
        self.vigil_5s = -1
        self.etag_5s = -1
        self.bac_5s = -1
        
        self.caisse_5s_occupe = False
        
    def update_items(self):
         self.give_money = self.pnj_bus
         self.drug_money = (0 + self.argent_vieille + self.argent_tox + 
                            self.argent_vois + self.argent_cond )
        
    def iter_objects(self):
        return (self.__dict__) 