import argparse
import random

# Generates maps

def main(args):
    print(args.Dimensions)
    print(args.BlockRate)

    rows, cols = (5, 5)
    matrix = [[0 for i in range(int(args.Dimensions[1]) + 1)] for j in range(int(args.Dimensions[0]) + 1)]

    for i in range(0, len(matrix), 1):
        print(matrix[i])

    for i in range(0, len(matrix), 1):
        for j in range(0, len(matrix[i]), 1):
            value = random.random()
            if value < float(args.BlockRate[0]):
                print("ITS A BLOCK:", value)
                matrix[i][j] = 1
            else:
                print("NOT A BLOCK:", value)
        print("NEW THING")

    for i in range(0, len(matrix), 1):
        print(matrix[i])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generates random maps.')
    parser.add_argument('Dimensions', metavar='Dimensions', nargs=2, help='X and Y dimensions')
    parser.add_argument('BlockRate', metavar='BlockRate', nargs=1, help = 'Probability of blockades, as a decimal from 0 to 1.')

    args = parser.parse_args()
    main(args)