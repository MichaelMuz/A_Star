import sys

from A_star import A_star
from Grid import Grid
from NodeGrid import load_map as load_map_gui, trace
from NodeGrid import run_app

if __name__ == "__main__" :
    filename = sys.argv[1]
    grid = Grid(filename)
    app, gui_grid = load_map_gui(filename)
    astar = A_star(grid)
    astar.run_algorithm()
    trace(grid, gui_grid)
    run_app(app)
