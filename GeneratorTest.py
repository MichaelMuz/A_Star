from AStar import AStar
from Grid import Grid


def GeneratorTest(filename: str) -> bool:
    return AStar(Grid(filename)).run_algorithm() == "path found"
