from argparse import ArgumentParser


def area(l, w):
    return l*w

if __name__ == "__main__":
    parser = ArgumentParser(description='Rectangle Calculator')
    parser.add_argument('-l', '--length', type=float, metavar='', required=True, help='Length of a rectangle')
    parser.add_argument('-w', '--width', type=float, metavar='', required=True, help='Width of a rectangle')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-s', '--silent', action='store_true', help='Print result only')
    group.add_argument('-v', '--verbose', action='store_true', help='Print formatted result')

    args = parser.parse_args()

    result = area(args.length, args.width)
    if args.verbose:
        print(f' Rectangle Calculator '.center(30, '='))
        print(f'Length: {args.length}, Width: {args.width}')
        print(f'Area: {result}')
        print('='*30)
    else:
        print(result)