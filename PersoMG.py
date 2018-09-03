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
        elif direction == "r" and self.x < width:
            self.new_position_MG(1,0)
        elif direction == "h" and self.y > 0:
            self.new_position_MG(0,-1)
        elif direction == "lo" and self.y < height:
             self.new_position_MG(0,1)
        else:
             print("You can't do that move")
        print(self.pocket)
        return self.x, self.y

    def new_position_MG(self, mouvement_x, mouvement_y):
        if self.structure[self.y+mouvement_y][self.x+mouvement_x] != "W" and self.structure[self.y+mouvement_y][self.x+mouvement_x] != "G":
            if set(self.structure[self.y+mouvement_y][self.x+mouvement_x]).issubset(set(objects)) and len(self.pocket) < 4:
                self.pocket.append(self.structure[self.y+mouvement_y][self.x+mouvement_x])
            self.structure[self.y][self.x] = " "    
            self.x += mouvement_x
            self.y += mouvement_y
            self.structure[self.y][self.x] = "M"
