import pygame
import random
from constants import *
from Perso import *


class Level:
    """
       this a class level which has a plenty method to generate, display and update the maze 
    """
    def __init__(self):
        self.structure = []
        self.random_choice = OBJECTS        
        
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
        wall = pygame.image.load(IMAGE_WALL).convert()
        start = pygame.image.load(IMAGE_START).convert()
        finish = pygame.image.load(IMAGE_FINISH).convert_alpha()

        num_line = 0
        for lines in self.structure:
            num_case = 0            
            for sprite in lines:
                x = num_case * PIXEL_LENGTH
                y = num_line * PIXEL_LENGTH
                if sprite == "W":
                    window.blit(wall, (x,y))
                elif sprite == "M":
                    window.blit(start, (x,y))
                elif sprite == "G":
                    window.blit(finish, (x,y))
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
        while i < len(self.random_choice):
            random_x = random.randint(0, 14)
            random_y = random.randint(0, 14)
            if self.structure[random_x][random_y] == " ":
                self.structure[random_x][random_y] = self.random_choice[i]
                if self.structure[random_x][random_y] == "E":
                    window.blit(ether_object, (random_x, random_y))
                elif self.structure[random_x][random_y] == "T":
                    window.blit(tube_object, (random_x, random_y))
                elif self.structure[random_x][random_y] == "R":
                    window.blit(needle_object, (random_x, random_y))
                i += 1

    def check_position(self,position_MG, position_G, pocket_full):        
        if position_MG == pposition_G and len(pocket_full) == 4:
            print("You're win!")
        else:
            print("You're not finished!")
