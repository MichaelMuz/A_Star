from Node import Node
import math


class Grid:

    # Takes map and saves dimensions, start node, end node, and list of obstacles
    def __init__(self, map_file: str):
        with open(map_file) as f:
            start_col, start_row = list(map(int, f.readline().strip().split()))
            end_col, end_row = list(map(int, f.readline().strip().split()))

            # Coordinates are given 1-indexed, so we need to scale down to 0-indexed
            start_col = start_col - 1
            start_row = start_row - 1
            end_col = end_col - 1
            end_row = end_row - 1

            # size is given by number of cells across by vertical so need to add one to each bc that many intersections
            cols, rows = list(map(int, f.readline().strip().split()))
            cols = cols + 1
            rows = rows + 1
            self.x_size = cols
            self.y_size = rows

            self.obstacles = []

            lines = f.readlines()
            for line in lines:
                col, row, val = list(map(int, line.strip().split()))
                if val == 1:
                    self.obstacles.append((col - 1, row - 1))
            for x in range(-1, self.x_size + 1):
                self.obstacles.append((x, -1))
                self.obstacles.append((x, self.y_size - 1))
            for y in range(-1, self.y_size + 1):
                self.obstacles.append((-1, y))
                self.obstacles.append((self.x_size - 1, y))

            self.terrain = []
            for column in range(0, self.x_size + 1):
                temp = []
                for row in range(0, self.y_size + 1):
                    h_value = self.straight_line_distance((column, row), (end_col, end_row))
                    temp.append(Node(column, row, h_value))
                self.terrain.append(temp)

            self.goal_node = self.terrain[end_col][end_row]
            self.goal_node.change_h_value(0)
            self.start_node = self.terrain[start_col][start_row]

    # Returns a list of only accessible nodes
    def get_adjacency_list(self, current_node: Node):
        possibilities = self.get_all_neighbors(current_node)
        actual_nodes = []
        for (x, y) in possibilities:
            in_sight = self.line_of_sight((current_node.x_coordinate, current_node.y_coordinate), (x, y))
            if in_sight:
                actual_nodes.append(self.terrain[x][y])
        return actual_nodes

    # Checks if node is the goal
    def is_goal_node(self, node: Node):
        return node.compare_nodes(self.goal_node)

    # Returns up to 8 possible neighbors
    def get_all_neighbors(self, current_node: Node) -> list[tuple[int]]:
        cur_pos = (current_node.x_coordinate, current_node.y_coordinate)
        """
            Basically:
                [(a, b) for a in [-1, 0, 1] for b in [-1, 0, 1] -> Get the cartesian product of [-1, 0, 1] x [-1, 0, 1]
                    This is the complete set of offsets a neighbor can be from some node
                lambda x: tuple([x[i] + cur_pos[i] for i in range(len(x))]) -> for some tuple x, add it to cur_pos (element-wise)
                Combining the above two with `map` creates the list of the coordinates of all neighbors
            Then:
                return [x for x in ... if x != cur_pos and self.node_in_grid_tup(x)] -> "..." is the above calculated set,
                    now we filter out the current position (It is not a neighbor of itself) and positions that are outside
                    the grid
        """
        return [x for x in list(map(lambda x: tuple([int(x[i] + cur_pos[i]) for i in range(len(x))]),
                                    [(a, b) for a in [-1, 0, 1] for b in [-1, 0, 1]])) if
                x != cur_pos and self.node_in_grid_tup(x)]

    # Checks if a node is in the grid
    # Helper function of get_adjacency_list
    def node_in_grid_tup(self, pos: tuple[int, int]) -> bool:
        x, y = pos
        return not (x < 0 or x > self.x_size - 1 or y < 0 or y > self.y_size - 1)

    def line_of_sight_wrapped(self, node1: Node, node2: Node):
        return self.line_of_sight((node1.x_coordinate, node1.y_coordinate), (node2.x_coordinate, node2.y_coordinate))
    
    # Checks if there is line of sight between two nodes
    def line_of_sight(self, p0: tuple[int, int], p1: tuple[int, int]):
        f = 0
        sy = 1
        sx = 1
        x0, y0 = p0
        x1, y1 = p1
        dy = y1 - y0
        dx = x1 - x0

        if dy < 0:
            dy = -dy
            sy = -1

        if dx < 0:
            dx = -dx
            sx = -1

        if dx >= dy:
            while x0 != x1:
                f = f + dy
                if f >= dx:
                    if (int(x0 + ((sx - 1) / 2)), int(y0 + ((sy - 1) / 2))) in self.obstacles:
                        return False
                    y0 = y0 + sy
                    f = f - dx
                if f != 0 and (int(x0 + ((sx - 1) / 2)), int(y0 + ((sy - 1) / 2))) in self.obstacles:
                    return False
                if dy == 0 and (int(x0 + ((sx - 1) / 2)), y0) in self.obstacles and (
                        int(x0 + ((sx - 1) / 2)), y0 - 1) in self.obstacles:
                    return False
                x0 = x0 + sx
        else:
            while y0 != y1:
                f = f + dx
                if f >= dy:
                    if (int(x0 + ((sx - 1) / 2)), int(y0 + ((sy - 1) / 2))) in self.obstacles:
                        return False
                    x0 = x0 + sx
                    f = f - dy
                if f != 0 and (int(x0 + ((sx - 1) / 2)), int(y0 + ((sy - 1) / 2))) in self.obstacles:
                    return False
                if dx == 0 and (x0, int(y0 + ((sy - 1) / 2))) in self.obstacles and (
                        x0 - 1, int(y0 + ((sy - 1) / 2))) in self.obstacles:
                    return False
                y0 = y0 + sy
        return True

    def straight_line_distance_wrapped(self, point1: Node, point2: Node):
        return self.straight_line_distance((point1.x_coordinate, point1.y_coordinate), (point2.x_coordinate, point2.y_coordinate))
    # Does this need to be Euclidean distance for Theta*?
    # Heuristic function
    def straight_line_distance(self, p1: tuple[int, int], p2: tuple[int, int]) -> float:
        x1, y1 = p1
        x2, y2 = p2
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        diagonal_counter = min(dx, dy)
        straight_counter = abs(dx - dy)
        sld = straight_counter + (math.sqrt(2) * diagonal_counter)
        return sld


if __name__ == "__main__":
    grid = Grid("map1.txt")
    print(grid.x_size)
    print(grid.y_size)
    print(grid.get_all_neighbors(Node(1, 3, 0)))
