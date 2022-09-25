from LineOfSight import lineOfSight
from Node import Node
import math

class Grid:
    #def __init__(self, x_size, y_size):
    #    self.x_size = x_size
    #    self.y_size = y_size
    #    self.terrain = []
    #    for outside_array in range(y_size):
    #        temp = []
    #        for inner_array in range(x_size):
    #            temp.append(Node(inner_array, outside_array))
    #        self.terrain.append(temp)
    def __init__(self, mapFile):
        with open(mapFile) as f:
            # TODO: i think i flipped the x and y or something? help lmao
            starty,startx = list(map(int, f.readline().strip().split()))
            endy,endx = list(map(int, f.readline().strip().split()))
            cols,rows = list(map(int, f.readline().strip().split()))
            self.x_size = cols
            self.y_size = rows
            
            #get obstacles
            self.obstacles = []

            lines = f.readlines()
            for line in lines:
                col,row,val = list(map(int, line.strip().split()))
                if val == 1:
                    self.obstacles.append((row,col))

            #generate 2D array
            self.terrain = []
            for outside_array in range(self.y_size):
                temp = []
                for inner_array in range(self.x_size):
                    h_value = self.heuristic_generator(inner_array, outside_array)
                    temp.append(Node(inner_array, outside_array, h_value))
                    self.terrain.append(temp)
            self.goal_node = self.terrain[endy][endx]
            self.goal_node.change_h_value(0)
            self.start_node = self.terrain[starty][startx] 
            
    def get_adjacency_list(self, current_node: Node):
        possibilities = Grid.get_possible_neighbors(current_node)
        actual_nodes = []
        for (x, y) in possibilities:
            in_sight = lineOfSight(current_node.x_coordinate, current_node.y_coordinate, x, y, self.obstacles)
            if(in_sight):
                actual_nodes.append(self.terrain[y][x])
        return actual_nodes

    
    #grid.py figure out endx and endy to straightline distance function
    
    def is_goal_node(self, node: Node):
        return node.compare_nodes(self.goal_node)

    

    # Heuristic Function
    def straight_line_distance(x1: int, y1: int, x2: int, y2: int) -> float:
        deltaX = x2 - x1
        deltaY = y2 - y1
        diagonal_counter = min(abs(deltaX), abs(deltaY))
        straight_counter = max(abs(deltaX), abs(deltaY)) - diagonal_counter
        total_distance = straight_counter + (math.sqrt(2) * diagonal_counter)
        return total_distance


    def node_in_grid(self, x: int, y: int) -> bool:
            if(x < 0 or x > self.x_size):
                return False
            if(y < 0 or y > self.y_size):
                return False

    #helper function of get_adjacency_list
    def get_possible_neighbors(current_node: Node):
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
    #wrapper function for straight_line_distance()
    def heuristic_generator(self, x, y):
        return Grid.straight_line_distance(
            x, 
            y, 
            self.goal_node.x_coordinate, 
            self.goal_node.y_coordinate
            )

