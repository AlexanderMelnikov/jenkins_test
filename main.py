import argparse
import sys


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('integers', metavar='N', type=int, nargs='+')
    return sum(parser.parse_args(args).integers)

if __name__ == "__main__":
    print(parse_args(sys.argv[1:]))