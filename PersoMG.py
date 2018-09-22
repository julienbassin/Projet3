from Perso import Perso
from constants import *

""" 
    Faire un enum  + tableau de translation

    EnumDirection = {

        high : (0,-1)
        Low : (0,1)
        Left : (-1,0)
        Right : (1,0)
        
    }

    EnumCase = {
        
        Guardian :  G
        Mac_Gyver : M
    }

    Vérifier que c'est un enum 
"""

class PersoMG(Perso):
    """
        this is a subclass herited by the root-class for Mac_Gyver
    """
    def __init__(self, structure, name):
        Perso.__init__(self, structure, name)
        self.pocket = []


    def move_position(self, direction):
        """
            this method allows Mac_Gyver to move on the left
        """
        if direction == "le" and self.x > 0:
            self.new_position_MG(-1,0)
        elif direction == "r" and self.x < NUMBER_SPRITE:
            self.new_position_MG(1,0)
        elif direction == "h" and self.y > 0:
            self.new_position_MG(0,-1)
        elif direction == "lo" and self.y < NUMBER_SPRITE:
             self.new_position_MG(0,1)
        else:
             print("You can't do that move")
        print(self.pocket)
        return self.x, self.y

    def new_position_MG(self, mouvement_x, mouvement_y):
        case_destination = self.structure[self.y+mouvement_y][self.x+mouvement_x]
        if case_destination not in  ["W", "G"]:
            if case_destination in OBJECTS and len(self.pocket) < POCKET_SIZE:
                self.pocket.append(case_destination)
                self.structure[self.y][self.x] = " "    
            self.x += mouvement_x
            self.y += mouvement_y
            self.structure[self.y][self.x] = "M"
