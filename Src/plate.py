from case import *

class Plate(object):

    def __init__(self):
        self.N = 8
        self.l_grid = np.array([[Case() for _ in range(self.N)] for _ in range(self.N)])

    def rotate(self):
        n = rd.randint(1,3)
        for _ in range(n % 4):  # Ensure n is between 1 and 3
            self.l_grid = np.rot90(self.l_grid,axes=(1,0))
            for i in range (self.N):
                for j in range (self.N):
                    self.l_grid[i][j].rot90()
                    
    #TOdo define qt the end of the project
    # def look_around_case(self,i,j):

    #     pass

    #   # Define random generation wall
    # def wall_generation(self,number_of_the_plate):
    #     i = rd.randint(1,6)
    #     j = rd.randint(1,6)
        
    #     if number_of_the_plate == 0:
    #         self.l_grid[0,j].wall[1] = True
    #         self.l_grid[i,0].wall[2] = True
        
    #     if number_of_the_plate == 1:
    #         self.l_grid[0,j].wall[1] = True
    #         self.l_grid[i,7].wall[2] = True

    #     if number_of_the_plate == 2 :
    #         self.l_grid[7,j].wall[1] = True
    #         self.l_grid[i,0].wall[2] = True
        
    #     if number_of_the_plate == 3:
    #         self.l_grid[7,j].wall[3] = True
    #         self.l_grid[i,7].wall[0] = True

    #     for i in range(4):
    #         k = rd.randint(1,7)
    #         l = rd.randint(1,7)

