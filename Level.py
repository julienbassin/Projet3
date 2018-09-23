import pygame
# -tc- not used from pygame.locals import *

import random
import constants as const
# -tc- not used from Perso import *


class Level:
    """
       this a class level which has a plenty method to generate, display and update the maze 
    """
    def __init__(self):
        self.structure = []
        self.objects = const.OBJECTS
        
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
        wall_object      = pygame.image.load(const.IMAGE_WALL).convert()
        mac_gyver_object = pygame.image.load(const.IMAGE_MACGYVER).convert()
        guardian_object  = pygame.image.load(const.IMAGE_GUARDIAN).convert()
        floor_object     = pygame.image.load(const.IMAGE_FLOOR).convert()

        tube_object      = pygame.image.load(const.IMAGE_TUBE).convert()
        ether_object     = pygame.image.load(const.IMAGE_ETHER).convert()
        needle_object    = pygame.image.load(const.IMAGE_NEEDLE).convert()

        num_line = 0
        for lines in self.structure:
            num_case = 0            
            for sprite in lines:
                x = num_case * const.PIXEL_LENGTH
                y = num_line * const.PIXEL_LENGTH
                if sprite == "W":
                    window.blit(wall_object, (x,y))
                elif sprite == "M":
                    window.blit(mac_gyver_object, (x,y))
                elif sprite == "G":
                    window.blit(guardian_object, (x,y))
                elif sprite == " ":
                    window.blit(floor_object, (x,y))
                elif sprite == "E":
                    window.blit(ether_object, (x, y))
                elif sprite == "T":
                    window.blit(tube_object, (x, y))
                elif sprite == "R":
                    window.blit(needle_object, (x, y))
                num_case +=1
            num_line +=1

    def randomize_item_maze(self, window):
        """
            Add 4 randomized items into the maze  
        """
        
        i=0
        while i < len(self.objects):
            random_x = random.randint(0, 14)
            random_y = random.randint(0, 14)
            x = random_x * const.PIXEL_LENGTH
            y = random_y * const.PIXEL_LENGTH
            if self.structure[random_x][random_y] not in ["W","M","G","E","T","R"]:
                self.structure[random_x][random_y] = self.objects[i]                
                i += 1

    def check_position(self,position_MG, position_G, pocket_full):        
        if position_MG.x == position_G.x -1 and position_MG.y == position_G.y and len(pocket_full) == 3:
            print("You're win!")
            return True
        else:
            print("You're not finished!")
            return False
