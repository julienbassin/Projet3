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
        for line in range(game_constants.width):
            for column in range(game_constants.height):
                if self.structure[line][column] == letter:
                    self.x, self.y = column, line
                    print("{0} has been created and his coordinates are : {1}".format(self.name, (self.x, self.y)))
