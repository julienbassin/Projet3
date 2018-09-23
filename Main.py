import pygame
from pygame.locals import *

from Level import *
from Perso import * 
from PersoMG import * 
from constants import *



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
            maze_loaded = a.load_maze_from_file("resource\labyrinthe.txt")
            a.display_maze(w)
            a.randomize_item_maze(w)
            b = Perso(a.structure)
            pygame.display.flip()
            
            continue_party = 1
            while continue_party:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        continue_party = 0
                        continue_game = 0
                    if event.type == KEYDOWN:
                        if event.key == K_DOWN:
                            b.move_position("low")
                        if event.key == K_UP:
                            b.move_position("high")
                        if event.key == K_LEFT:
                            b.move_position("left")
                        if event.key == K_RIGHT:
                            b.move_position("right")
                
                a.display_maze(w)
                pygame.display.flip()    

main()