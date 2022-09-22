from Grid import Grid

grid = Grid(5, 3)
for x in grid.terrain:
    for y in x:

        print(y.get_f_value(), end =" ")
    print("")



