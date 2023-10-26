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

            
class Plate(object):

    def __init__(self,N):
        self.N = N
        self.l_grid = np.array([[Case() for _ in range(N)] for _ in range(N)])
        # self.grid = np.array([[i+1 for _ in range(N)] for i in range(N)]) #Good example

    def rotate(self):
        n = rd.randint(1,3)
        for _ in range(n % 4):  # Ensure n is between 1 and 3
            self.l_grid = np.rot90(self.l_grid,axes=(1,0))
            for i in range (self.N):
                for j in range (self.N):
                    self.l_grid[i][j].rot90()


_plate1 = Plate(8)
_plate1.l_grid[0][3].wall[1] = True
_plate1.l_grid[2][5].wall[1] = True 
_plate1.l_grid[2][5].wall[2] = True
_plate1.l_grid[4][0].wall[2] = True
_plate1.l_grid[4][2].wall[1] = True
_plate1.l_grid[4][2].wall[0] = True
_plate1.l_grid[5][1].wall[2] = True
_plate1.l_grid[5][7].wall[2] = True
_plate1.l_grid[5][7].wall[3] = True
_plate1.l_grid[6][1].wall[3] = True
_plate1.l_grid[6][1].wall[0] = True

_plate2 = Plate(8)
_plate2.l_grid[0][1].wall[1] = True
_plate2.l_grid[1][5].wall[1] = True
_plate2.l_grid[1][5].wall[1] = True
_plate2.l_grid[1][5].wall[1] = True
_plate2.l_grid[3][1].wall[3] = True
_plate2.l_grid[3][1].wall[0] = True
_plate2.l_grid[4][6].wall[0] = True
_plate2.l_grid[4][6].wall[1] = True
_plate2.l_grid[6][4].wall[2] = True
_plate2.l_grid[6][4].wall[3] = True

_plate3 = Plate(8)
_plate3.l_grid[1][4].wall[2] = True
_plate3.l_grid[1][4].wall[3] = True
_plate3.l_grid[2][0].wall[2] = True
_plate3.l_grid[2][6].wall[3] = True
_plate3.l_grid[2][6].wall[0] = True
_plate3.l_grid[4][7].wall[0] = True
_plate3.l_grid[4][7].wall[1] = True
_plate3.l_grid[5][1].wall[0] = True
_plate3.l_grid[5][1].wall[1] = True
_plate3.l_grid[6][3].wall[1] = True
_plate3.l_grid[6][3].wall[2] = True
_plate3.l_grid[7][4].wall[1] = True

_plate4 = Plate(8)
_plate4.l_grid[1][5].wall[2] = True
_plate4.l_grid[1][5].wall[3] = True
_plate4.l_grid[3][1].wall[1] = True
_plate4.l_grid[3][1].wall[2] = True
_plate4.l_grid[4][7].wall[0] = True
_plate4.l_grid[5][6].wall[0] = True
_plate4.l_grid[5][6].wall[1] = True
_plate4.l_grid[6][2].wall[0] = True
_plate4.l_grid[6][2].wall[3] = True
_plate4.l_grid[7][4].wall[3] = True


class Grid(object):
    def __init__(self, plate1 : Plate,plate2 : Plate, plate3: Plate, plate4: Plate):
        self.plate1 = plate1
        self.plate2 = plate2
        self.plate3 = plate3
        self.plate4 = plate4
        self.grid = np.zeros((16,16),dtype=object)

    def wall_around(self):
        for i in range(16):
            self.grid[0, i].wall[0] = True
            self.grid[i, 0].wall[3] = True
            self.grid[-1, i].wall[2] = True
            self.grid[i, -1].wall[1] = True

    def center_goal(self):
        self.grid[7,7].wall[3] = True
        self.grid[7,7].wall[0] = True
        self.grid[7,8].wall[0] = True
        self.grid[7,8].wall[1] = True
        self.grid[8,7].wall[3] = True
        self.grid[8,7].wall[2] = True
        self.grid[8,8].wall[1] = True
        self.grid[8,8].wall[2] = True
    
    def create_grid(self):
        self.plate1.rotate()
        self.plate2.rotate()
        self.plate3.rotate()
        self.plate4.rotate()

        self.grid[:8,:8] = self.plate1.l_grid
        self.grid[:8,8:] = self.plate2.l_grid
        self.grid[8:,:8] = self.plate3.l_grid
        self.grid[8:,8:] = self.plate4.l_grid


    
    def grid_final(self):
        self.create_grid()
        self.wall_around()
        self.center_goal()

    def display(self, screen):
        for i in range(16):
            for j in range(16):
                x = j * 50
                y = i * 50

                if self.grid[i, j].wall[0]:
                    pygame.draw.line(screen, (0, 0, 0), (x, y), (x + 50, y), 5)
                else:
                    pygame.draw.line(screen, (0, 0, 0), (x, y), (x + 50, y), 1)
    
                if self.grid[i, j].wall[1]:
                    pygame.draw.line(screen, (0, 0, 0), (x + 50, y), (x + 50, y + 50), 5)
                else:
                    pygame.draw.line(screen, (0, 0, 0), (x + 50, y), (x + 50, y + 50), 1)
    
                if self.grid[i, j].wall[2]:
                    pygame.draw.line(screen, (0, 0, 0), (x, y + 50), (x + 50, y + 50), 5)
                else:
                    pygame.draw.line(screen, (0, 0, 0), (x, y + 50), (x + 50, y + 50), 1)
    
                if self.grid[i, j].wall[3]:
                    pygame.draw.line(screen, (0, 0, 0), (x, y), (x, y + 50), 5)
                else:
                    pygame.draw.line(screen, (0, 0, 0), (x, y), (x, y + 50), 1)






class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Rasende Roboter")
        self.clock = pygame.time.Clock()

        self.grid = Grid(_plate1,_plate2,_plate3,_plate4)  
        self.grid.grid_final()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill((255, 255, 255))
            self.grid.display(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

game = Game()
game.run()