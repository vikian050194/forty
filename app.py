#!/usr/bin/env python3

from sys import argv
from pathlib import Path

from forty import main


if __name__ == "__main__":
    home = Path.home().as_posix()
    options = argv[1:]
    main(home=home, options=options)
