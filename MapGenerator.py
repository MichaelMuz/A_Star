import argparse

# Generates maps

def main(args):
    print(args.Dimensions)
    print(args.BlockRate)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generates random maps.')
    parser.add_argument('Dimensions', metavar='sus', nargs=2, help='X and Y dimensions')
    parser.add_argument('BlockRate', metavar='sus', nargs=1, help = 'Rate of random obstacles')

    args = parser.parse_args()
    main(args)