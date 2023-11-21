from grid import *
   
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
        
        # print(self.grid.position_robot)
        # self.grid.possible_move()
        # self.grid.get_position(Color.BLUE,'DOWN')
        # print(self.grid.possible_move_per_robot)


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

