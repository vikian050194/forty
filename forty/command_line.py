#!/usr/bin/env python3

from sys import argv
from pathlib import Path

import forty


def main():
    home = Path.home().as_posix()
    options = argv[1:]
    forty.main(home=home, options=options)
