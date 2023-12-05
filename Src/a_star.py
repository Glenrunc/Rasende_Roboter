from grid import *
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


def test(grid):
    possible_move = grid.possible_move_goal(grid.goal_coordinate)
    defaut = 4
    objectif_secondaire = []
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
                    if abs(diff) < defaut:
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
                    if abs(diff) < defaut:
                        objectif_secondaire.clear()
                        defaut = abs(diff)
                        for k in range(abs(diff)):
                            if (diff>0):
                                k=-k
                            temp = (i[0]-diff+k,i[1])
                            objectif_secondaire.append(temp)
    print("OCJECTIF SECONDAIRE : ", objectif_secondaire)
    color_used = [Color.EMPTY]
    for o in objectif_secondaire:
        available_colors = [c for c in Color if c != grid.color_goal and c not in color_used]
        color = random.choice(available_colors)
        color_used.append(color)
        print("Couleur objectif secondaire : ",color)
        a_star_search(grid, grid.position_robot[color], color, o)
    print("Objectif principal !")
    a_star_search(grid, grid.position_robot[grid.color_goal], grid.color_goal, grid.goal_coordinate)

        
    

def a_star_search(grid, start, color, goal):
    Open = []
    Closed = []
    etat = start
    add_to_open(Open, etat, goal)
    iterations = 0

    while etat != goal:
        if iterations > 1000:
            print("Too many iterations, exiting...")
            break
        #print("Etat : ",etat)
        grid.possible_move()
        get_possible_coordinates_for_robot(grid, color)
        for voisin in get_possible_coordinates_for_robot(grid, color):
            add_to_open(Open, voisin, goal)
            #print(Open)
        
        
        for i in Open:
            if i not in Closed and i in get_possible_coordinates_for_robot(grid, color):
                grid.move(etat[0],etat[1])
                grid.move(i[0],i[1])
                Closed.append(etat)
                etat = i
                print("Etat : ",etat)
                break
        
        iterations += 1

    print(Closed)
    print("Vous avez gagné ! nombre de coups :", len(Closed))


def iaSolution(grid, color, goal):
    closed=[]
    open=[]
    open.append(grid)
    compteur=0
    while (open.count!=0 and compteur<3000):
        u=open[0]
        #print("je recommence avec ",u)
        del open[0]
        if (grid.position_robot[color]==goal):
            print("Jeu terminé avec succès")
            return closed
        else:
            #On génère les états qui peuvent être générés par u
            children=[]

            bleu=u[0]
            jaune=u[1]
            vert=u[2]
            rouge=u[3]
            #poids=u[4]+1
            grid.possible_move()
            #display_plateau(plateau)

            for states in get_possible_coordinates_for_robot(grid,Color.BLUE):
                grid_temp=grid
                grid_temp.move(grid_temp.position_robot[Color.BLUE][0],grid_temp.position_robot[Color.BLUE][1])
                grid_temp.move(states[0],states[1])
                children.append(grid_temp)
            for states in get_possible_coordinates_for_robot(grid, Color.YELLOW):
                grid_temp=grid
                grid_temp.move(grid_temp.position_robot[Color.YELLOW][0],grid_temp.position_robot[Color.YELLOW][1])
                grid_temp.move(states[0],states[1])
                children.append(grid_temp)
            for states in get_possible_coordinates_for_robot(grid, Color.RED):
                grid_temp=grid
                grid_temp.move(grid_temp.position_robot[Color.RED][0],grid_temp.position_robot[Color.RED][1])
                grid_temp.move(states[0],states[1])
                children.append(grid_temp)
            for states in get_possible_coordinates_for_robot(Color.GREEN):
                grid_temp=grid
                grid_temp.move(grid_temp.position_robot[Color.GREEN][0],grid_temp.position_robot[Color.GREEN][1])
                grid_temp.move(states[0],states[1])
                children.append(grid_temp)
            #Pour chaque child possible on vérifie s'il est dans les listes
            for child in children:
                if(child not in open and child not in closed):                         ##penser à ajouter qu'il n'existe pas avec un coût inférieur
                    open.append(child)
            closed.append(u)
            compteur+=1
    return 0
        