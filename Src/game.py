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
        # print(self.grid.position_robot)
        # self.grid.get_position(Color.BLUE,'DOWN')
    
    def run(self):
    
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



