import numpy as np
import random as rd
import pygame 
import sys
from player_mission import *

# bleu_pastel = (173, 216, 230)
# rouge_pastel = (255, 182, 193)
# vert_pastel = (173, 255, 173)
# jaune_pastel = (255, 255, 191)

class Case(object):

    def __init__(self,up=False,right=False,down=False,left=False, _status = Player(), _color =(255,255,255)):
        self.color= _color
        self.wall = np.array([up,right,down,left])
        self.status = _status
        
    def empty(self):
        self.wall = False
    
    def rot90(self):
        self.wall = np.roll(self.wall,1)
