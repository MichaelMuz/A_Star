from Grid import Grid
from Node import Node
from queue import PriorityQueue

class A_star:
    def __init__(self, grid):
        self.grid = grid
        self.fringe = PriorityQueue()
        self.closed_set = {}
    
    def run_algorithm(self, start_node: Node, goal_node: Node):
        start_node.change_g_value(0)
        start_node.change_parent(start_node)
        self.fringe.put(start_node)

        while(not self.fringe.empty):
            #.get will pop it
            s = self.fringe.get()
            if s.compare_nodes(goal_node):
                return "path found"
            self.add_to_closed_set(s)
            for s in adjacent_nodes(s):
                





    def add_to_closed_set(self, node: Node):
        self.closed_set[(node.x_coordinate, node.y_coordinate)] = node
    

    def is_in_closed_set(self, node: Node):
        return (node.x_coordinate, node.y_coordinate) in self.closed_set

        

        

    