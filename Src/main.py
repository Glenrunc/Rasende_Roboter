from game import *
from a_star import *



if __name__ == "__main__" :
    # game = Game()
    # game.run()


    grid = Grid()
    grid.grid_final()

    print("GOAL : ")
    print(grid.color_goal)
    print(grid.goal_coordinate)

    # grid.color_goal = Color.YELLOW 
    # grid.goal_coordinate = (9,4)

    # grid.color_goal = Color.BLUE 
    # grid.goal_coordinate = (10,6)

    initial_node = Node(grid.position_robot,None)
    clean_all_status(grid,grid.position_robot)
    grid.initHeur(initial_node.state)
    grid.printHeur()
    # grid.getHeur(initial_node.state)
    add_status_empty_grid(grid,initial_node.state)

    path = with_secondary_goal(grid)
    if path != None:
        for state in path:
             print(state)

    # initial_node = Node(grid.position_robot,None)
    # clean_all_status(grid,grid.position_robot)

    # test_fifo = deque()


    # path = BFS(grid,initial_node,grid.color_goal,grid.goal_coordinate)
    # if path != None:
    #     real_path = path[::-1]
    #     for state in real_path:
    #          print(state)

    # # pass