from Node import Node
import math

class Grid:
    def __init__(self, x_size: int, y_size: int):
        self.x_size = x_size
        self.y_size = y_size
        self.terrain = []
        for outside_array in range(y_size):
            temp = []
            for inner_array in range(x_size):
                temp.append(Node(inner_array, outside_array))
            self.terrain.append(temp)

    # TODO: Finish this method lol
    def get_neighbor(current_node: Node):
        neighbors = []
        above = (current_node.x_coordinate, current_node.y_coordinate)
        if(Grid.node_in_grid(above)):
            neighbors

    def node_in_grid(self, x: int, y: int) -> bool:
        if(x < 0 or x > self.x_size):
            return False
        if(y < 0 or y > self.y_size):
            return False

    # Heuristic Function
    def straight_line_distance(self, x1: int, y1: int, x2: int, y2: int) -> float:
        deltaX = x2 - x1
        deltaY = y2 - y1
        diagonal_counter = min(abs(deltaX), abs(deltaY))
        straight_counter = max(abs(deltaX), abs(deltaY)) - diagonal_counter
        total_distance = straight_counter + (math.sqrt(2) * diagonal_counter)
        return total_distance
