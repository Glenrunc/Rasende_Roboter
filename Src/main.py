from game import *
from a_star import *



if __name__ == "__main__" :
    grid = Grid()
    grid.grid_final()

    print("GOAL" ,grid.color_goal ," : " ,grid.goal_coordinate)
    # grid.color_goal = Color.BLUE
    # grid.goal_coordinate = (2,5)

    path = with_secondary_goal(grid)
    if path != None:
        for state in path:
             print(state)
    else:
        print("path not found")

    # initial_node = Node(grid.position_robot,None)
    # clean_all_status(grid,grid.position_robot)

    # test_fifo = deque()


    # path = BFS(grid,initial_node,grid.color_goal,grid.goal_coordinate)
    # if path != None:
    #     real_path = path[::-1]
    #     for state in real_path:
    #          print(state)


    #game = Game(grid)
    #level = game.menu()
    #game.run(0)

    # # pass