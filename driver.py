from Grid import Grid
from A_star import A_star
if __name__ == "__main__" :
    grid = Grid("map1.txt")
    a = A_star(grid)
    a.run_algorithm()
    
    



