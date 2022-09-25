from Node import Node
import math


class Grid:
    # def __init__(self, x_size, y_size):
    #    self.x_size = x_size
    #    self.y_size = y_size
    #    self.terrain = []
    #    for outside_array in range(y_size):
    #        temp = []
    #        for inner_array in range(x_size):
    #            temp.append(Node(inner_array, outside_array))
    #        self.terrain.append(temp)
    def __init__(self, map_file: str):
        with open(map_file) as f:
            end_col, end_row = list(map(int, f.readline().strip().split()))
            cols, rows = list(map(int, f.readline().strip().split()))
            self.x_size = cols
            self.y_size = rows
            self.end_row = end_row
            self.end_col = end_col

            # get obstacles
            self.obstacles = []

            lines = f.readlines()
            for line in lines:
                col, row, val = list(map(int, line.strip().split()))
                if val == 1:
                    self.obstacles.append((row, col))

            # generate 2D array
            self.terrain = []
            for outside_array in range(self.y_size):
                temp = []
                for inner_array in range(self.x_size):
                    h_value = Grid.straight_line_distance(inner_array, outside_array, self.end_col, self.end_col)
                    temp.append(Node(inner_array, outside_array, h_value))
                    self.terrain.append(temp)

    # TODO: Finish this method lol
    # be sure that all nodes returned have a prepopulated h value
    # grid.py figure out endx and endy to straightline distance function
    # this function should be called by a get_all_neighbors_I_can_actually_visit function
    def get_all_neighbors(self, current_node: Node) -> list[tuple[int]]:
        curPos = (current_node.x_coordinate, current_node.y_coordinate)
        """
            Basically:
                [(a, b) for a in [-1, 0, 1] for b in [-1, 0, 1] -> Get the cartesian product of [-1, 0, 1] x [-1, 0, 1]
                    This is the complete set of offsets a neighbor can be from some node
                lambda x: tuple([x[i] + curPos[i] for i in range(len(x))]) -> for some tuple x, add it to curPos (element-wise)
                Combining the above two with `map` creates the list of the coordinates of all neighbors
            Then:
                return [x for x in ... if x != curPos and self.node_in_grid_tup(x)] -> "..." is the above calculated set,
                    now we filter out the current position (It is not a neighbor of itself) and positions that are outside
                    the grid
        """
        return [x for x in list(map(lambda x: tuple([int(x[i] + curPos[i]) for i in range(len(x))]), [(a, b) for a in [-1, 0, 1] for b in [-1, 0, 1]])) if x != curPos and self.node_in_grid_tup(x)]

        """
        neighbors = []
        
        above = (current_node.x_coordinate, current_node.y_coordinate - 1)
        if(Grid.node_in_grid(above)):
            neighbors.append(above)

        top_right_diagonal = (current_node.x_coordinate + 1, current_node.y_coordinate - 1)
        if(Grid.node_in_grid(top_right_diagonal)):
            neighbors.append(top_right_diagonal)

        right = (current_node.x_coordinate + 1, current_node.y_coordinate)
        if(Grid.node_in_grid(right)):
            neighbors.append(right)
        
        bottom_right_diagonal = (current_node.x_coordinate + 1, current_node.y_coordinate + 1)
        if(Grid.node_in_grid(bottom_right_diagonal)):
            neighbors.append(bottom_right_diagonal)
        
        down = (current_node.x_coordinate, current_node.y_coordinate + 1)
        if(Grid.node_in_grid(down)):
            neighbors.append(down)
        
        bottom_left_diagonal = (current_node.x_coordinate - 1, current_node.y_coordinate + 1)
        if(Grid.node_in_grid(bottom_left_diagonal)):
            neighbors.append(bottom_left_diagonal)
        
        left = (current_node.x_coordinate - 1, current_node.y_coordinate)
        if(Grid.node_in_grid(left)):
            neighbors.append(left)
        
        top_left_diagonal = (current_node.x_coordinate - 1, current_node.y_coordinate - 1)
        if(Grid.node_in_grid(top_left_diagonal)):
            neighbors.append(top_left_diagonal)
        
        return neighbors
        """

    def node_in_grid_tup(self, pos: tuple[int, int]) -> bool:
        x, y = pos
        return not (x < 0 or x > self.x_size or y < 0 or y > self.y_size)

    # Does this need to be Euclidean distance for Theta*?
    def straight_line_distance_tup(self, p1: tuple[int, int], p2: tuple[int, int]) -> float:
        x1, y1 = p1
        x2, y2 = p2
        dx = abs(x2 - x1)
        dy = abs(x2 - x1)
        diagonal_counter = min(dx, dy)
        straight_counter = abs(dx - dy)
        return straight_counter + (math.sqrt(2) * diagonal_counter)


    def node_in_grid(self, x: int, y: int) -> bool:
        return not (x < 0 or x > self.x_size or y < 0 or y > self.y_size)

    # Heuristic Function
    def straight_line_distance(x1: int, y1: int, x2: int, y2: int) -> float:
        deltaX = x2 - x1
        deltaY = y2 - y1
        diagonal_counter = min(abs(deltaX), abs(deltaY))
        straight_counter = max(abs(deltaX), abs(deltaY)) - diagonal_counter
        total_distance = straight_counter + (math.sqrt(2) * diagonal_counter)
        return total_distance


if __name__ == "__main__":
    grid = Grid("map1.txt")
    print(grid.get_all_neighbors(Node(0, 2, 0)))
