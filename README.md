# Rasende Roboter (Ricochet Robots) Solver

A Python implementation of the board game *Rasende Roboter*, built with Pygame. This project features a playable game and multiple pathfinding algorithms (BFS, DFS, A*) to automatically find the shortest solution.
## Features

-   **Full Game Engine**: Complete game logic built from scratch.
-   **Graphical Interface**: A visual and interactive board powered by Pygame.
-   **Automated Solvers**: Watch different algorithms solve the puzzles in real-time.

## Algorithms Implemented

You can choose between three classic pathfinding algorithms:

1.  **Breadth-First Search (BFS)**: Explores the puzzle layer by layer. **Guaranteed to find the shortest path.**
2.  **Depth-First Search (DFS)**: Explores as far as possible down one path before backtracking. It's fast but doesn't guarantee the shortest solution.
3.  **A\* Search**: A smarter search algorithm that uses the Manhattan distance as a heuristic to find the shortest path more efficiently than BFS.

## Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/Glenrunc/Rasende_Roboter.git
    cd Rasende_Roboter
    ```

2.  **Install the required libraries:**
    ```sh
    pip install pygame numpy
    ```

## Usage

You can run the game from the command line. You can specify which level to load and which algorithm to use.

```sh
# General syntax
python main.py --level [level_number] --algo [BFS|DFS|A*]
