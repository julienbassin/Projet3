import pygame
from pygame.locals import *

from Level import *
from Perso import * 
from constants import *


def main():
    """ Main loop """
    pygame.init()
    w = pygame.display.set_mode((SIDE_PIXEL, SIDE_PIXEL))

    a = Level()
    a.load_maze_from_file("resource\labyrinthe.txt")
    a.display_maze(w)
    a.randomize_item_maze(w)
    pygame.display.flip()
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


main()