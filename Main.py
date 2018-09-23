import pygame
from pygame.locals import *

from Level import Level
from Perso import Perso, PersoMG
from constants import SIDE_PIXEL



def main():
    """ Main loop """
    continue_game = 1
    while continue_game:
        pygame.init()
        w = pygame.display.set_mode((SIDE_PIXEL, SIDE_PIXEL))

        continue_menu = 1
        while continue_menu:
            pygame.time.Clock().tick(30)
        
            for event in pygame.event.get():
                if event.type == QUIT:
                    continue_menu = 0
                    continue_game = 0
                    choice = 0
                elif event.type == KEYDOWN:
                    if event.key == K_1:
                        continue_menu = 0
                        choice = "l1"
                    elif event.key == K_2:
                        continue_menu = 0 
                        choice = "l2"
        if  choice != 0:
            a = Level()
            a.load_maze_from_file("resource\labyrinthe.txt")            
            a.randomize_item_maze(w)
            mac_gyver = PersoMG("M")
            guardian = Perso("G")
            mac_gyver.get_position(a.structure)
            guardian.get_position(a.structure)

            a.display_maze(w)
            pygame.display.flip()
            
            continue_party = 1
            while continue_party:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        continue_party = 0
                        continue_game = 0
                    if event.type == KEYDOWN:
                        if event.key == K_DOWN:
                            mac_gyver.move_position(a.structure, "low")
                        if event.key == K_UP:
                            mac_gyver.move_position(a.structure, "high")
                        if event.key == K_LEFT:
                            mac_gyver.move_position(a.structure, "left")
                        if event.key == K_RIGHT:
                            mac_gyver.move_position(a.structure, "right")
                if a.check_position(mac_gyver, guardian, mac_gyver.pocket):
                    break
                a.display_maze(w)
                pygame.display.flip()    

main()