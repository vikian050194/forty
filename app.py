#!/usr/bin/env python3

from os import environ
from sys import argv
from pathlib import Path

from forty import main
from forty.configuration import Configuration


if __name__ == "__main__":
    home = Path.home().as_posix()
    home = environ.get("FORTY_HOME", home)
    output = environ.get("FORTY_OUTPUT", None)

    configuration = Configuration(home, output)

    options = argv[1:]
    main(options=options, configuration=configuration)
