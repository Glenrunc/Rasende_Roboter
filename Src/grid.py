from plate import * 

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
        # self.plate1.rotate()
        # self.plate2.rotate()
        # self.plate3.rotate()
        # self.plate4.rotate()

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

