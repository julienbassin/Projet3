from constants import * 

class Perso():
    """
        the class Perso is mother-class which initialize the coordonates of persons
        it gets the position of any personnages
    """
    def __init__(self, structure, name):
        """
            Initialization of structure, Perso's name and coordinates
        """
        self.x = 0
        self.y = 0
        self.structure = structure
        self.name = name

    def get_position(self, letter):
        """
            Get the position of any personnages. it takes one parameter letter
        """
        for line in range(NUMBER_SPRITE):
            for column in range(NUMBER_SPRITE):
                if self.structure[line][column] == letter:
                    self.x, self.y = column, line
        return (self.x, self.y)
