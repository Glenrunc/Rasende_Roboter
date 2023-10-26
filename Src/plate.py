from case import *

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


