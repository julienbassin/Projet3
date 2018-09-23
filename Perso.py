import pygame
from pygame.locals import *

import random
from constants import *
from Level import *

class Perso():
    """
        the class Perso is mother-class which initialize the coordonates of persons
        it gets the position of any personnages
    """
    def __init__(self, structure):
        """
            Initialization of structure, Perso's name and coordinates
        """
        self.x = 0
        self.y = 0
        self.structure = structure
        self.pocket = []
        self.direction = 0 
            
    def move_position(self, direction):
        """
            this method allows Mac_Gyver to move on the left
        """
        if direction == "left" and self.x > 0:
            self.new_position_MG(-1,0)
        elif direction == "right" and self.x < NUMBER_SPRITE:
            self.new_position_MG(1,0)
        elif direction == "high" and self.y > 0:
            self.new_position_MG(0,-1)
        elif direction == "low" and self.y < NUMBER_SPRITE:
             self.new_position_MG(0,1)
        else:
             print("You can't do that move")
        print(self.pocket)

    def new_position_MG(self, mouvement_x, mouvement_y):
        case_destination = self.structure[self.y+mouvement_y][self.x+mouvement_x]
        if case_destination not in  ["W", "G"]:
            if case_destination in OBJECTS and len(self.pocket) < POCKET_SIZE:
                self.pocket.append(case_destination)
                self.structure[self.y][self.x] = " "    
            self.x += mouvement_x
            self.y += mouvement_y
            self.structure[self.y][self.x] = "M"
            