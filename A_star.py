from Grid import Grid
from Node import Node
from queue import PriorityQueue

class A_star:
    def __init__(self, grid):
        self.grid = grid
        self.fringe = PriorityQueue()
    
    def run_algorithm(self, start_node: Node, end_node: Node):
        start_node.change_g_value(0)
        start_node.change_parent(start_node)
        self.fringe.put(start_node)
        

        

    