from game import *



if __name__ == "__main__" :
    grid = Grid()
    game = Game(grid)
    level = game.menu()
    game.run(0)
    # # pass