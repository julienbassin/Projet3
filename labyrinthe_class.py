class Level:
    """ 
    la class game sera la classe mère 
    la class game initialisera les cartes des labyrinthes
    la class game ouvrira les fichiers 

    la class fille irritera de la class mère et de ses propriétés
    la class fille aura comme methode de récupérer la position de MG
    la class fille aura comme methode de modifier la position de MG
    la class fille aura comme méthode de bouger la position de MG (terminal ou grpahique)
    
    """
    def __init__(self, file):
        self.file = file
        self.structure = []
        self.random_choice = ['E','R','T', 'Y']
    
    def generate_maze(self):
        with open(self.file) as file:
            lines = file.read().split("\n")
            structure_level=[]        
            for line in lines:
                line_level=[]
                for sprite in line:
                    if sprite != "\n":
                        line_level.append(sprite)
                structure_level.append(line_level)
                self.structure = structure_level
    
    def display_maze(self):
        for liste in self.structure:
            for item in liste:
                print(item, end='')
            print()

    def random_item_maze(self):
        i = 0
        while i < len(self.random_choice):
            x  = random.randint(0,14)
            y =  random.randint(0,14)
            if self.structure[x][y] == " ":
                    self.structure[x][y] = self.random_choice[i]
                    i+=1
    @staticmethod
    def print_menu():
        print(30 * "-" , "MENU" , 30 * "-")
        print("1. Console Game")
        print("2. GUI Game")
        print("3. Exit")
        print(67 * "-")

class Perso():
    def __init__(self, structure, name):
        self.x = 0
        self.y = 0
        self.structure = structure
        self.name = name

    def get_position(self, letter):
        for line in range(game_constants.width):
            for column in range(game_constants.height):
                if self.structure[line][column] == letter:
                    self.x, self.y = column, line
                    print("{0} has been created and his coordinates are : {1}".format(self.name, (self.x, self.y)))

class Perso_MG(Perso):

    def move_position_left(self, direction):
        if direction == "le" and self.x > 0:
            if self.structure[self.y][self.x-1] != "W":
                self.structure[self.y][self.x] = " "
                self.x -=1                
                self.structure[self.y][self.x] = "M"
            else: 
                print("this is a wall !")

    def move_position_right(self, direction):
        if direction == "r" and self.x < game_constants.width:
            if self.structure[self.y][self.x+1] != "W":
                self.structure[self.y][self.x] = " "
                self.x +=1
                self.structure[self.y][self.x] = "M"
            else:
                print("this is a wall! ")

    def move_position_high(self, direction):
        if self.direction == "h" and self.y > 0:
            if self.structure[self.y-1][self.x] != "W":
                self.structure[self.y][self.x] = " "
                self.y -=1
                self.structure[self.y][self.x] = "M"
            else: 
                print("this is a wall !")

    def move_position_low(self, direction):
        if self.direction == "lo" and self.y < game_constants.height:
            if self.structure[self.y+1][self.x] != "W":
                self.structure[self.y][self.x] = " "
                self.y +=1
                self.structure[self.y][self.x] = "M"
            else:
                print("this is a wall !")

class Perso_Guardian(Perso):
    pass
            
a = Level("labyrinthe.txt")
continue_loop = 1
while continue_loop:
    continue_game = 1
    continue_menu = 1
    while continue_menu:
        a.print_menu()
        choice = input("Enter your choice [1-2] : ")
        if choice  == 'q' or choice == 'quit':
            continue_menu = 0
            continue_game = 0
        elif choice == "1":
            print("Let's play !")
            a.generate_maze()
            b = Perso_MG(a.structure, "MG")
            c = Perso_Guardian(a.structure, "G")
            #classe qui génère la position et affiche la carte
            b.get_position("M")
            c.get_position("G")
            a.random_item_maze()
            a.display_maze()
            continue_menu = 0
            while continue_game:                
                choice_move = input("Please enter a direction")
                if choice_move == "r":
                    b.move_position_right(choice_move)
                if choice_move == "le":
                    b.move_position_left(choice_move)
                if choice_move == "h":
                    b.move_position_high(choice_move)
                if choice_move == "lo":
                    b.move_position_low(choice_move)
                a.display_maze()
        elif choice == "2":
            print("choice 2 has been selected !")
            continue_menu = 0
            
        




