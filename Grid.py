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

    def get_neighbor(current_node: Node):
        neighbors = []
        above = (current_node.x_coordinate, current_node.y_coordinate)
        if(Grid.node_in_grid(above)):
            neighbors

    def node_in_grid(self, x, y):
        if(x < 0 or x > self.x_size):
            return False
        if(y < 0 or y > self.y_size):
            return False

        

