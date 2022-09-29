import sys

from AStar import AStar
from Grid import Grid
from NodeGrid import load_map as load_map_gui, trace
from NodeGrid import run_app

if __name__ == "__main__" :
    filename = sys.argv[1]
    grid = Grid(filename)
    app, gui_grid = load_map_gui(filename)
    astar = AStar(grid)
    astar.run_algorithm()
    gui_grid.bind_grid(grid)
    trace(grid, gui_grid)
    run_app(app)
