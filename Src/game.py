from grid import *
from a_star import *

    
class Game:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((HEIGHT,WIDTH))
        pygame.display.set_caption("Rasende Roboter")
        self.clock = pygame.time.Clock()
        self.screen.fill((255,255,255))
        self.grid = Grid()  
        self.grid.grid_final()
        # print(self.grid.position_robot)
        # self.grid.get_position(Color.BLUE,'DOWN')
    
    def run(self):

        # TESTS IA
        goal_position = self.grid.goal_coordinate
        color_robot =self.grid.color_goal
        print("position du robot", color_robot)
        print("position à atteindre", goal_position)

        robot_position = self.grid.position_robot[color_robot]
        #chemin = BFS(self.grid,robot_position, goal_position)
        #iaSolution(self.grid, color_robot, goal_position)

        test(self.grid)

        while True:
            self.grid.win(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if (event.type == pygame.MOUSEBUTTONDOWN):
                    if(event.button == 1):
                        (x,y) = pygame.mouse.get_pos()
                        
                        (x,y) = ((y-40)//45,(x-40)//45)
                        print((x,y))
                        self.grid.move(x,y)

            
            self.grid.display(self.screen)
            pygame.display.flip()
            self.clock.tick(60)



