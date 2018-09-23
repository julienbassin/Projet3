import pygame
from pygame.locals import *

import random
from constants import *
from Level import *

class Perso():
    """description of class"""
    def __init__(self, letter):
        self.x = 0
        self.y = 0 
        self.letter = letter
                
    def get_position(self, structure):
        for i, lines in enumerate(structure):
            for j, sprite in enumerate(lines):
                if sprite == self.letter:
                    self.x = j
                    self.y = i 
                    return (self.x, self.y)
        

class PersoMG(Perso):
    """
        the class Perso is mother-class which initialize the coordonates of persons
        it gets the position of any personnages
    """
    def __init__(self, letter):
        """
            Initialization of structure, Perso's name and coordinates
        """ 
        Perso.__init__(self, letter)
        self.pocket = []
            
    def move_position(self, structure, direction):
        """
            this method allows Mac_Gyver to move on the left
        """
        if direction == "left":
            self.new_position_MG(structure,-1,0)
        elif direction == "right":
            self.new_position_MG(structure,1,0)
        elif direction == "high":
            self.new_position_MG(structure,0,-1)
        elif direction == "low":
             self.new_position_MG(structure,0,1)        
        print(self.pocket)

    def new_position_MG(self, structure, movement_x, movement_y):
        case_destination = structure[self.y+movement_y][self.x+movement_x]
        if case_destination not in  ["W", "G"]:
            if case_destination in OBJECTS and len(self.pocket) < POCKET_SIZE:
                self.pocket.append(case_destination)
                structure[self.y][self.x] = " "
            structure[self.y][self.x] = " "
            self.x += movement_x
            self.y += movement_y
            structure[self.y][self.x] = "M"
 
            
