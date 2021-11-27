# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 15:45:18 2021

@author: basti
"""
import pygame

class gus():
    def __init__ (self):
        self.face = pygame.image.load('Gus/Gus.png')
        self.dos = pygame.image.load('Gus/Gus_dos.png')
        self.droite = pygame.image.load('Gus/Gus_droit.png')
        self.gauche = pygame.image.load('Gus/Gus_gauche.png')
        self.width = 48
        self.height = 52
        self.running=1.02
        self.state = "face"
        self.image = self.face
        self.pos ="face"
        
    def update_state(self,pos):
        if pos == "left":
            self.image = self.gauche
            self.state="gauche"
        if pos == "right":
            self.image = self.droite
            self.state="droite"
        if pos == "up":
            self.image = self.dos
            self.state="haut"
        if pos == "down":
            self.image = self.face
            self.state="face"
        