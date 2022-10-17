import argparse
import random

# Generates maps

def random_end(matrix, numberOfZeroesEnd):
    ## Select a random start
    tmp = numberOfZeroesEnd
    startCord = [len(matrix)-1,-1]
    for i in range(0, len(matrix[0]), 1):

        # end loop if startCoord defined
        if (startCord[1] != -1):
            break

        # take your chances
        value = random.random()
        if (matrix[len(matrix)-1][i] == 0):
            tmp = tmp - 1
            if (value <= 1 - (float(numberOfZeroesEnd / 10**(len(str(numberOfZeroesEnd)))))):
                # print(value, float(numberOfZeroesStart / 10**(len(str(numberOfZeroesStart)))))
                startCord[1] = i

        if (tmp == 0 and matrix[len(matrix)-1][i] == 0):
            # print("forced", value, float(numberOfZeroesStart / 10**(len(str(numberOfZeroesStart)))))
            startCord[1] = i

        # print(matrix[0][i], tmp)

    # print(startCord)
    return startCord

def random_start(matrix, numberOfZeroesStart):
    ## Select a random start
    tmp = numberOfZeroesStart
    startCord = [0,-1]
    for i in range(0, len(matrix[0]), 1):

        # end loop if startCoord defined
        if (startCord[1] != -1):
            break

        # take your chances
        value = random.random()
        if (matrix[0][i] == 0):
            tmp = tmp - 1
            if (value <= 1 - (float(numberOfZeroesStart / 10**(len(str(numberOfZeroesStart)))))):
                # print(value, float(numberOfZeroesStart / 10**(len(str(numberOfZeroesStart)))))
                startCord[1] = i

        if (tmp == 0 and matrix[0][i] == 0):
            # print("forced", value, float(numberOfZeroesStart / 10**(len(str(numberOfZeroesStart)))))
            startCord[1] = i

        # print(matrix[0][i], tmp)

    # print(startCord)
    return startCord

def main(args):
    # print(args.Dimensions)
    # print(args.BlockRate)
    numberOfZeroesStart = 0
    numberOfZeroesEnd = 0

    ## Generate empty matrix
    rows, cols = (5, 5)
    matrix = [[0 for i in range(int(args.Dimensions[1]))] for j in range(int(args.Dimensions[0]))]

    # ## Print empty matrix
    # for i in range(0, len(matrix), 1):
    #     print(matrix[i])

    ## Randomly populate empty matrix
    for i in range(0, len(matrix), 1):
        for j in range(0, len(matrix[i]), 1):
            value = random.random()
            if value < float(args.BlockRate[0]):
                # print("BLOCK:", value)
                matrix[i][j] = 1
            # else:
                # print("EMPTY:", value)
        # print("Next Row.")

    # ## Print populated matrix
    # for i in range(0, len(matrix), 1):
    #     print(matrix[i])

    ## Find number of zeroes for start and goal
    for i in range(0, len(matrix[0]), 1):
        # print(matrix[0][i])
        if (matrix[0][i]) == 0:
            numberOfZeroesStart += 1
        if (matrix[len(matrix)-1][i]) == 0:
            numberOfZeroesEnd += 1

    # print("====", numberOfZeroesStart, len(str(numberOfZeroesStart)), 10**(len(str(numberOfZeroesStart))))
    # print("====", numberOfZeroesEnd, len(str(numberOfZeroesEnd)), 10**(len(str(numberOfZeroesEnd))))

    print(random_start(matrix, numberOfZeroesStart)[0] + 1, random_start(matrix, numberOfZeroesStart)[1])
    print(random_end(matrix, numberOfZeroesEnd)[0], random_end(matrix, numberOfZeroesEnd)[1] + 1)
    print(args.Dimensions[1], args.Dimensions[0])

    # print("START: ", random_start(matrix, numberOfZeroesStart))
    # print("END: ", random_end(matrix, numberOfZeroesEnd))

    ## Print populated matrix
    rez = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    for i in range(len(rez)):
        for j in range(len(rez[i])):
            print(i+1, j+1, rez[i][j])

    # print("CHANCE: ", 1 - (float(numberOfZeroesStart / 10**(len(str(numberOfZeroesStart))))))

    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generates random maps.')
    parser.add_argument('Dimensions', metavar='Dimensions', nargs=2, help='X and Y dimensions')
    parser.add_argument('BlockRate', metavar='BlockRate', nargs=1, help = 'Probability of blockades, as a decimal from 0 to 1.')

    args = parser.parse_args()
    main(args)