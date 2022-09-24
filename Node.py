class Node:
    def __init__(self, x_coordinate, y_coordinate, h_value):
        self.g_value = 0
        self.h_value = h_value
        self.parent = None
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def get_f_value(self):
        return self.h_value + self.g_value

    def change_g_value(self, new_g):
        self.g_value = new_g

    def change_h_value(self, new_h):
        self.h_value = new_h

    #this overrides the less than operator which priority queue uses to compare
    def __lt__(self, other_node):
        return self.get_f_value() < other_node.get_f_value()
    
    def change_parent(self, parent):
        self.parent = parent
    
    def compare_nodes(self, other_node):
        return (self.x_coordinate == other_node.x_coordinate and self.y_coordinate == other_node.y_coordinate)