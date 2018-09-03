import random
from game_constants import objects
from Perso import Perso
from PersoMG import PersoMG

class Level:
    """
       this a class level which has a plenty method to generate, display and update the maze 
    """
    def __init__(self, file):
        self.file = file
        self.structure = []
        self.random_choice = objects
        
        
    def generate_maze(self):
        """
            Generate a maze in memory from the file
        """
        with open(self.file) as file:
            lines = file.read().split("\n")
            structure_level = []        
            for line in lines:
                line_level = []
                for sprite in line:
                    if sprite != "\n":
                        line_level.append(sprite)
                structure_level.append(line_level)
                self.structure = structure_level
    
    def display_maze(self):
        """
            Iterate the maze's structure and display the result
        """
        for liste in self.structure:
            for item in liste:
                print(item, end='')
            print()

    def randomize_item_maze(self):
        """
            Add 4 randomized items into the maze  
        """
        i=0
        while i < len(self.random_choice):
            random_x = random.randint(0, 14)
            random_y = random.randint(0, 14)
            if self.structure[random_x][random_y] == " ":
                self.structure[random_x][random_y] = self.random_choice[i]
                i += 1

    def check_position(self,position_MG, position_G):
        MG_x, MG_y = position_MG
        G_x, G_y = position_G
        if MG_y == G_y and MG_x == G_x -1 and len(pocket) == 4:
            print("You're win!")
        else:
            print("You're not finished!")

       
    @staticmethod
    def print_menu():
        """
            Display the principal menu
        """
        print(30 * "-" , "MENU" , 30 * "-")
        print("1. Console Game")
        print("2. GUI Game")
        print(67 * "-")

