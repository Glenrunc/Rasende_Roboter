from grid import *
from bfs_dfs import  *
from a_star import *
    
class Game:
    
    def __init__(self,grid:Grid):
        
        #Initialization
        pygame.init()
        self.screen = pygame.display.set_mode((HEIGHT,WIDTH))
        pygame.display.set_caption("Rasende Roboter")
        self.clock = pygame.time.Clock()
        self.screen.fill((255,255,255))

        #Boolean to decide which screen show 
        self.in_menu = True
        self.in_rules_menu = False
        self.in_choice_menu = False
        self.in_game = True
        self.mode_review = False
        self.is_end = False
        self.win_menu = False
        #Preparation of the grid 
        self.grid = grid  
        self.grid.grid_final()
        self.start_position_robot = self.grid.position_robot

        #While round_count <= 2 -> run 
        # self.round_count = 0
        #Usefull to process the review mode
        self.grid.begin_path = 0
        self.final_count_player = 0

        

    def display_menu(self):

        self.screen.blit(pygame.image.load("../Asset/play.png"),(225,300))
        self.screen.blit(pygame.image.load("../Asset/quit.png"),(225,450))
        self.screen.blit(pygame.image.load("../Asset/copyright.png"),(225,700))
        self.screen.blit(pygame.image.load("../Asset/designed.png"),(225,25))
        self.screen.blit(pygame.image.load("../Asset/by.png"),(225,110))
        self.screen.blit(pygame.image.load("../Asset/tag.png"),(225,175))

    def display_rules_menu(self):
        self.screen.blit(pygame.image.load("../Asset/rules.png"),(115,50))
        self.screen.blit(pygame.image.load("../Asset/rules_2.png"),(115,400))
        self.screen.blit(pygame.image.load("../Asset/next.png"),(750,0))
        self.screen.blit(pygame.image.load("../Asset/back.png"),(0,0))

    def display_choice_menu(self):
        self.screen.blit(pygame.image.load("../Asset/hardcore.png"),(115,50))
        self.screen.blit(pygame.image.load("../Asset/medium.png"),(115,250))
        self.screen.blit(pygame.image.load("../Asset/easy.png"),(115,500))
        self.screen.blit(pygame.image.load("../Asset/back.png"),(0,0))
    
    def display_mode_review(self):
        
        self.screen.blit(pygame.image.load("../Asset/arrow_right.png"), (500, 0))
        self.screen.blit(pygame.image.load("../Asset/arrow_left.png"), (400, 0))
        self.screen.blit(pygame.image.load("../Asset/ok.png"), (600, 0))

    def display_screen_ending(self):
        if self.final_count_player< self.count_final:
            self.screen.fill((34, 177, 76))
            font = pygame.font.Font(None,50)
            text = font.render("YOU HAVE WON",True,(0,0,0))
            pos = (125,375)
            pos2 = (125,425)
            if self.count_final == 999:
                score = "YOU : " + str(self.final_count_player) + " MOVE /  IA : NO MOVE FOUND"
            else:
                score = "YOU : " + str(self.final_count_player) + " MOVE /  IA : " + str(self.count_final) + " MOVE"

            text2= font.render(score,True,(0,0,0))
            self.screen.blit(text,pos)
            self.screen.blit(text2,pos2)
            self.screen.blit(pygame.image.load("../Asset/winner.png"), (120, 50))

        if self.final_count_player > self.count_final:
            self.screen.fill((227, 38, 26))
            font = pygame.font.Font(None,50)
            text = font.render("YOU HAVE LOST",True,(0,0,0))
            pos = (125,375)
            pos2 = (125,425)
            score = "YOU : " + str(self.final_count_player) + " MOVE /  IA : " + str(self.count_final) + " MOVE"
            text2= font.render(score,True,(0,0,0))
            self.screen.blit(text,pos)
            self.screen.blit(text2,pos2)
            self.screen.blit(pygame.image.load("../Asset/loser.png"), (120, 50))
        if self.final_count_player == self.count_final:
            self.screen.fill((255, 172, 42))
            font = pygame.font.Font(None,50)
            text = font.render("EQUALITY",True,(0,0,0))
            pos = (125,375)
            pos2 = (125,425)
            score = "YOU : " + str(self.final_count_player) + " MOVE /  IA : " + str(self.count_final) + " MOVE"
            text2= font.render(score,True,(0,0,0))
            self.screen.blit(text,pos)
            self.screen.blit(text2,pos2)

        text3 = font.render("RESTART THE GAME",True,(0,0,0))
        pos3 = (125,500)
        text4 = font.render("IF YOU WANT TO PLAY AGAIN",True,(0,0,0))
        pos4 = (125,550)
        self.screen.blit(text3,pos3)
        self.screen.blit(text4,pos4)


    def run(self,difficulty):
        self.screen.fill((255, 255, 255))
        #Use DFS
        if difficulty == 1 : 
            clean_all_status(self.grid,self.start_position_robot)
            result = BFS_or_DFS(self.grid,Node(self.start_position_robot,None),self.grid.color_goal,self.grid.goal_coordinate,False)
            if result is not None:
                self.path, self.count_final = result
            else:
                self.path = None
                self.count_final = 999
            # self.grid.initHeur(self.start_position_robot)
            self.grid.actualize_robot_position()
            clean_all_status(self.grid,self.grid.position_robot)
            add_status_empty_grid(self.grid,self.start_position_robot)
            if self.path != None:
                print("*********DFS_SOLUTION***********\n")
                print("In -->",self.count_final," move\n")
                for position in self.path:
                    print(position)
            else:
                print("No solution found for DFS........")
        #Use BFS
        if difficulty == 2 :
            clean_all_status(self.grid,self.start_position_robot)
            result = BFS_or_DFS(self.grid,Node(self.start_position_robot,None),self.grid.color_goal,self.grid.goal_coordinate,True)
            if result is not None:
                self.path, self.count_final = result
            else:
                self.path = None
                self.count_final = 999
            # self.grid.initHeur(self.start_position_robot)
            self.grid.actualize_robot_position()
            clean_all_status(self.grid,self.grid.position_robot)
            add_status_empty_grid(self.grid,self.start_position_robot)
            if self.path != None:
                print("*********BFS_SOLUTION***********\n")
                print("In -->",self.count_final," move\n")
                for position in self.path:
                    print(position)
            else:
                print("No solution found for BFS........")
        #Use A*
        if difficulty == 3 :
            self.grid.initHeur(self.start_position_robot)
            # self.grid.actualize_robot_position()
            # clean_all_status(self.grid,self.grid.position_robot)
            # add_status_empty_grid(self.grid,self.start_position_robot)
            # if self.path != None:
            #     print("*********A* SOLUTION***********\n")
            #     print("In -->",self.count_final," move\n")
            #     for position in self.path:
            #         print(position)
            # else:
            #     print("No solution found for A*........")

        if self.path != None:
            end_path = len(self.path) - 1

        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    x, y = (y - 40) // 45, (x - 40) // 45
                    self.grid.reset(x, y)
                    self.grid.move(x, y)   
                    
                    
                    if self.in_game:

                        if self.grid.win(self.screen):
                            self.final_count_player = self.grid.count_move
                            self.in_game = False
                            self.win_menu = True
                            self.grid.actualize_robot_position()
                            clean_all_status(self.grid,self.grid.position_robot)
                            add_status_empty_grid(self.grid,self.start_position_robot)
                           

                    if self.win_menu:
                        if x == -1 and y ==16:
                            
                            if self.count_final != 0:
                                self.grid.begin_path = 0
                                self.win_menu =False
                                is_find = False
                                self.mode_review = True
                                self.grid.actualize_robot_position()
                                clean_all_status(self.grid,self.grid.position_robot)
                                add_status_empty_grid(self.grid,self.start_position_robot)
                                self.grid.display(self.screen)

                            if self.count_final == 0:
                                self.win_menu =False
                                self.is_end =True
        

                    if self.mode_review:
                        if self.count_final == 999:
                            self.mode_review = False
                            self.is_end = True
                        if x == -1 and y == 8:
                            #Left_arrow
                            if self.grid.begin_path - 1 >= 0:
                                self.grid.count_move_ia = self.grid.count_move_ia - 1
                                self.grid.begin_path = self.grid.begin_path - 1
                                self.grid.actualize_robot_position()
                                clean_all_status(self.grid, self.grid.position_robot)
                                add_status_empty_grid(self.grid, self.path[self.grid.begin_path])
                                self.grid.display(self.screen)

                        if x == -1 and y == 10:
                            #Right_Arrow
                            if self.grid.begin_path + 1 <= end_path:
                                self.grid.count_move_ia = self.grid.count_move_ia +1
                                self.grid.begin_path = self.grid.begin_path + 1
                                self.grid.actualize_robot_position()
                                clean_all_status(self.grid, self.grid.position_robot)
                                add_status_empty_grid(self.grid, self.path[self.grid.begin_path])
                                self.grid.display(self.screen)

                        if x == -1 and y == 12:
                            #Check
                            self.grid.count_move_ia = 0
                            self.mode_review = False
                            self.is_end = True
                         

            if self.in_game :
                # is_find = self.grid.win(self.screen)


                self.screen.fill((255, 255, 255))
                self.begin_path = 0 
                self.grid.display(self.screen)
                police = pygame.font.Font(None, 36)
                text = police.render(str(self.grid.count_move), True, (0,0,0))
                self.screen.blit(text, (5,10))

            if self.mode_review:
                self.screen.fill((255, 255, 255))
                self.display_mode_review()
                self.grid.clean_color_grid()
                self.grid.display(self.screen)
                police = pygame.font.Font(None, 36)
                text = police.render(str(self.grid.count_move_ia), True, (0,0,0))
                self.screen.blit(text, (5,10))

            if self.win_menu:
                self.grid.win_display(self.screen)
            if self.is_end :
                self.screen.fill((255, 255, 255))
                self.display_screen_ending()

            
            pygame.display.flip()
            self.clock.tick(30)

    def menu(self):
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    x, y = (y - 40) // 45, (x - 40) // 45
                    print(y,x)
                    
                    if self.in_menu:
                        if 6 <= x <= 7 and 5 <= y <= 10:
                            self.in_menu = False
                            self.in_rules_menu = True
                            self.screen.fill((255, 255, 255))
                        elif 9 <= x <= 10 and 5 <= y <= 10:
                            pygame.quit()
                            sys.exit()
                    
                    if self.in_rules_menu:
                        if y == 16 and x == -1:
                            self.in_rules_menu = False
                            self.in_choice_menu = True
                            self.screen.fill((255, 255, 255))
                        if y == -1 and x == -1:
                            self.in_rules_menu =False
                            self.in_menu = True
                            self.screen.fill((255, 255, 255))

                    if self.in_choice_menu:
                        if 1 <= x <= 4 and 2 <= y <= 14:
                            return 3 
                        if 5 <= x <= 8 and 2 <= y <= 14:
                            return 2
                        if 10 <= x <= 13 and 2 <= y <= 14:
                            return 1
                        if y == -1 and x == -1:
                            self.in_choice_menu = False
                            self.in_rules_menu =True
                            self.screen.fill((255, 255, 255))
    


            if self.in_menu:
                self.display_menu()
            elif self.in_rules_menu:
                self.display_rules_menu()
            elif self.in_choice_menu:
                self.display_choice_menu()


            pygame.display.flip()
            self.clock.tick(30)

