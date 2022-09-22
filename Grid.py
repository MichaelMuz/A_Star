from Node import Node

class Grid:
    def __init__(self, x_size, y_size):
        self.x_size = x_size
        self.y_size = y_size
        self.terrain = []
        for _ in range(y_size):
            temp = []
            for __ in range(x_size):
                temp.append(Node())
            self.terrain.append(temp)

        

