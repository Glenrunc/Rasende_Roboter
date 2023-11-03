from grid import *
    
class Game:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Rasende Roboter")
        self.clock = pygame.time.Clock()

        self.grid = Grid()  
        self.grid.grid_final()

    def run(self):
    
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if(pygame.mouse.get_pressed()[0]):
                 (mx,my) = pygame.mouse.get_pos()
                 print(mx//50,my//50)
            
            self.grid.display(self.screen)
            pygame.display.flip()
            self.clock.tick(60)



