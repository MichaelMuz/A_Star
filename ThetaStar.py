from queue import PriorityQueue
from json.encoder import INFINITY
from Node import Node
from PathfindingAlgorithm import PathfindingAlgorithm


class ThetaStar(PathfindingAlgorithm):
    def __init__(self, grid):
        self.grid = grid
        self.fringe = PriorityQueue()
        self.closed_set = {}

    def run_algorithm(self):
        start_node = self.grid.start_node

        start_node.change_g_value(0)
        start_node.change_parent(start_node)
        self.fringe.put(start_node)

        while not self.fringe.qsize() == 0:
            # .get will pop it
            s = self.fringe.get()
            if self.grid.is_goal_node(s):
                return "path found"
            self.add_to_closed_set(s)
            for s_prime in self.grid.get_adjacency_list(s):
                if not self.is_in_closed_set(s_prime):
                    if s_prime not in self.fringe.queue:
                        s_prime.change_g_value(INFINITY)
                        s_prime.change_parent(None)
                    self.update_vertex(s, s_prime)
        return "not path found"

    def update_vertex(self, parent: Node, child: Node):
        if self.grid.line_of_sight_wrapped(parent.parent, child):
            straight_line_distance = self.grid.straight_line_distance_wrapped(child, parent.parent)
            if parent.parent.g_value + straight_line_distance < child.g_value:
                child.change_g_value(parent.parent.g_value + straight_line_distance)
                child.change_parent(parent.parent)
                if child in self.fringe.queue:
                    self.fringe.queue.remove(child)
                self.fringe.put(child)
        else:
            straight_line_distance = self.grid.straight_line_distance(
                (parent.x_coordinate, parent.y_coordinate), (child.x_coordinate, child.y_coordinate))
            if parent.g_value + straight_line_distance < child.g_value:
                child.change_g_value(parent.g_value + straight_line_distance)
                child.change_parent(parent)
                if child in self.fringe.queue:
                    self.fringe.queue.remove(child)
                self.fringe.put(child)

    def add_to_closed_set(self, node):
        self.closed_set[(node.x_coordinate, node.y_coordinate)] = node

    def is_in_closed_set(self, node: Node) -> bool:
        return (node.x_coordinate, node.y_coordinate) in self.closed_set
