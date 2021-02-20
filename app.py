#!/usr/bin/env python3

from sys import argv
from datetime import datetime

from utils import *


def main(args):
    if len(args) == 0:
        args = ['-h']

    [arg] = args
    if arg in ['-h', '--help']:
        print('fourty', 'v0.0.0')
        print('-h, --help\tget full available info')
        print('-i, --init\tinitialization')
        print('-s, --start\tappend "start" action')
        print('-f, --finish\tappend "finish" action')
        return


if __name__ == "__main__":
    # main(argv[1:])
    load_actions()