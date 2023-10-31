import numpy as np
import random as rd
import pygame 
import sys
from player_mission import *


class Case(object):

    def __init__(self,up=False,right=False,down=False,left=False, _status = Player_Mission()):

        self.wall = np.array([up,right,down,left])
        self.status = _status
        
    def empty(self):
        self.wall = False
    
    def rot90(self):
        self.wall = np.roll(self.wall,1)