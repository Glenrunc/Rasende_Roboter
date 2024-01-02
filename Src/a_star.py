from grid import *
from collections import deque
from player_mission import Color
import random
from math import sqrt
from bfs_dfs import *

def get_possible_coordinates_for_robot(self, target_robot):
    possible_coordinates = []
    for robot, moves in self.possible_move_per_robot.items():
        if robot == target_robot:
            for move in moves:
                possible_coordinates.append(list(move.values())[0])
    return possible_coordinates  

def heuristic(grid, a, b):
    heuristic = (abs(a[0] - b[0]) + abs(a[1] - b[1]))+5*grid.getHeur(a)
    #heuristic = sqrt(pow(abs(a[0] - b[0]),2) + pow(abs(a[1] - b[1]),2))
    # heuristic = grid.getHeur(a)
    # print("heuristique : ",heuristic)
    return heuristic

def add_to_open(grid, Open, state, goal):
    state_h = heuristic(grid, state, goal)
    for i in range(len(Open)):
        if state == Open[i]:
            return False
        elif state_h < heuristic(grid, Open[i], goal):
            Open.insert(i, state)
            return True
    Open.append(state)

    return True

def with_secondary_goal(grid):
    possible_move = grid.possible_move_goal(grid.goal_coordinate)
    defaut = 4
    objectif_secondaire = []
    list_state = []
    goal = grid.goal_coordinate

    initial_node = Node(grid.position_robot,None)
    clean_all_status(grid,grid.position_robot)
    grid.initHeur(initial_node.state)
    add_status_empty_grid(grid,initial_node.state)
    states_p = a_star_search(grid, grid.position_robot[grid.color_goal], grid.color_goal, grid.goal_coordinate) 
    if states_p == None:

        if(grid.goal_coordinate[0] == 0 or grid.goal_coordinate[0] == 15 or grid.goal_coordinate[1] == 0 or grid.goal_coordinate[1] == 15):
            for i in possible_move:
                if (i != grid.goal_coordinate):
                    if (grid.goal_coordinate[0]==i[0]):
                        diff = grid.goal_coordinate[1]-i[1]
                        #print("diff: ", diff)
                        if (abs(diff) < defaut):
                            objectif_secondaire.clear()
                            defaut = abs(diff)
                            for k in range(abs(diff)):
                                if (diff>0):
                                    k=-k
                                temp = (grid.goal_coordinate[0],grid.goal_coordinate[1]-diff-k)
                                objectif_secondaire.append(temp)
                    else:
                        diff = grid.goal_coordinate[0]-i[0]
                        #print("diff: ", diff)
                        if (abs(diff) < defaut):
                            objectif_secondaire.clear()
                            defaut = abs(diff)
                            for k in range(abs(diff)):
                                if (diff>0):
                                    k=-k
                                temp = (grid.goal_coordinate[0]-diff+k,grid.goal_coordinate[1])
                                objectif_secondaire.append(temp)

        for i in possible_move:
            #print("move possible: ", i)
            possible_next = grid.possible_move_goal(i)
            #print("move possible next: ", possible_next)
            for j in possible_next:
                if (j != grid.goal_coordinate and j != i):
                    if (i[0]==j[0]):
                        diff = i[1]-j[1]
                        # print("diff: ", diff)
                        if (abs(diff) < defaut):
                            objectif_secondaire.clear()
                            defaut = abs(diff)
                            for k in range(abs(diff)):
                                if (diff>0):
                                    k=-k
                                temp = (i[0],i[1]-diff-k)
                                objectif_secondaire.append(temp)
                    else:
                        diff = i[0]-j[0]
                        #print("diff: ", diff)
                        if (abs(diff) < defaut):
                            objectif_secondaire.clear()
                            defaut = abs(diff)
                            for k in range(abs(diff)):
                                if (diff>0):
                                    k=-k
                                temp = (i[0]-diff+k,i[1])
                                objectif_secondaire.append(temp)
        
        # print("OBJECTIF SECONDAIRE : ", objectif_secondaire)
        color_used = [Color.EMPTY]
        for o in objectif_secondaire:
            available_colors = [c for c in Color if c != grid.color_goal and c not in color_used]
            color = random.choice(available_colors)
            color_used.append(color)
            # print("Couleur objectif secondaire : ",color)
            grid.goal_coordinate = o
            initial_node = Node(grid.position_robot,None)
            clean_all_status(grid,grid.position_robot)
            grid.initHeur(initial_node.state)
            add_status_empty_grid(grid,initial_node.state)

            states_s = a_star_search(grid, grid.position_robot[color], color, o)
            if states_s != None:
                for state in states_s:
                    list_state.append(state)
            else:
                # print("Objectif secondaire impossible !")
                return None
        # print("OBJECTIF PRINCIPAL : ")
        grid.goal_coordinate = goal
        initial_node = Node(grid.position_robot,None)
        clean_all_status(grid,grid.position_robot)
        grid.initHeur(initial_node.state)
        add_status_empty_grid(grid,initial_node.state)
    
        states_p = a_star_search(grid, grid.position_robot[grid.color_goal], grid.color_goal, grid.goal_coordinate) 
        if states_p != None:
            for state in states_p:
                list_state.append(state)
            
            return list_state, len(list_state)-1
        else:
            # print("Objectif principal impossible !")
            
            return None
    else:
        for state in states_p:
            list_state.append(state)
       
        return list_state,len(list_state)-1
    

def a_star_search(grid, start, color, goal):
    Open = []
    Closed = []
    list_state = []
    list_state.append(grid.position_robot)


    etat = start
    add_to_open(grid, Open, etat, goal)
    iterations = 0

    while etat != goal:
        if iterations > 1000:
            # print("Too many iterations, exiting...")
            return None
        grid.possible_move()
        get_possible_coordinates_for_robot(grid, color)
        for voisin in get_possible_coordinates_for_robot(grid, color):
            add_to_open(grid, Open, voisin, goal)
        
        for i in Open:
            if i not in Closed and i in get_possible_coordinates_for_robot(grid, color):
                grid.move(etat[0],etat[1])
                grid.move(i[0],i[1])
                Closed.append(etat)
                list_state.append(grid.position_robot)

                etat = i
                break
        
        iterations += 1
      
    # print("Objectif : ",goal)
    return list_state

        