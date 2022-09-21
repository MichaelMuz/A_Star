from tkinter import *
from NodeGrid import *

class Obstacle():
    FILLED_COLOR = "black"
    EMPTY_COLOR = "white"
    BORDER_COLOR = "black"

    def __init__(self, master, x, y, size):
        self.master = master
        self.abs = x
        self.ord = y
        self.size = size
        self.filled = False

    def draw(self):
        if self.master != None:
            col = Obstacle.FILLED_COLOR
            if not self.filled:
                col = Obstacle.EMPTY_COLOR

            x0 = self.abs * self.size
            x1 = x0 + self.size
            y0 = self.ord * self.size
            y1 = y0 + self.size

            self.master.create_rectangle(x0, y0, x1, y1, outline = Obstacle.BORDER_COLOR, fill = col)

class ObstacleGrid(Canvas):
    def __init__(self,master, rowNumber, columnNumber, cellSize, *args, **kwargs):
        Canvas.__init__(self, master, width = cellSize * columnNumber , height = cellSize * rowNumber, *args, **kwargs)

        self.cellSize = cellSize

        self.grid = []
        for row in range(rowNumber):
            line = []
            for column in range(columnNumber):
                line.append(Obstacle(self, column, row, cellSize))

            self.grid.append(line)

        self.draw()

    def draw(self):
        for row in self.grid:
            for cell in row:
                cell.draw()


if __name__ == "__main__" :
    app = Tk()

    grid = ObstacleGrid(app, 50, 100, 20)
    nodes = NodeGrid(app, 50, 100, 20)

    app.mainloop()
