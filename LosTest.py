from LineOfSight import los
from NodeGrid import *


def loadMap(mapFile):
    with open(mapFile) as f:
        starty, startx = list(map(int, f.readline().strip().split()))
        endy, endx = list(map(int, f.readline().strip().split()))
        cols, rows = list(map(int, f.readline().strip().split()))

        obstacles = []

        app = Tk()

        grid = GuiGrid(app, rows, cols, 20, 8)
        grid.pack(pady=10, padx=10)

        grid.set_start(3, 1)
        grid.set_end(3, 3)

        lines = f.readlines()
        for line in lines:
            col, row, val = list(map(int, line.strip().split()))
            if val == 1:
                grid.fill_obstacle(row - 1, col - 1)
                obstacles.append((row, col))

    print(los((1, 3), (3, 3), obstacles))
    app.mainloop()
            
            
if __name__ == "__main__" :
    loadMap("map1.txt")
