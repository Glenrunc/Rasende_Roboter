import numpy as np
import random as rd
import pygame 
import sys
import time as t
from player_mission import *

# PASTEL BLUE (173, 216, 230)
# PASTEL RED  (255, 182, 193)
# PASTEL GREEN  (173, 255, 173)
# PASTEL YELLOW  (255, 255, 191) OR (255, 240, 100)

MOOVE_MAP ={
    (Color.BLUE) : (173, 216, 230),
    (Color.YELLOW) : (255, 240, 100),
    (Color.GREEN) : (173, 255, 173),
    (Color.RED) : (255, 182, 193),
}

class Case(object):

    def __init__(self,up=False,right=False,down=False,left=False, _status = Player(), _color =(255,255,255)):
        self.color= _color
        self.wall = np.array([up,right,down,left])
        self.status = _status
        
    def empty(self):
        self.wall = False
    
    def rot90(self):
        self.wall = np.roll(self.wall,1)

    def update_color(self,rgb):
        self.color = rgb

    def clean(self):
        self.color = (255,255,255)
