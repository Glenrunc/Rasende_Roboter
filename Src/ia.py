from grid import *
from collections import deque
from grid import *
from collections import deque
from queue import PriorityQueue

def get_possible_coordinates_for_robot(self, target_robot):
    possible_coordinates = []
    for robot, moves in self.possible_move_per_robot.items():
        if robot == target_robot:
            for move in moves:
                possible_coordinates.append(list(move.values())[0])
    return possible_coordinates


def BFS(grid,initial_state, final_state):
    file = deque([[initial_state]])
    vu = set([initial_state])
    while file:
        chemin = file.popleft()
        dernier_état = chemin[-1]
        if dernier_état == final_state:
            return chemin
        print("Etat : ",dernier_état)
        grid.possible_move()
        print("Possibilitées :")
        for voisin in get_possible_coordinates_for_robot(grid, Color.RED):
            #robot_position = grid.position_robot[Color.RED]
            #print("Position du robot : ",robot_position)
            #grid.move(robot_position[0],robot_position[1])
            #grid.move(dernier_état[0],dernier_état[1])

            print(voisin)
            if voisin not in vu:
                grid.move(dernier_état[0],dernier_état[1])
                grid.move(voisin[0],voisin[1])
                vu.add(voisin)
                file.append(chemin + [voisin])
                grid.possible_move()
            

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def add_to_open(Open, state, goal):
    state_h = heuristic(state, goal)
    for i in range(len(Open)):
        if state == Open[i]:
            return False
        elif state_h < heuristic(Open[i], goal):
            Open.insert(i, state)
            return True
    Open.append(state)
    return True


def a_star_search(grid, start, goal):
    Open = []
    Closed = []
    etat = start
    add_to_open(Open, etat, goal)
    iterations = 0

    while etat != goal:
        if iterations > 1000:
            print("Too many iterations, exiting...")
            break
        print("Etat : ",etat)
        grid.possible_move()
        get_possible_coordinates_for_robot(grid, Color.RED)
        for voisin in get_possible_coordinates_for_robot(grid, Color.RED):
            add_to_open(Open, voisin, goal)
            print(Open)
        
        
        for i in Open:
            if i not in Closed and i in get_possible_coordinates_for_robot(grid, Color.RED):
                grid.move(etat[0],etat[1])
                grid.move(i[0],i[1])
                Closed.append(etat)
                etat = i
                break
        
        iterations += 1
