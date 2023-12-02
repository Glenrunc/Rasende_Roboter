from grid import *
import numpy as np
from collections import deque #Usefull for FIFO in BFS

class Node:

    def __init__(self,_state:dict,_father_node):

        #state -> Will be representing by a list of the position of the robot
        #father_node-> Will be the father node
        self.state = _state
        self.father_node = _father_node

def BFS(empty_grid:Grid, initial_node_state:Node,color_mission:Color,coordinate_mission:tuple):
    fifo_state = deque()
    visited_state = deque()
    #empty_grid.initHeur()
    #empty_grid.printHeur()
    empty_grid.add_status(Color.RED, 0, 1)
    empty_grid.add_status(Color.BLUE, 2, 1)
    empty_grid.add_status(Color.YELLOW, 4, 7)
    empty_grid.add_status(Color.GREEN, 5, 12)
    empty_grid.actualize_robot_position()
    fifo_state.append(initial_node_state)
    temp_coordinate = initial_node_state.state[color_mission]
    start_time = time.time()
    
    while (len(fifo_state) != 0 and temp_coordinate != coordinate_mission):

        #print("processing...............................")
        process_node = fifo_state.popleft()
        visited_state.append(process_node.state)
        temp_coordinate = process_node.state[color_mission]

        if temp_coordinate == coordinate_mission:
            print("We have found a path")
            print(process_node.state)
            print('\n')
            print(color_mission)
            print('\n')
            print(coordinate_mission)
            path = find_final_path(process_node)
            return path
    
        next_state(process_node,empty_grid,fifo_state,visited_state)
    if len(fifo_state) != 0:
        return None
    end_time = time.time()  
    elapsed_time = end_time - start_time
    print(f"Time elapsed: {elapsed_time} seconds")



def add_status_empty_grid(grid:Grid,status:dict):
    for color in status:
        grid.add_status(color,status[color][0],status[color][1])
        


def clean_all_status(grid:Grid,status:dict):
    for color in status:
        grid.clean_status(status[color][0],status[color][1])
        
    grid.actualize_robot_position()


def is_already_visited(status,visited_state:deque,color:Color):
    for state in visited_state:
        if state[color] == status[color]:
            return True
    return False
    
    
def next_state(node_state:Node,empty_grid:Grid,fifo_state:deque,visited_state:deque):
    
    add_status_empty_grid(empty_grid,node_state.state)

    empty_grid.possible_move()
    for color,moves in empty_grid.possible_move_per_robot.items():
        # print(color)
        for move in moves:
            # print(list(move.values())[0])
            coordinates = list(move.values())[0]
            status_temp = dict(node_state.state)  
            status_temp[color] = coordinates
            if not is_already_visited(status_temp,visited_state,color):
                temp_node = Node(status_temp, node_state)
                fifo_state.append(temp_node)

    clean_all_status(empty_grid,node_state.state)


def find_final_path(final_node:Node):

    list_state = []
    list_state.append(final_node.state)
    father_node = final_node.father_node
    while father_node != None:
        list_state.append(father_node.state)
        father_node = father_node.father_node    

    return list_state


