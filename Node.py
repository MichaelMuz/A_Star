from json.encoder import INFINITY


class Node:
    def __init__(self, x_coordinate, y_coordinate, h_value):
        self.g_value = INFINITY
        self.h_value = h_value
        self.parent = None
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def get_f_value(self) -> float:
        return self.h_value + self.g_value

    def change_g_value(self, new_g: float):
        self.g_value = new_g

    def change_h_value(self, new_h: float):
        self.h_value = new_h

    def change_parent(self, new_parent: 'Node'):
        self.parent = new_parent

    # This overrides the "<" operator which priority queue uses to compare
    def __lt__(self, other_node: 'Node') -> bool:
        return self.get_f_value() < other_node.get_f_value()

    def print(self):
        return \
f"""
{self.x_coordinate, self.y_coordinate}
h = {self.h_value}
g = {self.g_value}
f = {self.get_f_value()}"""


    def compare_nodes(self, other_node: 'Node') -> bool:
        return self.x_coordinate == other_node.x_coordinate and self.y_coordinate == other_node.y_coordinate
