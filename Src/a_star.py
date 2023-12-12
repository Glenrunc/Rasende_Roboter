from grid import *
from game import *
from collections import deque
from player_mission import Color
import random

def get_possible_coordinates_for_robot(self, target_robot):
    possible_coordinates = []
    for robot, moves in self.possible_move_per_robot.items():
        if robot == target_robot:
            for move in moves:
                possible_coordinates.append(list(move.values())[0])
    return possible_coordinates  

def heuristic(grid, a, b):
    heuristic = (abs(a[0] - b[0]) + abs(a[1] - b[1]))+5*grid.getHeur(a)
    # heuristic = (abs(a[0] - b[0]) + abs(a[1] - b[1]))
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
    for i in possible_move:
        print("move possible: ", i)
        possible_next = grid.possible_move_goal(i)
        print("move possible next: ", possible_next)
        

        #if((grid[g[0],g[1]].wall[3] == True) & (grid[g[0],g[1]-1].wall[3] == True)):
         #   print("mur gauche droite")

        #if((grid[g[0],g[1]].wall[1] == True) & (grid[g[0],g[1]+1].wall[3] == True)):
            #print("mur haut bas")
        for j in possible_next:
            if (j != grid.goal_coordinate and j != i):
                if (i[0]==j[0]):
                    diff = i[1]-j[1]
                    print("diff: ", diff)
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
                    print("diff: ", diff)
                    if (abs(diff) < defaut):
                        objectif_secondaire.clear()
                        defaut = abs(diff)
                        for k in range(abs(diff)):
                            if (diff>0):
                                k=-k
                            temp = (i[0]-diff+k,i[1])
                            objectif_secondaire.append(temp)
    print("OBJECTIF SECONDAIRE : ", objectif_secondaire)
    color_used = [Color.EMPTY]
    for o in objectif_secondaire:
        available_colors = [c for c in Color if c != grid.color_goal and c not in color_used]
        color = random.choice(available_colors)
        color_used.append(color)
        print("Couleur objectif secondaire : ",color)
        states_s = a_star_search(grid, grid.position_robot[color], color, o)
        if states_s != None:
            for state in states_s:
                list_state.append(state)
        else:
            print("Objectif secondaire impossible !")
            return None
    print("OBJECTIF PRINCIPAL : ")
    states_p = a_star_search(grid, grid.position_robot[grid.color_goal], grid.color_goal, grid.goal_coordinate) 
    if states_p != None:
        for state in states_p:
            list_state.append(state)
        return list_state
    else:
        print("Objectif principal impossible !")
        return None
    

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
            print("Too many iterations, exiting...")
            return None
        #print("Etat : ",etat)
        grid.possible_move()
        get_possible_coordinates_for_robot(grid, color)
        for voisin in get_possible_coordinates_for_robot(grid, color):
            add_to_open(grid, Open, voisin, goal)
            #print(Open)
        
        for i in Open:
            if i not in Closed and i in get_possible_coordinates_for_robot(grid, color):
                grid.move(etat[0],etat[1])
                grid.move(i[0],i[1])
                Closed.append(etat)
                list_state.append(grid.position_robot)

                etat = i
                # print("Etat : ",etat)
                break
        
        iterations += 1
      
    print("Objectif : ",goal)
    list_state.append(grid.position_robot)
    return list_state

        