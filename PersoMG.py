import pygame
from pygame.locals import *

from Perso import Perso
from constants import *

""" 
    Faire un enum  + tableau de translation
    EnumDirection = {

        high : (0,-1)
        Low : (0,1)
        Left : (-1,0)
        Right : (1,0)
        
    }

    EnumCase = {
        
        Guardian :  G
        Mac_Gyver : M
    }

    Vérifier que c'est un enum 
"""

class PersoMG(Perso):
    """
        this is a subclass herited by the root-class for Mac_Gyver
    """
    def __init__(self,structure,name):
        Perso.__init__(self, structure, name)
        


    
