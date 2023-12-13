from grid import *
from bfs_dfs import  *

    
class Game:
    
    def __init__(self,grid:Grid):
        
        pygame.init()
        self.screen = pygame.display.set_mode((HEIGHT,WIDTH))
        pygame.display.set_caption("Rasende Roboter")
        self.clock = pygame.time.Clock()
        self.screen.fill((255,255,255))
        self.in_menu = True
        self.in_rules_menu = False
        self.in_choice_menu = False
        self.grid = grid  
        self.grid.grid_final()
        self.start_position_robot = self.grid.position_robot
        clean_all_status(self.grid,self.start_position_robot)
        self.grid.initHeur(self.start_position_robot)
        
     
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

    def run(self,difficulty):
        self.screen.fill((255, 255, 255))

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

            self.grid.display(self.screen)
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

