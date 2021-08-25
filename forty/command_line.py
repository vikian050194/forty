#!/usr/bin/env python3

from os import environ
from sys import argv
from pathlib import Path

import forty
from forty.configuration import Configuration


def main():
    home = Path.home().as_posix()
    home = environ.get("FORTY_HOME", home)
    output = environ.get("FORTY_OUTPUT", None)

    configuration = Configuration(home, output)
    options = argv[1:]

    forty.main(options=options, configuration=configuration)
