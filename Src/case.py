import numpy as np
import random as rd
import pygame 
import sys

class Case(object):

    def __init__(self,up=False,right=False,down=False,left=False):

        self.wall = np.array([up,right,down,left])

    def empty(self):

        self.wall = False
    
    def rot90(self):
        self.wall = np.roll(self.wall,1)