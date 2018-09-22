from Level import Level
from PersoMG import PersoMG
from PersoGuardian import PersoGuardian

#faire une class APP
    #def init
    #def run
    #design pattern
def main():
    """ Main loop """
    maze = Level("labyrinthe.txt")
    continue_loop = 1
    #virer les doubles boucles
    while continue_loop:
        continue_game = 1
        continue_menu = 1
        while continue_menu:
            #ajouter un design pattern pour le menu
            maze.print_menu()
            choice = input("Enter your choice [1-2]: ")
            if choice == 'q' or choice == 'quit':
                continue_menu = 0
                continue_game = 0
            elif choice == "1":
                maze.generate_maze()
                mac_gyver = PersoMG(a.structure, "M")
                guardian = PersoGuardian(a.structure, "G")
                position_MG = mac_gyver.get_position("M")
                position_G = guardian.get_position("G")
                #ajouter cela dans la génération de l'objet
                print("{0} has been created and his coordinates are : {1}".format(mac_gyver.name, position_MG))
                print("{0} has been created and his coordinates are : {1}".format(guardian.name, position_G))
                maze.randomize_item_maze()
                #ajouter un clear pour eviter de relancer le maze
                maze.display_maze()
                continue_menu = 0
                while continue_game:                
                    choice_move = input("Please enter a direction: ")
                    position_MG = b.move_position(choice_move)
                    maze.check_position(position_MG, position_G, b.pocket)                 
                    maze.display_maze()
            elif choice == "2":
                pygame.init()
                w = pygame.display.set_mode((SIDE_PIXEL, SIDE_PIXEL))

                a = GameLevel()
                a.load_maze_from_file("resource\labyrinthe.txt")
                a.display_maze(w)
                #a.randomize_item_maze(w)
                pygame.display.flip()

                continuer = 1
                #pygame.key.set_repeat(400, 30)
                #saut d'un pixel (exemple 1 case = 40 pixel)
                #while continuer:
                #    for event in pygame.event.get():
                #        if event.type == QUIT:
                #            continuer = 0
                #        if event.type == KEYDOWN:
                #            if event.key == K_DOWN:
                #                position_perso = position_perso.move(0,PIXEL_LENGTH)
                #            if event.key == K_UP:
                #                position_perso = position_perso.move(0,-PIXEL_LENGTH)
                #            if event.key == K_LEFT:
                #                position_perso = position_perso.move(-PIXEL_LENGTH,0)
                #            if event.key == K_RIGHT:
                #                position_perso = position_perso.move(PIXEL_LENGTH,0)

                #    fenetre.blit(fond, (0,0))
                #    fenetre.blit(perso, position_perso)
                #    pygame.display.flip()a = GameLevel("resource\labyrinthe.txt")


