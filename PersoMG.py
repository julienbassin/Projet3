from Perso import Perso
from game_constants import height
from game_constants import width

class PersoMG(Perso):
    """
        this is a subclass herited by the root-class for Mac_Gyver
    """
    def move_position(self, direction):
        """
                        this method allows Mac_Gyver to move on the left
        """
        if direction == "le" and self.x > 0:
            if self.structure[self.y][self.x-1] != "W":
                self.structure[self.y][self.x] = " "
                self.x -= 1                
                self.structure[self.y][self.x] = "M"
            if direction == "r" and self.x < width:
                if self.structure[self.y][self.x+1] != "W":
                    self.structure[self.y][self.x] = " "
                    self.x += 1
                    self.structure[self.y][self.x] = "M"
            if direction == "h" and self.y > 0:
                if self.structure[self.y-1][self.x] != "W":
                    self.structure[self.y][self.x] = " "
                    self.y -=1
                    self.structure[self.y][self.x] = "M"
            if direction == "lo" and self.y < height:
                if self.structure[self.y+1][self.x] != "W":
                    self.structure[self.y][self.x] = " "
                    self.y +=1
                    self.structure[self.y][self.x] = "M"
            else: 
                print("this is a wall!\n")
