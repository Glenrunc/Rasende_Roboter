from game import *
from bfs import *



if __name__ == "__main__" :
    # game = Game()
    # game.run()


    grid = Grid()
    grid.grid_final()
    grid.possible_move()
    # print(grid.possible_move_per_robot)
    initial_node = Node(grid.position_robot,None)
    test_fifo = deque()
    # print(grid.possible_move_per_robot)
    clean_all_status(grid,grid.position_robot)
    grid.actualize_robot_position()
    path = BFS(grid,initial_node,grid.color_goal,grid.goal_coordinate)
    if path != None:
        real_path = path[::-1]
        for state in real_path:
            print(state)

    # # pass