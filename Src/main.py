from game import *
from a_star import *



if __name__ == "__main__" :
    grid = Grid()
    game = Game(grid)
    level = game.menu()
    game.run(level)
  