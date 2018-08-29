from Perso import Perso
from game_constants import height, width, objects

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
        if direction == "r" and self.x < width:
            self.new_position_MG(1,0)
        if direction == "h" and self.y > 0:
            self.new_position_MG(0,-1)
        if direction == "lo" and self.y < height:
             self.new_position_MG(0,1)
        else:
             print("this is a wall!\n")
        print(self.pocket)
    
    def new_position_MG(self, mouvement_x, mouvement_y):
        if self.structure[self.y+mouvement_y][self.x+mouvement_x] != "W":
            if set(self.structure[self.y+mouvement_y][self.x+mouvement_x]).issubset(set(objects)):
                self.pocket.append(self.structure[self.y+mouvement_y][self.x+mouvement_x])
            self.structure[self.y][self.x] = " "    
            self.x += mouvement_x
            self.y += mouvement_y
            self.structure[self.y][self.x] = "M"