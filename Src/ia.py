from grid import *
from collections import deque


def BFS(grid,initial_state, final_state):
    file = deque([[initial_state]])
    vu = set([initial_state])
    while file:
        chemin = file.popleft()
        dernier_état = chemin[-1]
        if dernier_état == final_state:
            return chemin, len(vu)
        print(dernier_état)
        for voisin in grid.move(grid,dernier_état):
            if voisin not in vu:
                vu.add(voisin)
                file.append(chemin + [voisin])