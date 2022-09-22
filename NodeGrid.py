from tkinter import *
from LineOfSight import *

class Node():
    SELECTED_COLOR = "cyan"
    EMPTY_COLOR = "black"
    START_COLOR = "green"
    END_COLOR = "red"
    NODE_SIZE_MOD = 0.4

    def __init__(self, master, x, y, size, padding):
        self.master = master
        self.abs = x
        self.ord = y
        self.size = size
        self.padding = padding
        self.selected = False
        self.start = False
        self.end = False

    def _toggle(self):
        self.selected = not self.selected

    def _setStart(self):
        self.start = True

    def _setGoal(self):
        self.end = True

    def screenCoord(self):
        x0 = (self.abs * self.size) - Node.NODE_SIZE_MOD* self.size /2 + self.padding
        x1 = x0 + self.size * Node.NODE_SIZE_MOD
        y0 = (self.ord * self.size) - Node.NODE_SIZE_MOD* self.size /2 + self.padding
        y1 = y0 + self.size * Node.NODE_SIZE_MOD
        return x0,y0,x1,y1

    def draw(self):
        if self.master != None:
            bcol = "black"
            if self.end:
                col = Node.END_COLOR
                if self.selected:
                    bcol = Node.SELECTED_COLOR
            elif self.start:
                col = Node.START_COLOR
                if self.selected:
                    bcol = Node.SELECTED_COLOR
            elif self.selected:
                col = Node.SELECTED_COLOR
            else:
                col = Node.EMPTY_COLOR
                
            x0,y0,x1,y1 = self.screenCoord()

            self.master.create_oval(x0, y0, x1, y1, fill = col, outline = bcol)


class Obstacle():
    FILLED_COLOR = "black"
    EMPTY_COLOR = "white"
    BORDER_COLOR = "black"

    def __init__(self, master, x, y, size, padding):
        self.master = master
        self.abs = x
        self.ord = y
        self.size = size
        self.padding = padding
        self.filled = False

    def draw(self):
        if self.master != None:
            col = Obstacle.FILLED_COLOR
            if not self.filled:
                col = Obstacle.EMPTY_COLOR

            x0 = self.abs * self.size + self.padding
            x1 = x0 + self.size
            y0 = self.ord * self.size + self.padding
            y1 = y0 + self.size

            self.master.create_rectangle(x0, y0, x1, y1, outline = Obstacle.BORDER_COLOR, fill = col)
            if not self.filled:
                self.master.create_line(x0, y0, x1, y1)
                self.master.create_line(x0, y1, x1, y0)

class PathSegment():
    LINE_COLOR = "magenta"

    def __init__(self, master, p0, p1, size, padding):
        self.master = master
        self.abs, self.ord = p0
        self.abs2, self.ord2 = p1
        self.size = size
        self.padding = padding
        self.filled = False

    def screenCoord(self):
        x0 = (self.abs * self.size) + self.padding
        x1 = (self.abs2 * self.size) + self.padding
        y0 = (self.ord * self.size) + self.padding
        y1 = (self.ord2 * self.size) + self.padding
        return x0,y0,x1,y1

    def draw(self):
        if self.master != None:
            x0,y0,x1,y1 = self.screenCoord()
            self.master.create_line(x0,y0,x1,y1, fill = PathSegment.LINE_COLOR, tags = ("pathsegment"))
            

class Grid(Canvas):
    def __init__(self,master, rowNumber, columnNumber, cellSize, padding, *args, **kwargs):
        Canvas.__init__(self, master, width = cellSize * columnNumber + padding * 2, height = cellSize * rowNumber + padding * 2, *args, **kwargs)

        self.cellSize = cellSize
        self.padding = padding

        self.nodes = []
        for row in range(rowNumber + 1):
            line = []
            for column in range(columnNumber + 1):
                line.append(Node(self, column, row, cellSize, padding))

            self.nodes.append(line)

        self.obstacles = []
        self.paths = []
        self.robs = []
        for row in range(rowNumber):
            line = []
            for column in range(columnNumber):
                line.append(Obstacle(self, column, row, cellSize, padding))

            self.obstacles.append(line)
            
        self.bind("<Button-1>", self.handleMouseClick)

        self.draw()
        self.selected = None
        self.start = None
        self.end = None

    def draw(self):
        for row in self.obstacles:
            for cell in row:
                cell.draw()
        
        for row in self.nodes:
            for cell in row:
                cell.draw()

    def _eventCoords(self, event):
        row = int((event.y  + self.cellSize / 2 - self.padding) / self.cellSize)
        column = int((event.x + self.cellSize / 2 - self.padding) / self.cellSize)
        return row, column

    def handleMouseClick(self, event):
        row, col = self._eventCoords(event)
        cell = self.nodes[row][col]
        if self.selected != None:
            self.selected._toggle()
            self.selected.draw()
        self.selected = cell
        self.selected._toggle()
        self.selected.draw()

    def fillObstacle(self, row, col):
        self.obstacles[row][col].filled = True
        self.obstacles[row][col].draw()
        self.robs.append((row,col))

    def clearObstacle(self, row, col):
        self.obstacles[row][col].filled = False
        self.obstacles[row][col].draw()
        self.robs.remove((row,col))

    def setStart(self, row, col):
        if self.start != None:
            self.start.start = False
            self.nodes[row][col].draw()
        self.nodes[row][col].start = True
        self.nodes[row][col].draw()
        self.start = self.nodes[row][col]
        
    def setEnd(self, row, col):
        if self.end != None:
            self.end.end = False
            self.nodes[row][col].draw()
        self.nodes[row][col].end = True
        self.nodes[row][col].draw()
        self.end = self.nodes[row][col]

    def addPath(self, p0, p1):
        path = PathSegment(self, p0, p1, self.cellSize, self.padding)
        self.paths.append(path)
        path.draw()
        

    def removePath(self, p0, p1):
        self.paths = [x for x in self.paths if x.p0 != p0 and x.p1 != p1]
        
    

def loadMap(mapFile):
        with open(mapFile) as f:
            starty,startx = list(map(int, f.readline().strip().split()))
            endy,endx = list(map(int, f.readline().strip().split()))
            cols,rows = list(map(int, f.readline().strip().split()))

            app = Tk()

            

            grid = Grid(app, rows, cols, 20, 8, )
            grid.pack(pady=10, padx=10)

            grid.setStart(startx - 1, starty - 1)
            grid.setEnd(endx - 1, endy - 1)

            lines = f.readlines()
            for line in lines:
                col,row,val = list(map(int, line.strip().split()))
                if val == 1:
                    grid.fillObstacle(row - 1, col - 1)
                    
            app.mainloop()
            
            
if __name__ == "__main__" :
    loadMap("map1.txt")
    #app = Tk()

    #grid = Grid(app, 50, 100, 20, 8)
    #grid.pack(pady=10, padx=10)

    #app.mainloop()
