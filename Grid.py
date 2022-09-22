from Node import Node

class Grid:
    def __init__(self, x_size, y_size):
        self.x_size = x_size
        self.y_size = y_size
        self.terrain = []
        for outside_array in range(y_size):
            temp = []
            for inner_array in range(x_size):
                temp.append(Node(inner_array, outside_array))
            self.terrain.append(temp)

        

