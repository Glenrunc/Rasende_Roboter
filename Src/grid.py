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
     
class Plate:

    def __init__(self,N):
        self.N = N
        self.grid = np.array([[Case() for _ in range(N)] for _ in range(N)])
        # self.grid = np.array([[i+1 for _ in range(N)] for i in range(N)]) #Good example

    def rotate(self,n):
        for _ in range(n % 4):  # Ensure n is between 0 and 3
            self.grid = np.rot90(self.grid)

# plate  = Plate(8)

# for i in range(4):
#     print (plate.grid)
#     print("\n")
#     plate.rotate(i+1)

#Creation of four plate 

plate1 = Plate(8)
plate1.grid[0][5].right = True
plate1.grid[3][1].up = True 
plate1.grid[3][1].left = True
plate1.grid[4][6].right = True
plate1.grid[4][6].down = True
plate1.grid[5][0].up = True
plate1.grid[5][2].up = True
plate1.grid[5][2].right = True
plate1.grid[5][3].down = True
