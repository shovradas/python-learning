from argparse import ArgumentParser


def area(l, w):
    return l*w

if __name__ == "__main__":
    parser = ArgumentParser(description='Rectangle Calculator')
    parser.add_argument('-l', '--length', type=float, help='Length of a rectangle')
    parser.add_argument('-w', '--width', type=float, help='Width of a rectangle')
    args = parser.parse_args()
    print(args)
    print(area(args.length, args.width))