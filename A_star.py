from json.encoder import INFINITY
from Grid import Grid
from Node import Node
from queue import PriorityQueue


class A_star:
    def __init__(self, grid: Grid):
        self.grid = grid
        self.fringe = PriorityQueue()
        self.closed_set = {}

    def run_algorithm(self):
        start_node = self.grid.start_node

        start_node.change_g_value(0)
        start_node.change_parent(start_node)
        self.fringe.put(start_node)

        while not self.fringe.empty:
            # .get will pop it
            s = self.fringe.get()
            if self.grid.is_goal_node(s):
                return "path found"
            self.add_to_closed_set(s)
            for s in Grid.get_adjacency_list(s):
                if not self.is_in_closed_set(s):
                    if s not in self.fringe:
                        s.g_value = INFINITY
                        s.parent = None
                    self.update_vertex()
        return "not path found"

    def update_vertex(self, parent: Node, child: Node):
        straight_line_distance = self.grid.straight_line_distance_tup((parent.x_coordinate, parent.y_coordinate), (child.x_coordinate, child.y_coordinate))
        if parent.g_value + straight_line_distance < child.g_value():
            child.g_value = parent.g_value + straight_line_distance
            child.parent = parent
            if child in self.fringe:
                self.fringe.remove(child)
            self.fringe.insert(child)

    def add_to_closed_set(self, node):
        self.closed_set[(node.x_coordinate, node.y_coordinate)] = node

    def is_in_closed_set(self, node: Node) -> bool:
        return (node.x_coordinate, node.y_coordinate) in self.closed_set
