import pygame
from pygame.locals import *

import random
from constants import *
from Perso import *


class Level:
    """
       this a class level which has a plenty method to generate, display and update the maze 
    """
    def __init__(self):
        self.structure = []
        self.objects = OBJECTS        
        
    def load_maze_from_file(self, file):
        """
            Generate a maze in memory from the file
        """
        with open(file) as f:
            lines = f.read().split("\n")
            structure_level = []        
            for line in lines:
                line_level = []
                for sprite in line:
                    if sprite != "\n":
                        line_level.append(sprite)
                structure_level.append(line_level)
                self.structure = structure_level
    
    def display_maze(self, window):
        """
            Display the maze's structure
        """
        wall_object      = pygame.image.load(IMAGE_WALL).convert()        
        mac_gyver_object = pygame.image.load(IMAGE_MACGYVER).convert() 
        guardian_object  = pygame.image.load(IMAGE_GUARDIAN).convert()
        floor_object     = pygame.image.load(IMAGE_FLOOR).convert()

        num_line = 0
        for lines in self.structure:
            num_case = 0            
            for sprite in lines:
                x = num_case * PIXEL_LENGTH
                y = num_line * PIXEL_LENGTH
                if sprite == "W":
                    window.blit(wall_object, (x,y))
                if sprite == "M":
                    window.blit(mac_gyver_object, (x,y))
                if sprite == "G":
                    window.blit(guardian_object, (x,y))
                if sprite == " ":
                    window.blit(floor_object, (x,y))
                num_case +=1
            num_line +=1

    def randomize_item_maze(self, window):
        """
            Add 4 randomized items into the maze  
        """
        tube_object = pygame.image.load(IMAGE_TUBE).convert()
        ether_object = pygame.image.load(IMAGE_ETHER).convert()
        needle_object = pygame.image.load(IMAGE_NEEDLE).convert()

        i=0
        while i < len(self.objects):
            random_x = random.randint(0, 14)
            random_y = random.randint(0, 14)
            x = random_x * PIXEL_LENGTH
            y = random_y * PIXEL_LENGTH
            if self.structure[random_x][random_y] != "W":
                self.structure[random_x][random_y] = self.objects[i]
                if self.structure[random_x][random_y] == "E":
                    window.blit(ether_object, (x, y))
                if self.structure[random_x][random_y] == "T":
                    window.blit(tube_object, (x, y))
                if self.structure[random_x][random_y] == "R":
                    window.blit(needle_object, (x, y))
                i += 1

    def check_position(self,position_MG, position_G, pocket_full):        
        if position_MG == position_G and len(pocket_full) == 3:
            print("You're win!")
        else:
            print("You're not finished!")
