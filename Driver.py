import sys

from AStar import AStar
from Grid import Grid
from NodeGrid import load_map as load_map_gui, trace
from NodeGrid import run_app
from PathfindingAlgorithm import PathfindingAlgorithm
from ThetaStar import ThetaStar

# This file runs the pathfinding algorithm
# To run pathfinding on a map file "file.txt", use the command:
# `$ python Driver.py [-theta | -a] "file.txt"` to run either Theta* or A* on that file
# If no "-" flag is given, the program defaults to A*
if __name__ == "__main__":
    run_astar = True
    filename = ""
    algorithm: PathfindingAlgorithm
    if sys.argv[1].startswith("-theta"):
        run_astar = False
        filename = sys.argv[2]
    elif sys.argv[1].startswith("-a"):
        filename = sys.argv[2]
    else:
        filename = sys.argv[1]
    grid = Grid(filename)
    app, gui_grid = load_map_gui(filename)
    if run_astar:
        algorithm = AStar(grid)
    else:
        algorithm = ThetaStar(grid)
    algorithm.run_algorithm()
    gui_grid.bind_grid(grid)
    trace(grid, gui_grid)
    run_app(app)
