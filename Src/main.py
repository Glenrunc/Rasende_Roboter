from game import *
from bfs import *



if __name__ == "__main__" :
    game = Game()
    game.run()


    grid = Grid()
    grid.grid_final()

    initial_node = Node(grid.position_robot,None)
    clean_all_status(grid,grid.position_robot)

    test_fifo = deque()
    path = BFS(grid,initial_node,grid.color_goal,grid.goal_coordinate)
    if path != None:
        real_path = path[::-1]
        for state in real_path:
             print(state)

    # # pass