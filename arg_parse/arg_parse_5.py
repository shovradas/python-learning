from argparse import ArgumentParser


def area(l, w):
    return l*w

if __name__ == "__main__":
    parser = ArgumentParser(description='Rectangle Calculator')
    parser.add_argument('-l', '--length', type=float, metavar='', required=True, help='Length of a rectangle')
    parser.add_argument('-w', '--width', type=float, metavar='', required=True, help='Width of a rectangle')
    args = parser.parse_args()
    print(args)
    print(area(args.length, args.width))