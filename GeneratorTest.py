from AStar import AStar
from Grid import Grid
import os
import subprocess


def GeneratorTest(filename: str) -> bool:
    return AStar(Grid(filename)).run_algorithm() == "path found"

def main():
    hit_fifty = False
    ctr = 0
    while (not hit_fifty):
        if (ctr == 50):
            break;
        generateCMD = "python MapGenerator.py 50 100 .30 > test.txt"
        os.system(generateCMD)
        if (GeneratorTest("test.txt") is True):
            ctr = ctr + 1
            print(ctr, "WE MADE IT!")
            string = "test" + str(ctr) + ".txt"
            command = "cp test.txt tests/" + string
            os.system(command)
        else:
            print("RIP")
    os.system("rm test.txt")

if __name__ == "__main__":
    main()