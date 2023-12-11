from grid import *
from bfs import  *
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
        self.in_menu = True
        self.start_position_robot = self.grid.position_robot
        clean_all_status(self.grid,self.start_position_robot)
        self.grid.initHeur(self.start_position_robot)

        self.grid.printHeur()
        #print(self.grid.position_robot)
        # self.grid.possible_move()
        # self.grid.get_position(Color.BLUE,'DOWN')
        # print(self.grid.possible_move_per_robot)


        # TESTS IA
        # goal_position = self.grid.goal_coordinate
        # color_robot =self.grid.color_goal
        # print("position du robot", color_robot)
        # print("position à atteindre", goal_position)

        # robot_position = self.grid.position_robot[color_robot]

        # a_star_search(self.grid,robot_position, color_robot,goal_position)
        #chemin = BFS(self.grid,robot_position, goal_position)
        #iaSolution(self.grid, color_robot, goal_position)
        # test(self.grid)


    def display_menu(self):

        self.screen.blit(pygame.image.load("../Asset/play.png"),(225,300))
        self.screen.blit(pygame.image.load("../Asset/quit.png"),(225,450))
        self.screen.blit(pygame.image.load("../Asset/copyright.png"),(225,700))
        self.screen.blit(pygame.image.load("../Asset/designed.png"),(225,25))
        self.screen.blit(pygame.image.load("../Asset/by.png"),(225,110))
        self.screen.blit(pygame.image.load("../Asset/tag.png"),(225,175))

    def run(self):
        while True:
            self.grid.win(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    x, y = (y - 40) // 45, (x - 40) // 45


                    if self.in_menu:
                        if 6 <= x <= 7 and 5 <= y <= 10:
                            self.in_menu = False
                            self.screen.fill((255, 255, 255))
                        elif 9 <= x <= 10 and 5 <= y <= 10:
                            pygame.quit()
                            sys.exit()
                    else:
                        self.grid.reset(x, y)
                        self.grid.move(x, y)


            if self.in_menu:
                self.display_menu()
            else:
                self.grid.display(self.screen)

            pygame.display.flip()
            self.clock.tick(30)

