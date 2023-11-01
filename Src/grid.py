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

    def add_status(self, color, mission, i, j):
        player = Player_Mission(color, mission, i,j)
        self.grid[i,j].status = player

    def create_grid(self):
        # _plate1.rotate()
        # _plate2.rotate()
        # _plate3.rotate()
        # _plate4.rotate()

        self.grid[:8,:8] = _plate1.l_grid
        self.grid[:8,8:] = _plate2.l_grid
        self.grid[8:,:8] = _plate3.l_grid
        self.grid[8:,8:] = _plate4.l_grid
 
    def grid_final(self):
        self.create_grid()
        self.wall_around()
        self.center_goal()
        #ROBOT INITIALIZED
        self.add_status(Color.RED, Mission.EMPTY, 0, 0)
        self.add_status(Color.BLUE, Mission.EMPTY, 2, 1)
        self.add_status(Color.YELLOW, Mission.EMPTY, 4, 7)
        self.add_status(Color.GREEN, Mission.EMPTY, 5, 12)
        #MISSION INITIALIZED
        #RED
        self.add_status(Color.RED, Mission.SQUARE, 13, 14)
        self.add_status(Color.RED, Mission.TRIANGLE, 5, 7)
        self.add_status(Color.RED, Mission.CIRCLE, 4, 14)
        self.add_status(Color.RED, Mission.STAR, 13, 1)
        #YELLOW
        self.add_status(Color.YELLOW, Mission.SQUARE, 6, 1)
        self.add_status(Color.YELLOW, Mission.TRIANGLE, 9, 4)
        self.add_status(Color.YELLOW, Mission.CIRCLE, 11, 9)
        self.add_status(Color.YELLOW, Mission.STAR, 6, 12)    
        #BLUE
        self.add_status(Color.BLUE, Mission.SQUARE, 3, 9)
        self.add_status(Color.BLUE, Mission.TRIANGLE, 9, 13)
        self.add_status(Color.BLUE, Mission.CIRCLE, 10, 6)
        self.add_status(Color.BLUE, Mission.STAR, 2, 5)
        #GREEN
        self.add_status(Color.GREEN, Mission.SQUARE, 15, 3)
        self.add_status(Color.GREEN, Mission.TRIANGLE, 1, 13)
        self.add_status(Color.GREEN, Mission.CIRCLE, 4, 2)
        self.add_status(Color.GREEN, Mission.STAR, 14, 10)
        self.update_super_goal()

    def update_super_goal(self):
        goal = Player_Mission(Color(rd.randint(1,4)),Mission(rd.randint(1,4)),7,7)
        self.grid[7,7].status = goal
        self.color_goal = goal.color
        self.mission_goal = goal.mission
    
    def display(self, screen):
        screen.fill((self.grid[0,0].color))
        for i in range(16):
            for j in range(16):
                x = j * 50
                y = i * 50
                
                if self.grid[i, j].wall[0]:
                    pygame.draw.line(screen, (0, 0, 0), (x, y), (x + 50, y), 5)
                else:
                    if not (i in [7, 8] and j in [7, 8]):
                        pygame.draw.line(screen, (0, 0, 0), (x, y), (x + 50, y), 1)
                if self.grid[i, j].wall[1]:
                    pygame.draw.line(screen, (0, 0, 0), (x + 50, y), (x + 50, y + 50), 5)
                else:
                    if not (i in [7, 8] and j in [7, 8]):
                        pygame.draw.line(screen, (0, 0, 0), (x + 50, y), (x + 50, y + 50), 1)
                if self.grid[i, j].wall[2]:
                    pygame.draw.line(screen, (0, 0, 0), (x, y + 50), (x + 50, y + 50), 5)
                else:
                    if not (i in [7, 8] and j in [7, 8]):
                        pygame.draw.line(screen, (0, 0, 0), (x, y + 50), (x + 50, y + 50), 1)
                if self.grid[i, j].wall[3]:
                    pygame.draw.line(screen, (0, 0, 0), (x, y), (x, y + 50), 5)
                else:
                    if not (i in [7, 8] and j in [7, 8]):
                        pygame.draw.line(screen, (0, 0, 0), (x, y), (x, y + 50), 1)

                if (self.grid[i][j].status.asset != "empty") & (not(i in [7, 8] and j in [7, 8])):
                    screen.blit(pygame.image.load(self.grid[i][j].status.asset), (x+7, y+7))

                if (i==7) & (j==7):
                    original_image = pygame.image.load(self.grid[i][j].status.asset)
                    scaled_image = pygame.transform.scale(original_image, (original_image.get_width() * 2.5, original_image.get_height() * 2.5))
                    screen.blit(scaled_image, (x+7, y+7))


        
 # Creation of the fourth plates        
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
