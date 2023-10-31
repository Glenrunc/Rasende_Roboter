from plate import * 

class Grid(object):
    def __init__(self):

        self.grid = np.array([[Case() for _ in range(16)] for _ in range(16)])

    def wall_around(self):
        for i in range(16):
            self.grid[0, i].wall[0] = True
            self.grid[i,0].wall[3] = True
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

    def add_robot(self, color, mission, x, y):
        player = Player_Mission(color, mission, x, y)
        self.grid[y, x].status = player

    def create_grid(self):
        _plate1.rotate()
        _plate2.rotate()
        _plate3.rotate()
        _plate4.rotate()

        self.grid[:8,:8] = _plate1.l_grid
        self.grid[:8,8:] = _plate2.l_grid
        self.grid[8:,:8] = _plate3.l_grid
        self.grid[8:,8:] = _plate4.l_grid
 
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
                if self.grid[i][j].status.asset != "empty":
                    screen.blit(pygame.image.load(self.grid[i][j].status.asset), (x+7, y+7))

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
