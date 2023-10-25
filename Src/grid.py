import numpy as np


class Case:

    def __init__(self,up=False,down=False,right=False,left=False):
        self.up = up
        self.down = down
        self.right = right
        self.left = left

    def center(self):
        self.up = True
        self.down = True
        self.right = True
        self.left = True  

    def empty(self):
        self.up = False
        self.down = False
        self.right = False
        self.left = False  
    
    def rot90(self): None
        #Todo

class Plate:

    def __init__(self,N):
        self.N = N
        self.l_grid = np.array([[Case() for _ in range(N)] for _ in range(N)])
        # self.grid = np.array([[i+1 for _ in range(N)] for i in range(N)]) #Good example

    def rotate(self,n):
        for _ in range(n % 4):  # Ensure n is between 0 and 3
            self.l_grid = np.rot90(self.l_grid)


_plate1 = Plate(8)
_plate1.l_grid[0][3].right = True
_plate1.l_grid[2][5].right = True 
_plate1.l_grid[2][5].down = True
_plate1.l_grid[4][0].down = True
_plate1.l_grid[4][2].right = True
_plate1.l_grid[4][2].up = True
_plate1.l_grid[5][1].down = True
_plate1.l_grid[5][7].down = True
_plate1.l_grid[5][7].left = True
_plate1.l_grid[6][1].left = True
_plate1.l_grid[6][1].up = True

_plate2 = Plate(8)
_plate2.l_grid[0][1].right = True
_plate2.l_grid[1][5].right = True
_plate2.l_grid[1][5].right = True
_plate2.l_grid[1][5].right = True
_plate2.l_grid[3][1].left = True
_plate2.l_grid[3][1].up = True
_plate2.l_grid[4][6].up = True
_plate2.l_grid[4][6].right = True
_plate2.l_grid[6][4].down = True
_plate2.l_grid[6][4].left = True

_plate3 = Plate(8)
_plate3.l_grid[1][4].down = True
_plate3.l_grid[1][4].left = True
_plate3.l_grid[2][0].down = True
_plate3.l_grid[2][6].left = True
_plate3.l_grid[2][6].up = True
_plate3.l_grid[4][7].up = True
_plate3.l_grid[4][7].right = True
_plate3.l_grid[5][1].up = True
_plate3.l_grid[5][1].right = True
_plate3.l_grid[6][3].right = True
_plate3.l_grid[6][3].down = True
_plate3.l_grid[7][4].right = True

_plate4 = Plate(8)
_plate4.l_grid[1][5].down = True
_plate4.l_grid[1][5].left = True
_plate4.l_grid[3][1].right = True
_plate4.l_grid[3][1].down = True
_plate4.l_grid[4][7].up = True
_plate4.l_grid[5][6].up = True
_plate4.l_grid[5][6].right = True
_plate4.l_grid[6][2].up = True
_plate4.l_grid[6][2].left = True
_plate4.l_grid[7][4].left = True

class Grid:
    def __init__(self, plate1 : Plate,plate2 : Plate, plate3: Plate, plate4: Plate):
        self.plate1 = plate1
        self.plate2 = plate2
        self.plate3 = plate3
        self.plate4 = plate4
        self.grid = np.zero((16,16))

    def wall_around(self):
        self.grid[1,:].up = True
        self.grid[:,1].left = True
        self.grid[7,:].down = True
        self.grid[:,7].right = True

    def center_goal(self):
        self.grid[7:8,7:8].center()
    
    def create_grid(self):
        self.grid[:8,:8] = self.plate1
        self.grid[:8,8:] = self.plate2
        self.grid[8:,:8] = self.plate3
        self.grid[8:,8:] = self.plate4

    def grid_final(self):
        self.create_grid()
        self.wall_around()
        self.center_goal()
        #DO RANDOM ROTATION