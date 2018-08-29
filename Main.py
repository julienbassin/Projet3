from Level import Level
from PersoMG import PersoMG
from PersoGuardian import PersoGuardian
#faire une class APP
    #def init
    #def run

def main():
    """ Main loop """
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
                b = PersoMG(a.structure, "M")
                c = PersoGuardian(a.structure, "G")
                b.get_position("M")
                c.get_position("G")
                a.randomize_item_maze()
                a.display_maze()
                continue_menu = 0
                while continue_game:                
                    choice_move = input("Please enter a direction: ")
                    b.move_position(choice_move)
                    a.display_maze()
            elif choice == "2":
                print("choice 2 has been selected !")
                continue_menu = 0
main()

